---
layout: post
title: Creating Gantt Charts
author: Martin Thoma
date: 2012-12-13 00:02:19.000000000 +01:00
categories:
- The Web
tags:
- Software Development
- LaTeX
- Gantt-Chart
featured_image: 2012/12/gantt-thumb.png
---
I am currently involved in a software project and I should create a Gantt chart. So I've searched for tools that allow me to do so, but it was astonishingly difficult to find good tools. I'm not completely content with any of them, but I would like to share my experiences.

<h2>Gantter</h2>
<h3>Overview</h3>
<a href="https://app.gantter.com">Gantter</a> is a free online tool that allows you to create Gantt charts.

It looks like this:
{% caption align="aligncenter" width="300" caption="Overview of Gantter" url="../images/2012/12/gantter-overview-300x138.png" alt="Overview of Gantter" title="Overview of Gantter" height="138" class="size-medium wp-image-50231" %}

It is easy to use and has a good interface. I can simply define depencies:

{% caption align="aligncenter" width="300" caption="Gantter Predecessor depency" url="../images/2012/12/gantter-predecessor-depenency-300x138.png" alt="Gantter Predecessor depency" title="" height="138" class="size-medium wp-image-51101" %}

<h3>Export</h3>
Gantter offers some export options: HTML, <a href="../pdf/UpToDatE-Implementierung.pdf">PDF</a>, <a href="../images/2012/12/UpToDatE-Implementierung.png">PNG</a>, MS-Project (.xml). All export options I've tried are unconvincing. I couldn't save the HTML export, the PDF export was splitted over several pages and the PNG ... well, it's a PNG. As I am currently on a Linux machine, I can't try the MS-Project export.

<h3>Google Drive</h3>
Gantter also has a Google Drive integration, but it requests these permissions:
{% caption align="aligncenter" width="470" caption="Google Drive permissions requested by Gantter" url="../images/2012/12/gantter-google-drive-files.png" alt="Google Drive permissions requested by Gantter" title="Google Drive permissions requested by Gantter" height="471" class="size-full wp-image-50241" %}

I have contacted them today (11.12.2012) and asked why they want these permissions. I'll update this post as soon as I get an answer.

My recommendation: Don't give them those rights! You can create an account without a Google Drive permission.

<h2>GanttProject</h2>
<a href="http://www.ganttproject.biz/">GanttProject</a> is a Java Gantt chart program (as you might have noticed because of the SWING design):

{% caption align="aligncenter" width="300" caption="GanttProject - Overview" url="../images/2012/12/GanttProject-300x201.png" alt="GanttProject - Overview" title="GanttProject - Overview" height="201" class="size-medium wp-image-50361" %}

It's quite good, but sometimes I got the feeling that it doesn't instantly response. It's perhaps imagination as I always think that of Java projects.

The HTML-export is not so good. It basically converts the chart to an image and embeds this into a HTML page. This is not what I thought of! This way, you can't search or copy the tasks. You also can't see more information about the task.

{% caption align="aligncenter" width="300" caption="GanttProject export function" url="../images/2012/12/GanttProject-export-300x80.png" alt="GanttProject export function" title="GanttProject export function" height="80" class="size-medium wp-image-50371" %}

<h2>GNOME Planner</h2>
<a href="https://live.gnome.org/Planner">Planner</a> is part of GNOME.

{% caption align="aligncenter" width="300" caption="Planner - Overview" url="../images/2012/12/Planner-300x157.png" alt="Planner - Overview" title="Planner - Overview" height="157" class="size-medium wp-image-50291" %}

This is how you create a new task:
{% caption align="aligncenter" width="300" caption="Planner: Create a new task" url="../images/2012/12/Planner-new-task-300x275.png" alt="Planner: Create a new task" title="Planner: Create a new task" height="275" class="size-medium wp-image-50381" %}

It is very annoying that you always have to click on "Change", then on "As soon as possible" change it to "fixed date" and then you can click on a date. Why don't you allow the user to click on a date and when he does, change it automatically to "fixed date"?

The HTML-export is good, but I would also like to click on a tasks' bar and get the associated task highlighted (and perhaps some additional information).

<h2>Trac jsGantt plugin</h2>
You can let Trac automatically create a Gantt chart with <a href="http://trac-hacks.org/wiki/TracJsGanttPlugin">Trac jsGantt plugin</a>. According to this link, it should look like this:

{% caption align="aligncenter" width="300" caption="jsGanttSample" url="../images/2012/12/jsGanttSample-300x150.png" alt="jsGanttSample" title="jsGanttSample" height="150" class="size-medium wp-image-50511" %}

I knew that I had to install the <a href="http://trac-hacks.org/wiki/MasterTicketsPlugin">MasterTicketsPlugin</a> to make it possible to add ticket dependencies. With that, it looked like this:

{% caption align="aligncenter" width="300" caption="jsGantt only with MasterTicketsPlugin" url="../images/2012/12/jsGantt-without-plugins-300x205.png" alt="jsGantt only with MasterTicketsPlugin" title="jsGantt only with MasterTicketsPlugin" height="205" class="size-medium wp-image-50521" %}

Not quite what I've expected. So I guess I will also need <a href="http://trac-hacks.org/wiki/SubticketsPlugin">SubticketsPlugin</a> and <a href="http://trac-hacks.org/wiki/TimingAndEstimationPlugin">TimingAndEstimationPlugin</a>.

Update: These Trac-Plugins are crap. The Gantt-Chart that was created looks ugly and doesn't look like I've expected.

<h2>LaTeX</h2>
<h3>pgfgantt</h3>
This piece of LaTeX:

```latex
\documentclass{article}
\usepackage[pdftex,active,tightpage]{preview}
\setlength\PreviewBorder{2mm}
\usepackage{pgfgantt}

\begin{document}
\begin{preview}
    \begin{ganttchart}{12}
    \gantttitle{2012}{12} \\
    \gantttitlelist{1,...,12}{1} \\
    \ganttgroup{Group 1}{1}{7} \\
    \ganttbar{Task 1}{1}{2} \\
    \ganttlinkedbar{Task 2}{3}{7} \ganttnewline
    \ganttmilestone{Milestone}{7} \ganttnewline
    \ganttbar{Final Task}{8}{12}
    \ganttlink{elem2}{elem3}
    \ganttlink{elem3}{elem4}
    \end{ganttchart}
\end{preview}
\end{document}
```

generates this Gantt chart:

{% caption align="aligncenter" width="500" caption="LaTeX: pgfgantt for creating Gantt charts" url="../images/2012/12/gantt-pgf.png" alt="LaTeX: pgfgantt for creating Gantt charts" title="LaTeX: pgfgantt for creating Gantt charts" height="447" class="size-full wp-image-50541" %}

Source is <a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/gantt-pgf">here</a>.

<h3>Another LaTeX Gantt chart solution</h3>
This source:
```latex
\documentclass{article}
\usepackage[pdftex,active,tightpage]{preview}
\setlength\PreviewBorder{2mm}
\usepackage{gantt}

\begin{document}
\begin{preview}
  \begin{gantt}{10}{12}
    \begin{ganttitle}
    \numtitle{1}{1}{12}{1}
    \end{ganttitle}
    \ganttbar{a task}{0}{2}
    \ganttbarcon{a consecutive task}{2}{4}
    \ganttbarcon{another consecutive task}{8}{2}
    \ganttmilestone[color=cyan]{Milestone with color!}{4}
    \ganttbar{another task}{2}{2}
    \ganttbar[color=cyan]{another coloured task}{4}{4}
    \ganttbar{another task}{4}{2}
    \ganttcon{4}{5}{4}{7}
    \ganttmilestonecon{A connected Milestone}{7}
    \ganttbarcon{another consecutive task}{8}{2}
  \end{gantt}
\end{preview}
\end{document}
```

creates

{% caption align="aligncenter" width="500" caption="Another Gantt solution" url="../images/2012/12/gantt.png" alt="Another Gantt solution" title="Another Gantt solution" height="240" class="size-full wp-image-50551" %}

Full source is <a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/gantt">here</a>.

Although the result looks very nice, I don't think LaTeX is an optimal solution for Gantt charts of software projects. Yes, you get a great result. But it takes a lot of time and after a week or so this particular chart is definitely outdated. You can't add more information directly as you could do it with HTML tooltips. I don't know if you can produce a linked PDF, but I guess this would be quite a lot of manual work. 

<h2>More tools</h2>
<a href="http://www.projectlibre.org/">ProjectLibre</a> was recommended to me, but it is not in the Ubuntu repository :-(

<h2>Conclusion</h2>
LaTeX rulez. If you want nice looking results, you should definitely use LaTeX. Although I think combining an automatically generated Gantt-chart with tickes would be nice, this seems not to be possible by now.
