---
layout: post
status: publish
published: true
title: Eine Sprache ist nicht regul&auml;r - Beweis mit dem Pumping-Lemma
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 8491
wordpress_url: http://martin-thoma.com/?p=8491
date: 2011-11-10 16:05:33.000000000 +01:00
categories:
- German posts
tags:
- Computer science
- mathematics
- proof
- Theoretical computer science
comments:
- id: 44331
  author: ! 'Sprachen, Automaten und Grammatiken: Ein &Uuml;berblick'
  author_email: ''
  author_url: http://martin-thoma.com/sprachen-automaten-und-grammatiken/
  date: !binary |-
    MjAxMi0wMi0xMSAxODo1Mjo0MSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMi0xMSAxNjo1Mjo0MSArMDEwMA==
  content: ! '[...] (Leftrightarrow) Es existiert ein regul&auml;rer Ausdruck f&uuml;r
    L. L ist regul&auml;r (Rightarrow) Das Pumping-Lemma ist [...]'
- id: 49681
  author: S&ouml;ren
  author_email: soeren@soeren.de
  author_url: http://soeren.de
  date: !binary |-
    MjAxMi0wMi0xOSAyMzoxMDo1OCArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMi0xOSAyMToxMDo1OCArMDEwMA==
  content: ! "Hallo Martin,\r\n\r\nwas ist denn der grundlegende Unterschied zwischen
    Ogdens und Pumping Lemma? Mir ist bewusst, dass das Ogdens Lemma (OL) eine verallgemeinerte
    Form des Pumping Lemmas (PL) ist, aber gibt es nicht kontextfreie Grammatiken,
    die ich mit dem OL, aber nicht mit dem PL zeigen kann?\r\n\r\nGr&uuml;&szlig;e\r\nS&ouml;ren"
- id: 49981
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wMi0yMCAxMjozOTo0OSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMi0yMCAxMDozOTo0OSArMDEwMA==
  content: ! "Hallo S&ouml;ren,\r\n\r\nja, ich glaube es gibt Sprachen bei denen man
    mit Ogdens Lemma zeigen kann, dass sie nicht kontextfrei sind, jedoch nicht mit
    dem Pumping-Lemma. Allerdings habe ich noch kein Beispiel gefunden. Wenn ich eins
    habe, stelle ich es hier ein und schreibe noch einen kurzen Kommentar.\r\n\r\nBitte
    hinterlasst doch einen Kommentar, falls jemand eine nicht-kontextfreie Sprache
    kennt, die Ogdens Lemma nicht erf&uuml;llt!\r\n\r\nViele Gr&uuml;&szlig;e,\r\nMartin"
featured_image: 2011/10/deterministic-finite-state-machine-thumb.png
---
Regul&auml;re Sprachen k&ouml;nnen von endlichen Automaten erkannt werden. Das bedeutet, dass eine endliche Anzahl an Zust&auml;nden ausreicht, um ein Wort der Sprache zu akzeptieren. Wenn also eine Sprache $L = \{a^i b^{2i} | i \in \mathbb{N}\}$ beschrieben wird, m&uuml;sste gez&auml;hlt werden, wie oft a vorkommt. a kann aber beliebig oft vorkommen. Das ist ein Indiz daf&uuml;r, dass es sich nicht um eine regul&auml;re Sprache handelt.

Das <a href="http://de.wikipedia.org/wiki/Pumping-Lemma">Pumping-Lemma</a> ist ein notwendiges, aber kein hinreichendes Kriterium f&uuml;r regul&auml;re Sprachen. Daraus folgt, dass eine nicht-regul&auml;re Sprache eventuell durch das Lemma entlarvt werden kann. Allerdings muss nicht jede Sprache, die das Pumping-Lemma erf&uuml;llt, regul&auml;r sein.

Dies kann man durch einen Widerspruchsbeweis zeigen. Dabei nimmt man an, dass die Behauptung falsch ist. Dann zeigt man, dass man durch die Annahme zu einem Widerspruch kommt.

<h2>Beispiel</h2>
<strong>Voraussetzung</strong>: 

$L_2 = \{a^i b^j c^k | i \lt j \lt k\}$.

<strong>Behauptung</strong>: $L_2$ ist nicht regul&auml;r.

<strong>Beweis</strong>: (durch Widerspruch)

<strong>Annahme</strong>: $L_2$ sei regul&auml;r.

Aus dem Pumping-Lemma folgt: 
$\exists n \in \mathbb{N}: \forall w \in \{w \in L_2 | |w| \geq n\}: $
$\exists \text{ Darstellung } uvx = w \text{ mit } v \neq \varepsilon \land |uv| \leq n$ f&uuml;r die gilt:

$uv^i x \in L_2 \forall i \in \mathbb{N}_0$

In Worten: Wenn man ein Wort in L hat, dass mindestens so lang ist wie ein bestimmtes n, dann kann man dieses Wort in Teilworte u, v und x zerlegen. Bei dieser Zerlegung ist v niemals leer. Wenn man nun den Teil des Wortes, der in v steckt wiederholt, muss das Wort immer noch in $L_2$ sein.

Sei $n \in \mathbb{N}$ die Konstante aus dem Pumping-Lemma.

Betrachte nun $w = a^n b^{n+1} c^{n+2}$. Offensichtlich gilt $w \in L_2$. Da $|uv| \leq n$ muss in v mindestens ein a sein. 

$\Rightarrow uv^2 x = a^{n+2 \cdot i} b^{n+1} c^{n+2}, i \geq 1 $
$\Rightarrow uv^2x \notin L_2 $
$\Rightarrow \text{Widerspruch} $
$\Rightarrow \text{Die Annahme war falsch.} $
$\Rightarrow L_2$ ist nicht regul&auml;r.

<em>Bemerkung</em>: Eigentlich ist es ein Beweis durch Kontraposition. Man wei&szlig;, es gilt:
$L \in {\cal L_3} \Rightarrow $ L erf&uuml;llt das Pumping-Lemma.
Daraus folgt:
L erf&uuml;llt nicht das Pumping-Lemma $\Rightarrow L \notin {\cal L_3}$.
Um zu beweisen, dass L das Pumping-Lemma nicht erf&uuml;llt, benutzt man meist einen Widerspruchsbeweis wie oben.

<h2>Material</h2>
Ich habe mal ein paar <a href='http://martin-thoma.com/wp-content/uploads/2011/11/odgen-pumping.zip'>Beispiele f&uuml;r Ogdens Lemma und das Pumping-Lemma</a> gesammelt.
