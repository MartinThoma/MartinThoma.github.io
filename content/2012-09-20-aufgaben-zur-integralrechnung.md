---
layout: post
lang: de
title: Aufgaben zur Integralrechnung
author: Martin Thoma
date: 2012-09-20 08:56:07.000000000 +02:00
category: German posts
tags: mathematics, Integral calculus
featured_image: 2012/09/partielle-integration.png
---
Hier sind ein paar sch&ouml;ne Aufgaben und ausf&uuml;hrliche L&ouml;sungsfindungsbeschreibungen zur Integralrechnung.

Diesen Artikel werde ich erg&auml;nzen, wenn ich weitere sch&ouml;ne Aufgaben finde.

<h2>Aufgabe 1</h2>
<strong>Aufgabenstellung</strong>:

Berechne das bestimmte Integral $\int_1^2 \frac{\arctan(x)}{x^2} dx$.

<strong>Wissen</strong>:
<ul>
  <li>Partielle Integration</li>
  <li>Integration durch Substitution</li>
  <li>Partialbruchzerlegung</li>
  <li>$(\arctan(x))' = \frac{1}{1+x^2}$</li>
  <li>$\arctan(1) = \frac{1}{4}$</li>
</ul>

<strong>Rechnung</strong>:

Partielle Integration mit:
<ul>
  <li>$f(x) = \arctan(x) \rightarrow f'(x) = \frac{1}{1+x^2}$</li>
  <li>$g'(x)= x^{-2} \rightarrow g(x) = -x^{-1}$</li>
</ul>

\begin{align}
\int_1^2 \frac{\arctan(x)}{x^2} dx
&= \left [ \arctan(x) \cdot (- \frac{1}{x}) \right ]_1^2 - \int_1^2 \frac{-1}{x \cdot (1+x^2)} dx\\
&= - \frac{1}{2} \arctan(2) + \underbrace{\arctan(1)}_{\frac{1}{4}} + \int_1^2 \frac{1}{x \cdot (1+x^2)} dx
\end{align}

Partialbruchzerlegung mit:
$\frac{A}{x} + \frac{B}{1+x^2} = \frac{1}{x \cdot (1+x^2)}\\
\Leftrightarrow A \cdot (1+x^2) + B \cdot x = 1\\
\Leftrightarrow A + Bx + Ax^2 = 1\\
\Rightarrow A= 1  \land B = -x:\\
\frac{1}{x} + \frac{-x}{1+x^2} = \frac{1}{x \cdot (1+x^2)}$

\begin{align}
\int_1^2 \frac{\arctan(x)}{x^2} dx
&= \frac{1}{4} - \frac{1}{2} \arctan(2) + \int_1^2 \frac{1}{x} dx - \int_1^2 \frac{x}{1+x^2} dx\\
\end{align}

Substitution mit:
<ul>
  <li>$u := 1+x^2$</li>
  <li>$\frac{du}{dx} = u' = 2x \rightarrow dx = \frac{du}{2x}$</li>
</ul>

\begin{align}
\int_1^2 \frac{\arctan(x)}{x^2} dx
&= \frac{1}{4} - \frac{1}{2} \arctan(2) + \left [ \log x \right ]_1^2 - \int_2^5 \frac{1}{2u} du\\
&= \frac{1}{4} - \frac{1}{2} \arctan(2) + \log 2 - \frac{1}{2} \int_2^5 x dx\\
&= \frac{1}{4} - \frac{1}{2} \arctan(2) + \log 2 - \frac{1}{2} \left [ \log(x) \right ]_2^5\\
&= \frac{1}{4} - \frac{1}{2} \arctan(2) + \log 2 - \frac{1}{2} \log 5 + \frac{1}{2} \log 2\\
&= \frac{1}{4} - \frac{1}{2} \arctan(2) + \frac{3}{2} \log 2 - \frac{1}{2} \log 5\\
&= \frac{1}{2} \cdot \left (\frac{1}{2} - \arctan(2) + 3 \log 2 - \log 5 \right )
\end{align}

<strong>Kontrolle</strong>: <a href="http://www.wolframalpha.com/input/?i=int+arctan%28x%29%2Fx%5E2+dx">Wolfram|Alpha</a>

<h2>Aufgabe 2</h2>
Diese Aufgabe war in der Analysis I-Klausur vom Herbst 2006 am KIT.
<strong>Aufgabenstellung</strong>:

Berechne das bestimmte Integral $\displaystyle \int_0^1 \frac{1}{(\sqrt[3]{x}+2) \cdot (\sqrt[3]{x}+1)} dx$.

<strong>Wissen</strong>:
<ul>
  <li>Integration durch Substitution</li>
  <li>Partialbruchzerlegung</li>
  <li>Logarithmusgesetze</li>
</ul>

<strong>Rechnung</strong>:
Kommt vielleicht sp&auml;ter noch.
