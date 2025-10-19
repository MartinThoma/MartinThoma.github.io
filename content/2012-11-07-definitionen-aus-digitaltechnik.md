---
layout: post
title: Definitionen aus Digitaltechnik
slug: definitionen-aus-digitaltechnik
lang: de
author: Martin Thoma
date: 2012-11-07 13:33:53.000000000 +01:00
category: German posts
tags: Digitaltechnik
---
<div class="info">Dieser Blogpost ist vor allem für Hörer von Prof. Dr. Asfour im WS 2012 / 2013 interessant. Ich höre momentan die Vorlesung bei ihm. Deshalb sind die Inhalte teilweise identisch oder zumindest sehr ähnlich.</div>

Dieser Blogpost soll nur möglichst gute Definitionen liefern. Ich werde ihn vermutlich bis zum Ende des Semesters immer wieder erweitern.

<h2>Boolesche Algebra</h2>
<a href="http://de.wikipedia.org/wiki/Konjunktion_(Logik)">Konjunktion</a>: $\land$
<a href="http://de.wikipedia.org/wiki/Disjunktion">Disjunktion</a>: $\lor$

<div class="definition">Sei $x$ eine Variable.
L heißt <strong>Literal</strong> $:\Leftrightarrow L \in \{x, \bar x\}$.</div>

<div class="definition">Seien $L_1, \dots, L_n$ Literale.
$K(x_1, \dots, x_n)$ heißt ein <strong>Produktterm</strong> $:\Leftrightarrow K(x_1, \dots, x_n) = \bigwedge_{i=1}^n L_i$ oder $K = 1$ oder $K=0$.</div>

Jeder Produktterm $K(x_1, \dots, x_n)$ kann so dargestellt werden, dass eine Variable $x$ in höchstens einem Literal vorkommt.

<div class="definition">Sei $K(x_1, \dots, x_n)$ ein Produktterm und $y(x_1, \dots x_n)$ eine boolesche Funktion.
$K$ heißt <strong>Implikant</strong> von $y :\Leftrightarrow (K \Rightarrow y)$</div>

<div class="definition">Sei $K(x_1, \dots, x_n)$ ein Implikant der  boolesche Funktion $y(x_1, \dots x_n)$.
$K$ heißt <strong>Minterm</strong> von $y :\Leftrightarrow$ Für jede Variable $x_i$ in $y$ kommt genau ein mal in $K$ als Literal vor.</div>

<div class="definition">Sei $y(x_1, \dots x_n)$ eine boolesche Funktion und $x$ ein boolescher Ausdruck, der $y$ entspricht.

$x$ heißt <strong>disjunktive Normalform</strong> (DNF) von $y :\Leftrightarrow$
$x=\bigvee_{i=0}^k K_i, \; k \leq 2^n - 1:\quad K_i \neq K_j \Leftrightarrow i \neq j$</div>

<div class="definition">Sei $D(x_1, \dots, x_m)$ eine Disjunktion von Literalen $\bigvee_{i=1}^m L_i$ oder die Konstante &bdquo;0&ldquo; oder die Konstante &bdquo;1&ldquo;. Sei weiter $y(x_1, \dots x_n)$ eine boolesche Funktion.

$D$ heißt <strong>Implikat</strong> von $y :\Leftrightarrow \bar D \Rightarrow \bar y$</div>

Summenterm ist ein Synonym zu Implikat.

<div class="definition">Sei $y(x_1, \dots x_n)$ eine boolesche Funktion und $D$ ein Implikat von $y$.

$D$ heißt <strong>Maxterm</strong> von $y :\Leftrightarrow$ Ein Literal jeder Variable $x_i$ der Funktion $y$ kommt in $D$ genau einmal vor.</div>

Beispiele:
<table class="wikitable">
<tr>
  <th>&nbsp;</th>
  <th>Minterm</th>
  <th>Maxterm</th>
</tr>
<tr>
  <td>0</td>
  <td>$\bar a \bar b \bar c$</td>
  <td>$a \lor b \lor c$</td>
</tr>
<tr>
  <td>1</td>
  <td>$a \bar b \bar c$</td>
  <td>$\bar a \lor b \lor c$</td>
</tr>
<tr>
  <td>2</td>
  <td>$\bar a b \bar c$</td>
  <td>$a \lor \bar b \lor c$</td>
</tr>
<tr>
  <td>3</td>
  <td>$a b \bar c$</td>
  <td>$\bar a \lor \bar b \lor c$</td>
</tr>
<tr>
  <td>4</td>
  <td>$\bar a \bar b c$</td>
  <td>$a \lor b \lor \bar c$</td>
</tr>
<tr>
  <td>5</td>
  <td>$a \bar b c$</td>
  <td>$\bar a \lor b \lor \bar c$</td>
</tr>
<tr>
  <td>6</td>
  <td>$\bar a b c$</td>
  <td>$a \lor \bar b \lor \bar c$</td>
</tr>
<tr>
  <td>0</td>
  <td>$a b c$</td>
  <td>$\bar a \lor \bar b \lor \bar c$</td>
</tr>
</table>

<div class="definition">Ein boolescher Ausdruck der Form
$\bigwedge_i \bigvee_j (\neg)x_{ij}$
wird <strong>konjunktive Normalform</strong> (KNF) genannt.</div>
