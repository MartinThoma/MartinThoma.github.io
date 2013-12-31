#!/usr/bin/env ruby
# encoding: utf-8
#
# Jekyll SQLite database generator
require 'nokogiri'
require 'sequel'

# Design decision: URLs should have a trailing slash

module Jekyll

  # Jekyll hook - the generate method is called by jekyll
  class GenerateDB < Generator

    def generate(site)
        parser = get_markdown_parser(site.config)

        sqlite_db = 'search.db'
        puts Dir.pwd
        File.delete( sqlite_db ) if File.exists?( sqlite_db )
        puts "[Info] Deleted old DB. Start creating new one ..."

        db = Sequel.sqlite(sqlite_db)         
        db.run('CREATE TABLE pages(url text, title text, permalink text, text_content text, search_excerpt text, featured_image text, date text, page_rank) ;')
        db.run('CREATE TABLE tags(  tag text, page int) ;')
        db.run('CREATE TABLE categories(  category text, page int) ;')
        db.run('CREATE TABLE internal_links(  page_from int, page_to int, text text) ;')
        db.run('CREATE TABLE external_links(  page_from int, page_to text, text text) ;')

        beginning = Time.now
        site.posts.each do |post|
            permalink = "#{site.config['baseurl']}#{post.url}/"
            text = post.content
            search_excerpt = parser.convert(post.excerpt)
            insert_pages = db["INSERT INTO pages (url, title, permalink, text_content, search_excerpt, featured_image, date) VALUES (?, ? , ? , ?, ?, ? , ?)", post.url+"/", post.title, permalink, text, search_excerpt, post.data["featured_image"], post.data["date"]]
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

        # As every post is now in the database, we can begin to
        # add link information
        site.posts.each do |post|
            rows = db.fetch( "SELECT rowid FROM pages WHERE url='"+post.url+"/';" ).all
            if rows.nil?
                puts "[Warning]["+post.url+"/] seems to be not in database (nil)"
            elsif rows.count() == 0
                puts "[Warning]["+post.url+"/] seems to be not in database (count==0)"
            elsif rows.count() > 1
                puts "[Warning]["+post.url+"/] seems to be multiple times in database (count > 1)"
            else
                postid = rows[0][:rowid]
            end

            doc = Nokogiri::HTML.parse(post.content)
            links = doc.css('a').map { |link| [link['href'],link.text] }
            links.each do |link, linktext|
                if link.nil? || link.start_with?('#')
                    # This might be an anchor
                else
                    # split anchor away.
                    if link.include?("#")
                        link, *rest = link.split(/#/)
                    end

                    if link.start_with?('chrome://')
                        # chrome link. should probably be a warning, as this will not work
                    elsif link.start_with?('http://') || link.start_with?('https://') || link.start_with?('ftp://')
                        # external link
                        insert_link = db["INSERT INTO external_links (page_from, page_to, text) VALUES (?, ?, ?)", postid, link, linktext]
                        insert_link.insert
                    elsif link.start_with?('../images/') || link.start_with?('../pdf/') || link.start_with?('../html5/') || link.start_with?('../python/') || link.start_with?('../tag/') || link.start_with?('../category/') || link.start_with?('../author/')
                        # images and automatically generated pages are not relevant to search
                    elsif !link.start_with?('../')
                        puts "[Warning][Post:"+post.url+"/] Link '"+link+"' does not start with '../'"
                    else
                        # internal link, first search the post id of the target
                        rows = db.fetch( "SELECT rowid FROM pages WHERE url='"+link[2..-1]+"';" ).all
                        if rows.nil?
                            puts "[Warning][Post:"+post.url+"/] SELECT with link '"+link+"' resulted in NIL."
                        elsif rows.count() == 0
                            puts "[Warning][Post:"+post.url+"/] Link with url '"+link+"' has no database entry."
                        elsif rows.count() > 1
                            puts "[Warning][Post:"+post.url+"/] Link with url '"+link+"' has multiple pages."
                        elsif
                            targetid = rows[0][:rowid]
                            # insert data
                            insert_link = db["INSERT INTO internal_links (page_from, page_to, text) VALUES (?, ?, ?)", postid, targetid, linktext]
                            insert_link.insert
                        end
                    end
                end
            end
        end
        puts "[Info] Finished building DB after #{Time.now - beginning} seconds"
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
