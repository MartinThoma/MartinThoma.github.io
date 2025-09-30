---
layout: post
lang: de
title: Beweise aus der booleschen Algebra
slug: beweise-aus-der-booleschen-algebra
author: Martin Thoma
date: 2012-11-08 13:18:09.000000000 +01:00
category: German posts
tags: mathematics, Boolean algebra
---
## Definition
Edward Vermilye Huntington hat eine sehr kompakte Definition boolescher
Algebren erarbeitet:

Sei $B$ eine Menge und $\sqcap: B \times B \rightarrow B$ sowie
$\sqcup: B \times B \rightarrow B$ Verkn&uuml;fungen auf B.

Weiter gelte:

<strong>H1: Kommutativgesetze</strong>
<ul style="list-style-type:none;">
  <li>$\forall a,b \in B: a \sqcap b = b \sqcap a$</li>
  <li>$\forall a,b \in B: a \sqcup b = b \sqcup a$</li>
</ul>

<strong>H2: Distributivgesetze</strong>
<ul style="list-style-type:none;">
  <li>$\forall a,b,c \in B: a \sqcap (b \sqcup c) = (a \sqcap b) \sqcup (a \sqcap c)$</li>
  <li>$\forall a,b,c \in B: a \sqcup (b \sqcap c) = (a \sqcup b) \sqcup (a \sqcap c)$</li>
</ul>

<strong>H3: Neutrale Elemente</strong>
<ul style="list-style-type:none;">
  <li>$\exists e \in B \forall a \in B: a \sqcap e = a$ (e wird Einselement genannt)</li>
  <li>$\exists n \in B \forall a \in B: a \sqcup n = a$ (n wird Nullelement genannt)</li>
</ul>

<strong>H4: Komplement&auml;re Elemente</strong>
<ul style="list-style-type:none;">
  <li>$\forall a \in B: \exists \bar a: a \sqcap \bar a = n \land a \sqcup \bar a = e$</li>
</ul>

Dann wird $(B, \sqcap, \sqcup)$ eine boolesche Algebra gennant.

## Folgerungen
Sei im folgendem immer $\mathcal{B} = (B, \sqcap, \sqcup)$ eine boolesche
Algebra mit dem Einselement &bdquo;1&ldquo; und dem Nullelement
&bdquo;0&ldquo;.

### Eindeutigkeit des Nullelements
<u>Behauptung:</u> Es exisitiert genau ein Nullelement f&uuml;r $\mathcal{B}$.<br/>
<u>Beweis:</u> direkt

Die Existenz von mindestens einem Nullelement wird durch H3 garantiert.

Seien $n_1, n_2$ Nullelemente auf $\mathcal{B}$. Dann gilt:

\begin{align}
                           & \forall a \in B: a \sqcup n_1 \stackrel{H3}{=} a\\
\Rightarrow                & n_2 \sqcup n_1 = n_2\\
\stackrel{H3}{\Rightarrow} & n_1 = n_2 \blacksquare
\end{align}

### Eindeutigkeit des Einselements
<u>Behauptung:</u> Es exisitiert genau ein Einselement f&uuml;r $\mathcal{B}$.<br/>
<u>Beweis:</u> direkt

Die Existenz von mindestens einem Einselement wird durch H3 garantiert.

Seien $e_1, e_2$ Einselemente auf $\mathcal{B}$. Dann gilt:

\begin{align}
                           & \forall a \in B: a \sqcap e_1 \stackrel{H3}{=} a\\
\Rightarrow                & e_2 \sqcup e_1 = e_2\\
\stackrel{H3}{\Rightarrow} & e_1 = e_2 \blacksquare
\end{align}

### Eindeutigkeit der komplement&auml;ren Elemente
<u>Behauptung:</u> Die komplement&auml;ren Elemente bzgl. $\sqcup$ sind eindeutig<br/>
<u>Beweis:</u> direkt<br/>
Sei $a \in B$ beliebig und es gelte:<br/>
$a \sqcup \bar a_1 = 0$ und $a \sqcup \bar a_2 = 0$ sowie<br/>
$a \sqcap \bar a_1 = 1$ und $a \sqcap \bar a_2 = 1$

Schritt 1<br/>
Es gilt:

\begin{align}
 \bar a_1 \sqcap (a \sqcup \bar a_2) &\stackrel{H2}{=} (\bar a_1 \sqcap a) \sqcup (\bar a_1 \sqcap \bar a_2)\\
\Leftrightarrow \bar a_1 \sqcap 1    &= 0 \sqcup (\bar a_1 \sqcap \bar a_2)\\
\Leftrightarrow \bar a_1             &= \bar a_1 \sqcap \bar a_2
\end{align}

Schritt 2<br/>
Au&szlig;erdem gilt:

\begin{align}
\bar a_2 \sqcap (a \sqcup \bar a_1) &\stackrel{H2}{=} (\bar a_2 \sqcap a) \sqcup (\bar a_2 \sqcap \bar a_1)\\
\Leftrightarrow \bar a_2 \sqcap 1   &= 0 \sqcup (\bar a_2 \sqcap \bar a_1)\\
\Leftrightarrow \bar a_2            &= (\bar a_2 \sqcap \bar a_1) \stackrel{H1}{=} \bar a_1 \sqcap \bar a_2
\end{align}

Aus den Ergebnissen von Schritt 1 und Schritt 2 folgt:
$\bar a_1 = \bar a_2$.

Das bedeutet, zu jedem $a \in B$ existiert genau ein Komplement. $\blacksquare$


### Nullelement ungleich Einselement
<u>Behauptung:</u> $0 \neq 1$<br/>
<u>Beweis:</u><br/>
Wegen (H3) und (H4) gilt:
<ul>
  <li>$\exists 1 \in B \forall a \in B: a \sqcap 1 \stackrel{H1}{=} 1 \sqcap a = a$</li>
  <li>$\exists 0 \in B \forall a \in B: a \sqcup 0 \stackrel{H1}{=} 0 \sqcup a = a$</li>
  <li>$\forall a \in B: \exists \bar a \in B: a \sqcap \bar a \stackrel{H1}{=} 0$</li>
  <li>$\forall a \in B: \exists \bar a \in B: a \sqcup \bar a \stackrel{H1}{=} 1$</li>
</ul>

Annahme: 1 = 0<br/>
$\Rightarrow \forall a \in B: \exists \bar a \in B = a \sqcap \bar a = a \sqcup \bar a = 0 = 1$

Hmmm ... irgendwie konnte man $(0 = 1) \Rightarrow (\sqcap = \sqcup)$ zeigen
... aber wie genau?

### Extremalgesetze
$\forall a \in B: 1 \sqcup a = 1$
$\forall a \in B: 0 \sqcap a = 0$

Wie beweist man das?

### Absorptionsgesetz

#### Version 1
<u>Voraussetzungen:</u> Sei $\mathcal{B} = (B, \sqcap, \sqcup)$ eine boolesche Algebra.<br/>
<u>Behauptung:</u> $\forall a, b \in B: a \sqcup (a \sqcap b) = a$<br/>
<u>Beweis:</u> direkt

$a \sqcup (a \sqcap b) \stackrel{H3}{=} (a \sqcap 1) \sqcup (a \sqcap b) \stackrel{H3}{=} a \sqcap (1 \sqcup b) \stackrel{\text{Extremalgesetze}}{=} a \sqcap 1 \stackrel{H3}{=} a$

#### Version 2
<u>Voraussetzungen:</u> Sei $\mathcal{B} = (B, \sqcap, \sqcup)$ eine boolesche Algebra.<br/>
<u>Behauptung:</u> $\forall a, b \in B: a \sqcap (a \sqcup b) = a$<br/>
<u>Beweis:</u> Duale Aussage zu Version 1<br/>

#### Version 3
<u>Voraussetzungen:</u> Sei $\mathcal{B} = (B, \sqcap, \sqcup)$ eine boolesche Algebra.<br/>
<u>Behauptung:</u> $\forall a, b \in B: a \sqcup (\bar a \sqcap b) \stackrel{H2}{=} a \sqcup b$<br/>
<u>Beweis:</u> direkt<br/>
$a \sqcup (\bar a \sqcap b) \stackrel{H2}{=} (a \sqcup \bar a) \sqcap (a \sqcup b) \stackrel{H4}{=} 1 \sqcap (a \sqcup b) \stackrel{H3}{=} a \sqcup b \blacksquare$

## Körper
Ist jede Boolesche Algebra ein K&ouml;rper?

Ein K&ouml;rper ist eine Menge $V$ mit zwei Verkn&uuml;pfungen
$\oplus, \otimes$: $(V, \oplus, \otimes)$, f&uuml;r den gilt:
<ul>
  <li>$(K, \oplus)$ ist abelsche Gruppe mit neutralem Element 0</li>
  <li>$(K \setminus \{0\}, \otimes)$ ist abelsche Gruppe mit neutralem Element 1</li>
  <li>Es gelten die Distributivgesetze:
    <ul>
      <li>$\forall a, b, c \in V: a\cdot (b+c) = a\cdot b+a\cdot c$</li>
      <li>$\forall a, b, c \in V: (a+b)\cdot c= a\cdot c+b\cdot c$</li>
    </ul>
  </li>
</ul>

Es scheint relativ offensichtlich, dass jede boolesche Algebra ein K&ouml;rper
ist. Allerdings muss man aufpassen. F&uuml;r die neutrale Elemente eines
K&ouml;rpers $K = (V, \oplus, \otimes)$ muss gelten:

<ul>
    <li>$\forall a: 0 \oplus a = a$</li>
    <li>$\forall a: 1 \otimes a = a$</li>
</ul>

F&uuml;r eine boolesche Algebra $\mathcal{B} = (B, \sqcap, \sqcup)$ muss gelten
(H3):

<ul>
  <li>$\exists 1 \in B \forall a \in B: a \sqcap 1 = a$</li>
  <li>$\exists 0 \in B \forall a \in B: a \sqcup 0 = a$</li>
</ul>


F&uuml;r die Inversen von $K$ muss gelten:

<ul>
  <li>$\forall a \exists \bar a: a \oplus \bar a = 0$</li>
  <li>$\forall a \exists \bar a: a \otimes \bar a = 1$</li>
</ul>


F&uuml;r die Komplemente von $\mathcal{B}$ muss gelten:

<ul>
  <li>$\forall a \in B: \exists \bar a: a \sqcap \bar a = 0$</li>
  <li>$\forall a \in B: \exists \bar a: a \sqcup \bar a = 1$</li>
</ul>

Das Komplement eines Elements verkn&uuml;fpft mit $\sqcap$ ergibt also das
neutrale Element von $\sqcup$!

Offensichtlich ist, dass die Schaltalgebra mit den Operatoren XOR und AND, also
$(\{0,1\}, XOR, AND)$ ein K&ouml;rper ist, da Sie offensichtlich isomorph zu
$\mathbb{Z}/2\mathbb{Z}$ ist.

<u>Behauptung:</u> Alle booleschen Algebren mit drei oder mehr Elementen sind keine K&ouml;rper<br/>
<u>Beweis:</u> (<a href="http://de.wikipedia.org/wiki/Diskussion:Darstellungssatz_f%C3%BCr_Boolesche_Algebren#Beziehung zu K&ouml;rpern">danke an Chricho</a>)
Sei $\mathcal{B} = (B, \sqcap, \sqcup)$ mit $|B| \geq 3$. Sei $a \in B$ mit $0 \neq a \neq 1$.
<br/>
Es gilt:<br/>
$\forall b \in B: a \land b \leq a \lneq 1 \Rightarrow a$ hat kein Inverses $\Rightarrow \mathcal{B}$ ist kein K&ouml;rper $\blacksquare$


## Boolesche Algebren und die Schaltalgebra
Die wohl bekannteste boolesche Algebra ist die Schaltalgebra:
$(\{0,1\}, \lor, \land, 0, 1)$

Allerdings ist nicht jede Boolesche Algebra eine Schaltalgebra!

## Quellen

<ul>
  <li>Skript &bdquo;Technische Informatik - Digitaltechnik und Entwurfsverfahren&ldquo; von Dr.-Ing. Tamim Asfour. S.33 - 37</li>
  <li><a href="http://ti.ira.uka.de/TI-1/Vorlesung/Vorlesung.php">Folien</a> von Dr.-Ing. Tamim Asfour</li>
  <li><a href="http://youtu.be/2G-MQPKylPA?t=38m12s">Vorlesung</a> von Dr.-Ing. Tamim Asfour</li>
</ul>
