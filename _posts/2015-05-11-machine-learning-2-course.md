---
layout: post
title: Machine Learning 2
author: Martin Thoma
date: 2015-05-11 11:00
categories:
- German posts
tags:
- Klausur
- Machine Learning
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Machine Learning 2&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://tks.anthropomatik.kit.edu/21_52.php">Herrn Prof. Dr. Marius Zöllner</a> im Sommersemester&nbsp;2015 gehört. <br/>Es gibt auch einen Artikel zu <a href="http://martin-thoma.com/machine-learning-1-course/">Machine Learning 1</a></div>

## Behandelter Stoff

### Einführung

Slides: <a href="https://ilias.studium.kit.edu/ilias.php?ref_id=429607&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">`01_Einfu__hrung_MLII.pdf`</a>

Rückblick auf [ML 1](//martin-thoma.com/machine-learning-1-course/).
MLNN steht übrigens für <i>Multi-Layer Neural Network</i>.


### Semi-Supervised Learning

Slides: <a href="https://ilias.studium.kit.edu/ilias.php?ref_id=432731&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">`02_Semi-supervised-learning.pdf`</a>

<dl>
  <dt><dfn>Überwachtes Lernen</dfn> (engl. <dfn>Supervised Learning</dfn>)</dt>
  <dd>Alle Trainingsdaten liegen mit Labels vor.</dd>
  <dt><dfn>Unüberwachtes Lernen</dfn> (engl. <dfn>Unsupervised Learning</dfn>)</dt>
  <dd>Alle Trainingsdaten liegen ohne Labels vor.</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Semi-supervised_learning"><dfn>Semi-Supervised Learning</dfn></a> (<dfn>SSL</dfn>)</dt>
  <dd>Die meisten Trainingsdaten liegen ohne Labels vor, jedoch gibt es für
      jede Klasse auch gelabelte Daten.</dd>
  <dt><dfn>Self-Learning</dfn> (<dfn>Self-Training</dfn>, <dfn>Self-Labeling</dfn>, <dfn>Decision-directed learning</dfn>)</dt>
  <dd><i>Self-Training</i> ist ein Algorithmus zum Semi-supervised Learning.
      Er geht wie folgt vor:
      <ol>
          <li>Trainiere mit gelabelten Daten.</li>
          <li>Werte ungelabelte Daten aus.</li>
          <li>Füge Daten, bei denen sich der Klassifizierer sicher ist, zu
              den Trainingsdaten hinzu.</li>
          <li>Zurück zu Schritt&nbsp;1.</li>
      </ol>

      Dabei sind folgende Variationen vorstellbar:
      <ul>
          <li>Füge alle Daten hinzu.</li>
          <li>Füge nur Daten hinzu, bei denen sich der Klassifizierer sicher ist.</li>
          <li>Gewichte Daten mit der Sicherheit.</li>
      </ul>
  </dd>
  <dt><dfn>Co-Training</dfn> (<dfn>Mit-Lernen</dfn>)</dt>
  <dd><i>Co-Training</i> ist ein Algorithmus zum Semi-supervised Learning.
      Er geht wie folgt vor:
      <ol>
          <li>Splitte jeden Feature-Vektor auf die gleiche Art in zwei
              Feature-Vektoren mit disjunkten Features auf.</li>
          <li>Trainiere zwei unterschiedliche Klassifizierer auf den beiden
              unterschiedlichen Feature-Mengen der gelabelten Daten.</li>
          <li>Label mit den beiden Klassifizieren die ungelabelten Daten.</li>
          <li>Füge ungelabelte Daten dem Trainingsdatensatz (also den
              gelabelten Daten) hinzu, falls die Klassifizierer für diese eine
              hohe Konfidenz aufweisen.</li>
          <li>Zurück zu Schritt&nbsp;2.</li>
      </ol>

      Dabei sind folgende Variationen vorstellbar:
      <ul>
          <li>Demokratisches Voting: Bei mehr als 2&nbsp;Klassifizierern.</li>
          <li>Schwellwert: Nur hinzufügen, wenn alle Klassifizierer jeweils
              eine Schwelle überschreiten.</li>
          <li>Gewichtes Voting: Alle Klassifizierer zusammen müssen eine
              Schwelle überschreiten.</li>
      </ul>
  </dd>
  <dt><dfn>Low Density Separation</dfn></dt>
  <dd>Methoden, welche Low Density separation benutze versuchen die
      Entscheidungsgrenze in eine Region niedriger Dichte zu legen. Ein Beispiel
      ist die <i>Transductive SVM</i>.</dd>
</dl>

Weiteres:

Hier könnte ich mir gut vorstellen, dass man eine Bachelor / Master-Arbeit
macht. Man könnte sich große gelabelte Datensätze suchen, einen gewissen Teil
der Labels weglassen (also einige Trainingsdaten als "ungelabelt" behandeln)
und die verschiedenen <abbr title="Semi-Supervised Learning">SSL</abbr>-Methoden
untersuchen. Bis zu 20% gelabelte Daten hoch wäre es interessant; also z.B.
(0.5%, 1%, 2%, 3%, 5%, 10%, 15%, 20% gelabelte Daten). Mit mehr gelabelten
Daten könnte man argumentieren, dass man es sich vermutlich leisten könnte auch
den Rest noch zu labeln. Siehe Folie 28-31.


### SSL and Active Learning

Slides: `03_Semi-supervised+Active-learning.pdf`

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Lagrange-Multiplikator"><dfn>Lagrange-Multiplikator</dfn></a></dt>
  <dd>Lagrange-Multiplikatoren sind ein Verfahren der Optimierungstheorie.
      Sie werden genutzt, wenn ein Optimierungsproblem mit Nebenbedingungen
      vorliegt. Durch sie kann die Nebenbedingung eliminiert werden.</dd>
  <dt><dfn>Active Learning</dfn></dt>
  <dd>Die Lernmaschine wählt die zu lernenden Daten selbst aus.</dd>
  <dt><dfn>Query Synthesis</dfn> (siehe <a href="http://burrsettles.com/pub/settles.activelearning.pdf">Active Learning Literature Survey</a>)</dt>
  <dd>Der Lerner kann Feature-Vektoren (Querys)
      <a href="https://en.wikipedia.org/wiki/De_novo">de novo</a>, also von
      Grund auf neu / selbst erzeugen. Er kann für diesen neuen Query ein
      Orakel befragen, was das Label ist.</dd>
  <dt><dfn>Selective Sampling</dfn> (Selektive Entnahme, siehe <a href="http://dl.acm.org/citation.cfm?id=2503327">Selective sampling and active learning from single and multiple teachers</a>)</dt>
  <dd>Selective Sampling ist eine Methode des aktiven Lernens. Dabei wird
      jede Runde \(t\) dem Lerner ein Feature-Vektor \(x_t \in \mathbb{R}^n\)
      präsentiert. Der Lerner muss sich jede Runde entscheiden, ob er einen
      Preis bezahlt um das Label zu sehen. Der Lerner hat also zwei Ziele, die
      miteinander in Konflikt stehen: Er will alles richtig klassifizieren,
      aber zugleich die Kosten so niedrig wie möglich halten.</dd>
  <dt><dfn>Pool-Based Active Learning</dfn></dt>
  <dd>Pool-Based Active Learning ist eine Methode des aktiven Lernens. Dabei
      wird von einem Pool an ungelabelten Daten \(\mathcal{U}\) ausgegangen
      und einem deutlich kleineren Pool \(\mathcal{L}\) an gelabelten Daten.
      Queries werden aus \(\mathcal{U}\) gezogen. Dabei wird ganz
      \(\mathcal{U}\) evaluiert und für den hilfreichsten Feature-Vektor
      \(x \in \mathcal{U}\) nach einem Label gefragt.</dd>
  <dt><dfn>Hinge-Funktion</dfn></dt>
  <dd>\[f(x) = \max(x, 0)\]</dd>
  <dt>Query-by-Committee (<dfn>QBC</dfn>)</dt>
  <dd>Es wird ein Committee \(\mathcal{C}\) an Klassifikatoren trainiert,
      welches gemeinsam (z.B. durch majority vote) eine Klassifikation trifft.

    Allgemeiner Ansatz:
    <ul>
        <li>Trainiere eine Menge \(\mathcal{C}\) an Klassifikatoren</li>
        <li>Wähle neue Daten, wenn die Hypothesen Wiedersprüchlich sind</li>
    </ul>

    Selektive Entnahme:
    <ol>
        <li>Beobachte neue Instanz \(x\) und werte diese mit \(\mathcal{C}\) aus</li>
        <li>Frage das Label ab, falls es einen Wiederspruch in den Hypothesen
            von \(\mathcal{C}\) für \(x\) gibt.</li>
        <li>Neu trainiren, zurück zu 1</li>
    </ol>

    Pool-based Active Learning:
    <ol>
        <li>Messung des Wiederspruchs der Hypothesen für alle Instanzen \(x\)</li>
        <li>Ranking (z.B. Entropie)</li>
        <li>Abfrage der Labels für die \(k\) widersprüchlichsten Instanzen</li>
        <li>Neu trainiren, zurück zu 1</li>
    </ol>
  </dd>
</dl>

Weiteres:

* Ausreißerproblem: Ausreißer sollten im QBC nicht genommen werden. Dazu könnte
  die Dichte im Datenraum gemessen werden.


### Reinforcement Learning

Slides: `04_Reinforcement_Learning_II.pdf`

Siehe auch:

* [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/#tocAnchor-1-1-9)
* [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/#tocAnchor-1-1-4)
* [Cat vs. Mouse code](https://github.com/MartinThoma/cat-vs-mouse)
* Berkeley
    * CS188 Intro to AI: [Project 3: Reinforcement Learning](http://ai.berkeley.edu/reinforcement.html)
    * Dan Klein, Pieter Abbeel: [Lecture 10: Reinforcement Learning](https://www.youtube.com/watch?v=w33Lplx49_A) on YouTube. University of California, Berkeley. This expalins TD-learning.

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Markow-Entscheidungsproblem"><dfn>Markov Decision Process</dfn></a> (<dfn>MDP</dfn>)</dt>
  <dd>Ein Markovscher Entscheidungsprozess ist ein 5-Tupel
      \((S, A, T, r, p_0)\), wobei
      <ul>
          <li>\(S\) eine endliche Zustandsmenge,</li>
          <li>\(A\) eine endliche Menge von Aktionen,</li>
          <li>\(T_a(s, s') = T(s_{t+1}=s'|s_t = s, a_t = a)\) die
              Wahrscheinlichkeit zu einem beliebigen Zeitpunkt von Zustand
              \(s\) mit der Aktion \(a\) in den Zustand \(a'\) zu kommen
              (engl. Transition),</li>
          <li>\(r_a(s, s')\) ist die Belohnung (Reward), die man direkt
              erhält wenn man erhält wenn man von Zustand \(s\) mit Aktion
              \(a\) in Zustand \(s'\) kommt,</li>
          <li>\(p_0\) ist die Startverteilung auf die Zustände \(S\)</li>
      </ul>
  </dd>
  <dt><dfn>Partially observable Markov decision process</dfn> (<dfn>POMDP</dfn>)<a name="pomdp-definition"></a></dt>
  <dd>Ein <i>partially observable Markov decision process</i> ist ein
      7-tupel <span markdown="0">\(S, A, T, R, \Omega, O, \gamma\)</span>, wobei

      <ul>
          <li>\(S\) die Zustandsmenge,</li>
          <li>\(A\) die Aktionsmenge,</li>
          <li>\(T: S \times A \times S \rightarrow \mathbb{R}\) die probabilisitische Zustandsübergangsfunktion (transition function) ist,</li>
          <li>\(R: S \times A \rightarrow \mathbb{R}\) die Reward-Funktion,</li>
          <li>\(\Omega\) die Menge der möglichen Beobachtungen,</li>
          <li>\(O\) die Wahrscheinlichkeit der Beobachtungen, gegeben ein Zustand und eine Aktion und</li>
          <li>\(\gamma \in [0, 1]\) der Diskontierungsfaktor</li>
      </ul>
      ist.
  </dd>
  <dt><dfn>Options</dfn></dt>
  <dd>Eine <i>Option</i> ist wohl-definiertes Verhalten, welches im
      hierarchischen <abbr title="Reinforcement Learning">RL</abbr> eingesetzt
      werden kann. Es ist ein Baustein für komplexe Pläne.
      Options werden in Semi-MDPs eingesetzt und ersetzen dort die
      Aktionen.</dd>
  <dt><dfn>Hierarchien Abstrakter Maschinen</dfn> (<dfn>HAM</dfn>)</dt>
  <dd>Ein <abbr title="Markov Decision Process">MDP</abbr> wird mit
      Maschinen \(\{M_i\}\) kombiniert. Jede Maschine repräsentiert einen
      Teil der Policy. Jede Maschine verwendet eigene Zustände \(m_t^i\)
      und globale Zustände \(s_t\). Maschinen werden durch Zustandsautomaten
      abgebildet.</dd>
  <dt><dfn>MaxQ-Dekomposition</dfn> (siehe [<a href="#ref-die00" name="ref-die00-anchor">Die00</a>])</dt>
  <dd>Das zu lösende MDP \(M\) wird als Menge von Unteraufgaben \(\{M_0, \dots, M_n\}\)
      interpretiert. Dabei ist \(M_0\) das Haupt-MDP.

      TODO.</dd>
</dl>

Folie 35:

* NODO: Was heißt hier "mit festen Knoten"?


### <a name="dynamic-bayes-networks"></a>Dynamische Bayessche Netze

Slides: `05_DynamischeBayesscheNetze.pdf`

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Bedingte_Wahrscheinlichkeit#Multiplikationssatz"><dfn>Multiplikationssatz</dfn></a></dt>
  <dd>Seien \(A, B, X_i\) Ereignisse. Dann gilt:
      \[P(X_1, \dots, X_n) = P(X_1) \cdot \prod_{k=2}^n P(X_k | X_{k-1}, \dots, X_1)\]
      und insbesondere
      \[P(A\cap B) = P(A, B) = P(A\mid B) \cdot P(B)\]</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Bedingte_Wahrscheinlichkeit#Gesetz_der_totalen_Wahrscheinlichkeit"><dfn>Gesetz der totalen Wahrscheinlichkeit</dfn></a></dt>
  <dd>Seien \(A_1, \dots, A_n\) paarweise disjunkte Ereignisse mit
      \(A = \sum_{i=1}^n A_i\). Dann gilt für jedes beliebige Ereignis \(B\):
      \[P(B) = \sum_{i=1}^n P(B | A_i) \cdot P(A_i) = P(A_i, B)\]</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Satz_von_Bayes"><dfn>Satz von Bayes</dfn></a></dt>
  <dd>Seinen \(A, B\) Ereignisse mit \(P(B) > 0\). Dann gilt
      \[P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}\]

      Hierbei heißt \(P(A|B)\) die <i>a posteriori Wahrscheinlichkeit</i>,
      \(P(B|A)\) die <i>likelihood</i>, \(P(A)\) die
      <i>a priori Verteilung über \(A\)</i> und \(P(B)\) die
      <i>a priori Verteilung über \(B\)</i>.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Bayessches_Netz"><dfn>Bayessches Netz</dfn></a> (Siehe <a href="https://www.youtube.com/watch?v=VfyxPtlqZh4">Lecture 13: Bayes Nets</a>)</dt>
  <dd>Ein <i>Bayessches Netz</i> ist ein <abbr title="Directed Acyclical
      Graph">DAG</abbr>, bei dem die Knoten Zufallsvariablen und die Kanten
      bedingte Abhängigkeiten beschreiben.

      Bayessche Netze sind zur Modellierung kausaler Zusammenhänge geeignet.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Markov_Random_Field"><dfn>Markov Random Field</dfn></a></dt>
  <dd>Siehe <a href="https://martin-thoma.com/machine-learning-1-course/#mrf-definition">ML 1</a></dd>
  <dt><a href="https://en.wikipedia.org/wiki/Dynamic_Bayesian_network"><dfn>Dynamisches Bayessches Netz</dfn></a></dt>
  <dd><i>Dynamische Bayessche Netze</i> sind Bayessche Netze zur Beschreibung
      dynamischer Prozesse.</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Markov_blanket"><dfn>Markov Blanket</dfn></a></dt>
  <dd>Sei \(G=(V,E)\) ein DAG zu einem Bayesschen Netz und \(v_S \in V\).
      Dann ist der Markov Blanket die folgende Knotenmenge \(B \subseteq V \setminus \{v_S\}\):

      <ul>
          <li>Die Elternknoten von \(v_S\) sind in \(B\).</li>
          <li>Die Kindknoten \(K = \{v_{K_1}, \dots, v_{K_n}\}\) sind in \(B\)</li>
          <li>Die Elternknoten von \(K\), ausgenommen von \(v_S\), sind in
              \(B\)</li>
      </ul>

      Diese Knotenmenge macht \(v_S\) unabhängig von anderen Knoten.</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering"><dfn>Naive Bayes Spam Filter</dfn></a></dt>
  <dd>Ein naiver Bayes Spamfilter nutzt häufig Bag-of-Words Features. Man berechnet die Wahrscheinlichkeit,
      dass eine gegebene E-Mail Spam ist. Dazu geht man davon aus, dass die
      Wörter in einer E-Mail unabhängig von einander sind und nutzt den
      Satz von Bayes.
      Siehe <a href="https://de.wikipedia.org/wiki/Bayes-Klassifikator#Beispiel">Bayes-Klassifikator</a>
      für eine detailiertere Beschreibung.</dd>
  <dt><dfn>Bayes Filter</dfn></dt>
  <dd>Ein Bayes Filter ist eine Familie von Zufallsvariablen. Das könnte z.B.
      die \((x,y,z)\) Position eines GPS-Sensors sein. Diese Position ist
      verrauscht.

      Nun gibt es drei mögliche Anfragen:

      <ul>
          <li><b>Filtern</b>: Es liegen Messungen \(Z_0, \dots, Z_t\) vor,
              sage die aktuelle Position \(X_t\) vorher. Also <i>filtere das
              Rauschen</i> aus \(Z_t\) unter berücksichtigung, dass wir uns
              noch nicht teleportieren können:
              \[P(X_t | Z_t, \dots, Z_0)\]</li>
          <li><b>Prädizieren</b>: Es liegen Messungen \(Z_0, \dots, Z_t\) vor,
              sage die Position \(X_{t+k}\) vorher:
              \[P(X_{t+k} | Z_t, \dots, Z_0)\]</li>
          <li><b>Glätten</b>: Es liegen Messungen \(Z_0, \dots, Z_t\) vor,
              sage die Position \(P(X_{t-k} | Z_t, \dots, Z_0)\) vorher.</li>
      </ul>

      Beispiele für Bayes-Filter sind

      <ul>
          <li>Kalman-Filter</li>
          <li><abbr title="Hidden Markov Model">HMM</abbr></li>
          <li>Partikel Filter</li>
      </ul>

      </dd>
  <dt><dfn>Naiver Bayes'scher Spam Filter</dfn></dt>
  <dd>Ein probabilistischer Klassifikator welcher die Unabhängigkeit der
      Features vorraussetzt wird <i>naiv</i> genannt.<br/>
      <br/>
      Der naive bayessche Spam Filter nutzt Bayes Theorem um die
      Wahrscheinlichkeit zu berechnen, dass eine E-Mail Spam ist.
      </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Kalman-Filter"><dfn>Kalman-Filter</dfn></a> (siehe <a href="http://arxiv.org/abs/1204.0375">Python-Implementierung</a>)</dt>
  <dd>Der Kalman-Filter ist ein Bayes-Filter. Er wird z.B. zum Schätzen einer
      Fahrzeugtrajektorie eingesetzt.

      Der Kalman-Filter besteht aus zwei Schritten:

       <ul>
           <li><b>Predict</b> the next step of the system given the previous
               measurements.</li>
           <li><b>Update</b> the estimate of the current state given the
               measurement of this time step.</li>
       </ul>
    </dd>
    <dt><dfn>Expectation Maximizaion Algorithm</dfn> (<dfn>EM-Algorithmus</dfn>)</dt>
    <dd>
        Der EM-Algorithmus kann als ein Clusteringalgorithmus mit weicher
        Clusterzugehörigkeit gesehen werden. Er findet die Parameter für
        gegebene Verteilungen (üblicherweise multivariate Normalverteilungen).

        Er löst das Henne-Ei Problem
        <ul>
            <li>Wenn man weiß wie genau die Wahrscheinlichkeitsverteilungen
                der Cluster parametrisiert sind ist es leicht die Daten den
                Clustern zuzuordnen.</li>
            <li>Wenn man die Daten einem Cluster zuordnen kann, dann ist es
                leicht die Parameter der Wahrscheinlichkeitsverteilung zu
                schätzen.</li>
        </ul>

        Wenn man sowohl Clusterzugehörigkeit als auch die Parameter der
        Verteilung schätzen muss ist es schwer. Man kann "zufällig" die
        initialen Parameter wählen, dann die Zuordnung machen.

        Der EM-Algorithmus iteriert also:

        <ul>
            <li><b>Expectation</b>: Weise alle Datenpunkte ihrem Cluster zu.</li>
            <li><b>Maximization</b>: Berechne die Parameter der Cluster neu.</li>
        </ul>

        Siehe <a href="https://www.youtube.com/watch?v=REypj2sy_5U">Mixture Models 1: the EM algorithm</a>

    </dd>
</dl>

Typische Fragestellungen:

* Gegeben ist die Struktur eines Bayesschen Netzes: Wie lautet die Verteilung?
  - Dies wird üblicherweise mit dem <abbr title="Expectation Maximimization">EM</abbr>-Algorithmus
  gelöst.

Anwendungsfälle:

* Automatische Diagnose, gegeben die Symptome (Bayessches Netz)
* Fahrzeugverfolgung: Vorhersage von Routen, welche die Fahrzeuge nehmen werden
  (Dynamisches Bayessches Netz)

Anmerkungen: Die Folien sind hier sehr gut! Insbesondere Folie&nbsp;14-23
sollte man sich ansehen.

Es scheint folgende Beziehung zu gelten: HMMs, Kalman-Filter, Extended
Kalman-Filter, Partikel Filter sind Beispiele für Bayes-Filter. Bayes-Filter
sind Beispiele für dynamische Bayessche Netze.

Siehe auch:

* Udacity: [Artificial Intelligence for Robotics](https://www.youtube.com/watch?v=8O9GV4SUToA&index=77&list=PLAwxTw4SYaPkCSYXw6-a_aAoXVKLDwnHK) - good content for Kalman Filters

{% gallery columns="2" size="medium" %}
    ../images/2016/01/tracking-robots.png    "Tracking Robots"
    ../images/2016/01/probabilisitc-graphical-models.png    "Probabilistic Graphical Models"
{% endgallery %}


### Probablistisch Relationale Modelle

Slides: `06_Probablistisch_Relationale_Modelle.pdf`

Siehe auch:

* C. Howard and M. Stumptner and others. Model Construction
  Algorithms for Object-Oriented Probabilistic Relational Models. FLAIRS
  Conference, 2006.
* C. Howard and M. Stumptner. [Situation assessments using object oriented
  probabilistic relational models](http://ieeexplore.ieee.org/xpl/login.jsp?arnumber=1592031),
  in 8th International Conference on Information Fusion, 2005, vol.2. doi:
  10.1109/ICIF.2005.1592031

<dl>
  <dt><dfn>Objektorientierte Probablistisch Relationales Modelle</dfn> (<dfn>OPRM</dfn>)</dt>
  <dd>Ein OPRM besteht nach [<a href="#ref-schu15" name="ref-schu15-anchor">Schu15</a>] aus

  <ul>
      <li>Eine Klassenmenge \(\mathbf{C} = \{C_1, \dots, C_n\}\),</li>
      <li>einer partiellen Ordnung über C, welche die Klassenhierarchie definiert,</li>
      <li>einer Menge einfacher, nicht probabilisitscher Attribute \(\Lambda_C = \{\lambda_1, \dots, \lambda_n \forall C \in \mathbf{C}\}\),</li>
      <li>einer Menge beschreibender Attribute \(\Delta_C = \{\delta_1, \dots, \delta_n\} \forall C \in \mathbf{C}\),</li>
      <li>einer Menge komplexer Attribute \(\Phi_C = \{\phi_1, \dots, \phi_n\} \forall C \in \mathbf{C}\).
          Die komplexen Attribute beschreiben funktionale Beziehungen zwischen Klassen.</li>
  </ul>

    Dieses Modell wurde in <a href="https://staff.fnwi.uva.nl/j.m.mooij/libDAI/">libDAI</a>
    umgesetzt.
  </dd>
</dl>


### Gaussche Prozesse

Slides: `07_Gaussche_Prozesse.pdf`

I suggest reading the first two chapters of the online book
<a href="http://www.gaussianprocess.org/">gaussianprocess.org</a> before
starting to read the slides.

See also:

* [Function Approximation](https://martin-thoma.com/function-approximation/)
* The Talking Machines: [OpenAI and Gaussian Processes](http://www.thetalkingmachines.com/blog/2016/1/28/openai-and-gaussian-processes)

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Lineare_Regression"><dfn>Lineare Regression</dfn></a></dt>
  <dd>Die lineare Regression ist ein Modell zur approximation von Datenpunkten
      \((x, y) \in \mathbb{R}^n \times \mathbb{R}\) durch eine
      lineare Funktion, d.h. einer Funktion der Form \(f(x) = x^T \cdot w\).
      Dabei ist \(w \in \mathbb{R}^n\).<br/>
      <br/>
      Wenn man als Optimierungskriterium den quadratischen Abstand
      \[E(f, data) = \sum_{(x,y) \in data} (f(x) - y)^2\]
      nimmt, dann ist eine optimale Lösung durch
      \[w = (X^T X)^{-1} X^T y\]
      gegeben.<br/>
      <br/>
      Siehe auch: <a href="http://math.stackexchange.com/q/691812/6876">Proof of when is \(A=X^T X\) invertible?</a>
      sowie <a href="http://math.stackexchange.com/q/1626052/6876">Does a transformation + linear regression give the same regression as fitting a quadratic function?</a>
      </dd>
  <dt><dfn>Affine Regression</dfn></dt>
  <dd>Die affine Regression ist ein Modell zur approximation von Datenpunkten
      \((x, y) \in \mathbb{R}^n \times \mathbb{R}\) durch eine
      affine Funktion, d.h. einer Funktion der Form \(f(x) = x^T \cdot w + b\).
      Dabei ist \(w \in \mathbb{R}^n, b \in \mathbb{R}\). Um das Problem auf
      ein lineares zu reduzieren kann man den Feature-Vektor \(x\) durch ein
      konstantes Feature \(x_0 = 1\) erweitern.
      </dd>
  <dt><dfn>Korrelationskoeffizient</dfn></dt>
  <dd>Der Korrelationskoeffizient \(\kappa(X, Y) \in [-1, 1]\) ist ein Maß für
      den linearen Zusammenhang zwischen zwei Zufallsvariablen \(X, Y\). Er
      ist definiert als
      \[\kappa(X, Y) := \frac{Cov(X, Y)}{\sigma(X) \cdot \sigma(Y)}\]</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Gau%C3%9F-Prozess"><dfn>Gausscher Prozess</dfn></a> (<dfn>Kriging</dfn>, <a href="https://www.youtube.com/watch?v=4vGiHC35j9s">Machine learning - Introduction to Gaussian processes</a> by Nando De Freitas)</dt>
  <dd>Gaussche Prozesse approximieren eine Funktion dadurch, dass sie an jedem
      Punkt eine Normalverteilung (Gauss-Verteilung) annehmen.<br/>
      <br/>
      Siehe <a href="https://en.wikipedia.org/wiki/Kriging">Gaussian process regression</a>.</dd>
</dl>


### Deep Learning

Slides: `08_DeepLearning.pdf`

Siehe auch:

* [Neuronale Netze Vorlesung](//martin-thoma.com/neuronale-netze-vorlesung/)
* Udacity: [Neural Networks for Machine Learning](https://class.coursera.org/neuralnets-2012-001/lecture) by Hinton.

<dl>
  <dt><dfn>Deep Belief Netz</dfn> (<dfn>DBN</dfn>)</dt>
  <dd>Ein Deep Belief Netz ist ein gerichtetes, azyklisches, probabilistisches
      graphisches Modell.</dd>
  <dt><dfn>Restricted Boltzmann Machine</dfn> (<dfn>RBM</dfn>)</dt>
  <dd>Eine <i>RBM</i> ist ein neuronales Netz mit nur einem Hidden Layer.
      Es ist gleichzeitig ein Spezialfall von
      <abbr title="Markov Random Fields">MRFs</abbr>.

      Es werden keine Verbindungen zwischen den Hidden Units erlaubt (daher das "restricted" - Quelle: <a href="https://youtu.be/IcOMKXAw5VA?t=5m42s">Hinton, 2015</a>).<br/>
      <br/>
      Siehe <a href="https://www.cs.toronto.edu/~hinton/absps/guideTR.pdf">A Practical Guide to Training Restricted Boltzmann Machines</a> von Hinton, 2010.</dd>
  <dt><dfn>Contrastive Divergence</dfn> (<dfn>CD</dfn>, siehe <a href="https://www.youtube.com/watch?v=MD8qXWucJBY">YouTube Video</a> von Hugo Larochelle)</dt>
  <dd>Contrastive Divergence ist ein Trainingsalgorithmus für RBMs.

      Ein Hyperparameter ist \(k \in \mathbb{N}\).

      Er geht wie folgt vor:

      <ol>
          <li>Lege den Trainingsvektor \(x^{(t)}\) an die Eingabeknoten an.</li>
          <li>Berechne die Wahrscheinlichkeit für jede Hidden Unit, dass diese gleich 1 ist. Setze sie mit dieser Wahrscheinlichkeit gleich 1.</li>
          <li>Berechne die Wahrscheinlichkeit für jeden Eingabeknoten, dass dieser gleich 1 ist. Setze ihn mit dieser Wahrscheinlichkeit gleich 1.</li>
          <li>Gehe zu Schritt 2. Wiederhole dies für \(k\) Schritte (dies wird auch Gibbs-Sampling genannt).
              Das, was nach dem \(k\)-fachem Gibbs-Sampling in der Eingabeschicht
              steht wird auch "negative sample \(\tilde x\)" genannt.</li>
          <li>Update der Parameter:
            \[\begin{align}
                W &\leftarrow W + \alpha (h(x^{(t)}) {x^{(t)}}^T - h(\tilde x) {\tilde x}^T)\\
                b &\leftarrow b + \alpha (h(x^{(t)}) - h(\tilde x))\\
                c &\leftarrow c + \alpha (x^{(t)} - \tilde x)
              \end{align}
            \]
            wobei \(\alpha \in (0, 1) \) die Lernrate ist,
            \(b \in \mathbb{R}^n_h\) der Bias-Vektor der Hidden Units und
            \(c \in \mathbb{R}^{n_v}\) der Bias-Vektor der Eingabeknoten ist.
            \(h\) ist eine Zufallsvariable, welche der Hidden Layer ist. Diese
            sind abhängig von der Eingabeschicht.
          </li>
      </ol>

      In der Praxis funktioniert es schon mit \(k=1\) für Pre-Training. Wenn
      \(k\) groß ist konvergiert \(\tilde x\) gegen den wahren Modellwert. Das
      wäre dann eine Monte-Carlo Estimation.
  </dd>
  <dt><dfn>Contrastive Wake-Sleep Algorithm</dfn> (siehe <a href="https://www.youtube.com/watch?v=znQfKBOGnJ8">The wake-sleep algorithm</a> von Hinton - Lecture 13d aus "<a href="https://www.coursera.org/course/neuralnets">Neural Networks for Machine Learning</a>")</dt>
  <dd>Der Wake-Sleep Algorithmus ist ein Trainingsalgorithmus für gerichtete
      graphische Modelle wie Sigmoid Belief Networks. Er ist nicht für RBMs.

      Man hat im Grunde zwei Netzwerke mit der gleichen Topologie, jedoch ist
      die Richtung vertauscht: Das eine Netz stellt die Hypothese aus den Daten
      auf, das andere Netz geniert neue Daten aus einer gegebenen Hypothese.

      In der <b>wake phase</b> wird die Eingabe genutzt um die Hypothese zu
      erzeugen. In dieser Phase werden die Gewichte für das Generative Modell
      trainiert. Dieses soll die Aktivierung der vorhergehenden Schicht
      rekonstruieren.

      In der <b>sleep phase</b> wird das generative Modell genutzt um aus dem
      Modell samples zu erzeugen. Dann trainiert man die Gewichte des
      erkennenden Netzes (also vergleichbar mit der wake phase, nur anders
      rum).

      <br/>
      Siehe <a href="http://www.cs.toronto.edu/~fritz/absps/ncfast.pdf">A Fast Learning Algorithm for Deep Belief Nets</a></dd>
</dl>


#### Probleme von Tiefen Netzen und wie man sie lösen kann:

* **Lange Trainingsdauer**: GPUs / mehr Rechenpower / weniger Parameter durch
  Parameter sharing, z.B. in <abbr title="Convolutional Neural Networks">CNNs</abbr>
  / <abbr title="Time Delay Neural Networks">TDNNs</abbr>
* **Extrem viele gelabelte Trainingsdaten werden benötigt**: Internet
  (z.B. Wikipedia, Soziale Netzwerke, Amazon Mechanical Turk) reduziert dieses
  Problem; Nutzen ungelabelter Daten durch <abbr title="Semi-Supervised Learning">SSL</abbr>
  in Auto-Encodern
* **Lokale Minima**
* **Overfitting**: Regularis

#### Siehe auch

* [MNIST Demo](http://www.cs.toronto.edu/~hinton/adi/index.htm) (Flash):
  Neuronales Netz welches Ziffern generiert
* Geoffry Hinton: [Deep Learning](https://www.youtube.com/watch?v=IcOMKXAw5VA)
  on YouTube, 2015. 43&nbsp;minutes. (Topics: RBMs)


### Convolutional Neural Networks

Slides: `09_ConvolutionalNeuralNetworks.pdf`

Siehe auch: [Neuronale Netze Vorlesung](//martin-thoma.com/neuronale-netze-vorlesung/)

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Convolutional_Neural_Network"><dfn>Convolutional Neural Networks</dfn></a> (<dfn>CNNs</dfn>)</dt>
  <dd><abbr title="Convolutional Neural Networks">CNNs</abbr> sind neuronale
      Netze welche weight sharing einsetzen. Sie setzen eine diskrete Faltung
      um. Ein CNN muss mindestens einen <i>Convolutional Layer</i> haben.
      Dieser hat folgende Parameter:
      <ul>
          <li>Padding: None, Zero, Copy</li>
          <li>Stride: \(s \in \mathbb{N}_{> 0}\)</li>
          <li>Filter Size: \((x,y) \in \mathbb{N}^2\)</li>
          <li>Number of filters: How many filters should get learned?</li>
      </ul></dd>
  <dt><dfn>Feature Map</dfn></dt>
  <dd>Nach einem Convolutional Layer hat man die Ausgabe der Filter, welche
      auf die Eingabe angewandt wurden. Diese nennt man <i>Feature Map</i>.
      Für jeden Filter bekommt man eine Feature Map. Die Feature Maps sind
      wiederum Eingaben für die nächsten Schichten.</dd>
  <dt><dfn>Pooling Layer</dfn></dt>
  <dd>Ein <i>pooling layer</i> ist eine Schicht in einem CNN, welche
      Features zusammenfasst. Pooling Schichten haben folgende Parameter:

      <ul>
          <li>Größe: Typischerweise \(3 \times 3\)</li>
          <li>Stride \(s \in \mathbb{N}\): Typischerweise gleich der Größe des Pooling-Bereichs (also 3).</li>
          <li>Art: max, mean</li>
      </ul>

      Typischerweise reduziert sie die Anzahl der Features, da typischerweise
      ein \(s > 1\) gewählt wird.</dd>
</dl>


### Spiking Neural Nets

Slides: `10_SpikingNeuralNets.pdf`

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Gepulste_neuronale_Netze"><dfn>Spiking Neural Networks</dfn></a></dt>
  <dd>Gepulste neuronale Netze versuchen natürliche neuronen realistisch
      abzubilden. Das Hodgkin-Huxley Neuronenmodell wurde bereits 1952
      vorgestellt.</dd>
  <dt><dfn>Hodgkin-Huxley Neuronenmodell</dfn></dt>
  <dd>Das <i>Hodgkin-Huxley Neuronenmodell</i> modelliert die elektrochemischen
      Vorgänge innerhalb eines Neurons mit elektrischen Baugliedern. Dies
      resultiert in Differenzialgleichungen mit 4&nbsp;Variablen (Kapazität
      der Membran, Widerstände der Ionenkanäle, Gleichgewichtspotentiale,
      Öffnung der Ionenkanäle).

      Das Modell ist realistisch, aber sehr komplex. </dd>
  <dt><dfn>LIF Neuronenmodell</dfn> (Leaky integrate and Fire)</dt>
  <dd>Das <i>LIF Neuronenmodell</i> modelliert ein Neuron durch eine
      gewöhnliche Differentialgleichung erster Ordnung.</dd>
  <dt><dfn>SRM Neuronenmodell</dfn> (Spike Response Model)</dt>
  <dd>Das <i>SRM Neuronenmodell</i> modelliert die Refraktionszeit. Das ist
      die Zeit, in der kein neues Aktionspotential aufgebaut werden kann.

      Das SRM ist ein rein phänomenologisches Modell, welches trotz der
      Einfachheit allgemeiner ist als das LIF-Modell.</dd>
</dl>


### Evaluation

Slides: `11_Evaluation.pdf`

#### Für Klassifikation:

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Konfusionsmatrix"><dfn>Konfusionsmatrix</dfn></a></dt>
  <dd>Eine Konfusionsmatrix ist eine Tabelle, in welcher die Spalten angeben,
      welche Hypothese gemacht wurde (Testentscheid) und die Zeilen den wahren
      Wert angeben. So kann für beliebig viele Klassen gezeigt werden, wie gut
      der Klassifikator ist und welche Art der Verwechslung er macht.</dd>
  <dt><dfn>Klassifikationsfehler</dfn></dt>
  <dd>\(\text{Klassifikationsfehler} = \frac{\text{Fehlerhafte Hypothesen}}{\text{Anzahl aller Beispiele}} \in [0, 1]\)</dd>
  <dt><dfn>Klassifikationsgüte</dfn></dt>
  <dd>Klassifikationsgüte = 1 - Klassifikationsfehler</dd>
  <dt><dfn>False Alarm Rate</dfn> (<dfn>FA</dfn>, <dfn>Falsch Positiv Rate</dfn>, <dfn>FPR</dfn>)</dt>
  <dd>Es sei FP die Anzahl der False Positive Testdaten, also der Testdaten
      für welche <i>Positive</i> vorhergesagt wurde, die aber negative sind. Weiter
      sei TN die Anzahl der True Negatives, also der Testdaten, für welche
      korrekterweise negative vorhergesagt wurde.

      Dann ist die <i>FPR</i> definiert als
      \[\text{FPR} := \frac{FP}{FP + TN} \in [0, 1]\]

      Die FPR gibt also den Anteil an, wie viele der tatsächlich negativen
      fälschlicherweise als positiv erkannt wurden.</dd>
  <dt><dfn>Miss-Rate</dfn> (<dfn>MR</dfn>, <dfn>Falsch Negativ Rate</dfn>, <dfn>FNR</dfn>)</dt>
  <dd>\[FNR := \frac{FN}{TP + FN} \in [0, 1]\]</dd>
  <dt><dfn>Recall</dfn> (<dfn>True Positive Rate</dfn>, <dfn>TPR</dfn>, <dfn>Sensitivität</dfn>)</dt>
  <dd>\[TPR = \frac{TP}{TP + FN} = 1 - FNR \in [0, 1]\]

      Der Recall gibt den Anteil der erkannten positiven aus allen positiven
      an.

      <i>Sensitivität</i> ist ein in der Medizin üblicher Begriff.</dd>
  <dt><dfn>Precision</dfn> (<dfn>Genauigkeit</dfn>)</dt>
  <dd>\[Precision = \frac{TP}{TP + FP} \in [0, 1]\]

      Die Precision gibt den Anteil der real positiven aus den als positiv
      erkannten an.</dd>
  <dt><dfn>ROC-Graph</dfn> (<dfn>Receiver-Operator Curve</dfn>)</dt>
  <dd>Der ROC-Graph gibt für einen Klassifikator, bei dem man einen Parameter
      einstellen kann, den Fehler an.

      Die \(x\)-Achse ist dabei die FPR, die \(y\)-Achse die TPR.</dd>
  <dt><dfn>Spezifität</dfn></dt>
  <dd>Der Begriff der <i>Spezifität</i> ist in der Medizin üblich und
      ist definiert durch
      \[Spezifität = \frac{TN}{TN + FP} = 1 - FPR\]

      Es ist eine Art recall für die negative Klasse. Im Beispiel eines
      medizinischen Tests wäre das der Anteil der Gesunden, bei denen
      tatsächlich auch die Diagnose "Gesund" gestellt wurde.</dd>
  <dt><dfn>PRC-Graph</dfn> (<dfn>Precision-Recall-Graph</dfn>)</dt>
  <dd>Die \(x\)-Achse ist Recall, die \(y\)-Achse ist Precision.</dd>
  <dt><dfn>F-Maß</dfn></dt>
  <dd>\[F_\alpha = \frac{precision \cdot recall}{\alpha^2 \cdot precision + recall}\]</dd>
</dl>

Alternative:

* Aufstellen einer Kostenfunktion und optimieren nach Kosten.
* Plotten der Anzahl der Trainingsdaten (<span markdown="0">\(x\)</span>-Achse) und des Fehlers
  (<span markdown="0">\(y\)</span>-Achse). Die Kurven sollten der Test-Fehler sowie der Trainingsfehler
  sein. Damit lässt sich abschätzen, ob mehr Trainingsdaten ohne eine
  Veränderung des Modells hilfreich sind.


#### Für Regression

<dl>
    <dt><dfn>Mittlerer Quadratischer Fehler</dfn> (<dfn>MSE</dfn>, <dfn>Mean Squared Error</dfn>)</dt>
    <dd>\[E(f, data) = \frac{1}{|data|} \sum_{(x, y) \in data} (f(x) - y)^2\]</dd>
    <dt><dfn>Relativer Quadratischer Fehler</dfn></dt>
    <dd>\[E(f, data) = \frac{\sum_{(x, y) \in data} (f(x) - y)^2}{\sum_{(x,y) \in data} (y - \mu)^2}\]</dd>
    <dt><dfn>Mittlerer Absoluter Fehler</dfn></dt>
    <dd>\[E(f, data) = \frac{1}{|data|} \sum_{(x, y) \in data} |f(x) - y|\]</dd>
</dl>





#### Siehe auch

* [Beurteilung eines binären Klassifikators](https://de.wikipedia.org/wiki/Beurteilung_eines_binären_Klassifikators)
* [False positives and false negatives](https://en.wikipedia.org/wiki/False_positives_and_false_negatives)
* Matt Zeiler: [Visualizing and Understanding Deep Neural Networks](https://www.youtube.com/watch?v=ghEmQSxT6tw) on YouTube, 2015. 48 minutes.


## Prüfungsfragen

<ul>
    <li>Was versteht man unter einer "Transductive SVM"?<br/>
    → Eine Transductive SVM ist eine <abbr title="Support Vector Machine">SVM</abbr>
       welche neben gelabelten Daten auch noch ungelabelte benutzt. Sie versucht
       die Trennebene durch eine Region geringer Dichte zu legen.</li>
    <li>Wie lautet die Optimierungsformel der transductive SVM?<br/>
        → \[\text{minimize}_{w, b, y^*} \frac{1}{2} \|w\|^2\]
        unter den Nebenbedingungen
        \[\forall i \in 1, \dots, n: y_i (w \cdot x_i - b) \geq 1\]
        und
        \[\forall j \in 1, \dots, k: y_j^* (w \cdot x_j^* -b) \geq 1\text{ with }y_j^* \in \{-1, 1\}\]

        Dabei sind \(D^* = \{x_i^* | i = 1, \dots, k\}\) ungelabelte Daten.
    </li>
    <li>Was macht man im Reinforcement Learning, wenn Aktionen länger dauern?<br/>
        → Options verwenden (TODO: Wie ändert sich die Value Iteration Formel
           nun bzgl. der Zeit?)</li>
    <li>Warum heißen POMDPs "Partially Observable"?<br/>
        → Weil der Agent zwar Feedback über die Umgebung bekommt, aber nicht
           direkt erfährt in welchem Zustand er ist. Siehe
           <a href="#pomdp-definition">Definition</a>.</li>
    <li>Welche Active Learning Techniken gibt es?<br/>
        → Query / Selective / Pool-based (vgl. <a href="#tocAnchor-1-1-4">Query-by-Committee</a>)</li>
    <li>Wie nennt man ein instanziiertes OPRM?<br/>
        → TODO (Skelett?)</li>
    <li>Wie funktioniert aktives Lernen bei SVMs?<br/>
        → Bei SVMs gibt es die Dualität zwischen dem Feature-Space und dem
           Hypothesenraum. In dem Feature-Space stellen
           die Achsen <span markdown="0">\(x_i\)</span> die Features dar, Trainingsdaten Punkte sind und
           die SVM durch die Trennebene visualisiert wird. Im Hypothesenraum
           sind die Achsen <span markdown="0">\(w_i\)</span> zusammen der
           Normalenvektor der SVM, die verschiedenen Trennebenen der SVMs sind
           hier Punkte. Die Daten geben Bedingungen an die SVM vor, welche
           in diesem Raum als Hyperebenen dargestellt werden können. Der Margin ist
           in diesem Raum ein Kreis, der die Bedingungs-Hyperebenen berührt.

           Beim aktiven lernen versucht man den Version-Space im Inneren der
           Bedungungs-Hyperebenen so schnell zu verkleinern wie möglich.</li>
    <li>Was versteht man unter Transduktivem Lernen?<br/>
        → Unter Transduktiver Inferenz versteht man das Schließen von
           Trainingsbeispielen direkt auf auf spezifische Testfälle.</li>
    <li>Wie nennt man die Wahrscheinlichkeit des aktiellen Zustands in POMDPs?<br/>
        → Belief.</li>
</ul>


## Material und Links

* [Vorlesungswebsite](http://tks.anthropomatik.kit.edu/28_176.php)
* [Ilias](https://ilias.studium.kit.edu/goto_produktiv_crs_429082.html): Ist passwortgeschützt
* [Zusammenfassung der Vorlesung ML 1](//martin-thoma.com/machine-learning-1-course/)


## Literatur

* [<a href="#ref-schu15-anchor" name="ref-schu15">Schu15</a>] J. Schulz.
  Erkennung von Interaktionen zwischen Verkehrsteilnehmern zur
  Verhaltensprädiktion. Masterarbeit am FZI. Karlsruhe, 2015. Man kann
  <a href="https://www.fzi.de/wir-ueber-uns/organisation/mitarbeiter/address/kuhnt/">Florian Kuhnt</a>
  um Zugang dazu fragen.
* [<a href="#ref-die00-anchor" name="ref-die00">Die00</a>] T. Dietterich.
  <a href="https://www.jair.org/media/639/live-639-1834-jair.pdf">Hierarchical
  Reinforcement Learning with the MAXQ Value Function Decomposition</a>.
  Journal of Artificial Intelligence Research, 2000.


## Übungsbetrieb

Es gibt keine Übungsblätter, keine Übungen, keine Tutorien und keine
Bonuspunkte.


## Kontakt

* goettl@fzi.de: Sonja Göttl (Sekretariat, zum Anmelden zur mündlichen Prüfung)


## Termine und Klausurablauf

**Datum**: Mündliche Prüfung (in Zukunft schriftlich)<br/>
**Ort**: nach Absprache<br/>
**Zeit**: 15&nbsp;min<br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Ergebnisse**: werden ca. 5&nbsp;-&nbsp;10&nbsp;min. nach der mündlichen Prüfung gesagt<br/>
**Erlaubte Hilfsmittel**: keine
