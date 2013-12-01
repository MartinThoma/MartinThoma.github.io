---
layout: post
status: publish
published: true
title: CMOS circuits
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 56701
wordpress_url: http://martin-thoma.com/?p=56701
date: 2013-02-08 23:39:26.000000000 +01:00
categories:
- Cyberculture
tags:
- Digitaltechnik
- CMOS
- MOSFET
- digital circuit
comments:
- id: 1136491
  author: Stefan Koch
  author_email: blog@stefan-koch.name
  author_url: http://stefan-koch.name/
  date: !binary |-
    MjAxMy0wMi0wOSAwOTozNzo1NyArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMi0wOSAwODozNzo1NyArMDEwMA==
  content: Ich wei&szlig; im Moment nicht mehr, was die durchgezogenen Linien waren,
    aber mein &Auml;hnlichkeitssinn sagt mir, dass das zweite Bild bei "depletion"
    auch einen durchgezogenen Strich haben sollte.
- id: 1137301
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wMi0xMyAwODoyMTowMyArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMi0xMyAwNzoyMTowMyArMDEwMA==
  content: Dein &Auml;hnlichkeitssinn. So so. Mir sagt es die Bild-URL, die zwei mal
    vorkommt :-) Wurde korrigiert.
featured_image: 2013/02/cmos-nand-thumbnail.jpg
---
CMOS is a technology used to create digital circuits. The basic idea is to combine a pMOS circuit and a nMOS circuit.

<h2>MOSFET</h2>
Four <abbr title="metal&ndash;oxide&ndash;semiconductor field-effect transistor">MOSFET</abbr> are important for CMOS:

<table>
<tr>
  <th>&nbsp;</th>
  <th>nMOS</th>
  <th>pMOS</th>
</tr>
<tr>
<th>depletion</th>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2013/02/nmos-selbstsleitend.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/nmos-selbstsleitend.jpg" alt="nMOS - depletion type" width="222" height="174" class="size-full wp-image-56741" /></a></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2013/02/pmos-selbstsleitend.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/pmos-selbstsleitend.jpg" alt="pMOS depletion" width="215" height="181" class="size-full wp-image-56761" /></a></td>
</tr>
<tr>
<th>enhancement</th>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2013/02/nmos-selbstsperrend.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/nmos-selbstsperrend.jpg" alt="nMOS - enhancement type" width="221" height="171" class="size-full wp-image-56751" /></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2013/02/pmos-selbstsperrend.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/pmos-selbstsperrend.jpg" alt="pMOS - enhancement type" width="181" height="163" class="size-full wp-image-56771" /></a></td>
</tr>
</table>

<h2>Inverter</h2>
[caption id="attachment_56721" align="aligncenter" width="434"]<a href="http://martin-thoma.com/wp-content/uploads/2013/02/cmos-inverter.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/cmos-inverter.jpg" alt="Inverter in CMOS technology" width="434" height="512" class="size-full wp-image-56721" /></a> Inverter in CMOS technology[/caption]

<h2>NAND</h2>
[caption id="attachment_56731" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2013/02/cmos-nand.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/cmos-nand.jpg" alt="NAND gate in CMOS technology" width="512" height="488" class="size-full wp-image-56731" /></a> NAND gate in CMOS technology[/caption]

<h2>Images</h2>
I tried to find good software to create those images. I didn't find any that allowed me to create those images. I've tried this:

<ul>
  <li><a href="http://wwwu.uni-klu.ac.at/magostin/cirkuit.html">Cirkuit</a>: Looks good, but crashes.</li>
  <li>EAGLE: too complex</li>
  <li>KLogic: seems only to be able to create logic plans</li>
  <li>PCB Designer: too complex, weird interface</li>
</ul>

<h2>Anything else?</h2>
Which other circuits do we have to know? (Perhaps Transmission Gate?)
