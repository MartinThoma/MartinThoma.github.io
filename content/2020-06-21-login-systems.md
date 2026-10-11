---
layout: post
title: Login Systems
slug: login-systems
lang: en
author: Martin Thoma
date: 2019-06-21 20:00
category: My bits and bytes
tags: Security, Software Engineering, Web Development
featured_image: logos/star.png
status: draft
---
Authentication is one core component of all web communities. While building
enzado, I started thinking about it in detail. Login, registration and password reset look like solved problems, but
there are many small things that decide whether users can log in smoothly and
whether attackers can't.

This article is about the forms and flows. How passwords are stored is in
[Password Hashing](../password-hashing/); second factors are in
[Multi-Factor Authentication](../multi-factor-authentication/).


## HTML

Password managers and browsers fill forms based on the HTML. If they guess
wrong, users have to copy and paste passwords, choose weak ones, or give up.
The `autocomplete` attribute tells them what each field is
([MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)).

### Login

```html
<form method="post" action="/login">
  <label for="username">Email</label>
  <input id="username" name="username" type="email"
         autocomplete="username" required>

  <label for="password">Password</label>
  <input id="password" name="password" type="password"
         autocomplete="current-password" required>

  <button type="submit">Log in</button>
</form>
```

* Use `autocomplete="username"` for the identifier, even if it is an email
  address, and `current-password` for the password.
* Use a real `<form>` with a submit button. Password managers detect a login
  when the form is submitted.
* Use `type="email"` for email addresses: mobile keyboards show the `@`.
* Don't block pasting into password fields. It only hurts people who use a
  password manager.
* Give a generic error message: "Email or password is wrong". Saying which one
  is wrong tells attackers which accounts exist.
* If the login is split into two steps (identifier first, password second),
  put the identifier into a hidden field with `autocomplete="username"` on the
  second page, so the password manager knows which account it is.

### Registration

* Use `autocomplete="new-password"` for the password field. Browsers then
  suggest a strong, generated password.
* Allow long passwords and all characters, including spaces. Check new
  passwords against lists of breached passwords instead of enforcing
  composition rules such as "one digit, one special character". This is also
  what NIST recommends ([SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html)).
* Don't ask for the password twice if users can see it: a "show password"
  toggle prevents typos better.

### Reset Password

Make sure to use the `autocomplete="new-password"` for the new password fields
(for both the same).

The flow itself:

1. The user enters their email address. Always answer "If an account exists,
   we sent you an email", whether the address is known or not.
2. Send a link with a random, single-use token that expires after a short time
   (minutes to an hour). Store only a hash of the token.
3. On the reset page, ask for the new password, set it, invalidate the token
   and end all existing sessions of the account.
4. Notify the user by email that the password was changed.

The [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
describes this in detail.


## Server side

* **Rate limiting.** Limit login attempts per account and per IP address. This
  slows down password guessing and [credential stuffing](../credential-stuffing/).
* **Sessions.** After a successful login, create a new session ID (prevents
  session fixation). Set the cookie with `Secure`, `HttpOnly` and
  `SameSite=Lax`.
* **Logout** must invalidate the session on the server, not only delete the
  cookie.
* **Logging.** Log failed and successful logins, so suspicious patterns can be
  detected, but never log passwords.


## Without passwords

Passwords are not the only option:

* **Magic links**: the user enters an email address and clicks a link. Easy, but
  only as safe as the email account, and annoying when the email arrives late.
* **Login with an existing account** (OpenID Connect, "Sign in with Google"):
  no password to manage for you, but a dependency on the provider.
* **Passkeys** ([WebAuthn](https://www.w3.org/TR/webauthn-2/)): a key pair on the
  user's device, unlocked by fingerprint, face or PIN. They are bound to the
  domain, so phishing doesn't work.


## See also

* [Authentication](https://en.wikipedia.org/wiki/Authentication)
* [Making password managers play ball with your login form](https://hidde.blog/making-password-managers-play-ball-with-your-login-form/)
* [Hints by 1Password](https://support.1password.com/compatible-website-design/)
* [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
* [Password Managers](../password-managers/)
* [Identification vs Authentication vs Authorization](../identification-authentication-authorization/)
