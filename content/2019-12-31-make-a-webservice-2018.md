---
layout: post
title: Make a Webservice
slug: make-a-webservice
author: Martin Thoma
status: draft
date: 2019-06-01 20:00
category: The Web
tags: Web Development
featured_image: logos/star.png
---
I started doing web-stuff again! There are a gazillion decisions to take when
you create even a medium-sized web service. This article is intended to give
a small overview

## Quick n' Dirty

You can set up a first page in about than 10 minutes, if you have a [DigitalOcean](https://m.do.co/c/b5dd0c5d61b9) account and the domain via namecheap:

1. Create [Docker digital ocean droplet](https://marketplace.digitalocean.com/apps/docker)
2. Add SSH-Key to machine
3. Clone github repository
4. Create A-Record in namecheap ([takes 24h](https://support.stackpath.com/hc/en-us/articles/360001079683-How-long-does-it-take-for-DNS-changes-to-be-reflected-))

## Flask Ecosystem

* Miguel Grinberg: [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
* DB
    * [Flask-SQLalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
    * [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

## Databases

* [MariaDB vs MySQL](https://blog.panoply.io/a-comparative-vmariadb-vs-mysql)


## Front-End Framework

* [Bootstrap](https://getbootstrap.com/docs/) ([wiki](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)))
* [Materialize](https://materializecss.com/) ([wiki](https://en.wikipedia.org/wiki/Material_Design))
* [Foundation](https://foundation.zurb.com/) ([wiki](https://en.wikipedia.org/wiki/Foundation_(framework)))
* [Semantic UI](https://semantic-ui.com/)


## WYSIWYG Editors

I would like to have a WYSIWYG editor. It should support heading types,
bold/italic/underine, tables, images, videos from YouTube, file upload and
MathJax formulas.

It would be nice if  supported storing / rendering directly from Markdown. It
that doesn't exist, I might convert the HTML to Markdown and back with Pandoc.

<table class="table">
    <thead>
        <tr>
            <th>Editor</th>
            <th><a href="https://quilljs.com/">QuillJS</a></th>
            <th><a href="https://summernote.org/">Summernote</a></th>
            <th><a href="https://ckeditor.com/ckeditor-4/">CKEditor 4</a></th>
            <th><a href="https://alex-d.github.io/Trumbowyg/">Trumbowyg</a></th>
            <th><a href="https://imperavi.com/redactor/">Redactor</a></th>
            <th><a href="https://yabwe.github.io/medium-editor/">Medium</a></th>
            <th><a href="https://www.froala.com/">Froala</a></th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <th>Toolbar</th>
        <td><a href="https://quilljs.com/docs/modules/toolbar/#container">custom</a></td>
        <td><a href="https://summernote.org/deep-dive/">custom</a></td>
        <td><a href="https://ckeditor.com/docs/ckeditor4/latest/guide/dev_toolbar.html">custom</a></td>
        <td>?</td>
        <td><a href="https://imperavi.com/redactor/examples/buttons/change-buttons-in-the-toolbar/">custom</a></td>
        <td><a href="https://github.com/yabwe/medium-editor/issues/1133">?</a></td>
        <td><a href="https://www.froala.com/wysiwyg-editor/v1.2/docs/examples/custom-toolbar">custom</a></td>
    </tr>
    <tr>
        <th>Bold/Italic/Underline</th>
        <td>B+I+U</td>
        <td>B+U</td>
        <td>B+I</td>
        <td>B+I</td>
        <td>B+I</td>
        <td>B+I+U</td>
        <td>B+I+U</td>
    </tr>
    <tr>
        <th>Headings</th>
        <td>3</td>
        <td>6</td>
        <td>3</td>
        <td>4</td>
        <td style="background-color: #f2dede;">6</td>
        <td>2</td>
        <td>4</td>
    </tr>
    <tr>
        <th>Tables</th>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #c9f8c9;">Good</td>
        <td>Ok</td>
        <td style="background-color: #f2dede;">Bad, via Plugin</td>
        <td>Ok</td>
        <td style="background-color: #c9f8c9;">Good, via plugin</td>
        <td style="background-color: #c9f8c9;">Good</td>
    </tr>
    <tr>
        <th>Lists</th>
        <td>ol+ul</td>
        <td>ol+ul</td>
        <td>ol+ul</td>
        <td>ol+ul</td>
        <td>ol+ul</td>
        <td style="background-color: #f2dede;">No</td>
        <td>ol+ul</td>
    </tr>
    <tr>
        <th>Links</th>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <th>File Upload</th>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #f2dede;">No</td>
        <td>Yes</td>
        <td style="background-color: #f2dede;">No</td>
        <td>Yes</td>
        <td style="background-color: #f2dede;">No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <th>Images</th>
        <td style="background-color: #f2dede;">Bad</td>
        <td style="background-color: #c9f8c9;">Good</td>
        <td style="background-color: #c9f8c9;">Good</td>
        <td style="background-color: #f2dede;">Bad</td>
        <td>Basic, nice</td>
        <td style="background-color: #f2dede;">Bad, via plugin</td>
        <td style="background-color: #c9f8c9;">Very Good</td>
    </tr>
    <tr>
        <th>Code</th>
        <td>Yes</td>
        <td>Bad, also <a href="https://epiksel.github.io/summernote-highlight/">via plugin</a></td>
        <td style="background-color: #c9f8c9;">Good, <a href="https://ckeditor.com/docs/ckeditor4/latest/examples/codesnippet.html">via Plugin</a></td>
        <td>via plugin</td>
        <td>Bad</td>
        <td style="background-color: #f2dede;">No</td>
        <td>Bad</td>
    </tr>
    <tr>
        <th>MathJax</th>
        <td>Bad</td>
        <td style="background-color: #c9f8c9;">Good, <a href="https://github.com/tylerecouture/summernote-math">via plugin</a></td>
        <td style="background-color: #c9f8c9;">Good, <a href="https://ckeditor.com/cke4/addon/mathjax">via plugin</a></td>
        <td style="background-color: #c9f8c9;">Basic, <a href="https://alex-d.github.io/Trumbowyg/demos/#plugins-mathml">via plugin</a></td>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #f2dede;"><a href="https://github.com/yabwe/medium-editor/issues/1500">No</a></td>
        <td style="background-color: #f2dede;">Questionable, <a href="https://www.froala.com/wysiwyg-editor/examples/wiris">via plugin</a></td>
    </tr>
    <tr>
        <th>(Y)ouTube / (V)imeo</th>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #c9f8c9;">Y+V</td>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #f2dede;">No</td>
        <td>Bad, via plugin</td>
        <td style="background-color: #c9f8c9;">Yes</td>
    </tr>
    <tr>
        <th>Output</th>
        <td style="background-color: #f2dede;">JSON</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
    </tr>
    <tr>
        <th>Community</th>
        <td><a href="https://stackoverflow.com/questions/tagged/quill">604 SO</a></td>
        <td><a href="https://stackoverflow.com/questions/tagged/summernote">716 SO</a></td>
        <td style="background-color: #c9f8c9;"><a href="https://stackoverflow.com/questions/tagged/ckeditor">8033 SO</a></td>
        <td style="background-color: #f2dede;"><a href="https://stackoverflow.com/questions/tagged/trumbowyg">38 SO</a></td>
        <td><a href="https://stackoverflow.com/questions/tagged/redactor">268 SO</a></td>
        <td style="background-color: #f2dede;"><a href="https://stackoverflow.com/questions/tagged/medium-editor">60 SO</a></td>
        <td><a href="https://stackoverflow.com/questions/tagged/froala">344 SO</a></td>
    </tr>
    <tr>
        <th>Dependencies</th>
        <td></td>
        <td>jQuery</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <th>License/Price</th>
        <td style="background-color: #c9f8c9;">BSD</td>
        <td style="background-color: #c9f8c9;">MIT</td>
        <td style="background-color: #c9f8c9;">GPLv2, LGPLv2.1</td>
        <td style="background-color: #c9f8c9;">MIT</td>
        <td>$199</td>
        <td style="background-color: #c9f8c9;">MIT</td>
        <td style="background-color: #f2dede;">$1199</td>
    </tr>
    </tbody>
</table>

One should also mention that there are a couple of Markdown editors out there.
Usually, you can only write Markdown and see a preview:

* [StackEdit](https://stackedit.io/)
* [HackMD](https://hackmd.io/)
* [SimpleMDE](https://simplemde.com/)

See also:

* [OryEditor](https://ory-editor.aeneas.io/): Similar to Medium, but a lot more functionality
* [Trix](https://trix-editor.org/): Another super basic editor. Looks nice.
* [TinyMCE](https://www.tiny.cloud/)


## Decisions

* Display name, Username or Handle? (<a href="https://help.disqus.com/user-profile/what-is-the-difference-between-my-username-and-my-display-name">Disqus</a>, <a href="https://help.kik.com/hc/en-us/articles/115006041908-Username-vs-display-name">Kik</a>, <a href="https://community.spotify.com/t5/Social/Username-and-Displayed-name-are-different/td-p/4564880">Spotify</a>, <a href="https://help.twitch.tv/s/article/username-rename-and-recycling-policies?language=en_US">Twitch</a>)
* How Many Characters may a display name have? (e.g. [30 on StackExchange](https://meta.stackoverflow.com/questions/307118/maximum-size-for-display-names))
* Where are hard deletes allowed, where only soft deletes?


## Favicon

* [Font Awesome](https://fontawesome.com/) ([icon search](https://fontawesome.com/icons?d=gallery))
* [Feather Icons](https://feathericons.com/)
* https://favicon.io/favicon-generator/
* https://icons8.de/icons
* [gridicons](https://github.com/Automattic/gridicons) (Wordpress)


## Small Services

* [Gravatar](http://gravatar.com)


## E-Mail

* [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
* Mailgun, mailchimp ?
* [SendGrid](https://sendgrid.com/) ([users](https://stackshare.io/sendgrid))
* Mail-Server [Docker `tvial/docker-mailserver:latest`](https://github.com/tomav/docker-mailserver): Requires 1 GB RAM


## Image Upload

* [Imgur](https://imgur.com/)?

## Social Stuff

There are two aspects of social service optimization: Making it easy to share
stuff from your site and being active on that site. Or at least reachable.

* Twitter:
    * Is it worth to create an account?
    * [Twitter Card](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/summary-card-with-large-image.html)
* Facebook:
    * [Open Graph](https://en.wikipedia.org/wiki/Facebook_Platform#Open_Graph_protocol)


## Payment

* PayPal?
* [Stripe](https://stripe.com) ([users](https://stackshare.io/stripe)) ?


## Tests

* Google: [Pagespeed Insights](https://developers.google.com/speed/pagespeed/insights/)
* Google Analytics
* [gtmetrix.com](https://gtmetrix.com/reports/enzado.com/oM61ID2t): 98% speed, 93% YSlow, 0.9s, 219kb, 11 Requests
* [thinkwithgoogle.com: Test My Site](https://www.thinkwithgoogle.com/intl/de-de/feature/testmysite): 1.6s in einem 4G-Netz
* [IPv6](https://ipv6-test.com/validate.php)


## TODO

* OpenID: https://developer.okta.com/blog/2017/07/25/oidc-primer-part-1 and https://developer.okta.com/product/, [Coding Horror](https://blog.codinghorror.com/openid-does-the-world-really-need-yet-another-username-and-password/)
* [Login design](https://blog.codinghorror.com/the-god-login/)
* Bootstrap:
    * https://startbootstrap.com/templates/
    * https://getbootstrap.com/docs/4.1/examples/
    * https://getbootstrap.com/docs/4.1/examples/dashboard/
* Stock Photos:
    * https://www.pexels.com/photo/beach-blue-sky-idyllic-island-373394/
    * https://blog.snappa.com/free-stock-photos/
    * https://pixabay.com/de/
    * https://www.foleon.com/blog/5-sites-for-free-stock-photos
    * https://www.canva.com/photos/free/
    * https://unsplash.com/free-stock-photos
* Flask-Admin for database management
* Flask-Assets for asset management
* Flask-Security for authentication
