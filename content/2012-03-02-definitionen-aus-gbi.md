---
layout: post
title: Definitionen aus GBI
slug: definitionen-aus-gbi
lang: de
author: Martin Thoma
date: 2012-03-02 16:16:02.000000000 +01:00
category: German posts
tags: lecture-notes, KIT, Theoretical computer science, GBI
featured_image: 2011/10/deterministic-finite-state-machine-thumb.png
---
<h2>Formale Sprachen</h2>
A heißt Alphabet $:\Leftrightarrow$ A ist eine endliche, nicht leere Menge aus Zeichen.
w heißt Wort aus $A^*  : \Leftrightarrow$ w ist eine endliche Aneinanderreihung von Zeichen aus A
L heißt formale Sprache $: \Leftrightarrow L \subseteq A^*$
G heißt formale Grammatik $: \Leftrightarrow G = (N, T, S, P)$ wobei:
<ul>
  <li>N die endliche Menge der Nichtterminalsymbole bezeichne, </li>
  <li>T die endliche Menge der Terminalsymbole mit $N \cap T = \emptyset$ bezeichne,</li>
  <li>$S \in N$ das Startsymbol,</li>
  <li>$P \subseteq N \times (N \cup T)^*$ die endliche Menge der Produktionen bezeichne.</li>
</ul>

Es seien $L_1$ und $L_2$ formale Sprachen und $n \in \mathbb{N}$. Dann:

$L_1 \cdot L_2 :\Leftrightarrow \{w_1 w_2 | w_1 \in L_1 \land w_2 \in L_2\}$
$L_1 \cup L_2 :\Leftrightarrow \{w | w \in L_1 \lor w \in L_2\}$
$L_1 \cap L_2 :\Leftrightarrow \{w | w \in L_1 \land w \in L_2\}$
$L_1 \setminus L_2 :\Leftrightarrow \{w | w \in L_1 \land w \notin L_2\}$
$L_1^0 :\Leftrightarrow \{ \varepsilon\}$
$L_1^1 :\Leftrightarrow L$
$L_1^n :\Leftrightarrow L_1^{n-1} \cdot L_1$
$L_1^* :\Leftrightarrow \bigcup_{i=0}^\infty L_1^i$
$L_1^+ :\Leftrightarrow L_1^* \setminus L_1^0 = \bigcup_{i=1}^\infty L_1^i$

<h3>Kodierungstheorie</h3>
Seien $L_A, L_B$ formale Sprachen und $c: L_A \rightarrow L_B$.

c heißt codierung $: \Leftrightarrow$ c ist injektiv.
$L_B$ heißt präfixfrei $: \Leftrightarrow \forall_{u, v, w \in L_B}: uv = w \Rightarrow u = \varepsilon \lor v = \varepsilon$

Sei $h:A* \rightarrow B*$ eine Abbildung.
h  heißt Homomorphismus $:\Leftrightarrow h(\varepsilon) = \varepsilon \land \forall_{x \in A} \forall_{w \in A*}: h(xw) = h(x)h(w)$

<h2>Abbildungen und Relationen</h2>
Seien A und B Mengen.

R heißt binäre Relation von A in B $:\Leftrightarrow R \subseteq A \times B$

Sei im Folgendem R eine binäre Relation von A in B.

R ist linkstotal $:\Leftrightarrow \forall_{a \in A} : \exists_{b \in B} : (a, b) \in R$
R ist rechtseindeutig $:\Leftrightarrow \forall_{a \in A} : \forall_{b_1, b_2 \in B: b_1 \neq b_2} : (a, b_1) \in R \Rightarrow (a, b_2) \notin R$
R heißt Abbildung $:\Leftrightarrow$ R ist linkstotal und rechtseindeutig.
Für Abbildungen schreibt man auch: $R: A \rightarrow B$.

R heißt linkseindeutig $:\Leftrightarrow \forall_{(a_1, b_1) \in R} : \forall_{(a_2, b_2) \in R} : (a_1, b_1) \in R \Rightarrow (a_2, b_2) \notin R$
R heißt injektiv $:\Leftrightarrow$ R ist eine linkseindeutige Abbildung.
R heißt rechtstotal $:\Leftrightarrow \forall_{b \in B} : \exists_{a \in A} : (a, b) \in R$
R heißt surjektiv $:\Leftrightarrow$ R ist eine rechtstotale Abbildung.
R heißt bijektiv $:\Leftrightarrow$ R ist eine injektive und surjektive Abbildung

R heißt reflexiv $:\Leftrightarrow \forall_{x \in A} : (x, x) \in R$
R heißt symmetrisch $:\Leftrightarrow (x, y) \in R \rightarrow (y, x) \in R$
R heißt antisymmetrisch $:\Leftrightarrow (x, y) \in R \land (y, x) \in R \Rightarrow x = y$
R heißt transitiv $:\Leftrightarrow (x, y) \in R \land (y, z) \in R \Rightarrow (x, z) \in R$

R heißt Halbordnung $:\Leftrightarrow$ R ist reflexiv, antisymmetrisch und transitiv.
Eine Halbordnung ist ein Spezialfall der Ordnungsrelation.

R heißt Äquivalenzrelation $:\Leftrightarrow$ R ist reflexiv, symmetrisch und transitiv.

Sei C eine Menge und $S \subseteq B \times C$.
$S \circ R = \{(x,z) \in M_1 \times M_3 | \exists y \in M_2: (x, y) \in R \land (y, z) \in S\}$

Sei M eine Menge und $R \subseteq M \times M$ eine Halbordnung. Dann heißt M halbgeordnet bzw. $(M, R)$ halbgeordnete Menge. Sei $T \subseteq M$.
$x \in T$ heißt minimales Element von T $:\Leftrightarrow$ Es gibt kein $y \in T$ mit xRy und $x \neq y$.
$x \in T$ heißt kleinstes Element von T $:\Leftrightarrow$ $\forall_{y \in T}: xRy$.
Das maximale Element und das größte Element werden analog definiert.

R heißt vollständige Halbordnung $:\Leftrightarrow$ R ist eine Halbordnung, besitzt ein kleinstes Element und jede aufsteigende Kette besitzt ein Supremum.
R heißt Totalordnung $:\Leftrightarrow \forall_{a,b \in M} : aRb \lor bRa$

Sei $\equiv \subseteq M \times M$ eine Äquivalenzrelation, $f : M \rightarrow M$ eine Funktion und $\diamond$ eine binäre Operation auf der Menge M.
$f$ heißt verträglich $: \Leftrightarrow \forall_{x,y \in M} : x \equiv y \Rightarrow f(x) \equiv f(y)$
$\diamond$ heißt verträglich $: \Leftrightarrow \forall_{x_1, x_2,y_1, y_2 \in M} : x_1 \equiv x_2 \land y_1 \equiv y_2 \Rightarrow x_1 \diamond y_1 \equiv x_2 \diamond y_2$

<h2>Komplexitätstheorie</h2>
Seien $f : \mathbb{N_0} \rightarrow \mathbb{R}^+, g : \mathbb{N_0} \rightarrow \mathbb{R}^+$ Funktionen, die die Laufzeit von Algorithmen beschreiben.

${\cal O}(f(n)) = \{g(n) | \exists_{n_0 \in \mathbb{N}_0} : \exists_{c \in \mathbb{R}^+} : \forall_{n \geq n_0}: g(n) \leq c \cdot f(n)\}$
$\Omega(f(n)) = \{g(n) | \exists_{n_0 \in \mathbb{N}_0} : \exists_{c \in \mathbb{R}^+} : \forall_{n \geq n_0}: g(n) \geq c \cdot f(n)\}$
$\Theta(f(n)) = \Omega(f(n)) \cap {\cal O}(f(n))$

<h2>Graphentheorie</h2>
G heißt Graph $: \Leftrightarrow G = (V, E)$, wobei V eine endliche Menge an Knoten ist und $E \subseteq V \times V$ die Menge der Kanten bezeichne.

Sei G = (V, E) ein Graph.
G heißt ungerichteter Graph $: \Leftrightarrow \forall_{v_n, v_m \in V} : (v_n, v_m) \in E \Rightarrow (v_m, v_n) \in E$
G heißt gerichteter Graph $: \Leftrightarrow$ G ist nicht ungerichtet.
G heißt streng zusammenhängend $: \Leftrightarrow \forall_{x, y \in V}:$ Es gibt einen Pfad von x nach y.
G heißt vollständig $: \Leftrightarrow \forall_{x, y \in V}: (x, y) \in E$

p heißt Pfad in G von $v_0$ nach $v_n: \Leftrightarrow p = (v_0, ..., v_n): \forall_{i \in \mathbb{G}_n}: (v_i, v_{i+1}) \in E $

Ein Knoten $r \in V$ heißt Wurzel $: \Leftrightarrow \forall_{x \in V}:$ Es gibt genau einen Pfad von r nach x.
G heißt Baum $: \Leftrightarrow \exists r \in V: \forall_{x \in V}$ Es gibt genau einen Pfad von r nach x.
