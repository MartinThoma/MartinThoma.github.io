---
layout: post
title: Domain Registration
slug: domain-registration
author: Martin Thoma
status: draft
date: 2017-02-25 20:00
category: Cyberculture
tags: domain, Internet
featured_image: logos/internet.png
---
The registration of domains (such as `martin-thoma.com`,
`wikipedia.org`, `understand.ai`, `unicode.party`, …) is kind of broken.
There are people who register domains just because somebody might want them
sometime. Then they sell it to them. They do not intend to put content there.
This is called "domain parking". I guess it is similar to people who put their
car on a parking spot which they actually don't need. Then they put a sign
in there "if you want to park here, pay 20 Euro and call XYZ".

Why is this a problem (though not a too serious one)?

For physical goods people who buy stuff just because they think in future other
people might need it provides value. It smoothes the price over time, allows
the producers of that good to continue producing it while somebody else takes
care of storing it.

However, for rights it is different. There is only one domain like `comment.it`.
There will never be another one. There is no smoothing of the price over time
(as it can only be bought once). If it is not registered, there is no cost in
holding it available. In contrast, it is much more complicated to buy a domain
which is already registered by somebody else than registering it yourself.


## Whois Lookup

With sites like <a href="http://whois.domaintools.com/">whois.domaintools.com</a>
or tools like `whois` you can look up who owns a domain:

```
$ whois comment.it

*********************************************************************
* Please note that the following result could be a subgroup of      *
* the data contained in the database.                               *
*                                                                   *
* Additional information can be visualized at:                      *
* http://www.nic.it/cgi-bin/Whois/whois.cgi                         *
*********************************************************************

Domain:             comment.it
Status:             ok
Created:            2001-01-24 00:00:00
Last Update:        2017-01-08 00:41:49
Expire Date:        2017-12-23

Registrant
  Organization:     Valerio Morfino

Admin Contact
  Name:             Valerio Morfino
  Organization:     Valerio Morfino

Technical Contacts
  Name:             Tophost Srl > Registra il tuo dominio con www.tophost.it
  Organization:     Tophost Srl > L'hosting più conveniente d'Italia

Registrar
  Organization:     Seeweb S.r.l.
  Name:             TOPHOST-REG
  Web:              http://www.tophost.it

Nameservers
  ns1.th.seeweb.it
  ns2.th.seeweb.it

```


## Examples

Here is a list of interesting domains which are just held for the purpose of
selling it too expensive to somebody else:

* <a href="http://comment.it/">comment.it</a> (<a href="http://whois.domaintools.com/comment.it">whois</a>): Registered by Valerio Morfino in 2001
* <a href="http://admin.ai/">admin.ai</a> (<a href="http://whois.domaintools.com/admin.ai">whois</a>): Registered by SenseiHub in 2010
* <a href="http://face.it/">face.it</a>: Registered by Gianfranco Zanella in 2003
* <a href="http://detect.it/">detect.it</a>: Registered by Macrosten LTD in 2011
* <a href="https://ocr.ai/">ocr.ai</a>: Registered by DMS AI (at least in 2017)
* <a href="http://digitalize.it/">digitalize.it</a>: Registered by Vito Longo in 2015
* <a href="http://scan.it/">scan.it</a>: Registered by Luca Sambucci in 1999
* <a href="http://data.science/">data.science</a>: Registered by Alpnames Limited in 2014

And a couple of examples where I'm not too sure:

* <a href="http://ai.data/">ai.data</a>: This is strange. I get an Apache2 default page, but I can't find a WHOIS record
* <a href="http://comment.ai/">comment.ai</a> (<a href="http://whois.domaintools.com/comment.ai">whois</a>): Registered by Benjamin Milde in 2001


## Misc

I came across some interesting examples:

* <a href="http://stalk.com/">stalk.com</a>: I guess this can be used for training a model to find the geolocation just by image data?
* <a href="http://personal.id/">personal.id</a>
