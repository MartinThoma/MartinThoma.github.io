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


<figure class="ai-generated">
    <a href="../images/2020/04/authentication-authorization.jpg"><img src="../images/2020/04/authentication-authorization.jpg" alt="A bouncer checks an ID card at an entrance, behind it doors with a green check for allowed and a red lock for forbidden rooms" width="1376" height="768"></a>
    <figcaption>Authentication checks who you are, authorization what you may do.</figcaption>
</figure>

Both are often mixed up, also because HTTP calls the header that carries
credentials `Authorization`. In a web application they happen one after the
other: first the server finds out who sends the request (authentication), then
it checks whether this user may do what the request asks for (authorization).
A third, related term, identification, is explained in
[Identification vs Authentication vs Authorization](../identification-authentication-authorization/).

TODO: Should I merge this article into the already-published one?


## Authentication

The most basic solution is a username and a password. By telling the web server
the secret (password), the web server can be sure that the person logging in is
actually the person which is identified by the user name. The server doesn't
need to know the password itself: it stores a slow, salted hash
([Argon2](https://en.wikipedia.org/wiki/Argon2), bcrypt, scrypt) and compares the
hash of the transmitted password with it.

As we don't want our users to log in on every single request, the server hands
out something that the client sends with every following request. There are two
common approaches:

* **Session ID.** A random string that the server stores together with the user
  ID. The client gets it as a cookie. Logging out is easy: delete the session on
  the server.
* **Token.** A signed piece of data that contains the user ID and an expiry
  date, for example a [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token)
  (JWT). The server only has to verify the signature, it doesn't need to store
  anything. The flip side: a token can't be revoked before it expires, unless the
  server keeps a blocklist after all.

There are essentially two ways to store something on the client machine:
[cookies](https://en.wikipedia.org/wiki/HTTP_cookie) and
[local or session storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API).
The browser sends cookies automatically; values in local storage have to be
added to each request by JavaScript, usually in the `Authorization: Bearer …`
header. Cookies with the `HttpOnly` flag can't be read by JavaScript at all,
which protects them against cross-site scripting. That makes them the safer
choice for web applications.

### Basic Access Authentication

[Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
is one of the simplest authentication mechanisms. Essentially, the client transfers
the username and password in plain text (only Base64-encoded). For this reason,
HTTPS has to be used to prevent man-in-the-middle attacks.

Drawbacks:

* Password is transmitted with every request in plain text
    * Makes SSL / TLS necessary
* Replay attacks are possible if the traffic is intercepted
* Client has to store the password (browsers keep it for the session)
* There is no proper logout

The server, in contrast, can store a password hash as usual.

### Digest Access Authentication

[Digest access authentication](https://en.wikipedia.org/wiki/Digest_access_authentication)
([RFC 7616](https://datatracker.ietf.org/doc/html/rfc7616)) was meant to fix the
plain-text problem: the client sends a hash of the password and a server
nonce instead of the password.

Pro:

* Password only transmitted as hash
* [Nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce) / Timestamp used -> replay attacks are harder
* With `qop=auth-int`, the message body is protected against changes, too (rarely supported)

Con:

* Server has to store the password in plain text or a hash of username, realm
  and password, which is as good as the password for this site
* Client has to store password
* Based on MD5, and an attacker in the middle can downgrade the client to a
  weaker variant. It is not a replacement for TLS: use HTTPS anyway

Today both are mainly used for simple internal tools and APIs. Public web
applications use a login form and a session cookie, and increasingly
[passkeys](../login-systems/).

### Delegated authentication

With [OAuth 2.0](https://oauth.net/2/) and
[OpenID Connect](https://openid.net/developers/how-connect-works/), another
service does the authentication. "Sign in with Google" is OpenID Connect: Google
checks who you are and confirms it to the application, which never sees your
Google password. OAuth 2.0 itself is about authorization: it lets you allow an
application to access some of your data at another service, for example your
calendar.


## Authorization

Once the server knows who the user is, it checks every request against rules.
Common models:

* **Access control lists (ACL):** every object has a list of users and what they
  may do with it. File systems work like this.
* **Role-based access control (RBAC):** users get roles ("admin", "editor",
  "viewer"), roles get permissions. Easy to understand and to audit.
* **Attribute-based access control (ABAC):** rules on attributes of user, object
  and context, for example "managers may approve invoices of their own
  department below 10,000 €".

The most common mistake isn't choosing the wrong model, it is forgetting the
check: the server returns invoice 1234 to anyone who asks for `/invoices/1234`,
because it only checked that the user is logged in. OWASP lists this as the
number one API security risk
([Broken Object Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)).
Authorization has to happen on the server, for every object, on every request.
Hiding a button in the user interface is not authorization.


## See also

* [What are the main differences between JWT and OAuth authentication?](https://stackoverflow.com/q/39909419/562769)
* [github.com/hasgeek/lastuser](https://github.com/hasgeek/lastuser)
* [en.wikipedia.org/wiki/Argon2](https://en.wikipedia.org/wiki/Argon2)
* [de.slideshare.net/…/api-authentifizierung-und-aut…](https://de.slideshare.net/StefanKienzl/api-authentifizierung-und-autorisierung)
* [Password Hashing](../password-hashing/)
* [Multi-Factor Authentication](../multi-factor-authentication/)
