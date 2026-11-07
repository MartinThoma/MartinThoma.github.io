---
layout: post
title: Cross-Site Request Forgery 😈
slug: cross-site-request-forgery
lang: en
author: Martin Thoma
date: 2021-02-09 22:32
category: Security
tags: Security, AppSec
featured_image: logos/cybersecurity.png
summary: What CSRF is, how it’s done, and how you can prevent it
medium_url: https://medium.com/@martinthoma/cross-site-request-forgery-ead42933972d
status: draft
---
Cross-Site Request Forgery (short: CSRF or XSRF) is an attack that makes the victim's browser execute a request to a website where the victim has interesting privileges. It’s sometimes pronounced “sea surf” or called “session riding”. A CSRF attack could make your browser transfer money from your bank to the attacker, buy something for the attacker in an online store, connect in a social network, like a product/Tweet/post, and many other things.

Let’s learn how CSRF is done and how it’s prevented!

## Why you should care

Similar to SQL Injections, you can defend perfectly against CSRFs if you know that it is an issue. However, if you are not aware of the problem, you might also not take any measures against the attack.

* CSRF was #8 in OWASP Top-10 2013 and #5 in 2010.
* 2008: Netflix was vulnerable to CSRF attacks ([source](https://seclists.org/fulldisclosure/2006/Oct/316))
* 2016: AVM FritzBox was vulnerable to CSRF attacks ([source](https://www.zdnet.de/88256320/avms-fritzbox-router-mit-aelterer-firmware-von-sicherheitsluecke-betroffen/))
* 2019: [www.cert-bund.de](http://www.cert-bund.de) was vulnerable to CSRF attacks ([source](https://www.golem.de/news/websicherheit-cert-bund-war-anfaellig-fuer-csrf-angriff-1910-144699.html), [source 2](https://www.cert-bund.de/freetextmessage/CB-I19-0001)). This is an organization of the German government which is related to IT security.
* 2019: SupportAssist by Dell was vulnerable to CSRF attacks ([source](https://threatpost.com/dell-flaws-security-support-tool/144295/))
* 2020: Austrian mobile internet providers (Drei, Yesss) were vulnerable to CSRF attacks ([source](https://www.heise.de/news/rC3-Massive-Schwachstellen-in-Apps-von-Mobilfunkanbietern-4986008.html))
* 2020: Meetup.com was vulnerable to CSRF ([source](https://www.dev-insider.de/gefahr-im-gruppen-chat-von-meetup-a-957264/))

## How it works

Websites need a way to authenticate. When you log in, your browser stores some session information to prevent that you have to enter your username and password with every single request. It’s typically stored as a cookie. Let’s just call that part “session context”. The session context is automatically sent with every request your browser makes.

Let’s make an example attack. You are a loyal customer of bank.com. You’re logged in pretty much all the time. The attacker created a malicious website attack.com and tricked you to visit it. When you visit attack.com, your browser executes the JavaScript on it automatically. It also downloads all images. The attacker told your browser to call

```
bank.com/send_money?to=attacker&amount=1234.56
```

As you are logged in and a customer of bank.com, you just lost \$1234.56 USD. This is where the name comes from: The attacker made the victim's browser create a request. The **request was forged** on attack.com, but the request went to bank.com. The request is **cross-domain**.

How does the attacker make the browser call the domain?

**Image tags** are an option for GET requests:

```
<img src="bank.com/send_money?to=attacker&amount=1234.56" />
```

**Forms** are another option for GET or for POST requests:

```
<iframe style="display:none" name="iframe"></iframe>
<form method="POST" action="http://vulnerable-bank-953.com" target="iframe" id="form">
    <input type="hidden" name="to" value="attacker" />
    <input type="hidden" name="amount" value="1000" />
</form>
<script>document.getElementById("form").submit()</script>
```

PUT and DELETE requests are harder, but possible if the server has a [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) misconfiguration.

### CSRF Login attack

A CSRF Login attack is super weird. The attacker logs the victim out and makes sure that the victim is logged in with the attackers' account.

You might think that this can only harm the attacker, but it depends a lot on the website. The YouTube Channel LiveOverflow shows an awesome way how an [XSS attack](../xss/) targeting your own account + logout CSRF + login CSRF can be exploited to steal users’ passwords:

<iframe width="560" height="315" src="https://www.youtube.com/embed/KaEj_qZgiKY" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

## How can I defend against CSRF attacks?

There are a couple of things that work and others that seem reasonable, but actually don’t help. The defenses that work against CSRF are marked with ✓, the others are marked with ❌.

### Anti-CSRF Tokens ✓

You can add a random value to every form. When the form is submitted, the value is transferred as well. The backend then needs to know which random value was expected and validate. If the value does not match, the request is blocked.

This is called the Synchronizer Token Pattern (STP). Read Jude Niroshan’s nice article to learn more about it:

[**What is CSRF Synchronizer Token Pattern?** *CSRF or Cross-Site Request Forgery is a well-known security attack that is listed in OWASP security risks. CSRF is…*](https://medium.com/@jude.niroshan11/what-is-csrf-synchronizer-token-pattern-3b244791ab4b)

### SameSite Cookies ✓

Setting the `SameSite`[ cookie attribute](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite) to `Lax` or even `Strict` can help to prevent CSRF attacks. The idea is to tell the browser that the cookie should only be sent when the request originates from the same site.

The SameSite attribute is [supported by all relevant browsers](https://caniuse.com/same-site-cookie-attribute).

### Bearer Tokens ✓

CSRF is only possible if the browser automatically authenticates. For bearer tokens (JWT), the application has to create that header. So CSRF is not possible.

### Only accept state-changes via POST requests ❌

The attacker can add a form with `method=POST` on the evil.com page. The form is submitted via `onclick` on a link on the page.

### Multi-Factor authentication ❌

MFA or 2FA only helps if you have to do it for every request. And then I would rather call it an authorization mechanism.

If your bank wants a TAN for every transaction, this helps. If your bank just requires you to use the app on your smartphone to sign in, it doesn’t help. The attack targets requests, not the sign-in.

### Same-Origin Policy ❌

[The Same-Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) prevents pages that embed an iframe to read the cookie of the embedded page, except if they are from the same origin.

The point of Same-Origin Policy (SOP) is to prevent leaking data. Reading data is blocked, but sending data is not affected.

### Referrer-Headers ❌

Referrer-Headers might get stripped away by the browser for privacy reasons. For this reason, filtering on referrer-headers might affect normal users.

### As a user …

… you can log out when you’re finished using one account.

You could also use one browser for trustworthy content and another one for non-trustworthy content. But let’s be honest: Who will really do that?

## See also

The YouTube Channel [PwnFunction](https://www.youtube.com/channel/UCW6MNdOsqv2E9AjQkv9we7A) contains an awesome video that summarizes the topic. [OWASP](https://owasp.org/www-community/attacks/csrf) and [PortSwigger](https://portswigger.net/web-security/csrf) contain good articles as well.

<iframe width="560" height="315" src="https://www.youtube.com/embed/eWEgUcHPle0" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

<!-- series: appsec -->
