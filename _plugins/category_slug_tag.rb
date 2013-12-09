# Title: Cateogry Slug tag
# Author: Martin Thoma, http://martin-thoma.com
#
# Searches for:
#   {% caption align="aligncenter" width="500" alt="WER calculation" text="WER calculation" url="../images/2013/11/WER-calculation.png" %}
# and replaces it with:
#    <div style="width: 510px" class="wp-caption aligncenter">
#        <a href="../images/2013/11/WER-calculation.png">
#            <img src="../images/2013/11/WER-calculation.png" alt="WER calculation" width="500" height="494" class="size-full">
#        </a>
#        <p class="wp-caption-text">WER calculation</p>
#    </div>

module Jekyll
  class CategorySlugTag < Liquid::Tag

    def initialize(tag_name, text, tokens)
      super
      @text = text
      @tokens = tokens
    end

    def render(context)
        @loweredInput = @text.downcase
        if @loweredInput == "code"
            return "code"
        elsif @loweredInput == "the web"
            return "web"
        elsif @loweredInput == "mathematics"
            return "math"
        elsif @loweredInput == "my bits and bytes"
            return "bits-and-bytes"
        elsif @loweredInput == "german posts"
            return "deutschland"
        elsif @loweredInput == "cyberculture"
            return "cyberculture"
        else
            return @loweredInput
        end
    end
  end
end

Liquid::Template.register_tag('categoryslug', Jekyll::CategorySlugTag)
