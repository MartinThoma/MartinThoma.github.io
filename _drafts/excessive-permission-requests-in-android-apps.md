---
layout: post
title: Excessive Permission Requests in Android Apps
author: Martin Thoma
date: 2013-03-14 10:20:56
categories: 
- The Web
tags: 
- Android
featured_image: 2013/03/android-thumb.png
---
Some days ago I got <a href="http://martin-thoma.com/nexus-4/" title="Nexus 4">my first Android device</a>. Of course, I've installed some apps and I've noticed a problem with many apps: They request too many rights. It's quite difficult for a customer to decide if permission requests are ok.

<h2>Permissions - When they are necessary</h2>
<table>
  <tr>
    <th>Full Internet Access</th>
    <td>The app might have advertisement</td>
  </tr>
  <tr>
    <th>Read Phone State and Identity</th>
    <td>Necessary for games. You want the game to pause, when you get a call, don't you?</td>
  </tr>
</table>

<h2>Bahn-App</h2>
The App <a href="https://play.google.com/store/apps/details?id=de.hafas.android.db&feature=search_result">DB Navigator</a>

<table>
  <tr>
    <th style="background-color:yellow;">approximate location (network-based)</th>
    <td>that's ok, maybe the app wants to present my following train</td>
  </tr>
  <tr>
    <th style="background-color:yellow;">precise location (GPS and network-based)</th>
    <td>hmm ... does the app guide me to the platform? It would be ok if it does so.</td>
  </tr>
  <tr>
    <th style="background-color:lime;">full network access</th>
    <td>the app needs to receive the latest information for the train</td>
  </tr>
  <tr>
    <th>read calendar events plus confidential information</th>
    <td></td>
  </tr>
  <tr>
    <th>add or modify calendar events and send email to guests without owners' knowledge</th>
    <td></td>
  </tr>
  <tr>
    <th>read your contacts</th>
    <td></td>
  </tr>
  <tr>
    <th>modify or delete the contents of your USB storage modify or delete the contents of your SD card</th>
    <td></td>
  </tr>
</table>

<h2>AirDroid</h2>
https://play.google.com/store/apps/details?id=com.sand.airdroid&feature=search_result#?t=W251bGwsMSwxLDEsImNvbS5zYW5kLmFpcmRyb2lkIl0.

<h2>Tiny Flashlight</h2>
https://play.google.com/store/apps/details?id=com.devuni.flashlight&feature=search_result#?t=W251bGwsMSwxLDEsImNvbS5kZXZ1bmkuZmxhc2hsaWdodCJd

<h2>OpenSignal</h2>
https://play.google.com/store/apps/details?id=com.staircase3.opensignal

<h2>WiFi finder</h2>
https://play.google.com/store/apps/details?id=com.jiwire.android.finder&feature=search_result

<h2>Certificates</h2>
<h3>Trusted App</h3>
http://www.mediatest-digital.com/downloads/mTd_Factsheet_TrustedApp.pdf

<h3>Trust Go</h3>
http://www.trustgo.com/en/

<h2>Further reading</h2>
<ul>
  <li><a href="http://droid.usedavesvoice.com/android-app-permissions-when-should-you-worry/">Android App Permissions: When Should You Worry?</a></li>
  <li><a href="http://developer.android.com/reference/android/Manifest.permission.html">Manifest.permission</a> - What developers can use</li>
  <li><a href="https://play.google.com/store/apps/details?id=com.a0soft.gphone.aSpotCat&hl=de">aSpotCat</a>: An App that finds other apps on your phone that might cost you money. I think this should be built-in the Android Market.</li>
</ul>