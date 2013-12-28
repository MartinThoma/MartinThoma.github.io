---
layout: post
title: Mathematische Strukturen
author: Martin Thoma
date: 2013-06-16 18:14:57.000000000 +02:00
categories:
- German posts
tags:
- mathematics
- Algebra
featured_image: 2012/01/vector-space.png
---
Es gibt einen ganzen Haufen an mathematischen Strukturen. Dieser Artikel soll jeweils die Definition und bekannte Beispiele sammeln. Weitere Strukturen bzw. Beispiele k&ouml;nnen gerne in den Kommentaren genannt werden.

<h2>Magma</h2>
<div class="definition">Sei $M$ eine Menge und $*:M \times M \rightarrow M$ eine auf $M$ abgeschlossene Abbildung. Dann hei&szlig;t $(M,*)$ ein <strong>Magma</strong>.</div>

<div class="definition">Sei $(M,*)$ ein Magma.
$(M,*)$ hei&szlig;t <strong>kommutativ</strong> $:\Leftrightarrow \forall a, b \in M: a*b = b*a$.</div>

Ein Synonym zu &bdquo;kommutativ&ldquo; ist &bdquo;abelsch&ldquo;.

Beispiele:
<ul>
  <li>Jede Halbgruppe ist auch ein Magma.</li>
  <li>$(\mathbb{Z}, -)$ ist ein Magma, aber keine Halbgruppe:
      $1-(1-1) = 1-0 = 1 \neq -1 = 0-1 = (1-1)-1$</li>
  <li>$(\mathbb{R} \setminus \{0\}, : )$ ist ein Magma, aber keine Halbgruppe:
      $1 : (7:7)=1:1=1 \neq \frac{1}{49} = \frac{1}{7} : 7 = (1:7):7$</li>
</ul>

Gegenbeispiele:
<ul>
  <li>$(\mathbb{N}, : )$ ist nicht abgeschlossen, also kein Magma.</li>
  <li>$(\mathbb{N}, - )$ ist nicht abgeschlossen, also kein Magma.</li>
</ul>

<h2>Halbgruppe</h2>
<div class="definition">Sei $(M, *)$ ein Magma.
$(M, *)$ hei&szlig;t <strong>Halbgruppe</strong> $:\Leftrightarrow (M, *)$ ist assoziativ.</div>

Eine Verkn&uuml;pfung $*$ ist genau dann assoziativ auf einer Menge $M$, wenn gilt:
$\forall a,b,c \in M: (a*b)*c = a*(b*c)$

Beispiele:
<ul>
  <li>Jedes Monoid ist auch eine Halbgruppe.</li>
  <li>$(\mathbb{N}_{\geq 1}, +)$ ist eine Halbgruppe, aber kein Monoid.</li>
</ul>

<h2>Monoid</h2>
<div class="definition">Sei $(M, *)$ eine Halbgruppe.
$(M, *)$ hei&szlig;t <strong>Monoid</strong> $:\Leftrightarrow (M, *)$ hat ein neutrales Element $e_M$</div>

Ein Element $e_M \in M$ hei&szlig;t genau dann neutral, wenn gilt:
$\forall a \in M: e_M * a = a * e_M = a$

Beispiele:
<ul>
  <li>Jede Gruppe ist auch ein Monoid.</li>
  <li>$(\mathbb{N}_{0}, +)$ ist mit 0 als Neutralelement ein Monoid, aber keine Gruppe.</li>
  <li>$(\mathbb{N}_{0}, \cdot)$ ist mit 1 als Neutralelement ein Monoid, aber keine Gruppe.</li>
  <li>$(\mathbb{Z}, \cdot)$ ist mit 1 als Neutralelement ein Monoid, aber keine Gruppe.</li>
</ul>

<h2>Gruppe</h2>
<div class="definition">Sei $(M, *)$ ein Monoid.
$(M, *)$ hei&szlig;t <strong>Gruppe</strong> $:\Leftrightarrow \forall a \in M: \exists a^{-1} \in M: a * a^{-1} = a^{-1} * a = e_M$ </div>

Beispiele:
<ul>
  <li>Jeder Ring $(R, +, \cdot)$ beinhaltet eine Gruppe $(R, +)$.</li>
  <li>$(\mathbb{Q}, +)$</li>
  <li>$(\mathbb{R}, +)$</li>
  <li>$(\mathbb{Q} \setminus \{0\}, \cdot)$</li>
  <li>$(\mathbb{R} \setminus \{0\}, \cdot)$</li>
</ul>


<h2>Ring</h2>
<div class="definition">Sei $R$ eine Menge und $+:R \times R \rightarrow R$, $\cdot:R \times R \rightarrow R$ Verkn&uuml;pfungen darauf.

$(R, +, \cdot)$ hei&szlig;t <strong>Ring</strong> $:\Leftrightarrow$
<ul>
  <li>$(R,+)$ ist eine kommutative Gruppe (das Neutralelement hei&szlig;e 0),</li>
  <li>$(R,\cdot)$ ist eine Halbgruppe und</li>
  <li>die Distributivgesetze sind erf&uuml;llt.</li>
</ul>
</div>

Die Distributivgesetze lauten:

$\forall a,b,c,d \in R: (a+b) \cdot c = ac + bc$

und

$\forall a,b,c,d \in R: a \cdot (c+d) = ac + ad$

Au&szlig;erdem:

<div class="definition">Sei $(R,+,\cdot)$ ein Ring.
$(R,+,\cdot)$ hei&szlig;t <strong>Ring mit Eins</strong> $:\Leftrightarrow (R, \cdot)$ ist Monoid.
</div>

<div class="definition">Sei $(R,+,\cdot)$ ein Ring.
$(R,+,\cdot)$ hei&szlig;t <strong>kommutativer Ring</strong> $:\Leftrightarrow (R, \cdot)$ ist kommutativ.
</div>

Beispiele:
<ul>
  <li>Jeder K&ouml;rper ist auch ein Ring.</li>
  <li>$(\mathbb{Z}, +, \cdot)$ ist ein kommutativer Ring mit Eins, aber kein K&ouml;rper. Es fehlen die Inversen bei der Multiplikation.</li>
</ul>


<h2>K&ouml;rper</h2>
<div class="definition">Sei $(K, +, \cdot)$ ein kommutativer Ring mit Eins.
$(K, +, \cdot)$ hei&szlig;t <strong>K&ouml;rper</strong> $:\Leftrightarrow$
<ul>
  <li>$(K,+)$ ist kommutativ.</li>
  <li>$(K \setminus \{0\}, \cdot)$ ist kommutative Gruppe.</li>
</ul>
</div>

Beispiele:
<ul>
  <li>$(\mathbb{Q}, +, \cdot)$</li>
  <li>$(\mathbb{R}, +, \cdot)$</li>
  <li>$(\mathbb{C}, +, \cdot)$</li>
  <li>$(\mathbb{Z} / p \mathbb{Z}, +, \cdot)$, wobei $p$ eine Primzahl ist</li>
</ul>

<h2>Modul</h2>
<div class="definition">Sei $(R, +_R, \cdot_R)$ ein Ring und $(M, +_M)$ eine kommutative Gruppe.

Au&szlig;erdem sei 

$\cdot_V: R \times M \rightarrow M$

eine Abbildung.

$(M, R, \cdot_V)$ hei&szlig;t <strong>R-Modul</strong> $:\Leftrightarrow \forall \lambda, \mu \in R \; x,y \in M:$
<ul>
  <li>$1_R \cdot x = x$</li>
  <li>$\lambda \cdot (\mu \cdot x) = (\lambda \cdot \mu) \cdot x$</li>
  <li>$(\lambda + \mu) \cdot x = \lambda \cdot x + \mu \cdot x$</li>
  <li>$\lambda \cdot (x+y) = \lambda \cdot x + \lambda \cdot y$</li>
</ul>
</div>

Beispiele:
<ul>
  <li>Jeder K-Vektorraum ist auch ein K-Modul.</li>
  <li>Das $\mathbb{Z}$-Modul $\mathbb{Z}/2 \mathbb{Z}$ ist ein Modul ohne Basis, also kein Vektorraum.</li>
</ul>


<h2>Vektorraum</h2>
<div class="definition">Sei $(K, +_K, \cdot_K)$ ein K&ouml;rper und $(V,+_V)$ eine kommutative Gruppe.
Au&szlig;erdem sei 

$\cdot_V: K \times V \rightarrow V$

eine <strong>skalalre Multiplikation</strong>.

$(V, K, \cdot_V)$ hei&szlig;t <strong>$K$-Vektorraum</strong> $:\Leftrightarrow \forall \lambda, \mu \in K \; x,y \in V:$
<ul>
  <li>$1_K \cdot x = x$</li>
  <li>$\lambda \cdot (\mu \cdot x) = (\lambda \cdot \mu) \cdot x$</li>
  <li>$(\lambda + \mu) \cdot x = \lambda \cdot x + \mu \cdot x$</li>
  <li>$\lambda \cdot (x+y) = \lambda \cdot x + \lambda \cdot y$</li>
</ul>
</div>

Beispiele:
<ul>
  <li>$(\mathbb{R}[X], \mathbb{R}, \cdot_V)$: Der Vektorraum der polynome mit Koeffizienten aus $\mathbb{R}$.</li>
</ul>

<h2>Weitere</h2>
<h3>Ideal</h3>
<div class="definition">Ein Ideal in einem Ring $(R, +, \cdot)$ ist eine Teilmenge $I \subseteq R$, die bez&uuml;glich der Addition eine Untergruppe ist und die folgende Eigenschaft hat:

$\forall x \in I, r \in R: xr \in I \text{ und } rx \in I$</div>

Beispiele:
<ul>
  <li>Kerne von Ringhomomorphismen sind immer Ideale. (Und Ideale sind Kerne von Ringhomomorphismen.)</li>
</ul>

<h3>Algebra</h3>
<div class="definition">Es sei $R$ ein Ring. Eine $R$-Algebra ist ein Ring $A$ zusammen mit einem Ringhomomorphismus $\sigma: R \rightarrow A$, sodass gilt:

$\forall r \in R, a \in A: \sigma(r) \cdot a = a \cdot \sigma(r)$</div>

Beispiele:
<ul>
  <li>Jeder Ring ist eine $\mathbb{Z}$-Algebra.</li>
</ul>

<h3>Integrit&auml;tsring</h3>
<div class="definition">Es sei $R$ ein vom Null-Ring verschiedener Ring. 

$R$ hei&szlig;t integrit&auml;tsring $:\Leftrightarrow R$ ist kommuativ und Nullteilerfrei.</div>

Beispiele:
<ul>
  <li>Zu dem Ring $(\mathbb{Z}, +, \cdot)$ ist $(\mathbb{Q}, +, \cdot)$ ein Quotientenk&ouml;rper.</li>
</ul>

<h3>Hauptidealring</h3>
<div class="definition">Es sei $R$ ein Integrit&auml;tsring. 

$R$ hei&szlig;t Hauptidealring $:\Leftrightarrow$ Jedes Ideal $I \subseteq R$ ist ein Hauptideal.</div>

<h3>Quotientenk&ouml;rper</h3>
<div class="definition">Es sei $R$ ein Integrit&auml;tsring. Der kleinste K&ouml;rper, in den $R$ eingebettet werden kann, wird der Quotientenk&ouml;rper des Integrit&auml;tsrings genannt.</div>

Beispiele:
<ul>
  <li>Jeder K&ouml;rper ist ein Integrit&auml;tsring.</li>
  <li>$(\mathbb{Z}, +, \cdot)$</li>
</ul>

<h2>Hilfsbegriffe</h2>
<h3>Ideal</h3>
<div class="definition">Sei $(R, +, \cdot)$ ein Ring und $I \subseteq R$.

$I$ hei&szlig;t Ideal $:\Leftrightarrow$ 
<ol style="list-style-type:lower-roman">
  <li>$(I, +)$ ist eine Gruppe,</li>
  <li>$\forall r \in R \forall a \in I: r \cdot a \in I$ und</li>
  <li>$\forall r \in R \forall a \in I: a \cdot r \in I$.</li>
</ol></div>

Beispiele:
<ul>
  <li>Die Menge $2\mathbb{Z}$ der geraden ganzen Zahlen ist ein Ideal im Ring$(\mathbb{Z}, +, \cdot)$.</li>
</ul>

<h3>Hauptideal</h3>
<div class="definition">Sei $(R, +, \cdot)$ ein Ring und $I \subseteq R$ ein Ideal.

$I$ hei&szlig;t Hauptideal $:\Leftrightarrow I$ wird von einem Element erzeugt.</div>

Beispiele:
<ul>
  <li>$n\mathbb{Z}$</li>
</ul>

<h3>Primideal</h3>
<div class="definition">Sei $(R, +, \cdot)$ ein Ring und $I \subsetneq R$ ein Ideal.

$I$ hei&szlig;t Primideal in $R :\Leftrightarrow \forall x, y \in R: xy \in I \Rightarrow x \in I \lor y \in I$</div>

Beispiele:
<ul>
  <li>$2\mathbb{Z}$ ist Primideal in $(\mathbb{Z}, +, \cdot)$</li>
</ul>

<h3>Maximales Ideal</h3>
<div class="definition">Sei $(R, +, \cdot)$ ein Ring und $I \subsetneq R$ ein Ideal.

$I$ hei&szlig;t maximales Ideal in $R :\Leftrightarrow$ Es gibt kein Ideal $J$, f&uuml;r das gilt: $I \subsetneq J \subsetneq R$</div>

Beispiele:
<ul>
  <li>In $(\mathbb{Z},+,\cdot)$ ist jedes Primideal maximal.</li>
</ul>
