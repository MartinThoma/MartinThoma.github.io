# A Liquid tag for Jekyll sites that allows easy creation of 
# wikpedia-style image galleries.
#
# Author: Martin Thoma (info@martin-thoma.de)
# Source: https://github.com/MartinThoma/jekyll-gallery-tag
# Version: 1.0
#
# Example usage:
#   {% gallery columns="2" %}
#       ../images/2013/10/bash-vs-zsh-cd.png    "Bash vs zsh: cd command completion"
#       ../images/2013/10/bash-vs-zsh-git.png   "Bash vs zsh: Git prompt indicator"
#       ../images/2013/10/bash-vs-zsh-spelling-correction.png   "Bash vs zsh: Spelling correction"
#       ../images/2013/10/bash-vs-zsh-time.png  "Bash vs zsh: time command"
#   {% endgallery %}
#
# Plugin replaces the template above with:
#   <ul class="gallery mw-gallery-traditional">
#     <li class="gallerybox" style="width: 155px">
#       <div style="width: 155px">
#         <div class="thumb" style="width: 150px;">
#           <div style="margin:21px auto;">
#             <a href="../images/2013/10/bash-vs-zsh-cd.png" class="image">
#               <img src="../images/2013/10/bash-vs-zsh-cd.png" alt="" bash="" width="120" height="108">
#             </a>
#           </div>
#         </div>
#         <div class="gallerytext">"Bash</div>
#       </div>
#     </li>
#     ...
#   </ul>

require 'csv'
require 'dimensions'
require 'RMagick'
require 'fileutils'

module Jekyll
  class GalleryTag < Liquid::Block
    def initialize(tag_name, markup, tokens)
        super
        @markup = markup
        @tokens = tokens
    end

    def parseAttributes()
        @markup
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
        galleryAttributes = parse_attrs(@markup)
        if galleryAttributes.has_key?("columns")
            width = (163*(galleryAttributes["columns"].to_i)).to_s
            rendered = '<ul class="gallery mw-gallery-traditional" style="max-width: '+width+'px; width: '+width+'px;">'
        else
            rendered = '<ul class="gallery mw-gallery-traditional">'
        end

        @nodelist.each do |node|
            lines = node.split("\n")
            lines.each do |line|
                if line.nil?
                    puts "Line was nil!"
                else
                    options = { col_sep: ' ', row_sep: '\n', quote_char: '"' }
                    csv = CSV.new line, options
                    csv.each_with_object({}) do |words, attrs|
                        @hash = {}
                        if words.count() >= 1
                            words.push("") # make sure this one has at least two elements
                            src, gallerytext, *rest = words
                            if rest.count() == 0
                                alt = gallerytext
                            else
                                alt = rest[0]
                            end

                            @hash['url'] = src
                            @hash['width'] = "120"
                            @hash['height'] = "120"
                            @hash['orig-url'] = @hash['url']

                            @divWidth = (@hash['width'].to_i+10).to_s

                            img_path = get_image_path(context.registers[:site].config['source'], context.registers[:page]["path"], src)

                            # TODO: check if img_path actually contains an image
                            if File.exist?(img_path)
                                width, height = Dimensions.dimensions(img_path)

                                if width > @hash['width'].to_i
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
                                puts "[Warning] " + img_path + " does not exist."
                            end

                            rendered += '<li class="gallerybox" style="width: 155px">'
                            rendered += '<div style="width: 155px">'
                            rendered += '<div class="thumb" style="width: 150px;">'
                            rendered += '<div style="margin:21px auto;height: 113px;line-height: 150px;">'
                            rendered += "<a href=\"#{@hash['orig-url']}\" class=\"image\">"
                            rendered += '<img src="'+@hash['url']+'" alt="'+alt+'" style="max-width: 120px; max-height: 120px;"/>'
                            rendered += '</a>'
                            rendered += '</div>'
                            rendered += '</div>'
                            rendered += '<div class="gallerytext">'+gallerytext+'</div>'
                            rendered += '</div>'
                            rendered += '</li>'
                        end
                    end
                end
            end
        end
        rendered += "</ul>"
        return rendered
    end
  end
end

Liquid::Template.register_tag('gallery', Jekyll::GalleryTag)
