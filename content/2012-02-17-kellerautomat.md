---
layout: post
title: Kellerautomat
slug: kellerautomat
lang: de
author: Martin Thoma
date: 2012-02-17 20:17:01.000000000 +01:00
category: German posts
tags: Abstract machine, Theoretical computer science
---
Ein Kellerautomat ist ein endlicher Automat mit einem Stack („Kellerspeicher"). Er wird mit PDA (pushdown automaton) bzw. NPDA (nondeterministic pushdown automaton) abgekürzt.

Laut Wikipedia verwendet die Gleitkommaeinheit einen PDA. Dazu habe ich allerdings keine Quelle gefunden, das ist also mit Vorsicht zu genießen.

Ein weiterer Einsatzzweck ist die Syntaxanalyse einer Tokenfolge. Das kann für Compiler oder Interpreter von Interesse sein.

## Definitionen

Der **Kellerautomat** ist als 7-Tupel definiert:

$(Q, \Sigma, \Gamma, q_0, Z_0, \delta, F)$, wobei

- Q: endliche Zustandsmenge
- $\Sigma$: endliches Eingabealphabet
- $\Gamma$: endliches Stack-Alphabet
- $q_0 \in Q$: Anfangszustand
- $Z_0 \in \Gamma$: Initialisierung des Stacks
- $\delta: Q \times (\Sigma \cup \{\varepsilon\}) \times \Gamma \rightarrow 2^{Q \times \Gamma^*}$: Überführungsfunktion
- $F \subseteq Q$: Menge der akzeptierenden Endzustände

Bemerkenswert ist hierbei, dass F leer sein kann. Dies ist möglich, da ein PDA auch durch einen leeren Stack akzeptieren kann.

Die Zustandsüberführungsfunktion ist etwas umständlich beschrieben. Dort steht, dass jede Regel folgende Form hat:
$\delta(\text{Zustand}, \text{Eingabesymbol}, \text{Stack-Symbol}) = (\text{Neuer Zustand}, \text{Neuer Stack})$

Die **Konfiguration eines PDA** ist ein Tripel $(q, w, \alpha)$, wobei

- $q \in Q$: aktueller Zustand
- $w \in \Sigma^*$: der Teil der Eingabe, der noch nicht gelesen wurde
- $\alpha \in \Gamma^*$: der Stack-Inhalt

Ein PDA ist <strong>deterministisch</strong> $: \Leftrightarrow |\delta(q, a, Z)| + |\delta(q, \varepsilon, Z)| \leq 1 ~~~ \forall_{q \in Q, a \in \Sigma, Z \in \Gamma}$.

## Anschaulich

Du hast einen Kartenstapel (deine Eingabe, auf der du immer nur ein Zeichen lesen darfst),
einen Stapel für Notizzettel, wobei am Anfang nur ein Notizzettel dort liegt und immer nur ein Symbol auf dem Zettel steht (dein Stack, der mit $Z_0 \in \Gamma$ initialisiert ist),
einen Zustand und eine Menge Regeln ($\delta$).

Nun schaust du dir in jedem Schritt die oberste Karte auf dem Kartenstapel an und legst sie weg. Des Weiteren schaust du dir deine oberste Notiz an und legst sie weg und überprüfst deinen Zustand. Aus diesen Informationen schlussfolgerst du, was du als nächstes machst. Du kannst dir aussuchen in welchen Zustand du gehen willst und was du noch auf deinen Notiz-Stapel tun willst. Du kannst auch einfach nichts auf den Notiz-Stapel legen.

## Beispiele
Sei $L = \{w \in \{0,1,2\}^* | w = 0^i1^j2^j ~~~ i, j \in \mathbb{N}\}$

$(\{q_0, q_1, q_2\}, \{0, 1, 2\}, \{1, \#\}, q_0, \#, \delta, \emptyset)$ mit

$\delta(q_0, 0, \#) = \{(q_0, \#), (q_1, \#)\}, $
$\delta(q_1, 1, \#) = \{(q_1, 1)\}, $
$\delta(q_1, 1, 1) = \{(q_1, 11)\}, $
$\delta(q_1, 2, 1) = \{(q_2, \varepsilon)\}, $
$\delta(p, a, Z) = \emptyset $ sonst.

Der Kellerautomat akzeptiert durch einen leeren Stack. Aus diesem Grund legen wir am Anfang auch immer wieder # auf den Stack. Sonst würde der PDA zu früh akzeptieren.

Da $|\delta(q_0, 0, \#)| = 2 > 1$ ist dieser Kellerautomat nicht-deterministisch.

## Umformungen

### Akzeptierender Endzustand → leerer Stack
Siehe Skript von Prof. Dr. Dorothea Wagner, S. 107.

Gegeben sei ein Kellerautomat ${\cal K}_1 (Q_1, \Sigma, \Gamma_1, \delta_1, q_0^1, Z_0^1, F_1)$ der durch akzeptierenden Endzustand akzeptiert.
Wir wollen einen neuen Automaten ${\cal K}_2 (Q_2, \Sigma, \Gamma_2, \delta_2, q_0^2, Z_0^2, F_2)$, der durch einen leeren Stack akzeptiert.

**Idee**: Wir führen einen neuen Zustand $q_E$ ein, bei dessen Erreichen wir den Stack leeren. Um zu verhindern, dass der Stack zwischenzeitlich leer wird, legen wir zu Beginn das Stack-Symbol $Z_0^2$ ab.

**Formal**:
$Q_2 := Q_1 \cup \{q_0^2, q_E\}$, wobei $q_0^2$ der neue Anfangszustand von ${\cal K}_2$ ist.
$\Gamma_2 := \Gamma_1 \cup \{Z_0^2\}$, wobei $Z_0^2$ den Stack initialisiert.

Die Menge $\delta_2(q, a, Z)$ für $a \in \Sigma \cup \{\varepsilon\}$ und $Z \in \Gamma_2$ sei durch folgende Bedingungen festgelegt:

Sorge für die gleiche Anfangssituation:
$\delta_2(q_0^2, \varepsilon, Z_0^2) = \{(q_0^1, Z_0^1Z_0^2)\}$

Falls der Zustand, das gelesene Zeichen und das Stack-Symbol im „alten" Automaten sind, dann wie gehabt:
$\delta_2(q, a, Z) = \delta_1(q, a, Z) \text{ für } (q \in Q_1, a \neq \varepsilon, Z \in \Gamma_1) \lor (q \in Q_1 \setminus F_1, a = \varepsilon, Z \in \Gamma_1)$

Sorge dafür, dass die Stack-Leerungsregel aufgerufen wird, falls der Zustand akzeptierend ist:
$\delta_2(q, \varepsilon, Z) = \delta_1(q, \varepsilon, Z) \cup \{(q_E, \varepsilon)\} \text{ für } q \in F_1, Z \in \Gamma_2$

Diese Regel leert den Stack:
$\delta_2(q_E, \varepsilon, Z) = \{(q_E, \varepsilon)\}  \text{ für } Z \in \Gamma_2$

### Leerer Stack → akzeptierender Endzustand

Siehe Skript von Prof. Dr. Dorothea Wagner, S. 107.

Gegeben sei ein Kellerautomat ${\cal K}_1 (Q_1, \Sigma, \Gamma_1, \delta_1, q_0^1, Z_0^1, F_1)$, der durch einen leeren Stack akzeptiert.
Wir wollen einen neuen Automaten ${\cal K}_2 (Q_2, \Sigma, \Gamma_2, \delta_2, q_0^2, Z_0^2, F_2)$, der durch einen akzeptierenden Endzustand akzeptiert.

**Idee**: Wir legen ein zusätzliches Symbol $Z_0^2$ auf den Stack. Wird $Z_0^2$ gelesen, ist der Stack noch nicht leer, aber man kann in einen akzeptierenden Zustand $q_F$ wechseln.

**Formal**:
$Q_2 := Q_1 \cup \{q_0^2, q_F\}$, wobei $q_0^2$ Anfangszustand von ${\cal K}_2$ ist und $F_2 := \{q_F\}$
$\Gamma_2 := \Gamma_1 \cup \{Z_0^2\}$, wobei $Z_0^2$ Initialisierung des Stacks von ${\cal K}_2$ ist und $\delta_2$ festgelegt durch:

Zuerst sorgen wir dafür, dass $Z_0^2$ ganz unten im Stack ist:
$$\delta_2(q_0^2, a, X) =
\begin{cases}
\{q_0^1, Z_0^1, Z_0^2\} & \text{falls } a= \varepsilon \text{ und } X = Z_0^2\\
\emptyset               & \text{sonst}
\end{cases}$$

Dann wie gehabt:
$\delta_2(q, a, Z) = \delta_1(q, a, Z) \text{, falls } q \in Q_1, a \in \Sigma \cup \{\varepsilon\} \text{ und } Z \in \Gamma_1$

Und am Schluss auch akzeptieren:
$\delta_2(q, \varepsilon, Z_0^2) = \{(q_F, \varepsilon)\} \text{ für } q \in Q_1$.

## Dies und das

- Ein Kellerautomat mit zwei Stacks ist Turing-mächtig. (→ [Zweikellerautomat](http://de.wikipedia.org/wiki/Zweikellerautomat))
- Ein NPDA erkennt genau die kontextfreien Sprachen.
- Ein PDA erkennt manche kontextfreie Sprachen, aber nicht alle. (Genauer: [Deterministisch kontextfreie Sprache](http://de.wikipedia.org/wiki/Deterministisch_kontextfreie_Sprache))
- Zu jedem PDA, der eine Sprache L durch einen akzeptierenden Endzustand akzeptiert, kann ein PDA konstruiert werden, der L mit leerem Stack akzeptiert (und umgekehrt).
- Für jede Grammatik G in Greibach-Normalform gibt es einen PDA.


## Siehe auch

- Wikipedia: [Kellerautomat](http://de.wikipedia.org/wiki/Kellerautomat)
- [Theoretische Grundlagen der Informatik](http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/tgi_skript_ws11.pdf): Skript von Prof. Dr. Dorothea Wagner, ab S. 105
- [Sprachen, Automaten und Grammatiken: Ein Überblick](../sprachen-automaten-und-grammatiken/)
