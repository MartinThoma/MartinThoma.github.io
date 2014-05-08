# Title: Directory Listing Plugin for Jekyll
# Author: Simon Heimlicher http://simon.heimlicher.com
# Description: Display list of pages and directories beneath current directory
# Configuration: You can set default title in _config.yml as follows:
#    directory_listing_title: "Contents: "
#    directory_listing_prefix: "Contents of "
#
# Syntax {% directory_listing Title of Listing %}
#
# Example 1:
# {% directory_listing Further reading: %}
#
# Source: http://simon.heimlicher.com/articles/2012/02/01/jekyll-directory-listing

require 'pathname'

module Jekyll
  class Page
    def source_path
      # File.join(@dir, @name).gsub(/^\/*/,'')
      File.join(@dir, @name).sub(%r{^/*},'')
    end
    def parent
      @dir.sub(%r{^/*},'')
    end
  end
  class IncludeListingTag < Liquid::Tag
    include TemplateWrapper
    def initialize(tag_name, markup, tokens)
      @title = nil
      @file = nil
      if markup.strip =~ /\s*lang:(\w+)/i
        @filetype = $1
        markup = markup.strip.sub(/lang:\w+/i,'')
      end
      if markup.strip =~ /(.*)?(\s+|^)(\/*\S+)/i
        @title = $1 || nil
        @file = $3
      end
      super
    end

    def add_item(page)
      if page.index?
        title = page.parent
      else
        title = page.basename
      end
      # Try to read title from source file
      source_file = File.join(@source,page.source_path)
      if File.exists?(source_file)
        content = File.read(source_file)

        if content =~ /^(---\s*\n.*?\n?)^(---\s*$\n?)/m
          content = $POSTMATCH
          begin
            data = YAML.load($1)
          rescue => e
            puts "YAML Exception reading #{name}: #{e.message}"
          end
        end

        if data['title']
          title = data['title']
        end
      else
        puts "File not found: #{source_file}"
      end
      s = "<li><a href=\"/#{page.parent}#{page.url}\">#{title}</a></li>"
    end

    def render(context)
      site = context.registers[:site]
      @source = site.source
      site_pages = context.environments.first['site']['pages']
      @page = context.environments.first['page']
      @title = @page["title"]
      @url = @page["url"]
      @dir = @url.sub(%r{\A/?(.+?)/[^/]*\z},'\1')
      @title ||= (context.registers[:site].config['directory_listing_title'] ||
      context.registers[:site].config['directory_listing_prefix']+@dir || @dir)
      html = '<ul>'
      folders = []
      pages = []
      site_pages.each do |page|
        next unless page.parent && page.parent.match(%r{^#{@dir}(/[A-Za-z][^/]+)?$})
        if page.index?
          relative_dir = page.parent.match(%r{^#{@dir}/([A-Za-z][^/]+)$})
          if relative_dir && relative_dir[1]
            html += self.add_item(page)
          end
        elsif page.parent == @dir
          html += self.add_item(page)
        end
      end
      html += '</ul>'

      safe_wrap(html)
    end
  end
end

Liquid::Template.register_tag('directory_listing', Jekyll::IncludeListingTag)