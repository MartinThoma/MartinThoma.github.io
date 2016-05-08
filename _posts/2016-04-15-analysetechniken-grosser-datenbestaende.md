---
layout: post
title: Analysetechniken für große Datenbestände
author: Martin Thoma
date: 2016-04-15 11:22
category: German posts
tags: Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Analysetechniken für große Datenbestände&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="https://dbis.ipd.kit.edu/english/336.php">Herrn Prof. Dr.-Ing. Klemens Böhm</a> im Wintersemester 2015/2016 gehört. Der Artikel ist noch am Entstehen.</div>

In der Vorlesung 'Analysetechniken für große Datenbestände' werden vor allem
Association Rule Mining und Clustering-Techniken besprochen. Zum Association
Rule minining ist vor allem der Apriori-Algorithmus sowie die Verbesserung mit
FP-Trees zu nennen. Beim Clustering ist k-means, EM, DBSCAN, OPTICS und BIRCH
von großer Bedeutung. Ein weiteres großes Kapitel sind Bayessche Netze.

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
  <dt><a href="https://en.wikipedia.org/wiki/Association_rule_learning"><dfn>Association Rules</dfn></a></dt>
  <dd>Association Rules sind Regeln der Form:
      Wenn eine Transaktion A enthält, dann auch B (formal: $A \Rightarrow B$).
      <br/>
      Association rules werden z.B. in der Market Basket Analysis eingesetzt.
      Sie können aus Frequent item sets relativ einfach erzeugt werden.
      <br/>
      Der Apriori Algorithmus dient dem Finden von Association Rules.<br/>
      <br/>
      Association Rules sind stark mit <a href="https://en.wikipedia.org/wiki/Collaborative_filtering">Collaborative filtering</a> verwandt.
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
    <dd>Ein Metrischer Raum ist eine Menge $M$ mit einer Funktion
        $d: M \times M \rightarrow \mathbb{R}_0^+$ für die gilt:

        <ul>
            <li>Symmetrie: $\forall p,q \in M: d(p, q) = d(q, p) $</li>
            <li>Definitheit: $\forall p,q \in M: d(p, q) = 0 \Leftrightarrow p = q$</li>
            <li>Dreiecksungleichung: $\forall p,q,r \in M: d(p, r) \leq d(p,q) + d(q, r)$</li>
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
        Es gibt eine Funktion $G$, so dass
        $$F(\{X_{i,j}\}) = G(\{F(X_{i,j} | i=1, \dots, l) | j = 1, \dots, J\})$$

        MIN, MAX und COUNT sind distributive Aggregatfunktionen.
    </dd>
    <dt><dfn>Algebraische Aggregatfunktion</dfn></dt>
    <dd>Es gibt eine Funktion $G$, die ein $M$-Tupel liefert und $H$,
        so dass
        $$F(\{X_{i,j}\}) = H(\{G(\{X_{i,j} | i=1, \dots, l\}) | j=1, \dots, J\})$$

        AVG ist eine Algebraische Aggregatfunktion. Hier berechnet $G$ die
        Summe und gibt zusätzlich die Anzahl der Werte zurück. $H$ summiert
        die Summen auf und teilt das Ergebnis durch die Gesamtzahl.<br/>
        <br/>
        Weitere: Truncated Average</dd>
    <dt><dfn>Holistische Aggregatfunktion</dfn></dt>
    <dd>Man kann keine Beschränkung des Speicherbedarfs für Sub-Aggregate,
        d.h. Aggregate über $\{X_{i,j}| i=1, \dots, l\}$, angeben.<br/>
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
    <dd>$$\frac{MAX-MIN}{2}$$</dd>
    <dt><dfn>Entropie</dfn></dt>
    <dd>$$E(S) = - \sum_{j} p_j \cdot \log p_j$$

        $E(S)=0$ ist minimal, wenn es ein $j$ gibt mit $p_j = 1$.
        $E(S)=\log(n)$ ist maximal, wenn $p_i = p_j$ gilt für $i, j$.</dd>
    <dt><dfn>Korrelationsmaße</dfn></dt>
    <dd>Sind üblicherweise auf [-1, 1] normiert. Die Kovarianz ist ein
        nicht-normiertes Korrelationsmaß.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Kovarianz_(Stochastik)#Definition"><dfn>Kovarianz</dfn></a></dt>
    <dd>$$\operatorname{Cov}(X,Y) := \operatorname E\bigl[(X - \operatorname E(X)) \cdot (Y - \operatorname E(Y))\bigr]$$</dd>
    <dt><a id="korrelationskoeffizient" href="https://de.wikipedia.org/wiki/Korrelationskoeffizient#Definitionen"><dfn>Korrelationskoeffizient</dfn></a></dt>
    <dd>$$\varrho(X,Y) =\frac{\operatorname{Cov}(X,Y)}{\sigma(X)\sigma(Y)} \in [-1, 1]$$</dd>
    <dt><dfn>PCA</dfn> (<dfn>Principal Component Analysis</dfn>)</dt>
    <dd>PCA ist ein Algorithmus zur Reduktion von Daten durch das Entfernen von
        Attributen. Er projeziert die Datenobjekte auf eine Hyperebene, sodass
        ein Maximum der Varianz beibehalten wird (vgl. <a href="https://martin-thoma.com/neuronale-netze-vorlesung/#pca">Neuronale Netze</a>)</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Chi-Quadrat-Test#Unabh.C3.A4ngigkeitstest"><dfn>Chi-Quadrat-Test</dfn></a></dt>
    <dd>Oberbegriff für mehrere Tests; hier nur der Unabhängigkeitstest.<br/>
        <br/>
        Gegeben sind zwei Verteilungen von Zufallsvariablen $X, Y$. Die Frage
        ist, ob sie unabhängig sind.<br/>
        Dazu zählt man die Ausprägungen $i=1, \dots, m_1$ des Merkmals $X$
        und die Ausprägungen $j=1, \dots, m_2$ des Merkmals $Y$ sowie
        wie häufig diese in Kombination auftreten ($n_{ij}$). Man schätzt den
        erwarteten Wert durch $e_{ij} = \frac{1}{n} \left(\sum_{k=1}^{m_2} n_{ik} \right) \cdot \left (\sum_{k=1}^{m_2} n_{kj}\right )$. Der Chi-Quadrat wert ist dann:

        $$\chi^2 = \sum_{i=1}^{m_1} \sum_{j=1}^{m_2} \frac{(n_{ij} - e_{ij})^2}{e_{ij}}$$

        Daraus wird ein $p$-Wert abgeleitet. Wenn dieser unter einem
        Schwellwert wie $\alpha = 0.01$ ist, dann wird die Hypothese, dass
        die Verteilungen unabhängig sind, zurückgewiesen.

        Die Nullhypothese, dass $X, Y$ unabhängig sind wird auf dem
        Signifikanzniveau $\alpha$ verworfen, falls

        $$\chi^2 > \chi^2_{(1-\alpha; (m_1-1)(m_2-1))}$$

        </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Kolmogorow-Smirnow-Test"><dfn>Kolmogorow-Smirnow-Test</dfn></a> (<dfn>KSA-Test</dfn>)</dt>
    <dd>Test auf unabhängigkeit kontinuierlicher Verteilungen, also:
        $$H_0: F_X(x) = F_0(x)$$

        Es wird die empirsche Verteilungsfunktion $S$ gebildet und diese mit
        der hypothetischen Verteilungsfunktion $F_0$ verglichen, wobei
        $S(x_0) = 0$ gesetzt wird:
        $$d_{\max} = \max(\max_{i=1, \dots, n}|S(x_i) - F_0(x_i)|, \max_{i=1, \dots, n} |S(x_{i-1} - F_0(x_i))|)$$
        $H_0$ wird verworfen, wenn $d_{\max} > d_\alpha$, wobei $d_\alpha$
        bis zu $n=35$ tabelliert vorliegt. Bei großerem $n$ kann
        näherungsweise
        $$d_\alpha = \sqrt{\frac{-\frac{1}{2} \ln(\frac{\alpha}{2})}{n}}$$
        </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Wilcoxon-Mann-Whitney-Test"><dfn>Wilcoxon-Mann-Whitney-Test</dfn></a> ($U$-Test)</dt>
    <dd>Es seien $X,Y$ Zufallsvariablen mit Verteilungsfunktionen
        $F_X(x) = F_Y(x-a)$ für ein $a \in \mathbb{R}$.<br/>
        <br/>
        $H_0: a = 0$ vs $H_1: a \neq 0$<br/>
        Vorgehen: Gemeinsame Stichprobe sortieren, Rangsumme für $X$ und $Y$
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
    <li>Wahrscheinlichkeitsraum, Ereignis, Ergebnis, Ergebnismenge $\Omega$,
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
    <dd>Ein balancierter kD-Baum. Die Balancierung wird durch eine Kombination
        aus heterogenem k-d-Baum und B*-Baum erreicht. Der baum ist also nicht
        auf logischer, sondern nur auf physischer Ebene balanciert.</dd>
    <dt><a id="r-tree"></a><dfn>R-Baum</dfn></dt>
    <dd>Ein R-Baum ist ein balancierter Baum, welcher die Datenobjekte in
        minimale <abbr title="umhüllende achsenparallele bounding-boxen">AABBs</abbr>
        einschließt. Jeder Knoten hat eine solche AABB und jedes der Kinder -
        egal ob es wieder ein AABB oder Datenpunkte sind - ist darin.
        Diese AABBs können sich überschneiden.<br/>
        <br/>
        TODO <a href="http://cs.stackexchange.com/q/56337/2914">What is the difference between a R-tree and a BVH?</a></dd>
    <dt><dfn>Nearest Neighbor in R-Tree</dfn></dt>
    <dd>Siehe <a href="https://github.com/MartinThoma/algorithms/blob/master/nearest-neighbor-r-tree/nn_r_tree_pseudo.py">Pseudo-Code</a>.</dd>
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

    $$E(S_1, S_2) = \frac{n_1}{n} E(S_1) + \frac{n_2}{n} E(S_2)$$

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
    <dt><a id="cross-validation"></a><dfn>$k$-Fold Cross-Validation</dfn> (<dfn>Kreuzvalidierung</dfn>)</dt>
    <dd>Unterteile den Datensatz in $k$ Teile. Dabei sollten die Klassen in
        etwa gleich häufig in allen Teilen vorkommen.

        Mache nun $k$ durchläufe, wobei der $k$-te Datensatz immer zum
        Testen und alle anderen zum Trainieren verwendet werden. Berechne die
        $k$ Testfehler. Mittle diese am Ende. Das ist ein besserer Schätzwert
        für den realen Fehler als eine einmalige Unterteilung in Training- und
        Testmenge.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Stratified_sampling" id="stratification"><dfn>Stratification</dfn></a></dt>
    <dd>Sicherstellen, dass bestimmte Eigenschaften (z.B. Klassenzugehörigkeit) in Partitionen etwa gleich verteilt ist.</dd>
    <dt><dfn>Loss function</dfn></dt>
    <dd>Eine Funktion, die angibt, wie viel man durch eine unkorrekte
        Vorhersage verliert.</dd>
    <dt><dfn>Informational Loss function</dfn></dt>
    <dd>$$- \log_2 p_i$$ - Wahrscheinlichkeiten der nicht-eintretenden Klassen spielen keine Rolle</dd>
    <dt><dfn>Quadratic Loss function</dfn></dt>
    <dd>$$\sum_{j} (p_j - a_j)^2$$ mit tatsächlichem Label $a_j \in \{0,1\}$
        und geschätzter Wahrscheinlichkeit $p_j$ für die Klasse $j$.</dd>
    <dt><dfn>Bias</dfn></dt>
    <dd>Das Verfahren an sich funktioniert nicht gut. Selbst beliebig viele
        Trainingsdaten beheben dieses Problem nicht. Der Fehler ist
        inhärent im Verfahren verankert.</dd>
    <dt><dfn>Varianz</dfn></dt>
    <dd>Fehler welcher durch das Fehlen von Trainingsdaten verursacht wird.</dd>
    <dt><a id="erfolgsquote"></a><dfn>Gesamt-Erfolgsquote</dfn></dt>
    <dd>$$\frac{TP+TN}{TP+TN+FP+FN}$$</dd>
    <dt><dfn>Konfusionsmatrix</dfn> (<dfn>Confusion matrix</dfn>)</dt>
    <dd>Eine Tabelle, in der jede Zeile für die tatsächlichen Klassen stehen
        und die Spalten für die vorhergesagten Klassen. Die Diagonalelemente
        zählen also die richtig vorhergesagten Datenobjekte; alle anderen
        Zellen zählen falsche Vorhersagen.</dd>
    <dt><dfn>Kappa-Koeffizient</dfn> (<a href="https://de.wikipedia.org/wiki/Cohens_Kappa"><dfn>Cohens Kappa</dfn></a>)</dt>
    <dd>Vergleich mit Klassifier, der nur den Anteil der Klassenzugehörigkeit
        schätzt:
        $$\kappa =\frac{p_0-p_c}{1-p_c}$$
        wobei $p_0$ die gemessene Übereinstimmung ist und $p_c$ die
        erwartete Übereinstimmung bei Unabhängigkeit. Wenn also $h_{ij}$ die
        Anzahl der Datenobjekte ist, für die der erste Klassifizierer die Klasse
        $i$ und der zweite Klassifizierer die Klasse $j$ vorhergesagt hat
        sowie $N$ die Gesamtzahl der Datenobjekte und $z$ die Gesamtzahl
        der Klassen, dann gilt:

        $$p_0 = \frac{\sum_{i=1}^z h_{ii}}{N}$$

        Die erwartete Übereinstimmung $p_c$ wird über die Randhäufigkeiten
        geschätzt:
        $$p_c = \frac{1}{N^2} \sum_{i=1}^z h_{.i} \cdot h_{i.}$$

        Der Wertebereich ist also: $\kappa \in (-\infty; 1]$, wobei
        der minimale Wert von $\kappa$ nicht beliebig klein werden kann.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Association_rule_learning#Lift"><dfn>Lift-Faktor</dfn></a></dt>
    <dd>Faktor, um den sich die Rücklaufquote erhöht:

        $$\mathrm{lift}(X\Rightarrow Y) = \frac{ \mathrm{supp}(X \cup Y)}{ \mathrm{supp}(X) \cdot \mathrm{supp}(Y) }$$

        Der Lift ist ein Indiz für die Unabhängigkeit von $X$ und $Y$.
        Ist der Lift nahe bei 1, dann spricht das für die Unabhängigkeit. Ein
        Lift-Faktor kleiner als 1 bedeutet, dass die Itemsets zusammen seltener
        vorkommen als bei Unabhängigkeit zu erwarten wäre. Ein Lift-Faktor von
        größer als 1 bedeutet, dass die Itemsets zusammen häufiger vorkommen
        als bei Unabhängigkeit zu erwarten wäre.

    </dd>
    <dt><a href="https://en.wikipedia.org/wiki/Receiver_operating_characteristic"><dfn>ROC</dfn></a> (<dfn>Receiver Operator Characteristic</dfn>)</dt>
    <dd>x-Achse: $\frac{FP}{FP+TN} \cdot 100$ (FP-Rate),<br/>
        y-Achse: $\frac{TP}{TP+FN} \cdot 100$ (TP-Rate)

        Siehe auch: <a href="https://www.reddit.com/r/answers/comments/4g2wgx/where_does_the_name_receiver_operating/">Namensherkunft</a></dd>
    <dt><dfn>Recall</dfn> (<dfn>True Positive Rate</dfn>, <dfn>TPR</dfn>, <dfn>Sensitivität</dfn>)</dt>
    <dd>$$TPR = \frac{TP}{TP + FN} = 1 - FNR \in [0, 1]$$

        Der Recall gibt den Anteil der erkannten positiven aus allen positiven
        an.

        <i>Sensitivität</i> ist ein in der Medizin üblicher Begriff.</dd>
    <dt><dfn>Precision</dfn> (<dfn>Genauigkeit</dfn>)</dt>
    <dd>$$Precision = \frac{TP}{TP + FP} \in [0, 1]$$

        Die Precision gibt den Anteil der real positiven aus den als positiv
        erkannten an.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/F1_score"><dfn>F-Measure</dfn></a> (<dfn>F1 score</dfn>)</dt>
    <dd>$$\frac{2 \cdot \text{precision} \cdot \text{recall}}{\text{recall} + \text{precision}}$$</dd>
    <dt><dfn>Correlation Coefficient</dfn></dt>
    <dd>Der Correlation Coefficient ist kein Fehlermaß. Der
        $CC(p, a)$ ist groß, wenn sich $p$ und $a$ ähnlich sind.

        $$CC(p, a) = \frac{COV(p, a)}{\sigma(p) \cdot \sigma(a)}$$

        Mit $\sigma(x) = \frac{1}{n-1} \cdot \sum_{i} (x_i - \bar{x})^2$</dd>
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

* Folie 23: Wo kommt die 140 her?<br/>
  → Summe der Diagonalelemente auf Folie 21.
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
    <dt><a id="support"></a><dfn>Support</dfn></dt>
    <dd>Die Anzahl der Transaktionen, die das Itemset $I$ enthalten wird
    <i>Support von $I$</i> genannt.<br/>
        Es gilt:
        $$\text{support}(A \Rightarrow B) = \text{support}(A \cup B)$$</dd>
    <dt><dfn>Closed Itemset</dfn></dt>
    <dd>Ein Itemset $I$ heißt closed, wenn es keine echte Obermenge $I' \supsetneq I$ gibt,
        die den gleichen support $\text{supp}(I') = \text{supp}(I)$ hat.</dd>
    <dt><a id="confidence"></a><dfn>Confidence</dfn></dt>
    <dd>Confidence von $A \Rightarrow B$ ist der Anteil der Transaktionen,
        die $A$ und $B$ enthalten, von den Transaktione die $A$ enthalten:

        $$\text{conf}(A \Rightarrow B) = \frac{\text{support}(A \cup B)}{\text{support}(A)} \in [0, 1]$$</dd>
    <dt><dfn>Apriori Algorithmus</dfn></dt>
    <dd>Der Apriori-Algorithmus ist ein Generate-and-Test-Algorithmus zum
        Finden von Frequent Itemsets.

        <ol>
            <li>Erzeuge alle einelementigen Frequent Itemsets</li>
            <li>for k in range(2, n): Erzeuge die $k$-elementigen frequent
                Itemsets (join, prune, support counting)</li>
            <li>Frequent itemsets: Association Rules</li>
        </ol>

        Der Algorithmus nutzt aus, dass eine notwendige Bedingung für
        $k$-elementige Frequent Itemsets ist, dass alle $k-1$-elementigen
        Frequent Itemsets auch Frequent sein müssen.

        Verbesserungen:

        <ul>
            <li>Stichproben verwenden (Sampling)</li>
            <li>Aggressiver durch Datenbestand gehen (z.B. von k=3 zu k=6 springen)</li>
            <li>Hashfilter</li>
        </ul>
    </dd>
    <dt><dfn id="fp-tree">FP-Trees</dfn></dt>
    <dd>FP-Trees (FP für "frequent pattern") sind eine Datenstrutkur zum
        schnellen Finden von Frequent Itemsets. Jeder Knoten im Baum
        repräsentiert ein Item. Jeder Knoten speichert zusätzlich die
        Häufigkeit des Präfixes, welcher durch den Pfad von der Wurzel zu dem
        Knoten dargestellt wird. Zusätzlich speichert jeder Knoten des Items
        $i$ einen Zeiger auf einen anderen Knoten mit einem Item $i$. Jede
        Transaktion entspricht einem Pfad im FP-Tree.<br/>
        Zusätzlich zum FP-Tree gibt es eine Header-Tabelle. Die Zeilen dieser
        Tabelle sind einzelne Items $i$, denen jeweils ein Zeiger auf einen
        Knoten im FP-Tree zugeordnet sind, der auch das Item $i$
        repräsentiert.<br/>
        Für jedes Item gibt es also eine verkettete Liste, die das Vorkommen im
        Baum angibt.<br/>

        Zum Finden von Frequent Items geht man also wie folgt vor:
    <ol>
        <li>Für jedes Item: Zähle in wie vielen Transaktionen das Item vorkommt.</li>
        <li>Sortiere Items in Transaktion absteigend nach Häufigkeit. Bei
            gleicher Häufigkeit wird z.B. alphabetisch sortiert. Damit ergibt
            sich eine eindeutige Reihenfolge.</li>
        <li>Sortiere Transaktionen nach den Items innerhalb der Transaktionen.</li>
        <li>Aufbau des FP-Trees
        <ol>
            <li>Aufbau des Baums</li>
            <li>Aufbau der Header-Tabelle: Absteigend eindeutig nach Häufigkeit
                sortiert</li>
        </ol>
        </li>
        <li>Starte mit dem niedrigsten Element in der Header-Tabelle. Überprüfe
            den Präfix auf den erwarteten support. Gehe dazu alle Elemente
            dieses Items durch (alle Präfix-Pfade im Baum) und wende eine Art
            Apriori-Algorithmus an um in diesen Präfix-Pfaden mit dem Item
            $i$ die Frequent-Itemsets zu finden.</li>
    </ol>

    Siehe auch: <a href="https://www.cs.sfu.ca/~jpei/publications/sigmod00.pdf">Mining Frequent Patterns without Candidate Generation</a>
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
    <dd>Ein 1-var Constraint heißt anti-monoton, wenn für alle Mengen $S, S'$
        gilt:

        $$(S \supseteq S' \land (S \text{ erfüllt } C )) \Rightarrow S' \text{ erfüllt } C$$

        Wenn also ein Constraint $C$ für eine Menge $S$ erfüllt ist, dann
        auch für jede Teilmenge $S'$.

        Beispiele:
        <ul>
            <li>$\min(S) \geq v, \;\;\; v \in \mathbb{R}$ ist anti-monoton</li>
            <li>$\max(s) \geq v, \;\;\; v \in \mathbb{R}$ ist nicht anti-monoton</li>
            <li>$\text{size}(s) \leq v, \;\;\; v \in \mathbb{N}$ ist anti-monoton</li>
            <li>$\text{size}(s) \geq v, \;\;\; v \in \mathbb{N}$ ist nicht anti-monoton</li>
        </ul>

        Eine gutartige Eigenschaft von Constraints. Hier kann das
        Constraint sehr früh überprüft werden.</dd>
    <dt><dfn>Succinctness</dfn></dt>
    <dd>Ein Constraint heißt succinct, wenn alle Itemsets die es erfüllen
        schnell erzeugt werden können.<br/>
        <br/>
        Beispiel: Man hat das Constraint, dass der Typ "Non-Food" sein soll.
        Aber es gibt nur 3&nbsp;Produkte die diesen Typ haben. Kandidaten, die
        das Constraint nicht erfüllen werden gar nicht erst erzeugt.</dd>
</dl>

* Meta-Rule Guided mining
* Constraint durch schwächeres Anti-Monotones Constraint ersetzen.


### Clustering

Slides: `9-Clustering-1.pdf` und `9-Clustering-2.pdf`

<dl>
    <dt><dfn>Silhouette-Koeffizient</dfn></dt>
    <dd>Sei $C = (C_1, \dots, C_k)$ ein Clustering.

    <ul>
        <li>Durchschnittlicher Abstand zwischen Objekt o und anderen Objekten in seinem Cluster:
            $$a(o) = \frac{1}{|C(o)|} \sum_{p \in C(o)} dist(o, p)$$</li>
        <li>Durchschnittlicher Abstand zum zweitnächsten Cluster:
            $$b(o) = \min_{C_i \in \text{Cluster} \setminus C(o)}(\frac{1}{C_i}) \sum_{p\in C_i} \sum_{p \in C_i} \text{dist}(o, p)$$</li>
        <li>Silhouette eines Objekts:
            \[s(o) = \begin{cases}0  &\text{if } a(o) = 0, \text{i.e. } |C_i|=1\\
                    \frac{b(o)-a(o)}{\max(a(o), b(o))} &\text{otherwise}\end{cases}\]
            Es gilt:
            $$s(o) \in [-1, 1]$$</li>
        <li>$\text{silh}(C) = \frac{1}{|C|} \sum_{C_i \in C} \frac{1}{|C_i|} \sum_{o \in C_i} s(o)$.
            Es gilt:
            $$\text{silh}(C) \in [-1; 1]$$
            Es ist ein möglichst großer Wert gewünscht. Alles kleiner als 0 ist schlecht.</li>
    </ul>
    </dd>
    <dt><dfn>Distanzfunktionen für Cluster</dfn></dt>
    <dd>
        Seien $X, Y$ Cluster.

        <ul>
            <li>Durschnittlicher Objektabstand: $\text{dist}_{avg}(X, Y) = \frac{1}{|X| \cdot |Y|} \cdot \sum_{x in X, y\in Y} \text{dist}(x, y)$</li>
            <li>Single Link: $\text{dist}_{sl}(X, Y) = \min_{x \in X, y \in Y} \text{dist}(x, y)$</li>
            <li>Complete Link: $\text{dist}_{cl}(X, Y) = \max_{x \in X, y \in Y} \text{dist}(x, y)$</li>
        </ul>
    </dd>
    <dt><dfn id="k-means">$k$-means Clustering</dfn></dt>
    <dd>Siehe <a href="https://martin-thoma.com/machine-learning-1-course/#tocAnchor-1-1-15">ML 1</a>.</dd>
    <dt><dfn id="clarans">CLARANS</dfn></dt>
    <dd>CLARANS ist ein Clustering-Algorithmus, der mit $k$-Means
        verwandt ist. Auch er erwartet einen Parameter $k \in \mathbb{N}$,
        der die erwartete Anzahl an Clustern angibt. Dann geht CLARANS davon
        aus, dass jeder Medeoid durch einen Datenpunkt im Datensatz
        repräsentiert werden kann. Für eine zufällige Wahl von $k$ Punkten
        $M = \{p_1, \dots, p_k\}$ wird ein Score berechnet. Dann überprüft
        man, was der Tausch eines Punktes $p_i$ durch den Punkt $p_j$
        für beliebige $p_i \in M$ und $p_j \notin M$ am Score ändern würde.
        Den besten Tausch führt man durch.<br/>
        <br/>
        Siehe auch: <a href="http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=1033770&url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F69%2F22199%2F01033770.pdf%3Farnumber%3D1033770">CLARANS: a method for clustering objects for spatial data mining</a>
        </dd>
    <dt><dfn>CF-Tree</dfn> (<dfn>Clustering Feature Tree</dfn>)</dt>
    <dd>Ein CF-Tree ist ein höhenbalancierter Baum. Jeder Knoten des Baums
        entspricht ein Cluster.<br/>
        <br/>
        Clustering-Feature (N, LS, SS) für Cluster $C_i$ mit
        <ul>
            <li>$N = |C_i|$: Anzahl der Punkte im Cluster</li>
            <li>$LS = \sum_{i \in C_i} X_i$</li>
            <li>$SS = \sum_{i \in C_i} X_i^2$</li>
        </ul>
        </dd>
    <dt><a id="birch" href="https://en.wikipedia.org/wiki/BIRCH"><dfn>BIRCH</dfn> (<dfn>Balanced Iterative Reducing and Clustering using Hierarchies</dfn>)</a></dt>
    <dd>BIRCH ist ein Clustering-Algorithmus, welcher CF-Trees benutzt und
        mit wenig Speicherplatz auskommt. Der CF-Tree wird im ersten Schritt
        aufgebaut.<br/>
        <br/>
        BIRCH ist KEIN hierarchisches Clustering ("hierarchies" bezieht sich
        auf den Baum, nicht auf das Clusteringergebnis).<br/>
        <br/>
        Parameter von BIRCH:
        <ul>
            <li>$k \in \mathbb{N}^+$: Anzahl der Cluster</li>
            <li>$B \in \mathbb{N}^+$: (Fan-out), maximale Anzahl an Kindknoten</li>
            <li>$B' \in \mathbb{N}^+$: maximale Blatt-Kapazität (Anzahl Elementarcluster)</li>
            <li>$T  \in \mathbb{R}^+$ (Schwellwert): Maximaler Radius (oder Durchmesser), bevor ein
                Elementar-Cluster gesplittet wird</li>
        </ul>
        Siehe auch:
        <ul>
            <li><a href="https://www.youtube.com/watch?v=FAVETO6EK9E">YouTube</a> (7:24min)</li>
            <li></li>
        </ul>
    </dd>
    <dt><dfn>Hierarchisches Clustering</dfn></dt>
    <dd>Beim hierarchischen Clustern werden Datenpunkte Baumartig zu Clustern
        zusammengefasst. Das ganze sieht einem Abstammungsbaum der Arten in der
        Biologie sehr ähnlich.<br/>
        <br/>
        Es gibt zwei Vorgehensweisen:
        <ul>
            <li><a href="#agglomerative-clustering">Agglomorativ</a></li>
            <li><a href="#divisive-clustering">Divisives Clustering</a></li>
        </ul>

        <a href="https://de.wikipedia.org/wiki/Hierarchische_Clusteranalyse#Dendrogramm">Dendrogramme</a> sind eine typische Visualisierung für das Ergebnis einer
        hierarchischen Clusteranalyse.

    </dd>
    <dt><dfn>Probabilistisches Clustering</dfn></dt>
    <dd>Datenobjekte werden nicht hart zu einem Cluster zugeordnet sondern
        weich (also mit einer gewissen Wahrscheinlichkeit) jedem Cluster
        zugeordnet.</dd>
    <dt><dfn>Zentrum eines Clusters</dfn></dt>
    <dd>$$Z_{i} = \frac{1}{|C_i|} \sum_{i \in C_i} X_i$$</dd>
    <dt><dfn>Radius eines Clusters</dfn></dt>
    <dd>

    Der Radius enes Centroids ist der durchschnittliche Abstand zum Centroiden:

    $$R(C_i) = \sqrt{\frac{1}{|C_i|} \sum_{j \in C_i} {(X_j - Z_i)}^2}$$

    </dd>
    <dt><dfn>Durchmesser eines Clusters</dfn></dt>
    <dd>

    Der Durchmesser eines Centroiden ist die durchschnittle paarweise Distanz:

    $$D(C_i) = \sqrt{\frac{1}{|C_i| \cdot (|C_i|-1)} \sum_{j \in C_i} \sum_{k \in C_i} {(X_j - X_k)}^2}$$</dd>
    <dt><dfn>Interclusterdistanz</dfn></dt>
    <dd>Durchschnittliche Inter-Clusterdistanz von Cluster 1 und Cluster 2:

        $$D(C_1, C_2) = \sqrt{\frac{\sum_{i \in C_1} \sum_{j \in C_2} {(X_i - X_j)}^2}{|C_1| \cdot |C_2|}}$$</dd>
    <dt><a id="agglomerative-clustering"></a><dfn>Agglomeratives Clustering</dfn></dt>
    <dd>

        <ul>
            <li>Jedes Objekt ist ein Cluster. Füge die Cluster in die Menge $M$ ein.</li>
            <li>Berechne alle paarweise Abstände zwischen Clustern in $M$. Das ist in $\mathcal{O}(|M|^2)$.</li>
            <li>Merge das Paar $A, B$ mit kleinstem Abstand zu $C = A \cup B$. Entferne $A, B$ aus $M$ und füge $C$ ein.</li>
            <li>Abbruch, wenn $|M| = 1$</li>
            <li>Gehe zu Schritt 2.</li>
        </ul>

        Gesamtkomplexität: $\mathcal{O}(n^2)$
    </dd>
    <dt><a id="divisive-clustering"></a><dfn>Divisives Clustering</dfn> (<dfn id="diana">DIANA</dfn>, <dfn>DIvisive ANAlysis</dfn>)</dt>
    <dd>Divisives Clustering ist ein hierarchisches Clusteringverfahren. Es
        startet mit einem großen Cluster und unterteilt diesen rekursiv immer
        weiter in je zwei kleine Cluster.<br/>
        <br/>
        Das Unterteilen funktioniert wie folgt: Wähle in einem Cluster $C$ das
        Datenobjekt $o$, welches den höchsten durchschnittlichen Abstand von
        allen anderen Datenobjekten $o' \in C \setminus \{o\}$ hat. Dieses ist
        nun das erste Objekt einer neu erstellten sogenannten Splittergruppe
        $S = \{o\}$
        (engl. <i>splinter group</i>). Nun gibt es noch das Maß
        $$D(o) = \sum_{o' \in C \setminus S} \frac{d(o, o')}{|C \setminus S|} - \sum_{o'} \frac{d(o, o')}{|S|}$$
        Solange $D(o) > 0$ für ein $o \in C \setminus S$ wird $o^* = \text{arg max}_{o \in C \setminus S} D(o)$ aus dem Cluster in die Splittergruppe gesteckt.
        <br/>
        Siehe auch:
        <ul>
            <li><a href="https://stat.ethz.ch/R-manual/R-devel/library/cluster/html/diana.html">R implementierung</a></li>
            <li><a href="http://onlinelibrary.wiley.com/book/10.1002/9780470316801">Leonard Kaufman, Peter J. Rousseeuw: Finding Groups in Data: An Introduction to Cluster Analysis.</a></li>
        </ul>
    </dd>
    <dt><dfn>Projected Clustering</dfn></dt>
    <dd>Input sind die Anzahl $k$ der Cluster, die gefunden werden sollen und
        die durchschnittliche Anzahl der Dimensionen pro Cluster $l$.

        Output ist eine Partitionierung der Daten in $k+1$ Mengen</dd>
    <dt><dfn>Manhatten Segmental Distance</dfn></dt>
    <dd>$d(x_1, x_2) = \frac{1}{n} \cdot \sum_{i=1}^n |x_1^{(i)} - x_2^{(i)}|$ wobei
        $n$ die Anzahl der Dimensionen von $x_1, x_2$ ist.</dd>
    <dt><dfn>Jaccard Koeffizient</dfn></dt>
    <dd>$$J(A, B) = \frac{|A \cap B|}{|A \cup B|} \in [0; 1]$$</dd>
    <dt><a href="https://de.wikipedia.org/wiki/DBSCAN" id="dbscan"><dfn>DBSCAN</dfn></a></dt>
    <dd>DBSCAN ist ein Algorithmus zum finden von Clustern.

    Er unterscheidet 3 Arten von Datenpunkten:

    <ul>
        <li>Dichte Objekte: Epsion-Umgebung hat viele Datenobjekte.</li>
        <li>Dichte-erreibare Objekte: In Epsilon-Umgebung von dichten Objekt.</li>
        <li>Ausreißer: Weder dicht noch dichte-erreichbar.</li>
    </ul>

    Idee: Gehe über alle Punkte $p \in P$ genau ein mal. Sei $P' \leftarrow P$ die
    Menge der nicht-markierten Punkte. Solange $|P'| > 0$ wird ein Punkt
    entnommen. Ist er dicht, so ist es ein neues Cluster. Von diesem Punkt aus
    wird rekursiv alles in der $\varepsilon$-Umgebung zum Cluster hinzugefügt.
    Hat der Punkt weniger als min_point Punkte in seiner $\varepsilon$-Umgebung,
    so wird er als Ausreißer markiert.

    Siehe auch: <a href="http://www.dbs.ifi.lmu.de/Publikationen/Papers/KDD-96.final.frame.pdf">A density-based algorithm for discovering clusters in large spatial databases with noise</a>
    </dd>
    <dt><dfn>Noise</dfn></dt>
    <dd>Noise sind Punkte, die zu keinem Cluster gehören.</dd>
    <dt><dfn>Outlier</dfn></dt>
    <dd>Noise, welcher weit von jedem Objekt entfernt ist.</dd>
    <dt><dfn>Core-Distanz</dfn></dt>
    <dd>$C(o) = \min\{\varepsilon \in \mathbb{R} | o \text{ ist mit DBSCAN und } \varepsilon \text{ dicht}\}$.<br/>
        Die Core-Distanz eines Objekts $o$ ist also die kleinste Distanz, sodass
        $o$ noch ein dichtes Objekt ist.</dd>
    <dt><dfn>Reachability-Distanz</dfn></dt>
    <dd>Seien $p, o$ Datenpunkte.

    \[\text{reach\_d}(p, o) = \begin{cases}\max(d(p, o), \text{coreDist}(p, o)) &\text{if } d(p, o) < \varepsilon\\
                                 \text{undefined} &\text{otherwise}\end{cases}\]</dd>
    <dt><a href="https://de.wikipedia.org/wiki/OPTICS" id="optics"><dfn>OPTICS</dfn></a></dt>
    <dd>OPTICS ist ein Algorithmus, der mit den Parametern min_points und
        $\varepsilon$ (maximaler Radius für Cluster-Distanz) automatisch
        Cluster findet. Er startet dabei bei einem beliebigen Punkt. Dieser
        Punkt definiert ein Cluster, wenn mindestens min_points von ihm aus
        maximal $\varepsilon$ entfernt sind. Dann wird der naheste Punkt zu
        dem Cluster hinzugefügt. Dies wird so lange gemacht, wie die Punkte
        maximal $\varepsilon$ von einem Punkt im Cluster entfernt sind.
        Dann wird ein bisher nicht betrachteter Punkt als genommen und man
        macht für diesen Outlier / neuen Cluster so weiter wie zuvor.

        <ul>
            <li>ControlList (Priority Queue) enthält nur Objekte, die noch
                nicht in der Output-Liste sind.</li>
            <li>Kriterium: Minimale reachability-distanz zu Objekten in der
                Output-Liste.</li>
            <li>Rekursiv expandieren wie bei DBSCAN.</li>
        </ul>

        Siehe <a href="http://www.dbs.informatik.uni-muenchen.de/Publikationen/Papers/OPTICS.pdf">OPTICS: Ordering Points To Identify the Clustering Structure</a>.
    </dd>
    <dt><dfn>Reachability-Plot</dfn> (<dfn>Erreichbarkeitsdiagramm</dfn>)</dt>
    <dd>Der Reachability-Plot veranschaulicht die Cluster und zeigt, welche
        Wahl von $\varepsilon$ zu verschiedenen Clustern in DBSCAN führen würde.
        Er veranschaulicht das Ergebnis von OPTICS.

        <figure class="wp-caption aligncenter img-thumbnail">
            <a href="https://commons.wikimedia.org/wiki/File:OPTICS.svg"><img src="../images/2016/04/optics.png" alt="OPTICS" /></a>
            <figcaption class="text-center">OPTICS: Der Reachability-Plot ist ganz unten.</figcaption>
        </figure>

    </dd>
    <dt><dfn id="em">EM-Algorithmus</dfn> (<dfn>Expectation Maximization</dfn>)</dt>
    <dd>Siehe <a href="https://martin-thoma.com/machine-learning-2-course#em-algorithmus">ML 2</a>.</dd>
    <dt><dfn>Overall Likelihood</dfn></dt>
    <dd>Die Overall Likelihood ist ein Gütemaß für Clusterings.
        $$\prod_{i} \left ( p_A P(x_i | A) + p_B P(x_i | B) \right )$$</dd>
</dl>

Verfahren im Überblick:

Im Folgenden sei $k \in \mathbb{N}$ die Anzahl der Cluster, $d \in \mathbb{N}$
die Dimension der $n \in \mathbb{N}$ Datenpunkte.

<table class="table" id="clustering-overview">
    <tr>
        <th>Algorithm</th>
        <th>Parameters</th>
        <th>Category</th>
        <th>Complexity</th>
        <th>Comment</th>
    </tr>
    <tr>
        <td><a href="#k-means">$k$-means</a></td>
        <td>$k$</td>
        <td>next neighbor based</td>
        <td>$\mathcal{O}(dkni)$</td>
        <td>$i$ is the number of iterations</td>
    </tr>
    <tr>
        <td>$k$-medoids</td>
        <td>$k$</td>
        <td>next neighbor based</td>
        <td>$\mathcal{O}(dkni)$</td>
        <td>$i$ is the number of iterations</td>
    </tr>
    <tr>
        <td><a href="#em">EM</a></td>
        <td>$k$, distribution-type</td>
        <td>probabilisitc</td>
        <td>O(dkni)</td>
        <td>i is the number of iterations</td>
    </tr>
    <tr>
        <td><a href="#dbscan">DBSCAN</a></td>
        <td>$\varepsilon$, min-points</td>
        <td>density-based</td>
        <td>$\mathcal{O}(n \log n)$</td>
        <td>requires existing index structure which executes neighborhood-query in log n</td>
    </tr>
    <tr>
        <td><a href="#optics">OPTICS</a></td>
        <td>$\varepsilon$, min_points</td>
        <td>density-based</td>
        <td>$\mathcal{O}(n \log n)$</td>
        <td>$\varepsilon$ heavily influences the runtime</td>
    </tr>
    <tr>
        <td><a href="#diana">DIANA</a></td>
        <td></td>
        <td>hierarchical</td>
        <td>$\mathcal{O}(n)$</td>
        <td></td>
    </tr>
    <tr>
        <td><a href="#birch">BIRCH</a></td>
        <td>$k$, branching factor $B$, threshold $T$</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><a href="#clarans">CLARANS</a></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>


### Statistische Modellierung

Slides: `10-StatistModellierung.pdf`

<dl>
    <dt><dfn>Naive Baies</dfn></dt>
    <dd>$$P(H | E) = \frac{P(E_1 | H) \cdot \dots \cdot P(E_n | H) \cdot P(H)}{P(E)}$$</dd>
    <dt><dfn>Laplace-Smoothing</dfn></dt>
    <dd>Um Wahrscheinlichkeiten von 0 zu vermeiden, werden die Zähler mit $k$ initilisiert.
        Beachte, dass man auch die Gesamtzahl dann um $k$ erhöhen muss.</dd>
    <dt><dfn>Bayessche Netze</dfn></dt>
    <dd>Siehe <a href="https://martin-thoma.com/machine-learning-1-course/#bayes-net">ML 1</a>.</dd>
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
    <dd>Model $y = M x$, wobei $x \in \mathbb{R}^n$ die Features sind,
        $y \in \mathbb{R}^m$ die Vorhersage und $M \in \mathbb{R}^{n \times m}$
        die Modellparameter.</dd>
    <dt><dfn>Cross Entropy Fehlermaß</dfn></dt>
    <dd>$$E_{CE}(w) = \sum_{i=1}^n [(1-y_i) \cdot \log (1-p) + y_i \cdot \log p]$$</dd>
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
        <li>Wahrscheinlichkeiten können genauer geschätzt werden</li>
    </ul>

    Typische Techniken sind Bagging und Boosting.</dd>
    <dt><dfn>Bagging</dfn></dt>
    <dd>Ensemble-Learning Technik, bei der Stichproben des
        Trainingsdatenbestandes für die Classifier verwendet werden.
    </dd>
    <dt><dfn>MetaCost</dfn></dt>
    <dd>MetaCost ist ein Verfahren zum Relabeling (TODO: Was ist Relabeling?).
        MetaCost wendet Bagging an.<br/>
        <br/>
        <a href="http://dl.acm.org/citation.cfm?id=312220">MetaCost: a general method for making classifiers cost-sensitive</a> (<a href="http://www.shortscience.org/paper?bibtexKey=conf/kdd/Domingos99">summary</a>)
    </dd>
    <dt><dfn>Boosting</dfn></dt>
    <dd>Boosting ist eine Ensemble-Learning-Technik, die mehrere Modelle vom
        gleichen Typ durch Voting / Durchschnittsberechnung kombiniert. Dabei
        nimmt Boosting Rücksicht auf zuvor falsch Klassifizierte Beispiele
        und gewichtet diese stärker.

        Gewichtungsänderung für korrekte Objekte bei Fehllerrate e: $\frac{e}{1-e}$</dd>
</dl>


## Prüfungsfragen

* Was ist Overfitting?<br/>
  → Siehe <a href="https://martin-thoma.com/machine-learning-1-course/#overfitting">ML 1</a>
* Wie berechnet man die Covarianz zweier Zufallsvariablen <span markdown="0">$X, Y$</span>?<br/>
  → <span markdown="0">$\operatorname{Cov}(X,Y) := \operatorname E\bigl[(X - \operatorname E(X)) \cdot (Y - \operatorname E(Y))\bigr]$</span>
* Warum muss man für NN-Anfragen mit kD-Bäumen nur ein paar Rechtecke anschauen?<br/>
  → Weil man mit der Priority-Queue Algorithmus nur Rechtecke betrachten muss,
    die von der Sphäre, welchen durch den Anfragepunkt un den tatsächlichen
    nachsten Nachbarn gebildet wird, geschnitten werden.
* Warum kann man für räumliche Anfragen nicht ohne weiteres auswerten, wenn man
  für jede Dimension separat einen B-Baum angelegt hat?<br/>
  → TODO: Fragestellung nicht klar. War B-Baum und nicht R-Baum / kdB-Baum gemeint?
* Wie ist ein R-Baum aufgebaut?<br/>
  → Siehe <a href="#r-tree">oben</a>.
* Wie funktioniert die Suche nach dem nächsten Nachbarn mit dem R-Baum?<br/>
  → Man fügt den Wurzel-Knoten in eine Priority-Queue ein. Die Priority-Queue
    ist eine Min-Queue mit dem Abstand vom Anfragepunkt. Es wird im folgenden
    so lange das höchstpriore Objekt aus der Queue entfernt
* Was ändert sich, wenn die Objekte eine räumliche Ausdehnung haben?<br/>
  → Man splittet nach mehreren Dimensionen.
* Stören uns Überlappungen von Knoten des R-Baums? Wenn ja, warum?<br/>
  → Ja, weil die Suche nach dem nächsten Nachbarn ineffizienter wird. Es müssen
     gegebenenfalls mehr Knoten betrachtet werden.
* Wie unterscheiden sich R-Baum, kD-Baum und kDB-Baum?<br/>
  → R-Bäume partitionieren im gegensatz zu kD- und kDB-Bäumen den Datensatz
    nicht. kDB-Bäume sind im Gegensatz zu kD-Bäumen auf physischer Ebene
    balanciert.
* Wie funktioniert das Einfügen in den R-Baum, inklusive Split?<br/>
  → Siehe <a href="https://github.com/MartinThoma/algorithms/blob/master/nearest-neighbor-r-tree/nn_r_tree_pseudo.py#L29">Pseudocode</a>
* Was für Anfragen unterstützen die diversen räumlichen Indexstrukturen?<br/>
  → Nearest-Neighbor, Bereichsanfragen, Punktanfrage
* `3-Informatik-Grundlagen.pdf`, Folie 19
* Warum werden bei der NN-Suche nur genau die Knoten inspiziert, deren Zonen
  die NN-Sphere überlappen?<br/>
  → Weil alle anderen Knoten in der Priority Queue weiter hinten liegen.
* Welche Classifier kennen Sie?<br/>
  → Decision Stumps (1-Rules), Entscheidungsbäume, SVMs, Neuronale Netze, <span markdown="0">$k$</span>-nearest neighbor (es gibt <a href="https://martin-thoma.com/comparing-classifiers/">mehr Classifier</a>)
* Was ist der Vorteil von Postpruning verglichen mit Prepruning?<br/>
  → Es könnte sein, dass ein Feature nur in Kombination mit einem anderen
    deutliche Vorteile bringt. Dies kann man bei Prepruning nicht erkennen,
    ist bei Postpruning gegebenenfalls jedoch offensichtlich.
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
  → [0, 1]: Die FP-Rate ist definiert als <span
  markdown="0">$\frac{FP}{FP+TN}$</span>. Offensichtlich sind alle Werte
  nicht-negativ, also kann der Bruch nicht negativ werden. Deshalb ist auch der
  Nenner mindestens so groß wie der Zähler. Wenn TN=0 und <span
  markdown="0">$FP \neq 0$</span>, dann ist die FP-Rate gleich 1. Das geht,
  wenn man z.B. immer "True" vorhersagt. Wenn man immer "False" vorhersagt ist
  die FP-Rate gleich 0.
* Wie berechnet man den Korrelationskoeffizienten?
  → vgl. <a href="https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#korrelationskoeffizient">oben</a>
* Was ist die "10-fold cross validation"?<br/>
  → vgl. <a href="https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#cross-validation">oben</a>
* Wie haben wir die Erfolgsquote definiert?<br/>
  → vgl. <a href="https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#erfolgsquote">oben</a>
* Was ist ein Lift Chart?<br/>
  → Ein Lift Chart hat auf der x-Achse den Rang (Top-k) und auf der y-Achse der
     Gewinn. Die x-Achse verläuft von 0 bis 100% und die y-Achse von 0 bis zum
     maximalen Gewinn im Datenbestand. Die Diagonale von (0, 0) nach (100%,
     Maximaler Gewinn) entspricht Raten, alles über der Diagonalen ist positiv.
     Der Lift-Chart muss nicht monoton steigend sein.
* Wie unterscheidet sich ein Lift Chart von der ROC Kurve?<br/>
  → Die ROC-Kurve ist monoton steigend, der Lift-Chart jedoch nicht.
* Was für Fehlerarten gibt es bei Vorhersagen von Klassenzugehörigkeiten?<br/>
  → False-Positive, False-Negative (oder: Konfusionsmatrix)
* Was für Kennzahlen kennen Sie, die diese Fehlerarten sämtlich
  berücksichtigen?<br/>
  → F score und Gesamtfehler.
* Was ist Unterschied zwischen Kovarianz und dem Korrelationskoeffizienten?<br/>
  → Der Korrelationskoeffizient ist normiert (vgl. <a href="https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#korrelationskoeffizient">oben</a>)
* Warum kommt bei der informational loss Funktion die Logarithmusfunktion zur
  Anwendung?<br/>
  → Die Logarithmusfunktion hat die gewünschte Form: Bei perfekter
     Klassifizierung soll der Loss gleich 0 sein. Wenn es nicht perfekt ist,
     also $0 \leq p_i < 1$, dann soll der Loss streng monoton fallen.


### Association Rules
* Was sind Association Rules?<br/>
  → Association Rules sind im Kontext von Transaktionen von Items zu verstehen.
     Eine Association Rule ist eine Regel <span markdown="0">$A \Rightarrow B$</span>,
     wobei A und B Item-Mengen sind.
* Wie findet man Association Rules?<br/>
  → In der Warenkorbanalyse / in Transaktionen.
* Wie überprüft man rasch für viele Transaktionen, welche Kandidaten sie enthalten?<br/>
  → TODO
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule
  <span markdown="0">$A \Rightarrow B$</span> hohen
  <a href="#support">Support</a> und hohe <a href="#confidence">Confidence</a>
  hat?<br/>
  → Viele Transaktionen müssen <span markdown="0">$A \cup B$</span> enthalten.
     Wenn <span markdown="0">$A$</span> vorkommt, muss auch
     <span markdown="0">$B$</span> häufig vorkommen.
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule
  <span markdown="0">$A \Rightarrow B$</span> hohen
  Support und geringe Confidence hat?<br/>
  → Viele Transaktionen müssen <span markdown="0">$A \cup B$</span>
  enthalten, aber noch deutlich mehr nur $A$.
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule
  <span markdown="0">$A \Rightarrow B$</span>
  geringen Support und hohe Confidence hat?<br/>
  → Wenige Transaktionen müssen <span markdown="0">$A \cup B$</span>
  enthalten, wenn <span markdown="0">$A$</span> mal vorkommt, dann immer
  auch <span markdown="0">$B$</span>.
* Wie muss der Datenbestand beschaffen sein, damit eine Association Rule
  <span markdown="0">$A \Rightarrow B$</span>
  geringen Support und geringe Confidence hat?<br/>
  → Wenige Transaktionen müssen <span markdown="0">$A \cup B$</span>
  enthalten. Wenn <span markdown="0">$A$</span> mal vorkommt, dann sehr
  selten auch <span markdown="0">$B$</span>.
* Im Apriori-Algorithmus hat man bei k=2 keinen Prune-Schritt. Warum?<br/>
  → (Antwort: 24.11.2015, 14:34)
* Wie groß sollte man die Hash-Tabelle machen?<br/>
  → So groß wie sinnvoll möglich. Der verfügbare Arbeitsspeicher ist hier eine
  Grenze.
* Was sind multidimensionale Association Rules?<br/>
  → Association Rules die auf verschiedenen Begriffsebenenen sind, z.B.
    <span markdown="0">Oreo $\Rightarrow$ Milch</span>
* Wie findet man multidimensionale Association Rules?<br/>
  → TODO
* In welchen Situationen ist Apriori teuer, und warum?<br/>
  → Apriori ist teuer, wenn es sehr große Itemsets gibt. Dann müssen alle
     darin enthaltenen Itemsets gebildet werden.
* Was kann man gegen die Schwächen von Apriori tun?<br/>
  → Laufzeit: Hash-Filter, FP-Trees, Apriori-B, Sampling; TODO
* Was sind FP-Trees, und wie lassen sie sich für die Suche nach Frequent Itemsets verwenden?<br/>
  → Erklärung von <a href="#fp-tree">FP-Trees</a>
* Was kann man tun, wenn FP-Trees für den Hauptspeicher zu groß sind?<br/>
  → TODO (Sampling, Projektion)
* Was ist Constraint-basiertes Mining? Was sind die Vorteile?<br/>
  → TODO
* Was für Arten von Constraints kennen sie? Beispiele hierfür.<br/>
  → TODO
* Was ist Anti-Monotonizität, Succinctness? <Für ein bestimmtes Constraint sagen/begründen, ob anti-monoton/succinct.><br/>
  → TODO
* Wie lässt sich Apriori für das Mining von Teilfolgen verallgemeinern?<br/>
  → TODO
* Antagonismus von Support-basiertem und Constraint-basiertem Pruning erklären können.<br/>
  → TODO
* Alternativen für Constraint-basiertes Pruning (wenn Constraint nicht anti-monoton) erklären können.<br/>
  → TODO
* Welche zwei Sprachen haben wir für die Formulierung der Constraints
  kennengelernt?<br/>
  → 1-var und 2-var bzw. MetaRule Guided
* Warum ist SQL nicht geeignet um Constraints zu formulieren?<br/>
  → Weil SQL keine Aussage über die Struktur machen kann (TODO)

### Clustering
* BIRCH-Algorithmus: Wie kann man die Interclusterdistanz aus N, LS, SS
  herleiten?<br/>
  → $R(C_i) = \sqrt{\frac{1}{N} (SS - 2 \frac{LS}{N} \cdot LS + N (\frac{LS}{N})^2)}$
* BIRCH-Algorithmus: Wie kann man den Durchmesser aus N, LS, SS herleiten?<br/>
  → $\sqrt{\frac{1}{N \cdot (N-1)} (N \cdot SS - 2 LS^2 + N^2 \cdot SS)}$
* BIRCH-Algorithmus: Wie kann man die Interclusterdistanz aus N, LS, SS
  herleiten?<br/>
  → $D(C_1, C_2) = \sqrt{\frac{SS_{C_1} - 2 LS_{C_2} LS_{C_1} + SS_{C_2}}{N_{C_1} \cdot N_{C_2}}}$
* BIRCH-Algorithmus: Wie lassen sich die Clustering-Features eines Zusammengefügten
  Clusters <span markdown="0">$C_{12} = C_1 \cup C_2$</span> aus den
  Komponenten berechnen?<br/>
  → Durch Addition der jeweiligen Features der Einzelcluster.
* Was spricht dagegen, <span markdown="0">$\mathbf{\varepsilon}$</span> in
  OPTICS riesig zu wählen?<br/>
  → Dann sind gleich am Anfang mit dem ersten Objekt alle Datenobjekte in der
     Priority-Queue. Damit wäre der Aufwand für die Queue zu hoch.
* Welche Clustering-Verfahren kennen Sie?<br/>
  → <a href="#k-means">$k$-means</a>, <a href="#clarans">CLARANS</a>,
     <a href="#dbscan">DBSCAN</a>, <a href="#optics">OPTICS</a>,
     <a href="#birch">BIRCH</a>, <a href="#diana">DIANA</a>, <a href="#em">EM</a>
* Gegeben Szenario X, welche Clustering-Verfahren sind sinnvoll, und warum?<br/>
  → Autohersteller will Anzahl der Teile minimieren um Kosten zu senken
    (Hierarchisches Clustering), finden von neuen Symbolen (TODO).
* Warum funktionieren herkömmliche Clustering-Verfahren in hochdimensionalen
  Merkmalsräumen nicht? Skizzieren Sie eine mögliche Lösung.<br/>
  → TODO
* Erklären Sie, warum Clustering mit kategorischen Attributen besonders ist?
  Warum ist Link-basiertes Clustering hier hilfreich?<br/>
  → TODO

### Bayes

* <Gegeben ein beispielhafter Datenbestand, vergleichbar mit dem
auf Folie 10, Vorhersage mit Naive Bayes erklären/vorführen können.><br/>
  → TODO
* Was ändert sich, wenn die Attribute nicht voneinander unabhängig sind?<br/>
  → TODO


## Übungen

Kommt noch.

## Material und Links

Die Vorlesung wurde gestreamt und ist unter
[mml-streamdb01.ira.uka.de](http://mml-streamdb01.ira.uka.de/) verfügbar.

* [Vorlesungswebsite](https://dbis.ipd.kit.edu/2261.php)
* [Ilias](https://ilias.studium.kit.edu/goto_produktiv_crs_477914.html)

Literatur:

* Harvey J. Miller,Jiawei Han: Geographic Data Mining and Knowledge Discovery
  (Clustering)


## Vorlesungsempfehlungen

Folgende Vorlesungen sind ähnlich:

* [Analysetechniken großer Datenbestände](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/)
* [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/)
* [Machine Learning 2](https://martin-thoma.com/machine-learning-2-course/)
* [Mustererkennung](https://martin-thoma.com/mustererkennung-klausur/)
* [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)
* Lokalisierung Mobiler Agenten

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
