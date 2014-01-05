# A Liquid tag for Jekyll sites that allows easy creation of image
# galleries
#
# Author: Martin Thoma (info@martin-thoma.de)
# Source: https://github.com/MartinThoma/MartinThoma.github.io/blob/source/_plugins/gallery_tag.rb
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

    def render(context)
        galleryAttributes = parse_attrs(@markup)
        if galleryAttributes.has_key?("columns")
            width = (163*(galleryAttributes["columns"].to_i)).to_s
            rendered = '<ul class="gallery mw-gallery-traditional" style="max-width: '+width+'px;">'
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
                        if words.count() >= 1
                            words.push("") # make sure this one has at least two elements
                            src, alt, *rest = words
                            rendered += '<li class="gallerybox" style="width: 155px">'
                            rendered += '<div style="width: 155px">'
                            rendered += '<div class="thumb" style="width: 150px;">'
                            rendered += '<div style="margin:21px auto;">'
                            rendered += '<a href="'+src+'" class="image">'
                            rendered += '<img src="'+src+'" alt="'+alt+'" width="120" height="108"/>'
                            rendered += '</a>'
                            rendered += '</div>'
                            rendered += '</div>'
                            rendered += '<div class="gallerytext">'+alt+'</div>'
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
