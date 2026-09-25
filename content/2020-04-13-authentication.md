---
layout: post
title: Authentication vs Authorization
slug: authentication-vs-authorization
lang: en
author: Martin Thoma
date: 2019-01-17 20:00
category: My bits and bytes
tags: Security, Software Engineering, Web Development
featured_image: logos/star.png
status: draft
---
Authentication is about the question of who you are. Authorization is about the
question of what you are allowed to do.


## Authentication

The most basic solution is a username and a password. By telling the web server
the secret (password), the web server can be sure that the person logging in is
actually the person which is identified by the user name.

As we don't want our users to log in on every single request, we store something
on their machine that the browser keeps sending with every request. A common
solution is a [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token) (JWT).

There are essentially two ways to store something on the client machine: [cookies](https://en.wikipedia.org/wiki/HTTP_cookie) and [local or session storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API).

### Basic Access Authentication

[Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
is one of the simplest authentication mechanisms. Essentially, the client transfers
the username and password in plain text. For this reason, HTTPS has to be used to
prevent man-in-the-middle attacks.

Drawbacks:

* Password is transmitted with every request in plain text
    * Makes SSL / TLS necessary
* Replay attacks possible
* Server has to store password in plain text
* Client has to store password

### Digest Access Authentication

Pro:

* Password only transmitted as hash
* Messages are signed
* [Nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce) / Timestamp used -> replay attacks not possible
* SSL / TLS not necessary

Con:

* Server has to store password in plain text
* Client has to store password



## See also

* [What are the main differences between JWT and OAuth authentication?](https://stackoverflow.com/q/39909419/562769)
* [github.com/hasgeek/lastuser](https://github.com/hasgeek/lastuser)
* [en.wikipedia.org/wiki/Argon2](https://en.wikipedia.org/wiki/Argon2)
* [de.slideshare.net/…/api-authentifizierung-und-aut…](https://de.slideshare.net/StefanKienzl/api-authentifizierung-und-autorisierung)
