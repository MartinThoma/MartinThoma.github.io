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

Rückblick auf [ML 1](http://martin-thoma.com/machine-learning-1-course/).

Meine Fragen (TODO):

* Folie 27: Was heißt MLNN?


### Semi-Supervised Learning

Slides: 02_Semi-supervised-learning.pdf

TODO

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
  <dd>TODO</dd>
</dl>


### Reinforcement Learning

Slides: 04_Reinforcement_Learning_II.pdf

TODO


### Reinforcement Learning 2

Slides: 04_Reinforcement_Learning_II-2.pdf

TODO


### Dynamische Bayessche Netze

Slides: 05_DynamischeBayesscheNetze.pdf

TODO

<dl>
  <dt><dfn>Dynamisches Bayessches Netz</dfn></dt>
  <dd>TODO</dd>
</dl>



### Probablistisch Relationale Modelle

Slides: 06_Probablistisch_Relationale_Modelle.pdf

TODO

<dl>
  <dt><dfn>Probablistisch Relationales Modelle</dfn></dt>
  <dd>TODO</dd>
</dl>


### Gaussche Prozesse

Slides: 07_Gaussche_Prozesse.pdf

TODO

<dl>
  <dt><dfn>Gausscher Prozess</dfn></dt>
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
* [Zusammenfassung der Vorlesung ML 1](http://martin-thoma.com/machine-learning-1-course/)


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
