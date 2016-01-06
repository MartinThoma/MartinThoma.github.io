---
layout: post
title: Machine Learning 2 - Vorlesung
author: Martin Thoma
date: 2015-05-11 11:00
categories:
- German posts
tags:
- Klausur
- Machine Learning
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Machine Learning 2&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://tks.anthropomatik.kit.edu/21_52.php">Herrn Prof. Dr. Marius Zöllner</a> im Sommersemester 2015 gehört. Der Artikel wird bis zur mündlichen Prüfung laufend erweitert.</div>

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
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=429607&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">Einleitung</a></td>
    <td>Wiederholung ML1; Definition 'Machine Learning'</td>
</tr>
<tr>
    <td>24.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=432731&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">Semi Supervised Learning (SSL)</a></td>
    <td>Transduktives Lernen; Self-Learning; Co-Training; Generative Models; EM-Algorithmus; Low-Density seperation; Transductive SVM</td>
</tr>
<tr>
    <td>01.05.2015</td>
    <td>-</td>
    <td>Vorlesung fällt aus (vgl. erster Foliensatz, Folie 49)</td>
</tr>
<tr>
    <td>08.05.2015</td>
    <td><abbr title="Semi-Supervised Learning">SSL</abbr></td>
    <td>Transductive SVM, Aktives Lernen</td>
</tr>
<tr>
    <td>15.05.2015</td>
    <td>-</td>
    <td>Vorlesung fällt aus (vgl. erster Foliensatz, Folie 49)</td>
</tr>
<tr>
    <td>22.05.2015</td>
    <td>Reinforcement Learning</td>
    <td>Beschreibung als MDP, Strategielernen, Bellman-Gleichungen; Q-Learning, <abbr title="Hierarchische Abstrakte Maschinen">HAM</abbr>, MAXQ</td>
</tr>
<tr>
    <td>05.06.2015</td>
    <td>-</td>
    <td>Vorlesung fällt aus (vgl. erster Foliensatz, Folie 49)</td>
</tr>
</table>


### Einführung

Slides: 01_Einfu__hrung_MLII.pdf

Rückblick auf [ML 1](//martin-thoma.com/machine-learning-1-course/).

Meine Fragen (TODO):

* Folie 27: Was heißt MLNN?


### Semi-Supervised Learning

Slides: 02_Semi-supervised-learning.pdf

<dl>
  <dt><dfn>Überwachtes Lernen</dfn> (engl. <dfn>Supervised Learning</dfn>)</dt>
  <dd>Alle Trainingsdaten liegen mit Labels vor.</dd>
  <dt><dfn>Unüberwachtes Lernen</dfn> (engl. <dfn>Unsupervised Learning</dfn>)</dt>
  <dd>Alle Trainingsdaten liegen ohne Labels vor.</dd>
  <dt><dfn>Semi-Supervised Learning</dfn> (<dfn>SSL</dfn>, siehe <a href="https://en.wikipedia.org/wiki/Semi-supervised_learning">Wikipedia</a>)</dt>
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
          <li>Zurück zu Schritt 1.</li>
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
          <li>Zurück zu Schritt 2.</li>
      </ol>

      Dabei sind folgende Variationen vorstellbar:
      <ul>
          <li>Demokratisches Voting: Bei mehr als 2 Klassifizierern.</li>
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


### Semi-Supervised and Active Learning

Slides: 03_Semi-supervised+Active-learning.pdf

TODO

<dl>
  <dt><dfn>Lagrange-Multiplikator</dfn> (siehe <a href="https://de.wikipedia.org/wiki/Lagrange-Multiplikator">Wikipedia</a>)</dt>
  <dd>TODO</dd>
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

Slides: 04_Reinforcement_Learning_II.pdf

<dl>
  <dt><dfn>Options</dfn></dt>
  <dd>Eine <i>Option</i> ist wohl-definiertes Verhalten, welches im
      hierarchischen <abbr title="Reinforcement Learning">RL</abbr> eingesetzt
      werden kann. Es ist ein Baustein für komplexe Pläne.</dd>
  <dt><dfn>Hierarchien Abstrakter Maschinen</dfn> (<dfn>HAM</dfn>)</dt>
  <dd>Ein <abbr title="Markov Decision Process">MDP</abbr> wird mit
      Maschinen \(\{M_i\}\) kombiniert. Jede Maschine repräsentiert einen
      Teil der Policy. Jede Maschine verwendet eigene Zustände \(m_t^i\)
      und globale Zustände \(s_t\). Maschinen werden durch Zustandsautomaten
      abgebildet.</dd>
  <dt><dfn>MAXQ</dfn></dt>
  <dd>TODO</dd>
</dl>

Folie 35:

* Was heißt hier "mit festen Knoten"?


### Dynamische Bayessche Netze

Slides: 05_DynamischeBayesscheNetze.pdf

TODO

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Bedingte_Wahrscheinlichkeit#Multiplikationssatz"><dfn>Multiplikationssatz</dfn></a></dt>
  <dd>Seien \(A, B, X_i\) Ereignisse. Dann gilt:
      \[P(X_1, \dots, X_n) = P(X_1) \cdot \prod_{k=2}^n P(X_k | X_{k-1}, \dots, X_1)\]
      und insbesondere
      \[P(A\cap B) = P(A, B) = P(A\mid B) \cdot P(B)\]</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Bedingte_Wahrscheinlichkeit#Gesetz_der_totalen_Wahrscheinlichkeit"><dfn>Gesetz der totalen Wahrscheinlichkeit</dfn></a></dt>
  <dd>Seien \(A_1, \dots, A_n\) paarweise disjunkte Ereignisse mit
      \(\sum_{i=1}^n\). Dann gilt für jedes beliebige Ereignis \(B\):
      \[P(B) = \sum_{i=1}^n P(B | A_i) \cdot P(A_i) = P(A_i, B)\]</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Satz_von_Bayes"><dfn>Satz von Bayes</dfn></a></dt>
  <dd>Seinen \(A, B\) Ereignisse mit \(P(B) > 0\). Dann gilt
      \[P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}\]

      Hierbei heißt \(P(A|B)\) die <i>a posteriori Wahrscheinlichkeit</i>,
      \(P(B|A)\) die <i>likelihood</i>, \(P(A)\) die
      <i>a priori Verteilung über \(A\)</i> und \(P(B)\) die
      <i>a priori Verteilung über \(B\)</i>.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Bayessches_Netz"><dfn>Bayessches Netz</dfn></a></dt>
  <dd>Ein <i>Bayessches Netz</i> ist ein <abbr title="Directed Acyclical Graph">DAG</abbr> TODO
      Bayessche Netze sind zur Modellierung kausaler Zusammenhänge geeignet.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Markov_Random_Field"><dfn>Markov Random Field</dfn></a></dt>
  <dd>Ein <i>MRF</i> ist ein ungerichteter Graph TODO.
      MRFs sind zur Modellierung von Korrelation geeignet.</dd>
  <dt><dfn>Dynamisches Bayessches Netz</dfn></dt>
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
  <dt><a href="https://de.wikipedia.org/wiki/Kalman-Filter"><dfn>Kalman-Filter</dfn></a></dt>
  <dd>TODO</dd>
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


### Probablistisch Relationale Modelle

Slides: 06_Probablistisch_Relationale_Modelle.pdf

TODO

<dl>
  <dt><dfn>Objektorientierte Probablistisch Relationales Modelle</dfn> (<dfn>OPRM</dfn>)</dt>
  <dd>TODO</dd>
</dl>


### Gaussche Prozesse

Slides: 07_Gaussche_Prozesse.pdf

TODO

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Gau%C3%9F-Prozess"><dfn>Gausscher Prozess</dfn></a> (siehe <a href="http://www.gaussianprocess.org/">gaussianprocess.org</a>)</dt>
  <dd>TODO</dd>
</dl>


### Deep Learning

Slides: 08_DeepLearning.pdf

TODO

<dl>
  <dt><dfn>Deep Learning</dfn></dt>
  <dd>TODO</dd>
</dl>


### Convolutional Neural Networks

Slides: 09_ConvolutionalNeuralNetworks.pdf

TODO

<dl>
  <dt><dfn>Convolutional Neural Networks</dfn> (siehe <a href="https://de.wikipedia.org/wiki/Convolutional_Neural_Network">Wikipedia</a>)</dt>
  <dd>TODO</dd>
</dl>


### Spiking Neural Nets

Slides: 10_SpikingNeuralNets.pdf

TODO

<dl>
  <dt><dfn>Spiking Neural Networks</dfn> (siehe <a href="https://de.wikipedia.org/wiki/Gepulste_neuronale_Netze">Wikipedia</a>)</dt>
  <dd>TODO</dd>
</dl>


### Evaluation

Slides: 11_Evaluation.pdf

TODO


## Material und Links

* [Vorlesungswebsite](http://tks.anthropomatik.kit.edu/28_176.php)
* [Ilias](https://ilias.studium.kit.edu/goto_produktiv_crs_429082.html): Ist passwortgeschützt
* [Zusammenfassung der Vorlesung ML 1](//martin-thoma.com/machine-learning-1-course/)


## Übungsbetrieb

Es gibt keine Übungen und keine Übungsblätter.


## Kontakt

* goettl@fzi.de: Sonja Göttl (Sekretariat, zum Anmelden zur Prüfung)


## Termine und Klausurablauf

**Datum**: nach Terminvereinbarung<br/>
**Ort**: ?<br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Erlaubte Hilfsmittel**: keine
