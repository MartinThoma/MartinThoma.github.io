---
layout: post
title: Static Blog Generators
author: Martin Thoma
date: 2013-11-24 04:22:57
categories: 
- The Web
tags:
- Jekyll
featured_image: 2013/12/jekyll-thumbnail.png
---
I currently want to get my mind clear about static blog generators.

If I understand it correctly, the idea is something I did years ago as I did not have enough money to get a web server that supports PHP. So I had to deliver static sites (HTML, CSS, JavaScript). Now I have enough money to use a webserver hosting WordPress. But still, static websites have some important advantages compared to dynamically generated ones like WordPress:
<ul>
  <li><strong>Speed</strong>: Serving a static page is a no-brainer. You don't need to compute anything, because it is static. The webserver needs only to serve it to the client.</li>
  <li><strong>Security</strong>: Updating WordPress and plugins is important, because your site could get hacked by using errors in WordPress and/or plugins. But if you use a static blog generators, it is <del datetime="2013-11-24T02:23:09+00:00">impossible</del> MUCH more complicated to use errors in them to hack your website.</li>
  <li><strong>Simplicity</strong>: I was thinking about website dumps to make sure I don't loose all my content by a server crash. But when I have everything on my computer, that gets easier. I can make regular dumps of my hdd and it will contain my website.</li>
  <li><strong>Scalability</strong>: Suppose your blog gets more and more visitors. For dynamic websites, solutions get complex. In contrast, serving a static website is easier.</li>
</ul>

Reasons against using a static website generator are:
<ul>
  <li><strong>User base</strong>: WordPress has A LOT of users and developers. You can find plugins for everything you want. I think that might get much more difficult with Jekyll and Hyde or Nikola.</li>
  <li><strong>Comments</strong>: Comments are dynamic. Well, kind of. As most comments need to be approved, they don't really are. But this is something the server has to handle. Or I have to use a given service.</li>
</ul>

<h2>Comments</h2>
I think 

Services:
<ul>
  <li><a href="http://disqus.com/">Disqus</a></li>
</ul>

<h2>Jekyll</h2>
<table>
  <tr>
    <td>Official Website</td>
    <td><a href="http://jekyllrb.com/">jekyllrb.com</a></td>
  </tr>
  <tr>
    <td>Written with</td>
    <td>Ruby</td>
  </tr>
  <tr>
    <td>Templates</td>
    <td><a href="http://liquidmarkup.org/">LiquidMarkup.org</a></td>
  </tr>
  <tr>
    <td>Example blogs</td>
    <td><a href="http://www.ericlathrop.com/">Eric Lathrop</a></td>
  </tr>
</table>

<h3>Setting a new website up</h3>
```bash
jekyll new my-awesome-site
cd my-awesome-site
jekyll serve
```

Open <a href="http://localhost:4000">http://localhost:4000</a> in a browser

<h2>Hyde</h2>

<h2>Nikola</h2>
<table>
  <tr>
    <td>Official Website</td>
    <td><a href="http://getnikola.com/">getnikola.com</a></td>
  </tr>
  <tr>
    <td>Written with</td>
    <td>Python?</td>
  </tr>
  <tr>
    <td>Templates</td>
    <td>?</td>
  </tr>
  <tr>
    <td>Example blogs</td>
    <td>?</td>
  </tr>
</table>

<h2>More information</h2>
<ul>
  <li>Jekyll:
    <ul>
      <li><a href="http://vitobotta.com/migrating-from-wordpress-to-jekyll-part-one-why-I-gave-up-on-wordpress/">Reasons to migrate from WordPress to Jekyll</a></li>
      <li><a href="http://vitobotta.com/how-to-migrate-from-wordpress-to-jekyll">How to migrate</a></li>
    </ul>
  </li>
</ul>
