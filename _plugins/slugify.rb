# Title: Cateogry Slug tag
# Author: Martin Thoma, http://martin-thoma.com

module Jekyll
  module SlugifyFilter
    def slugify(input)
        @loweredInput = input.downcase.gsub('/[ ]/', ' ' => '-')
        return @loweredInput
    end
  end
end

Liquid::Template.register_filter(Jekyll::SlugifyFilter)
