---
layout: post
title: Famous Software Bugs
author: Martin Thoma
date: 2013-11-23 12:37:19
categories: 
- Cyberculture
tags: []
featured_image: 2012/06/mars-climate-orbiter.jpg
---
<h2>Mars Climate Oribiter</h2>
[caption id="attachment_28651" align="alignright" width="128"]<a href="http://martin-thoma.com/wp-content/uploads/2012/06/mars-climate-orbiter.jpg"><img class="size-full wp-image-28651 " title="Mars Climate Oribiter" src="http://martin-thoma.com/wp-content/uploads/2012/06/mars-climate-orbiter.jpg" alt="Mars Climate Oribiter" width="128" height="128" /></a> Mars Climate Oribiter[/caption]
<strong>Type of Bug</strong>: Bad specification
<strong>Description</strong>:  The flight system software on the Mars Climate Orbiter was written to calculate thruster performance using the <em>metric unit</em> Newtons (N), while the ground crew was entering course correction and thruster data using the <em>Imperial measure</em> Pound-force (lbf).
<strong>Outcome</strong>: The cost of the mission was $327.6 million total for both orbiter and lander, $193.1 million for spacecraft development, $91.7 million for launching it, and $42.8 million for mission operations.
<strong>Source</strong>: <a href="http://en.wikipedia.org/wiki/Mars_Climate_Orbiter">Wikipedia</a>

<h2>Ariane V88</h2>
<iframe width="512" height="384" src="http://www.youtube.com/embed/kYUrqdUyEpI" frameborder="0" allowfullscreen></iframe>

The <a href="http://de.wikipedia.org/wiki/Ariane_V88">Ariane V88</a> exploded 40 seconds after its start.

<strong>Type of Bug</strong>: The software was written for another type of hardware
<strong>Description</strong>: A 64 Bit floating point number was converted into a 16 bit integer in the "inertial reference system" → Overflow → the rocket got into a tilted position and destroyed itself for security reasons. The interesting part is, that this program wasn't even needed for the flight! It had been developed for the Ariane 4.
<strong>Outcome</strong>: 290 Million Euro destroyed



http://www.codinghorror.com/blog/2009/11/whitespace-the-silent-killer.html
http://bugsniffer.blogspot.de/2007/11/infamous-software-failures.html
https://www.google.com/search?q=failure+'missing+semicolon'
http://www.ual.es/~plopez/docencia/itis/patriot.htm