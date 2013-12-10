# Title: Cateogry Slug tag
# Author: Martin Thoma, http://martin-thoma.com

module Jekyll
  module CategorySlugFilter
    def CategorySlugFilter(input)
        @loweredInput = input.downcase
        if @loweredInput == "code"
            return "code"
        elsif @loweredInput == "the web"
            return "web"
        elsif @loweredInput == "mathematics"
            return "maths"
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

Liquid::Template.register_filter(Jekyll::CategorySlugFilter)
