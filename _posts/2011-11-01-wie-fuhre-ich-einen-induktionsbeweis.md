---
layout: post
title: Wie f&uuml;hre ich einen Induktionsbeweis?
author: Martin Thoma
date: 2011-11-01 01:29:35.000000000 +01:00
category: German posts
tags: mathematics, lecture-notes, Mathematical induction, Structural induction
featured_image: 2011/10/eulers-formula.png
---
Der Induktionsbeweis eignet sich h&auml;ufig, wenn es um Aussagen &uuml;ber die Nat&uuml;rlichen Zahlen $\mathbb{N}$ geht, allerdings kann er auch f&uuml;r die ganzen Zahlen $\mathbb{Z}$ verwendet werden.

<h2>Prinzip</h2>
Der Gedanke hinter dem Induktionsbeweis ist, dass man sehr leicht f&uuml;r ein einzelnes Element zeigen kann, dass eine Aussage gilt. Diese Aussage ist die Behauptung. Dann zeigt man allgemein, wenn die Aussage f&uuml;r eine Zahl gilt muss sie auch f&uuml;r die n&auml;chste Zahl gelten.

Wenn man also f&uuml;r n = 1 zeigt dass die Aussage A(n) korrekt ist, dann gilt sie f&uuml;r alle positiven Zahlen.

<h2>Aufbau</h2>
<ul>
  <li><strong>Induktionsanfang</strong> (I.A.): 
Zeige, dass die Aussage f&uuml;r ein bestimmtes $n_0$ (also z.B. $n_0 = 0$) gilt. Daf&uuml;r muss man einfach nur einsetzen.</li>
  <li><strong>Induktionsvorraussetzung</strong> (I.V.)): 
"Sei $n \in \mathbb{N}$ beliebig, aber fest und es gelte: <Aussage>"</li>
  <li><strong>Induktionsschluss</strong> (I.S.): 
Ausgehend von I.V. ist zu zeigen, dass die Aussage f&uuml;r $n_0 + 1$ gilt.</li>
</ul>

<h2>Beispiele</h2>
<h3>Identit&auml;ten</h3>
Es gibt viele Identit&auml;ten, die sich gut mit einem Induktionsbeweis zeigen lassen:
Bei den folgenden Identit&auml;ten sei $n \in \mathbb{N}$.

<h4>Gau&szlig;sche Summenformel</h4>
<strong>Behauptung</strong>: $\sum_{k=1}^n k = \frac{1}{2} \cdot n \cdot (n+1)$
<strong>Beweis</strong>: durch vollst&auml;ndige Induktion
<strong>I.A.</strong>: Sei n = 1. Dann: $\sum_{k=1}^1 k = 1 = \frac{1}{2} \cdot 1 \cdot (1+1)$
<strong>I.V.</strong>: Sei $n \in \mathbb{N}$ beliebig, aber fest und es gelte: 
$\sum_{k=1}^n k = \frac{1}{2} \cdot n \cdot (n+1)$
<strong>I.S.</strong>:
$\sum_{k=1}^{n+1} k = \sum_{k=1}^{n} k + (n+1) \stackrel{I.V.}{=} \frac{1}{2} \cdot n \cdot (n+1) + (n+1) = $
$= \frac{1}{2} \cdot (n^2 + n) + (n+1) = \frac{1}{2} \cdot (n^2 + 3n + 2) = \frac{1}{2} \cdot (n+1)(n+2) \blacksquare$

<h4>Weitere</h4>

<ol type="i" style="list-style-type:lower-roman">
  <li>$\sum_{k=1}^n k^3 = \frac{1}{4}n^2 (n+1)^2$</li>
  <li>Fibonacci: $f(m+n) = f(n+1) \cdot f(m) + f(n) \cdot f(m-1)$</li>
</ol>

<h3>Binomischer Satz</h3>
Das folgende habe ich als Mitschrift der Vorlesung "Analysis I" am KIT gemacht:

<div style="background-color:#FFFF66;border:2px solid #FF0000;padding:5px;">
Seien $a, b \in \mathbb{R}.$ Dann gilt f&uuml;r alle $n \in \mathbb{N}$:
$(a+b)^{n+1} = (a+b)(a+b)^n = (a+b) \underbrace{\sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k}_\text{Binomischer Lehrsatz}$
</div>


<strong>I.A.</strong>: $n=1: \sum_{k=0}^{1}\binom{1}{k} a^{1-k} b^k = (a+b)^n$

<strong>I.V.</strong>: Sei $n \in \mathbb{N}$ und es gelte $(a+b)^{n+1} = (a+b)(a+b)^n = (a+b) \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$

<strong>I.S.</strong>: 
$
\begin{align} 
(a+b)^{k+1} &= (a+b)(a+b)^n \\
&= (a+b) \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k \\
&= \sum_{k=0}^{n} \binom{n}{k} a^{n+1-k} b^k + \sum_{k=0}^n \binom{n}{k} a^{n-k} b^{k+1} \\
&= \underbrace{\binom{n}{0}}_{\binom{n+1}{0}} a^{n+1} + \sum_{k=1}^n \binom{n}{k} a^{n+1-k} b^k + \underbrace{\sum_{k=0}^{n-1} \binom{n}{k} a^{n-k} b^{k+1}}_\text{Vorbemerkung} + \binom{n}{n} b^{n+1} \\
&= \binom{n+1}{0} a^{n+1} + \sum_{k=1}^{n} [\binom{n}{k} + \binom{n}{k-1}] a^{n+1} b^k + \binom{n+1}{n+1} b^{n+1} \\
&= \sum_{k=0}^{n+1} \binom{n+1}{k} a^{n+1-k} b^k
\end{align}$

<h3>Rekursive Folgen</h3>
Der Grenzwert rekursiv definierter Folgen l&auml;sst sich h&auml;ufig sehr sch&ouml;n mit mehreren Induktionsbeweisen beweisen.

<ol>
  <li>Finde f&uuml;r dich heraus: Ist die Folge monoton steigend oder fallend? ist 0 oder 1 eine untere / obere Schranke? gibt es andere untere oder obere Schranken?</li>
  <li>Beweise, dass du eine obere / untere Schranke gefunden hast</li>
  <li>Beweise, dass die Folge monoton steigt / f&auml;llt</li>
  <li>Mache den Ansatz: Sei $a$ der Grenzwert der Folge $(a_n)_{n \in \mathbb{N}}$ mit $a_n = f(a_{n-1})$. Dann gilt: $a = f(a)$. L&ouml;se dann nach $a$ auf.</li>
</ol>

Eine Folge in der das wunderbar klappt ist folgende:

Sei $(a_n)_{n \in \mathbb{N}}$ eine Folge und definiert durch:
$a_0 = 2,~~~~~ a_n = \sqrt[3]{a_n^2+a_n-1}$.

<h2>Strukturelle Induktion</h2>
Bei der vollst&auml;ndigen Induktion iteriert man &uuml;ber eine nat&uuml;rliche Zahl und gelangt so, ab einer festen nat&uuml;rlichen Zahl $n_0$ zu jeder beliebigen gr&ouml;&szlig;eren nat&uuml;rlichen Zahl.

Die strukturelle Induktion nutzt allerdings nicht direkt Zahlen, sondern strukturen. Man hat eine sog. "Atomare Struktur" bzw. "Atomares Element", also in einem gewissen Sinn das oder die kleinsten Teilchen, gegeben. Diese Teilchen erf&uuml;llen die Aussage. Nun zeigt man, dass aus den Atomaren Elementen alle Strukturen gebildet werden k&ouml;nnen, &uuml;ber die in der Behauptung die Aussage getroffen wird und dass die Aussage bei jeder neuen Struktur richtig ist.

Insbesondere bietet sich die strukturelle Induktion bei komplexen Graphen, aussagelogischen Formeln und W&ouml;rtern an.

<h3>Beispiele</h3>
<h4>Voller, vollst&auml;ndiger Bin&auml;rbaum</h4>
Sei G(V, E) ein Bin&auml;rbaum.

G ist ein voller Bin&auml;rbaum $: \Leftrightarrow$ alle inneren Knoten von G haben den Verzweigungsgrad 2
G ist ein voller, vollst&auml;ndiger Bin&auml;rbaum $: \Leftrightarrow$ G ist ein voller Bin&auml;rbaum und alle Bl&auml;tter haben die gleiche H&ouml;he

<strong>Behauptung</strong> ${\cal B} (n)$: Jeder volle, vollst&auml;ndige Bin&auml;rbaum der H&ouml;he $n, n \in \mathbb{N}$ hat $2^{n-1} - 1$ innere Knoten.
<strong>Beweis</strong>: durch strukturelle Induktion
<strong>I.A.</strong>: zeige ${\cal B} (1)$. 
Ein voller, vollst&auml;ndiger Bin&auml;rbaum der H&ouml;he n = 1 besteht nur aus einem Knoten. Er hat also $0 = 2^{n-1} - 1 = 2^{1-1} - 1 = 2^0 - 1 = 1 - 1 = 0$ innere Knoten.
<strong>I.V.</strong>: F&uuml;r beliebige, aber feste volle, vollst&auml;ndige Bin&auml;rb&auml;ume G der H&ouml;he n gilt:
G hat $2^{n-1} - 1$ innere Knoten.
<strong>I.S.</strong>: zeige ${\cal B} (n+1)$ 
F&uuml;r jeden vollen, vollst&auml;ndigen Bin&auml;rbaum der H&ouml;he $n+1$ gibt es einen Teilgraphen T, der ein voller, vollst&auml;ndiger Bin&auml;rbaum der H&ouml;he n ist. $\stackrel{I.V.}{\Rightarrow}$ T hat $2^{n-1} - 1$ innere Knoten. Das sind auch innere Knoten von G. Da die H&ouml;he von G um eins h&ouml;her ist als die von T und sowohl G als auch T volle, vollst&auml;dige Bin&auml;rbaume sind, kommen zu jedem der $2^{n-1}$ Bl&auml;tter aus T noch 2 Bl&auml;tter. Dadurch hat G genau $2^{n-1}$ innere Knoten mehr als T $\Rightarrow$ G hat $2^{n-1}-1+2^{n-1} = 2^n - 1$ innere Knoten $\blacksquare$

<h4>Aussagenlogische Ausdr&uuml;cke</h4>
Die Idee habe ich aus dem <a href="http://www.matheboard.de/archive/470377/thread.html">Matheboard</a> von "MoeMoeson". Bei diesem Beweis bin ich mir aber nicht sicher, ob es tats&auml;chlich strukturelle Induktion ist :-/

Definition: Aussagenlogischer Ausdruck
<ol type="i" style="list-style-type: lower-roman;">
  <li>Jede Variable $p_i, i \in \mathbb{N}$ ist ein aussagenlogischer Ausdruck &uuml;ber V.</li>
  <li>Sind A und B aussagenlogische Ausdr&uuml;cke &uuml;ber V, so sind auch $\neg A, A \land B, A \lor B, A \Rightarrow B, A \Leftrightarrow B, (A)$.</li>
  <li>Ein Wort &uuml;ber V ist nur dann ein aussagenlogischer Ausdruck &uuml;ber V, falls dies aufgrund endlich oftmaliger Anwendung von (i) und (ii) der Fall ist.</li>
</ol>

<strong>Behauptung</strong> Jeder aussagenlogischer Ausdruck endet entweder auf eine Variable oder auf eine schlie&szlig;ende Klammer.
<strong>Beweis</strong>: durch strukturelle Induktion
<strong>I.A.</strong>: Jeder aussagenlogischer Ausdruck aus (i) endet auf eine Variable.
<strong>I.V.</strong>: F&uuml;r beliebige, aber feste aussagenlogische Ausdr&uuml;cke A gilt:
A endet auf eine Variable oder eine schlie&szlig;ende Klammer.
<strong>I.S.</strong>: Ein aussagenlogischer Ausdruck kann nur durch endlich h&auml;ufige Anwendung von (i) und (ii) erzeugt werden (vgl. (iii)). (i) erf&uuml;llt die Bedingung laut I.V., (ii) auch. $\blacksquare$

<strong>Behauptung</strong> F&uuml;r jeden aussagenlogischen Ausdruck A gibt es einen &auml;quivalenten aussagenlogischen Ausdruck B, der nur $\neg$ und $\land$ als Operatoren verwendet.
<strong>Beweis</strong>: durch strukturelle Induktion
<strong>I.A.</strong>: 
Seien $p_1, p_2$ aussagenlogische Variablen. Dann gilt:
$p_1 \lor p_2 = \neg (\neg p_1 \land \neg p_2)$
$p_1 \Leftrightarrow p_2 = \neg (p_1 \land \neg p_2) \land \neg (\neg p_1 \land p_2)$
$p_1 \Rightarrow p_2 = p_1 \land \neg p_2$
F&uuml;r alle weiteren Ausdr&uuml;cke aus (i) und (ii) gilt die Behauptung offensichtlich.

<strong>I.V.</strong>: F&uuml;r beliebige, aber feste aussagenlogische Ausdr&uuml;cke A gilt:
Es gibt einen &auml;quivalenten aussagenlogischen Ausdruck B, der nur $\neg$ und $\land$ als Operatoren verwendet.
<strong>I.S.</strong>: Ein aussagenlogischer Ausdruck kann nur durch endlich h&auml;ufige Anwendung von (i) und (ii) erzeugt werden (vgl. (iii)). (i) und (ii) erf&uuml;llen die Bedingung laut I.V.. $\blacksquare$

<h2>Unendlich - Wann Induktion nicht funktioniert</h2>
Mit Induktion kann man Aussagen f&uuml;r beliebig gro&szlig;e/kleine ganze Zahlen treffen. Allerdings eben nur f&uuml;r ganze Zahlen. Unendlich ist keine ganze Zahl. Also kann man auch keine Aussagen f&uuml;r "unendliche Aussagen" treffen.

Hier ein Beispiel:

Sei A eine Menge.
A hei&szlig;t offen $:\Leftrightarrow \forall_{x \in A} : \exists_{\delta = \delta(x) > 0} : U_\delta(x) \subseteq A$
Es gilt: U und V  sind offene Mengen $\Rightarrow U \cap V$ ist offen.*

Nun k&ouml;nnte man den Trugschluss machen, dass der Schnitt unendlich vieler offener Mengen auch offen ist. Der <strong>falsche Induktionsbeweis</strong> w&uuml;rde in etwa so aussehen:

<strong>Voraussetungen:</strong> Seien $M_i, i \in \mathbb{N}_0$ offene Mengen. Sei M eine Menge und definiert durch $M := \displaystyle \bigcap_{i=0}^\infty M_i$.
<strong>Behauptung</strong>: M ist offen.
<strong>Beweis</strong>: durch vollst&auml;ndige Induktion
<strong>I.A.</strong>: Sei n = 1. Dann: $\cap_{i=0}^1 M_i = M_0 \cap M_1$ ist laut * offen.
<strong>I.V.</strong>: Sei $n \in \mathbb{N}$ beliebig, aber fest und es gelte: 
$\displaystyle \bigcap_{i=0}^n M_i$ ist offen.
<strong>I.S.</strong>:
$\displaystyle \bigcap_{i=0}^{n+1} M_i = \bigcap_{i=0}^{n} M_i \cap M_{n+1}$. Nun gilt:
$\displaystyle \bigcap_{i=0}^{n} M_i$ ist per I.V. offen.
$M_{n+1}$ ist per Vorraussetzung offen.
Der Schnitt von beiden ist wegen * offen. Da n beliebig gro&szlig; werden kann, ist auch M offen $\blacksquare$

Allerdings gilt: 
$\displaystyle \bigcap_{n=1}^\infty \left (1 - \frac{1}{n}, 2+\frac{1}{n} \right) = [1, 2]$, also ein Gegenbeispiel.

Der "Beweis" ist also offensichtlich falsch. Wo ist aber der Fehler? 
Man hat gezeigt, dass beliebig viele Schnitte von offenen Mengen wieder offen sind. Die Behauptung sagt aber, dass unendlich viele Schnitte offener Mengen wieder offen sind. Es gibt also einen unterschied zwischen "beliebig viel" und "unendlich".

<h2>Weitere &Uuml;bungen</h2>
<ul>
    <li>KIT, GBI: <a href="http://gbi.ira.uka.de/archiv/2008/blatt-uebung2-aufgaben.pdf">Zusatzblatt 2</a>, &Uuml;bungsaufgabe 16 - <a href="http://gbi.ira.uka.de/archiv/2008/blatt-uebung2-aufgaben.pdf">L&ouml;sungen</a></li>
    <li>KIT, GBI: <a href="http://gbi.ira.uka.de/archiv/2008/blatt-uebung3-aufgaben.pdf">Zusatzblatt 3</a>, &Uuml;bungsaufgabe 26 d) und 38 d) - <a href="http://gbi.ira.uka.de/archiv/2008/blatt-uebung3-loesungen.pdf">L&ouml;sungen</a></li>
    <li>Otto Forster: &Uuml;bungsbuch zur Analysis I, 5. Auflage, S. 3 - 6. ISBN 978-3-8348-1252-0.</li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Otto Forster: Analysis I, 10. Auflage, S. 1 - 11. ISBN 978-3-8348-1251-3. (Sehr zu empfehlen!)</li>
  <li><a href="http://gbi.ira.uka.de/uebungen/uebung-2.pdf">Folien zur GBI-&Uuml;bung</a> am KIT</li>
  <li><a href="http://gbi.ira.uka.de/vorlesungen/VL11.01.2012.pdf">Vorlesung vom 11.01.2012</a></li>
  <li><a href="http://mitschriebwiki.nomeata.de/WS07/Ana1.html">Analysis I Skript</a> (inoffiziell)</li>
</ul>
