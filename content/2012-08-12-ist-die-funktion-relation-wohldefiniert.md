---
layout: post
title: Ist die Funktion / Relation wohldefiniert?
slug: ist-die-funktion-relation-wohldefiniert
lang: de
author: Martin Thoma
date: 2012-08-12 17:00:14.000000000 +02:00
category: Cyberculture
tags: mathematics
featured_image: 2012/08/pi-thumbnail.png
---
Ich verstehe unter einer wohldefinierten Funktion / Relation die Unabhängigkeit von den Repräsentanten. Wikipedia sagt dazu:

<blockquote>Man kann in der Mathematik ein Objekt nicht nur durch eine Definitionsgleichung (explizit), sondern auch durch eine charakteristische Eigenschaft (implizit) definieren. Während eine explizite Definition immer zulässig ist, ist eine implizite Definition nur unter der Bedingung zulässig, dass es tatsächlich genau ein Objekt mit der angegebenen Eigenschaft gibt. Diese Bedingung nennt man die Wohldefiniertheit der impliziten Definition.</blockquote>
Quelle: <a href="http://de.wikipedia.org/wiki/Wohldefiniertheit">Wohldefiniertheit</a>

<h2>Beispiel 1</h2>
Sei $f:\mathbb{Q} \rightarrow \mathbb{Q}$ eine Abbildung und definiert durch:

$f(\frac{p}{q}) := \frac{p}{q}$

<strong>Frage</strong>: Ist $f$ wohldefiniert?
<strong>Antwort</strong>: Ja.
Es sei $\frac{p'}{q'}$ die vollständig gekürzte Darstellung von $\frac{p}{q}$.
Also gilt: $p = p' \cdot \lambda \land q = q' \cdot \lambda$ mit $\lambda \in \mathbb{R} \setminus \{0\}$.
$\Rightarrow \frac{p}{q} = \frac{p' \cdot \lambda}{q' \cdot \lambda}$.
$\Rightarrow f(\frac{p}{q}) = \frac{p' \cdot \lambda}{q' \cdot \lambda} = \frac{p'}{q'}$.
$\Rightarrow f(\frac{p}{q})$ ist unabhängig vom Repräsentanten.
$\Rightarrow f$ ist wohldefiniert $\blacksquare$

<h2>Beispiel 2</h2>
Sei $f:\mathbb{Q} \rightarrow \mathbb{Q}$ eine Abbildung und definiert durch:

$f(\frac{p}{q}) := \frac{p+1}{q}$

<strong>Frage</strong>: Ist $f$ wohldefiniert?
<strong>Antwort</strong>: Nein.

$f(\frac{0}{1}) = \frac{0+1}{1} = 1 \neq \frac{1}{2} = \frac{0+1}{2} = f(\frac{0}{2}) \blacksquare$

<h2>Beispiel 3</h2>
Sei $f:\mathbb{Q} \rightarrow \mathbb{Q}$ eine Abbildung und definiert durch:

$f(\frac{p}{q}) := \frac{p-q}{p+q}$

<strong>Frage</strong>: Ist $f$ wohldefiniert?
<strong>Antwort</strong>: Ja.

Es sei $\frac{p'}{q'}$ die vollständig gekürzte Darstellung von $\frac{p}{q}$.
Also gilt: $p = p' \cdot \lambda \land q = q' \cdot \lambda$ mit $\lambda \in \mathbb{R} \setminus \{0\}$.

$\Rightarrow f(\frac{p}{q}) = f(\frac{\lambda \cdot p'}{\lambda \cdot q'}) = \frac{\lambda \cdot p' - \lambda \cdot q'}{\lambda \cdot p' + \lambda \cdot q'} = \frac{\lambda (p' - q')}{\lambda (p' + q')} = \frac{p' - q'}{p' + q'} \blacksquare$
