# Title: Cateogry Slug tag
# Author: Martin Thoma, http://martin-thoma.com

module CategorySlugFilter
    def readingtime(input)
        @loweredInput = input.downcase
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

Liquid::Template.register_filter(CategorySlugFilter)
