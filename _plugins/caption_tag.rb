    # A Liquid tag for Jekyll sites that allows easy creation of captioned
    # images like they are in WordPress.
    #
    # Author: Martin Thoma (info@martin-thoma.de)
    # Source: https://github.com/MartinThoma/jekyll-caption-tag
    # Version: 1.2
    #
    # Example usage:
    #   {% caption align="aligncenter" width="500" alt="WER calculation" text="WER calculation" url="../images/2013/11/WER-calculation.png" %}
    #
    # Plugin replaces the template above with:
    #    <div style="width: 510px" class="wp-caption aligncenter">
    #        <a href="../images/2013/11/WER-calculation.png">
    #            <img src="../images/2013/11/WER-calculation.png" alt="WER calculation" width="500" height="494" class="size-full">
    #        </a>
    #        <p class="wp-caption-text">WER calculation</p>
    #    </div>

    require 'csv'
    require 'dimensions'
    require 'RMagick'
    require 'fileutils'

    module Jekyll
      class CaptionTag < Liquid::Tag

        def initialize(tag_name, text, tokens)
          super
          @text = text
          @tokens = tokens
        end

        def parse_attrs(input)
          options = { col_sep: '=', row_sep: ' ', quote_char: '"' }
          csv = CSV.new input, options

          csv.each_with_object({}) do |row, attrs|
            attr, value = row
            value ||= true
            attrs[attr] = value
          end
        end

        def render(context)
            @hash = parse_attrs(@text)

            if @hash.has_key?('text') && @hash.has_key?('caption')
                puts "[Warning]["+context.environments.first["page"]["url"]+"] One caption Liquid tag has both, 'text' and 'caption' attribute. Using 'caption' is better."
            end

            if @hash.has_key?('title') && @hash.has_key?('caption')
                puts "[Warning]["+context.environments.first["page"]["url"]+"] One caption Liquid tag has both, 'title' and 'caption' attribute. Using 'caption' is better."
            end

            if @hash.has_key?('text') && !@hash.has_key?('caption')
                @hash['caption'] = @hash['text']
            end

            if @hash.has_key?('title') && !@hash.has_key?('caption')
                @hash['caption'] = @hash['title']
            end

            @divWidth = (@hash['width'].to_i+10).to_s

            if false
                current_post_path = File.join(context.registers[:site].config['source'], context.registers[:page]["path"])
                current_post_folder_path = File.dirname(current_post_path)
                img_path = File.join(current_post_folder_path, @hash['url'])
                # TODO: check if img_path actually contains an image
                width, height = Dimensions.dimensions(img_path)
                if width > @hash['width'].to_i
                    @hash['height'] = "800"
                    puts "[Info] Image was bigger than it should be. Start resizing."
                    puts "[Info] Image path:"+img_path.inspect
                    puts "[Info] Image width:"+width.to_s()
                    puts "[Info] Image height:"+height.to_s()
                    puts post.name

                    # TODO: Filename should have image size encoded ... eventually some users migh have different sizes of one image
                    destination_path = File.join(context.registers[:site].config['destination'], context.registers[:page]["path"])
                    destination_img_path = File.join(destination_path, @hash['url'])
                    destination_img_path_folder = File.dirname(destination_img_path)
                    new_filename = File.join(destination_img_path_folder, "captions/" + File.basename(img_path))
                    puts "[Info] new_filename" + new_filename.inspect

                    # Create folder if not exists
                    dirname = File.dirname(new_filename)
                    unless File.directory?(dirname)
                      FileUtils.mkdir_p(dirname)
                    end

                    image = Magick::Image.read(img_path).first
                    image.change_geometry!(@hash['width']+"x"+@hash['height']) { |cols, rows, img|
                        newimg = img.resize(cols, rows)
                        newimg.write(new_filename)
                    }
                end
            end

            "<div style=\"width: #{@divWidth}px\" class=\"wp-caption #{@hash['align']}\">" +
            "<a href=\"#{@hash['url']}\">" +
                "<img src=\"#{@hash['url']}\" alt=\"#{@hash['text']}\" width=\"#{@hash['width']}\" height=\"#{@hash['height']}\" class=\"#{@hash['class']}\"/>" +
            "</a>" +
            "<p class=\"wp-caption-text\">#{@hash['caption']}</p>" +
            "</div>"
        end
      end
    end

    Liquid::Template.register_tag('caption', Jekyll::CaptionTag)
