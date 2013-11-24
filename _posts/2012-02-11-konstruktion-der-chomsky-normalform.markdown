---
layout: post
status: publish
published: true
title: Konstruktion der Chomsky-Normalform
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 13521
wordpress_url: http://martin-thoma.com/?p=13521
date: 2012-02-11 17:25:36.000000000 +01:00
categories:
- German posts
tags:
- lecture-notes
- Theoretical computer science
comments:
- id: 44341
  author: i42n
  author_email: anon@web.de
  author_url: ''
  date: !binary |-
    MjAxMi0wMi0xMSAxOTowNzozOSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMi0xMSAxNzowNzozOSArMDEwMA==
  content: Die Chomsky-Normalform in Schritt 3 ist noch nicht fertig. Sie ist nicht
    wirklich falsch, gen&uuml;gt aber nicht den Regeln der Chomsky-Normalform. Rechts
    d&uuml;rfen keine einzelnen Nichtterminale stehen (bei dir Ya und Yb). Du m&uuml;sstest
    da die Terminale a und b daf&uuml;r einsetzen, dann sollte es passen.
- id: 45811
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wMi0xMyAxNTozOTowNyArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMi0xMyAxMzozOTowNyArMDEwMA==
  content: ! "Hallo i42n,\r\n\r\nvielen Dank f&uuml;r deinen Hinweis. Ich habe es
    korrigiert. Das ist schon wichtig, dass es die richtige Form hat, weil sonst die
    Anzahl der Ableitungen nicht so direkt aus der Wortl&auml;nge abgelesen werden
    kann.\r\n\r\nViele Gr&uuml;&szlig;e,\r\nMartin"
- id: 1124051
  author: Jens
  author_email: ich@tessarakt.de
  author_url: ''
  date: !binary |-
    MjAxMy0wMS0yMyAyMDo0OTo0MiArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMS0yMyAxOTo0OTo0MiArMDEwMA==
  content: ! "\"Schritt 4\r\nKeine Kettenregel vorhanden.\"\r\n\r\n&Auml;hm, bitte
    was? S->Y<sub>a</sub> <em>ist</em> eine Kettenproduktion. Was soll das
    denn sonst sein?\r\n\r\n\"Ich habe es korrigiert.\"\r\n\r\nEben nicht ...\r\n\r\n###\r\n\r\n\"In
    diesem Schritt entfernen wir eventuell vorhandene Kettenregeln, also regeln der
    Form A1&rarr;A2&rarr;A3&rarr;Au&rarr;A1.\"\r\n\r\nHier geht es schon los.\r\n\r\nSchon
    A1->A2 ist eine \"Kettenregel\". Da noch unn&ouml;tig mehr hinterzuschreiben,
    verwirrt nur.\r\n\r\n###\r\n\r\nAchja: Es finden auch Leute \"&uuml;ber Google\"
    diese Seite, die noch dabei sind, das zu lernen. Daf&uuml;r, dass die sich von
    einer anderen Reihenfolge der Schritte verwirren lassen (\"Schritt 1 sieht da
    ganz anders aus als bei uns auf den Folien!\") kannst Du nat&uuml;rlich nichts.\r\n\r\nAber
    die &uuml;brige Verwirrung (siehe vorherige Kommentare) muss nicht sein. Und warum
    benutzt Du 3 (in Worten: DREI!) verschiedene Worte, mit denen Du dasselbe meinst,
    n&auml;mlich \"Regel\", \"Produktion\" und \"&Uuml;bergang\"?"
- id: 1124081
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wMS0yMyAyMTozMjoxNSArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMS0yMyAyMDozMjoxNSArMDEwMA==
  content: ! "Hallo Jens,\r\n\r\nder Fehler wurde korrigiert. Hast du bis &bdquo;Ergebnis&ldquo;
    gelesen? Dort steht rechts kein einzelnes Nicht-Terminal.\r\n\r\nWarum soll S
    &rarr; Y<sub>a</sub> eine Kettenregel sein? Wie habt ihr Kettenregel definiert?
    (Kannst du mir eventuell den Link zu den Folien und die entsprechende Seite nennen?)\r\n\r\nZu
    den drei W&ouml;rtern &bdquo;Regel&ldquo;, &bdquo;Produktion&ldquo; und &bdquo;&Uuml;bergang&ldquo;:\r\n<ul>\r\n<li>Ich
    habe niemals nur &bdquo;&Uuml;bergang&ldquo; geschrieben. Ich habe von Epsilon-&Uuml;berg&auml;ngen
    geredet. Das nennt man halt so.</li>\r\n<li>Sowohl &bdquo;Regel&ldquo; als
    auch &bdquo;Produktion&ldquo; sind &uuml;bliche Begriffe. Ich w&uuml;rde sagen,
    dass ist vergleichbar mit &bdquo;Addition&ldquo; und &bdquo;Summe&ldquo;. Ich
    sehe keinen guten Grund auf diese Synonyme zu verzichten, die sowieso aus GBI
    bekannt sein sollten.</li>\r\n</ul>"
- id: 1124091
  author: Jens
  author_email: ich@tessarakt.de
  author_url: ''
  date: !binary |-
    MjAxMy0wMS0yMyAyMTo0MjoxNiArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMS0yMyAyMDo0MjoxNiArMDEwMA==
  content: ! "https://de.wikipedia.org/wiki/Chomsky-Normalform\r\n\r\n<blockquote>Kettenregeln
    (Produktionen der Form A&rarr;B)</blockquote>\r\n\r\nOder auch das von Dir
    verlinkte Wagner-Skript:\r\n\r\n<blockquote>4. Schritt: Ersetzung aller Kettenregeln
    A &rarr; B.</blockquote>\r\n\r\nAlso frage ich mal zur&uuml;ck: \"Wie habt
    ihr Kettenregel definiert?\"\r\n\r\n<blockquote>der Fehler wurde korrigiert. Hast
    du bis &bdquo;Ergebnis&ldquo; gelesen?</blockquote>\r\n\r\nJa, habe ich. Worauf
    ich hinaus wollte, war, dass Du die Sachen, die nach Schritt 4 geh&ouml;ren (laut
    dem von Dir verlinkten Skript), nach Schritt 4 in einem Extra-Schritt untergebracht
    hast."
- id: 1152261
  author: Simon
  author_email: baechsim@students.zhaw.ch
  author_url: ''
  date: !binary |-
    MjAxMy0wMy0xNyAxMTo1Mjo0MCArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMy0xNyAxMDo1Mjo0MCArMDEwMA==
  content: ! "Hallo Martin\r\n\r\nBist du Sicher, dass deine L&ouml;sung stimmt? z.B.
    das Wort abba. Als Startwert ist S' gegeben. Somit muss man als erste Ableitung
    S'->S ausf&uuml;hren, um die weiteren Buchstaben generieren zu k&ouml;nnen. Nun
    kannst du aber nicht mehr auf das leere Wort zur&uuml;ck da es diese Regel nicht
    gibt.\r\nAusser man definiert zus&auml;tzlich S&rarr;YaYa|YbYb."
- id: 1152491
  author: Simon
  author_email: ''
  author_url: ''
  date: !binary |-
    MjAxMy0wMy0xNyAxMzoxMjo0MiArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMy0xNyAxMjoxMjo0MiArMDEwMA==
  content: ! "Hi\r\n\r\nM&uuml;ssten c1 und c2 nicht jeweils auf S'Ya und S'Yb abbilden?
    Weil sonst ist es nicht m&ouml;glich folgendes Palindrom zu bilden: abba\r\n\r\nFreundliche
    Gr&uuml;sse\r\nSimon"
- id: 1152711
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wMy0xNyAxMzo1ODo0MCArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMy0xNyAxMjo1ODo0MCArMDEwMA==
  content: Ich bin in dem Thema leider gar nicht mehr drin und habe auch keine Lust
    mich jetzt nochmal einzulesen. Ich habe zu beginn des Artikels auf diese Kommentare
    hingewiesen. Wenn jeman sich sicher ist zu wissen was falsch ist, bitte ich um
    einen ausf&uuml;hrlichen Kommentar. Eventuell korrigiere ich den Artikel dann
    mal, wenn ich Zeit habe.
- id: 1225691
  author: JakobD
  author_email: icrosoft@gmx.de
  author_url: ''
  date: !binary |-
    MjAxMy0wNi0yNyAxNzowMDo1MSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNi0yNyAxNTowMDo1MSArMDIwMA==
  content: ! "Allein die Existenz der Regel S' -> S bedeutet ja, dass es keine Chomsky-Normalform
    ist ;)\r\nMein Vorschlag w&auml;re (hab mir aber nur kurz den Wikipedia-Artikel
    durchgelesen und deine urspr&uuml;ngliche Grammatik zur Grundlage genommen, bin
    mir also nicht ganz sicher damit):\r\nN = { S', S, Xa, Xb, Xas, Xbs } \r\nP =
    { S' -> e / a / b / XasXa / XbsXb\r\nS -> a / b / XasXa
    / XbsXb\r\nXa -> a\r\nXb -> b\r\nXas -> XaS\r\nXbs -> XbS }\r\n\r\nGr&uuml;&szlig;e,\r\nJakob"
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
