---
layout: post
title: Wie berechne ich das multiplikativ Inverse einer komplexen Zahl?
author: Martin Thoma
date: 2012-04-04 16:57:06.000000000 +02:00
category: German posts
tags: Complex number
---
Im Folgenden werde ich kurz und b&uuml;ndig erkl&auml;ren, wie man das multiplikativ Inverse einer komplexen Zahl berechnet.

<h2>Beispiel</h2>
Berechne das multiplikativ Inverse zur komplexen Zahl $(\frac{1}{10} + \frac{1}{5}i)$.

Das Ergebnis ist von der Form $(c + di) \in \mathbb{C}$.
Es muss folgende Gleichung erf&uuml;llen:
<a id="more"></a><a id="more-20591"></a>
$(\frac{1}{10} + \frac{1}{5}i) \cdot (c + di) = 1$
$\Leftrightarrow (\frac{1}{10} \cdot c - \frac{1}{5} d) + (\frac{1}{5} c + \frac{1}{10} d)i = 1$
$\Leftrightarrow (\frac{1}{10} \cdot c - \frac{1}{5} d) = 1 \land (\frac{1}{5} c + \frac{1}{10} d) = 0$
$\Leftrightarrow \left( \begin{array}{c c | c} 
  \frac{1}{10} & -\frac{1}{5} & 1 \\ 
  \frac{1}{5} & \frac{1}{10}  & 0
\end{array} \right)
\Leftrightarrow \left( \begin{array}{c c | c} 
  \frac{1}{10} & -\frac{1}{5} & 1 \\ 
  0 & \frac{1+4}{10}  & -2
\end{array} \right) = 
\left( \begin{array}{c c | c} 
  \frac{1}{10} & -\frac{1}{5} & 1 \\ 
  0 & \frac{1}{2}  & -2
\end{array} \right)$
$\Leftrightarrow \left( \begin{array}{c c | c} 
  \frac{1}{10} & -\frac{1}{5} & 1 \\ 
  0 & 1 & -4
\end{array} \right)
\Leftrightarrow \left( \begin{array}{c c | c} 
  \frac{1}{10} & 0 & 1 - \frac{4}{5} \\ 
  0 & 1 & -4
\end{array} \right) =
\left( \begin{array}{c c | c} 
  \frac{1}{10} & 0 & \frac{1}{5} \\ 
  0 & 1 & -4
\end{array} \right)$
$\Leftrightarrow
\left( \begin{array}{c c | c} 
  1 & 0 & 2 \\ 
  0 & 1 & -4
\end{array} \right)$

Das Ergebnis lautet also:
Das multiplikativ Inverse zu $(\frac{1}{10} + \frac{1}{5}i)$ ist $(2 -4i)$.

<h2>Allgemein</h2>
Berechne das multiplikativ Inverse zur komplexen Zahl $(a + bi)$.

Das Ergebnis ist von der Form $(c + di) \in \mathbb{C}$.
Es muss folgende Gleichung erf&uuml;llen:
$(a + bi) \cdot (c + di) = 1$
$\Leftrightarrow (a c - b d) + (b c + a d)i = 1$
$\Leftrightarrow (a c - b d) = 1 \land (b c + a d) = 0$

<h3>Fall 1: a ungleich 0</h3>
$\Leftrightarrow \left( \begin{array}{c c | c} 
  a & -b & 1 \\ 
  b & a  & 0
\end{array} \right)
\Leftrightarrow \left( \begin{array}{c c | c} 
  a & -b & 1 \\ 
  0 & a + \frac{b^2}{a}  & - \frac{b}{a}
\end{array} \right)
= \left( \begin{array}{c c | c} 
  a & -b & 1 \\ 
  0 & \frac{a^2 + b^2}{a}  & - \frac{b}{a}
\end{array} \right)$
$\Leftrightarrow \left( \begin{array}{c c | c} 
  a & -b & 1 \\ 
  0 & 1 & -\frac{b}{a^2 + b^2}
\end{array} \right)
\Leftrightarrow \left( \begin{array}{c c | c} 
  a & 0 & 1 - \frac{b^2}{a^2 + b^2} \\ 
  0 & 1 & -\frac{b}{a^2 + b^2}
\end{array} \right)
\Leftrightarrow \left( \begin{array}{c c | c} 
  1 & 0 & (1 - \frac{b^2}{a^2 + b^2})/a \\ 
  0 & 1 & -\frac{b}{a^2 + b^2}
\end{array} \right)$
$= \left( \begin{array}{c c | c} 
  1 & 0 & (\frac{a^2 + b^2 - b^2}{a^2 + b^2})/a \\ 
  0 & 1 & -\frac{b}{a^2 + b^2}
\end{array} \right)
= \left( \begin{array}{c c | c} 
  1 & 0 & \frac{a}{a^2 + b^2} \\ 
  0 & 1 & -\frac{b}{a^2 + b^2}
\end{array} \right)$

Das Ergebnis lautet also:
Das multiplikativ Inverse zu $(a + bi)$ ist also in diesem Fall $(\frac{a}{a^2 + b^2} - \frac{b}{a^2 + b^2}i)$.

<h3>Fall a gleich 0</h3>
$\Leftrightarrow - b d = 1 \land b c= 0$
$\implies c = 0 \land d = - \frac{1}{b}$

Das multiplikativ Inverse zu $(bi)$ ist also in diesem Fall $(0 - \frac{1}{b}i)$ = (\frac{0}{0^2 + b^2} - \frac{b}{0^2 + b^2}i)$.

<h3>Ergebnis</h3>
Ganz allgemein kann man f&uuml;r das multiplikativ Inverse einer beliebigen komplexen Zahl also folgendes Angeben:
$(\frac{a}{a^2 + b^2} - \frac{b}{a^2 + b^2}i)$.

<h2>Siehe auch</h2>
<ul>
  <li>Wikipedia: <a href="http://de.wikipedia.org/wiki/Komplexe_Zahl">Komplexe Zahlen</a>, <a href="http://de.wikipedia.org/wiki/Inverses_Element">Inverses Element</a></li>
</ul>
