---
layout: post
title: Mustererkennung - Klausur
author: Martin Thoma
date: 2015-04-27 21:15
categories:
- German posts
tags:
- Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Mustererkennung&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://ies.anthropomatik.kit.edu/mitarbeiter.php?person=beyerer">Herrn Prof. Dr.-Ing. Jürgen Beyerer</a> im Sommersemester 2015 gehört. Der Artikel wird bis zur Klausur laufend erweitert.</div>

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

Einleitendes Kapitel welches erklärt, was Klassifikation ist.

* Beispiele für Klassifikation: Blumen/Schmetterlinge in Arten; Schrauben in Schraubentypen; Schüttgut in Mineralien, Pflanzen, Glasscheiben, Diamante, ...
* Formalismen
  * Domäne $\Omega \subseteq $ Welt, Elemente der Domäne heißen Objekte, Objekte werden in paarweise disjunkte Äquivalenzklassen $\omega_i$ gruppiert, sodass jedes Objekt genau eine Äquivalenzklasse hat.
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

#### ME-Kap2_V84.pdf

In diesem Foliensatz geht es um Merkmale und ihre Eigenschaften.

<table border="1">
    <tr>
        <th rowspan="3">&nbsp;</th>
        <th colspan="5">Skala</th>
    </tr>
    <tr>
        <th colspan="2">qualitativ</th>
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


## Material und Links

* [Vorlesungswebsite](http://ies.anthropomatik.kit.edu/lehre_mustererkennung.php): Ist passwortgeschützt. Das Passwort (das ausnahmsweise mal nicht zu erraten ist) kann ich hier natürlich nicht schreiben. Aber der Benutzername ist `asbstudent`.


## Übungsbetrieb

Es gibt keine Übungsblätter, keine Übungen, keine Tutorien und keine
Bonuspunkte.


## Termine und Klausurablauf

**Datum**: Donnerstag, der 10.09.2015 von 11:00-13:00 Uhr (Quelle: Wurde in der Vorlesung vom 22.04.2015 gesagt)<br/>
**Ort**: <a href="http://www.kithub.de/map/2287">Gerthsen-Hörsal</a><br/>
**Punkte**: ?<br/>
**Punkteverteilung**: ?<br/>
**Bestehensgrenze**: ?<br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Ergebnisse**: ?<br/>
**Einsicht**: ?<br/>
**Erlaubte Hilfsmittel**: ?
