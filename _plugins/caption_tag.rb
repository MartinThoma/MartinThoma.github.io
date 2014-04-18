# A Liquid tag for Jekyll sites that allows easy creation of captioned
# images like they are in WordPress.
#
# Author: Martin Thoma (info@martin-thoma.de)
# Source: https://github.com/MartinThoma/jekyll-caption-tag
# Version: 1.8
#
# Example usage:
#   {% caption align="aligncenter" width="500" alt="WER calculation" caption="WER calculation" url="../images/2014/03/lolcat.jpg" %}
#
# Plugin replaces the template above with:
#    <div style="width: 510px" class="wp-caption aligncenter">
#        <a href="../images/2013/11/WER-calculation.png">
#            <img src="../images/2014/03/lolcat.jpg" alt="WER calculation" 
#                 width="500" height="494" class="size-full">
#        </a>
#        <p class="wp-caption-text">WER calculation</p>
#    </div>

require 'csv'
require 'dimensions'
require 'RMagick'
require 'fileutils'
require 'yaml'
require 'logger'

$logger = Logger.new(STDOUT)
$logger.level = Logger::WARN ## Other loggin levels are: DEBUG, INFO, ERROR

module Jekyll
  class CaptionTag < Liquid::Tag

    def initialize(tag_name, text, tokens)
      super
      @text = text
      @tokens = tokens
      @serialized_filename = "caption_tag_serialized.yaml"
      @written_files = load_serialized_data(@serialized_filename)
    end

    # Load a serialized file so that images don't get scaled multiple times
    # 
    # * *Args*    :
    # +filename+:: Name of the serialized file
    def load_serialized_data(filename)
        if File.exist?(filename)
          contents = File.read(filename)
          written_files = YAML::load(contents)
        else
          written_files = {}
        end

        return written_files
    end


    def dump_serialized_data(serialization_filename, written_files,
                             original_image_path, orig_width, orig_height,
                             scaled_width, scaled_height)
        if written_files.has_key?(original_image_path)
            if !written_files[original_image_path]["scaled"].
                                                        has_key?(scaled_width)
                # The scaled image is not in the written_files set. Insert it.
                written_files[original_image_path]["scaled"][scaled_width] =
                                        scaled_height
            end
        else
            written_files[original_image_path] = {"orig_width" => orig_width,
                                         "orig_height" => orig_height,
                                         "scaled" => 
                                             {scaled_width => scaled_height }
                                        }
        end

        serialized = YAML::dump(written_files)
        File.open(serialization_filename, 'w') { |file| file.write(serialized) }
    end

    # Check if 'original_image_path' was already scaled before.
    # 
    # * *Args*    :
    # +written_files+:: datastructure that contains all scaled files
    # +original_image_path+:: pre-captioning image
    # +scaled_width+:: width of the scaled caption
    # 
    # * *Returns*    : Boolean
    def was_already_scaled(written_files, original_image_path, scaled_width)
        if written_files.has_key?(original_image_path)
            # TODO: Sure that you only have to check width?
            #       Or maybe also height?
            return written_files[original_image_path]["scaled"].
                                                        has_key?(scaled_width)
        end

        return false
    end


    # Parse what's within {% caption XYZ %}.
    # 
    # * *Args*    :
    # +input+:: The caption tag, e.g. 
    #          'align="aligncenter" width="500" 
    #           alt="xyz" text="abc" 
    #           url="../images/2014/03/lolcat.jpg"'
    # * *Returns*    :
    # {"align"=>"aligncenter", "width"=>"500", "alt"=>"xyz", "text"=>"abc", 
    #  "url"=>"../images/2014/03/lolcat.jpg"}
    def parse_attrs(input)
      options = { col_sep: '=', row_sep: ' ', quote_char: '"' }
      csv = CSV.new input, options

      csv.each_with_object({}) do |row, attrs|
        attr, value = row
        value ||= true
        attrs[attr] = value
      end
    end

    # Returns the absolute image path.
    #
    # * *Args*    :
    #   - +site_source+:: e.g. '/home/moose/Downloads/MartinThoma.github.io'
    #   - +page_path+:: e.g. '_posts/2014-04-02-tcl.md'
    #   - +img_src+:: The source that was within the 'url' attribute of the 
    #                 caption tag. e.g. '../images/2014/03/lolcat.jpg'
    # * *Returns*    :
    #   - e.g. '/home/moose/Downloads/MartinThoma.github.io/images/2014/03/lolcat.jpg'
    def get_image_path(site_source, page_path, img_src)
        if img_src.include?('://')
            # TODO:download to local storage
            new_path = img_src
        else
            current_post_path = File.join(site_source, page_path)
            current_post_folder_path = File.dirname(current_post_path)
            new_path = File.expand_path(File.join(current_post_folder_path,
                                                  img_src))

            if !File.exist?(new_path)
                # Use site_soure as root, not current_post_folder_path
                new_path = File.expand_path(File.join(site_source, img_src))
            end
        end
        return new_path
    end


    # Returns the url of the image where it will be online.
    #
    # * *Args*    :
    #   - +baseurl+:: e.g. 'http://localhost/blog' or 'http://martin-thoma.com'
    #   - +new_filename+:: e.g.
    #         '/home/moose/Downloads/MartinThoma.github.io/captions/lolcat.jpg'
    # * *Returns*    :
    #   - e.g.  http://localhost/blog/captions/lolcat.jpg
    def get_online_url(baseurl, new_filename)
        File.join(baseurl, @caption_folder, File.basename(new_filename))
    end


    # Get the path where the image will be before the actual site gets 
    # generated.
    # 
    # * *Args*    :
    #   - +site_source+:: e.g. '/home/moose/Downloads/MartinThoma.github.io'
    #   - +post_path+:: e.g. '_posts/2014-04-02-tcl.md'
    #   - +img_src+:: e.g. '../images/2014/03/lolcat.jpg'
    # * *Returns*    :
    #   - e.g.  /home/moose/Downloads/MartinThoma.github.io/captions/lolcat.jpg
    def get_destination_path(site_source, post_path, img_src)
        destination_path = File.join(site_source, @caption_folder)
        ext  = File.extname(img_src)
        base = File.basename(img_src, ext)
        destination_img_path = File.join(destination_path, base + ext)
        new_filename = File.expand_path(destination_img_path)

        if File.exists?(new_filename)
            i = 1
            begin
                i += 1
                destination_img_path = File.join(destination_path,
                                                 base + "-" + i.to_s + ext)
                new_filename = File.expand_path(destination_img_path)
            end while File.exists?(new_filename)
        end
        
        return new_filename
    end


    # Replace caption tag with HTML. This is the main part of this plugin.
    def render(context)
        @max_width = context.registers[:site].config['caption_max_width'] || "512"
        @max_height = context.registers[:site].config['caption_max_height'] || "800"
        @caption_folder = context.registers[:site].config['caption_folder'] || "/captions"

        @attributes = parse_attrs(@text)

        if !@attributes.has_key?('url')
            $logger.error("Image in post '" +
                          context.registers[:page]["path"] +
                          "' has no 'url' attribute.")
            exit
        end

        if @attributes.has_key?('text') && @attributes.has_key?('caption')
            $logger.warn("[" + context.environments.first["page"]["url"] +"] " +
                "One caption Liquid tag has both, 'text' and 'caption' " +
                "attribute. 'text' is deprecated.")
        end

        if @attributes.has_key?('title') && @attributes.has_key?('caption')
            $logger.warn("["+context.environments.first["page"]["url"] +"] " +
                "One caption Liquid tag has both, 'title' and 'caption' " +
                "attribute. 'title' is deprecated.")
        end

        if @attributes.has_key?('text') && !@attributes.has_key?('caption')
            @attributes['caption'] = @attributes['text']
        end

        if @attributes.has_key?('title') && !@attributes.has_key?('caption')
            @attributes['caption'] = @attributes['title']
        end

        original_url = @attributes['url']

        @divWidth = (@attributes['width'].to_i+10).to_s

        original_image_path = get_image_path(context.registers[:site].config['source'],
                                  context.registers[:page]["path"],
                                  @attributes['url'])
        $logger.debug("Process '" + original_image_path + "'")
        # TODO: check if original_image_path actually contains an image
        if File.exist?(original_image_path)
            orig_width, orig_height = Dimensions.dimensions(original_image_path)

            if orig_width.nil?
                $logger.error("Image '" + original_image_path + "' is defect.")
                exit
            end

            # Set height of caption image if not done already
            @attributes['height'] = @attributes['height'] || @max_height

            # Set width of caption image if not done already
            @attributes['width'] = @attributes['width'] || @max_height

            if orig_width > @attributes['width'].to_i
                new_filename = get_destination_path(
                                     context.registers[:site].config['source'],
                                     context.registers[:page]["path"],
                                     @attributes['url'])

                # Create folder if not exists
                dirname = File.dirname(new_filename)
                unless File.directory?(dirname)
                    FileUtils.mkdir_p(dirname)
                end

                if was_already_scaled(@written_files, original_image_path, @attributes['width'])
                    $logger.debug("Image was already scaled")
                    @attributes['caption_width'] = @attributes['width']
                    @attributes['caption_height'] = @written_files[original_image_path]["scaled"][@attributes['caption_width']]
                else
                    $logger.debug("Image needs to get scaled scaled")
                    image = Magick::Image.read(original_image_path).first
                    image.change_geometry!(@attributes['width']+"x"+
                        @attributes['height']) { |cols, rows, img|
                        newimg = img.resize(cols, rows)
                        newimg.write(new_filename)
                    }
                    @attributes['caption_width'], @attributes['caption_height'] = Dimensions.dimensions(new_filename)
                    dump_serialized_data(@serialized_filename, @written_files,
                     original_image_path, orig_width.to_s, orig_height.to_s,
                     @attributes['caption_width'], @attributes['caption_height'])
                end

                @attributes['caption_width']  = @attributes['caption_width'].to_s
                @attributes['caption_height'] = @attributes['caption_height'].to_s

                @attributes['caption_url'] = get_online_url(
                                context.registers[:site].config['baseurl'],
                                new_filename)
            elsif orig_width < @attributes['width'].to_i
                $logger.warn("The original has width of " + orig_width.to_s +
                             ". The caption width is " + @attributes['width'] +
                             "(in "+ context.environments.first["page"]["url"] +
                             " for "+original_image_path+")")
                @attributes['width'] = orig_width.to_s
                @attributes['caption_url'] = @attributes['url']
            else
                $logger.info("Scaled width = original width. Nothing to do.")
                @attributes['caption_url'] = @attributes['url']
            end
        else
            $logger.warn(original_image_path + " does not exist (in " +
                        context.registers[:page]["path"] + ")")
        end

        "<div style=\"width: #{@divWidth}px\" " +
             "class=\"wp-caption #{@attributes['align']}\">" +
        "<a href=\"#{original_url}\">" +
            "<img src=\"#{@attributes['caption_url']}\" " +
                 "alt=\"#{@attributes['alt']}\" width=\"#{@attributes['caption_width']}\" " +
                 "height=\"#{@attributes['caption_height']}\" " +
                 "class=\"#{@attributes['class']}\"/>" +
        "</a>" +
        "<p class=\"wp-caption-text\">#{@attributes['caption']}</p>" +
        "</div>"
    end
  end
end

Liquid::Template.register_tag('caption', Jekyll::CaptionTag)
