---
layout: post
title: Konstruktion der Chomsky-Normalform
slug: konstruktion-der-chomsky-normalform
lang: de
author: Martin Thoma
date: 2012-02-11 17:25:36.000000000 +01:00
category: German posts
tags: Lecture Notes, Theoretical Computer Science, University, Computer Science
---
<figure class="ai-generated">
    <a href="../images/2012/02/chomsky-normalform.jpg"><img src="../images/2012/02/chomsky-normalform.jpg" alt="Binärer Ableitungsbaum, in dem sich jeder innere Knoten in genau zwei Kinder teilt, daneben Schere und Schraubenschlüssel" width="1376" height="768"></a>
    <figcaption>In der Chomsky-Normalform ist jeder Ableitungsbaum binär.</figcaption>
</figure>

Die Chomsky-Normalform ist eine bestimmte Art, eine kontextfreie Grammatik zu formulieren. Dabei haben nur die Produktionsregeln eine festgelegte Form, alles andere ist wie immer. Die Chomsky-Normalform kommt bei dem CYK-Algorithmus, der das Wortproblem für kontextfreie Grammatiken löst, zum Einsatz. Jede kontextfreie Grammatik kann in Chomsky-Normalform gebracht werden.

<h2>Die Chomsky-Normalform</h2>
Das Besondere an der Chomsky-Normalform ist, dass alle Regeln der Grammatik $G (V, \Sigma, P, S)$ folgende Form haben:
$A \rightarrow BC$ oder
$A \rightarrow a$.
Dabei sind $A, B, C \in V$ und $a \in \Sigma$.

Falls die Grammatik in der Lage ist, das Leere Wort $\varepsilon$ zu erzeugen, dann führt man ein neues Startsymbol $S'$ ein. Es bekommt die Sonderregel $S' \rightarrow \varepsilon$ und für jede Regel $S \rightarrow \alpha$ eine Regel $S' \rightarrow \alpha$. Dabei darf S' niemals auf der rechten Seite einer Produktion stehen. (Eine Regel $S' \rightarrow S$ wäre selbst keine Regel der Chomsky-Normalform.)

Eine Eigenschaft der Chomsky-Normalform ist, dass jedes nicht-leere Wort $w$ in genau $2 \cdot |w| - 1$ Ableitungsschritten gebildet wird: $|w| - 1$ Schritte der Form $A \rightarrow BC$ erzeugen die $|w|$ Nicht-Terminale, und $|w|$ Schritte der Form $A \rightarrow a$ machen daraus Terminale. Das leere Wort braucht genau einen Schritt ($S' \rightarrow \varepsilon$).

<h2>Konstruktion der CNF</h2>
Aus einer Grammatik $G (V, \Sigma, P, S)$ kann mit folgenden vier Schritten eine Grammatik $G' (V', \Sigma, P', S)$ in Chomsky-Normalform (CNF) erstellt werden:

<h3>Schritt 1</h3>
Immer wenn ein Terminal $a \in \Sigma$ auf einer rechten Seite mit mindestens zwei Symbolen steht, wird es durch eine neue Variable $Y_a$ ersetzt und eine neue Produktion $Y_a \rightarrow a$ zu P' hinzugefügt. Regeln der Form $A \rightarrow a$ bleiben, wie sie sind.

Es ist somit sichergestellt, dass alle Regeln entweder nur Nicht-Terminale auf der rechten Seite der Produktion stehen haben oder $\varepsilon$ oder dass dort ein einzelnes Terminal steht.

<h3>Schritt 2</h3>
Immer wenn mehr als zwei Variablen auf der rechten Seite stehen, werden diese durch neue ersetzt. Sagen wir es stehen rechts m Variablen. Dann führt man m - 2 neue Variablen $C_1, ..., C_{m-2}$ ein, fügt diese zu V' hinzu, und macht aus einer Regel $A \rightarrow B_1 B_2 ... B_m$ die Regeln $A \rightarrow B_1 C_1, C_1 \rightarrow B_2 C_2, ..., C_{i-1} \rightarrow B_i C_i, ..., C_{m-2} \rightarrow B_{m-1} B_m$.

An dieser Stelle ist sichergestellt, dass alle Regeln entweder nur ein oder zwei Nicht-Terminale auf der rechten Seite der Produktion stehen haben oder $\varepsilon$ oder dass dort ein einzelnes Terminal steht.

<h3>Schritt 3</h3>
Nun wollen wir alle $\varepsilon$-Übergänge entfernen.

Um dies zu erreichen, bestimmen wir zuerst die Menge $V_\varepsilon$ aller Variablen, aus denen sich $\varepsilon$ ableiten lässt: Zuerst gehören alle $A$ mit einer Regel $A \rightarrow \varepsilon$ dazu, dann wiederholt alle $B$ mit einer Regel $B \rightarrow C_1 ... C_k$, deren rechte Seite nur aus Variablen in $V_\varepsilon$ besteht.

Für jede Regel $B \rightarrow CD$ mit $C \in V_\varepsilon$ fügen wir die Regel $B \rightarrow D$ hinzu, und mit $D \in V_\varepsilon$ die Regel $B \rightarrow C$. Erst danach streichen wir alle Regeln $A \rightarrow \varepsilon$. Würde man sie einfach streichen, gingen Wörter verloren: Aus $C_1 \rightarrow S Y_a$ mit $S \rightarrow \varepsilon$ wird nur dann noch $Y_a$, wenn man $C_1 \rightarrow Y_a$ hinzufügt.
Am Ende fügen wir die Regeln $S' \rightarrow S | \varepsilon$ hinzu, falls $S \in V_\varepsilon$ ist, die Grammatik also das leere Wort erzeugen konnte.

Nun ist sichergestellt, dass alle Regeln (außer $S' \rightarrow \varepsilon$) entweder nur ein oder zwei Nicht-Terminale auf der rechten Seite der Produktion stehen haben oder dass dort ein einzelnes Terminal steht. Regeln mit nur einem Nicht-Terminal auf der rechten Seite gibt es allerdings noch.

<h3>Schritt 4</h3>
In diesem Schritt entfernen wir die Kettenregeln, also Regeln der Form $A \rightarrow B$ mit $A, B \in V$.

Zuerst entfernt man Kreise von Kettenregeln, also $A_1 \rightarrow A_2 \rightarrow A_3 \rightarrow ... \rightarrow A_u \rightarrow A_1$. Diese findet man mit einer Tiefensuche.
Dann ersetzt man alle $A_2, ..., A_u$ durch $A_1$. Die Regel $A_1 \rightarrow A_1$ kann entfernt werden, da sie ja nichts ändert.

Danach sind die Kettenregeln kreisfrei. Für jede Kettenregel $A \rightarrow B$ fügt man für jede Regel $B \rightarrow \alpha$ die Regel $A \rightarrow \alpha$ hinzu und streicht $A \rightarrow B$. Dabei arbeitet man von hinten nach vorne, sodass $B$ selbst keine Kettenregeln mehr hat. Jetzt ist die Grammatik in Chomsky-Normalform.

<h2>Beispiele</h2>
<h3>Die Sprache der Palindrome</h3>
Gegeben sei folgende Grammatik:
$G(\underbrace{\{S\}}_{V}, \underbrace{\{a,b\}}_{\Sigma}, P, S)$ mit
$P = \{S \rightarrow \varepsilon | a | b | aSa | bSb \}$.

<h4>Schritt 1</h4>
$S \rightarrow \varepsilon | a | b | Y_aSY_a | Y_bSY_b$
$Y_a \rightarrow a$
$Y_b \rightarrow b$

<h4>Schritt 2</h4>
$S \rightarrow \varepsilon | a | b | Y_aC_1 | Y_bC_2$
$C_1 \rightarrow SY_a$
$C_2 \rightarrow SY_b$
$Y_a \rightarrow a$
$Y_b \rightarrow b$

<h4>Schritt 3</h4>
$V_\varepsilon = \{S\}$. Da $S$ in $C_1 \rightarrow SY_a$ und $C_2 \rightarrow SY_b$ vorkommt, kommen $C_1 \rightarrow Y_a$ und $C_2 \rightarrow Y_b$ hinzu:
$S \rightarrow a | b | Y_aC_1 | Y_bC_2$
$C_1 \rightarrow SY_a | Y_a$
$C_2 \rightarrow SY_b | Y_b$
$Y_a \rightarrow a$
$Y_b \rightarrow b$
$S' \rightarrow S | \varepsilon$

<h4>Schritt 4</h4>
Die Kettenregeln sind $C_1 \rightarrow Y_a$, $C_2 \rightarrow Y_b$ und $S' \rightarrow S$. Kreise gibt es keine. $C_1 \rightarrow Y_a$ wird zu $C_1 \rightarrow a$, $C_2 \rightarrow Y_b$ wird zu $C_2 \rightarrow b$, und $S' \rightarrow S$ wird durch die Regeln von $S$ ersetzt.

<h4>Ergebnis</h4>
Damit ist die Grammatik:
$G_{CNF} (\{S, S', Y_a, Y_b, C_1, C_2\}, \{a,b\}, P', S')$ mit folgenden Produktionen P':
$P' = \{S' \rightarrow \varepsilon | a | b | Y_aC_1 | Y_bC_2,$
$~ S \rightarrow a | b | Y_aC_1 | Y_bC_2,$
$~ C_1 \rightarrow SY_a | a,$
$~ C_2 \rightarrow SY_b | b,$
$~ Y_a \rightarrow a,$
$~ Y_b \rightarrow b\}$

Zur Probe: Das Palindrom $abba$ entsteht in $2 \cdot 4 - 1 = 7$ Schritten: $S' \rightarrow Y_aC_1 \rightarrow aC_1 \rightarrow aSY_a \rightarrow aY_bC_2Y_a \rightarrow abC_2Y_a \rightarrow abbY_a \rightarrow abba$.

Sie ist also nicht schöner oder einfacher geworden, hat aber eine bestimmte Struktur erhalten.

<h2>Weiterführende Links und Quellen</h2>
<ul>
    <li><a href="http://de.wikipedia.org/wiki/Chomsky-Normalform">Wikipedia</a></li>
    <li>Uwe Schöning: <i>Theoretische Informatik- kurz gefasst</i>. 5.&nbsp;Auflage. Spektrum Akademischer Verlag, Heidelberg <span style="white-space:nowrap;">2008</span>, ISBN 978-3-8274-1824-1, S.&nbsp;44, <span class="plainlinks-print"><a rel="nofollow" class="external text" href="http://d-nb.info/986529222">DNB 986529222</a></span>.</li>
    <li>KIT:
<ul>
<li><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/tgi_skript_ws11.pdf">Skript</a> von Prof. Dr. Dorothea Wagner, S. 98</li>
<li><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/uebung7.pdf">Übung</a> vom 02.02.2012 - Hier ist ein sehr gutes, detailliertes Beispiel! </li>
</ul></li>
</ul>
