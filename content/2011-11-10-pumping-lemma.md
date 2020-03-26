---
layout: post
title: Eine Sprache ist nicht regul&auml;r - Beweis mit dem Pumping-Lemma
slug: pumping-lemma
author: Martin Thoma
date: 2011-11-10 16:05:33.000000000 +01:00
category: German posts
tags: Computer science, mathematics, proof, Theoretical computer science
featured_image: 2011/10/deterministic-finite-state-machine-thumb.png
---
Regul&auml;re Sprachen k&ouml;nnen von endlichen Automaten erkannt werden. Das bedeutet, dass eine endliche Anzahl an Zust&auml;nden ausreicht, um ein Wort der Sprache zu akzeptieren. Wenn also eine Sprache $L = \{a^i b^{2i} | i \in \mathbb{N}\}$ beschrieben wird, müsste gez&auml;hlt werden, wie oft a vorkommt. a kann aber beliebig oft vorkommen. Das ist ein Indiz dafür, dass es sich nicht um eine regul&auml;re Sprache handelt.

Das <a href="http://de.wikipedia.org/wiki/Pumping-Lemma">Pumping-Lemma</a> ist ein notwendiges, aber kein hinreichendes Kriterium für regul&auml;re Sprachen. Daraus folgt, dass eine nicht-regul&auml;re Sprache eventuell durch das Lemma entlarvt werden kann. Allerdings muss nicht jede Sprache, die das Pumping-Lemma erfüllt, regul&auml;r sein.

Dies kann man durch einen Widerspruchsbeweis zeigen. Dabei nimmt man an, dass die Behauptung falsch ist. Dann zeigt man, dass man durch die Annahme zu einem Widerspruch kommt.

<h2>Beispiel</h2>
<strong>Voraussetzung</strong>:

$L_2 = \{a^i b^j c^k | i \lt j \lt k\}$.

<strong>Behauptung</strong>: $L_2$ ist nicht regul&auml;r.

<strong>Beweis</strong>: (durch Widerspruch)

<strong>Annahme</strong>: $L_2$ sei regul&auml;r.

Aus dem Pumping-Lemma folgt:
$\exists n \in \mathbb{N}: \forall w \in \{w \in L_2 | |w| \geq n\}: $
$\exists \text{ Darstellung } uvx = w \text{ mit } v \neq \varepsilon \land |uv| \leq n$ für die gilt:

$uv^i x \in L_2 \forall i \in \mathbb{N}_0$

In Worten: Wenn man ein Wort in L hat, dass mindestens so lang ist wie ein bestimmtes n, dann kann man dieses Wort in Teilworte u, v und x zerlegen. Bei dieser Zerlegung ist v niemals leer. Wenn man nun den Teil des Wortes, der in v steckt wiederholt, muss das Wort immer noch in $L_2$ sein.

Sei $n \in \mathbb{N}$ die Konstante aus dem Pumping-Lemma.

Betrachte nun $w = a^n b^{n+1} c^{n+2}$. Offensichtlich gilt $w \in L_2$. Da $|uv| \leq n$ muss in v mindestens ein a sein.

$\Rightarrow uv^2 x = a^{n+2 \cdot i} b^{n+1} c^{n+2}, i \geq 1 $
$\Rightarrow uv^2x \notin L_2 $
$\Rightarrow \text{Widerspruch} $
$\Rightarrow \text{Die Annahme war falsch.} $
$\Rightarrow L_2$ ist nicht regul&auml;r.

<em>Bemerkung</em>: Eigentlich ist es ein Beweis durch Kontraposition. Man weiß, es gilt:

$L \in {\cal L_3} \Rightarrow$ L erfüllt das Pumping-Lemma.
Daraus folgt:
L erfüllt nicht das Pumping-Lemma $\Rightarrow L \notin {\cal L_3}$.
Um zu beweisen, dass L das Pumping-Lemma nicht erfüllt, benutzt man meist einen Widerspruchsbeweis wie oben.

<h2>Material</h2>
Ich habe mal ein paar <a href='../images/2011/11/odgen-pumping.zip'>Beispiele für Ogdens Lemma und das Pumping-Lemma</a> gesammelt.
