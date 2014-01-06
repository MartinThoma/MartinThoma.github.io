---
layout: post
title: What is the best programming language?
author: Martin Thoma
date: 2012-11-03 11:48:36.000000000 +01:00
categories:
- Code
tags:
- Programming
- Python
- C
- Java
featured_image: 2012/07/testing_cartoon-thumb.jpg
---
There is no such thing as a best programming language. Sorry about that, I've just thought it would be a catchy title. I would rather choose my tools after I know the problem I have to solve.

Some programming languages are very good at some tasks. I don't know any that is very good at every task.

This comic illustrates what I mean:

{% caption align="alignnone" width="582" caption="A fair test" url="../images/2012/07/testing_cartoon.jpg" alt="A fair test - comic - illustration - cartoon - caricature"  height="402" class="size-full wp-image-32731 "  %}
<h2>Bash</h2>
The bash is great for tiny tasks where other programs are involved.
<h3>Example</h3>
Resizing all jpg-images in a given folder to a maximum resolution of 1600x1600 while maintaining the aspect ratio:

{% highlight bash %}for i in *.JPG;do convert "$i" -resize 1600x1600 "${i%.JPG}-resized.jpg"; done{% endhighlight %}

See <a href="../converting-files-with-linux/">Converting Files with Linux</a> for more examples.
<h2>Python</h2>
Python does a incredibly well job for small problems. I don't have experience with big projects, but some have been done using Python (see list below).
Python is dynamically typed, offers a lot of functions out of the box and is easy to learn and understand. You might argue that Python is executable Pseudocode as it is so easy to read. Additionally, it offers a very neat library for math functions with <a href="http://docs.scipy.org/doc/">NumPy</a>.

Examples of Python-Code in applications include:
<ul>
	<li><a href="http://security.stackexchange.com/a/2897">PDF malware analysis</a></li>
	<li><a href="http://en.wikipedia.org/wiki/BitTorrent_(software)">BitTorrent</a></li>
	<li>My <a href="../python-one-liners-for-project-euler/">ProjectEuler Snippets</a> :-)</li>
	<li>Scripting within an application:
<ul>
	<li><a href="http://en.wikipedia.org/wiki/GIMP">GIMP</a></li>
	<li><a href="http://en.wikipedia.org/wiki/Blender_(software)">Blender</a></li>
</ul>
</li>
	<li>Websites and Services:
<ul>
	<li><a href="http://en.wikipedia.org/wiki/GNU_Mailman">GNU Mailman</a></li>
	<li><a href="http://en.wikipedia.org/wiki/Reddit">Reddit</a></li>
	<li><a href="http://en.wikipedia.org/wiki/Trac">Trac</a></li>
</ul>
</li>
</ul>
<h2>Java</h2>
Java is used in the economy for <strong>simple, but huge tasks</strong>. It is <a href="http://en.wikipedia.org/wiki/Type_system#Static_typing">static</a> and <a href="http://en.wikipedia.org/wiki/Type_system#Strong_and_weak_typing">strong</a> typed, has some widely used <a href="http://www.oracle.com/technetwork/java/codeconv-138413.html">coding convetions</a>, is easy to learn and has a big library.

Here are some examples for programs written in Java:
<ul>
	<li>Mars Rovers (<a href="http://java.sys-con.com/node/39220">source</a>)</li>
	<li>BitTorrent client <a href="http://en.wikipedia.org/wiki/Vuze">Vuze</a></li>
	<li>Sites that have URLs like "*.do", "*.jsp" and "...servlet..." are most likely written in Java.</li>
	<li>Games:
<ul>
	<li><a href="http://en.wikipedia.org/wiki/FreeCol">FreeCol</a></li>
	<li><a href="http://en.wikipedia.org/wiki/Minecraft">Minecraft</a></li>
</ul>
</li>
</ul>
<h2>C++</h2>
C++ is easy to write and blazing-fast. See <a href="../matrix-multiplication-python-java-cpp/">Performance of Matrix multiplication in Python, Java and C++</a>.

Some projects done in C++ are:
<ul>
	<li>NASA flight software: 300k LOC (<a href="http://trs-new.jpl.nasa.gov/dspace/bitstream/2014/37499/1/05-0539.pdf">source</a>)</li>
	<li><a href="http://en.wikipedia.org/wiki/Google_Chrome">Chrome</a>, <a href="http://en.wikipedia.org/wiki/Firefox">Firefox</a></li>
	<li>Games:
<ul>
	<li><a href="http://en.wikipedia.org/wiki/Cube_2:_Sauerbraten">Cube 2: Sauerbraten</a></li>
	<li><a href="http://en.wikipedia.org/wiki/UFO:_Alien_Invasion">UFO: Alien Invasion</a></li>
	<li><a href="http://en.wikipedia.org/wiki/The_Battle_for_Wesnoth">The Battle for Wesnoth</a></li>
	<li><a href="http://www.openclonk.org/">OpenClonk</a> (<a href="http://hg.openclonk.org/openclonk/">Repository</a>)</li>
	<li><a href="http://www.openlierox.net/">OpenLierox</a> (<a href="https://github.com/albertz/openlierox">Repository</a>)</li>
	<li><a href="http://secretmaryo.org/">Secret Maryo Chronicles</a> (<a href="https://github.com/FluXy/SMC">Repository</a>)</li>
</ul>
</li>
</ul>
<h2>C</h2>
See <a href="http://programmers.stackexchange.com/questions/103897/is-the-c-programming-language-still-used">Is C still used?</a> and a <a href="http://thread.gmane.org/gmane.comp.version-control.git/57643/focus=57918">comment from Linus Torvalds</a>.

Programs done with C:
<ul>
	<li><a href="http://jonls.dk/freeserf/">Freeserf</a> (<a href="https://github.com/jonls/freeserf">Repository</a>)</li>
</ul>
<h2>See also</h2>
<ul>
	<li><a href="http://readwrite.com/2012/06/05/5-ways-to-tell-which-programming-lanugages-are-most-popular">5 Ways to Tell Which Programming Languages are Most Popular</a></li>
	<li><a href="http://osgameclones.com/">OpenGameClones</a></li>
</ul>

<h2>Matlab</h2>
<a href="http://stackoverflow.com/q/179904/562769">What is MATLAB good for? Why is it so used by universities? When is it better than Python?</a>


Do you know some more programs that are famous and should be in these lists? Preferably with an open repository?
