---
layout: post
lang: en
title: LaTeX + Versioning = A great Experience
slug: latex-versioning-a-great-experience
author: Martin Thoma
date: 2012-06-29 22:52:03.000000000 +02:00
category: Cyberculture
tags: LaTeX
---
Some people keep asking me questions like "Why do you use LaTeX?" - "Wouldn't it be faster to do it with Word?"

Here is the answer:
<ul>
  <li><strong>Versioning</strong>: I do quite often create repositories for documentation (e.g. on GITHub). Versioning LaTeX-files is much better than versioning Word-files, as LaTeX is line-based. Versioning is my way to solve the following problems:
  <ul>
    <li><strong>Dead end</strong>: Once in a while I stuck while writing. I tried to improve some part of the documentation, but it didn't work. So I want to jump back. It is much more convenient to jump back in a versioning system than to press <kbd>CTRL</kbd> + <kbd>Z</kbd> often or to create copies of the old version.</li>
     <li><strong>Versioning</strong>: This might sound strange, but versioning was a problem for me as I wrote my "Facharbeit" (a thesis you have to write in Germany at the end of secondary school). I had so many backups that I didn't know what was the original. If you use a versioning system, you can have everything in one place.</li>
      <li><strong>Simpler collaboration</strong>: Some weeks ago I had to prepare a <a href="http://cloud.github.com/downloads/MartinThoma/ICPC-Referat/Graphentheorie-2.pdf">presentation about graph algorithms</a> with three fellow students. We just met once to decide how to split the project. After that, everybody could work on his part while everybody could see the progress. We had no need of merging the documents. (See <a href="https://github.com/MartinThoma/ICPC-Referat">GITHub-Repository</a>)</li>
      <li><strong>Simpler proofreading</strong>: The proofreader can make a fork of the repository with the documentation and make changes on his copy. After that, the writer can make a diff and see if he wants to take those changes. You can't forget small changes of the proofreader (like a "," you forgot / you made too much) with diffs.</li>
      <li><strong>Backups</strong>: I've been ultra-paranoid as I wrote my thesis for secondary school. I regularly sent a copy to my father per Email and I had at least two copies on different data storage mediums. I wouldn't have needed this if I used versioning with GITHub. (I trust in the reliability of the service GITHub offers)</li>
  </ul>
  </li>
  <li><strong>Accessibility</strong>: To open LaTeX, you only need a text editor. If you want to complie it, you have to get one of many free LaTeX distributions like TeX-Live. After compiling it you get a PDF. PDFs look always the same, so you don't have the problem of shifted margins.</li>
  <li><strong>Speed</strong>: I can write mathematical formulae much faster with LaTeX than with Word.</li>
  <li><strong>Professional look</strong>: You can quite often see if a presentation / documentation was written with LaTeX or with Word. I think the LaTeX-Documentations do look much more professional.</li>
  <li><strong>Source Code Inclusion</strong>: You can include and highlight source code directly within LaTeX. No need for copy and paste (see <a href="../how-to-print-source-code-with-latex/" title="How to print Source Code with LaTeX">How to print Source Code with LaTeX</a>, <a href="../how-print-mips-assembly-code-latex/" title="How to print MIPS assembly code in LaTeX">How to print MIPS assembly code in LaTeX</a>)</li>
  <li><strong>Great Visualizations</strong>: You can create great visualizations directly within LaTeX (see , <a href="../how-to-draw-a-finite-state-machine/" title="How to draw a finite-state machine">How to draw a finite-state machine</a>, <a href="../plotting-function-graphs-with-latex/" title="Plotting function graphs with LaTeX">Plotting function graphs with LaTeX</a> and <a href="../complex-latex-visualizations-tikz/" title="Complex LaTeX visualizations (Tikz)">Complex LaTeX visualizations (Tikz)</a>)</li>
</ul>

I guess some might not know what a diff is or how it can look like. diff is a program that compares text files. This is an example with two text files. Each of them has 100 paragraphs:

```bash
moose@pc07:~/Desktop$ diff file1.txt file2.txt
127,128d126
< And here is another one.
<
189c187
< Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue dui s dolore te feugait nulla facilisi.
---
> Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.
191c189
< Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nosnummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.
---
> Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.
```

If you use meld it looks like this:
<a href="../images/2012/06/meld-diff.png"><img src="../images/2012/06/meld-diff-300x156.png" alt="" title="meld-diff" width="300" height="156" class="aligncenter size-medium wp-image-29051" /></a>

<h2>My LaTeX configuration</h2>
First, you have to install the latest LaTeX-Version: <a href="../how-to-install-the-latest-latex-version/" title="How to install the latest LaTeX Version">How to install the latest LaTeX Version</a>.

I like editing the source code directly very much. To do so, I use gEdit. When I press <kbd>Ctrl</kbd>+<kbd>M</kbd>, my LaTeX document gets saved, compiled and the temporary files are thrown away. If you want this, you should follow these instructions.

<ul>
 <li>Create a "Makefile" (a file called this way) with this content in the folder where your LaTeX file is:</li>
</ul>

```basemake
make:
	pdflatex matrix.tex -output-format=pdf
	make clean

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux
```

<ul>
  <li>Enable the Plugin "External Tools"</li>
  <li>Go to Preferences &rarr; Plugins &rarr; External Tools &rarr; Configure Plugin</li>
  <li>Click on the New Page icon</li>
  <li>Insert "make" into the Edit-Window</li>
  <li>Create the Shortcut Key. I've added <kbd>Ctrl</kbd>+<kbd>M</kbd>.</li>
</ul>

<h2>See also</h2>
<ul>
  <li><a href="http://academia.stackexchange.com/a/5281/4092">Why use version control systems for writing a paper</a> instead of Dropbox</li>
</ul>
