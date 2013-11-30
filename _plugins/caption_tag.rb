# Title: Caption tag
# Author: Martin Thoma, http://martin-thoma.com

require 'csv' 

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
        #"#{@text} #{@tokens}"
        "<div style=\"width: #{@hash['width']}px\" class=\"wp-caption #{@hash['alignment']}\">" +
        "<a href=\"../images/#{@hash['url']}\">" +
            "<img src=\"../images/#{@hash['url']}\" alt=\"#{@hash['text']}\" width=\"#{@hash['width']}\" height=\"#{@hash['height']}\" class=\"#{@hash['class']}\">" +
        "</a>" +
        "<p class=\"wp-caption-text\">#{@hash['text']}</p>" +
        "</div>"
    end
  end
end

Liquid::Template.register_tag('caption', Jekyll::CaptionTag)
