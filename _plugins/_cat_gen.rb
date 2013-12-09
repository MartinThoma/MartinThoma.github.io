module Jekyll
  class CategoryPage < Page
    def initialize(site, base, dir, category)
      @site = site
      @base = base
      @dir = dir
      @name = 'index.html'
      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'category_index.html')
      self.data['category'] = category
      category_title_prefix = site.config['category_title_prefix'] || 'Category: '
      category_title_suffix = site.config['category_title_suffix'] || '&rdquo;'
      self.data['title'] = "#{category_title_prefix}#{category}#{category_title_suffix}"
    end
  end
  class CategoryPageGenerator < Generator
    safe true
    def generate(site)
      if site.layouts.key? 'category_index'
        dir = site.config['category_dir'] || 'category'
        site.categories.keys.each do |category|
            if category.downcase == "the web"
                site.pages << CategoryPage.new(site, site.source, File.join(dir, "web"), category)
            elsif category.downcase == "cyberculture"
                site.pages << CategoryPage.new(site, site.source, File.join(dir, "cyberculture"), category)
            elsif category.downcase == "code"
                site.pages << CategoryPage.new(site, site.source, File.join(dir, "code"), category)
            elsif category.downcase == "german posts"
                site.pages << CategoryPage.new(site, site.source, File.join(dir, "deutschland"), category)
            elsif category.downcase == "my bits and bytes"
                site.pages << CategoryPage.new(site, site.source, File.join(dir, "bits-and-bytes"), category)
            else
                site.pages << CategoryPage.new(site, site.source, File.join(dir, category), category)
            end
        end
      end
    end
  end

end
