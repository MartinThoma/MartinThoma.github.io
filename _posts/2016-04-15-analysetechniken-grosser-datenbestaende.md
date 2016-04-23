---
layout: post
title: Analysetechniken für große Datenbestände
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
        Association rules (Apriori Algorithmus)
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
    <td>\(\chi^2\)-Test, \(\chi^2 = \sum_{i=1}^{m_1} \sum_{j=1}^{m_2} \frac{(h_{ij}- e_{ij})^2}{e_{ij}}\) mit erwartetem Wert \(e\) (Sind zwei Zufallsvariablen unabhängig)<br/>
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
    <td>41 min Evaluation, dann Association Rules. Frequent Itemset, Apriori-Algorithmus</td>
</tr>
<tr>
    <td>24.11.2015, 08:00</td>
    <td>Kapitel 6: Association Rules (12-Ende), Kapitel 7 (1-12)</td>
    <td>Apriori-Algorithmus, Hash-Tree, Multidimensionale Association Rules,
        Level-Crossing-Association Rules, FP-Trees</td>
</tr>
<tr>
    <td>01.12.2015, 08:00</td>
    <td>Kapitel 7, Kapitel 8 (Pattern Mining mit Constraints)</td>
    <td>Korrekturen zu Kapitel "Evaluation"; Wiederholung von Apriori-Algorithmus und Hash-Filter; ab Minute 27 FP-Trees</td>
</tr>
<tr>
    <td>01.12.2015, 11:30</td>
    <td>Kapitel 8 (Pattern Mining mit Constraints), Kapitel 9 (Clustering)</td>
    <td>Meta-Rule-Guided Mining, Anti-Monotonizität, Support-basiertes Pruning, Constrained Sequences, Clustering Criterion Function</td>
</tr>
<tr>
    <td>15.12.2015, 08:00</td>
    <td>Kapitel 9 (Clustering)</td>
    <td>k-means; CF-Trees</td>
</tr>
<tr>
    <td>15.12.2015, 11:30</td>
    <td>Kapitel 9 (Clustering)</td>
    <td>CF-Trees; Hierarchisches Clustern mit Minimum Spanning Tree; DIANA; Hochdimensionale Merkmalsräume</td>
</tr>
<tr>
    <td>08.12.2015, 08:00</td>
    <td>R-Übung</td>
    <td>-</td>
</tr>
<tr>
    <td>19.01.2016, 08:00</td>
    <td>Kapitel 9</td>
    <td>Jaccard Koeffizient, ...</td>
</tr>
<tr>
    <td>19.01.2016, 11:30</td>
    <td>Kapitel 9; Kapitel 10 (1 - )</td>
    <td>EM-Algorithmus; Generative Modelle</td>
</tr>
<tr>
    <td>26.01.2016, 08:00</td>
    <td>Übung</td>
    <td>-</td>
</tr>
<tr>
    <td>26.01.2016, 11:30</td>
    <td>Kapitel 10</td>
    <td>Regression</td>
</tr>
<tr>
    <td>02.02.2016, 08:00</td>
    <td>Kapitel 10</td>
    <td>Logistische Regression, Cross Entropy</td>
</tr>
</table>


### Einleitung

Slides: `1-Einleitung.pdf`

<dl>
  <dt><dfn>Aufgabentypen</dfn></dt>
  <dd><ul>
      <li>Klassifikation</li>
      <li>Clustering</li>
      <li>Finden von <a href="https://de.wikipedia.org/wiki/Assoziationsanalyse">Association Rules</a></li>
  </ul></dd>
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
  <dd>Association Rules sind Regeln der Form:
      Wenn eine Transaktion A enthält, dann auch B (formal: \(A \Rightarrow B\)).

      Association rules werden z.B. in der Market Basket Analysis eingesetzt.
      Sie können aus Frequent item sets relativ einfach erzeugt werden.

      Der Apriori Algorithmus dient dem Finden von Association Rules.
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
  <dt><dfn>Change detection</dfn></dt>
  <dd>Erkennung wesentlicher Veränderungen in einer Zeitreihe.</dd>
</dl>


### Statistische Grundlagen

Slides: `2-statistGrundlagen.pdf`

<dl>
    <dt><dfn>Skalen</dfn></dt>
    <dd>Siehe <a href="https://martin-thoma.com/mustererkennung-klausur/#merkmale">Mustererkennung</a></dd>
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
    <dt><dfn>Metrische Daten</dfn></dt>
    <dd>Ein Metrischer Raum ist eine Menge \(M\) mit einer Funktion
        \(d: M \times M \rightarrow \mathbb{R}_0^+\) für die gilt:

        <ul>
            <li>Symmetrie: \(\forall p,q \in M: d(p, q) = d(q, p) \)</li>
            <li>Definitheit: \(\forall p,q \in M: d(p, q) = 0 \Leftrightarrow p = q\)</li>
            <li>Dreiecksungleichung: \(\forall p,q,r \in M: d(p, r) \leq d(p,q) + d(q, r)\)</li>
        </ul>

    </dd>
    <dt><dfn>Aggregatfunktion</dfn></dt>
    <dd>Eine Funktion, welche als Eingabe eine Menge von Werten erwartet und
        einen Wert ausgibt (z.B. SUM, COUNT, MIN, MAX, AVG, MEAN,
        häufigster Wert, Truncated Average, mid range).<br/>
        <br/>
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
        die Summen auf und teilt das Ergebnis durch die Gesamtzahl.<br/>
        <br/>
        Weitere: Truncated Average</dd>
    <dt><dfn>Holistische Aggregatfunktion</dfn></dt>
    <dd>Man kann keine Beschränkung des Speicherbedarfs für Sub-Aggregate,
        d.h. Aggregate über \(\{X_{i,j}| i=1, \dots, l\}\), angeben.<br/>
        <br/>
        Der häufigste Wert und der Median sind holistische Aggregatfunktionen.</dd>
    <dt><dfn>Self-Maintainable Aggregatfunktion</dfn></dt>
    <dd>Wenn man den aktuellen Wert der Aggregatfunktion kennt und man löscht
        einen Wert bzw. fügt einen Wert ein, dann kann man direkt den neuen
        Wert der Aggregatfunktion über den angepassten Datenbestand berechnen.<br/>
        <br/>
        Nicht-self-maintainable ist der häufigste Wert.<br/>
        <br/>
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
    <dt><a href="https://de.wikipedia.org/wiki/Kovarianz_(Stochastik)#Definition"><dfn>Kovarianz</dfn></a></dt>
    <dd>\[\operatorname{Cov}(X,Y) := \operatorname E\bigl[(X - \operatorname E(X)) \cdot (Y - \operatorname E(Y))\bigr]\]</dd>
    <dt><a name="korrelationskoeffizient" href="https://de.wikipedia.org/wiki/Korrelationskoeffizient#Definitionen"><dfn>Korrelationskoeffizient</dfn></a></dt>
    <dd>\[\varrho(X,Y) =\frac{\operatorname{Cov}(X,Y)}{\sigma(X)\sigma(Y)} \in [-1, 1]\]</dd>
    <dt><dfn>PCA</dfn> (<dfn>Principal Component Analysis</dfn>)</dt>
    <dd>TODO (vgl. <a href="https://martin-thoma.com/neuronale-netze-vorlesung/#pca">Neuronale Netze</a>)</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Chi-Quadrat-Test#Unabh.C3.A4ngigkeitstest"><dfn>Chi-Quadrat-Test</dfn></a></dt>
    <dd>Oberbegriff für mehrere Tests; hier nur der Unabhängigkeitstest.<br/>
        <br/>
        Gegeben sind zwei Verteilungen von Zufallsvariablen \(X, Y\). Die Frage
        ist, ob sie unabhängig sind.<br/>
        Dazu zählt man die Ausprägungen \(i=1, \dots, m_1\) des Merkmals \(X\)
        und die Ausprägungen \(j=1, \dots, m_2\) des Merkmals \(Y\) sowie
        wie häufig diese in Kombination auftreten (\(n_{ij}\)). Man schätzt den
        erwarteten Wert durch \(e_{ij} = \frac{1}{n} \left(\sum_{k=1}^{m_2} n_{ik} \right) \cdot \left (\sum_{k=1}^{m_2} n_{kj}\right )\). Der Chi-Quadrat wert ist dann:

        \[\chi^2 = \sum_{i=1}^{m_1} \sum_{j=1}^{m_2} \frac{(n_{ij} - e_{ij})^2}{e_{ij}}\]

        Daraus wird ein \(p\)-Wert abgeleitet. Wenn dieser unter einem
        Schwellwert wie \(\alpha = 0.01\) ist, dann wird die Hypothese, dass
        die Verteilungen unabhängig sind, zurückgewiesen.

        Die Nullhypothese, dass \(X, Y\) unabhängig sind wird auf dem
        Signifikanzniveau \(\alpha\) verworfen, falls

        \[\chi^2 > \chi^2_{(1-\alpha; (m_1-1)(m_2-1))}\]

        </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Kolmogorow-Smirnow-Test"><dfn>Kolmogorow-Smirnow-Test</dfn></a> (<dfn>KSA-Test</dfn>)</dt>
    <dd>Test auf unabhängigkeit kontinuierlicher Verteilungen, also:
        \[H_0: F_X(x) = F_0(x)\]

        Es wird die empirsche Verteilungsfunktion \(S\) gebildet und diese mit
        der hypothetischen Verteilungsfunktion \(F_0\) verglichen, wobei
        \(S(x_0) = 0\) gesetzt wird:
        \[d_{\max} = \max(\max_{i=1, \dots, n}|S(x_i) - F_0(x_i)|, \max_{i=1, \dots, n} |S(x_{i-1} - F_0(x_i))|)\]
        \(H_0\) wird verworfen, wenn \(d_{\max} > d_\alpha\), wobei \(d_\alpha\)
        bis zu \(n=35\) tabelliert vorliegt. Bei großerem \(n\) kann
        näherungsweise
        \[d_\alpha = \sqrt{\frac{-\frac{1}{2} \ln(\frac{\alpha}{2})}{n}}\]
        </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Wilcoxon-Mann-Whitney-Test"><dfn>Wilcoxon-Mann-Whitney-Test</dfn></a> (\(U\)-Test)</dt>
    <dd>Es seien \(X,Y\) Zufallsvariablen mit Verteilungsfunktionen
        \(F_X(x) = F_Y(x-a)\) für ein \(a \in \mathbb{R}\).<br/>
        <br/>
        \(H_0: a = 0\) vs \(H_1: a \neq 0\)<br/>
        Vorgehen: Gemeinsame Stichprobe sortieren, Rangsumme für \(X\) und \(Y\)
        bilden, Betrag der Differenz mit Tabelleneintrag vergleichen.
    </dd>
    <dt><dfn>Datenreduktion</dfn></dt>
    <dd>

        <ul>
            <li>Numerosity Reduction: Reduziere die Anzahl der betrachteten
                Datenobjekte
            <ul>
                <li>Parametrische Verfahren: Nehme eine bekannte
                    Wahrscheinlichkeitsverteilung der Datenobjekte an und
                    schätze deren Paramter. Arbeite  dann nur mit der
                    Verteilung</li>
                <li>Nichtparametrische Verfahren: Sampling, Clustering,
                    Histogramme</li>
            </ul>
            </li>
            <li>Dimensionality Reduction: Reduziere die Anzahl der Attribute.

            <ul>
                <li>Forward Feature Construction: Starte nur mit einem Feature
                    und gebe dem Classifier so lange neue Features, bis die
                    gewünschte Genauigkeit erreicht wurde.</li>
                <li>Feature Elimination: Starte mit allen Features und
                    entferne so lange Features, wie die gewünschte Genauigkeit
                    erhalten bleibt.</li>
                <li>PCA</li>
            </ul>
            </li>
            <li>Diskretisierung: Reduziere die Werte pro Attribut.</li>
        </ul>

    </dd>
</dl>

Weitere

<ul>
    <li>Boxplots: Whiskers</li>
    <li>Histogramme: Nicht geeignet für viele Dimensionen.</li>
    <li>Wahrscheinlichkeitsraum, Ereignis, Ergebnis, Ergebnismenge \(\Omega\),
        Wahrscheinlichkeitsmaß, Kovarianzmatrix, Bernoulli-Experiment</li>
</ul>


### Räumliche Indexstrutkuren

Slides: `3-Informatik-Grundlagen.pdf`

<dl>
    <dt><dfn>B<sup>+</sup>-Tree</dfn> (see <a href="https://www.youtube.com/watch?v=CYKRMz8yzVU">YouTube</a>)</dt>
    <dd>A balanced search tree.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Datenbankindex"><dfn>Index</dfn></a></dt>
    <dd>Beschleunigung der Suche von linearer Suchzeit auf logarithmische
        durch <a href="https://de.wikipedia.org/wiki/B%2B-Baum">B<sup>+</sup>-Bäume</a>.</dd>
    <dt><dfn>Anfragetypen</dfn></dt>
    <dd>

        <ul>
            <li>Punkt-Anfragen: Ist ein Punkt im Datensatz?</li>
            <li>Bereichs-Anfragen: Ist mindestens ein Datenobjekt im gegebenen Bereich?</li>
            <li>Nearest-Neighbor-Anfragen (NN-Anfragen): Was ist das nächste Datenobjekt zu einem gegebenen Punkt?</li>
        </ul>

    </dd>
    <dt><dfn>kD-Baum</dfn></dt>
    <dd>Siehe <a href="https://martin-thoma.com/cg-klausur/#kd-tree">Computergrafik</a>.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/K-D-B-tree"><dfn>kDB-Baum</dfn></a></dt>
    <dd>Kombination aus heterogenem k-d-Baum und B*-Baum<br/>
        TODO</dd>
    <dt><dfn>R-Baum</dfn></dt>
    <dd>TODO: <a href="http://cs.stackexchange.com/q/56337/2914">What is the difference between a R-tree and a BVH?</a></dd>
</dl>


### Entscheidungsbäume

Slides: `4-Entscheidungsbaeume.pdf`

Dieses Kapitel beschäftigt sich mit der Klassifikation mit Entscheidungsbäumen.

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
    <dt><a name="cross-validation"></a><dfn>\(k\)-Fold Cross-Validation</dfn> (<dfn>Kreuzvalidierung</dfn>)</dt>
    <dd>Unterteile den Datensatz in \(k\) Teile. Dabei sollten die Klassen in
        etwa gleich häufig in allen Teilen vorkommen.

        Mache nun \(k\) durchläufe, wobei der \(k\)-te Datensatz immer zum
        Testen und alle anderen zum Trainieren verwendet werden. Berechne die
        \(k\) Testfehler. Mittle diese am Ende. Das ist ein besserer Schätzwert
        für den realen Fehler als eine einmalige Unterteilung in Training- und
        Testmenge.</dd>
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
    <dt><a name="erfolgsquote"></a><dfn>Gesamt-Erfolgsquote</dfn></dt>
    <dd>\[\frac{TP+TN}{TP+TN+FP+FN}\]</dd>
    <dt><dfn>Konfusionsmatrix</dfn> (<dfn>Confusion matrix</dfn>)</dt>
    <dd>Eine Tabelle, in der jede Zeile für die tatsächlichen Klassen stehen
        und die Spalten für die vorhergesagten Klassen. Die Diagonalelemente
        zählen also die richtig vorhergesagten Datenobjekte; alle anderen
        Zellen zählen falsche Vorhersagen.</dd>
    <dt><dfn>Kappa-Koeffizient</dfn></dt>
    <dd>Vergleich mit Klassifier, der nur den Anteil der Klassenzugehörigkeit
        schätzt.<br/>
        Sei \(D\) die Menge der Datenobjekte, \(K\) die Menge der Klassen,
        \(f: D \rightarrow K\) der Klassifizierer und \(k:D \rightarrow K\) die tatsächliche Klasse des Datenobjekts. Dann gilt:
        \[\kappa(f, D) = \frac{TODO - }{|D|-|\{1|d \in D, f(d) = k(d)\}|}\]
        Der Wertebereich ist also: TODO</dd>
    <dt><dfn>Lift-Faktor</dfn></dt>
    <dd>Faktor, um den sich die Rücklaufquote erhöht.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Receiver_operating_characteristic"><dfn>ROC</dfn></a> (<dfn>Receiver Operator Characteristic</dfn>)</dt>
    <dd>x-Achse: \(\frac{FP}{FP+TN} \cdot 100\) (FP-Rate),<br/>
        y-Achse: \(\frac{TP}{TP+FN} \cdot 100\) (TP-Rate)

        Siehe auch: <a href="https://www.reddit.com/r/answers/comments/4g2wgx/where_does_the_name_receiver_operating/">Namensherkunft</a></dd>
    <dt><dfn>Recall</dfn> (<dfn>True Positive Rate</dfn>, <dfn>TPR</dfn>, <dfn>Sensitivität</dfn>)</dt>
    <dd>\[TPR = \frac{TP}{TP + FN} = 1 - FNR \in [0, 1]\]

        Der Recall gibt den Anteil der erkannten positiven aus allen positiven
        an.

        <i>Sensitivität</i> ist ein in der Medizin üblicher Begriff.</dd>
    <dt><dfn>Precision</dfn> (<dfn>Genauigkeit</dfn>)</dt>
    <dd>\[Precision = \frac{TP}{TP + FP} \in [0, 1]\]

        Die Precision gibt den Anteil der real positiven aus den als positiv
        erkannten an.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/F1_score"><dfn>F-Measure</dfn></a> (<dfn>F1 score</dfn>)</dt>
    <dd>\[\frac{2 \cdot \text{precision} \cdot \text{recall}}{\text{recall} + \text{precision}}\]</dd>
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
    <dd>Minimale Länge zum Beschreiben des Modells.</dd>
</dl>

Weiteres:

* Qualitätsmaße für numerische Vorhersagen

Fragen:

* TODO, Folie 23: Wo kommt die 140 her?
* TODO, Folie 27: Lift Faktor ist 2 wenn man nur die 400 anschreibt, oder?


### Association Rules

Slides: `6-Association-Rules-1.pdf` und `7-Association-Rules-2.pdf`

Es zieht sich die Warenkorbanalyse als Beispiel durch. Allerdings sind folgende
Anwendungen von Association Rules denkbar:

* Netflix: Man kennt User und welche Filme diese mögen (5 Sterne). Welche
  weiteren, unbewerteten Filme könnten diesen gefallen?
* Amazon: Im Warenkorb sind Produkte XY. Was wird der User wohl noch kaufen?
* Online-Konfiguratoren: Welche Konfigurationen sollte man "bündeln", z.B. bei
  Autos in eine "Sport-Variante"?
* Last FM: Music Recommendations
* Medicine: [Implementation of Apriori Algorithm in Health Care Sector: A Survey](http://static.ijcsce.org/wp-content/uploads/2013/12/IJCSCE110513.pdf)

<dl>
    <dt><dfn>Frequent Itemset</dfn></dt>
    <dd>Ein Frequent Itemset ist eine Menge von Items, die häufig zusammen
        gekauft werden.</dd>
    <dt><dfn>Transaktion</dfn> (<dfn>Itemset</dfn>)</dt>
    <dd>Menge von Items, die zusammen gekauft wurden.</dd>
    <dt><dfn>Association rules</dfn></dt>
    <dd>Drücken aus wie Phänomene zueinander in Beziehung stehen.

        Beispiel: Wer Bier kauft, der kauft auch Chips.</dd>
    <dt><dfn>Support</dfn></dt>
    <dd>Anzahl der Transaktionen, die das Itemset I unterhalten wird Support von I genannt.<br/>
        Der \(\text{support}(A \cup B)\) ist die Anzahl der Mengen, die \(A \cup B\) enthalten.</dd>
    <dt><dfn>Closed Itemset</dfn></dt>
    <dd>Ein Itemset \(I\) heißt closed, wenn es keine echte Obermenge \(I' \supsetneq I\) gibt,
        die den gleichen support \(\text{supp}(I') = \text{supp}(I)\) hat.</dd>
    <dt><dfn>Confidence</dfn></dt>
    <dd>Confidence von \(A \Rightarrow B\) ist \(\frac{Support(A \cup B)}{support(A)}\)</dd>
    <dt><dfn>Apriori Algorithmus</dfn></dt>
    <dd>Der Apriori-Algorithmus ist ein Generate-and-Test-Algorithmus zum
        Finden von Frequent Itemsets.

        <ol>
            <li>Erzeuge alle einelementigen Frequent Itemsets</li>
            <li>for k in range(2, n): Erzeuge die \(k\)-elementigen frequent
                Itemsets (join, prune, support counting)</li>
            <li>Frequent itemsets: Association Rules</li>
        </ol>

        Der Algorithmus nutzt aus, dass eine notwendige Bedingung für
        \(k\)-elementige Frequent Itemsets ist, dass alle \(k-1\)-elementigen
        Frequent Itemsets auch Frequent sein müssen.

        Verbesserungen:

        <ul>
            <li>Stichproben verwenden (Sampling)</li>
            <li>Aggressiver durch Datenbestand gehen (z.B. von k=3 zu k=6 springen)</li>
            <li>Hashfilter</li>
        </ul>
    </dd>
    <dt><dfn>FP-Trees</dfn></dt>
    <dd>Datenstrutkur zum schnellen Finden von Frequent Itemsets.<br/>
    <br/>
    TODO<br/>
    <br/>
    Jede Transaktion entspricht einem Pfad im FP-Tree.
    Für jedes Item gibt es eine verkettete Liste, die das Vorkommen im Baum
    angibt.<br/>
    <br/>
    Jeder Knoten im Baum ist ein Item und die Häufigkeit des Präfixes.

    <ol>
        <li>Für jedes Item: Zähle in wie vielen Transaktionen das Item vorkommt.</li>
        <li>Sortiere Items in Transaktion absteigend nach Häufigkeit. Bei gleicher Häufigkeit wird z.B. alphabetisch sortiert. Damit ergibt sich eine eindeutige Reihenfolge.</li>
        <li>Sortiere Transaktionen nach den Items innerhalb der Transaktionen.</li>
        <li>Aufbau des FP-Trees
        <ol>
            <li>Aufbau des Baums</li>
            <li>Aufbau der Header-Tabelle</li>
        </ol>
        </li>
    </ol>

    </dd>
    <dt><dfn>Sampling</dfn></dt>
    <dd>Berechnung auf einer Stichprobe durchführen</dd>
    <dt><dfn>Negative Border</dfn></dt>
    <dd>Die negative border ist abhängig vom minimalen geforderten Support.
        Wenn dieser Schwellenwert größer wird, wandert die negative border
        nach oben; es gibt also weniger frequent Itemsets.</dd>
    <dt><dfn>Projected Database</dfn></dt>
    <dd>Zerlegung des Datenbestands in Partitionen (z.B. Transaktionen mit Item A
        und Transaktionen ohne Item A).</dd>
</dl>


Siehe auch:

* [Market Basket Analysis with R](http://www.salemmarafi.com/code/market-basket-analysis-with-r/comment-page-1/)
* [Market Basket Analysis and Recommendation Engines](https://www.knime.org/knime-applications/market-basket-analysis-and-recommendation-engines)

### Constraints

Slides: `8-ConstrainedAssociationRules.pdf`


<dl>
    <dt><dfn>Constraint-Typen</dfn></dt>
    <dd>
        <ul>
            <li>Data Constraints: Einschränken auf konkrete Werte, z.B. Transaktionen bei denen der Ort Karlsruhe ist.</li>
            <li>Rule Constraints: z.B. nur Itemsets der Größe 3</li>
        </ul>
    </dd>
    <dt><dfn>1-var Constraint</dfn></dt>
    <dd>Nur eine Seite (links oder rechts) der Association Rule wird
        eingeschränkt.</dd>
    <dt><dfn>2-var Constraint</dfn></dt>
    <dd>Beide Seiten (links und rechts) der Association Rule werden
        eingeschränkt.</dd>
    <dt><dfn>Anti-Monotonizität</dfn></dt>
    <dd>Ein 1-var Constraint heißt anti-monoton, wenn für alle Mengen \(S, S'\)
        gilt:

        \[(S \supseteq S' \land (S \text{ erfüllt } C )) \Rightarrow S' \text{ erfüllt } C\]

        Wenn also ein Constraint \(C\) für eine Menge \(S\) erfüllt ist, dann
        auch für jede Teilmenge \(S'\).

        Beispiele:
        <ul>
            <li>\(\min(S) \geq v, \;\;\; v \in \mathbb{R}\) ist anti-monoton</li>
            <li>\(\max(s) \geq v, \;\;\; v \in \mathbb{R}\) ist nicht anti-monoton</li>
            <li>\(\text{size}(s) \leq v, \;\;\; v \in \mathbb{N}\) ist anti-monoton</li>
            <li>\(\text{size}(s) \geq v, \;\;\; v \in \mathbb{N}\) ist nicht anti-monoton</li>
        </ul>

        Eine gutartige Eigenschaft von Constraints. Hier kann das
        Constraint sehr früh überprüft werden.</dd>
    <dt><dfn>Succinctness</dfn></dt>
    <dd>Ein Constraint heißt succinct, wenn alle Itemsets die es erfüllen
        schnell erzeugt werden können.

        Beispiel: Man hat das Constraint, dass der Typ "Non-Food" sein soll.
        Aber es gibt nur 3 Produkte die diesen Typ haben.

    Kandidaten, die das Constraint nicht erfüllen werden gar nicht erst
        erzeugt.</dd>
</dl>

* Meta-Rule Guided mining
* Constraint durch schwächeres Anti-Monotones Constraint ersetzen.


### Clustering

Slides: `9-Clustering-1.pdf` und `9-Clustering-2.pdf`

<dl>
    <dt><dfn>Silhouette-Koeffizient</dfn></dt>
    <dd>Sei \(C = (C_1, \dots, C_k)\) ein Clustering.

    <ul>
        <li>Durchschnittlicher Abstand zwischen Objekt o und anderen Objekten in seinem Cluster:
            \[a(o) = \frac{1}{|C(o)|} \sum_{p \in C(o)} dist(o, p)\]</li>
        <li>Durchschnittlicher Abstand zum zweitnächsten Cluster:
            \[b(o) = \min_{C_i \in \text{Cluster} \setminus C(o)}(\frac{1}{C_i}) \sum_{p\in C_i} \sum_{p \in C_i} \text{dist}(o, p)\]</li>
        <li>Silhouette eines Objekts:
            \[s(o) = \begin{cases}0  &\text{if } a(o) = 0, \text{i.e. } |C_i|=1\\
                    \frac{b(o)-a(o)}{\max(a(o), b(o))} &\text{otherwise}\end{cases}\]
            Es gilt:
            \[s(o) \in [-1, 1]\]</li>
        <li>\(\text{silh}(C) = \frac{1}{|C|} \sum_{C_i \in C} \frac{1}{|C_i|} \sum_{o \in C_i} s(o)\).
            Es gilt:
            \[\text{silh}(C) \in [-1; 1]\]
            Es ist ein möglichst großer Wert gewünscht. Alles kleiner als 0 ist schlecht.</li>
    </ul>
    </dd>
    <dt><dfn>Distanzfunktionen für Cluster</dfn></dt>
    <dd>
        <ul>
            <li>Durschnittlicher Objektabstand</li>
            <li>Single Link: Maximaler bzw. Minimaler Abstand</li>
        </ul>
    </dd>
    <dt><dfn>\(k\)-means Clustering</dfn></dt>
    <dd>Siehe <a href="https://martin-thoma.com/machine-learning-1-course/#tocAnchor-1-1-15">ML 1</a>.</dd>
    <dt><dfn>CLARANS</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>CF-Tree</dfn> (<dfn>Clustering Feature Tree</dfn>)</dt>
    <dd>Ein CF-Tree ist ein höhenbalancierter Baum. Jeder Knoten des Baums
        entspricht ein Cluster.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/BIRCH"><dfn>BIRCH</dfn> (<dfn>Balanced Iterative Reducing and Clustering using Hierarchies</dfn>)</a></dt>
    <dd>KEIN hierarchisches Clustering ("hierarchies" bezieht sich auf den Baum, nicht auf das Clusteringergebnis)

    Clustering-Feature (N, LS, SS) für Cluster \(C_i\) mit
    <ul>
        <li>\(N = |C_i|\): Anzahl der Punkte im Cluster</li>
        <li>\(LS = \sum_{i \in C_i} X_i\)</li>
        <li>\(SS = \sum_{i \in C_i} X_i^2\)</li>
    </ul>

    </dd>
    <dt><dfn>Hierarchisches Clustering</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Probabilistisches Clustering</dfn></dt>
    <dd>Datenobjekte werden nicht hart zu einem Cluster zugeordnet sondern
        weich (also mit einer gewissen Wahrscheinlichkeit) jedem Cluster
        zugeordnet.</dd>
    <dt><dfn>Zentrum eines Centroids</dfn></dt>
    <dd>\[X_0 = \frac{1}{N} \sum_{i=1}^N X_i\]</dd>
    <dt><dfn>Radius eines Centroids</dfn></dt>
    <dd>\[R(C_i) = {(\frac{1}{|C_i|} \sum_{j \in C_i}^N {(X_j - X_0)}^2)}^2\]</dd>
    <dt><dfn>Durchmesser eines Centroids</dfn></dt>
    <dd>\[D(C_i) = {(\frac{1}{|C_i| \cdot (|D_i|-1)} \sum_{j \in C_i} \sum_{k \in C_i}^N {(X_j - X_k)}^2)}^2\]</dd>
    <dt><dfn>Interclusterdistanz</dfn></dt>
    <dd>Durchschnittliche Inter-Clusterdistanz von Cluster 1 und Cluster 2:

        \[D_2 = \sqrt{\frac{\sum_{i \in C_1} \sum_{j \in C_2} {(X_i - X_j)}^2}{|C_1| \cdot |C_2|}}\]</dd>
    <dt><dfn>Agglomeratives Clustering</dfn></dt>
    <dd>

        <ul>
            <li>Jedes Objekt ist ein Cluster. Füge die Cluster in die Menge \(M\) ein.</li>
            <li>Berechne alle paarweise Abstände zwischen Clustern in \(M\). Das ist in \(\mathcal{O}(|M|^2)\).</li>
            <li>Merge das Paar \(A, B\) mit kleinstem Abstand zu \(C = A \cup B\). Entferne \(A, B\) aus \(M\) und füge \(C\) ein.</li>
            <li>Abbruch, wenn \(|M| = 1\)</li>
            <li>Gehe zu Schritt 2.</li>
        </ul>

        Gesamtkomplexität: \(\mathcal{O}(n^2)\)
    </dd>
    <dt><dfn>Divisives Clustering</dfn> (<dfn>DIANA</dfn>)</dt>
    <dd>TODO (Splinter group)</dd>
    <dt><dfn>Projected Clustering</dfn></dt>
    <dd>Input sind die Anzahl \(k\) der Cluster, die gefunden werden sollen und
        die durchschnittliche Anzahl der Dimensionen pro Cluster \(l\).

        Output ist eine Partitionierung der Daten in \(k+1\) Mengen</dd>
    <dt><dfn>Manhatten Segmental Distance</dfn></dt>
    <dd>\(d(x_1, x_2) = \frac{1}{n} \cdot \sum_{i=1}^n |x_1^{(i)} - x_2^{(i)}|\) wobei
        \(n\) die Anzahl der Dimensionen von \(x_1, x_2\) ist.</dd>
    <dt><dfn>Jaccard Koeffizient</dfn></dt>
    <dd>\[J(A, B) = \frac{|A \cap B|}{|A \cup B|} \in [0; 1]\]</dd>
    <dt><dfn>DB-Scan</dfn></dt>
    <dd>

    Unterscheidet:

    <ul>
        <li>Dichte Objekte: Epsion-Umgebung hat viele Datenobjekte.</li>
        <li>Dichte-erreibare Objekte: In Epsilon-Umgebung von dichten Objekt.</li>
        <li>Ausreißer: Weder dicht noch dichte-erreichbar.</li>
    </ul>

    Idee: Gehe über alle Punkte \(p \in P\) genau ein mal. Sei \(P' = P\) die
    Menge der nicht-markierten Punkte. Solange es noch
    </dd>
    <dt><dfn>Noise</dfn></dt>
    <dd>Noise sind Punkte, die zu keinem Cluster gehören.</dd>
    <dt><dfn>Outlier</dfn></dt>
    <dd>Noise, welcher weit von jedem Objekt entfernt ist.</dd>
    <dt><dfn>Core-Distanz</dfn></dt>
    <dd>\(C(o) = \min\{\varepsilon \in \mathbb{R} | o \text{ ist mit DBSCAN und } \varepsilon \text{ dicht}\}\).<br/>
        Die Core-Distanz eines Objekts \(o\) ist also die kleinste Distanz, sodass
        \(o\) noch ein dichtes Objekt ist.</dd>
    <dt><dfn>Reachability-Distanz</dfn></dt>
    <dd>\[\text{reach\_d}() = \begin{cases}d(p, o)               &\text{if } d(p, o) > \text{coreDist}(p, o)\\
                                 \text{coreDist}(p, o) &\text{if } d(p, o) < \text{coreDist}(p, o)\end{cases}\]</dd>
    <dt><a href="https://de.wikipedia.org/wiki/OPTICS"><dfn>OPTICS</dfn></a></dt>
    <dd>OPTICS ist ein Algorithmus, der mit den Parametern min_points und
        epsilon (Radius für Cluster-Distanz) automatisch Cluster findet.

        <ul>
            <li>ControlList (Priority Queue) enthält nur Objekte, die noch
                nicht in der Output-Liste sind.</li>
            <li>Kriterium: Minimale reachability-distanz zu Objekten in der
                Output-Liste.</li>
            <li>Rekursiv expandieren wie bei DB-SCAN.</li>
        </ul>

        Siehe <a href="http://www.dbs.informatik.uni-muenchen.de/Publikationen/Papers/OPTICS.pdf">OPTICS: Ordering Points To Identify the Clustering Structure</a>.
    </dd>
    <dt><dfn>Reachability-Plot</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>EM-Algorithmus</dfn> (<dfn>Expectation Maximization</dfn>)</dt>
    <dd>Siehe <a href="https://martin-thoma.com/machine-learning-2-course#em-algorithmus">ML 2</a>.</dd>
    <dt><dfn>Overall Likelihood</dfn></dt>
    <dd>Die Overall Likelihood ist ein Gütemaß für Clusterings.
        \[\prod_{i} \left ( p_A P(x_i | A) + p_B P(x_i | B) \right )\]</dd>
</dl>


### Statistische Modellierung

Slides: `10-StatistModellierung.pdf`

<dl>
    <dt><dfn>Naive Baies</dfn></dt>
    <dd>\[P(H | E) = \frac{P(E_1 | H) \cdot \dots \cdot P(E_n | H) \cdot P(H)}{P(E)}\]</dd>
    <dt><dfn>Laplace-Smoothing</dfn></dt>
    <dd>Um Wahrscheinlichkeiten von 0 zu vermeiden, werden die Zähler mit \(k\) initilisiert.
        Beachte, dass man auch die Gesamtzahl dann um \(k\) erhöhen muss.</dd>
    <dt><dfn>Bayessche Netze</dfn></dt>
    <dd>Ein bayessches Netz ist ein <abbr title="Directed Acyclical Graph">DAG</abbr>.
        Ein Knoten für jedes Attribut sowie Klassenzugehörigkeit.
        Kanten zwischen nicht unabhängigen Attributen.<br/>
        <br/>
        Netzkonstruktion: Meist von Hand (z.B. anhand von Kausalitäten)<br/>
        <br/>
        Finden der Maximum-Likelihood-Parameter.<br/>
        <br/>
        Behandeln fehlender Werte</dd>
    <dt><dfn>Duplikateleminierung</dfn></dt>
    <dd>Spezialfall von Klassifikation</dd>
    <dt><dfn>Versteckte Variablen</dfn></dt>
    <dd>Abstraktion, damit der Raum der zu betrachteten Variablen bei Bayesschen Netzen kleiner wird.</dd>
</dl>

Siehe auch:

* [Is the direction of edges in a Bayes Network irrelevant?](http://datascience.stackexchange.com/q/10064/8820)


### Support Vector Machines

Slides: `11-SupportVectorMachines.pdf`

<dl>
    <dt><dfn>Lineare Regression</dfn></dt>
    <dd>Model \(y = M x\), wobei \(x \in \mathbb{R}^n\) die Features sind,
        \(y \in \mathbb{R}^m\) die Vorhersage und \(M \in \mathbb{R}^{n \times m}\)
        die Modellparameter.</dd>
    <dt><dfn>Cross Entropy Fehlermaß</dfn></dt>
    <dd>\[E_{CE}(w) = \sum_{i=1}^n [(1-y_i) \cdot \log (1-p) + y_i \cdot \log p]\]</dd>
    <dt><dfn>SVM</dfn> (<dfn>Support Vector Machine</dfn>)</dt>
    <dd>See <a href="https://martin-thoma.com/svm-with-sklearn/">SVM article</a>.</dd>
</dl>


### Ensembles

Slides: `12-Ensembles.pdf` (vgl. <a href="https://martin-thoma.com/machine-learning-1-course/#boosting">ML 1</a>)

<dl>
    <dt><dfn>Ensembles</dfn></dt>
    <dd>Mehrere Instanzen auf Trainingsdaten trainieren.

    Vorteile:

    <ul>
        <li>Overfitting wird minimiert.</li>
        <li>Besseres Gesamtsystem</li>
        <li>Parallelisierbarkeit</li>
        <li>TODO: Gibt es mehr Vorteile von Ensembles gegenüber einzelnen Classifieren?</li>
    </ul>

    Typische Techniken sind Bagging und Boosting.</dd>
    <dt><dfn>Bagging</dfn></dt>
    <dd>Ensemble-Learning Technik, bei der Stichproben des
        Trainingsdatenbestandes für die Classifier verwendet werden.
    </dd>
    <dt><dfn>MetaCost</dfn></dt>
    <dd>MetaCost ist ein Verfahren zum Relabeling (TODO: Was ist Relabeling?).
        MetaCost wendet Bagging an.
    </dd>
    <dt><dfn>Boosting</dfn></dt>
    <dd>Boosting ist eine Ensemble-Learning-Technik, die mehrere Modelle vom
        gleichen Typ durch Voting / Durchschnittsberechnung kombiniert. Dabei
        nimmt Boosting Rücksicht auf zuvor falsch Klassifizierte Beispiele
        und gewichtet diese stärker.

        Gewichtungsänderung für korrekte Objekte bei Fehllerrate e: \(\frac{e}{1-e}\)</dd>
</dl>


## Prüfungsfragen

* Was ist Overfitting?<br/>
  → Siehe <a href="https://martin-thoma.com/machine-learning-1-course/#overfitting">ML 1</a>
* Wie berechnet man die Covarianz zweier Zufallsvariablen <span markdown="0">\(X, Y\)</span>?<br/>
  → <span markdown="0">\(\operatorname{Cov}(X,Y) := \operatorname E\bigl[(X - \operatorname E(X)) \cdot (Y - \operatorname E(Y))\bigr]\)</span>
* Warum muss man für NN-Anfragen mit kD-Bäumen nur ein paar Rechtecke anschauen?<br/>
  → TODO
* Warum kann man für räumliche Anfragen nicht ohne weiteres auswerten, wenn man
  für jede Dimension separat einen B-Baum angelegt hat?<br/>
  → TODO
* Wie ist der R-Baum aufgebaut?<br/>
  → TODO
* Wie funktioniert die Suche nach dem nächsten Nachbarn mit dem R-Baum?<br/>
  → TODO
* Was ändert sich, wenn die Objekte eine räumliche Ausdehnung haben?<br/>
  → TODO (Dto. Anfragen)
* Stören uns Überlappungen von Knoten des R-Baums? Wenn ja, warum?<br/>
  → TODO
* Wie unterscheiden sich R-Baum, kD-Baum und kDB-Baum?<br/>
  → TODO
* Wie funktioniert Einfügen in den R-Baum, inklusive Split?<br/>
  → TODO
* Was für Anfragen unterstützen die diversen räumlichen Indexstrukturen?<br/>
  → TODO
* `3-Informatik-Grundlagen.pdf`, Folie 19
* Warum werden bei der NN-Suche nur genau die Knoten inspiziert, deren Zonen
  die NN-Sphere überlappen?<br/>
  → TODO
* Welche Classifier kennen Sie?<br/>
  → Decision Stumps (1-Rules), Entscheidungsbäume, SVMs, Neuronale Netze (TODO: einer fehlt!)
* Was ist der Vorteil von Postpruning verglichen mit Prepruning?<br/>
  → TODO
* Wie baut man einen Entscheidungsbaum auf?<br/>
  → Gehe durch alle Attribute. Finde für jedes einzelne Attribut den Wert, der
     die niedrigste Schnitt-Entropie hat. Nehme dann das Attribut als
     Split-Attribut, welches die niedrigste Schnitt-Entropie hat. Fahre so mit
     den beiden Kindknoten fort, bis ein Abbruchkriterium erfüllt ist. Das
     könnte z.B. eine Entropie von 0 oder eine maximale Tiefe sein.
* Wie kann man Overfitting beim Aufbau eines Entscheidungsbaums
  berücksichtigen?<br/>
  → Prepruning oder Postpruning.
* Wie kann man beim Aufbau des Entscheidungsbaums berücksichtigen, dass
  unterschiedliche Fehlerarten unterschiedlich schlimm sind?<br/>
  → Mehr Trainingsdaten für den schlimmeren Fehler. (TODO, vgl. <a href="http://datascience.stackexchange.com/q/11379/8820">How can decision trees be tuned for non-symmetrical loss?</a>)
* Was ist Wertebereich der FP-Rate?<br/>
  → [0, 1]: Die FP-Rate ist definiert als <span markdown="0">\(\frac{FP}{FP+TN}\)</span>.
  Offensichtlich sind alle Werte nicht-negativ, also kann der Bruch nicht negativ werden.
  Deshalb ist auch der Nenner mindestens so groß wie der Zähler. Wenn TN=0 und
  \(FP \neq 0\), dann ist die FP-Rate gleich 1. Das geht, wenn man z.B. immer
  "True" vorhersagt. Wenn man immer "False" vorhersagt ist die FP-Rate gleich
  0.
* Wie berechnet man den Korrelationskoeffizienten?
  → vgl. <a href="https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#korrelationskoeffizient">oben</a>
* Was ist die "10-fold cross validation"?<br/>
  → vgl. <a href="https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#cross-validation">oben</a>
* Wie haben wir die Erfolgsquote definiert?<br/>
  → vgl. <a href="https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#erfolgsquote">oben</a>
* Was ist ein Lift Chart? Wie unterscheidet es sich von der ROC Kurve?<br/>
  → TODO
* Was für Fehlerarten gibt es bei Vorhersagen von Klassenzugehörigkeiten?<br/>
  → False-Positive, False-Negative (oder: Konfusionsmatrix)
* Was für Kennzahlen kennen Sie, die diese Fehlerarten sämtlich
  berücksichtigen?<br/>
  → F score und Gesamtfehler. (TODO: mehr?)
* Was ist Unterschied zwischen Kovarianz und dem Korrelationskoeffizienten?<br/>
  → Der Korrelationskoeffizient ist normiert (vgl. <a href="https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#korrelationskoeffizient">oben</a>)
* Warum kommt bei der informational loss Funktion die Logarithmusfunktion zur
  Anwendung?<br/>
  → TODO


### Association Rules
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule hohen
  Support und hohe Confidence hat?
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule hohen
  Support und geringe Confidence hat?
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule
  geringen Support und hohe Confidence hat?
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule
  geringen Support und geringe Confidence hat?
* Im Apriori-Algorithmus hat man bei k=2 keinen Prune-Schritt. Warum?<br/>
  → (Antwort: 24.11.2015, 14:34)
* Wie groß sollte man die Hash-Tabelle machen?<br/>
  → So groß wie sinnvoll möglich. Der verfügbare Arbeitsspeicher ist hier eine
  Grenze.
* Welche zwei Sprachen haben wir für die Formulierung der Constraints
  kennengelernt?<br/>
  → TODO
* Warum ist SQL nicht geeignet um Constraints zu formulieren?<br/>
  → TODO

### Clustering
* Wie kann man Radius, Durchmesser und Interclusterdistanz aus N, LS, SS herleiten?<br/>
  → TODO
* Was spricht dagegen, <span markdown="0">\(\mathbf{\varepsilon}\)</span> in
  OPTICS riesig zu wählen?<br/>
  → Dann sind gleich am Anfang mit dem ersten Objekt alle Datenobjekte in der
     Priority-Queue. Damit wäre der Aufwand für die Queue zu hoch.


## Übungen

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

* [Analysetechniken großer Datenbestände](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/)
* [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/)
* [Machine Learning 2](https://martin-thoma.com/machine-learning-2-course/)
* [Mustererkennung](https://martin-thoma.com/mustererkennung-klausur/)
* [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)


## Termine und Klausurablauf

Es ist noch nicht klar, ob es eine mündliche oder eine schriftliche Prüfung
wird.

Falls es mündlich ist, soll es mindestens einen Termin pro Monat geben.

**Datum**: Noch ist es eine mündliche Prüfung<br/>
**Ort**: Noch ist es eine mündliche Prüfung<br/>
**Punkte**: Noch ist es eine mündliche Prüfung<br/>
**Zeit**: Noch ist es eine mündliche Prüfung<br/>
**Punkteverteilung**: Noch ist es eine mündliche Prüfung<br/>
**Bestehensgrenze**: Noch ist es eine mündliche Prüfung<br/>
**Übungsschein**: Gibt es nicht.<br/>
**Bonuspunkte**: Gibt es nicht.<br/>
**Ergebnisse**: Noch ist es eine mündliche Prüfung<br/>
**Einsicht**: Noch ist es eine mündliche Prüfung<br/>
**Erlaubte Hilfsmittel**: keine
