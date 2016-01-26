---
layout: post
title: Why I will migrate from Jekyll to Pelican
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Cyberculture
tags:
- Jekyll
featured_image: logos/star.png
---

When I build my blog ([source](https://github.com/MartinThoma/MartinThoma.github.io)), I get

```bash
  Liquid Exception: Missing or stray quote in line 4 in _posts/2015-06-24-languages-for-back-ends.md
/usr/lib/ruby/2.1.0/csv.rb:1824:in `block (2 levels) in shift': Missing or stray quote in line 4 (CSV::MalformedCSVError)
    from /usr/lib/ruby/2.1.0/csv.rb:1817:in `each'
    from /usr/lib/ruby/2.1.0/csv.rb:1817:in `block in shift'
    from /usr/lib/ruby/2.1.0/csv.rb:1777:in `loop'
    from /usr/lib/ruby/2.1.0/csv.rb:1777:in `shift'
    from /usr/lib/ruby/2.1.0/csv.rb:1719:in `each'
    from /home/moose/GitHub/MartinThoma.github.io/_plugins/caption_tag.rb:115:in `each_with_object'
    from /home/moose/GitHub/MartinThoma.github.io/_plugins/caption_tag.rb:115:in `parse_attrs'
    from /home/moose/GitHub/MartinThoma.github.io/_plugins/caption_tag.rb:199:in `render'
    from /usr/lib/ruby/vendor_ruby/liquid/block.rb:109:in `block in render_all'
    from /usr/lib/ruby/vendor_ruby/liquid/block.rb:96:in `each'
    from /usr/lib/ruby/vendor_ruby/liquid/block.rb:96:in `render_all'
    from /usr/lib/ruby/vendor_ruby/liquid/block.rb:82:in `render'
    from /usr/lib/ruby/vendor_ruby/liquid/template.rb:128:in `render'
    from /usr/lib/ruby/vendor_ruby/liquid/template.rb:138:in `render!'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/convertible.rb:106:in `render_liquid'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/convertible.rb:233:in `do_layout'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/post.rb:261:in `render'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/site.rb:298:in `block in render'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/site.rb:297:in `each'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/site.rb:297:in `render'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/site.rb:51:in `process'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/command.rb:28:in `process_site'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/commands/build.rb:56:in `build'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/commands/build.rb:34:in `process'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/lib/jekyll/commands/build.rb:18:in `block (2 levels) in init_with_program'
    from /var/lib/gems/2.1.0/gems/mercenary-0.3.5/lib/mercenary/command.rb:220:in `call'
    from /var/lib/gems/2.1.0/gems/mercenary-0.3.5/lib/mercenary/command.rb:220:in `block in execute'
    from /var/lib/gems/2.1.0/gems/mercenary-0.3.5/lib/mercenary/command.rb:220:in `each'
    from /var/lib/gems/2.1.0/gems/mercenary-0.3.5/lib/mercenary/command.rb:220:in `execute'
    from /var/lib/gems/2.1.0/gems/mercenary-0.3.5/lib/mercenary/program.rb:42:in `go'
    from /var/lib/gems/2.1.0/gems/mercenary-0.3.5/lib/mercenary.rb:19:in `program'
    from /var/lib/gems/2.1.0/gems/jekyll-2.5.3/bin/jekyll:20:in `<top (required)>'
    from /usr/local/bin/jekyll:23:in `load'
    from /usr/local/bin/jekyll:23:in `<main>'
```

I have `jekyll (2.5.3, 2.5.1)`. Jekyll says the error comes from https://github.com/MartinThoma/MartinThoma.github.io/blob/source/_posts/2015-06-24-languages-for-back-ends.md in Line 4, but 

How can I fix it? How can I even find out where the problem is?

## What I've tried

### convert “ “ into quotes that look like this - " "

According to https://docs.shopify.com/manual/your-store/products/common-import-issues#quote
But I searched for the quotes " “ “" (with `grep -nPIr '“' *`). This showed only some very old blog posts. So I don't think this is the error.

### Search for \r

`grep -nPIr '\r' *` revealed that I don't have and `\r` (I found this via http://stackoverflow.com/questions/29289208/missing-or-stray-quote-in-line-1-csvmalformedcsverror) 
```

## Build time

It takes 584,63s to deploy my blog, even if I only made a small change.