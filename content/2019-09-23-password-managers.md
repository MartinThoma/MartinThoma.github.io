---
layout: post
title: Password Managers
slug: password-managers
author: Martin Thoma
status: draft
date: 2019-09-23 20:00
category: My bits and bytes
tags: IT Security, password
featured_image: logos/star.png
---
A few days ago I had a small argument with my girlfriend, because she keeps
forgetting her passwords. This made me think about good solutions for passwords
in general. I have found one with which I was ok for a while, but more and more
services get compromised. Try [haveibeenpwned.com](https://haveibeenpwned.com/) or [Firefox Monitor](https://monitor.firefox.com/) to see if you are affected. One easy way
to keep the damage small is not to re-use passwords. It is impractical to have
strong passwords for every web service I use. I have to either use a password
service or note things down.

A good way of creating a single strong password is [diceware](https://www.youtube.com/watch?v=Pe_3cFuSw1E). Once you have this, you should create a new password for
every single service and keep it in your password manager.

This article focuses on what a good password manager is. I will judge them in
three categories:

* **Security**: Are the passwords locally encrypted strong enough? How many
  incidents happened so far? Does it support 2FA / MFA?
* **Usability**: Is it convenient to use? Is it available on Linux and Android?
  Can I use it outside of the browser (e.g. if the password field is not
  detected). Does it have an UI for generating strong random passwords when
  creating a new account?
* **Long-Term Support**: Is this backed by a (bigger) company / a team of
  developers? Is ther vendor-locking?


## Google Smart Lock

[Google Smart Lock](https://support.google.com/accounts/answer/6197437?hl=en&visit_id=637048670466644275-4172869288&rd=1) is another password manager. If you use Google Chrome, chances are high that you are already using it.

## LastPass

[LastPass](https://en.wikipedia.org/wiki/LastPass) is developed by LogMeIn
since 2015. The initial release was in 2008.

### Security

The wikipedia page lists four security incidents and one security breach:

* 2011: Network anomaly; unclear if anything actually happened.
* 2015: LastPass account email addresses, password reminders, server per user
  salts, and authentication hashes were compromised; however, encrypted user
  vault data had not been affected.
* 2016: Detectify and Google Security found an issue in URL parsing
* 2017: [Tavis Ormandy](https://en.wikipedia.org/wiki/Tavis_Ormandy) (Google Security / Project Zero) found another issue in the
  browser extension
* 2019: [Password-exposing bug purged from LastPass extensions](https://arstechnica.com/information-technology/2019/09/lastpass-fixes-bug-that-leaked-the-password-of-last-logged-in-account/), [Tweet](https://twitter.com/taviso/status/1173401754257375232)

The advantage compared to Google Smart Lock are:

* You don't use Google
* LastPass has

### Usability

[Supported Clients](https://lastpass.com/misc_download2.php):

* [Linux](https://lastpass.com/lplinux.php)
* Desktop: [Chrome](https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd?hl=de), [Firefox](https://lastpass.com/lastpassffx/)
* Mobile: [Android](https://play.google.com/store/apps/details?id=com.lastpass.lpandroid&hl=de)


### Long-Term Support

LogMeIn has 2778 employees and a revenue of over 1 billion USD.

According to their website, they have over 16 million users and 58000 companies.[^1]
It costs 2.67 EUR/month.


## KeePass

[KeePass](https://en.wikipedia.org/wiki/KeePass) is developed by Dominik Reichl.
It is free and open source.


## KeePassX

[KeePassX](https://en.wikipedia.org/wiki/KeePassX) started in 2016 as a port of KeePass to Linux. The [code is on Github](https://github.com/keepassx/keepassx) and it has
4063 stars and 591 forks. It's mostly C++.

The last version was released in 2016, so about 3 years ago. **KeePassX is not maintained**.[^2]

## KeePassXC

[KeePassXC](https://en.wikipedia.org/wiki/KeePassXC) is a fork of KeePassX


## Dashlane

[Dashlane](https://en.wikipedia.org/wiki/Dashlane) was initially released in 2012


## See also

* [Keeper](https://en.wikipedia.org/wiki/Keeper_(password_manager)): [Security incident](https://twitter.com/taviso/status/941710362717470720)
* 1Password
* Martin Monperrus: [What's the difference between KeePass and KeePassX?](https://superuser.com/q/878902/64857), February 2017.
* Wikipedia: [List of password managers](https://en.wikipedia.org/wiki/List_of_password_managers)
* [KeeWeb](https://keeweb.info/)


## Footnotes

[^1]: [LastPass: Frequently asked questions](https://www.lastpass.com/de/pricing), downloaded 2019-09-23.
[^2]: Reddit: [KeePass vs KeePassX](https://www.reddit.com/r/privacy/comments/6inegj/keepass_vs_keepassx/), 2017.
