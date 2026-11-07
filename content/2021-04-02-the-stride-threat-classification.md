---
layout: post
title: The STRIDE Threat Classification
slug: the-stride-threat-classification
lang: en
author: Martin Thoma
date: 2021-04-02 18:02
category: Security
tags: Security, AppSec
featured_image: logos/cybersecurity.png
summary: STRIDE is a model which categorizes threats into 6 groups.
medium_url: https://medium.com/@martinthoma/the-stride-threat-classification-33f3808b7158
---
<figure>
    <a href="../images/2021/04/the-stride-threat-classification-1.png"><img src="../images/2021/04/the-stride-threat-classification-1.png" alt="The letters S, T, R, I, D, E in colored boxes, labeled Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service and Elevation of Privilege" width="800" height="221"></a>
    <figcaption>Image by Martin Thoma</figcaption>
</figure>

STRIDE is an acronym for:

* **Spoofing**: Impersonating someone else; e.g. [email spoofing](../email-spoofing/). A common example is the [grandparent scam](https://en.wikipedia.org/wiki/List_of_confidence_tricks#Persuasion_tricks). Spoofing breaks Authenticity.
* **Tampering**: Modifying data or code; e.g. manipulating the data sent by the browser. A non-digital tampering attack is when you look at your children's yearly school report and they changed the grades. Tampering breaks Integrity.
* **Repudiation**: Claim you didn’t send an email / perform a transaction/edit that Wikipedia page. Repudiation breaks non-repudiability.
* **Information Disclosure**: A privacy breach or a data leak. Information Disclosure breaks Confidentiality.
* **Denial of Service**: e.g. uploading big files to a service; causing heavy computation; pinging the server to overload the network; [ZIP bombs](../zip-bombs/); [A billion laughs](../billion-laughs-dos/). Denial of Service breaks availability.
* **Elevation of privilege**: e.g. [SQL Injection](../sql-injections/). Elevation of privilege breaks authorization.
