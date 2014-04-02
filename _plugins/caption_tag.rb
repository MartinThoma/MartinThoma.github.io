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

    def get_image_path(site_source, page_path, img_src)
        if img_src.include?('://')
            # TODO:download to local storage
            new_path = img_src
        else
            current_post_path = File.join(site_source, page_path)
            current_post_folder_path = File.dirname(current_post_path)
            new_path = File.expand_path(File.join(current_post_folder_path, img_src))
        end
        return new_path
    end

    def get_online_url(site_source, baseurl, new_filename)
        dest = File.join(baseurl, new_filename[site_source.length..-1])
        return dest
    end

    def get_destination_path(site_source, post_path, img_src)
        destination_path = File.join(site_source, "/captions")
        ext  = File.extname(img_src)
        base = File.basename(img_src, ext)
        destination_img_path = File.join(destination_path, base + ext)
        new_filename = File.expand_path(destination_img_path)

        if File.exists?(new_filename)
            i = 1
            begin
                i += 1
                destination_img_path = File.join(destination_path, base + "-" + i.to_s + ext)
                new_filename = File.expand_path(destination_img_path)
            end while File.exists?(new_filename)
        end
        
        return new_filename
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

        @hash['orig-url'] = @hash['url']

        @divWidth = (@hash['width'].to_i+10).to_s

        img_path = get_image_path(context.registers[:site].config['source'], context.registers[:page]["path"], @hash['url'])
        # TODO: check if img_path actually contains an image
        if File.exist?(img_path)
            width, height = Dimensions.dimensions(img_path)

            if width > @hash['width'].to_i
                @hash['height'] = "800"
                new_filename = get_destination_path(context.registers[:site].config['source'], context.registers[:page]["path"], @hash['url'])

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
                width, height = Dimensions.dimensions(new_filename)
                @hash['width']  = width.to_s()
                @hash['height'] = height.to_s()
                @hash['url'] = get_online_url(context.registers[:site].config['source'],context.registers[:site].config['baseurl'], new_filename)
            elsif width < @hash['width'].to_i
                @hash['width'] = width.to_s
            end
        else
            puts "[Warning] " + img_path + " does not exist (in " + context.registers[:page]["path"] + ")"
        end

        "<div style=\"width: #{@divWidth}px\" class=\"wp-caption #{@hash['align']}\">" +
        "<a href=\"#{@hash['orig-url']}\">" +
            "<img src=\"#{@hash['url']}\" alt=\"#{@hash['text']}\" width=\"#{@hash['width']}\" height=\"#{@hash['height']}\" class=\"#{@hash['class']}\"/>" +
        "</a>" +
        "<p class=\"wp-caption-text\">#{@hash['caption']}</p>" +
        "</div>"
    end
  end
end

Liquid::Template.register_tag('caption', Jekyll::CaptionTag)
