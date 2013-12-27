# Title: Caption tag
# Author: Martin Thoma, http://martin-thoma.com
#
# Searches for:
#   {% caption align="aligncenter" width="500" alt="WER calculation" text="WER calculation" url="/images/2013/11/WER-calculation.png" %}
# and replaces it with:
#    <div style="width: 510px" class="wp-caption aligncenter">
#        <a href="/images/2013/11/WER-calculation.png">
#            <img src="/images/2013/11/WER-calculation.png" alt="WER calculation" width="500" height="494" class="size-full">
#        </a>
#        <p class="wp-caption-text">WER calculation</p>
#    </div>

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
        "<div style=\"width: #{@hash['width']}px\" class=\"wp-caption #{@hash['align']}\">" +
        "<a href=\"" + context.registers[:site].config['baseurl'] + "/images/#{@hash['url']}\">" +
            "<img src=\"" + context.registers[:site].config['baseurl'] + "/images/#{@hash['url']}\" alt=\"#{@hash['text']}\" width=\"#{@hash['width']}\" height=\"#{@hash['height']}\" class=\"#{@hash['class']}\">" +
        "</a>" +
        "<p class=\"wp-caption-text\">#{@hash['text']}</p>" +
        "</div>"
    end
  end
end

Liquid::Template.register_tag('caption', Jekyll::CaptionTag)
