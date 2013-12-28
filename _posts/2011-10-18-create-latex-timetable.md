---
layout: post
title: Create LaTeX timetable
author: Martin Thoma
date: 2011-10-18 16:10:55.000000000 +02:00
categories:
- Code
tags:
- LaTeX
featured_image: 2012/01/latex-logo.png
---
LaTeX is a quite cool document markup language and document preparation system. You can easily create mathematical formulas.

Today I've created a LaTeX timetable. Well, to be honest I have only used the timetable package from Pascal Gwosdek found on <a href="http://www.planetk.de/index.php/Stundenplan">planetk.de</a>.

Here is the LaTeX-Code:

{% highlight text %}\documentclass[a4paper,10pt]{report}

% Definitions
\usepackage{lscape}
\usepackage[height=25cm]{geometry}
\usepackage{timetable}

\begin{document}
\thispagestyle{empty}
\begin{landscape}
\noindent\printheading{Stundenplan von Martin Thoma - 1. Semester}

% Define the layout of your time tables
\setslotsize{2.8cm}{0.3cm}
\setslotcount {5} {40}
\settopheight{3}
\settextframe{0.8mm}

% Retro
\setframetype[t]{1}
\seteventcornerradius{0pt}

% Print timestamps into event blocks
%\setprinttimestamps{2}

% Define event types
\defineevent{lecture}{0.0} {0.28}{1.0} {1.0}{1.0}{1.0}
\defineevent{exercise-course}    {1.0} {0.4} {0.2} {1.0}{1.0}{1.0}
\defineevent{tutorial}   {0.6} {0.8} {1.0} {1.0}{1.0}{1.0}
\defineevent{langcourse} {1.0} {0.4} {0.2} {1.0}{1.0}{1.0}
\defineevent{work}       {0.21}{0.5} {0.16}{1.0}{1.0}{1.0}

% Start the time table
\begin{timetable}
  \hours{8}{15}{1}
  \germandays{1}
  \event 1 {0945} {1115} {Betriebssysteme}                        {Bellosa}          {10.23 Nusselt}     {lecture}
  \event 1 {1130} {1300} {Wahrscheinlichkeits-theorie}            {Hug}              {11.40 Tulla HS}    {lecture}
  \event 1 {1400} {1530} {Programmieren}                          {Pretschner}       {50.35 HS a. F.}    {lecture}
  \event 1 {1545} {1715} {LinAlg und Ana}                         {Leuzinger}        {30.46 Neue Chemie} {exercise-course}
  \event 2 {0800} {0930} {Analysis I}                             {Schmoeger}        {30.46 Neue Chemie} {lecture}
  \event 2 {0945} {1115} {Betriebssysteme}                        {Bellosa}          {20.40 HS 37}       {exercise-course}
  \event 2 {1130} {1300} {Theoretische Grundlagen der Informatik} {Wagner}           {30.21 Gerthsen}    {lecture}
  \event 3 {0800} {0930} {LinAlg und Analytische Geometrie I}     {Leuzinger}        {10.21 Daimler}     {lecture}
  \event 3 {1400} {1530} {Grundbegriffe der Informatik}           {Schultz}          {50.35 HS a. F.}    {lecture}
  \event 4 {0800} {0930} {Analysis I}                             {Schmoeger}        {30.46 Neue Chemie} {lecture}
  \event 4 {1130} {1300} {Theoretische Grundlagen der Informatik} {Wagner}           {30.21 Gerthsen}    {lecture}
  \event 5 {0800} {0930} {LinAlg und Analytische Geometrie I}     {Leuzinger}        {11.40 Tulla HS}    {lecture}
  \event 5 {0945} {1115} {Grundbegriffe der Informatik}           {Schultz}          {50.35 HS a. F.}    {exercise-course}
  \event 5 {1545} {1715} {Analysis I}                             {Schmoeger}        {10.21 Benz}        {exercise-course}
\end{timetable}
\end{landscape}
\end{document}{% endhighlight %}

Here is the <a href='http://martin-thoma.com/wp-content/uploads/2011/10/timetable.sty'>timetable</a> and the <a href='http://martin-thoma.com/wp-content/uploads/2011/10/example.tex'>example timtable in LaTeX</a>.
If you have a Linux machine, you can create the timetable with this command:
{% highlight bash %}pdflatex example.tex -output-format=pdf{% endhighlight %}
