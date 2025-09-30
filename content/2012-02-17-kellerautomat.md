---
layout: post
lang: de
title: Kellerautomat
slug: kellerautomat
author: Martin Thoma
date: 2012-02-17 20:17:01.000000000 +01:00
category: German posts
tags: Abstract machine, Theoretical computer science
---
Ein Kellerautomat ist ein Endlicher Automat mit einem Stack ("Kellerspeicher"). Er wird mit PDA (pushdown automaton) bzw. NPDA (nondeterministic pushdown automaton) abgek&uuml;rzt.

Laut Wikipedia verwendet die Gleitkommaeinheit einen PDA. Dazu habe ich allerdings keine Quelle, das ist also mit Vorsicht zu genie&szlig;en.

Ein weiterer Einsatzzweck ist die Syntaxanalyse einer Tokenfolge. Das kann f&uuml;r Compiler oder Interpreter von Interesse sein.

<h2>Definitionen</h2>
Der <strong>Kellerautomat</strong> ist als 7-Tupel definiert:

$(Q, \Sigma, \Gamma, q_0, Z_0, \delta, F)$, wobei
<ul>
	<li>Q: endliche Zustandsmenge</li>
	<li>$\Sigma$: endliches Eingabealphabet</li>
	<li>$\Gamma$: endliches STACK-Alphabet</li>
	<li>$q_0 \in Q$: Anfangszustand</li>
	<li>$Z_0 \in \Gamma$: Initialisierung des STACK</li>
	<li>$\delta: Q \times (\Sigma \cup \{\varepsilon\}) \times \Gamma \rightarrow 2^{Q \times \Gamma^*}$.</li>
	<li>$F \subseteq Q$: Menge der akzeptierenden Endzust&auml;nde.</li>
</ul>

Bemerkenswert ist hierbei, dass F leer sein kann. Dies ist m&ouml;glich, da ein PDA auch durch leeren Stack akzeptieren kann.

Die Zustands&uuml;berf&uuml;hrungsfunktion ist etwas umst&auml;ndlich beschrieben. Dort steht, dass jede Regel folgende Form hat:
$\delta(\text{Zustand}, \text{Eingabesymbol}, \text{Stacksymbol}) = (\text{Neuer Zustand}, \text{Neuer Stack})$

Die <strong>Konfiguration eines PDA</strong> ist ein Tripel $(q, w, \alpha)$, wobei
<ul>
	<li>$q \in Q$: aktueller Zustand</li>
	<li>$w \in \Sigma^*$: der Teil der Eingabe, der noch nicht gelesen wurde</li>
	<li>$\alpha \in \Gamma^*$: der STACK-Inhalt</li>
</ul>

Ein PDA ist <strong>deterministisch</strong> $: \Leftrightarrow |\delta(q, a, Z)| + |\delta(q, \varepsilon, Z)| \leq 1 ~~~ \forall_{q \in Q, a \in \Sigma, Z \in \Gamma}$.

<h2>Anschaulich</h2>
Du hast einen Kartenstapel (deine Eingabe, auf der du immer nur ein Zeichen lesen darfst),
einen Stapel f&uuml;r Notizzettel, wobei am Anfang nur ein Notizzettel dort liegt und immer nur ein Symbol auf dem Zettel steht (dein Stack, der mit $Z_0 \in \Gamma$ initialisiert ist),
einen Zustand und eine Menge Regeln ($\delta$).

Nun schaust du dir in jedem Schritt die oberste Karte auf dem Kartenstapel an und legst sie weg. Des Weiteren schaust du dir deine oberste Notiz an und legst sie weg und &uuml;berpr&uuml;fst deinen Zustand. Aus diesen Informationen schlussfolgerst du, was du als n&auml;chstes machst. Du kannst dir aussuchen in welchen Zustand du gehen willst und was du noch auf deinen Notiz-Stapel tun willst. Du kannst auch einfach nichts auf den Notiz-Stapel legen.

<h2>Beispiele</h2>
Sei $L = \{w \in \{0,1,2\}^* | w = 0^i1^j2^j ~~~ i, j \in \mathbb{N}\}$

$(\{q_0, q_1, q_2\}, \{0, 1, 2\}, \{1, \#\}, q_0, \#, \delta, \emptyset)$ mit

$\delta(q_0, 0, \#) = \{(q_0, \#), (q_1, \#)\}, $
$\delta(q_1, 1, \#) = \{(q_1, 1)\}, $
$\delta(q_1, 1, 1) = \{(q_1, 11)\}, $
$\delta(q_1, 2, 1) = \{(q_2, \varepsilon)\}, $
$\delta(p, a, Z) = \emptyset $ sonst.

Der Kellerautomat akzeptiert durch leeren STACK. Aus diesem Grund legen wir am Anfang auch immer wieder # auf den Stack. Sonst w&uuml;rde der PDA zu fr&uuml;h akzeptieren.

Da $|\delta(q_0, 0, \#) = 2 > 1|$ ist dieser Kellerautomat Nicht-Deterministisch.

<h2>Umformungen</h2>
<h3>Akzeptierender Endzustand &rarr; leerer STACK</h3>
Siehe Skript von Prof. Dr. Dorothea Wagner, S. 107.

Gegeben sei ein Kellerautomat ${\cal K}_1 (Q_1, \Sigma, \Gamma_1, \delta_1, q_0^1, Z_0^1, F_1)$ der durch akzeptierenden Endzustand akzeptiert.
Wir wollen einen neuen Automaten ${\cal K}_2 (Q_2, \Sigma, \Gamma_2, \delta_2, q_0^2, Z_0^2, F_2)$ der durch leeren STACK akzeptiert.

<strong>Idee</strong>: Wir f&uuml;hren einen neuen Zustand $q_E$ ein, bei dessen Erreichen wir den STACK leeren. Um zu verhindern, dass der STACK zwischenzeitlich leer wird, legen wir zu beginn das STACK-Symbol $Z_0^2$ ab.

<strong>Formal</strong>:
$Q_2 := Q_1 \cup \{q_0^2, q_E\}$, wobei $q_0^2$ der neue Anfangszustand von ${\cal K}_2$ ist.
$\Gamma_2 := \Gamma_1 \cup \{Z_0^2\}$, wobei $Z_0^2$ den STACK initialisiert.

Die Menge $\delta_2(q, a, Z)$ f&uuml;r $a \in \Sigma \cup \{\varepsilon\}$ und $Z \in \Gamma_2$ sei durch folgende Bedingungen festgelegt:

Sorge f&uuml;r die gleiche Anfangssituation:
$\delta_2(q_0^2, \varepsilon, Z_0^2) = \{(q_0^1, Z_0^1Z_0^2)\}$

Falls der Zustand, das gelesene Zeichen und das STACK-Symbol im "alten" Automaten sind, dann wie gehabt:
$\delta_2(q, a, Z) = \delta_1(q, a, Z) \text{f&uuml;r } (q \in Q_1, a \neq \varepsilon, Z \in \Gamma_1) \lor (q \in Q_1 \setminus F_1, a = \varepsilon, Z \in \Gamma_1)$

Sorge daf&uuml;r, dass die STACK-Leerungsregel aufgerufen wird, falls der Zustand akzeptierend ist:
$\delta_2(q, \varepsilon, Z) = \delta_1(q, \varepsilon, Z) \cup \{(q_E, \varepsilon)\} \text{f&uuml;r } q \in F_1, Z \in \Gamma_2$

Diese Regel leert den STACK:
$\delta_2(q_E, \varepsilon, Z) = \{(q_E, \varepsilon)\}  \text{ f&uuml;r } Z \in \Gamma_2$

<h3>Leerer STACK &rarr; akzeptierender Endzustand</h3>
Siehe Skript von Prof. Dr. Dorothea Wagner, S. 107.

Gegeben sei ein Kellerautomat ${\cal K}_1 (Q_1, \Sigma, \Gamma_1, \delta_1, q_0^1, Z_0^1, F_1)$ der durch leeren STACK akzeptiert.
Wir wollen einen neuen Automaten ${\cal K}_2 (Q_2, \Sigma, \Gamma_2, \delta_2, q_0^2, Z_0^2, F_2)$ der durch akzeptierenden Endzustand akzeptiert.

<strong>Idee</strong>: Wir legen ein zus&auml;tzliches Symbol $Z_0^2$ auf den STACK. Wird $Z_0^2$ gelesen, ist der STACK noch nicht leer, aber man kann in einen akzeptierenden Zustand $q_F$ wechseln.

<strong>Formal</strong>:
$Q_2 := Q_1 \cup \{q_0^2, q_F\}$, wobei $q_0^2$ Anfangszustand von ${\cal K}_2$ ist und $F_2 := \{q_F\}$
$\Gamma_2 := \Gamma_1 \cup \{Z_0^2\}$, wobei $Z_0^2$ Initialisierung des STACKS von ${\cal K}_2$ ist und $\delta_2$ festgelegt durch:

Zuerst sorgen wir daf&uuml;r, dass $Z_0^2$ ganz unten im STACK ist:
$$\delta_2(q_0^2, a, X) =
\begin{cases}
\{q_0^1, Z_0^1, Z_0^2\} & \text{falls } a= \varepsilon \text{ und } X = Z_0^2\\
\emptyset               & \text{sonst}
\end{cases}$$

Dann wie gehabt:
$\delta_2(q, a, Z) = \delta_1(q, a, Z) \text{, falls } q \in Q_1, a \in \Sigma \cup \{\varepsilon\} \text{ und } Z \in \Gamma_1$

Und am Schluss auch akzeptieren:
$\delta_2(q, \varepsilon, Z_0^2) = \{(q_F, \varepsilon)\} \text{ f&uuml;r } q \in Q_1$.

<h2>Dies und das</h2>
<ul>
    <li>Ein Kellerautomat mit zwei STACKs ist Turingm&auml;chtig. (&rarr; <a href="http://de.wikipedia.org/wiki/Zweikellerautomat" title="Zweikellerautomat">Zweikellerautomat</a>)</li>
	<li>Ein NPDA erkennt genau die kontextfreien Sprachen.</li>
	<li>Ein PDA erkennt manche kontextfreie Sprachen, aber nicht alle. (Genauer: <a href="http://de.wikipedia.org/wiki/Deterministisch_kontextfreie_Sprache">Deterministisch kontextfreie Sprache</a>)</li>
	<li>Zu jedem PDA, der eine Sprache L durch einen akzeptierenden Endzustand akzeptiert, kann ein PDA konstruiert werden, der L mit leerem STACK akzeptiert (und umgekehrt).</li>
	<li>F&uuml;r jede Grammatik G in Greibach-Normalform gibt es einen PDA.</li>

</ul>


<h2>Siehe auch</h2>
<ul>
    <li>Wikipedia: <a href="http://de.wikipedia.org/wiki/Kellerautomat">Kellerautomat</a></li>
    <li><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/tgi_skript_ws11.pdf">Theoretische Grundlagen der Informatik</a>: Skript von Prof. Dr. Dorothea Wagner, ab S. 105</li>
	<li><a href="../sprachen-automaten-und-grammatiken/" title="Sprachen, Automaten und Grammatiken: Ein &Uuml;berblick">Sprachen, Automaten und Grammatiken: Ein &Uuml;berblick</a></li>

</ul>
