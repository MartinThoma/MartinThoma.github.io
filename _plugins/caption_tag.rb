# A Liquid tag for Jekyll sites that allows easy creation of captioned
# images like they are in WordPress.
#
# Author: Martin Thoma (info@martin-thoma.de)
# Source: https://github.com/MartinThoma/jekyll-caption-tag
# Version: 1.2
#
# Example usage:
#   {% caption align="aligncenter" width="500" alt="WER calculation" text="WER calculation" url="/images/2013/11/WER-calculation.png" %}
#
# Plugin replaces the template above with:
#    <div style="width: 510px" class="wp-caption aligncenter">
#        <a href="/images/2013/11/WER-calculation.png">
#            <img src="/images/2013/11/WER-calculation.png" alt="WER calculation" width="500" height="494" class="size-full">
#        </a>
#        <p class="wp-caption-text">WER calculation</p>
#    </div>

require 'csv'
require 'dimensions'

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
        puts Dimensions.dimensions(@hash['url'])

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
