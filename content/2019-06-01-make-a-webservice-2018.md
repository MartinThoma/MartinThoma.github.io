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

## Flask Ecosystem

* Miguel Grinberg: [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
* DB
    * [Flask-SQLalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
    * [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)


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
        <td style="background-color: #f2dede;">6</td>
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
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #c9f8c9;">Good</td>
        <td style="background-color: #c9f8c9;">Good</td>
        <td style="background-color: #f2dede;">Bad</td>
        <td>Basic, nice</td>
        <td style="background-color: #f2dede;">Bad, via plugin</td>
        <td style="background-color: #c9f8c9;">Very Good</td>
    </tr>
    <tr>
        <th>Code</th>
        <td style="background-color: #f2dede;">No</td>
        <td>Yes</td>
        <td style="background-color: #f2dede;">No</td>
        <td>via plugin</td>
        <td>Bad</td>
        <td style="background-color: #f2dede;">No</td>
        <td>Bad</td>
    </tr>
    <tr>
        <th>MathJax</th>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #c9f8c9;">via plugin</td>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #f2dede;">No</td>
        <td style="background-color: #f2dede;">No</td>
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
        <td style="background-color: #c9f8c9;">JSON</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
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

* [SimpleMDE](https://simplemde.com/)


See also:

* https://www.tiny.cloud/ (TinyMCE)


## Decisions

* Display name? User name?
* How Many Characters may a display name have? (e.g. [30 on StackExchange](https://meta.stackoverflow.com/questions/307118/maximum-size-for-display-names))


## Favicon

* [Font Awesome](https://fontawesome.com/) ([icon search](https://fontawesome.com/icons?d=gallery))
* [Feather Icons](https://feathericons.com/)
* https://favicon.io/favicon-generator/
* https://icons8.de/icons


## Small Services

* [Gravatar](http://gravatar.com)


## E-Mail

* [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
* Mailgun, mailchimp ?


## Image Upload

* [Imgur](https://imgur.com/)?


## TODO

* OpenID: https://developer.okta.com/blog/2017/07/25/oidc-primer-part-1 and https://developer.okta.com/product/
