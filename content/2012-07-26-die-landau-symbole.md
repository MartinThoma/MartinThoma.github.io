---
layout: post
lang: de
title: Die Landau-Symbole
slug: die-landau-symbole
author: Martin Thoma
date: 2012-07-26 08:41:08.000000000 +02:00
category: German posts
tags: algorithms, Big-O
featured_image: 2012/07/landau-thumb.png
---
<h2>Definitionen</h2>
$
\begin{eqnarray*}
  {\cal O}(g(n)) &:= \{f(n) | \exists_{c > 0} \exists_{n_0 > 0} \forall_{n \geq n_0}: f(n) < c \cdot g(n) \} \\
  {\cal o}(g(n)) &:= \{f(n) | \forall_{c > 0} \exists_{n_0 > 0} \forall_{n \geq n_0}: f(n) < c \cdot g(n) \} \\
  \Omega (g(n))  &:= \{f(n) | \exists_{c > 0} \exists_{n_0 > 0} \forall_{n \geq n_0}: f(n) > c \cdot g(n) \} \\
  \omega (g(n))  &:= \{f(n) | \forall_{c > 0} \exists_{n_0 > 0} \forall_{n \geq n_0}: f(n) > c \cdot g(n) \} \\
\end{eqnarray*}
$
$\Theta (g(n))  := \{f(n) | \exists_{c_0 > 0} \exists_{c_1 > 0} \exists_{n_0 > 0} \forall_{n > n_0}: c_0 \cdot g(n) < f(n) < c_1 \cdot g(n) \}$

<h2>Wichtige Aussagen der Mengen</h2>
\begin{align}
f(n) \in {\cal O}(g(n)) &\Leftrightarrow g(n) \in \Omega(f(n)) \\
f(n) \in {\cal o}(g(n)) &\Leftrightarrow g(n) \in \omega(f(n)) \\
f(n) \in {\cal O}(g(n)) \land f(n) \in \Omega(g(n)) &\Leftrightarrow f(n) \in \Theta(g(n)) \\
f(n) \in o(g(n))        &\Leftrightarrow \lim \frac{f(n)}{g(n)} = 0 \\
f(n) \in \Theta ( g(n)) &\Leftrightarrow g(n) \in \Theta(f(n)) \\
f(n) \in \omega(g(n))   &\Leftrightarrow \lim \frac{g(n)}{f(n)} = 0
\end{align}

<h2>Logarithmusgesetze</h2>
\begin{align}
  \log(x \cdot y)   &= \log(x) + \log(y) \\
  \log(\frac{x}{y}) &= \log(x) &ndash; \log(y) \\
  \log(x^r)         &= r \cdot \log(x)
\end{align}


<h2>Wichtige Beziehungen von Funktionen</h2>
${\cal O}(1) \subsetneq {\cal O}(\log n) \subsetneq {\cal O}(n) \subsetneq {\cal O}(n^{2.1}) \subsetneq {\cal O} \subsetneq (n^{2.2}) {\cal O}(n^{100}) \subsetneq {\cal O}(n!) \subsetneq {\cal O}(2^n)$
${\cal O}(2^n) \subsetneq {\cal O}(2^{2n}) \subsetneq {\cal O}(3^n) \subsetneq {\cal O}(n^n) \subsetneq {\cal O}(n^{(n^2)}) \subsetneq$

<h2>Beispiele</h2>
Im Folgenden gelte immer:
$f: \mathbb{N} \rightarrow \mathbb{R^+}$ und $g:\mathbb{N} \rightarrow \mathbb{R^+}$

<h3>Nummer 1</h3>
<strong>Voraussetzungen</strong>:
Sei $f(n) := \sqrt{2}^{\lg(n)}$ und $g(n) := n \cdot \lg(n)$.
<strong>Behauptung</strong>: $f \in {\cal O}(g(n))$
<strong>Beweis</strong>:
$f(n) = \sqrt{2}^{\lg(n)} = 10^{\lg(\sqrt{2}^{\lg(n)})} = 10^{\lg(\sqrt{2}) \cdot \lg(n)} = n^{\lg(\sqrt{2})}= n^{\frac{1}{2} \cdot \lg(2)} < n^1 = n$

Es gilt: $n \in {\cal O}(n \cdot \lg(n)) = {\cal O}(g(n))$
$\Rightarrow f(n) \in {\cal O}(g(n)) \blacksquare$

<h3>Nummber 2</h3>
<strong>Voraussetzungen</strong>:
Sei $f(n) := \sqrt{5}^{\log_3(n)}$ und $g(n) := n^2$.
<strong>Behauptung</strong>: $f \in {\cal o}(g(n))$
<strong>Beweis</strong>:
$f(n) = \sqrt{5}^{\log_3(n)} = 3^{\log_3(\sqrt{5}^{\log_3(n)})} = 3^{\log_3(5) \cdot \log_3(n)} = n^{\log_3(5)} < n^{\log_3(9)} = n^{\log_3(3^2)} = n^2$

Sei $\varepsilon > 0$. Dann gilt:
$n^{2- \varepsilon} \in o(n^2) \Rightarrow f(n) \in o(g(n)) \blacksquare$
