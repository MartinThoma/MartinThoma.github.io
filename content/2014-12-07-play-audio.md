---
layout: post
lang: en
title: Play Audio
slug: play-audio
author: Martin Thoma
date: 2014-12-07 00:31
category: Cyberculture
tags: Audio, Senses, HTML5
featured_image: logos/signal.png
---
Our senses have a limited capability to distinguish signals. This might not be
surpristing. However, we also have a limited capability to tell in which
order signals arrived at our sensory organs.

As I learned this, I wanted to check it. I wrote a little JavaScript / HTML5
page where you can check it. You can adjust the time in which two sounds are
played. The clicking noise is played on the left and the right speaker in
random order. A textfield below shows which speaker played the sound first.

You should use headphones for this demo.

According to the KIT lecture "Mensch-Maschine-Wechselwirkung in der Anthropomatik (Vorlesung Universität Karlsruhe im KIT, WS 2013/14, J. Geisler)", the time resolution of the human ear is
between 2 and 5 ms. This means you will not be able to distinguish the two
signlas for less than 2ms. But you will need the signals to be 30-40ms apart
to tell which one played first.

I rather need 10ms, but this might also be caused by hardware problems. I doubt
that JavaScripts `timeout` is accurate enough.

<h2>Audio Test</h2>
<audio id="left_channel" src="//martin-thoma.com/audio/click_left.wav" preload="auto"></audio>
<audio id="right_channel" src="//martin-thoma.com/audio/click_right.wav" preload="auto"></audio>
<a href="javascript:play_sound();">Play sound</a>
<input type="number" id="seconds" name="seconds" value="20" /> ms
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<h2>Which was first</h2>
<p id="results"></p>
<script type="text/javascript" src="//martin-thoma.com/js/playsounds.js"></script>
