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

In der Vorlesung 'Informationsfusion' ist der Kalman-Filter ein zentraler
Inhalt.

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
    <dd>Der Kalman-Filter ist ein iterativer Algorithmus, welcher in jedem
        Schritt weitere Daten erhält und so den wahren Wert
        (z.B. Geschwindigkeit) ermittelt. Er
        benötigt unsicherheitsbehaftete Messungen unter dem Einfluss von
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
        $$x_{n+1}^P = A x_n + B u_n + G v_n$$
        mit
        <ul>
             <li>$x \in \mathbb{R}^{p \times 1}$ ist der Systemzustand.</li>
             <li>$A \in \mathbb{R}^{p \times p}$ heißt Systemmatrix bzw.
                  Übergangsmatrix und beschreibt wie der Zustand $x_n$ in
                  $x_{n+1}$ übergeht. Sie ist also z.B.
                  $$A = \begin{pmatrix}1 & \Delta t\\0 & 1\end{pmatrix}$$</li>
             <li>$u_n \in \mathbb{R}^{q \times 1}$ ist der deterministische
                 Eingangsvektor (control variable matrix)</li>
             <li>$B \in \mathbb{R}^{p \times q}$ heißt Steuermatrix</li>
             <li>$v_n \in \mathbb{R}^{s \times 1}$ ist der Rauschvektor</li>
             <li>$G \in \mathbb{R}^{p \times s}$ heißt Rauschmatrix</li>
             <li></li>
         </ul>

        Beobachtungsgleichung:
        $$\hat{z}_n = C x_n^M + \mu_n$$
        mit
        <ul>
            <li>$\hat{z}_n \in \mathbb{R}^{r \times 1}$ Ausgangsvektor /
                Beobachtungsvektor</li>
            <li>$C \in \mathbb{R}^{r \times p}$ heißt Beobachtungsmatrix</li>
            <li>$x \in \mathbb{R}^{p \times 1}$ ist der Systemzustand.</li>
            <li>$\mu_n \in \mathbb{R}^{r \times 1}$ heißt
                Beobachtungs-Rauschvektor</li>
        </ul>

        Update der process covariance matrix (mit process noise covariance
        matrix $Q_k$):

        $$P_{k}^P = A P_{k-1} A^T + Q_k$$

        Der Kalman-Gain ist:

        $$K = \frac{P_k^P H}{H P_k^P H^T + R}$$

        Update das Zustands:

        $$x_n = x_k^P + K (\hat{z}_n - H x_k^P)$$

        Update des Fehlers:

        $$P_k = (I - KH) P_k^P$$

        Weiteres:
        <ul>
            <li>Michael van Biezen: <a href="http://www.ilectureonline.com/lectures/subject/SPECIAL%20TOPICS/26/190">Kalman Filter</a></li>
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


## Prüfungsfragen

* Welche Arten von Unsicherheit kennen Sie?<br/>
  → TODO
* Wie lautet die Formel für verteilte Fusion?<br/>
  → TODO
* Wie lauten die Axiome von Kolmogorov?<br/>
  → TODO
* Was sind Zugehörigkeitsfunktionen?<br/>
  → TODO

### Kalman-Filter

* Aus welchen Schritten besteht der Kalman-Filter?<br/>
  → Prädiktion, Innovation
* Welche erweiterungen zum Kalman-Filter kennen Sie?<br/>
  → Extended Kalman Filter (EKF), UKF (TODO)
* Für welche Systeme ist der Kalman-Filter geeignet?<br/>
  → Lineare Zeitinvariante Systeme (LTI-Systeme)
* Wie entwickeln sich die Wahrscheinlichkeiten beim Kalman-Filter?<br/>
  → Bei der Prädiktion steigt die Unsicherheit, bei der Innovation sinkt sie.
* Wie lautet das Systemmodell im Kalman-Filter?<br/>
  → TODO (Systemgleichung und Beobachtungsgleichung)


## Material und Links

* [Vorlesungswebsite](http://ies.anthropomatik.kit.edu/lehre_informationsfusion.php)
* [Anki-Deck](https://ankiweb.net/shared/info/1070725022)


## Vorlesungs&shy;empfehlungen

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
