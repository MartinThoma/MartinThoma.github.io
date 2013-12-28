---
layout: post
title: Why is the intersection of two normal subgroups a normal subgroup?
author: Martin Thoma
date: 2013-08-25 18:04:56.000000000 +02:00
categories:
- Mathematics
tags:
- mathematics
- Algebra
featured_image: 2013/08/algebra-thumb.jpg
---
Let $(G, \cdot)$ be a group and $X \lhd G$ and $Y \lhd G$ be two normal subgroups.

I will show this in two steps:
<ol>
  <li>Show that $X \cap Y$ is a group</li>
  <li>Show that $X \cap Y$ is a normal group of $(G, \cdot)$</li>
</ol>

<h2>Intersection of two subgroups is a subgroup</h2>
<strong>Theorem</strong>: $(X \cap Y) \leq G$
<strong>Proof</strong>:

$X \cap Y$ is not empty:
$e_G \in X \land e_G \in Y \Rightarrow e_G \in (X \cap Y)$

$X \cap Y$ has inverse elements. Let $a \in (X \cap Y)$. As a is in $X$ and $X$ is a group, $a^{-1} \in X$. The same is true for $Y$. So: 
$\forall a \in (X \cap Y) \exists a^{-1} \in (X \cap Y): a \cdot a^{-1} = a^{-1} \cdot a = e_G$

$\forall a,b \in (X \cap Y): a \cdot b^{-1} \in (X \cap Y)$, because both, $a$ and $b^{-1}$ are in $X$. As $X$ is a group, the result has to be in $X$. Same argumentation for $Y$. Then the result is in $X$ and $Y \blacksquare$

<h2>Intersection of two normal subgroups is normal</h2>
First the definition of a normal subgroup:
<div class="definition">Let $N \leq G$ be a subgroup of $G$.

$N \lhd G :\Leftrightarrow \forall n \in N \forall g \in G: g \cdot n \cdot g^{-1} \in N$</div>

<strong>Theorem</strong>: $(X \cap Y) \lhd G$

<strong>Proof</strong>: 

$X \cap Y$ is a subgroup of $G$ as I have proved above. 

$\forall n \in (X \cap Y) \forall g \in G: g \cdot n \cdot g^{-1} \in X$ and
$\forall n \in (X \cap Y) \forall g \in G: g \cdot n \cdot g^{-1} \in Y$

$\Rightarrow \forall n \in (X \cap Y) \forall g \in G: g \cdot n \cdot g^{-1} \in (X \cap Y)$

$\Rightarrow (X \cap Y) \lhd G \blacksquare$
