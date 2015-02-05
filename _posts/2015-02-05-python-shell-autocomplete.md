---
layout: post
title: Python Shell autocomplete
author: Martin Thoma
date: 2015-02-05 09:58
categories: 
- Code
tags: 
- Python
- Shell
featured_image: logos/python.png
---
One feature I really miss in Pythons interactive shell is tab autocompletion.
Thanks to [blog.e-shell.org](http://blog.e-shell.org/221) I know how to get it:

```python
>>> import rlcompleter, readline
>>> readline.parse_and_bind('tab:complete')
>>> smtplib.
smtplib.CRLF                      smtplib.__getattribute__(
smtplib.LMTP                      smtplib.__hash__(
smtplib.LMTP_PORT                 smtplib.__init__(
smtplib.OLDSTYLE_AUTH             smtplib.__name__
smtplib.SMTP                      smtplib.__new__(
smtplib.SMTPAuthenticationError(  smtplib.__package__
smtplib.SMTPConnectError(         smtplib.__reduce__(
smtplib.SMTPDataError(            smtplib.__reduce_ex__(
smtplib.SMTPException(            smtplib.__repr__(
smtplib.SMTPHeloError(            smtplib.__setattr__(
smtplib.SMTPRecipientsRefused(    smtplib.__sizeof__(
smtplib.SMTPResponseException(    smtplib.__str__(
smtplib.SMTPSenderRefused(        smtplib.__subclasshook__(
smtplib.SMTPServerDisconnected(   smtplib._addr_only(
smtplib.SMTP_PORT                 smtplib._have_ssl
smtplib.SMTP_SSL                  smtplib.base64
smtplib.SMTP_SSL_PORT             smtplib.email
smtplib.SSLFakeFile               smtplib.encode_base64(
smtplib.__all__                   smtplib.hmac
smtplib.__class__(                smtplib.quoteaddr(
smtplib.__delattr__(              smtplib.quotedata(
smtplib.__dict__                  smtplib.re
smtplib.__doc__                   smtplib.socket
smtplib.__file__                  smtplib.ssl
smtplib.__format__(               smtplib.stderr
```

Now if you want to always have that, you can get it by editing your
`~/.pythonrc`:

```python
import rlcompleter, readline
readline.parse_and_bind('tab:complete')
```

You also have to make sure that the environment variable `PYTHONSTARTUP` is set to
`~/.pythonrc`. In my case, I had to add the line `export PYTHONSTARTUP=~/.pythonrc`
to `~/.zshrc`.

I have also seen that there is another, "more powerful", Python shell called
ipython. However, I don't understand how this shell supports autocompletion
(see [How does ipython3 import autocomplete work?](http://stackoverflow.com/q/28329269/562769)).