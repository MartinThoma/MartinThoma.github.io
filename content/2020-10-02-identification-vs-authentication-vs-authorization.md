---
layout: post
title: Identification vs Authentication vs Authorization
slug: identification-authentication-authorization
URL: https://medium.com/plain-and-simple/identification-vs-authentication-vs-authorization-e1f03a0ca885
author: Martin Thoma
date: 2020-10-02 20:00
category: My bits and bytes
tags: Security, AppSec, 2FA, MFA, JWT, OAuth
featured_image: logos/cybersecurity.png
---
Identification, authentication, and authorization are closely related, but not the same.
> # Identification is about knowing who somebody is, even without their cooperation.

Surveillance systems, fingerprints, DNA samples are the techniques that come to mind in the physical world. In the digital world, [device fingerprinting](https://en.wikipedia.org/wiki/Device_fingerprint) is used. It’s also possible to identify individuals by their way of writing or even [how they play computer games](http://User identification based on game-play activity patterns).
> # Authentication is about proving who I am.

I want to show my bank who I am by entering a secret only I know — the PIN. The same for pretty much any other website. The difference between identification and authentication is that the former is happening without my (explicit) cooperation, whereas the latter includes me in the process. Typical terms in this area are two-factor authentication (2FA), multi-factor authentication (MFA). As authentication is hard, single-sign-on (SSO) and [OpenID](https://en.wikipedia.org/wiki/OpenID) come into play.
> # Authorization is about access control.

Most authorization schemes need either identification or authentication, but not all. The best real-world examples are keys. If you own the key, people will assume that you are allowed to have access.
Adult websites are other examples. It is assumed that you may access them if you have a credit card. No need to know your identity (although it would be easy from there). Or the [Fight Club](https://en.wikipedia.org/wiki/Fight_Club) — if you know where it is, you are authorized.

Access control and authorization for complex systems can be done by roles. You don’t give permissions to single people, but you assign people different roles instead.

[OAuth](https://en.wikipedia.org/wiki/OAuth) is an example of a standard for authorization. [JSON Web Tokens](https://en.wikipedia.org/wiki/JSON_Web_Token) (JWT) also fit well in this context.
