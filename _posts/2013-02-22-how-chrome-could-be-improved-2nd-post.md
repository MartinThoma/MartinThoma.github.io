---
layout: post
title: How Chrome could be improved - 2nd Post
author: Martin Thoma
date: 2013-02-22 09:55:07.000000000 +01:00
category: Cyberculture
tags: Browser, Chrome
featured_image: 2012/04/google-chrome-logo.png
---
Chrome 25 was just released and I would like to mention some features I am still missing. As I already wrote an article <a href="../how-chrome-could-be-improved/">How Chrome could be improved</a> for Chrome 18 I will also mention what  was realised meanwhile. If you're curious if you have the current version, just visit <a href="chrome://chrome/">chrome://chrome/</a>.

<h2>Caps lock indicator for password fields</h2>
It's annoying to have caps lock on while typing passwords. So an indicator is needed.

I would prefer a caps icon indicator solution:
{% caption align="alignnone" width="160" caption="Password field caps icon indicator" url="../images/2013/02/password-field-caps-icon-indicator.png" alt="Password field caps icon indicator"  height="29" class="size-full wp-image-76613" %}

Another way to indicate it would be by text:
{% caption align="alignnone" width="236" caption="Password field caps lock warning" url="../images/2013/02/password-field-caps-warning.png" alt="Password field caps lock warning"  height="67" class="size-full wp-image-76614" %}

<h2>Improve MathML support</h2>
Chrome uses WebKit and WebKit didn't support MathML for quite a long time. A quite good work-around is <a href="http://www.mathjax.org/">MathJax</a>, but it is a work-around. Native support would be nice. With Chrome 24, they have added MathML support, but its still not optimal:
<ul>
  <li>The font doesn't look very nice (see <a href="http://www.mozilla.org/projects/mathml/demo/texvsmml.html">MathML Torture Test</a> and image below)</li>
  <li>Multiscripts seems not to work</li>
  <li>big brackets get a whitespace in the middle (see image below)</li>
  <li>Scriptlevel seems not to work (see <a href="https://eyeasme.com/Joe/MathML/MathML_browser_test">MathML Browser test</a>)</li>
</ul>

Here is an image where you can see some of the problems:
{% caption align="aligncenter" width="621" caption="MathML rendered with Chrome 24" url="../images/2013/01/mathml-chrome24-rendering.png" alt="MathML rendered with Chrome 24"  height="60" class="size-full wp-image-53981" %}

In Chrome 25, MathML was deactivated.

<ul>
  <li><a href="http://caniuse.com/mathml">Which Browsers support MathML?</a></li>
  <li><a href="http://www.w3.org/Math/XSL/csmall2.xml">Test page</a></li>
  <li><a href="http://html5test.com/">HTML5test.com</a> - Chrome seems to cheat, MathML is not supported as you can see on the test page. Chrome 25 scores 448/500 Points and 13 bonus points.</li>
  <li><a href="https://trac.webkit.org/wiki/MathML">Webkit MathML project</a>, <a href="https://bugs.webkit.org/show_bug.cgi?id=3251">Webkit MathML master bug</a></li>
</ul>

<h2>Stop Animations</h2>
Sometimes I would like to be able to stop animations. It can be very useful to be able to stop animations if you want to explain something in the animation. For example, <a href="http://de.wikipedia.org/wiki/Kurvenintegral#Kurvenintegral_erster_Art">this page on Wikipedia</a> has some animations. If you give private lessons in math to another person, you might want to tell something to the single images of the animation. But I am quite sure, that you can't speak that fast.

It would also be nice if you were able to stop all animations on the page. Regrettably, some webmasters carry the usage of animations to excess.

<h2>What do I still miss?</h2>
<h3>Disable sound for tabs</h3>
Sometimes I watch a movie while I play a flash game. Some flash games don't offer an option to mute them. So I would like to get the possibility to disable sound for one tab.

It could look like this.
{% caption align="aligncenter" width="300" caption="Disable the sound of a tab" url="../images/2012/04/disable-tab-sound-300x172.png" alt="Disable the sound of a tab"  height="172" class="size-medium wp-image-20981" %}

UPDATE: This is <a href="https://code.google.com/p/chromium/issues/detail?id=3541">issue 3541</a>.

<h3>Spell checker</h3>
I write Blogs in German and in English. So I would like a spell-checker option at the bottom-left corner to switch languages:
{% caption align="aligncenter" width="698" caption="Spell checker" url="../images/2012/04/spell-checker.png" alt="Spell checker"  height="91" class="size-full wp-image-21021" %}

<h3>PDF page numbers</h3>
It would be great, if I could see the number of the page your currently on. Sometimes PDF-Documents don't even have numbers (e.g. LaTeX beamer slides). What do you do if you have a question to one slide if there are dozens of slides? Manually count them, to get the page number you're looking for?

<strong>UPDATE</strong>: You actually can jump to any page and share it as links! You only have to add <code>#page=123</code>.
For example, you can take a look at this <a href="http://paws.wcu.edu/tsfoguel/tikzpgfmanual.pdf#page231">huge TikZ PDF manual</a>. 

<strong>UPDATE2</strong>: You could automatically adjust this <code>#page=123</code> string according to the page that gets currently viewed. This would make sharing much easier and it would fix the issue that you don't know where you. Another advantage of this solution is that it doesn't bloat up the user interface.

<strong>UPDATE3</strong>: I finally found it! It's <a href="https://code.google.com/p/chromium/issues/detail?id=66900">issue 66900</a>

<h3>Security</h3>
<h4>Disabling Extensions</h4>
Auto-Disable extensions for https. Only PayPal, Amazon, Ebay, GMail and my bank accounts work with https. I don't need my Addons for these sites and I would appreciate if I could auto-disable them for https.

<h4>Password Reuse Visualizer</h4>
Firefox offers a tool which helps to identify passwords, that get reused often. It is called '<a href='https://addons.mozilla.org/de/firefox/addon/password-reuse-visualizer/'>Password Reuse Visualizer</a>' and looks like this:

{% caption align="aligncenter" width="300" caption="Password Reuse Visualizer" url="../images/2012/04/password-reuse.png" alt="Password Reuse Visualizer"  height="269" class="size-full wp-image-21101" %}

<h2>What was realized?</h2>
<h3>Rotate PDF</h3>
You can view <a href="http://cloud.github.com/downloads/MartinThoma/free-books/01-A-Study-in-Scarlet.pdf">this PDF</a> online as an example. If you make a right-click on it, you can rotate it now.

{% caption align="aligncenter" width="412" caption="Rightclick menu of Google Chrome" url="../images/2012/08/pdf-chrome-rightclick-menu.png" alt="Rightclick menu of Google Chrome"  height="338" class="size-full wp-image-42081" %}

<h3>HTML5 input elements - partly</h3>
Chrome 25 does still not support the <a href="http://www.w3schools.com/html5/html5_form_input_types.asp">datetime input element</a>, tel input element, .
They have added a very nice color input element:
<input type="color" />
Some Screenshots for non-Chrome users:
The button gets displayed like that:
{% caption align="aligncenter" width="55" caption="Google Chrome input type color element" url="../images/2012/08/chrome-color-chooser.png" alt="Google Chrome input type color element"  height="33" class="size-full wp-image-42051" %}
If you click on it, this dialog box gets displayed:
{% caption align="aligncenter" width="540" caption="Google Chrome Color Dialog Box" url="../images/2012/08/chrome-color-dialog.png" alt="Google Chrome Color Dialog Box"  height="315" class="size-full wp-image-42061" %}

They have added support to many of the time-elements like week:
{% caption align="aligncenter" width="462" caption="HTML5 input type 'week'" url="../images/2013/02/html5-week.png" alt="HTML5 input type 'week'"  height="298" class="size-full wp-image-58061" %}

If you want to check how your browser displays the different input types, here is a <a href="http://www.martin-thoma.de/html5/input.php">test page for input elements</a>.

According to 

<h2>What was realized that I don't need?</h2>
The German wiki offers a really nice <a href="http://de.wikipedia.org/wiki/Google_Chrome#Versionsgeschichte">overview of version changes</a>:
<ul>
  <li>Checking spelling mistakes with Google</li>
  <li>Chrome to mobile</li>
  <li>Metro-App for Windows 8</li>
  <li>Support for Retina-Displays</li>
  <li>Google Cloud Print</li>
  <li>Improved support for Gamepads</li>
</ul>

<h3>Web Speech API</h3>
Although I think that this feature is very cool, it doesn't quite work. Here is a <a href="https://www.google.com/intl/en/chrome/demos/speech.html">demo for Web Speech</a>.

I said: "Hallo Marie. Die Web Speech API funktioniert nocht nicht so richtig." (German)
which means "Hello Marie. The Web Speech API doesn't quite work by now."
Web Speech recognized: "Hallo Mausi Mausi. Zieh dich aus." (German)
which means "Hello darling. Undress!". 
I guess this would be interesting if I sent it per email without checking the recognized text.
