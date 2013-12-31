---
layout: post
title: Wahrscheinlichkeitstheorie: Aufgaben und Lösungen
author: Martin Thoma
date: 2012-01-14 11:50:50
categories: 
- Cyberculture
- German posts
tags: 
- mathematics
featured_image: 
---
<h2>Kombinatorik</h2>
<h3>Kartenspiel</h3>
Wie hoch ist die Wahrscheinlichkeit im <a href="http://de.wikipedia.org/wiki/Schafkopf">Schafkopf</a> (32&nbsp;Blatt) genau 2 Ober auf der ersten Hand (4&nbsp;Karten) zu haben?

Lösung: 
[latex]A := \text{"Alle möglichen Kombinationen der 4 vorhandenen Ober"}[/latex]
[latex]B := \text{"Alle möglichen Kombinationen für die verbleibenden 2 Karten."}[/latex]
[latex]\frac{A \cdot B}{\text{"Alle möglichen Kombinationen aus 4 Karten"}} = \frac{\binom{28}{2} \cdot \frac{4}{2}}{\binom{32}{4}} = \frac{567}{8990} \approx 6,3 \%[/latex]

Wie hoch ist die Wahrscheinlichkeit, mindestens eine 7, 8 oder 9 auf der Hand (8 Karten) zu haben?

Lösung:
[latex]1 - \frac{\binom{32-3\cdot4}{8}}{\binom{32}{8}} \approx 98,8 \%[/latex]

<h2>Ereignisse umschreiben</h2>
Von drei stochastisch unabhängigen Ereignissen A, B, C sei bekannt [latex]\mathbb{P}(A) = 0,5 ~ \mathbb{P}(B) = 0,6 ~ \mathbb{P}(C) = 0,7[/latex]. Wie hoch ist die Wahrscheinlichkeit, dass A oder B eintritt?

Lösung:
[latex]\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B) = 0,5 + 0,6 - 0,5 \cdot 0,6 = 0,8 = 80 \%[/latex]

<h2>Modellierung</h2>
Eine häufige Aufgabenstellung ist das modellieren von Ereignissen. "Drücken Sie mit Hilfe der Zufallsvariablen [latex]X_n[/latex] die folgenden Ereignisse aus". 

Für Studenten des KIT: Im <a href="https://studium.kit.edu/sites/vab/0x8763DF03F4275B4F908D321A58479E61/vorlesungsunterlagen_pwg/Forms/AllItems.aspx?RootFolder=%2fsites%2fvab%2f0x8763DF03F4275B4F908D321A58479E61%2fvorlesungsunterlagen_pwg%2f%C3%9Cbung%2f%C3%9Cbungsschein&FolderCTID=&View=%7b2672A6DD-CB1A-408E-888B-441716F3F757%7d">VAB</a> für Wahrscheinlichkeitstheorie für Informatiker sind solche Aufgaben auf Blatt 1, Aufgabe 4; Blatt 3, Aufgabe 11.

Gemeinsame Zähldichte errechnen: Blatt 4, Aufgagbe 14