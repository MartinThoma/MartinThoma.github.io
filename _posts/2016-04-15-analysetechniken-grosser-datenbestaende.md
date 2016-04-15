---
layout: post
title: Analysetechniken für große Datenbestände - Klausur
author: Martin Thoma
date: 2016-04-15 11:22
categories:
- German posts
tags:
- Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Analysetechniken für große Datenbestände&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="https://dbis.ipd.kit.edu/english/336.php">Herrn Prof. Dr.-Ing. Klemens Böhm</a> im Wintersemester 2015/2016 gehört. Der Artikel ist noch am Entstehen.</div>

## Behandelter Stoff

### Übersicht

<table>
<tr>
    <th>Datum</th>
    <th>Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
    <td>20.10.2015, 08:00</td>
    <td>Einleitung (Folie 1-26)</td>
    <td>Overfitting, Entscheidungsbäume, 1-Rules (→ Decision Strump), Outliers<br/>
        Mengenwertige Attribute, Kategorische Attribute, Zeitreihen<br/>
        Clustering<br/>
        Market Basket Analysis: Zusammenhang zwischen Waren<br/>
        Association rules (A priory Algorithmus)
    </td>
</tr>
<tr>
    <td>20.10.2015, 11:30</td>
    <td>Einleitung, Statistische Tests (Folie 27 - 43)</td>
    <td>Predictive Maintenance
    </td>
</tr>
<tr>
    <td>27.10.2015, 08:00</td>
    <td>Statistische Tests (Folie 38 - )</td>
    <td>$\chi^2$-Test, $\chi^2 = \sum_{i=1}^{m_1} \sum_{j=1}^{m_2} \frac{(h_{ij}- e_{ij})^2}{e_{ij}}$ mit erwartetem Wert $e$ (Sind zwei Zufallsvariablen unabhängig)<br/>
    Kolmogorov-Smirnov-Test (Sind 2 Verteilungen unabhängig; bei kontinuierlichen Zufallsvariablen)<br/>
    Wilcoxon-Wann-Whitney Test<br/>
    Bernoulli-Experiment (Folie 53?)<br/>
    Datenreduktion (Attribute entfernen, z.B. PCA; Datensätze entfernen, z.B. Clustering; Attributsgenauigkeit reduzieren)<br/>
    Diskretisierung: Zielfunktion ist Information Gain. Dieser soll minimiert werden.
    </td>
</tr>
<tr>
    <td>03.11.2015, 08:00</td>
    <td>Räumliche Indexstrukturen</td>
    <td>Widerholung der Statistischen Tests</td>
</tr>
<tr>
    <td>03.11.2015, 11:30</td>
    <td>Entscheidungsbäume, Evaluation (1-18)</td>
    <td>Split-Attribute, Pruning; Loss-Funktionen</td>
</tr>
<tr>
    <td>17.11.2015, 08:00</td>
    <td>Evaluation (19-47)</td>
    <td>Qulitätsmaße (Korrelationskoeffizient)</td>
</tr>
<tr>
    <td>17.11.2015, 11:30</td>
    <td>Evaluation, Association Rules (1-26)</td>
    <td>Association Rules, Frequent Itemset, Apriori-Algorithmus</td>
</tr>
<tr>
    <td>24.11.2015, 08:00</td>
    <td>Association Rules (12-TODO)</td>
    <td>Apriori-Algorithmus, Hash-Tree, Multidimensionale Association Rules</td>
</tr>
<tr>
    <td>08.12.2015, 08:00</td>
    <td>R-Übung</td>
    <td>-</td>
</tr>
<tr>
    <td>26.01.2016, 08:00</td>
    <td>Übung</td>
    <td>-</td>
</tr>
</table>


### Einleitung

Slides: `1-Einleitung.pdf`

* 3 Aufgabentypen: Klassifikation, Clustering und finden von [Association Rules](https://de.wikipedia.org/wiki/Assoziationsanalyse)


<dl>
  <dt><a href="https://en.wikipedia.org/wiki/Decision_stump"><dfn>1-Rule</dfn></a> (<dfn>Decision stump</dfn>)</dt>
  <dd>1-Rules ist ein Klassifikationsverfahren. Jedes Attribut wird für sich
      betrachtet. Es wird anhand von dem Attribut gesplittet, bei dem die
      Fehlerquote am geringsten ist.</dd>
  <dt><dfn>Clustering</dfn></dt>
  <dd>Suchen von Punkten, die nahe bei einander liegen.

      Unterschiede:

      <ul>
          <li>Attribute: Abstandsmaße</li>
          <li>Form</li>
          <li>Dichte</li>
          <li>Größe</li>
          <li>Zeitlicher Aspekt: Alte Daten weniger wichtig</li>
          <li>Alternate Clustering</li>
      </ul>
  </dd>
  <dt><dfn>Association Rules</dfn></dt>
  <dd>z.B. in Market Basket Analysis. Frequent item sets

      A priori Algorithmus zum finden von Association Rules. TODO
  </dd>
  <dt><dfn>Predictive Maintenance</dfn></dt>
  <dd>Ziel: Für Motoren will man vorhersagen, wann diese einen Fehler aufweisen
      und damit gewartet werden müssen.

      Dabei gibt es zwei Fehlerarten, die unterschiedliche hohe Kosten
      aufweisen:
      <ul>
          <li>Ausfall wird vorhergesagt, tritt aber nicht ein: Unnötige Wartung</li>
          <li>Ausfall wird nicht vorhergesagt, tritt aber ein: Teurer Ausfall</li>
      </ul>
  </dd>

  <dt><dfn>Subspace Search</dfn></dt>
  <dd>TODO</dd>

  <dt><dfn>Change detection</dfn></dt>
  <dd>TODO</dd>
</dl>


### Statistische Grundlagen

Slides: `2-statistGrundlagen.pdf`

<dl>
    <dt><dfn>Kennzahlen für Daten</dfn></dt>
    <dd>
        <ul>
            <li>Median / Mean</li>
            <li>Min / Max</li>
            <li>Quantile</li>
            <li>Varianz / Streuung</li>
            <li>Outlier</li>
        </ul>
    </dd>
    <dt><dfn>Aggregatfunktion</dfn></dt>
    <dd>Eine Funktion, welche als Eingabe eine Menge von Werten erwartet und
        einen Wert ausgibt (z.B. SUM, COUNT, MIN, MAX, AVG, MEAN,
        häufigster Wert, Truncated Average, mid range).

        Aggregatfunktionen sind entweder <strong>distributiv</strong>,
        <strong>algebraisch</strong> oder <strong>holistisch</strong>.
    </dd>
    <dt><dfn>Distributive Aggregatfunktion</dfn></dt>
    <dd>
        Es gibt eine Funktion \(G\), so dass
        \[F(\{X_{i,j}\}) = G(\{F(X_{i,j} | i=1, \dots, l) | j = 1, \dots, J\})\]

        MIN, MAX und COUNT sind distributive Aggregatfunktionen.
    </dd>
    <dt><dfn>Algebraische Aggregatfunktion</dfn></dt>
    <dd>Es gibt eine Funktion \(G\), die ein \(M\)-Tupel liefert und \(H\),
        so dass
        \[F(\{X_{i,j}\}) = H(\{G(\{X_{i,j} | i=1, \dots, l\}) | j=1, \dots, J\})\]

        AVG ist eine Algebraische Aggregatfunktion. Hier berechnet \(G\) die
        Summe und gibt zusätzlich die Anzahl der Werte zurück. \(H\) summiert
        die Summen auf und teilt das Ergebnis durch die Gesamtzahl.

        Weitere: Truncated Average</dd>
    <dt><dfn>Holistische Aggregatfunktion</dfn></dt>
    <dd>Man kann keine Beschränkung des Speicherbedarfs für Sub-Aggregate,
        d.h. Aggregate über \(\{X_{i,j}| i=1, \dots, l\}\), angeben.

        Der häufigste Wert und der Median sind holistische Aggregatfunktionen.</dd>
    <dt><dfn>Self-Maintainable Aggregatfunktion</dfn></dt>
    <dd>Wenn man den aktuellen Wert der Aggregatfunktion kennt und man löscht
        einen Wert bzw. fügt einen Wert ein, dann kann man direkt den neuen
        Wert der Aggregatfunktion über den angepassten Datenbestand berechnen.

        Nicht-self-maintainable ist der häufigste Wert.

        MIN und MAX ist self-maintainable bzgl. Einfügen.</dd>
    <dt><dfn>Mid-Range</dfn></dt>
    <dd>\[\frac{MAX-MIN}{2}\]</dd>
    <dt><dfn>Entropie</dfn></dt>
    <dd>\[E(S) = - \sum_{j} p_j \cdot \log p_j\]

        \(E(S)=0\) ist minimal, wenn es ein \(j\) gibt mit \(p_j = 1\).
        \(E(S)=\log(n)\) ist maximal, wenn \(p_i = p_j\) gilt für \(i, j\).</dd>
    <dt><dfn>Korrelationsmaße</dfn></dt>
    <dd>Sind üblicherweise auf [-1, 1] normiert. Die Kovarianz ist ein
        nicht-normiertes Korrelationsmaß.</dd>
    <dt><dfn>PCA</dfn> (<dfn>Principal Component Analysis</dfn>)</dt>
    <dd>TODO</dd>
    <dt><dfn>Chi-Quadrat-Test</dfn></dt>
    <dd>Oberbegriff für mehrere Tests; hier nur der Unabhängigkeitstest.

        Gegeben sind zwei Verteilungen. Die Frage ist, ob sie unabhängig sind.

        \[\chi^2 = \sum_{i=1}^{m_1} \sum_{j=1}^{m_2} \frac{(n_{ij} - e_{ij})^2}{e_{ij}}\]

        Daraus wird ein \(p\)-Wert abgeleitet. Wenn dieser unter einem
        Schwellwert wie \(\alpha = 0.01\) ist, dann wird die Hypothese, dass
        die Verteilungen unabhängig sind, zurückgewiesen.</dd>
    <dt><dfn>Kolmogorov-Smirnov-Test</dfn></dt>
    <dd>Test auf unabhängigkeit kontinuierlicher Verteilungen</dd>
</dl>

Weitere

<ul>
    <li>Boxplots: Whiskers</li>
    <li>Histogramme</li>
    <li>Wahrscheinlichkeitsraum, Ereignis, Ergebnis, Ergebnismenge \(\Omega\),
        Wahrscheinlichkeitsmaß, Kovarianzmatrix, Bernoulli-Experiment</li>
</ul>

Siehe auch:

* [Arten von Merkmalen](https://martin-thoma.com/mustererkennung-klausur/#me-kap2v84pdf)


### Räumliche Indexstrutkuren

Slides: `3-Informatik-Grundlagen.pdf`

TODO


### Klassifikation mit Entscheidungsbäumen

Slides: `4-Entscheidungsbaeume.pdf`

<dl>
    <dt><dfn>Qualitätskriterien für Entscheidungsbäume</dfn></dt>
    <dd>

        <ul>
            <li>Ergebnisqualität</li>
            <li>Kompaktheit: Je kompakter der Baum, desto besser kann die
                Entscheidung vom Benutzer nachempfunden werden.</li>
        </ul>

    </dd>
    <dt><dfn>Wahl der Split-Attribute</dfn></dt>
    <dd>Entropie eines Splits minimieren:

    \[E(S_1, S_2) = \frac{n_1}{n} E(S_1) + \frac{n_2}{n} E(S_2)\]

    </dd>
    <dt><dfn>Overfitting</dfn></dt>
    <dd>Entscheidungsbaum ist zu sehr an Trainingsdatenbestand angepasst</dd>
    <dt><dfn>Prepruning</dfn> (<dfn>Forward pruning</dfn>)</dt>
    <dd>Schon beim Erstellen des Entscheidungsbaumes wird ab einer gewissen
        Tiefe abgebrochen</dd>
    <dt><dfn>Postpruning</dfn> (<dfn>Backward pruning</dfn>)</dt>
    <dd>Der Entscheidungsbaum wird komplett aufgebaut, aber dannach wird
        greprunt.</dd>
</dl>


### Evaluation

Slides: `5-Evaluation.pdf`

<dl>
    <dt><dfn>Resubsitution Error</dfn></dt>
    <dd>Trainingsfehler</dd>
    <dt><dfn>Cross-Validation</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Stratification</dfn></dt>
    <dd>Sicherstellen, dass bestimmte Eigenschaften (z.B. Klassenzugehörigkeit) in Partitiionen etwa gleich verteilt ist.</dd>
    <dt><dfn>Loss function</dfn></dt>
    <dd>Eine Funktion, die angibt, wie viel man durch eine unkorrekte
        Vorhersage verliert.</dd>
    <dt><dfn>Informational Loss function</dfn></dt>
    <dd>\[- \log_2 p_i\] - Wahrscheinlichkeiten der nicht-eintretenden Klassen spielen keine Rolle</dd>
    <dt><dfn>Quadratic Loss function</dfn></dt>
    <dd>\[\sum_{j} (p_j - a_j)^2\] mit tatsächlichem Label \(a_j \in \{0,1\}\)
        und geschätzter Wahrscheinlichkeit \(p_j\) für die Klasse \(j\).</dd>
    <dt><dfn>Bias</dfn></dt>
    <dd>Das Verfahren an sich funktioniert nicht gut. Selbst beliebig viele
        Trainingsdaten beheben dieses Problem nicht. Der Fehler ist
        inhärent im Verfahren verankert.</dd>
    <dt><dfn>Varianz</dfn></dt>
    <dd>Fehler welcher durch das Fehlen von Trainingsdaten verursacht wird.</dd>
    <dt><dfn>Gesamt-Erfolgsquote</dfn></dt>
    <dd>\[\frac{TP+TN}{TP+TN+FP+FN}\]</dd>
    <dt><dfn>Kappa-Koeffizient</dfn></dt>
    <dd>Vergleich mit Klassifier, der nur den Anteil der Klassenzugehörigkeit
        schätzt.</dd>
    <dt><dfn>Lift-Faktor</dfn></dt>
    <dd>Faktor, um den sich die Rücklaufquote erhöht.</dd>
    <dt><dfn>ROC</dfn> (<dfn>Receiver Operator Characteristic</dfn>)</dt>
    <dd>x-Achse: \(\frac{FP}{FP+TN} \cdot 100\) (FP-Rate),<br/>
        y-Achse: \(\frac{TP}{TP+FN} \cdot 100\) (TP-Rate)</dd>
    <dt><dfn>Precision</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Recall</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Correlation Coefficient</dfn></dt>
    <dd>Der Correlation Coefficient ist kein Fehlermaß. Der
        \(CC(p, a)\) ist groß, wenn sich \(p\) und \(a\) ähnlich sind.

        \[CC(p, a) = \frac{COV(p, a)}{\sigma(p) \cdot \sigma(a)}\]

        Mit \(\sigma(x) = \frac{1}{n-1} \cdot \sum_{i} (x_i - \bar{x})^2\)</dd>
    <dt><dfn>Code</dfn></dt>
    <dd>Abbildung, die jedem Element des Alphabets eine Folge aus 0en und
        1en zuweist.

        Beispiele:

        <ul>
            <li>Morse-Code</li>
            <li>Unicode</li>
            <li>Ascii-Code</li>
        </ul></dd>
    <dt><dfn>Minimum Description Length</dfn> (<dfn>MDL</dfn>)</dt>
    <dd>TODO</dd>
</dl>

Weiteres:

* Qualitätsmaße für numerische Vorhersagen


### Association Rules

<dl>
    <dt><dfn>Frequent Itemset</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Association rules</dfn></dt>
    <dd>Drücken aus wie Phänomene zueinander in Beziehung stehen.</dd>
    <dt><dfn>Support</dfn></dt>
    <dd>Anzahl der Transaktionen, die das Itemset I unterhalten wird Support von I genannt.</dd>
    <dt><dfn>Closedness</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Support</dfn></dt>
    <dd>Der Support(A \cup B) ist die Anzahl der Mengen, die \(A \cup B\) enthalten.</dd>
    <dt><dfn>Confidence</dfn></dt>
    <dd>Confidence von \(A \Rightarrow B\) ist \(\frac{Support(A \cup B)}{support(A)}\)</dd>
    <dt><dfn>Apriori Algorithmus</dfn></dt>
    <dd>

        <ol>
            <li>Erzeuge alle einelementigen Frequent Itemsets</li>
            <li>for k in range(2, n): Erzeuge die k-Elementigen frequent Itemsets (join, prune, support counting)</li>
            <li>Frequent itemsets: Association Rules</li>
        </ol>

        Der Algorithmus nutzt aus, dass eine notwendige Bedingung für k-Elementige
        Frequent Itemsets ist, dass alle k-1-elementigen Frequent Itemsets auch
        Frequent sein müssen.
    </dd>
</dl>


### Prüfungsfragen

* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule hohen Support und hohe Confidence hat?
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule hohen Support und geringe Confidence hat?
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule geringen Support und hohe Confidence hat?
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule geringen Support und geringe Confidence hat?
* Im Apriori-Algorithmus hat man bei k=2 keinen Prune-Schritt. Warum? (Antwort: 24.11.2015, 14:34)

### Übungen

Kommt noch.

## Material und Links

Die Vorlesung wurde gestreamt und ist unter
[mml-streamdb01.ira.uka.de](http://mml-streamdb01.ira.uka.de/) verfügbar.

* [Vorlesungswebsite](https://dbis.ipd.kit.edu/2261.php)
* [Ilias](https://ilias.studium.kit.edu/goto_produktiv_crs_477914.html)


## Übungsbetrieb

?


## Vorlesungsempfehlungen

Folgende Vorlesungen sind ähnlich:

* [Mustererkennung](https://martin-thoma.com/mustererkennung-klausur/)
* [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/)
* [Machine Learning 2](https://martin-thoma.com/machine-learning-2-course/)
* [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)


## Termine und Klausurablauf

Es ist noch nicht klar, ob es eine mündliche oder eine schriftliche Prüfung
wird.

Falls es mündlich ist, soll es mindestens einen Termin pro Monat geben.

**Datum**: Noch nicht bekannt (Stand: 09.11.2015)<br/>
**Ort**: Noch nicht bekannt (Stand: 09.11.2015)<br/>
**Punkte**: ?<br/>
**Zeit**: ?<br/>
**Punkteverteilung**: ?<br/>
**Bestehensgrenze**: ?<br/>
**Übungsschein**: ?<br/>
**Bonuspunkte**: ?<br/>
**Ergebnisse**: ?<br/>
**Einsicht**: Noch nicht bekannt (Stand: 09.11.2015)<br/>
**Erlaubte Hilfsmittel**: keine
