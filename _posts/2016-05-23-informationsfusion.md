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
* Kalmann-Filter (KF)
* Extended Kalmann-Filter (EKF)
* Guide to the Expression of Uncertainty in Measurement (GUM)
* Bayessche Methodik

<dl>
    <dt><a href="https://en.wikipedia.org/wiki/Probability_axioms#Axioms"><dfn id="kolmogorov-axioms">Kolmogorov-Axiome</dfn></a></dt>
    <dd>TODO</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Kalman-Filter"><dfn id="kalman-filter">Kalman-Filter</dfn></a></dt>
    <dd>Siehe <a href="https://martin-thoma.com/kalman-filter/">Kalman-filter Artikel</a>.</dd>
    <dt><dfn id="extended-kalman-filter">Extended Kalman Filter</dfn> (<dfn id="ekf">EKF</dfn>)</dt>
    <dd>

        Siehe: <a href="http://www.cbcity.de/das-extended-kalman-filter-einfach-erklaert">Das Extended Kalman Filter einfach erklärt</a>

    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/GUM_(Norm)"><dfn id="gum">GUM</dfn></a> (<dfn>Guide to the Expression of Uncertainty in Measurement</dfn>)</dt>
    <dd>GUM ist eine internationale Norm welche das Ziel hat, die
        Vergleichbarkeit zwischen Messergebnissen herzustellen. Dazu
        wurden in der Norm Grundsätze und Vorgehensweisen zur Bestimmung der
        Messunsicherheit festgelegt.<br/>
        <br/>
        GUM ist auf metrische Merkmale beschränkt.</dd>
    <dt><dfn>Standardunsicherheit</dfn></dt>
    <dd>Die Standardunsicherheit einer Messung ist

        $$u_i = s(\bar{x_i}) = \sqrt{\frac{s^2(x_i)}{n}}$$</dd>
</dl>


### Dempster-Shafer-Theorie

Slides: `IF-Kap3_160125.pdf`

<dl>
    <dt><dfn>Dempsters Kombinationsregel</dfn> (<dfn>Dempsters rule of combination</dfn>, <dfn>DRC</dfn>)</dt>
    <dd>$$m_1 \oplus m_2 (A) := \begin{cases}0&\text{for } A = \emptyset\\
                                             \frawc{\sum{X, Y: X \cap Y = A} m_1(X) m_2(Y)}{|1-K|}\end{cases}$$
        für Konfliktgrad $$K := \sum_{X, Y: X \cap Y = \emptyset} m_1(X) m_2(Y)$$
        Bei einem Konfliktgrad von $0 < K < 1$ spricht man von einem
        partiellen Konflikt. Ist der Konfliktgrad gleich $K=1$, so ist DRC
        nicht anwendbar.<br/>
        <br/>
        DRC ist assoziativ und kommutativ, allerdings nicht idempotent.
        Es gilt also im Allgemeinen nicht $m \oplus m = m$.</dd>
</dl>


### Fuzzy-Systeme

Slides: `IF-Kap4_160125.pdf`

<dl>
    <dt><dfn>Zugehörigkeitsfunktion</dfn></dt>
    <dd>Eine Zugehörigkeitsfunktion ist eine Funktion $\mu_A: A \rightarrow [0, 1]$ zu
        einem Grundraum $\Omega$ mit $A \subseteq \Omega$.
        Dann gilt
        $$\mu_{\Omega \setminus A}(t) = 1 - \mu_{A}$$</dd>
    <dt><dfn>Defuzzifizierung</dfn></dt>
    <dd>Unter Defuzzifizierung versteht man die Berechnung des scharfen
        Wertes der Ausgangsgröße.</dd>
    <dt><dfn>Schwerpunktverfahren</dfn></dt>
    <dd>Das Schwerpunktverfahren dient zur Defuzzifizierung.</dd>
</dl>


### Neuronale Netze

Slides: `IF-Kap5_160125.pdf`

Siehe [Vorlesung Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)


### Registrierung

Slides: `IF-Kap6_160125.pdf`

Wurde nicht besprochen.


### Energiefunktionale

Slides: `IF-Kap7_160125.pdf`

<dl>
    <dt><a href="https://de.wikipedia.org/wiki/Funktional"><dfn>Funktional</dfn></a></dt>
    <dd>Ein <i>Funktional</i> ist eine Funktion aus einem Vektorraum $V$ in
        den Körper, der dem Vektorraum zugrunde liegt. Oft ist $V$ ein
        Funktionenraum, also ein Vektorraum, dessen Elemente reell- oder
        komplexwertige Funktionen sind. Ein Funktional ist somit eine Funktion
        auf Funktionen.</dd>
    <dt><dfn id="energiefunktionale">Energiefunktionale</dfn></dt>
    <dd>Durch die Einführung von Energietermen $E_k$ lassen sich
        fusionsrelevante Informationen modellieren. Die Fusionsaufgabe wird
        dann durch das Energiefunktional

        $$E = \sum_k \lambda_k E_k, \qquad \lambda_k > 0$$

        repräsentiert. Die unterschiedliche Relevanz der Energieterme $E_k$
        wird durch die Vorfaktoren $\lambda_k$ berücksichtigt.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Boltzmann_distribution"><dfn id="gibbs-distribution">Gibbs-Verteilung</dfn></a></dt>
    <dd>Die Gibbs-Verteilung mit dem Energiefunktional $E$ ist
        $$\pi_{\beta, E}(x) = \frac{1}{Z} e^{- \beta E(x)},$$
        mit Normierungskonstante $Z$ und der inversen Temperatur
        $\beta = \frac{1}{T}$.<br/>
        <br/>
        <u>Interpretation</u>:
        Es sei $E: V \rightarrow \mathbb{R}$, $V$ endlich.
        <ul>
            <li>$V$: Die Menge aller Konfigurationen eines physikalischen Systems.</li>
            <li>$E(x)$: Energie des Systems, wenn es sich in der Konfiguration $x$ befindet.</li>
            <li>$T$: Temperatur. Ist die Temperatur groß, so sind alle
                Konfigurationen etwa gleich wahrscheinlich. Bei niedriger
                Temperatur werden Konfigurationen mit niedriger Energie
                bevorzugt.</li>
            <li>$\pi_{\beta, E}(x)$: Wahrscheinlichkeit, dass sich das System
                in der Konfiguration $x$ befindet.</li>
        </ul>

        Für $E$ kann dann eine Gibbsche Wahrscheinlichkeitsdichtefunktion WDF
        $$WDF \propto e^{- \beta E} = \prod_k e^{-\frac{\lambda_k E_k}{T}}$$
        definiert werden.
        </dd>
    <dt><dfn>Energieminimierung</dfn></dt>
    <dd>

        <ol>
            <li>Lösung eines linearen Gleichungssystems (selten möglich)</li>
            <li>Graph-Cuts-Verfahren</li>
            <li>Approximative Lösung durch sukzessive Optimierung</li>
            <li>Methode des steilsten abstiegs</li>
            <li>Monte-Carlo-Methode</li>
            <li>Simulated Annealing</li>
            <li>Lineare Programme</li>
            <li>Dynamische Programmierung</li>
            <li>Mean Field Theorie (Betrachte Erwartungswerte)</li>
        </ol>

    </dd>
</dl>


## Abkürzungen

* EKF: Extended Kalman Filter
* GUM: Guide to the Expression of Uncertainty in Measurement
* KF: Kalman Filter
* LS: Least Squares
* UKF: Unscented Kalman Filter


## Meine Fragen

* Kapitel 1, Folie 61: Was ist der Definitions / Wertebereich von Information?
* Kapitel 2, Folie 5: Alle Ereignisse paarweise disjunkt
* Kapitel 2, Folie 22: Man muss für wirksame Schätzer noch fordern, dass sie
                       erwartungstreu sind. Es gibt immer den konstanten
                       Schätzer, welcher die Stichprobe ignoriert und somit
                       eine Varianz von 0 hat.
* Kapitel 2, Folie 37: Was ist ein Arbeitspunkt?
* Kapitel 2, Folie 44f: Fusion 2er größen / Verteilungen
* Kapitel 2, Folie 79: Was ist der Trunkation error? Was ist der base point error und warum ist es ein Problem, dass man um den Schätzwert und nicht um den wahren Wert linearisiert?

## Prüfungsfragen

* Welche Arten von Unsicherheit kennen Sie?<br/>
  → TODO
* Wie lautet die Formel für verteilte Fusion?<br/>
  → TODO
* Wie lauten die Axiome von Kolmogorov?<br/>
  → Siehe <a href="#kolmogorov-axioms">oben</a>
* Was sind Zugehörigkeitsfunktionen?<br/>
  → TODO

### Kalman-Filter

* Aus welchen Schritten besteht der Kalman-Filter?<br/>
  → Prädiktion, Innovation
* Welche erweiterungen zum Kalman-Filter kennen Sie?<br/>
  → Extended Kalman Filter (EKF), UKF (Unscented Kalman Filter)
* Für welche Systeme ist der Kalman-Filter geeignet?<br/>
  → Lineare Zeitinvariante Systeme (LTI-Systeme)
* Wie entwickeln sich die Wahrscheinlichkeiten beim Kalman-Filter?<br/>
  → Bei der Prädiktion steigt die Unsicherheit, bei der Innovation sinkt sie.
* Wie lautet das Systemmodell im Kalman-Filter?<br/>
  → TODO (Systemgleichung und <a href="#beobachtungsgleichung">Beobachtungsgleichung</a>)


## Absprachen

* Kapitel 5 (Neuronale Netze) und Kapitel 6 (Registrierung) kommen nicht dran
* Übungsaufgaben sind auch Prüfungsrelevant


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
