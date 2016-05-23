---
layout: post
title: Mustererkennung - Klausur
author: Martin Thoma
date: 2015-04-27 21:15
category: German posts
tags: Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Mustererkennung&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://ies.anthropomatik.kit.edu/mitarbeiter.php?person=beyerer">Herrn Prof. Dr.-Ing. Jürgen Beyerer</a> im Sommersemester 2015 gehört und einige Abschnitte direkt aus den Folien übernommen.</div>

## Behandelter Stoff

### Vorlesung

<table>
<tr>
    <th>Datum</th>
    <th>Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
    <td>15.04.2015</td>
    <td><a href="https://ies.anthropomatik.kit.edu/ies/download/lehre/me/ME-Kap1_V33.pdf">Einleitung</a></td>
    <td>$\hat{w}$ - das <code>^</code> bedeutet, dass die Klasse geschätzt ist.</td>
</tr>
<tr>
    <td>22.04.2015</td>
    <td><a href="https://ies.anthropomatik.kit.edu/ies/download/lehre/me/ME-Kap2_V85.pdf">Kapitel 2 - Merkmale</a>: 1-31?</td>
    <td>Welt; Domäne; Objekte; Klassen; Merkmalsraum; Merkmalsvektor; Klassifikation; Skalen (nominal, ordinal, intervall-, verhältnis- und absolutskaliert); Projektionen; <a href="https://de.wikipedia.org/wiki/Norm_(Mathematik)#Definition">Norm</a> (Minkowski, Euklidisch, Chebychev, Mahalanobis); <a href="https://de.wikipedia.org/wiki/Metrischer_Raum#Formale_Definition">Metrik</a> (Tanimoto)</td>
</tr>
<tr>
    <td>14.07.2015</td>
    <td><a href="http://ies.anthropomatik.kit.edu/ies/download/lehre/me/ME-Kap8_V25.pdf">Kapitel 8 - Klassifikatoren</a> (1-28), <a href="https://ies.anthropomatik.kit.edu/ies/download/lehre/me/ME-Kap9_V29.pdf">Kapitel 9</a>: 1-?</td>
    <td>Entscheidungsbäume, Grammatiken; Lernen nach Vapnik, VC-dimension, Kreuzvalidierung und Leave-One-Out, Boosting</td>
</tr>
</table>

### Folien

#### ME-Kap1_V31.pdf

**Einleitendes Kapitel** welches erklärt, was Klassifikation ist.

* Beispiele für Klassifikation: Blumen/Schmetterlinge in Arten; Schrauben in Schraubentypen; Schüttgut in Mineralien, Pflanzen, Glasscheiben, Diamante, ...
* Formalismen
  * Domäne $\Omega \subseteq$ Welt, Elemente der Domäne heißen Objekte, Objekte werden in paarweise disjunkte Äquivalenzklassen $\omega_i$ gruppiert, sodass jedes Objekt genau eine Äquivalenzklasse hat.
  * Man beobachtet / misst Eigenschaften realer Objekte. Dies kann als Funktion
    **m** aufgefasst werden, die von der Domäne in den Merkmalsraum abbildet.
    Optimalerweise ist diese Abbildung injektiv, bei ungünstig gewählten
    Merkmalen jedoch nicht. Klassifikatoren arbeiten auf dem Merkmalsraum und
    finden eine Partition des Merkmalsraumes in Klassen
* **Muster**: Gesamtheit der beobachteten / gemessenen Werte einer einzelnen
  Stichprobe (eines einzelnen Objekts).
* **Erkennung**: (Wieder)erkennung von etwas, was bereits bekannt ist.
* **Merkmale**: eruirbare, charakteristische Eigenschaften, die als Basis für
  die Untersuchung von Mustern dienen soll.
* **Mustererkennungsschritte**: Sensierung ergibt Muster; Vorverarbeitung;
  Segmentierung; Merkmalsextraktion ergibt Merkmale; Klassifikation ergibt
  Äquivalenzklassen
* **Überwachtes lernen**: Vorklassifizierte Beispiele sowie die Klassenstruktur
  sind gegeben; eventuell auch Auftrittswahrscheinlichkeiten $P(\omega_i)$ der
  Klassen
* Gesamtstichprobe wird in die disjunkten Mengen Lernstrichprobe,
  Validierungsstichprobe und Teststichprobe zerlegt.

#### Merkmale

Slides: `ME-Kap2_V84.pdf`

In diesem Foliensatz geht es um **Merkmale** und ihre Eigenschaften.

<table border="1">
    <tr>
        <th rowspan="3">&nbsp;</th>
        <th colspan="5">Skala</th>
    </tr>
    <tr>
        <th colspan="2">qualitativ (kategorial)</th>
        <th colspan="3">quantitativ (metrisch)</th>
    </tr>
    <tr>
        <th>Nominal-</th>
        <th>Ordinal-</th>
        <th>Intervall-</th>
        <th>Verh&auml;ltnis-</th>
        <th>Absolut</th>
    </tr>
    <tr>
        <th>Empirische Relation</th>
        <td>~ &Auml;quivalenz</td>
        <td>~ &Auml;quivalenz<br/>Ordnung</td>
        <td>~ &Auml;quivalenz<br/>Ordnung<br/>Emp. Addition</td>
        <td>~ &Auml;quivalenz<br/>Ordnung<br/>Emp. Addition<br/>Emp. Multipliation</td>
        <td>~ &Auml;quivalenz<br/>Ordnung<br/>Emp. Addition<br/>Emp. Multipliation</td>
    </tr>
    <tr>
        <th>Zul&auml;ssige Transformationen</th>
        <td>m' = f(m)<br/>f bijektiv</td>
        <td>m' = f(m)<br/>f streng monoton</td>
        <td>m' = am+b<br/>mit a&gt;0</td>
        <td>m' = am<br/>mit a&gt;0</td>
        <td>m' = m</td>
    </tr>
    <tr>
        <th>Beispiele zugeh&ouml;rige Merkmale</th>
        <td>Telefonnummern, Kfz-Kennz., Typen, PLZ, Geschlecht</td>
        <td>G&uuml;teklassen, H&auml;rtegrad, Windst&auml;rke</td>
        <td>Temp. in &deg;C, &deg;F, Kalenderzeit, geographische H&ouml;he</td>
        <td>Masse, L&auml;nge, el. Strom</td>
        <td>Quantenzahlen, Teilchenanzahl, Fehlerzahl</td>
    </tr>
    <tr>
        <th>Werte von m</th>
        <td>Zahlen, Namen, Symbole</td>
        <td>in der Regel nat&uuml;rliche Zahlen</td>
        <td>in der Regel reele Zahlen</td>
        <td>in der Regel reele Zahlen &gt; 0</td>
        <td>in der Regel nat&uuml;rliche Zahlen</td>
    </tr>
</table>

Der Merkmalsraum ist häufig ein $\mathbb{R}^n$ mit $n>3$. Er kann auf
vorhandene Strukturen analysiert werden, indem er auf einen 2- oder
3-dimensionalen unterraum projeziert wird. Dies kann bei einfachen Projektionen
jedoch nicht erfolgreich sein, wenn beispielsweise zwei Klassen Schalenförmig
um den Urspruch angeordnet sind.

Um Stichproben im Merkmalsraum zu vergleichen können Metriken benutzt werden.
Eine [Metrik](https://de.wikipedia.org/wiki/Metrischer_Raum#Formale_Definition)
ist eine Abbildung $d(m_1, m_2)$, für die gilt:

* Positive Definitheit: $d(m_1, m_2) \geq 0$ und $d(m_1, m_2) = 0 \Leftrightarrow m_1 = m_2$,
* Symmetrie: $d(m_1, m_2) = d(m_2, m_1)$,
* Dreiecksungleichung: $d(m_1, m_2) \leq d(m_1, m_3) + d(m_3, m_2)$

Metriken können durch [Normen](https://de.wikipedia.org/wiki/Norm_(Mathematik)#Definition)
erzeugt werden, indem $d(m_1, m_2) := \|m_1 - m_2\|$ definiert wird. Eine Norm
ist eine Abbildung $\| \cdot \|: V \rightarrow \mathbb{R}_0^+, x \mapsto \|x\|$
für die gilt:

* Definitheit: $\|x\| = 0 \Rightarrow x = 0$
* Absolute Homogenität: $\|\alpha \cdot x \| = \alpha \cdot \| x \|$
* Dreiecksungleichung: $\|x+y\| \leq \|x\| + \|y\|$

Typische Normen sind die
[euklidische Norm](https://de.wikipedia.org/wiki/Euklidische_Norm) und die
Mahalanobis Norm $\|m\| := \sqrt{m^T A m}$ mit $A$ positiv definit.

**Hauptkomponentenanalyse** (HKA, engl. PCA)

1. Finde $m_0$, sodass $J_0(m) := \sum_{k=1}^N \|m - m_k\|^2$ minimal ist, also
   $m_0 = \frac{1}{N} \sum_{k=1}^N m_k$
2. Finde Gerade $h: m = \bar{m} + ae$, welche die Punkte optimal repräsentiert.
    1. Finden der $a_k$ (TODO: Was ist das?)<br/>
       Fehlermaß $J_1(a_1, \dots, a_N, e) = \sum_{k=1}^N \|\bar{m} + a_k e - m_k \|^2$.<br/>
       Ergibt: $a_k = e^T (m_k - \bar{m})$
    2. Berechnung des optimalen Richtungsvektors<br/>
       Streumatrix $S := \sum_{k=1}^N (m_k - \bar{m}) (m_k - \bar{m})^T$
3. Finden eines affinen $d'$-dimensionalen Unterraumes des Merkmalsraumes,
   welcher die Daten $D$ mit minimalen quadratischem Fehler repräsentiert.

Siehe [gist](https://gist.github.com/MartinThoma/09799f5d143c09399eed) für
eine kurze Python-Implementierung. Keine Garantie für die Korrektheit!

* Kernelized PCA
* Independent Component Analysis (ICA)
* Multiple Discriminant Analysis (MDA)


#### ME-Kap3_V52.pdf

**Bayessche Klassifikatoren** wählen die Klasse aus, die die größte
Wahrscheinlichkeit besitzt. Dazu verfolgt man den Ansatz

$$P(\omega|m) = \frac{p(m|\omega) \cdot P(\omega)}{p(m)}$$

Dabei wird $P(\omega|m)$ die *A Posteriori Wahrscheinlichkeitsverteilung*
und $P(\omega)$ die *A Priori Wahrscheinlichkeitsverteilung* genannt.

#### ME-Kap4_V33.pdf

**Parameterschätzung** kann entweder mit der Likelihood-Methodik oder mit der
Bayesschen Methodik durchgeführt werden. Die Idee der Likelihood-Methodik ist
es, den Parameter $\theta$ als unbekannte konstante (d.h. nicht-stochastische)
Größe anzusehen. Man wählt $\theta$ also so, dass die Wahrscheinlichkeit der
Beobachtungen gegeben $\theta$ maximiert wird.

Die Bayessche Methodik geht dagegen davon aus, dass $\theta$ auch eine
Zufallsvariable ist und über eine Wahrscheinlichkeitsverteilung beschrieben
werden kann.

Schätzer können verschiedene Qualitätskriterien erfüllen, z.B.
[Erwartungstreue](https://de.wikipedia.org/wiki/Erwartungstreue)
oder [Konsistenz](https://de.wikipedia.org/wiki/Konsistenz_(Statistik)).

Bei der Parameterschätzung können folgende Fehler passieren:

* Bayesscher Fehler: (TODO: Was ist das?)
* Modellfehler: Unpassendes Modell gewählt (Falsche Verteilungsannahme?)
* Schätzfehler: Zu wenige Daten um Parameter korrekt zu bestimmen


#### ME-Kap5_V31.pdf

**Parameterfreie Methoden** heißen "parameterfrei", weil sie keine konkrete
Wahrscheinlichkeitsverteilung parametrisieren und den Parameter schätzen.
Die Parameterfreien Methoden können sehr wohl Parameter benutzen. Beispiele
sind:

* [Parzen Window](https://de.wikipedia.org/wiki/Kerndichtesch%C3%A4tzer)
* [Nächste Nachbarn](https://de.wikipedia.org/wiki/N%C3%A4chste-Nachbarn-Klassifikation)


#### ME-Kap6_V18.pdf

**Allgemeine Problemstellungen**:

* Dimension des Merkmalsraumes
* Overfitting

#### ME-Kap7_V54.pdf

**Spezielle Klassifikatoren**:

* Lineare Diskriminanzfunktionen: Linear bezieht sich hier auf die Kombination
  der Merkmale. Man kann allerdings Merkmale wählen, die z.B. das quadrat eines
  gemessenen wertes sind.
* Perzeptron
* Lineare Regression
* Künstliche Neuronale Netze
* Support Vector Machines (SVMs)
* Matched Filter
* HMMs (Sequenzen)
* Klassifikation mit Rückweisung (Maximum / Minimum / Differenz / Abstand)

#### ME-Kap8_V21.pdf

**Klassifikation bei nominalen Merkmalen**:

* Entscheidungsbäume
* String-Verfahren
* Grammatiken


#### ME-Kap9_V27.pdf

**Klassifikatorunabhängige Prinzipien**:

* Generalisierung / Generalisierungsfähigkeit
* VC-Konfidenz / VC-Dimension
* Structural Risc Minimization
* [Kreuzvalidierungsverfahren](https://de.wikipedia.org/wiki/Kreuzvalidierungsverfahren) / Leave-one-out
* Boosting


### Prüfungsfragen

* Warum ist ein hochdimensionaler Merkmalsraum schlecht
  ([curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality))?
  - Je nach Klassifikator, viele zu lernende Parameter
  - Daten haben einen sehr hohen Abstand zueinander → Gefahr des Overfittings
* Wie kann man die Dimension des Merkmalsraumes reduzieren?<br/>
  → Merkmalsauswahl, suboptimales iteratives Verfahren, HKA
  (Varianzen maximieren), MDA (Klassentrennbarkeit maximieren), ICA
* Wie viele Möglichkeiten gibt es 5 Merkmale aus 10 auszuwählen? → [Binomialkoeffizient](https://de.wikipedia.org/wiki/Binomialkoeffizient)
* Was ist Overfitting?<br/>
  → Siehe <a href="https://martin-thoma.com/machine-learning-1-course/#overfitting">ML 1</a>
* Welche Probleme gibt es, wenn man Länge, Masse und Temperatur als Merkmale hat?
  - Unterschiedliche Einheiten (→ Entdimensionalisieren)
  - Unterschiedliche Skalen (→ Teilen durch Varianz oder durch Wertebereich)
  - Unterschiedliche Wertebereiche (→ Durchschnitt abziehen)
* Wie funktioniert MDA?<br/>
  → Sie maximiert <span markdown=0>$J(w) = \frac{|m'_1 - m'_2|^2}{s'_1^2 - s'_2^2}$</span>
  (im 2-Klassen Fall, wobei $w$ die Ebene ist, auf die projeziert wird)
* Wie unterscheidet sich PCA/MDA von dem suboptimalen Algorithmus zur
  Merkmalsauswahl?<br/>
  → PCA/MDA sind Klassifikatorunabhängig, aber der suboptimale
  Algorithmus benötigt bereits einen Klassifikator.
* Wie lautet die Fundamentalformel der Bayesschen Klassifikation?<br/>
  → $P(A|B) = \frac{P(A)\, P(B | A)}{P(B)}$ (wobei üblicherweise B das Merkmal
  ist und A die Klasse)
* Wie lautet die Hauptformel der PCA?<br/>
  $m' = A^T \cdot (m - \bar{m})$, wobei $A$ die Basiswechselmatrix ist.
* Wie kann man invariante Merkmale erzeugen?<br/>
  → Integration über eine Transformationsgruppe, Differentielle Methode,
  Normalisierung
* Wie kann man normalisieren?<br/>
  → Fourierdeskriptoren kann man invariant bzgl. Translation und Rotation und
  radialer Streckung (Skalierung) machen
* Wie lauten die Prinzipien (A) - (E) der SVMs?
    - (A) Lineare Trennung mit maximalen Abstand der Trennebenen zu den
          nächstgelegenen Stichproben (Support Vektoren)
    - (B) Duale Formulierung des linearen Klassifikators.
          (vgl. [Wiki](https://de.wikipedia.org/wiki/Support_Vector_Machine#Duales_Problem), $k(m) = w^T m + b = \langle w, m \rangle + b = \sum_{j=1}^N \alpha_j z_j \langle m_j, m \rangle + b$)
    - (C) Nichtlineare Abbildung der primären Merkmale in einen
          hochdimensionalen Merkmalsraum $\Phi$
    - (D) Implizite Nutzung des unter Umständen $\infty$-dimensionalen
          Eigenfunktionsraumes einer sog. Kernfunktion $K$ als transformierten
          Merkmalsraum $\Phi$. Dabei müssen die transformierten Merkmale nicht
          explizit berechnet werden und der Klassifikator hat trotz der hohen
          Dimension von $\Phi$ nur eine niedrige Zahl von freien Parametern
          (Kernel-Trick).
    - (E) Relaxation der Forderung nach linearer Trennbarkeit durch Einführung
          von Schlupfvariablen (slack variables).
* Wie lautet die Dichtefunktion der [$d$-dimensionale Gaußverteilung](https://de.wikipedia.org/wiki/Mehrdimensionale_Normalverteilung)? $f_X(x) = \frac{1}{\sqrt{(2\pi \det{\Sigma})}} \exp(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu))$
* Wie lautet Mercers Theorem? → [wiki](https://de.wikipedia.org/wiki/Satz_von_Mercer)
* Wie ist die [Kullback-Leibler-Divergenz](https://de.wikipedia.org/wiki/Kullback-Leibler-Divergenz) defininiert?

## Material und Links

* [Vorlesungswebsite](http://ies.anthropomatik.kit.edu/lehre_mustererkennung.php): Ist passwortgeschützt. Das Passwort (das ausnahmsweise mal nicht zu erraten ist) kann ich hier natürlich nicht schreiben. Aber der Benutzername ist `asbstudent`.
* SVMs
  * [Why bother with the dual problem when fitting SVM?](http://stats.stackexchange.com/q/19181/25741)
  * [A Tutorial on Support Vector Machines for Pattern Recognition](http://research.microsoft.com/pubs/67119/svmtutorial.pdf)

## Übungsbetrieb

Es gibt keine Übungsblätter, keine Übungen, keine Tutorien und keine
Bonuspunkte.


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

**Datum**: Donnerstag, der 10.09.2015 von 11:00-13:00 Uhr (Quelle: Wurde in der Vorlesung vom 22.04.2015 gesagt)<br/>
**Ort**: <a href="http://www.kithub.de/map/2287">Gerthsen-Hörsal</a><br/>
**Punkte**: 90<br/>
**Zeit**: 90 min<br/>
**Punkteverteilung**: ?<br/>

<ul>
    <li>ab 60.5: 1.7</li>
</ul>

**Bestehensgrenze**: ?<br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Ergebnisse**: Am 30.09.2015 war die (vorläufige) Note im Notenauszug<br/>
**Einsicht**: Montag 12.10.2015,  9:00-15:00 Uhr im <a href="https://www.kithub.de/map/2577">Geb. 50.21</a>, Raum 015.1<br/>
**Erlaubte Hilfsmittel**: keine


## Notenverteilung

Wenn ihr mir schreibt was ihr habt, kann ich das updaten:

* 1,3: min 1
* 2,0: min 1