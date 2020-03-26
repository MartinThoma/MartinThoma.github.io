---
layout: post
title: Wie sollte man xfig-Bilder in LaTeX-Dokumente einbinden?
author: Martin Thoma
date: 2013-04-18 05:27:30
categories:
- German posts
tags:
- Digitaltechnik
- xfig
featured_image:
---
<a href="http://de.wikipedia.org/wiki/Xfig">xfig</a> 3.2 bietet 39 Export-Optionen. Im folgenden werde ich beschreiben, welche davon für das Einbinden von xfig-Bildern in LaTeX-Dokumente geeignet sind.

[caption id="attachment_63651" align="aligncenter" width="300"]<a href="//martin-thoma.com/wp-content/uploads/2013/04/xfig-3.2.png"><img src="//martin-thoma.com/wp-content/uploads/2013/04/xfig-3.2-300x206.png" alt="xfig 3.2 Export-Optionen" width="300" height="206" class="size-medium wp-image-63651" /></a> xfig 3.2 Export-Optionen[/caption]

Die 9 Pixel-Formate schließe ich direkt aus, da ich hochqualitative Bilder will.

<table>
<tr>
  <th>Format</th>
  <th>Kann man LaTeX-Formaln in xfig schreiben?</th>
</tr>
<tr>
  <th>EPS (4 verschiedene)</th>
  <td style="background-color:red;">Nein</td>
</tr>
<tr>
  <th>PDF</th>
  <td style="background-color:red;">Nein</td>
</tr>
</table>

<h2>Detaillierte Ergebnisse</h2>
Ich habe mit xfig folgendes Bild erstellt:

[caption id="attachment_63671" align="aligncenter" width="300"]<a href="//martin-thoma.com/wp-content/uploads/2013/04/example-image.png"><img src="//martin-thoma.com/wp-content/uploads/2013/04/example-image-300x257.png" alt="Beispiel zum Testen der Export-Funktionen von xfig" width="300" height="257" class="size-medium wp-image-63671" /></a> Beispiel zum Testen der Export-Funktionen von xfig[/caption]

<h3>LaTeX box (figure boundary)</h3>
```text
\makebox[2.595in]{\rule{0in}{1.596in}}
```

Diese Export-Möglichkeit schein nur die Bildgröße zu exportieren.

<h3>LaTeX image</h3>
Erzeugt eine .latex-Datei mit folgendem Inhalt:

```text
\setlength{\unitlength}{4144sp}%
%
\begingroup\makeatletter\ifx\SetFigFont\undefined%
\gdef\SetFigFont#1#2#3#4#5{%
  \reset@font\fontsize{#1}{#2pt}%
  \fontfamily{#3}\fontseries{#4}\fontshape{#5}%
  \selectfont}%
\fi\endgroup%
\begin{picture}(2505,1824)(76,-1423)
\thinlines
{\color[rgb]{0,0,0}\put(991,-1411){\framebox(1350,1800){}}
}%
{\color[rgb]{0,0,0}\put(631,-61){\line( 1, 0){360}}
}%
{\color[rgb]{0,0,0}\put(631,-1051){\line( 1, 0){360}}
}%
{\color[rgb]{0,0,0}\put(2341,-331){\line( 1, 0){180}}
}%
\put( 91,-151){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}\$a\_i\$}%
}}}}
\put(136,-1141){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}\$b\_i\$}%
}}}}
\put(1306,164){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}\$Sigma\$}%
}}}}
\put(2566,-376){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}\$s\_i\$}%
}}}}
\put(1936,-1231){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\color[rgb]{0,0,0}CO}%
}}}}
\end{picture}%
```

Nun muss nur noch `\usepackage{color}` in die Präambel und die Datei eingebunden werden:

```tex
\documentclass[a4paper]{scrreprt}
\usepackage{graphicx}
\usepackage{graphics}
\usepackage{color}

\begin{document}
\chapter{Your Chapter}
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam
erat, sed diam voluptua. At vero eos et accusam et justo duo dolores
et ea
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem
ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur
sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et
dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam
et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea
takimata sanctus est Lorem ipsum dolor sit amet.
\begin{figure}[h]
    \centering
    \input{exampleImage.latex}
\end{figure}
\end{document}
```

Allerdings fällt auf, dass der Mathmode escapt wird.

<h3>Combined PDF/LaTeX (both parts)</h3>
Hier werden zwei Dateien erstellt. Eine <code>.pdf_t</code> und eine <code>.pdf</code>.

Eingebunden wird das ganze so:

```tex
\documentclass{article}
\usepackage{graphicx}

\begin{document}
\section{Your Chapter}
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam
erat, sed diam voluptua. At vero eos et accusam et justo duo dolores
et ea
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem
ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur
sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et
dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam
et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea
takimata sanctus est Lorem ipsum dolor sit amet.

\begin{figure}[h!]
    \begin{center}
        \begin{picture}(0,0)%
          \includegraphics{exampleImage.pdf}%
        \end{picture}%
        \input{exampleImage.pdf_t}%
    \end{center}
\end{figure}
\end{document}
```

<h2>Dies und das</h2>
Wenn man neue Texte erstellt, sollte man das „Special Flag“ direkt einstellen. Man kann es nicht später hinzufügen:

[caption id="attachment_63711" align="aligncenter" width="300"]<a href="//martin-thoma.com/wp-content/uploads/2013/04/xfig-text-latex.png"><img src="//martin-thoma.com/wp-content/uploads/2013/04/xfig-text-latex-300x73.png" alt="xfig LaTeX Special Flag" width="300" height="73" class="size-medium wp-image-63711" /></a> xfig LaTeX Special Flag[/caption]
