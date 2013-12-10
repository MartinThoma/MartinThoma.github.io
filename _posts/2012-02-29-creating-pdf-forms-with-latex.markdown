---
layout: post
status: publish
published: true
title: Creating pdf-forms with LaTeX
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 16071
wordpress_url: http://martin-thoma.com/?p=16071
date: 2012-02-29 15:11:07.000000000 +01:00
categories:
- My bits and bytes
tags:
- LaTeX
comments:
- id: 178391
  author: Aravind
  author_email: aravindmnps@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMi0wNy0xNSAwOTo1MzozNiArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNy0xNSAwNzo1MzozNiArMDIwMA==
  content: ! "Hi\r\nThis is a brilliant way to create forms through Latex. Thanks
    a ton for the code! But could you suggest a way to make it a save-able pdf?"
- id: 178401
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wNy0xNSAwOTo1NTo0NCArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNy0xNSAwNzo1NTo0NCArMDIwMA==
  content: ! "Does this help?\r\nhttp://tex.stackexchange.com/q/29842/5645"
- id: 1154981
  author: Alex
  author_email: alexvergaragil@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wMy0xOSAxODoxODozMiArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMy0xOSAxNzoxODozMiArMDEwMA==
  content: ! 'I&acute;ve just saw this page and it is a very good example for creating
    forms but I am lacking of a feature I need: I want a textfield to be disabled
    until a determined checkbox is checked, and the other way if it is unckecked then
    the textfield must be disabled. How do I do this? What would be the right place
    to add the javascript code'
- id: 1155041
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wMy0xOSAyMDoyNToxMSArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMy0xOSAxOToyNToxMSArMDEwMA==
  content: ! 'Dear Alex,


    I don''t know how to do this. But I can recommend http://tex.stackexchange.com/
    for such questions.

    When you ask it there, please share a link to the question in the comments.


    Best regards,

    Martin'
- id: 1223061
  author: Cornie Malan
  author_email: ctmalan@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNi0yMSAxNjoxNjoyNiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNi0yMSAxNDoxNjoyNiArMDIwMA==
  content: ! "The TextField [default = Default Entry] is very handy, but how do you
    do something like a multiline default such as an address?\r\n\r\ndefault={Name\\newline\r\nLine1\\newline\r\nLine2\\newline\r\nPcode}
    gives errors!\r\n\r\nSee http://tex.stackexchange.com/q/120250/27312\r\n\r\nC-:"
---
I've just stumbled across a full, working example how to create a html form within an LaTeX document. You can fill this form within your PDF-Reader. Here is the <a href='http://martin-thoma.com/wp-content/uploads/2012/02/pdf-form.pdf'>example PDF-file</a>.

It looks like this in Chromes PDF reader:
{% caption align="aligncenter" width="421" caption="PDF LaTeX form in Chrome" url="../images/2012/02/pdf-latex-form-chrome.png" alt="PDF LaTeX form in Chrome" title="PDF LaTeX form in Chrome" height="279" class="size-full wp-image-16711" %}

{% highlight text %}\documentclass[a4paper,12pt]{article}
\usepackage{amssymb} % needed for math
\usepackage{amsmath} % needed for math
\usepackage[utf8]{inputenc} % this is needed for german umlauts
\usepackage[ngerman]{babel} % this is needed for german umlauts
\usepackage[T1]{fontenc}    % this is needed for correct output of umlauts in pdf
\usepackage[margin=2.5cm]{geometry} %layout

\usepackage{hyperref}  % this is needed for forms and links within the text

\hypersetup{ 
  pdfauthor   = {Martin Thoma}, 
  pdfkeywords = {Martin Thoma, exmple, LaTeX, form}, 
  pdftitle    = {An example for a LaTeX form} 
} 

\begin{document}

\title{An example for a LaTeX form}
\author{Martin Thoma}
\date{\today}

\section{An example for a \LaTeX~form}

\begin{Form}[action=mailto:info@example.com,encoding=html,method=post]
\subsection{Some general information:}
\begin{tabbing}
xxxxxxxxxx: \= \kill  % This is needed for the right tab width
Name: 			\> \TextField[name=name,width=3cm,charsize=12pt]
{\mbox{}}
Prename: \TextField[name=vor,width=3cm,charsize=12pt]
{\mbox{}} \\

City: 			\> 
\ChoiceMenu[combo,name=city,width=5cm,charsize=12pt,default=Karlsruhe]{\mbox{}}
{Chemnitz,Dresden,Leipzig,Berlin,Hamburg,Karlsruhe,M&uuml;nchen} \\

Sex: 	\> 
\ChoiceMenu[radio,default=f,name=sex,charsize=14pt]{\mbox{}}{Male=m,Female=f}
\end{tabbing}

\subsection{Education:}
\CheckBox[name=highschool,charsize=12pt]{High School}
\CheckBox[name=college,charsize=12pt]{College}
\CheckBox[name=university,charsize=12pt]{University} \\


\Submit{Submit}
\Reset{Clear}
\hfill ~\\
\end{Form}

\end{document}{% endhighlight %}

You can save this as pdf-form.tex and run this command in Linux:
{% highlight bash %}pdflatex pdf-form.tex -output-format=pdf{% endhighlight %}

It seems as if the \ChoiceMenu radio option is buggy at the moment. Does anybody know how to fix that?
edit: Hmm ... it works in Chromes PDF reader, but not in Document Viewer. Mayby Document Viewer is buggy.

<h2>Sources</h2>
<ul>
    <li>TeX Users Group: <a href="http://www.tug.org/applications/hyperref/manual.html#x1-190006">PDF and HTML forms</a></li>
    <li><a href="http://www.qucosa.de/fileadmin/data/qucosa/documents/4512/data/vortrag2.pdf">Teil 2: LATEX und PDF</a> - TU Chemnitz (German)</li>
    <li><a href="http://www2.informatik.hu-berlin.de/~piefel/LaTeX-PS/Archive-2004/V12-PDF.pdf">Dokumentation der HU Berlin</a> (German)</li>
</ul>
