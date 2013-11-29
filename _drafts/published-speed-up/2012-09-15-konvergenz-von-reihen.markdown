---
layout: post
status: publish
published: true
title: Konvergenz von Reihen
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 41881
wordpress_url: http://martin-thoma.com/?p=41881
date: 2012-09-15 09:02:02.000000000 +02:00
categories:
- German posts
tags:
- mathematics
- analysis
comments: []
---
Die folgenden Definitionen sind wortw&ouml;rtlich aus dem <a href="http://mitschriebwiki.nomeata.de/Ana1.pdf">inoffiziellem Skript f&uuml;r Analysis I</a> bei Herrn Dr. Schmoeger &uuml;bernommen worden.

<h2>Dreiecksungleichung</h2>
<div class="definition">Ist $\sum_{n=1}^{\infty}a_n$ absolut konvergent, so ist $\sum_{n=1}^{\infty}a_n$ konvergent und es gilt:
$\left | \sum_{n=1}^{\infty}a_n \right | \leq \sum_{n=1}^{\infty} |a_n|$</div>

<h2>Leibniz-Kriterium</h2>
<div class="definition">Sei $(a_n)_{n \in \mathbb{N}}$ eine monoton fallende, reelle Nullfolge. Dann konvergiert die alternierende Reihe
$s = \sum_{n=0}^\infty (-1)^n a_n$.</div>

<h2>Wurzelkriterium</h2>
<div class="definition">Sei $(a_n)$ eine Folge und $\alpha := \lim \sup \sqrt[n]{|a_n|}$.

<ol>
  <li>$\alpha < 1 \Rightarrow \sum_{n=1}^{\infty} a_n$ konvergiert absolut</li>
  <li>$\alpha > 1 \Rightarrow \sum_{n=1}^{\infty} a_n$ divergiert</li>
  <li>$\alpha = 1 \Rightarrow$ keine Aussage &uuml;ber die Konvergenz von $\sum_{n=1}^{\infty} a_n$ m&ouml;glich</li>
</ol>
</div>

<h2>Majorantenkriterium</h2>
<div class="definition">Gilt $|a_n| \leq b_n ~\text{ffa } n \in \mathbb{N}$ und ist $\sum_{n=1}^{\infty} b_n$ konvergent, so gilt:
$\sum_{n=1}^{\infty} a_n$ ist absolut konvergent.</div>

<h2>Minorantenkriterium</h2>
<div class="definition">Gilt $a_n \geq b_n \geq 0 ~\text{ffa } n \in \mathbb{N}$ und ist $\sum_{n=1}^{\infty} b_n$ divergent, so gilt:
$\sum_{n=1}^{\infty} a_n$ ist divergent.</div>

<h2>Quotientenkriterium</h2>
<div class="definition">Sei $(a_n)$ eine Folge in $\mathbb{R}$ und $a_n \ne 0 \text{ ffa } \mathbb{N}$. $\alpha_n := \frac{a_{n+1}}{a_n}$ (ffa $n \in \mathbb{N}$).
<ul>
  <li>Ist $|\alpha_n| \ge 1 \text{ ffa } n \in \mathbb{N} \Rightarrow \sum a_n$ ist divergent.</li>
  <li>Es sei $(\alpha_n)$ beschr&auml;nkt, $\beta := \liminf |\alpha_n|$ und $\alpha := \limsup |\alpha_n|$.</li>
   <ul>
    <li>Ist $\beta > 1 \Rightarrow \sum a_n$ ist divergent.</li>
    <li>Ist $\alpha < 1 \Rightarrow \sum a_n$ ist absolut konvergent.</li>
    <li>Ist $\alpha = \beta = 1$, so ist keine allgemeine Aussage m&ouml;glich.</li>
   </ul>
  </li>
</ul></div>
