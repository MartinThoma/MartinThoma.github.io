---
layout: post
title: How to use Jekyll with GitHub
author: Martin Thoma
categories:
- The Web
tags:
- Jekyll
- Git
- GitHub
- rsync
featured_image: 2013/12/jekyll-thumbnail.png
description: Jekyll, a static blog generator, is nice for several reasons. Those reasons and some hints how to migrate from WordPress to Jekyll are provided below.
---

You've probably noticed that I didn't write any posts the last few 
weeks. The reason is that I've migrated my WordPress Blog to Jekyll. 
This means it takes some source files and generates purely static 
pages from that. The generation process is independant of user 
requests.

[Jekyll](http://jekyllrb.com/) is a static blog generator, just like
[Pelican](http://blog.getpelican.com/), [Hyde](http://ringce.com/hyde),
[nanoc](http://nanoc.ws/) and [Octopress](http://octopress.org/).

I've spend about 40-80 hours to migrate from WordPress to Jekyll.
And I'm not done jet.

## Jekyll compared with WordPress ##
Jekyll is a static site generator. This means you have the
source files on your computer. Then you generate the website
with Jekyll and upload only the generated files. So you only push
content to the server, but you don't have to download anything from
the server.

Reasons for Jekyll:

* **Security**: With Jekyll, you only upload static files (HTML, CSS,
  JavaScript, Images, ...). There is nothing where the user can pass some data.
  This also means there is one thing less to update.<br/>
  Assuming your provider updates your server software (e.g. Apache) you don't
  have to update anything. In contrast, when you don't regularly install
  updates on your WordPress blog (and hope that those updates don't break
  anything), your blog is quite likely to be hacked.
* **Speed**: The webserver needs only to serve the sites. Nothing else. Of
  course, when you use caching with PHP you might get into a similar situation
  with WordPress. But it will never be faster.
* **Hosting**: You only need webspace. This reduces hosting cost significantly.
  Additionally, you can use [Amazon S3](http://aws.amazon.com/s3/) for hosting!
* **Backups**: Creating security backups is VERY easy with Jekyll. Every tool
  that can make bakups of files can backup your Jekyll blog. No need to worry
  about databases. If a file is corrupt, only that file is affected. No worries
  about maximum execution time for importing / exporting backups. No need to
  get SSH access. Simple FTP access does the job.

Reasons for WordPress:

* **Comments**: There is no way to get comments only with static pages. So you
  need something else, e.g. <a href="http://disqus.com/">disqus</a>.
* **Search**: Could probably be done with JavaScript, but I guess it is
  difficult.
* **Editor**: WordPress gives you a WYSIWYG editor. I don't know if there is
  something similar for Jekyll.
* **Compile time**: Compilation time is very long for Jekyll. For my blog, it
  needs over 6 minutes. As I test the result quite often before I publish
  posts, this is very annoying.
* **Tagging, Category pages, Author pages**: Currently, Jekyll lacks basic
  support for blogging. You don't have tag pages per default, the plugins that
  provide tags don't have paginated tag index pages. The same problem occurs
  when it comes to categories or authors.
* **Timed posts**: I did not use timed posts very often, but it is very easy to
  create them with WordPress. With Jekyll, on the other hand, you have to know
  how to create cronjobs. And your computer has to be running.

## Install Jekyll

On an Ubunty system I need for this blog:

```bash
$ sudo apt-get install ruby1.9.1-dev imagemagick ruby-rmagick libmagickwand-dev ruby-execjs ruby-nokogiri
$ sudo gem install jekyll
$ sudo gem install dimensions
$ sudo gem install fileutils
$ sudo mkdir -p /var/www/blog
```

## GitHub ##

### Create your repository ###
1. Go to <a href="https://github.com/">github.com</a>, sign in and create a new repo:
2. Call it `[Username].github.io`.

### Branches ###
The way to use Jekyll with GitHub is by using branches.
Go to your Git repository that cointains your blog:

```bash
moose@pc08 ~/Downloads/MartinThoma.github.io $ ls
_config.yml  favicon.ico  index.html  Makefile  Readme.md
css          images       js          _plugins  _site
_drafts      _includes    _layouts    _posts    thumbs
```

Now you should create a new branch that will contain your source files.
The following command creates a branch `sources` that starts where
the branch `master` currently is:

```bash
git checkout -b source master
```

Now update this branch to the server:

```bash
git push -u origin source
```

When you enter

```bash
git checkout . master
```

you will switch to the `master` brach. The same way you can switch
to the `source` branch. After you've entered the command, you can
look at the folder in your file system. There will only be the data
of the current branch.

### Custom Domain ###
If you want to host your content at GitHub, but have a custom Domain
like `martin-thoma.com` instead of `martinthoma.github.io`, you
have to:

1. Ask your provider (in my case "Knallhart") to add an A-record to
   Github.
2. Add a file called `CNAME` with content `martin-thoma.com`
   (yes, without `http://`) to the root of your directory

GitHub also offers some help on [setting up a custom domain with Pages](https://help.github.com/articles/setting-up-a-custom-domain-with-pages).

## FTP Server ##
If you have your own FTP server, you probably want to use it.

One tool that might now come to your mind is `rsync`. But rsync 
needs SSH ([source](http://serverfault.com/a/24627/113899)). If you
have SSH, then you can do something like this:

```bash
rsync -avz --delete _site/ user@host:/path/to/web/root
```

The `--delete` options "delete[s] extraneous files from dest dirs",
`-a` means archive which preserves the owner, group, change date
and some more of files, `-v` is verbose as always and `-z` is for
compression while the file transfer happens. `--progress` might also
be interesting, especially for the first upload.

Otherwise, you might want to try `curlftpfs`. This program lets you
mount a FTP folder:

```bash
curlftpfs ftp.example.com/backups /mnt/ftpserver
```

and you can also umount it:

```bash
rsync --delete /var/backups /mnt/ftpserver
```

## Markdown ##
I've switched between `rdiscount` and `redcarpet`. The former is
faster, the latter supports fenced code blocks. I finally stuck with
redcarped, because Liquid has problems when it comes to C++ for loops
after curly braces.

Other Markdown parsers are `maruku` (which has a 
[Multiple lines for HTML &lt;li&gt;-tag](https://github.com/bhollis/maruku/issues/121)
issue) and `kramdown` (which is slow and does not handle fenced
code blocks and LaTeX correctly).

Similar to [Matthias](http://bloerg.net/2013/03/07/using-kramdown-instead-of-maruku.html)
I would like to share a feature matrix of Markdown parsers included
into Jekyll. I have used `jekyll 1.4.3` to create the following table.
I've used [this page](../formatting-strings-python/) to see if fenced
code blocks and pygments is working and [that page](../solve-linear-congruence-equations/) for LaTeX.
Everything was tested with [this site](https://github.com/MartinThoma/MartinThoma.github.io).

|                    | `redcarpet` | `rdiscount` | `kramdown` | `maruku` |
|--------------------|-------------|-------------|------------|----------|
| LaTeX              |  ✓          | ✓           | ✓          | ?        |
| Fenced code blocks |  ✓          | ✓           | ~          | ?        |
| Pygments           |  ✓          | ✓           | ✓          | ?        |
| Site generation    |  176.90s    | 165.41s     | 293.26s    | ?        |

Kramdown destroyed some fenced code blocks (but not all) and maruku
did not even compile my site at all.

### Linebreaks and newline ###
Linebreaks are an issue. Sometimes I want to get a `<br/>`, sometimes
I make linebreaks to make reading of the text files easier. It's
basically [this discussion](http://meta.stackoverflow.com/questions/26011/should-the-markdown-renderer-treat-a-single-line-break-as-br).

Currently, I'm not satisfied with the situation. I never had that
problem with WordPress. WordPress simply created paragraphs just at
the right location.

## Customization ##
You can create [custom Liquid filters](http://jekyllrb.com/docs/plugins/),
plugins and templates. Everything is quite easy. The Liquid templating
language seems to be very similar to Django Templates (Python).

## Make the Website super-fast ##

### CSS Minification ###
```bash
sudo gem install juicer
juicer install jslint
juicer install yui_compressor
```

### Images ###
I've included small images as base64 (used [this online tool](http://webcodertools.com/imagetobase64converter/Create)). According to [caniuse](http://caniuse.com/datauri) it's quite save to use.

## Site Search ##
Site search is a real problem. I've seen three solutions so far:

1. **Dynamic Search**: You can add a dynamic part to your statically
   generated website. For example, I create a `search/index.php` and
   a SQLite database like it was [described here](http://www.businessguide.co.uk/blog/jekyll-search-ways-to-search-a-static-site/).
2. **Static JavaScript**: Create a JSON file or something similar and
   search dynamically with JavaScript in it.
3. **External Search Engines**: You could use a search engine for 
   searching your site, of course.
   * Hosted by you:
   * Commercial
        * [Google Custom Search](https://www.google.com/cse)
        * [Index Den](http://www.indexden.com/): Has no direct support
          to parse your website

### PHP+SQLite ###

### JavaScript solutions ###
One JavaScript solution I've found is [lunr](https://github.com/slashdotdash/jekyll-lunr-js-search).
This one is really bad as it copies the whole body to a json file.
This json file has to be loaded before it works. But my posts total
at the moment to 2MB. I'm pretty sure my readers don't want to wait
until 2MB are downloaded. So this one does only work for smaller
websites.

[Christan Fei's solution](http://christian-fei.com/simple-jekyll-search-jquery-plugin/)
does only search in the title and category.

## Templates ##
Jekyll uses Liquid as a templating language. It is similar to Django
templates. [Here](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers)
is a short introduction to Liquid.

## Some tests ##
* Validation
  * [validator.w3.org](http://validator.w3.org/check?uri=martin-thoma.com):
    My site is HTML-valid. The error that this validator shows is caused
    by an bug inside of the validator itself.
  * [jigsaw.w3.org](http://jigsaw.w3.org/css-validator/validator?uri=martin-thoma.com):
  My site is CSS-valid.
* Speed: Could be better...
  * [tools.pingdom.com](http://tools.pingdom.com/)
  * [PageSpeed](http://developers.google.com/speed/pagespeed/insights/?url=martin-thoma.com) 72 on mobile and 85 on desktop
* Accessiblity:
  * [wave.webaim.org](http://wave.webaim.org/report#/http%3A%2F%2Fmartin-thoma.com%2F)
  * [Functional Accessibility Evaluator](http://fae.cita.uiuc.edu/report/14396f38bc6546f6/)
* More:
  * [Mobile readyness](http://ready.mobi/launch.jsp?locale=en_EN#fragment-1)
  * [Load test](http://loadimpact.com/)
  * [Alexa](http://www.alexa.com/siteinfo/martin-thoma.com)
  * [Google Structured Data Testing Tool](http://www.google.com/webmasters/tools/richsnippets): Test if google can extract the author from your blog posts
  * [Twitter card validator](https://dev.twitter.com/docs/cards/validation/validator) (more about [Twitter cards](https://dev.twitter.com/cards))
  * [Nibbler](http://nibbler.silktide.com/reports/martin-thoma.com): This one tests quite a lot.

I've also used LinkChecker to check if all new links are valid. I've found quite a lot of old links and replaced them with new links.

## Resources ##
* <a href="https://help.github.com/articles/setting-up-a-custom-domain-with-pages#setting-the-domain-in-your-repo">Setting up a custom domain with Pages</a>
* <a href="https://alybadawy.com/developing/2013/08/02/search-a-jekyll-generated-website/">Search a Jekyll-generated website</a>
* <a href="http://philipm.at/2011/jekyll_vs_hyde.html">Jekyll vs. Hyde - A Comparison Of Two Static Site Generators</a>

