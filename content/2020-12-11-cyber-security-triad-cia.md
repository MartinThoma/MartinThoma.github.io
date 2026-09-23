---
layout: post
title: The Cyber Security Triad
slug: cyber-security-triad-cia
lang: en
author: Martin Thoma
date: 2020-12-11 20:00
category: Security
tags: Security
featured_image: logos/cybersecurity.png
subtitle: It’s the CIA 🕵 — but maybe not what you think
medium_url: https://medium.com/plain-and-simple/the-cyber-security-triad-df9911f85955
---

The Cyber Security Triad, also called the CIA triad, is a set of three goals:

* **Confidentiality**: Information or resources can only be accessed by
  authorized parties.
* **Integrity**: Information can only be added, edited, or removed by
  authorized parties.
* **Availability**: Systems are available to their users according to the
  service level agreements (SLAs).

![A triangle with Confidentiality at the apex and Integrity and Availability at the base corners](../images/2020/12/cia-triad.svg)*The three goals of the CIA triad. Image by Martin Thoma*

## Email Example

* **Confidentiality**: Ideally, only the sender and the receiver can read an email. (Without end-to-end encryption, the mail providers can read it as well.)
* **Integrity**: Only you can delete emails you received. Nobody can edit the
  emails you received.
* **Availability**: You can read emails in your inbox whenever you want.

## WhatsApp Example

Let’s ignore groups for the moment.

* **Confidentiality**: Only the sender and the receiver can read a message.
* **Integrity**: Only you can delete messages you received, with the exception
  of messages you haven’t read / which are not older than a certain time.
  Nobody can edit the messages you received.
* **Availability**: You can read your messages whenever you want.

Please note that the integrity criterion is different for WhatsApp compared to
email! This shows that the meaning of the criterion depends on the context.
Similarly, availability in many business applications can mean “available at
typical business hours”.
