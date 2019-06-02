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
    <tr>
        <td>Bold/Italic/Underline</td>
        <td>B+I+U</td>
        <td>B+U</td>
        <td>B+I</td>
        <td>B+I</td>
        <td>B+I</td>
        <td>B+I+U</td>
        <td>B+I+U</td>
    </tr>
    <tr>
        <td>Headings</td>
        <td>3</td>
        <td>6</td>
        <td>3</td>
        <td>4</td>
        <td>6</td>
        <td>2</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Tables</td>
        <td>No</td>
        <td>Good</td>
        <td>Ok</td>
        <td>Bad, via Plugin</td>
        <td>Ok</td>
        <td>Good, via plugin</td>
        <td>Good</td>
    </tr>
    <tr>
        <td>Lists</td>
        <td>ol+ul</td>
        <td>ol+ul</td>
        <td>ol+ul</td>
        <td>ol+ul</td>
        <td>ol+ul</td>
        <td>No</td>
        <td>ol+ul</td>
    </tr>
    <tr>
        <td>Links</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>File Upload</td>
        <td>No</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Images</td>
        <td>No</td>
        <td>Good</td>
        <td>Good</td>
        <td>Bad</td>
        <td>Basic, nice</td>
        <td>Bad, via plugin</td>
        <td>Very Good</td>
    </tr>
    <tr>
        <td>Code</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>via plugin</td>
        <td>Bad</td>
        <td>No</td>
        <td>Bad</td>
    </tr>
    <tr>
        <td>MathJax</td>
        <td>No</td>
        <td>No</td>
        <td>No</td>
        <td>via plugin</td>
        <td>No</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>(Y)ouTube / (V)imeo</td>
        <td>No</td>
        <td>Y+V</td>
        <td>No</td>
        <td>No</td>
        <td>No</td>
        <td>Bad, via plugin</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Output</td>
        <td>JSON</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
        <td>HTML</td>
    </tr>
    <tr>
        <td>License/Price</td>
        <td>BSD</td>
        <td>MIT</td>
        <td>GPLv2, LGPLv2.1</td>
        <td>MIT</td>
        <td>$199</td>
        <td>MIT</td>
        <td>$1199</td>
    </tr>
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
