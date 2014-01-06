---
layout: post
title: CMOS circuits
author: Martin Thoma
date: 2013-02-08 23:39:26.000000000 +01:00
categories:
- Cyberculture
tags:
- Digitaltechnik
- CMOS
- MOSFET
- digital circuit
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
  <td><a href="../images/2013/02/nmos-selbstsleitend.jpg"><img src="../images/2013/02/nmos-selbstsleitend.jpg" alt="nMOS - depletion type" width="222" height="174" class="size-full wp-image-56741" /></a></td>
  <td><a href="../images/2013/02/pmos-selbstsleitend.jpg"><img src="../images/2013/02/pmos-selbstsleitend.jpg" alt="pMOS depletion" width="215" height="181" class="size-full wp-image-56761" /></a></td>
</tr>
<tr>
<th>enhancement</th>
  <td><a href="../images/2013/02/nmos-selbstsperrend.jpg"><img src="../images/2013/02/nmos-selbstsperrend.jpg" alt="nMOS - enhancement type" width="221" height="171" class="size-full wp-image-56751" /></td>
  <td><a href="../images/2013/02/pmos-selbstsperrend.jpg"><img src="../images/2013/02/pmos-selbstsperrend.jpg" alt="pMOS - enhancement type" width="181" height="163" class="size-full wp-image-56771" /></a></td>
</tr>
</table>

<h2>Inverter</h2>
{% caption align="aligncenter" width="434" caption="Inverter in CMOS technology" url="../images/2013/02/cmos-inverter.jpg" alt="Inverter in CMOS technology"  height="512" class="size-full wp-image-56721" %}

<h2>NAND</h2>
{% caption align="aligncenter" width="512" caption="NAND gate in CMOS technology" url="../images/2013/02/cmos-nand.jpg" alt="NAND gate in CMOS technology"  height="488" class="size-full wp-image-56731" %}

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
