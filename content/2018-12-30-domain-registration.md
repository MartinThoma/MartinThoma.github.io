---
layout: post
title: Domain Registration
slug: domain-registration
author: Martin Thoma
date: 2018-12-30 20:00
category: Cyberculture
tags: domain, Internet
featured_image: logos/internet.png
---
<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>
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

```shell
$ whois martin-thoma.com
   Domain Name: MARTIN-THOMA.COM
   Registry Domain ID: 1678176835_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.namecheap.com
   Registrar URL: http://www.namecheap.com
   Updated Date: 2018-01-25T12:13:13Z
   Creation Date: 2011-09-21T08:11:13Z
   Registry Expiry Date: 2024-09-21T08:11:13Z
   Registrar: NameCheap, Inc.
   Registrar IANA ID: 1068
   Registrar Abuse Contact Email: abuse@namecheap.com
   Registrar Abuse Contact Phone: +1.6613102107
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Name Server: AMY.NS.CLOUDFLARE.COM
   Name Server: KAI.NS.CLOUDFLARE.COM
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2019-02-07T21:00:04Z <<<
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
