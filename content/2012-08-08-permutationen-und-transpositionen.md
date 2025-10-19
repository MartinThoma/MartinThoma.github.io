---
layout: post
title: Permutationen und Transpositionen
slug: permutationen-und-transpositionen
lang: de
author: Martin Thoma
date: 2012-08-08 10:36:06.000000000 +02:00
category: German posts
tags: Linear algebra
featured_image: 2012/08/pi-thumbnail.png
---
<h2>Permutation</h2>
<h3>Definition</h3>
<div class="definition">Es sei M eine endliche Menge. Eine bijektive Selbstabbildung von M heißt <strong>Permutation</strong>. Die Menge $S_M$ der Permutationen von M ist eine Gruppe bezüglich der Verkettung $\circ$ von Abbildungen und heißt symmetrische Gruppe von M.</div>
Quelle: <a href="https://studium.kit.edu/sites/vab/0x40F0348A9ACDCE49A96EEE39EB076112/Vorlesungsunterlagen/LA.pdf">Skript</a> von Herrn Prof. Dr. Leuzinger, KIT

<h3>Allgemeines</h3>
Es ist nun egal, ob ich die Permutationen von {1, 2, 3} oder {42, 1337, ABC} anschaue. Es sind einfach nur drei Objekte, die unterscheidbar sind. Um es einfacher zu machen, gehen wir nun von den Objekten {1, 2, ..., m} aus. Alle Permutationen dieser Objekte bilden eine Gruppe. Diese nennen wir <span markdown="0">$S_m$</span>.

Ein einzelnes Element aus <span markdown="0">$S_m$</span> wird meist <span markdown="0">$\pi$</span> oder <span markdown="0">$\sigma$</span> genannt, also <span markdown="0">$\pi \in S_m$</span>. Da <span markdown="0">$\pi$</span> eine Permutation ist, ist es insbesondere eine bijektive Selbstabbildung, also:

$$M = {1, ..., m}$$
$$\pi: M \rightarrow M$$
$$i \mapsto \pi(i)$$

Kurz schreibt man auch:
<span markdown="0">\(\pi =
\begin{pmatrix} 1 & 2      & 3      & ... & m\\
           \pi(1) & \pi(2) & \pi(3) & ... & \pi(m)
\end{pmatrix}\)</span>

<h3>Anzahl der Permutationen</h3>
Wenn ich n Elemente habe, die ich auf n Plätze verteilen muss: Wie viele unterschiedliche Zuordnungen von Elementen zu den Plätzen gibt es?

Die Antwort ist <span markdown="0">$n! = 1 \cdot 2 \cdot ... (n - 1) \cdot n = \prod_{i=1}^n i$</span>. Für das erste Element sind <span markdown="0">$n$</span> Plätze frei. Das Zweite kann nur noch auf <span markdown="0">$(n-1)$</span> Plätze verteilt werden, ... , das letzte hat nur noch einen Platz zur "Auswahl".

<h3>Erzeugung der Permutationen</h3>
Angenommen, man muss in einem Test <span markdown="0">$S_3$</span> explizit angeben. Wie geht das?

Nun, zu erst erzeugt man alle Permutationen. Dafür rechnet man sich die Anzahl aus. Es gibt 3 Elemente, also <span markdown="0">$3 \cdot 2 \cdot 1 = 6$</span> Permutationen:
1. _ _ _
2. _ _ _
3. _ _ _
4. _ _ _
5. _ _ _
6. _ _ _

Nun zuerst zum ersten Element, der 1. Diese kann ich an die erste, die zweite oder die dritte Stelle verschieben. Also:
1. 1 _ _
2. 1 _ _
3. _ 1 _
4. _ 1 _
5. _ _ 1
6. _ _ 1

<table>
<tr>
<td>Nun zum zweiten Element, der 2. Wieder das gleiche Prinzip:</td>
<td>Und nun nur noch das letzte Einfüllen:</td>
</tr>
<tr>
<td>1. 1 2 _
2. 1 _ 2
3. 2 1 _
4. _ 1 2
5. 2 _ 1
6. _ 2 1</td>
<td>1. 1 2 3
2. 1 3 2
3. 2 1 3
4. 3 1 2
5. 2 3 1
6. 3 2 1</td>
</tr>
</table>

Und nun noch als Menge in der mathematischen Schreibweise aufschreiben:

<span markdown="0">\(S_3 = \left \{
\underbrace{\begin{pmatrix}
  1 & 2 & 3 \\
  1 & 2 & 3
\end{pmatrix}}_{\pi_1},
\underbrace{\begin{pmatrix}
  1 & 2 & 3 \\
  1 & 3 & 2
\end{pmatrix}}_{\pi_2},
\underbrace{\begin{pmatrix}
  1 & 2 & 3 \\
  2 & 1 & 3
\end{pmatrix}}_{\pi_3},
\underbrace{\begin{pmatrix}
  1 & 2 & 3 \\
  3 & 1 & 2
\end{pmatrix}}_{\pi_4},
\underbrace{\begin{pmatrix}
  1 & 2 & 3 \\
  2 & 3 & 1
\end{pmatrix}}_{\pi_5},
\underbrace{\begin{pmatrix}
  1 & 2 & 3 \\
  3 & 2 & 1
\end{pmatrix}}_{\pi_6}
\right \}\)</span>

<h3>Verkettung</h3>
Was passiert, wenn ich die Permuation <span markdown="0">$\pi_2$</span> mit der Permutation <span markdown="0">$\pi_3$</span> verkette? Also:
<span markdown="0">\(\pi_x(i) = \pi_2(\pi_3(i)) = \begin{pmatrix}1 & 2 & 3\\
3 & 1 & 2 \end{pmatrix} = \pi_6\)</span>
Aber:

<span markdown="0">\(\pi_y(i) = \pi_3(\pi_2(i)) = \begin{pmatrix}1 & 2 & 3\\
2 & 3 & 1 \end{pmatrix} = \pi_5 \neq \pi_6\)</span>

Die Verkettung von Permutationen ist also nicht kommutativ!

Es ergibt sich insgesamt folgende Verknüfungstabelle (gelesen wird: Zeile zuerst, Spalte später):
<table>
<tr>
  <th style="border-right: 1px solid #000;border-bottom: 1px solid #000;">&nbsp;</th>
  <th style="border-bottom: 1px solid #000;"><span markdown="0">$\pi_1$</span></th>
  <th style="border-bottom: 1px solid #000;"><span markdown="0">$\pi_2$</span></th>
  <th style="border-bottom: 1px solid #000;"><span markdown="0">$\pi_3$</span></th>
  <th style="border-bottom: 1px solid #000;"><span markdown="0">$\pi_4$</span></th>
  <th style="border-bottom: 1px solid #000;"><span markdown="0">$\pi_5$</span></th>
  <th style="border-bottom: 1px solid #000;"><span markdown="0">$\pi_6$</span></th>
</tr>
<tr>
  <th style="border-right: 1px solid #000;"><span markdown="0">$\pi_1$</span></th>
  <td><span markdown="0">$\pi_1$</span></td>
  <td><span markdown="0">$\pi_2$</span></td>
  <td><span markdown="0">$\pi_3$</span></td>
  <td><span markdown="0">$\pi_4$</span></td>
  <td><span markdown="0">$\pi_5$</span></td>
  <td><span markdown="0">$\pi_6$</span></td>
</tr>
<tr>
  <th style="border-right: 1px solid #000;"><span markdown="0">$\pi_2$</span></th>
  <td><span markdown="0">$\pi_2$</span></td>
  <td><span markdown="0">$\pi_1$</span></td>
  <td><span markdown="0">$\pi_5$</span></td>
  <td><span markdown="0">$\pi_6$</span></td>
  <td><span markdown="0">$\pi_3$</span></td>
  <td><span markdown="0">$\pi_4$</span></td>
</tr>
<tr>
  <th style="border-right: 1px solid #000;"><span markdown="0">$\pi_3$</span></th>
  <td><span markdown="0">$\pi_3$</span></td>
  <td><span markdown="0">$\pi_4$</span></td>
  <td><span markdown="0">$\pi_1$</span></td>
  <td><span markdown="0">$\pi_2$</span></td>
  <td><span markdown="0">$\pi_6$</span></td>
  <td><span markdown="0">$\pi_5$</span></td>
</tr>
<tr>
  <th style="border-right: 1px solid #000;"><span markdown="0">$\pi_4$</span></th>
  <td><span markdown="0">$\pi_4$</span></td>
  <td><span markdown="0">$\pi_3$</span></td>
  <td><span markdown="0">$\pi_6$</span></td>
  <td><span markdown="0">$\pi_5$</span></td>
  <td><span markdown="0">$\pi_1$</span></td>
  <td><span markdown="0">$\pi_2$</span></td>
</tr>
<tr>
  <th style="border-right: 1px solid #000;"><span markdown="0">$\pi_5$</span></th>
  <td><span markdown="0">$\pi_5$</span></td>
  <td><span markdown="0">$\pi_6$</span></td>
  <td><span markdown="0">$\pi_2$</span></td>
  <td><span markdown="0">$\pi_1$</span></td>
  <td><span markdown="0">$\pi_4$</span></td>
  <td><span markdown="0">$\pi_3$</span></td>
</tr>
<tr>
  <th style="border-right: 1px solid #000;"><span markdown="0">$\pi_6$</span></th>
  <td><span markdown="0">$\pi_6$</span></td>
  <td><span markdown="0">$\pi_5$</span></td>
  <td><span markdown="0">$\pi_4$</span></td>
  <td><span markdown="0">$\pi_3$</span></td>
  <td><span markdown="0">$\pi_2$</span></td>
  <td><span markdown="0">$\pi_1$</span></td>
</tr>
</table>

Man sieht nun, und das finde ich durchaus erstaunlich, man landet immer wieder in <span markdown="0">$S_3$</span>. Durch die Verknüpfung von Permutationen kommt also <em>immer</em> wieder eine Permutation heraus! Das bedeutet, <span markdown="0">\(\)</span> ist unter dieser Verknüpfung abgeschlossen.

Man kann nun auch noch sehen, jedes Element aus <span markdown="0">$(S_3, \circ)$</span> ein inverses hat, da in jeder Zeile ein mal <span markdown="0">$\pi_1$</span> vorkommt.

Außerdem ist <span markdown="0">$(S_3, \circ)$</span> assoziativ.

Kurz: <span markdown="0">$(S_3, \circ)$</span> ist eine Gruppe, die jedoch nicht abelsch ist.

Es wurde in der Vorlesung auch gezeigt, dass allgemein <span markdown="0">$(S_m, \circ)$</span> eine Gruppe ist.

<h3>Die Fehlstandszahl</h3>
<div class="definition">Es sei $\pi \in S_m$ eine Permutation. Die <strong>Fehlstandszahl</strong> <span markdown="0">$F(\pi)$</span> von <span markdown="0">$\pi$</span> ist die (eindeutige) Anzahl der Fälle, in denen für <span markdown="0">$i < k$</span> gilt <span markdown="0">$\pi(i) > \pi(k)$</span>. Die Permutationen mit gerader Fehlstandszahl <span markdown="0">$F(\pi)$</span> heißen gerade, die Permutationen mit ungerader Fehlstandszahl heißen ungerade.</div>

<h4>Beispiele</h4>
<span markdown="0">\(\pi_1 = \begin{pmatrix}
  1 & 2 & 3 \\
  1 & 2 & 3
\end{pmatrix}\)</span> hat die Fehlstandszahl 0.

<span markdown="0">\(\pi_2 = \begin{pmatrix}
  1 & 2 & 3 \\
  1 & 3 & 2
\end{pmatrix}\)</span> hat die Fehlstandszahl 1, da <span markdown="0">$i = 2 < 3 = k$</span> gilt, aber <span markdown="0">$\pi_2(2) = 3 > 2 = \pi_2(3)$</span>.

<span markdown="0">\(\pi_3 = \begin{pmatrix}
  1 & 2 & 3 \\
  2 & 1 & 3
\end{pmatrix}\)</span> hat die Fehlstandszahl 1.

<span markdown="0">\(\pi_4 = \begin{pmatrix}
  1 & 2 & 3 \\
  3 & 1 & 2
\end{pmatrix}\)</span> hat die Fehlstandszahl 2.

<span markdown="0">\(\pi_5 = \begin{pmatrix}
  1 & 2 & 3 \\
  2 & 3 & 1
\end{pmatrix}\)</span> hat die Fehlstandszahl 2.

<span markdown="0">\(\pi_6 = \begin{pmatrix}
  1 & 2 & 3 \\
  3 & 2 & 1
\end{pmatrix}\)</span> hat die Fehlstandszahl 2.


<h2>Transposition</h2>
<div class="definition">Eine <strong>Transposition</strong> ist eine Permutation aus $S_m$, bei der zwei verschiedene,
fest gewahlte Zahlen $i, k \in \{1, 2, ..., m\}$ vertauscht werden, während alle anderen Zahlen fest bleiben.
Man schreibt fur diese Transposition auch kurz $(i~k)$.</div>

Transpositionen werden gerne mit <span markdown="0">$\tau$</span> abgekürzt.

Also: <span markdown="0">$\pi_2 = (2~3), \pi_3=(1~2), \pi_6 = (1~3)$</span> sind Transpositionen.
<span markdown="0">$\pi_1, \pi_4, \pi_5$</span> sind keine Transpositionen.

Es gilt: <span markdown="0">$\tau \circ \tau = id$</span>

wir haben in der Vorlesung gezeigt:
<div class="satz">Jede Permutation <span markdown="0">$\pi \in S_m, m \geq 2,$</span> lässt sich als Verkettung von Transpositionen darstellen.</div>

Beispiel:
<span markdown="0">\(\sigma = \begin{pmatrix}1 & 2 & 3 & 4 & 5 & 6 \\
6 & 5 & 4 & 1 & 3 & 2\end{pmatrix} = (1~6) \circ (2~5) \circ (3~4) \circ (4~6) \circ (5~6)\)</span>

Gelesen wird das ganze von rechts nach links. Die Transposition <span markdown="0">$(5~6)$</span> wird also zuerst angewendet. Wie bei Abbildungen die verkettet werden halt auch.

Die Fehlstandszahl von <span markdown="0">$\sigma$</span> ist 13 und die Anzahl der Transpositionen ist ungerade.

Interessanterweise gilt auch <span markdown="0">$\sigma = (1~4) \circ (3~5) \circ (2~6) \circ (1~3) \circ (1~2)$</span>.
Außerdem kann man beliebig häufig eine Transposition doppelt hinzufügen, da es ja die Identität ist. Die Darstellung einer Permutation als folge von Transpositionen ist also nicht eindeutig.

<h2>Siehe auch</h2>
Wikipedia: <a href="http://de.wikipedia.org/wiki/Permutation">Permutation</a>
