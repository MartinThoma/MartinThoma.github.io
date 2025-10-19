---
layout: post
title: Gauß'sche Zahlen und verwandte Ringe
slug: gaussche-zahlen-und-verwandte-ringe
lang: de
author: Martin Thoma
date: 2013-09-04 09:16:41.000000000 +02:00
category: Mathematics
tags: Algebra
featured_image: 2013/08/algebra-thumb.jpg
---
Sei $\mathbb{Z}[\sqrt{z}]$ mit $z \in \mathbb{Z}$ der kleinste Ring, der $\mathbb{Z}$ und $\sqrt{z}$ enthält.
Sei $A := \{a + b \sqrt{z} | a, b \in \mathbb{Z}\}$.

<strong>Behauptung</strong>: $\mathbb{Z}[\sqrt{z}] = A$
<strong>Beweis</strong>: z.Z.: $\mathbb{Z}[\sqrt{z}] \subseteq A$ und $\mathbb{Z}[\sqrt{z}] \supseteq A$

Zuerst zeige ich $\mathbb{Z}[\sqrt{z}] \supseteq A$:

<ul>
<li>$\mathbb{Z}[\sqrt{z}]$ enthält $\mathbb{Z} \Rightarrow \{a \in \mathbb{Z}\} \subseteq \mathbb{Z}[\sqrt{z}]$</li>
<li>$\mathbb{Z}[\sqrt{z}]$ enthält $\sqrt{z} \Rightarrow \{\sqrt{z}\} \subseteq \mathbb{Z}[\sqrt{z}]$</li>
<li>$\mathbb{Z}[\sqrt{z}]$ ist ein Ring, also ist $(\mathbb{Z}[\sqrt{z}], +)$ eine abelsche Gruppe.</li>
<li>$\Rightarrow A \subseteq \mathbb{Z}[\sqrt{z}]$</li>
</ul>

Nun $\mathbb{Z}[\sqrt{z}] \subseteq A$:
<ul>
<li>$(A, +) \leq (\mathbb{R}, +)$, denn (UG-Kriterium)
  <ul>
    <li>$0 = 0 + 0 \sqrt{z} \in A \Rightarrow A \neq \emptyset$</li>
    <li>$\forall (a+b \sqrt{z}), (c + d \sqrt{z}) \in A:$ $(a+b\sqrt{z}) - (c+d\sqrt{z}) = \underbrace{(a-c)}_{\in \mathbb{Z}} + \underbrace{(b-d)}_{\in \mathbb{Z}} \sqrt{z} \in A$</li>
  </ul>
</li>
<li>$(A, +)$ ist abelsch, da $(\mathbb{R}, +)$ abelsch ist</li>
<li>$(A, \cdot)$ ist Untermonoid von $(\mathbb{R}, \cdot)$, denn
  <ul>
    <li>$1 = 1 + 0 \sqrt{z} \in A$</li>
    <li>$\forall (a+b \sqrt{z}), (c + d \sqrt{z}) \in A:$
        $(a+b\sqrt{z}) \cdot (c+ d\sqrt{z}) = \underbrace{(ac + z bd)}_{\in \mathbb{Z}} + \underbrace{(ad + bc)}_{\in \mathbb{Z}} \sqrt{z} \in A$</li>
  </ul>
</li>
<li>Distributivgesetze: Vererben sich aus $(\mathbb{R}, \cdot)$</li>
<li>$\Rightarrow \mathbb{Z}[\sqrt{z}] \subseteq A$</li>
</ul>

$\Rightarrow \mathbb{Z}[\sqrt{z}] = A \blacksquare$
