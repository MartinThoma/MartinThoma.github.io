---
layout: post
title: Improving lecture notes: Job (almost) done!
author: Martin Thoma
date: 2013-08-10 15:50:09.000000000 +02:00
category: My bits and bytes
tags: LaTeX
featured_image: 2013/08/latex1.png
---
Some of you might know that I've bin improving the lecture notes for the computer engineering lecture (digital electronics) since April 2013.

<h2>How I've got the job</h2>
This was kind of funny. I send Prof. Dr. Asfour some notes of passages that could be improved (mainly typos). About two days later he proposed me to correct it by myself. Another day later I signed the contract. I've never signed a contract that fast.

<h2>What I did</h2>
My job was
<ul>
  <li>to correct errors (German language, statements about computer science and LaTeX),</li>
  <li>find parts that were outdated and update them,</li>
  <li>find sections that were difficult to understand and simplify them and</li>
  <li>to make it easier to make changes in the future (Well, I don't think Prof. Dr. Asfour thought this was my job ... but I think it's important.)</li>
</ul>

So Prof. Dr. Asfour created a SVN repository with all LaTeX sources of the latest lecture notes (which were already great!). He also sent me Emails he received from students who mentioned errors just like I did and some notes from a tutor who tried to improve the script some time ago.

<h2>Revisions</h2>
With <code>svn checkout svn://somepath@1 working-directory</code> you can checkout the first revision of a SVN repository.

Total number of files and folders: <code>find . | wc -l</code>
<ul>
  <li>Revision 1: 1885</li>
  <li>Revision 30: 1488</li>
</ul>

How often did I change files (<a href="http://wirespeed.wordpress.com/2011/06/08/subversion-how-many-times-has-a-file-been-modified/">source</a>):

```bash
svn log -qvr 1:HEAD|perl -nle 'print if /^Changed paths:/ ... /^-+$/ and /^\s/' \
    | sort | uniq -c | sort -n
```

```bash

      1    M /ti1.bib
      2    M /
      2    M /anhang-1.tex
      2    M /anhang-3.tex
      2    M /anhang-5.tex
      2    M /diss-report.cls
      2    M /figures/Makefile
      2    M /titel.tex
      2    M /zahlen_codes
      3    M /vorwort.tex
      7    M /einleitung.tex
      8    M /Makefile
     10    M /my_def.tex
     11    M /sw.tex
     14    M /arith.tex
     14    M /skript.tex
     16    M /daten.tex
     19    M /sn.tex
     22    M /README.txt
     28    M /skript.pdf

```

With <a href="https://sourceforge.net/projects/codeanalyze-gpl/">CodeAnalyzer</a> over all .tex files:
<table>
<tr>
<th>&nbsp;</th>
<th>Revision 1</th>
<th>Revision 30</th>
</tr>
<tr>
<th>Total files</th>
<td>31</td>
<td>14</td>
</tr>
<tr>
<th>Total Lines</th>
<td>24,679</td>
<td>11,077</td>
</tr>
<tr>
<th>Avg Line Length</th>
<td>39</td>
<td>45</td>
</tr>
<tr>
<th>Code Lines</th>
<td>18,500</td>
<td>8,967</td>
</tr>
<tr>
<th>Comment Lines</th>
<td>1,124</td>
<td>871</td>
</tr>
<tr>
<th>Whitespace Lines</th>
<td>5,177</td>
<td>1,391</td>
</tr>
<tr>
<th>Resulting PDF pages</th>
<td>229</td>
<td>233</td>
</tr>
<tr>
<th>Examples</th>
<td>93 <</td>
<td>93</td>
</tr>
<tr>
<th>Images</th>
<td>211</td>
<td>211</td>
</tr>
</table>

<h2>StackExchange</h2>
I've learned quite a lot about LaTeX while correcting the document. My questions on StackExchange might reflect that:

<ul>
  <li>xfig:
    <ul>
      <li><a href="http://tex.stackexchange.com/q/109388/5645">What are epic macro, eepic macro and eepicemu macro in xfig?</a></li>
      <li><a href="http://tex.stackexchange.com/questions/115773/setfigfontnfss-vs-setfigfont">SetFigFontNFSS vs. SetFigFont</a></li>
    </ul>
  </li>
  <li><a href="http://tex.stackexchange.com/q/117704/5645">Quotation marks: Is there any difference between \grqq/\glqq and &ldquo;` / &rdquo;'?</a></li>
  <li><a href="http://tex.stackexchange.com/q/117751/5645">How to use nag?</a> - This gave me a lot of input what I could improve</li>
  <li><a href="http://tex.stackexchange.com/q/121725/5645">How should I prevent images from floating between list and paragraph before</a></li>
  <li><a href="http://tex.stackexchange.com/q/125657/5645">Can I tell LaTeX to break a list?</a></li>
  <li><a href="http://tex.stackexchange.com/q/126790/5645">How can I prevent breaks in a custom environment?</a></li>
  <li><a href="http://tex.stackexchange.com/q/127561/5645">Is it possible to define an environment that might not be displayed?</a></li>
  <li><a href="http://stackoverflow.com/q/18158930/562769">Why doesn't grep give the matching line?</a></li>
</ul>

And some language questions:
<ul>
  <li><a href="http://german.stackexchange.com/q/7027/655">Nummerierung im Text</a></li>
  <li><a href="http://german.stackexchange.com/q/6589/655">Gibt es ein Verb f&uuml;r &ldquo;Ein Zeichen wird durch seine Escape-Sequenz ersetzt&rdquo;?</a></li>
  <li><a href="http://german.stackexchange.com/q/6154/655">&ldquo;Theoretische Informatik&rdquo; oder &ldquo;theoretische Informatik&rdquo;</a></li>
</ul>

<h2>What I've learned</h2>
<ul>
  <li>You can open file skript.tex on line 1234 with <code>vim +1234 skript.tex</code></li>
  <li><code>grep -rniI</code>, <code>find</code>, <code>xargs</code>, make and <a href="http://en.wikipedia.org/wiki/Meld_(software)">Meld</a> are VERY useful</li>
  <li>I like Git more than SVN (because I don't need internet to commit)</li>
  <li>nag package is interesting</li>
  <li>There seems to be no good way to create images for digital electronics which might contain LaTeX. xfig is the best I found, but it is very hard to use.</li>
</ul>

<h2>Conclusion</h2>
Working as a "Skript-HiWi" is easy work, but more time consuming than you might think. Even if you know how to work with LaTeX. Rebuilding a big document takes some time.

I was astonished that there were some topics which I didn't understand yet. After I've prepared for the exam, I thought I knew everything in the lecture notes. Obviously, this was not the case (or I forgot how to do division with twos complement meanwhile).
