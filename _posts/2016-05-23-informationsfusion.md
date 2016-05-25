---
layout: post
title: Informationsfusion
slug: informationsfusion
author: Martin Thoma
date: 2016-05-23 20:00
category: German posts
tags: Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Informationsfusion&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen nicht gehört, aber die Folien von <a href="http://ies.anthropomatik.kit.edu/mitarbeiter.php?person=heizmann">Herrn Prof. Dr.-Ing. Michael Heizmann</a> aus dem Wintersemester 2015/2016 gelesen.</div>

## Behandelter Stoff

### Grundlagen

Slides: `IF-Kap1_151110.pdf`

Es wurden Grundbegriffe wie Daten, Information, Merkmal, Informationsfusion,
Signal, usw. eingeführt.


### WT

Slides: `IF-Kap2_151215.pdf`

* Wahrscheinlichkeitsraum, Zufallsvariable
* Kalmann-Filter
* Extended Kalmann-Filter
* GUM
* Bayessche Methodik

<dl>
    <dt><a href="https://de.wikipedia.org/wiki/Kalman-Filter"><dfn id="kalman-filter">Kalman-Filter</dfn></a></dt>
    <dd>Der Kalman-Filter ist eine Menge mathematischer Gleichungen. Sie
        benötigen unsicherheitsbehaftete Messungen unter dem Einfluss von
        Störungen und erlauben es eine gute Schätzung für den tatsächlichen
        Wert anzugeben. So geht es z.B. darum die aktuelle Position eines
        sich mit gleichmäßiger Geschwindigkeit bewegenden Agenten zu
        bestimmen. Dabei gibt es zwei Störungen: Zum einen die Messung der
        Position, zum anderen ist die Geschwindigkeit nicht perfekt gleich.<br/>
        <br/>
        Kalman-Filter arbeiten mit linearen verschiebungsinvarianten
        (zeitdiskreten) Systemen.<br/>
        <br/>
        Zustandsgleichung:
        $$x_{n+1} = A x_n + B u_n + G v_n$$
        mit
        <ul>
             <li>$x \in \mathbb{R}^{p \times 1}$ ist der Systemzustand.</li>
             <li>$A \in \mathbb{R}^{p \times p}$ heißt Systemmatrix bzw.
                  Übergangsmatrix und beschreibt wie der Zustand $x_n$ in
                  $x_{n+1}$ übergeht.</li>
             <li>$u_n \in \mathbb{R}^{q \times 1}$ ist der deterministische
                 Eingangsvektor</li>
             <li>$B \in \mathbb{R}^{p \times q}$ heißt Steuermatrix</li>
             <li>$v_n \in \mathbb{R}^{s \times 1}$ ist der Rauschvektor</li>
             <li>$G \in \mathbb{R}^{p \times s}$ heißt Rauschmatrix</li>
             <li></li>
         </ul>

        Beobachtungsgleichung:
        $$\hat{z}_n = C x_n + \mu_n$$
        mit
        <ul>
            <li>$\hat{z}_n \in \mathbb{R}^{r \times 1}$ Ausgangsvektor /
                Beobachtungsvektor</li>
            <li>$C \in \mathbb{R}^{r \times p}$ heißt Beobachtungsmatrix</li>
            <li>$x \in \mathbb{R}^{p \times 1}$ ist der Systemzustand.</li>
            <li>$\mu_n \in \mathbb{R}^{r \times 1}$ heißt
                Beobachtungs-Rauschvektor</li>
        </ul>

        </dd>
</dl>


### Dempster-Shafer-Theorie

Slides: `IF-Kap3_160125.pdf`

TODO


### Fuzzy-Systeme

Slides: `IF-Kap4_160125.pdf`

TODO


### Neuronale Netze

Slides: `IF-Kap5_160125.pdf`

TODO


### Registrierung

Slides: `IF-Kap6_160125.pdf`

TODO


### Energiefunktionale

Slides: `IF-Kap7_160125.pdf`

TODO


## Meine Fragen

* Kapitel 1, Folie 61: Was ist der Definitions / Wertebereich von Information?
* Kapitel 2, Folie 5: Alle Ereignisse paarweise disjunkt
* Kapitel 2, Folie 22: Man muss für wirksame Schätzer noch fordern, dass sie
                       erwartungstreu sind. Es gibt immer den konstanten
                       Schätzer, welcher die Stichprobe ignoriert und somit
                       eine Varianz von 0 hat.
* Kapitel 2, Folie 44f: Fusion 2er größen / Verteilungen


## Material und Links

* [Vorlesungswebsite](http://ies.anthropomatik.kit.edu/lehre_informationsfusion.php)
* [Anki-Deck](https://ankiweb.net/shared/info/1070725022)


## Vorlesungsempfehlungen

Folgende Vorlesungen sind ähnlich:

* [Analysetechniken großer Datenbestände](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/)
* [Informationsfusion](https://martin-thoma.com/informationsfusion/)
* [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/)
* [Machine Learning 2](https://martin-thoma.com/machine-learning-2-course/)
* [Mustererkennung](https://martin-thoma.com/mustererkennung-klausur/)
* [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)
* [Lokalisierung Mobiler Agenten](https://martin-thoma.com/lma/)
* [Probabilistische Planung](https://martin-thoma.com/probabilistische-planung/)


## Termine und Klausurablauf

Es ist eine mündliche Prüfung.
