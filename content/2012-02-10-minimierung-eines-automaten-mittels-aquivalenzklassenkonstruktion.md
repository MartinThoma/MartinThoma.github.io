---
layout: post
title: Minimierung eines Automaten mittels &Auml;quivalenzklassenkonstruktion
author: Martin Thoma
date: 2012-02-10 22:18:38.000000000 +01:00
category: German posts
tags: Theoretical computer science
featured_image: 2011/10/deterministic-finite-state-machine-thumb.png
---
Wenn ein Endlicher Automat gegeben ist, kann durch die Konstruktion von &Auml;quivalenzklassen sehr einfach ein Automat mit gleichem Akzeptanzverhalten und minimaler Anzahl an Zust&auml;nden gefunden werden. Daf&uuml;r ben&ouml;tigt man im Wesentlichen sogar nur drei Schritte.

<h2>Der Algorithmus</h2>
<ol>
  <li><strong>&Uuml;berfl&uuml;ssige Zust&auml;nde streichen</strong>: Manche Zust&auml;nde sind nicht erreichbar. Diese k&ouml;nnen offensichtlich gestrichen werden.</li>
  <li><strong>Akzeptierende von nichtakzeptierenden Zust&auml;nden trennen</strong>: Alle akzeptierenden Zust&auml;nde werden in eine &Auml;quivalenzklasse gepackt, alle Zust&auml;nde die nicht akzeptieren kommen in eine andere Klasse.</li>
  <li><strong>Zust&auml;nde trennen</strong>: F&uuml;r jedes Zeichen des Eingabealphabets $\Sigma$ schreibt man sich auf, in welchen Zustand der Zustand f&uuml;hrt. Wenn zwei Zust&auml;nde in verschiedene Klassen f&uuml;hren, werden diese getrennt. Dies wiederholt man so lange, bis man ein mal alle Zeichen aus $\Sigma$ durchgegangen ist, ohne dass Zust&auml;nde getrennt wurden.</li>
</ol>

<h2>Beispiel</h2>
Gegeben sei folgender Endlicher Automat A: 
$A = (\{0,1\}, \{S, A, B, C, D, E, F, G, H, I\}, S, \sigma, \{D\})$ mit folgender &Uuml;bergangsfunktion $\sigma$:
<figure class="aligncenter">
            <a href="../images/2012/02/endlicher-automat-gross.png"><img src="../images/2012/02/endlicher-automat-gross.png" alt="Endlicher Automat mit &uuml;berfl&uuml;ssigen Zust&auml;nden" style="max-width:392px;max-height:389px" class="size-full wp-image-13451"/></a>
            <figcaption class="text-center">Endlicher Automat mit &uuml;berfl&uuml;ssigen Zust&auml;nden</figcaption>
        </figure>

Es ist offensichtlich, dass I nicht erreicht werden kann. Da der Graph gerichtet ist, kann man schnell sehen, dass auch  H und G nicht erreicht werden k&ouml;nnen. Algorithmisch kann man diese Zust&auml;nde durch eine Tiefensuche bestimmen.

Nach Schritt 1 haben wir also den Automaten 
$A_1 = (\{0,1\}, \{S, A, B, C, D, E, F\}, S, \sigma, \{D\})$:
<figure class="aligncenter">
            <a href="../images/2012/02/endlicher-automat-kleiner.png"><img src="../images/2012/02/endlicher-automat-kleiner.png" alt="Keine &uuml;berfl&uuml;ssen Zust&auml;nde im Endlichen Automaten" style="max-width:340px;max-height:381px" class="size-full wp-image-13471"/></a>
            <figcaption class="text-center">Keine &uuml;berfl&uuml;ssen Zust&auml;nde im Endlichen Automaten</figcaption>
        </figure>

In Schritt 2 erstellen wir also zuerst eine &Auml;quivalenzklasse der Zust&auml;nde:
$\{S, A, B, C, D, E, F\}$.

Die akzeptierenden Zust&auml;nde werden von den nicht akzeptierenden getrennt: $\{D\}, \{S, A, B, C, E, F\}$

In Schritt 3 gehen wir nun immer wieder die Zeichen "0" und "1" aus $\Sigma$ durch:
In welche Klassen f&uuml;hrt "0"?
<a href="../images/2012/02/aequivalenzklassen-1.png"><img src="../images/2012/02/aequivalenzklassen-1.png" alt="&Auml;quivalenzklassen - Schritt 1" title="&Auml;quivalenzklassen - Schritt 1" width="220" height="71" class="aligncenter size-full wp-image-13631" /></a>

C wird also von $\{S, A, B, E, F\}$ getrennt. Wir haben folgende Klassen:
$\{C\}, \{D\}, \{S, A, B, E, F\}$

"1" trennt nun "A" von $\{S, B, E, F\}$:
<a href="../images/2012/02/aequivalenzklasse-2.png"><img src="../images/2012/02/aequivalenzklasse-2.png" alt="&Auml;quivalenzklassen - Schritt 2" title="&Auml;quivalenzklassen - Schritt 2" width="246" height="66" class="aligncenter size-full wp-image-13661" /></a>

"0" trennt nun "S" von $\{B, E, F\}$:
<a href="../images/2012/02/aequivalenzklasse-3.png"><img src="../images/2012/02/aequivalenzklasse-3.png" alt="&Auml;quivalenzklassen - Schritt 3" title="&Auml;quivalenzklassen - Schritt 3" width="267" height="65" class="aligncenter size-full wp-image-13681" /></a>

Wir haben nun die &Auml;quivalenzklassen $\{S\}, \{A\}, \{C\}, \{D\}, \{B, E, F\}$.

Im n&auml;chsten Schritt sehen wir, dass "1" nicht mehr trennt und "0" auch nicht nochmals etwas trennt. Wir sind also fertig. Die Zust&auml;nde B, E und F k&ouml;nnen zu einem zusammengefasst werden. Ich nenne ihn mal T (f&uuml;r Trash, da man in diesem Zustand niemals mehr akzeptieren kann). Damit ist unser minimaler Endlicher Automat folgender:

<a href="../images/2012/02/endlicher-automat-minimal.png"><img src="../images/2012/02/endlicher-automat-minimal.png" alt="Minimaler Endlicher Automat" title="Minimaler Endlicher Automat" width="346" height="278" class="aligncenter size-full wp-image-13711" /></a>

<h2>LaTeX</h2>
Das ist der LaTeX-Code f&uuml;r die Automaten:
```python
\documentclass{scrartcl}
\usepackage{amsmath}
\usepackage{tikz}
\usepackage{pst-node}
\usetikzlibrary{arrows,automata}

 
\begin{document}
\begin{tikzpicture}[>=stealth',shorten >=1pt,auto,node distance=2cm]
  \node[initial,state]   (S)                          {$S$};
  \node[state]           (A) [below of=S, left of=S]  {$A$};
  \node[state]           (B) [below of=A]             {$B$};
  \node[state]           (C) [below of=A, right of=A] {$C$};
  \node[state,accepting] (D) [right of=A, below of=S] {$D$};
  \node[state]           (E) [below of=C]             {$E$};
  \node[state]           (F) [below of=B]             {$F$};
  \node[state]           (G) [left of=B]              {$G$};
  \node[state]           (H) [right of=S]             {$H$};
  \node[state]           (I) [left of=A]              {$I$};
 
  \path[->]          (S)  edge              node {0, 1} (A);
  \path[->]          (A)  edge              node {0}    (B);
  \path[->]          (A)  edge              node {1}    (C);
  \path[->]          (B)  edge              node {0,1}  (F);
  \path[->]          (C)  edge              node {0}    (D);
  \path[->]          (C)  edge              node {1}    (E);
  \path[->]          (D)  edge              node {0,1}  (S);
  \path[->]          (E)  edge [loop right] node {0,1}  (E);
  \path[->]          (F)  edge [loop left]  node {0,1}  (F);
  \path[->]          (G)  edge              node {0}    (B);
  \path[->]          (G)  edge              node {1}    (F);
  \path[->]          (H)  edge              node {0,1}  (S);
  \path[->]          (I)  edge [loop above] node {0,1}  (I);
\end{tikzpicture}

Ueberfluessige weg:

\begin{tikzpicture}[>=stealth',shorten >=1pt,auto,node distance=2cm]
  \node[initial,state]   (S)                          {$S$};
  \node[state]           (A) [below of=S, left of=S]  {$A$};
  \node[state]           (B) [below of=A]             {$B$};
  \node[state]           (C) [below of=A, right of=A] {$C$};
  \node[state,accepting] (D) [right of=A, below of=S] {$D$};
  \node[state]           (E) [below of=C]             {$E$};
  \node[state]           (F) [below of=B]             {$F$};
 
  \path[->]          (S)  edge              node {0, 1} (A);
  \path[->]          (A)  edge              node {0}    (B);
  \path[->]          (A)  edge              node {1}    (C);
  \path[->]          (B)  edge              node {0,1}  (F);
  \path[->]          (C)  edge              node {0}    (D);
  \path[->]          (C)  edge              node {1}    (E);
  \path[->]          (D)  edge              node {0,1}  (S);
  \path[->]          (E)  edge [loop right] node {0,1}  (E);
  \path[->]          (F)  edge [loop left]  node {0,1}  (F);
\end{tikzpicture}

Minimal:

\begin{tikzpicture}[>=stealth',shorten >=1pt,auto,node distance=2cm]
  \node[initial,state]   (S)                          {$S$};
  \node[state]           (A) [below of=S, left of=S]  {$A$};
  \node[state]           (B) [below of=A]             {$T$};
  \node[state]           (C) [below of=A, right of=A] {$C$};
  \node[state,accepting] (D) [right of=A, below of=S] {$D$};

 
  \path[->]          (S)  edge              node {0, 1} (A);
  \path[->]          (A)  edge              node {0}    (B);
  \path[->]          (A)  edge              node {1}    (C);
  \path[->]          (B)  edge [loop left]  node {0,1}  (B);
  \path[->]          (C)  edge              node {0}    (D);
  \path[->]          (C)  edge              node {1}    (B);
  \path[->]          (D)  edge              node {0,1}  (S);
\end{tikzpicture}

\end{document}
```

Und hier die Bilder mit den Pfeilchen:
```python
\documentclass{article}
\usepackage{amsmath}

\usepackage{tikz}
\usetikzlibrary{calc,shapes}

\newcommand{\tikzmark}[1]{\tikz[overlay,remember picture] \node (#1) {};}
\newcommand{\DrawBoxi}[5]{
  \begin{tikzpicture}[overlay,remember picture,-latex,shorten >=5pt,shorten <=5pt,out=70,in=130]
    \draw[distance=0.9cm,#1] (s.north) to (a.north);
    %\draw[distance=0.45cm,#2] (a.north) to (b.north);
    \draw[distance=0.7cm, #3] (b.north) to (f.north);
    %\draw[distance=1.1cm, #4] (c.north) to (d.north);
    \draw[distance=0.45cm,#5] (e.north) to (e.north);
    \draw[distance=0.45cm,#5] (f.north) to (f.north);
  \end{tikzpicture}
}
\newcommand{\DrawBoxii}[5]{
  \begin{tikzpicture}[overlay,remember picture,-latex,shorten >=5pt,shorten <=5pt,out=70,in=130]
    \draw[distance=0.45cm,#1] (s.north) to (a.north);
    \draw[distance=0.8cm,#2] (a.north) to (c.north);
    \draw[distance=0.9cm, #3] (b.north) to (f.north);
    \draw[distance=0.45cm,#5] (e.north) to (e.north);
  \end{tikzpicture}
}
\begin{document}
Schritt 3 - 1.0:
\begin{gather*}
%\{D\tikzmark{d}\} ~ \{S\tikzmark{s}, A\tikzmark{a}, B\tikzmark{b}, C\tikzmark{c}, E\tikzmark{e}, F\tikzmark{f}\} \DrawBoxi{red}{blue}{green}{purple}{orange}\\
\end{gather*}

Schritt 3 - 1.1:
\begin{gather*}
%\{C\tikzmark{c}\} ~ \{D\tikzmark{d}\} ~ \{S\tikzmark{s}, \tikzmark{a}A, B\tikzmark{b}, E\tikzmark{e}, F\tikzmark{f}\} \DrawBoxii{red}{blue}{green}{purple}{orange}\\
\end{gather*}

Schritt 3 - 2.0:
\begin{gather*}
\{\tikzmark{a}A\} ~ \{C\tikzmark{c}\} ~ \{D\tikzmark{d}\} ~ \{\tikzmark{s}S, \tikzmark{b}B, E\tikzmark{e}, F\tikzmark{f}\} \DrawBoxi{red}{blue}{green}{purple}{orange}\\
\end{gather*}
\end{document}
```
