---
layout: post
status: publish
published: true
title: Why is the stabilizer subgroup a subgroup?
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 76329
wordpress_url: http://martin-thoma.com/?p=76329
date: 2013-08-26 11:24:54.000000000 +02:00
categories:
- Mathematics
tags:
- Algebra
comments: []
featured_image: 2013/08/algebra-thumb.jpg
---
<div class="definition">Let $(G, \cdot)$ be a group and $M$ a set. A <strong>group action</strong> is a function:
$G \circ M \rightarrow M$
that satisfies the following two conditions
<ul>
  <li>Identity: $\forall m \in M: e_G \circ m = m$</li>
  <li>Associativity: $\forall g, h \in G, m \in M: (g \cdot h) \circ m= g \circ (h \circ m)$</li>
</ul></div>
<div class="definition">Let $m \in M$. Then $G_m := \{g \in G | g \circ m = m\}$ is called the <strong>stabilizer</strong> of $m$.</div>

<strong>Theorem</strong>: $G_m$ is a group

<strong>Proof</strong>: 

Let $m \in M$.

$\stackrel{identity}{\Rightarrow}e_G \in G_m$

Let $a \in G_m$. This means, that $a \circ m = m$. And $\exists a^{-1} \in G$, as $G$ is a group.
$a^{-1} \cdot a = e_G$, this means $(a^{-1} \cdot a) \circ m = m$. 
$\stackrel{associativity}{\Rightarrow}a^{-1} \circ (a \circ m) = m \Leftrightarrow a^{-1} \circ m = m \Leftrightarrow a^{-1} \in G_m$

Let $a, b \in G_m$. 
Then: $a \circ m = m$ and $b \circ m = m$

$\Rightarrow a \circ (b \circ m) = m$
$\stackrel{associativity}{\Rightarrow} (a \cdot b) \circ m = m \Leftrightarrow (a \cdot b) \in G_m \blacksquare$
