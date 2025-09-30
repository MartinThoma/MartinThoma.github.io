---
layout: post
lang: de
title: Konstruktion der Chomsky-Normalform
slug: konstruktion-der-chomsky-normalform
author: Martin Thoma
date: 2012-02-11 17:25:36.000000000 +01:00
category: German posts
tags: lecture-notes, Theoretical computer science
---
<div class="warning">Dieser Artikel k&ouml;nnte inhaltliche Fehler beinhalten. Bitte lest euch die Kommentare durch.</div>

Die Chomsky-Normalform ist eine bestimmte Art, eine kontextfreie Grammatik zu formulieren. Dabei haben nur die Produktionsregeln eine festgelegte Form, alles andere ist wie immer. Die Chomsky-Normalform kommt bei dem CYK-Algorithmus, der das Wortproblem f&uuml;r kontextfreie Grammatiken l&ouml;st, zum Einsatz. Jede kontextfreie Grammatik kann in Chomsky-Normalform gebracht werden.

<h2>Die Chomsky-Normalform</h2>
Das Besondere an der Chomsky-Normalform ist, dass alle Regeln der Grammatik $G (V, \Sigma, P, S)$ folgende Form haben:
$A \rightarrow BC$ oder
$A \rightarrow a$.
Dabei sind $A, B, C \in V$ und $a \in \Sigma$.

Falls die Grammatik in der Lage ist, das Leere Wort $\varepsilon$ zu erzeugen, dann f&uuml;gt man folgende Sonderregel hinzu: $S' \rightarrow S | \varepsilon$. Dabei darf S' niemals auf der rechten Seite einer Produktion stehen.

Eine Eigenschaft der Chomsky-Normalform ist, dass jedes Wort aus $2 \cdot |w| - 1$ Ableitungen gebildet werden kann. (Falls das leere Wort gebildet werden kann sind es $2 \cdot |w|$ Ableitungen f&uuml;r jedes nicht-leere Wort und eine Ableitung f&uuml;r das leere Wort) In jedem Ableitungsschritt erh&auml;lt man entweder ein Terminal, oder ein weiteres Nicht-Terminal.

<h2>Konstruktion der CNF</h2>
Aus einer Grammatik $G (V, \Sigma, P, S)$ kann mit folgenden vier Schritten eine Grammatik $G' (V', \Sigma, P', S)$ in Chomsky-Normalform (CNF) erstellt werden:

<h3>Schritt 1</h3>
Immer wenn ein Symbol aus $\Sigma$ in einer Produktion steht, wird dieses durch $Y_a$ ersetzt und eine neue Produktion $Y_a \rightarrow a$ zu P' hinzugef&uuml;gt.

Es ist somit sichergestellt, dass alle Regeln entweder nur Nicht-Terminale auf der rechten Seite der Produktion stehen haben oder $\varepsilon$ oder dass dort ein einzelnes Terminal steht.

<h3>Schritt 2</h3>
Immer wenn mehr als zwei Variablen auf der rechten Seite stehen, werden diese durch neue ersetzt. Sagen wir es stehen rechts m Variablen. Dann f&uuml;hrt man m - 2 neue Variablen ein, f&uuml;gt diese zu V' hinzu, und macht aus einer Regel $A \rightarrow B_1 B_2 ... B_m$ die Regeln $A \rightarrow B_1 C_1, C_1 \rightarrow B_2 C_2, ..., C_{i+1} \rightarrow B_i C_i ... C_{m-2} \rightarrow B_{m-3} C_{m-3}$.

An dieser Stelle ist sichergestellt, dass alle Regeln entweder nur ein oder zwei Nicht-Terminale auf der rechten Seite der Produktion stehen haben oder $\varepsilon$ oder dass dort ein einzelnes Terminal steht.

<h3>Schritt 3</h3>
Nun wollen wir alle $\varepsilon$-&Uuml;berg&auml;nge entfernen.

Um dies zu erreichen, suchen wir alle Regeln, die nach $\varepsilon$ abbilden, also von der Form $A \rightarrow \varepsilon$ sind. Dabei streichen wir die Regeln $A \rightarrow \varepsilon$. Falls A nun nicht mehr auf der linken Seite auftaucht, streichen wir es &uuml;berall aus der rechten Seite. Falls dabei eine Regel zu $B \rightarrow \varepsilon$ wird, streichen wir auch diese. Das wiederholen wir so lange, bis keine $\varepsilon$-&Uuml;berg&auml;nge mehr vorhanden sind.
Am Ende f&uuml;gen wir die Regel $S' \rightarrow S | \varepsilon$ hinzu, falls die Grammatik auf das leere Wort abbilden konnte.

Nun ist sichergestellt, dass alle Regeln entweder nur ein oder zwei Nicht-Terminale auf der rechten Seite der Produktion stehen haben oder dass dort ein einzelnes Terminal steht. Allerdings kann es noch Kreise in der Ableitung geben, die man entfernen kann.

<h3>Schritt 4</h3>
In diesem Schritt entfernen wir eventuell vorhandene Kettenregeln, also Regeln der Form $A_1 \rightarrow A_2 \rightarrow A_3 \rightarrow A_u \rightarrow A_1$. Diese findet man mit einer Tiefensuche.
Dann ersetzt man alle $A_2, ..., A_u$ durch $A_1$. Die Regel $A_1 \rightarrow A_1$ kann entfernt werden, da sie ja nichts &auml;ndert.

<h2>Beispiele</h2>
<h3>Die Sprache der Palindrome</h3>
Gegeben sei folgende Grammatik:
$G(\underbrace{\{S\}}_{V}, \underbrace{\{a,b\}}_{\Sigma}, S, P)$ mit
$P = \{S \rightarrow \varepsilon | a | b | aSa | bSb \}$.

<h4>Schritt 1</h4>
$S \rightarrow \varepsilon | Y_a | Y_b | Y_aSY_a | Y_bSY_b$
$Y_a \rightarrow a$
$Y_b \rightarrow b$

<h4>Schritt 2</h4>
$S \rightarrow \varepsilon | Y_a | Y_b | Y_aC_1 | Y_bC_2$
$C_1 \rightarrow SY_a$
$C_2 \rightarrow SY_b$
$Y_a \rightarrow a$
$Y_b \rightarrow b$

<h4>Schritt 3</h4>
$S \rightarrow Y_a | Y_b | Y_aC_1 | Y_bC_2$
$C_1 \rightarrow SY_a$
$C_2 \rightarrow SY_b$
$Y_a \rightarrow a$
$Y_b \rightarrow b$
$S' \rightarrow S | \varepsilon$

<h4>Schritt 4</h4>
Keine Kettenregel vorhanden.

<h4>Ergebnis</h4>
Nun werden noch einzelne Nicht-Terminale durch die m&ouml;glichen Terminale ersetzt und man ist fertig.

Damit ist die Grammatik:
$G_{CNF} (\{S, S', Y_a, Y_b, C_1, C_2\}, \{a,b\}, S', P'))$ mit folgenden Produktionen P':
$P' = \{S \rightarrow a | b | Y_aC_1 | Y_bC_2,$
$~ C_1 \rightarrow SY_a,$
$~ C_2 \rightarrow SY_b,$
$~ Y_a \rightarrow a,$
$~ Y_b \rightarrow b,$
$~ S' \rightarrow S | \varepsilon\}$

Sie ist also nicht sch&ouml;ner oder einfacher geworden, hat aber eine bestimmte Struktur erhalten.

<h2>Weiterf&uuml;hrende Links und Quellen</h2>
<ul>
    <li><a href="http://de.wikipedia.org/wiki/Chomsky-Normalform">Wikipedia</a></li>
    <li>Uwe Sch&ouml;ning: <i>Theoretische Informatik- kurz gefasst</i>. 5.&nbsp;Auflage. Spektrum Akademischer Verlag, Heidelberg <span style="white-space:nowrap;">2008</span>, ISBN 978-3-8274-1824-1, S.&nbsp;44, <span class="plainlinks-print"><a rel="nofollow" class="external text" href="http://d-nb.info/986529222">DNB 986529222</a></span>.</li>
    <li>KIT:
<ul>
<li><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/tgi_skript_ws11.pdf">Skript</a> von Prof. Dr. Dorothea Wagner, S. 98</li>
<li><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/uebung7.pdf">&Uuml;bung</a> vom 02.02.2012 - Hier ist ein sehr gutes, detailliertes Beispiel! </li>
</ul></li>
</ul>
