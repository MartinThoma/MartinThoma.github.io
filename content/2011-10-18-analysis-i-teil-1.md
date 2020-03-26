---
layout: post
title: Analysis I - Teil 1
author: Martin Thoma
date: 2011-10-18 17:50:21.000000000 +02:00
category: German posts
tags: mathematics, lecture-notes
featured_image: 2012/07/math-symbol-thumb.png
---
<h2>Begriffe und Bezeichnungen</h2>
<h3>Mengen</h3>
Es seien M und N Mengen.

$M \cup N$: Vereinigung - Die Elemente sind in M oder N
$M \cap N$: Durchschnitt ("Schnittmenge") - Die Elemente sind in M und N
$M \setminus N$: Differenzmenge - Die Elemente sind in M aber nicht in N
$M \subseteq N$: Teilmenge - Alle Elemente in M sind auch in N
$\emptyset$: Leere Menge
$a \in M$: a ist ein Element von M
$a \notin M$: a ist kein Element von M

<h3>Funktionen</h3>
Seien M, N Mengen mit $M \neq \emptyset \neq N$.
$f: \underbrace{M}_{\mathbb{D}} \to \underbrace{N}_{\mathbb{W}}$

<h3>Logische Zeichen</h3>
$\Rightarrow$: Implikation, z.B. $A \Rightarrow B$: Aus A folgt B<br/>
$\Leftrightarrow$: &Auml;quivalenz. $A \Rightarrow B \wedge B \Rightarrow A$: Aus A folgt B und umgekehrt.<br/>
$\underbrace{: \Leftrightarrow}_\text{"genau dann"}$, z.B. $M \subseteq N : \Leftrightarrow \text{aus } x \in M \text{ folgt stets } x \in N$.<br/>
$\forall$: <a href="http://de.wikipedia.org/wiki/Existenzquantor#Existenz-_und_Allquantor">Allquantor</a>, sprich "f&uuml;r alle" oder "f&uuml;r jedes"<br/>
$\exists$: <a href="http://de.wikipedia.org/wiki/Existenzquantor#Existenz-_und_Allquantor">Existenzquantor</a>, sprich "es gibt mindestens ein" oder "es existiert"

<h2>Reele Zahlen</h2>
Die Grundmenge der Analysis ist die Menge $\mathbb{R}$, die Menge der reelen Zahlen. Diese f&uuml;hren wir durch die folgenden 15 Axiome ein.

<h3>K&ouml;rperaxiome</h3>
In $\mathbb{R}$ seien zwei Verkn&uuml;pfungen "+" und "&middot;" gegeben. Sie ordnen jedem Paar $a, b \in \mathbb{R}$ genau ein $ab := a \cdot b \in \mathbb{R}$ zu. Dabei soll gelten:

$$\left. \begin{array}{lllll}
A.1 & a+    (b+c)  & = & (a+b)+c      & \forall a, b, c \in \mathbb{R} \\
A.2 & a \cdot (bc) & = & (ab) \cdot c & \forall a, b, c \in \mathbb{R} \\
\end{array} \right \} \text{Assoziativgesetze}$$

$$\left. \begin{array}{lllll}
A.3 & a  +    b & = & b  +     a & \forall a, b \in \mathbb{R} \\
A.4 & a \cdot b & = & b) \cdot a & \forall a, b \in \mathbb{R} \\
\end{array} \right \} \text{Kommutativgesetze}$$


$$\left. \begin{array}{lllll}
A.5 & \exists 0 \in \mathbb{R} & : & a +     0 = a                  & \forall a \in \mathbb{R} \text{ ("Null")} \\
A.6 & \exists 1 \in \mathbb{R} & : & a \cdot 1 = a  \wedge 1 \neq 0 & \forall a \in \mathbb{R} \text{ ("Eins")} \\
\end{array} \right \} \text{Neutrales Element}$$

$$\left. \begin{array}{lllll}
A.7 & \forall a \in \mathbb{R} \exists -a \in \mathbb{R} & : & a + (-a) = 0 \\
A.8 & \forall a \in \mathbb{R} \setminus {0} \exists -a^{-1} \in \mathbb{R} & : & a \cdot a^{-1} = 1
\end{array} \right \} \text{Inverses Element}$$

$$\text{A.9 } a(b+c) = ab+ac \forall a, b, c \in \mathbb{R}$: Distributivgesetz$

Schreibweisen: f&uuml;r $a, b \in \mathbb{R}: a -b := a + (-b)$
f&uuml;r $b \neq 0: \frac{a}{b} := a \cdot b^{-1}$

Alle Rechenregeln bzgl der Grundrechenarten lassen sich aus A.1 - A.9 herleiten. Diese Regeln seien von nun an bekannt.

<strong>Behauptung</strong>: Es existiert genau ein $0 \in \mathbb{R}: a+0 = a \forall a \in \mathbb{R}$
<strong>Beweis</strong>:
Existenz: folgt aus A.5
Eindeutigkeit: Sei $\tilde 0 \in \mathbb{R} \text{ mit }a+\tilde 0 a \forall a \in \mathbb{R}$
Mit $a = 0: 0 = 0 + \tilde 0 \underbrace{=}_{\text{A.3}} \tilde 0 + 0 \underbrace{=}_{\text{A.5}} = \tilde 0$

<strong>Behauptung</strong>: Ist $a \in \mathbb{R}\text{, so ist }a \cdot 0 = 0$
<strong>Beweis</strong>: $ b := a \cdot 0 \underbrace{\Rightarrow}_\text{A.5} b = a (0 + 0) \Rightarrow a \cdot 0 + a \cdot 0 = b + b$
$0 = b + (-b) = (b+b) + (-b) = b + (b + (-b)) = b + 0 = b$

<h3>Anordnungsaxiome</h3>
In $\mathbb{R}$ sei eine Relation "$\leq$" gegeben. Dabei soll gelten:

$$
\begin{array}{lll}
A.10 & a \leq b \lor  b \leq a & \forall a, b \in \mathbb{R} \\
A.11 & a \leq b \land b \leq a & \rightarrow a = b \\
A.12 & a \leq b \land b \leq c & \rightarrow a \leq c \\
A.13 & a \leq b \rightarrow a + c \leq b + c & \forall c \in \mathbb{R} \\
A.14 & a \leq b \land 0 \leq c \Rightarrow a \leq c
\end{array}
$$

Schreibweise:
$a \geq b: \Leftrightarrow b \geq a$
$a \lt b: \Leftrightarrow a \leq b \land a \neq b$
$a \gt b: \Leftrightarrow b \lt a$

Alle Regeln f&uuml;r Ungleichungen lassen sich aus A.1 - A.14 herleiten. Diese Regeln seien nun bekannt.

<strong>Definition</strong>: F&uuml;r $a \in \mathbb{R}$ sei
$$|a| : =
\left \{ \begin{array}{ll}
a  & \text{, falls } a \geq 0 \\
-a & \text{, falls } a \lt 0
\end{array}
\right.$$

Anschaulich: Der Betrag misst den absoluten Abstand zur 0 auf dem Zahlenstrahl.

$|a-b| \mathrel{\widehat{=}} \text{Abstand von a und b}$

<strong>Satz</strong>: Seien $a, b \in \mathbb{R}$. Dann:
<ul>
  <li>$|a| \geq 0$</li>
  <li>$|ab| = |a| \cdot |b|$</li>
  <li>$\pm a \leq |a|$</li>
  <li>$|a+b| \leq |a| + |b|$: Dreiecksungleichung</li>
  <li>$| |a| - |b| | \leq | a-b|$</li>
</ul>

<strong>Beweis</strong>: 1, 2, 3 leichte &Uuml;bung<br/>
<strong>Beweis von 4.</strong>:<br/>
Fall 1: $a+b \geq 0$. Dann $|a+b| = a + b \leq |a| + |b|$
Fall 2: $a+b \lt 0$. Dann $|a+b| = -(a+b) = (-a) + (-b) \leq |a| + |b|$<br/>
<strong>Beweis von 5.</strong>:<br/>
$c := |a| - |b|$. Es ist $|a| = |a - b + b| \leq |a - b | + |b| \Rightarrow |a| - |b| \leq |a - b|$, also $c \leq |a - b|$

Analog: $ -c = |b| - |a| \leq |b-a| = |a - b|$.
Es ist $| |a| - |b| | = c \text{ oder } = -c$.

<h3>Intervalle</h3>
Seien $a, b \in \mathbb{R} \land a \lt b$.

$(a,b)      := \{x \in \mathbb{R} a \lt  x \lt  b\}$: offenes Intervall<br/>
$[a,b]      := \{x \in \mathbb{R} a \leq x \leq b\}$: geschlossenes Intervall<br/>
$(a,b]      := \{x \in \mathbb{R} a \lt x \leq b\}$: halboffenes Intervall<br/>
$[a,\infty) := \{x \in \mathbb{R} a \leq x \}$.<br/>
$(a,\infty) := \{x \in \mathbb{R} a \lt x \}$.<br/>
$(-\infty,a]:= \{x \in \mathbb{R} x \leq a \}$.<br/>
$(-\infty,\infty):= \mathbb{R}$.<br/>
$[a,a]:= \{a\}$: entartetes Intervall
