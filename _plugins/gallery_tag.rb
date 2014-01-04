module Jekyll
  class GalleryTag < Liquid::Block
    def initialize(tag_name, markup, tokens)
      super
      @markup = markup
      @tokens = tokens
    end

    def render(context)
        lines = @markup.split("\n")
        lines.strip!
        rendered = '<ul class="gallery mw-gallery-traditional">'
        lines.each do |line|
            if line.nil?
                puts "Line was nil!"
            else
                words = line.split(" ")
                words.strip!
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
        rendered += "</div>"
        return rendered
    end
  end
end

Liquid::Template.register_tag('gallery', Jekyll::GalleryTag)
