---
layout: post
title: Machine Learning 1
author: Martin Thoma
date: 2015-11-09 16:02
categories:
- German posts
tags:
- Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Machine Learning 1&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://www.fzi.de/wir-ueber-uns/organisation/mitarbeiter/address/39/?no_cache=1">Herrn Prof. Dr. Zöllner</a> im Wintersemester 2014/2015 gehört.<br/>Es gibt auch einen Artikel über <a href="//martin-thoma.com/machine-learning-2-course/">Machine Learning 2</a></div>

## Folien

### Einordnungskriterien

Slide name: `ML-Einordnungskriterien.pdf`

* **Inferenztyp**: Induktiv (version-space Algorithmus, k-NN, CBR, ID3, ID5R, von Beispielen auf allgemeine Regel "raten") ↔ Deduktiv (Erklärungsbasierte Generalisierung; Von allgemeinen auf spezielles)
* **Lernebene**: symbolisch (Special-to-General Konzeptlernen, CBR, ID3, ID5R; Semantik in Daten von der der Algorithmus Gebrauch macht) ↔ subsymbolisch (Neuronale Netze, k-NN; Daten sind Signale)
* **Lernvorgang**: überwacht (k-NN, CBR, ID3, ID5R) ↔ unüberwacht (k-Means)
* **Beispielgebung**: inkrementell (Version Space Algorithmus, CBR, ID5R) ↔ nicht inkrementell (k-Means, k-NN, ID3)
* **Beispielumfang**: umfangreich (Neuronale Netze, k-NN, ID3, ID5R) ↔ gering (CBR)
* **Hintergrundwissen**: empirisch (SVMs, k-NN, CBR, ID3, ID5R) ↔ axiomatisch (Erklärungsbasierte Generalisierung)

### Einführung

Slide name: `MLI_01_Einfuehrung_slides1.pdf`

* Was ist Intelligenz? (Problemlösen, Erinnern, Sprache, Kreativität,
  Bewusstsein, Überleben in komplexen Welten, )
* Wissensrepräsentation:
    * Assoziierte Paare (Eingangs- und Ausgangsvariablen)
    * Entscheidungsbäume (Klassen diskriminieren)
    * Parameter in algebraischen ausdrücken
    * Formale Grammatiken
    * Logikbasierte Ausdrücke
    * Taxonomien
    * Semantische Netze
    * Markov-Ketten

<dl>
  <dt><dfn>Machine Learning</dfn> von Tom Mitchell</dt>
  <dd>A computer program is said to learn from experience E with respect to
      some class of tasks T and performance measure P, if its performance at
      tasks in T, as measured by P, improves with experience E.</dd>
  <dt><dfn>Deduktion</dfn></dt>
  <dd>Die Deduktion ist eine Schlussfolgerung von gegebenen Prämissen auf die
      logisch zwingenden Konsequenzen. Deduktion ist schon bei Aristoteles als
      „Schluss vom Allgemeinen auf das Besondere“ verstanden worden.</dd>
  <dt><dfn>Modus ponens</dfn></dt>
  <dd>Der Modus ponens ist eine Art des logischen Schließens. Er besagt: Wenn
      die Prämissen \(A \rightarrow B\) und \(A\) gelten, dann gilt auch \(B\).</dd>
  <dt><dfn>Abduktion</dfn> by Peirce</dt>
  <dd>Deduction proves that something must be; Induction shows that something
      actually is operative; Abduction merely suggests that something may
      be.</dd>
</dl>


### Induktives Lernen

Slide name: `MLI_02_InduktivesLernen_slides1.pdf`

* Konzept: Beschreibt Untermenge von Objekten oder Ereignissen definiert auf
  größerer Menge.
* Konsistenz: Keine negativen Beispiele werden positiv klassifiziert.
* Vollständigkeit: Alle positiven Beispiele werden als positiv klassifiziert.
* Algorithmen: Bäume (Wälder?)
    * Suche vom Allgemeinen zum Speziellen: Negative Beispiele führen zur Spezialisierung
    * Suche vom Speziellen zum Allgemeinen: Positive Beispiele führen zur Verallgemeinerung
    * [Version Space](https://de.wikipedia.org/wiki/Versionsraum): Beides gleichzeitig anwenden
* Präzendenzgraphen: In welcher Reihenfolge werden Aktionen ausgeführt?

Version Space Algorithmus ist:

* Induktiver Inferenztyp
* Symbolische Ebene des Lernens
* Überwachtes Lernen
* Inkrementelle Beispielgebung
* Umfangreich (viele Beispiele)
* Empirisches Hintergrundwissen
* Voraussetzungen: Konsistente Beispiele, korrekte Hypothese im Hypothesenraum
* Positive Aspekte:
  * Es ist feststellbar, welche Art von Beispielen noch nötig ist
  * Es ist feststellbar, wann das Lernen abgeschlossen ist

Weiteres

<dl>
  <dt><dfn>Inductive bias</dfn></dt>
  <dd>Induktives Lernen benötigt Vorannahmen.</dd>
  <dt><dfn>Bias</dfn> ("Vorzugskriterium")</dt>
  <dd>Vorschrift, nach der Hypothese gebildet werden.</dd>
</dl>


### Reinforcement Learning

Slide name: `MLI_03_ReinforcementLearning_slides1.pdf`

<dl>
  <dt><a href="https://en.wikipedia.org/wiki/Reinforcement_learning"><dfn>Reinforcement Learning</dfn></a> (<dfn>RL</dfn>, <dfn><a href="https://de.wikipedia.org/wiki/Best%C3%A4rkendes_Lernen">Bestärkendes Lernen</a></dfn>)</dt>
  <dd>Beim bestärkenden Lernen ist man in einem
      <a href="https://de.wikipedia.org/wiki/Markow-Entscheidungsproblem">Markow-Entscheidungsproblemen</a>.
      Es gibt also einen Agenten, der Aktionen ausführen kann. Diese können
      (nicht notwendigerweise sofort) bewertet werden.</dd>
</dl>

* Beispiel für RL: Roboter muss zu einem Ziel navigieren

Algorithmen:

* Policy Learning
* Simple Value Iteration
* Simple Temporal Difference Learning
* [TD-Learning](https://de.wikipedia.org/wiki/Temporal_Difference_Learning) (Temporal Difference Learning): TODO - wo genau ist der Unterschied zum Q-Learning?

#### Q-Learning
* [Q-learning](https://en.wikipedia.org/wiki/Q-learning)
    * [YouTube: Lecture 18: RL Part 1: Q-Learning](https://www.youtube.com/watch?v=yS5F_vm9Ahk): 1:16:11. BrownCS141 Spring 2014.
    * [YouTube: PacMan](https://www.youtube.com/watch?v=3sLV0OJLdns)

Pseudocode:

```text
initialize Q[num_states, num_actions]
start in state s
repeat:
    select and execute action a
    observe reward r and new state s'
    Q[s', a] <- Q[s, a] + \alpha (r + \gamma \max_{a'} Q[s', a'] - Q[s, a])
    s <- s'
```

where \(\alpha \in (0, 1]\) is a learning rate and \(\gamma\) is a discount
factor.


#### Siehe auch

* [Optimalitätsprinzip von Bellman](https://de.wikipedia.org/wiki/Optimalit%C3%A4tsprinzip_von_Bellman)
* Guest Post (Part I): [Demystifying Deep Reinforcement Learning](http://www.nervanasys.com/demystifying-deep-reinforcement-learning/)


### Lerntheorie

Slide name: `MLI_04_Lerntheorie_slides1.pdf`

<dl>
  <dt><dfn>Ockhams Rasiermesser</dfn> (Quelle: <a href="https://de.wikipedia.org/wiki/Ockhams_Rasiermesser">Wikipedia</a>)</dt>
  <dd>Von mehreren möglichen Erklärungen für ein und denselben Sachverhalt ist
  die einfachste Theorie allen anderen vorzuziehen. Eine Theorie ist einfach,
  wenn sie möglichst wenige Variablen und Hypothesen enthält, und wenn diese in
  klaren logischen Beziehungen zueinander stehen, aus denen der zu erklärende
  Sachverhalt logisch folgt.</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Structural_risk_minimization"><dfn>Structural Risc Minimization</dfn></a> (<dfn>SRM</dfn>)</dt>
  <dd>Unter <i>Structural risk minimization</i> versteht man die Abwägung
      zwischen einem einfachen Modell und einem komplexen Modell, welches
      auf den Trainingsdaten besser funktioniert aber eventuell mehr unter
      Overfitting leidet.</dd>
  <dt><dfn>Vapnik-Chervonenkis Dimension</dfn> (<dfn>VC-Dimension</dfn>)</dt>
  <dd>Die VC-Dimension \(VC(H^\alpha)\) eines Hypothesenraumes \(H^\alpha\)
      ist gleich der maximalen Anzahl an Datenpunkten, die von \(H^\alpha\)
      beliebig separiert werden können.</dd>
</dl>

* Lernmaschine wird definiert durch Hypothesenraum \\(\{h_\alpha: \alpha \in A\}\\)
  und Lernverfahren. Das Lernverfahren ist die Methode um \\(\alpha_{\text{opt}}\\)
  mit Hilfe von Lernbeispielen zu finden.
* Probleme beim Lernen:
    * Größe des Hypothesenraums im Vergleich zur Anzahl der Trainingsdaten.
    * Das Verfahren könnte nur suboptimale Lösungen finden.
    * Das Verfahren könnte die passende Hypothese nicht beinhalten.
* Lernproblemtypen: Sei die Menge der Lernbeispiele in \\(X \times Y\\), mit \\(X \times Y =\\)...
    * \\(\\{Attribut_1, Attribut_2, ...\\} \times \\{True, False\\}\\): Konzeptlernen
    * \\(\mathbb{R}^n \times \\{Klasse_1, ..., Klasse_n\\}\\): Klassifikation
    * \\(\mathbb{R}^n \times \mathbb{R}\\): Regression
* Gradientenabstieg, Overfitting
* Kreuzvalidierung
* Bootstrap: TODO (Folie 18 - 20)
* <a href="https://en.wikipedia.org/wiki/Probably_approximately_correct_learning">Probably approximately correct learning</a>
    * Folie 35: Was ist eine Instanz der Länge \\(n\\)? (TODO)
* VC-Dimension
    * Folie 44: Was ist \\(\eta\\)? (TODO)
* TODO: Wie hängen PAC und VC-Dimension zusammen?

#### Boosting
<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Boosting"><dfn>Boosting</dfn></a></dt>
  <dd>Kombiniere mehrere schwache Modelle um ein gutes zu bekommen, indem
      Trainingsbeispiele unterschiedlich gewichtet werden.</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Bootstrap_aggregating"><dfn>Bagging</dfn></a> (<dfn>Bootstrap aggregating</dfn>)</dt>
  <dd>Kombiniere mehrere schwache Modelle um ein gutes zu bekommen. Dabei
      bekommt jedes schwache Modell nur eine Teilmenge aller Trainingsdaten.</dd>
  <dt><dfn>AdaBoost</dfn> (<dfn>Adaptive Boosting</dfn>)</dt>
  <dd>Learn a classifier for data. Get examples where the classifier got it
      wrong. Train new classifier on the wrong ones.</dd>
</dl>

* Fragen zu Folie 20:
    * Sind die Datensätze disjunkt?
    * TODO: Verstehe Algorithmus nicht.
* Folie 22:
    * Wofür steht \\(i\\) und welchen Wertebereich hat \\(i\\)?
    * Stellt \\(W_k(i)\\) die Wahrscheinlichkeit dar, dass Beispiel \\(i\\) im \\(k\\)-ten
      Durchlauf für das Training verwendet wird?


Siehe auch:

* Alexander Ihler: <a href="https://www.youtube.com/watch?v=ix6IvwbVpw0">AdaBoost</a>.


{% caption align="aligncenter" width="500" alt="Ensemble Learning Techniques: Boosting, Bagging, Random Subspaces, Pasting, Random Patches" text="Ensemble Learning Techniques: Boosting, Bagging, Random Subspaces, Pasting, Random Patches" url="../images/2015/12/ml-ensemble-learning.png" %}


#### VC-Dimension

<dl>
  <dt>VC-Dimension</dt>
  <dd>Sei \(H^\alpha = \{h_\alpha : \alpha \in A\}\) der Hypothesenraum. Die
      VC-Dimension \(VC(h_\alpha)\) von \(H^\alpha\) ist gleich der maximalen
      Anzahl von beliebig platzierten Datenpunkten, die von \(H^\alpha\) separiert
      werden können.</dd>
</dl>

* TODO - Folie 39: Was ist \\(A\\)? Warum ist \\(h_\alpha\\) wichtig? Sollte es
  nicht eher \\(VC(H^\alpha)\\) sein?


### Neuronale Netze

Slide name: `MLI_05_Neuronale_Netze_slides1.pdf`

Siehe auch [Neuronale Netze - Vorlesung](//martin-thoma.com/neuronale-netze-vorlesung/)

* Einsatzfelder:
    * Klassifiktion: Spracherkennung, Schrifterkennung
    * Funktionsapproximation
    * Mustervervollständigung: Kodierung, Bilderkennung (TODO: Warum zählt das nicht zu Klassifikation?)
* Perzeptron von Rosenblatt (1960)
    * Auswertung: Input-Vektor und Bias mit Gewichten multiplizieren, addieren und Aktivierungsfunktion anwenden.
    * Training: Zufällige Initialisierung des Gewichtsvektors, addieren von fehlklassifizierten Vektoren auf Gewichtsvektor.
* Gradientenabstieg
* Delta-Regel
* Kernel-Methoden (TODO)
* Radial-Basis Funktion Netz (TODO)
* <abbr title="Resilient Propagation">RPROP</abbr>: TODO


### Instanzbasiertes Lernen

Slide name: `MLI_06_InstanzbasiertesLernen_slides1.pdf`

<dl>
  <dt><dfn>Instanzenbasiertes Lernen</dfn> bzw. <dfn>Lazy Learning</dfn></dt>
  <dd>Instanzenbasiertes Lernen ist ein Lernverfahren, welches einfach nur
      die Beispiele abspeichert, also faul (engl. lazy) ist. Soll der Lerner
      neue Daten klassifizieren, so wird die Klasse des ähnlichsten
      Datensatzes gewählt.</dd>
  <dt><dfn>Case-based Reasoning</dfn> bzw. kurz <dfn>CBR</dfn></dt>
  <dd>CBR ist ein allgemeines, abstraktes Framework und kein direkt anwendbarer
      Algorithmus. Die Idee ist, dass nach ähnlichen, bekannten Fällen gesucht
      wird, auf die der aktuelle Fall übertragen werden kann.</dd>
  <dt><dfn>Fall</dfn> im Kontext des CBR</dt>
  <dd>Ein Fall ist eine Abstraktion eines Ereignisses, die in Zeit und Raum
      begrenzt ist. Ein Fall enthält eine Problembeschreibung, eine Lösung und
      ein Ergebnis. Zusätzlich kann ein Fall eine Erklärung enthalten warum
      das Ergebnis auftrat, Informationen über die Lösungsmethode, Verweise
      auf andere Fälle oder Güteinformationen enthalten.</dd>
</dl>

* Beispiel für Lazy Learning: <abbr title="k Nearest Neighbors">\(k\)-NN</abbr>,
  <abbr title="Case-based Reasoning">CBR</abbr>

* TODO: Folie 3: „Fleißige“ Lernalgorithmen mit dem gleichen Hypothesenraum sind
  eingeschränkter - was ist damit gemeint?
* TODO: Folie 6 - Was ist CBR?

### SVM

Slide name: `MLI_07_SVM_slides1.pdf`

TODO: Allgemeines Verständnis, mal auf konkrete Fälle anwenden

* SVMs sind laut Vapnik die Lernmaschine mit der kleinsten möglichen VC-
  Dimension, falls die Klassen linear trennbar sind.
* Primäres Optimierungsproblem: Finde einen Sattelpunkt der Funktion<br/>
  \\(L_P = L(\vec{w}, b, \vec{\alpha}) = \frac{1}{2}\|\vec{w}\|^2 - \sum_{i=1}^N \alpha_i (y_i(\vec{w}\vec{x_i}+b)-1)\\)
  wobei \\(\alpha_1, \dots, \alpha_N \geq 0\\) Lagrange-Multiplikatoren sind
* Soft Margin Hyperebene
* Der Parameter $C$ dient der Regularisierung. Ist $C$ groß gibt es wenige
  Missklassifikationen in der Trainingsdatenmenge. Ist $C$ klein, werden die
  Margins größer.
* Nichtlineare Kernelmethoden
* Kernel-Trick


<div class="alert alert-info"><h4>Abschätzung des Testfehlers</h4>
Mit Wahrscheinlichkeit \(P(1-\eta)\) gilt:
\[E(h_\alpha) \leq E_{emp}(h_\alpha) + \sqrt{\dots \frac{VC(h_\alpha)}{N} \dots}\]

wobei gilt:

<ul>
    <li>\(E(h_\alpha)\) ist der reale Fehler der mit der Hypothese \(h_\alpha\)
        gemacht wird</li>
    <li>\(E_{emp}(h_\alpha)\) ist der empirische Fehler der mit der Hypothese \(h_\alpha\)
        gemacht wird</li>
    <li>\(VC(h_\alpha)\) ist die VC-Dimension der Lernmaschine</li>
    <li>\(N\) ist die Anzahl der Lernbeispiele</li>
</ul>

Dieser Term wird in der <i>Structural Risc Minimization</i> minimiert.
</div>


<div class="alert alert-info"><h4>Die fünf Prinzipien von SVMs</h4>
<ol>
    <li>Lineare Trennung mit maximalen Abstand der Trennebenen zu den
        nächstgelegenen Stichproben (Support Vektoren)</li>
    <li>Duale Formulierung des linearen Klassifikators.
        (vgl. <a href="https://de.wikipedia.org/wiki/Support_Vector_Machine#Duales_Problem">Wiki</a>, \(k(m) = w^T m + b = \langle w, m \rangle + b = \sum_{j=1}^N \alpha_j z_j \langle m_j, m \rangle + b\))</li>
    <li>Nichtlineare Abbildung der primären Merkmale in einen hochdimensionalen
        Merkmalsraum \(\Phi\)</li>
    <li>Implizite Nutzung des unter Umständen \(\infty\)-dimensionalen
        Eigenfunktionsraumes einer sog. Kernfunktion \(K\) als transformierten
        Merkmalsraum \(\Phi\). Dabei müssen die transformierten Merkmale nicht
        explizit berechnet werden und der Klassifikator hat trotz der hohen
        Dimension von \(\Phi\) nur eine niedrige Zahl von freien Parametern
        (Kernel-Trick).</li>
    <li>Relaxation der Forderung nach linearer Trennbarkeit durch Einführung
        von Schlupfvariablen (slack variables).</li>
</ol>
</div>


### Entscheidungsbäume

Slide name: `MLI_08_Entscheidungsbaeume_slides1.pdf`

<dl>
  <dt><dfn>Entscheidungsbaum</dfn></dt>
  <dd>Ein Entscheidungsbaum ist ein Klassifikator in Baumstruktur. Die
      inneren Knoten des Entscheidungsbaumes sind Attributtests, die Blätter
      sind Klassen.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/ID3"><dfn>ID3</dfn></a> (siehe <a href="(https://github.com/MartinThoma/LaTeX-examples/tree/master/source-code/Pseudocode/ID3">pseudocode</a>)</dt>
  <dd>ID3 ist ein Top-Bottom Verfahren zum Aufbau eines Entscheidungsbaumes.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/C4.5"><dfn>C4.5</dfn></a> (siehe <a href="(https://github.com/MartinThoma/LaTeX-examples/tree/master/source-code/Pseudocode/ID3">pseudocode</a>)</dt>
  <dd>ID3 ist ein Top-Bottom Verfahren zum Aufbau eines Entscheidungsbaumes, welches auf ID3 basiert.</dd>
  <dt><dfn>Random Forest</dfn>, Quelle: <a href="https://de.wikipedia.org/wiki/Random_Forest">Wikipedia</a></dt>
  <dd>Ein Random Forest ist ein Klassifikationsverfahren, welches aus mehreren
  verschiedenen, unkorrelierten Entscheidungsbäumen besteht. Alle
  Entscheidungsbäume sind unter einer bestimmten Art von Randomisierung während
  des Lernprozesses gewachsen. Für eine Klassifikation darf jeder Baum in
  diesem Wald eine Entscheidung treffen und die Klasse mit den meisten Stimmen
  entscheidet die endgültige Klassifikation.</dd>
</dl>

* Der Algorithmus ID5R dienen dem Aufbau eines Entscheidungsbaumes.
* C4.5 unterstützt - im Gegensatz zu ID3 - kontinuierliche Attributwerte.
  Außerdem kann C4.5 mit fehlenden Attributwerten umgehen.
* Mögliches Qualtitätsmaß ist Entropie:<br/>
  \\(Entropie(S) = - p_\oplus \log_2 p_\oplus - p_\ominus \log_2 p_\ominus\\)
  wobei $\oplus$ die positiven Beispiele und $\ominus$ die negativen Beispiele
  bezeichnet.
* TODO, Folie 41: Wo ist der Vorteil von ID5R im Vergleich zu ID3, wenn das
  Ergebnis äquivalent ist?
* Random Forest: Erstelle mehrere Entscheidungsbäume mit einer zufälligen
  Wahl an Attributen. Jeder Baum stimmt für eine Klasse und die Klasse, für die
  die meisten Stimmen, wird gewählt.


### Bayes Lernen

Slide name: `MLI_09_BayesLernen_slides1.pdf`

<dl>
  <dt><dfn>Satz von Bayes</dfn></dt>
  <dd>Seien \(A, B\) Ereignisse, \(P(B) > 0\). Dann gilt:
      \(P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}\)<br/>
      Dabei wird \(P(A)\) a priori Wahrscheinlichkeit, \(P(B|A)\) likelihood,
      und \(P(A|B)\) a posteriori Wahrscheinlichkeit genannt.</dd>
  <dt><dfn>Naiver Bayes-Klassifikator</dfn></dt>
  <dd>Ein Klassifizierer heißt naiver Bayes-Klassifikator, wenn er den
      Satz von Bayes unter der naiven Annahme der Unabhängigkeit der Features
      benutzt.</dd>
  <dt><dfn>Produktregel</dfn></dt>
  <dd>\(P(A \land B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)\)</dd>
  <dt><dfn>Summenregel</dfn></dt>
  <dd>\(P(A \lor B) = P(A) + P(B) - P(A \land P)\)</dd>
  <dt><dfn>Theorem der totalen Wahrscheinlichkeit</dfn></dt>
  <dd>Es seien \(A_1, \dots, A_n\) Ereignisse mit \(i \neq j \Rightarrow A_i \cap A_j = \emptyset \;\;\;\forall i, j \in 1, \dots, n\) und \(\sum_{i=1}^n A_i = 1\). Dann gilt:<br/>
      \(P(B) = \sum_{i=1}^n P(B|A_i) P(A_i)\)</dd>
  <dt><dfn>Maximum A Posteriori Hypothese</dfn> (MAP-Hypothese)</dt>
  <dd>Sei \(H\) der Raum aller Hypothesen und \(D\) die Menge der beobachteten
      Daten. Dann heißt<br/>
      \(h_{MAP} = \text{arg max}_{h \in H} P(h|D) \cdot P(h)\)<br/>
      die Menge der Maximum A Posteriori Hypothesen.</dd>
  <dt><dfn>Maximum Likelihood Hypothese</dfn> (ML-Hypothese)</dt>
  <dd>Sei \(H\) der Raum aller Hypothesen und \(D\) die Menge der beobachteten
      Daten. Dann heißt<br/>
      \(h_{ML} = \text{arg max}_{h \in H} P(h|D)\)<br/>
      die Menge der Maximum Likelihood Hypothesen.</dd>
  <dt><dfn>Normalverteilung</dfn></dt>
  <dd>Eine stetige Zufallsvariable \(X\) mit der Wahrscheinlichkeitsdichte
      \(f\colon\mathbb{R}\to\mathbb{R}\), gegeben durch<br/>
      \(f(x) = \frac {1}{\sigma\sqrt{2\pi}} e^{-\frac {1}{2} \left(\frac{x-\mu}{\sigma}\right)^2}\)<br/>
      heißt \(\mathcal N\left(\mu, \sigma^2\right)\)-verteilt, normalverteilt
      mit den Erwartungswert \(\mu\) und Varianz \(\sigma^2\).</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Minimum_Description_Length"><dfn>Prinzip der minimalen Beschreibungslänge</dfn></a></dt>
  <dd>Das Prinzip der minimalen Beschreibungslänge ist eine formale
      Beschreibung von Ockhams Rasiermesser. Nach diesem Prinzip werden
      Hypothesen bevorzugt, die zur besten Kompression gegebener Daten führen.
  </dd>
  <dt><dfn>Gibbs-Algorithmus</dfn> (<a href="https://de.wikipedia.org/wiki/Gibbs-Sampling">Wikipedia</a> und <a href="http://stats.stackexchange.com/a/10216/25741">stats.stackexchange</a>)</dt>
  <dd>Der Algorithmus von Gibbs ist eine Methode um Stichproben von bedingten
      Verteilungen zu erzeugen. TODO: Ist das richtig? Wann wird es verwendet?
  </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Bedingte_Unabh%C3%A4ngigkeit"><dfn>Bedingte Unabhängigkeit</dfn></a></dt>
  <dd>Seien \(X, Y, Z\) Zufallsvariablen. Dann heißt \(X\) bedingt unabhängig
      von \(Y\) gegeben \(Z\), wenn \[P(X|Y,Z) = P(X|Z)\] gilt.
  </dd>
  <dt><a href="https://en.wikipedia.org/wiki/Additive_smoothing"><dfn>Add \(k\) smoothing</dfn></a></dt>
  <dd>Unter Add-\(k\)-smoothing versteht man eine Technik, durch die
      sichergestellt wird, dass die geschätzte Wahrscheinlichkeit für kein
      Ereignis gleich null ist. Wenn man \(d \in \mathbb{N}\) mögliche
      Ergebnisse eines Experiments hat, \(N \in \mathbb{N}\) experimente
      durchgeführt werden, dann schätzt man die Wahrscheinlichkeit von dem
      Ergebnis \(i\) mit
      \[\hat{\theta_i} = \frac{x_i + k}{N+ kd}, \]
      wobei \(x_i\) die Anzahl der Beobachtungen von \(i\) ist und \(k \geq 0\)
      der Glättungsparameter ist.
  </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Bayessches_Netz"><dfn>Bayessches Netz</dfn></a></dt>
  <dd>Ein bayessches Netz ist ein gerichteter azyklischer Graph in dem die
      Knoten Zufallsvariablen und die Kanten bedingte Abhängigkeiten
      beschreiben.
  </dd>
</dl>

Fragen:

* Folie 23: Warum ist \\(h_{MAP(x)}\\) nicht die wahrscheinlichste
  Klassifikation?
* Folie 24: Was ist \\(V\\)?


### HMM

Slide name: `MLI_10_HMM_slides1.pdf`

<dl>
  <dt><dfn>Markov-Bedingung</dfn> (Beschränkter Horizont)</dt>
  <dd>\(P(q_{t+1}=S_{t+1}|q_t = S_t, q_{t-1} = S_{t-1}, \dots) = P(q_{t+1}=S_{t+1}|q_t = S_t)\)</dd>
  <dt><dfn>Hidden Markov Modell</dfn> (<dfn>HMM</dfn>)</dt>
  <dd>Eine HMM ist ein Tupel \(\lambda = (S, V, A, B, \Pi)\):
      <ul>
          <li>\(S = \{S_1, \dots, S_n\}\): Menge der Zustände</li>
          <li>\(q_t\): Zustand zum Zeitpunkt \(t\)</li>
          <li>\(V = \{v_1, \dots, v_m\}\): Menge der Ausgabezeichen</li>
          <li>\(A \in [0,1]^{n \times n}\) = (a_{ij}): Übergangsmatrix, die die Wahrscheinlichkeit von Zustand \(i\) in Zustand \(j\) zu kommen beinhaltet</li>
          <li>\(B = (b_{ik})\) die Emissionswahrscheinlichkeit \(v_k\) im Zustand \(S_i\) zu beobachten</li>
          <li>\(\Pi = (\pi_i) = P(q_1 = i)\): Die Startverteilung</li>
      </ul></dd>
  <dt><a href="https://de.wikipedia.org/wiki/Forward-Algorithmus"><dfn>Vorwärts-Algorithmus</dfn></a></dt>
  <dd>Der Vorwärts-Algorithmus löst das Evaluierungsproblem. Er benutzt dazu
      dynamische Programmierung: Die Variablen \(\alpha_t(i) = P(o_1 o_2 \dots o_t; q_t = s_i)\) gibt die Wahrscheinlichkeit
      an zum Zeitpunkt \(t \in 1 \leq t \leq T\) im Zustand \(s_i \in S\) zu
      sein und die Sequenz \(o_1 o_2 \dots o_t\) beobachtet zu haben. Diese
      werden rekursiv berechnet.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Backward-Algorithmus"><dfn>Rückwärts-Algorithmus</dfn></a></dt>
  <dd>Der Rückwärts-Algorithmus löst das Dekodierungsproblem. Er benutzt dazu
      dynamische Programmierung: Die Variablen \(\beta_t(i) = P(o_{t+1} o_{t+2} \dots o_{T}|q_t = s_i, \lambda)\) geben
      die Wahrscheinlichkeit an, dass die Sequenz \(o_{t+1} o_{t+2} \dots o_{T}\)
      beobachtet werden wird, gegeben das HMM&nbsp;\(\lambda\) und den
      Startzustand&nbsp;\(s_i\).</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Viterbi-Algorithmus"><dfn>Viterbi-Algorithmus</dfn></a></dt>
  <dd>Löst P2: TODO</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Baum-Welch-Algorithmus"><dfn>Baum-Welch-Algorithmus</dfn></a></dt>
  <dd>Löst P3: TODO</dd>
  <dt><dfn>Ergodisches Modell</dfn></dt>
  <dd>TODO</dd>
  <dt><dfn>Bakis-Modell</dfn> (<dfn>Links-nach-Rechts-Modell</dfn>)</dt>
  <dd>TODO</dd>
</dl>

Die drei Probleme von HMMs sind

* **P1 - Evaluierungsproblem**: Wie wahrscheinlich ist eine Sequenz
  \\(\bf{o} = o_1 o_2 \dots o_T\\)
  gegeben ein HMM \\(\lambda\\), also \\(P(\bf{o}|\lambda)\\).
* **P2 - Dekodierungsproblem**: Finden der wahrscheinlichsten Zustandssequenz,
  gegeben eine Sequenz von Beobachtungen.
* **P3 - Lernproblem**: Optimieren der Modellparameter.


Anwendungen:

* Gestenerkennung
* Phonem-Erkennung


### Markov Logik Netze

Slides: `MLI_11-MLN_slides1`

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Markov_Logik_Netze"><dfn>Markov Logik Netze</dfn></a> (<dfn>MLN</dfn>)</dt>
  <dd>Ein Markov Logik Netz \(L\) ist ein Menge aus Tupeln \((F_i, w_i)\), wobei \(F_i\) eine Formel der Prädikatenlogik erster Ordnung ist und \(w_i \in \mathbb{R}\) ein Gewicht ist.</dd>
</dl>

Siehe auch:

* Matthew Richardson, Pedro Domingos: [Markov logic networks](http://link.springer.com/article/10.1007/s10994-006-5833-1)
* Coursera: [Probabilistic Graphical Models](https://www.coursera.org/course/pgm)
* Pedro Domingos: [Unifying Logical and Statistical AI](https://www.youtube.com/watch?v=bW5DzNZgGxY), September 2009.
* Software: [Alchemy](https://alchemy.cs.washington.edu/)


## Prüfungsfragen

<ul>
    <li>Was ist Induktives Lernen?
        → Eine große Menge an Beispielen wird gegeben. Der Lerner muss selbst
           das Konzept herausfinden.</li>
    <li>Was ist Deduktives Lernen?
        → Fakten werden gegeben. Der lernende bekommt das allgemeine Konzept
           gesagt und muss nur logische Schlussfolgerungen machen.</li>
    <li>Wie lautet die Bellman-Gleichung?
        → \(Q(s, a) = r + \gamma \max_{a'} Q(s', a')\) wobei \(\gamma\) ein
        Diskontierungsfaktor ist, \(s'\) der Zustand in den man kommt, wenn
        man \(a\) ausführt und \(r\) der Reward nach ausführen von \(a\) in
        \(s\) ist.</li>
    <li>Wie lautet die Fehlerabschätzung von Vapnik?
        → (TODO: Empirischer Fehler / realer Fehler)</li>
    <li>Wie funktioniert Q-Learning?
        → TODO</li>
    <li>Was versteht man unter Cascade Correlation?
        → TODO</li>
</ul>

## Material und Links

* [Vorlesungswebsite](http://cg.ivd.kit.edu/lehre/ws2015/cg/index.php)
* [&Uuml;bungswebsite](http://cg.ivd.kit.edu/lehre/ws2015/cg/uebung.php)
* StackExchange
  * [What is the difference between concept learning and classification?](http://datascience.stackexchange.com/q/8642/8820)
* [Zusammenfassung der Vorlesung ML 2](//martin-thoma.com/machine-learning-2-course/)

## Übungsbetrieb

Es gibt keine Übungsblätter, keine Übungen, keine Tutorien und keine
Bonuspunkte.


## Termine und Klausurablauf

**Datum**: Mündliche Prüfung<br/>
**Ort**: nach Absprache<br/>
**Zeit**: ? min<br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Ergebnisse**: werden ca. 5 - 10 min. nach der Prüfung gesagt<br/>
**Erlaubte Hilfsmittel**: keine
