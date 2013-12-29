#!/usr/bin/env ruby
# encoding: utf-8
#
# Jekyll SQLite database generator
require 'nokogiri'
require 'sequel'

module Jekyll

  # Jekyll hook - the generate method is called by jekyll
  class GenerateDB < Generator

    def generate(site)
        parser = get_markdown_parser(site.config)

        sqlite_db = 'search.db'
        puts Dir.pwd
        File.delete( sqlite_db ) if File.exists?( sqlite_db )

        db = Sequel.sqlite(sqlite_db)         
        db.run('CREATE TABLE pages(  title text, permalink text, meta_keywords text, meta_description  text, text_content text, search_excerpt text, featured_image text, date text) ;')
        db.run('CREATE TABLE tags(  tag text, page int) ;')
        db.run('CREATE TABLE categories(  category text, page int) ;')
        puts "Deleted old DB. Start creating new one ..."

        site.posts.each do |post|
            permalink = "#{site.config['baseurl']}#{post.url}"
            meta_keywords = ""
            meta_description = ""
            text = post.content
            search_excerpt = parser.convert(post.excerpt)
            insert_pages = db["INSERT INTO pages (title, permalink, meta_keywords, meta_description, text_content, search_excerpt, featured_image, date) VALUES (? , ? , ?, ?, ? , ?, ?, ?)", post.title, permalink, meta_keywords, meta_description, text, search_excerpt, post.data["featured_image"], post.data["date"]]
            postid = insert_pages.insert
            post.tags.each do |tag|
                insert_tags = db["INSERT INTO tags (tag, page) VALUES (?, ?)", tag, postid]
                insert_tags.insert
            end.empty? and begin
                puts "[Info] '" + post.title + "' has no tags."
            end

            post.categories.each do |category|
                insert_category = db["INSERT INTO categories (category, page) VALUES (?, ?)", category, postid]
                insert_category.insert
            end.empty? and begin
                puts "[Info] '" + post.title + "' has no category."
            end
        end
    end

    # Gets a parser object for the parser specified in the configuration
    #
    # config - the site's configuration hash
    #
    # Returns a parser or raises exception if one isn't found
    def get_markdown_parser(config)
      return case config['markdown']
        when 'redcarpet'
          Jekyll::Converters::Markdown::RedcarpetParser.new config
        when 'kramdown'
          Jekyll::Converters::Markdown::KramdownParser.new config
        when 'rdiscount'
          Jekyll::Converters::Markdown::RDiscountParser.new config
        when 'maruku'
          Jekyll::Converters::Markdown::MarukuParser.new config
        else
          STDERR.puts "Invalid Markdown processor: #{config['markdown']}"
          STDERR.puts "  Valid options are [ maruku | rdiscount | kramdown | redcarpet ]"
          raise FatalException.new("Invalid Markdown process: #{config['markdown']}")
      end
    end
  end
end

