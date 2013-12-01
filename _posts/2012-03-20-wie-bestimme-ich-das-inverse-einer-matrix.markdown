---
layout: post
status: publish
published: true
title: Wie bestimme ich das Inverse einer Matrix?
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 19271
wordpress_url: http://martin-thoma.com/?p=19271
date: 2012-03-20 16:07:50.000000000 +01:00
categories:
- German posts
tags:
- Wolfram|Alpha
- mathematics
- Linear algebra
- Matrix
comments:
- id: 79371
  author: i42n
  author_email: g@web.de
  author_url: ''
  date: !binary |-
    MjAxMi0wMy0yMCAxNzowNjoxMiArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMy0yMCAxNTowNjoxMiArMDEwMA==
  content: ! '&Auml;h, hei&szlig;t das nicht DIE inverse Matrix?'
- id: 79391
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wMy0yMCAxNzoxODoyNSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMy0yMCAxNToxODoyNSArMDEwMA==
  content: ! "Das Inverse Element einer Gruppe ist eindeutig, da eine Gruppe G(M,
    *) drei Eigenschaften haben muss:\r\n\r\n1. Die Verkn&uuml;pfung * ist assoziativ\r\n2.
    Es gibt ein Element e in M, sodass gilt: F&uuml;r alle x in M gilt: x * e = e
    * x = x\r\n3. F&uuml;r jedes x in M gilt: Es existiert ein x^-1 in M, sodass x
    * x^-1 = x^-1 * x = e\r\n\r\nBeh.: Das Inverse in einer Gruppe ist eindeutig.\r\nBew.:
    Durch Widerspruch\r\nAnnahme: Es gibt f&uuml;r min. ein element g neben g^-1 ein
    weiteres Inverses h, sodass g * h = h * g = e und g^-1 = h\r\n=> h = e * h = (g^-1
    * g) * h = g^-1 * (g * h) = g^-1\r\n=> Es gibt kein anderes Inverses => Das Inverse
    einer Gruppe ist eindeutig.\r\n\r\nIch hoffe das wolltest du wissen. Kannst du
    mir sagen, welche stelle dich gest&ouml;rt hat?"
- id: 79991
  author: i42n
  author_email: g@web.de
  author_url: ''
  date: !binary |-
    MjAxMi0wMy0yMSAwODo1Njo1MSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMy0yMSAwNjo1Njo1MSArMDEwMA==
  content: Ich meinte eigentlich nur die Grammatik. Also DIE EINE inverse Matrix.
    Siehe http://de.wikipedia.org/wiki/Regul%C3%A4re_Matrix#Berechnung_der_Inversen_einer_Matrix
---
Nicht alle Matrizen sind invertierbar. Matrizen, die invertierbar sind, nennt man auch regul&auml;r. Die Menge aller invertierbaren $n \times n$&ndash;Matrizen &uuml;ber einem Grundk&ouml;rper (oder Grundring) K bildet eine Gruppe bez&uuml;glich der Matrixmultiplikation, die allgemeine lineare Gruppe $GL_n(K)$.

Das Inverse einer Matrix A wird berechnet, indem eine Matrix (A|E) gebildet wird und mit dem Gau&szlig;schem Eliminationsverfahren in $(E | A^{-1})$ aufgel&ouml;st wird.

<h2>Beispiel</h2>
<h3>Ein Inverses existiert</h3>
$\left( \begin{array}{c c c c | c c c c} 
  4 & 2 & 4 & 2 & 1 & 0 & 0 & 0 \\ 
  3 & 1 & 4 & 1 & 0 & 1 & 0 & 0\\ 
  2 & 7 & 1 & 8 & 0 & 0 & 1 & 0\\ 
  0 & 1 & 1 & 2 & 0 & 0 & 0 & 1 
\end{array} \right) \rightsquigarrow
\left( \begin{array}{c c c c | c c c c} 
  2 & 1 & 2 & 1 & \frac{1}{2} & 0 & 0 & 0 \\ 
  0 & -\frac{1}{2} & 1 & -\frac{1}{2} & -\frac{3}{4} & 1 & 0 & 0\\ 
  0 & 6 & -1 & 7 & -\frac{1}{2} & 0 & 1 & 0\\ 
  0 & 1 & 1 & 2 & 0 & 0 & 0 & 1 
\end{array} \right)$

$\rightsquigarrow^* 
\frac{1}{8}
\begin{pmatrix}
12  & -12 & -2 &   2 \\
-16 &  18 &  5 & -13 \\
 -8 &  10 &  1 &  -1 \\
 12 & -14 & -3 &  11
\end{pmatrix}$
(siehe <a href="http://www.wolframalpha.com/input/?i=Inverse%5B%7B%7B4%2C2%2C4%2C2%7D%2C%7B3%2C1%2C4%2C1%7D%2C%7B2%2C7%2C1%2C8%7D%2C%7B0%2C1%2C1%2C2%7D%7D%5D">Wolfram|Alpha</a>)

<h3>Kein Inverses existiert</h3>
Matrizen, zu denen kein Inverses existiert, werden singul&auml;r genannt. Das ist ein Beispiel:
$\begin{pmatrix}
 1 & 0 & 0 & 0 \\
 0 & 1 & 0 & 0 \\
 0 & 0 & 1 & 0 \\
 0 & 0 & 1 & 0
\end{pmatrix}$ (siehe <a href="http://www.wolframalpha.com/input/?i=Inverse%5B%7B%7B1%2C0%2C0%2C0%7D%2C%7B0%2C1%2C0%2C0%7D%2C%7B0%2C0%2C1%2C0%7D%2C%7B0%2C0%2C1%2C0%7D%7D%5D">Wolfram|Alpha</a>)
Sobald also erkennbar ist, dass beim Eliminationsverfahren eine Nullzeile auftritt, kann man abbrechen.

Matrizen, die nicht quadratisch sind, haben kein Inverses:
$\begin{pmatrix}
 1 & 0 & 0 \\
 0 & 1 & 0 \\
 0 & 0 & 1 \\
 0 & 0 & 2
\end{pmatrix}$
(siehe <a href="http://www.wolframalpha.com/input/?i=Inverse%5B%7B%7B1%2C0%2C0%7D%2C%7B0%2C1%2C0%7D%2C%7B0%2C0%2C1%7D%2C%7B0%2C0%2C2%7D%7D%5D">Wolfram|Alpha</a>)

<h2>Siehe auch</h2>
<ul>
  <li>Wikipedia: <a href="http://de.wikipedia.org/wiki/Regul%C3%A4re_Matrix">Regul&auml;re Matrix</a>, <a href="http://de.wikipedia.org/wiki/Gau%C3%9Fsches_Eliminationsverfahren">Gau&szlig;sches Eliminationsverfahren</a></li>
  <li>Skript von Prof. Dr. Leuzinger, ab S. 53</li>
</ul>
