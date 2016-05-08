---
layout: post
title: Machine Learning 1
slug: machine-learning-1-course
author: Martin Thoma
date: 2015-11-09 16:02
category: German posts
tags: Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Machine Learning 1&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://www.fzi.de/wir-ueber-uns/organisation/mitarbeiter/address/39/?no_cache=1">Herrn Prof. Dr. Zöllner</a> im Wintersemester 2014/2015 gehört.<br/>Es gibt auch einen Artikel über <a href="//martin-thoma.com/machine-learning-2-course/">Machine Learning 2</a>.</div>

## Folien

### Einordnungskriterien

Slide name: `ML-Einordnungskriterien.pdf`

<table class="table" style="font-size: 0.8em;table-layout:initial;">
    <thead>
        <tr>
            <th rowspan="2" colspan="2">Algorithmus</th>
            <th colspan="2" style="text-align: center; border-right: solid;">Inferenztyp</th>
            <th colspan="2" style="text-align: center; border-right: solid;">Lernebene</th>
            <th colspan="2" style="text-align: center; border-right: solid;">Lernvorgang</th>
            <th colspan="2" style="text-align: center; border-right: solid;">Beispielgebung</th>
            <th colspan="2" style="text-align: center; border-right: solid;">Beispielumfang</th>
            <th colspan="2" style="text-align: center;">Hintergrundwissen</th>
        </tr>
        <tr>
            <td style="text-align: center;"><abbr title="induktiv">ind.</abbr></td>
            <td style="text-align: center; border-right: solid;"><abbr title="deduktiv">ded.</abbr></td>
            <td style="text-align: center;"><abbr title="symbolisch">symb.</abbr></td>
            <td style="text-align: center; border-right: solid;"><abbr title="subsymbolisch">subsymb.</abbr></td>
            <td style="text-align: center;">&uuml;berwacht</td>
            <td style="text-align: center; border-right: solid;"><abbr title="unüberwacht">un&uuml;b.</abbr></td>
            <td style="text-align: center;"><abbr title="inkrementell">inkr.</abbr></td>
            <td style="text-align: center; border-right: solid;"><abbr title="nicht inkrementell">nicht inkr.</abbr></td>
            <td style="text-align: center;">gering</td>
            <td style="text-align: center; border-right: solid;">gro&szlig;</td>
            <td style="text-align: center;"><abbr title="empirisch">emp.</abbr></td>
            <td style="text-align: center;"><abbr title="axiomatisch">axio.</abbr></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2"><abbr title="k nearest neighbor"><span markdown="0">$k$</span>-NN</abbr></td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2"><abbr title="Support Vector Machines"><a href="#svm">SVMs</a></abbr></td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="1" rowspan="2"><a href="#decision-trees">Decision Trees</a></td>
            <td>ID3</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td>ID5R</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="1" rowspan="2"><abbr title="neuronale Netze">NN</abbr></td>
            <td>klassisch</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td>Auto-Encoder</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2">Bayessche Netze</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2"><abbr title="Hidden Markov Models"><a href="#hmm">HMMs</a></abbr></td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2">Version-Space Algorithmus</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2">Specific-to-General Konzeptlernen</td>
            <td style="text-align: center;">?</td>
            <td style="text-align: center; border-right: solid;">?</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">?</td>
            <td style="text-align: center; border-right: solid;">?</td>
            <td style="text-align: center;">?</td>
            <td style="text-align: center; border-right: solid;">?</td>
            <td style="text-align: center;">?</td>
            <td style="text-align: center; border-right: solid;">?</td>
            <td style="text-align: center;">?</td>
            <td style="text-align: center;">?</td>
        </tr>
        <tr>
            <td colspan="2">k-means clustering</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2">AHC</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2">COBWEB</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2">CBR</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center;">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="2"><abbr title="Erklärungsbasierte Generalisierung">EBG</abbr></td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center; border-right: solid;">x</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">x</td>
            <td style="text-align: center; border-right: solid;">&nbsp;</td>
            <td style="text-align: center;">&nbsp;</td>
            <td style="text-align: center;">x</td>
        </tr>
    </tbody>
</table>




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
      die Prämissen $A \rightarrow B$ und $A$ gelten, dann gilt auch $B$.</dd>
  <dt><dfn>Abduktion</dfn> by Peirce</dt>
  <dd>Deduction proves that something must be; Induction shows that something
      actually is operative; Abduction merely suggests that something may
      be.</dd>
</dl>


### Induktives Lernen

Slide name: `MLI_02_InduktivesLernen_slides1.pdf`

<dl>
    <dt><dfn>Version Space</dfn></dt>
    <dd>Der Raum aller Hypotesen, welche mit den Trainingsbeispielen konsistent sind.</dd>
    <dt><dfn>Version Space Algorithmus</dfn></dt>
    <dd>Der Version Space Algorithmus ist ein binärer Klassifikator für
        diskrete Feature-Spaces. Er startet mit der generellsten Hypothese
        $G = (?, \dots, ?)$ - alles ist wahr - und der speziellsten Hypothese
        $S = (\#, \dots, \#)$ - nichts ist wahr. Wenn ein Beispiel mit dem Label
        <code>true</code> gesehen wird, dann wird die speziellste Hypothese
        angepasst und veralgemeinert. Wenn ein Beispiel mit dem Label
        <code>false</code> gesehen wird, wird die generellste Hypothese spezialisiert.<br/>
        So kann man den Raum aller mit den Trainingsdaten konsistenten
        Hypothesen finden.</dd>
    <dt><dfn>Konzept</dfn></dt>
    <dd>Ein <i>Konzept</i> beschreibt eine Untermenge von Objekten oder
        Ereignissen definiert auf einer größerer Menge.</dd>
    <dt><dfn>Konsistenz</dfn></dt>
    <dd>Keine negativen Beispiele werden positiv klassifiziert.</dd>
    <dt><dfn>Vollständigkeit</dfn></dt>
    <dd>Alle positiven Beispiele werden als positiv klassifiziert.</dd>
</dl>

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

Siehe auch:

* [Neuronale Netze](../neuronale-netze-vorlesung/#tocAnchor-1-1-9)
* [Machine Learning 2](../machine-learning-2-course/#tocAnchor-1-1-5)
* [Cat vs. Mouse code](https://github.com/MartinThoma/cat-vs-mouse)
* Berkeley
    * CS188 Intro to AI: [Project 3: Reinforcement Learning](http://ai.berkeley.edu/reinforcement.html)
    * Dan Klein, Pieter Abbeel: [Lecture 10: Reinforcement Learning](https://www.youtube.com/watch?v=w33Lplx49_A) on YouTube. University of California, Berkeley. This expalins TD-learning.
* [What is the Q function and what is the V function in reinforcement learning?](http://datascience.stackexchange.com/q/9832/8820)
* [Demystifying Deep Reinforcement Learning](http://www.nervanasys.com/demystifying-deep-reinforcement-learning/)

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Markow-Entscheidungsproblem"><dfn>Markovsches Entscheidungsproblem</dfn></a> (<dfn>Markov Decision Process</dfn>, <dfn>MDP</dfn>)</dt>
  <dd>Ein Markovsches Entscheidungsproblem ist ein 5-Tupel $S, A, P, R, \gamma$
      mit:

      <ul>
          <li>$S$: Endliche Zustandsmenge (states)</li>
          <li>$A(s)$: Die Menge von möglichen Aktionen im Zustand $s$</li>
          <li>$P(s, s', a) = P(s_{t+1} = s' | s_t = s, a_t = a)$: Die Wahrscheinlichkeit
              im Zeitschritt $t+1$ im Zustand $s'$ zu sein, wenn man zum Zeitpunkt
              $t$ im Zustand $s$ ist und die Aktion $a$ ausführt</li>
          <li>$R(s, s', a) \in \mathbb{R}$: Die direkte Belohnung, wenn durch die Aktion $a$ vom Zustand $s$ in den Zustand $s'$ gekommen ist.</li>
          <li>$\gamma \in [0, 1]$: Der Diskontierungsfaktor, welche die
              Bedeutung von direkten Belohnungen im Vergleich zu künftigen
              Belohnungen anzeigt.</li>
      </ul></dd>
  <dt><a href="https://en.wikipedia.org/wiki/Reinforcement_learning"><dfn>Reinforcement Learning</dfn></a> (<dfn>RL</dfn>, <dfn><a href="https://de.wikipedia.org/wiki/Best%C3%A4rkendes_Lernen">Bestärkendes Lernen</a></dfn>)</dt>
  <dd>Beim bestärkenden Lernen liegt ein Markow-Entscheidungsproblemen vor.
      Es gibt also einen Agenten, der Aktionen ausführen kann. Diese können
      (nicht notwendigerweise sofort) bewertet werden.</dd>
  <dt><dfn>Policy</dfn></dt>
  <dd>Eine <b>policy $\pi: S \rightarrow A$</b> ist die Vorschrift, in
      welchem Zustand welche Aktion ausgeführt werden soll.</dd>
  <dt><dfn>Policy Learning</dfn></dt>
  <dd>Unter <i>Policy Learning</i> versteht man die Suche nach einer
      optimalen Policy $\pi^*$.</dd>
  <dt><dfn>Value-Funktion</dfn></dt>
  <dd>Die Funktion $V^\pi: S \rightarrow \mathbb{R}$ heißt Value-Funktion.
      Sie gibt den erwarteten Wert (nicht die Belohnung, da bei der V-Funktion
      noch der Diskontierungsfaktor eingeht!) eines Zustands $s$ unter der
      policy $\pi$ an.

      Mit $V^*$ wird der Wert unter der optimalen policy bezeichnet.</dd>
  <dt><dfn>Q-Funktion</dfn></dt>
  <dd>Die Funktion $Q^\pi: S \times A \rightarrow \mathbb{R}$ gibt den erwarteten
      Wert einer eines Zustandes $s$ unter der policy $\pi$, wenn die
      Aktion $a$ ausgeführt wird an.

      Es gilt: $$Q^\pi(s, \pi(s)) = V^\pi(s)$$</dd>
   <dt><a name="rl-eligibility-trace"></a><dfn>Eligibility Traces</dfn></dt>
   <dd>Die Idee scheint einfach zu sein, dass man ein späteres Update auch auf
       frühere Ereignisse "zurückpropagiert".
       TODO

       See also: <a href="https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node72.html">Reinforcement Learning: An Introduction</a> by Sutton.
   </dd>
</dl>

* Beispiel für RL: Roboter muss zu einem Ziel navigieren

Algorithmen:

<dl>
    <dt><dfn>Simple Value Iteration</dfn></dt>
    <dd>Simple Value Iteration estimates the value function by updating it
        as long as necessary to converge:

        $$\hat{V}^*(s_t) \leftarrow r_t + \gamma \hat{V}^*(s_{t+1})$$

        "Simple" means that the transition function is deterministic.
        <!--
        In the
        non-deterministic case the update rule is

        $$\hat{V}^*(s_t) \leftarrow r_t + \gamma E(\hat{V}^*(s_{t+1}))$$ -->

        It is explained in

        <ul>
            <li>Sebastian Thrun: <a href="https://www.youtube.com/watch?v=oefOCk3koZo">Unit 9 17 Value Iteration 1</a> on YouTube.</li>
            <li>Sebastian Thrun: <a href="https://www.youtube.com/watch?v=8-pzJXUiXrM">Unit 9 17 Value Iteration 2</a> on YouTube.</li>
            <li>Sebastian Thrun: <a href="https://www.youtube.com/watch?v=glHKJ359Cnc">Unit 9 17 Value Iteration 3</a> on YouTube.</li>
        </ul>
    </dd>
    <dt><dfn>Simple Temporal Difference Learning</dfn></dt>
    <dd>Simple Temporal Difference Learning is just like
        Simple Value Iteration, but now the Value function is updated with
        a learning rate $\alpha$:
        $$\hat{V}^*(s_t) \leftarrow (1-\alpha) \cdot \hat{V}^*(s_t) + \alpha(r_t + \gamma \hat{V}^*(s_{t+1}))$$

        Mehr dazu im <a href="#td-learning">nächsten Abschnitt</a>.
    </dd>
    <dt><dfn>Q-Learning</dfn></dt>
    <dd>Siehe <a href="#q-learning">nächster Abschnitt</a></dd>
    <dt><a name="sarsa" href="https://en.wikipedia.org/wiki/State-Action-Reward-State-Action"><dfn>SARSA</dfn></a> (<dfn>State-Action-Reward-State-Action</dfn>)</dt>
    <dd>SARSA is a learning algorithm which updates the Q-function:

    $$Q(s_t,a_t) \leftarrow (1-\alpha) \cdot Q(s_t,a_t) + \alpha [r_{t+1} + \gamma Q(s_{t+1}, a_{t+1})]$$

    where $\alpha \in (0, 1)$ is the learning rate and $\gamma \in [0, 1]$
    is the discount factor.

    </dd>
    <dt><dfn>SARSA($\lambda$)</dfn></dt>
    <dd>SARSA($\lambda$) ist SARSA mit Eligibility Traces.

    TODO
    </dd>
</dl>


#### <a name="q-learning"></a> Q-Learning

Das "Q" in der Q-Funktion steht für "quality".

* [Q-learning](https://en.wikipedia.org/wiki/Q-learning)
    * [YouTube: Lecture 18: RL Part 1: Q-Learning](https://www.youtube.com/watch?v=yS5F_vm9Ahk): 1:16:11. BrownCS141 Spring 2014.
    * [YouTube: PacMan](https://www.youtube.com/watch?v=3sLV0OJLdns)

Pseudocode:

```text
initialize Q[num_states, num_actions]
start in state s
repeat:
    select and execute action a
    r ← R(s, a)  # Receive reward
    s' ← T(s, a) # Get on new state
    Q[s', a] ← (1- α) * Q[s, a] + α * (r + γ max_{a'} Q[s', a'])
    s ← s'
```

where $\alpha \in (0, 1]$ is a learning rate and $\gamma$ is a discount
factor.

See also:

* [Mario Q-learning](https://www.youtube.com/watch?v=ntZ0Hc1_LsY) on YouTube. 2010.


#### <a name="td-learning"></a> TD-Learning

* R. Sutton und A. Barto: [Temporal-Difference Learning](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node60.html). 1998.

Der TD-Learning Algorithmus beschäftigt sich mit dem Schätzen der Value-Funktion
$V^\pi$ für eine gegebene Policy $\pi$. Das wird auch <i>policy evaluation</i>
oder <i>prediction</i> genannt.

* [TD-Learning](https://de.wikipedia.org/wiki/Temporal_Difference_Learning) (Temporal Difference Learning)


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
  <dt><a href="" name="overfitting"></a><dfn>Overfitting</dfn></dt>
  <dd>Zu starke Anpassung des Klassifizierers an die Lerndaten; geringe
      Generalisierungsfähgikeit</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Structural_risk_minimization"><dfn>Structural Risc Minimization</dfn></a> (<dfn>SRM</dfn>)</dt>
  <dd>Unter <i>Structural risk minimization</i> versteht man die Abwägung
      zwischen einem einfachen Modell und einem komplexen Modell, welches
      auf den Trainingsdaten besser funktioniert aber eventuell mehr unter
      Overfitting leidet.</dd>
  <dt><dfn>Vapnik-Chervonenkis Dimension</dfn> (<dfn>VC-Dimension</dfn>)</dt>
  <dd>Die <abbr title="Vapnik-Chervonenkis">VC</abbr>-Dimension $VC(H, X) \in \mathbb{N} \cup \infty$
      eines Hypothesenraumes $H$ ist gleich der maximalen Anzahl an
      Datenpunkten aus $X$, die von $H$ beliebig in zwei Mengen gespalten
      werden können. Dabei muss es nur eine Teilmenge $X' \subseteq X $ der
      Größe $n$ geben, damit $VC(H, X) \geq n$ gilt.

      Falls beliebige Teilmengen von $X$ durch $H$ separiert werden können,
      so gilt $VC(H, X) = \infty$.

      Praktisch gesehen ist $X$, die Menge aller möglichen Features, sowie
      $H$, die Menge aller möglichen Trennlinien im Feature-Space, vorgegeben.
      Die Frage ist ob man eine Teilmenge $X' \subseteq X$ findet mit
      $|X'| = n$, sodass man für $X'$ jede Mögliche Teilung in zwei
      Mengen durch $H$ realisieren kann.</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Probably_approximately_correct_learning">Probably approximately correct learning</a> (<dfn>PAC</dfn>)</dt>
  <dd>PAC macht eine Aussage über die Anzahl der benötigten Stichproben, wenn
      man einen bestimmten realen Fehler mit einer frei zu wählenden
      Wahrscheinlichkeit bekommen will.</dd>
</dl>

* Lernmaschine wird definiert durch Hypothesenraum $\{h_\alpha: \alpha \in A\}$
  und Lernverfahren. Das Lernverfahren ist die Methode um $\alpha_{\text{opt}}$
  mit Hilfe von Lernbeispielen zu finden.
* Probleme beim Lernen:
    * Größe des Hypothesenraums im Vergleich zur Anzahl der Trainingsdaten.
    * Das Verfahren könnte nur suboptimale Lösungen finden.
    * Das Verfahren könnte die passende Hypothese nicht beinhalten.
* Lernproblemtypen: Sei die Menge der Lernbeispiele in $X \times Y$, mit $X \times Y =$...
    * $\\{Attribut_1, Attribut_2, ...\\} \times \\{True, False\\}$: Konzeptlernen
    * $\mathbb{R}^n \times \\{Klasse_1, ..., Klasse_n\\}$: Klassifikation
    * $\mathbb{R}^n \times \mathbb{R}$: Regression
* Gradientenabstieg, Overfitting
* Kreuzvalidierung
* PAC
    * Folie 35: Was ist eine Instanz der Länge $n$?<br/>
      Eine Hypothese mit $n$ Literalen.


#### Boosting
<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Boosting"><dfn>Boosting</dfn></a></dt>
  <dd>Kombiniere mehrere schwache Modelle um ein gutes zu bekommen, indem
      Trainingsbeispiele unterschiedlich gewichtet werden.</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Bootstrap_aggregating"><dfn>Bagging</dfn></a> (<dfn>Bootstrap aggregating</dfn>)</dt>
  <dd>Kombiniere mehrere schwache Modelle um ein gutes zu bekommen. Dabei
      bekommt jedes schwache Modell nur eine Teilmenge aller Trainingsdaten.</dd>
  <dt><dfn>AdaBoost</dfn> (<dfn>Adaptive Boosting</dfn>; see <a href="https://www.youtube.com/watch?v=ix6IvwbVpw0">YouTube</a>)</dt>
  <dd>Learn a classifier for data. Get examples where the classifier got it
      wrong. Train new classifier on the wrong ones.</dd>
</dl>

* Folie 22:
    * Wofür steht $i$ und welchen Wertebereich hat $i$?<br/>
      → $i$ ist eine Zählvariable, welche die Trainingsdaten durchnummeriert.
    * Stellt $W_k(i)$ die Wahrscheinlichkeit dar, dass Beispiel $i$ im $k$-ten
      Durchlauf für das Training verwendet wird?<br/>
      → Nein. $W_k(i)$ ist das Gewicht des $i$-ten Trainingsbeispiels
      für den $k$-ten klassifikator. Siehe Folie&nbsp;24 und folgende für
      ein Beispiel.


Siehe auch:

* Alexander Ihler: <a href="https://www.youtube.com/watch?v=ix6IvwbVpw0">AdaBoost</a>.


<figure class="aligncenter">
            <a href="../images/2015/12/ml-ensemble-learning.png"><img src="../images/2015/12/ml-ensemble-learning.png" alt="Ensemble Learning Techniques: Boosting, Bagging, Random Subspaces, Pasting, Random Patches" style="max-width:500px;" class=""/></a>
            <figcaption class="text-center">Ensemble Learning Techniques: Boosting, Bagging, Random Subspaces, Pasting, Random Patches</figcaption>
        </figure>


#### VC-Dimension

<dl>
  <dt><dfn>VC-Dimension</dfn>, siehe <a href="https://youtu.be/puDzy2XmR5c">YouTube</a> und [<a href="#ref-mit97" name="ref-mit97-anchor">Mit97</a>]</dt>
  <dd>Sei $H^\alpha = \{h_\alpha : \alpha \in A\}$ der Hypothesenraum. Die
      VC-Dimension $VC(h_\alpha)$ von $H^\alpha$ ist gleich der maximalen
      Anzahl von beliebig platzierten Datenpunkten, die von $H^\alpha$ separiert
      werden können.</dd>
</dl>

* Folie 44: $\eta \in [0, 1]$ ist ein Parameter, der beliebig gewählt
  werden kann. Siehe Info-Box <a href="#fehlerabschaetzung">Abschätzung des realen Fehlers</a>.


### Neuronale Netze

Slide name: `MLI_05_Neuronale_Netze_slides1.pdf`

* Einsatzfelder:
    * Klassifiktion: Spracherkennung, Schrifterkennung
    * Funktionsapproximation
    * Mustervervollständigung: Kodierung, Bilderkennung (NODO: Warum zählt das nicht zu Klassifikation?)
* Perzeptron von Rosenblatt (1960)
    * Auswertung: Input-Vektor und Bias mit Gewichten multiplizieren, addieren und Aktivierungsfunktion anwenden.
    * Training: Zufällige Initialisierung des Gewichtsvektors, addieren von fehlklassifizierten Vektoren auf Gewichtsvektor.
* Gradientenabstieg
* Software:
  * [Lasagne](http://lasagne.readthedocs.org/en/latest/index.html): Python, hat eine exzellente Dokumentation, die auch größtenteils auf explizit auf Literatur verweist und die Formeln hinter den Funktionen direkt angibt.
  * [Google TensorFlow](https://martin-thoma.com/tensor-flow-quick/)

<dl>
    <dt><dfn>Cascade Correlation</dfn> (siehe Fahlman und Lebiere: <a href="http://papers.nips.cc/paper/207-the-cascade-correlation-learning-architecture.pdf">The Cascade-Correlation Learning Architecture</a>)</dt>
    <dd>Cascade Correlation ist ein konstruktiver Algorithmus zum erzeugen
        von Feed-Forward Neuronalen Netzen. Diese haben eine andere Architektur
        als typische multilayer Perceptrons. Bei Netzen, welche durch
        Cascade Correlation aufgebaut werden, ist jede Hidden Unit mit
        den Input-Neuronen verbunden, mit den Output-Neuronen und mit allen
        Hidden Units in der Schicht zuvor.<br/>
        <br/>
        Siehe <a href="https://www.youtube.com/watch?v=1E3XZr-bzZ4">YouTube</a> (4:05 min)
        und <a href="http://datascience.stackexchange.com/q/9672/8820">How exactly does adding a new unit work in Cascade Correlation?</a></dd>
    <dt><a href="https://en.wikipedia.org/wiki/Rprop"><abbr title="Resilient Propagation"><dfn>RPROP</dfn></abbr></a> (siehe <a href="https://www.youtube.com/watch?v=Cy2g9_hR-5Y">YouTube</a> - 15:00min)</dt>
    <dd><i>Rprop</i> ist eine Gewichtsupdate-Regel für neuronale Netze. Sie
        betrachtet nur das Vorzeichen des Gradienten, jedoch nicht den Betrag.
        Jedes Gewicht wird unabhängig von den anderen behandelt.

        Der Algorithmus hat Konstanten $\eta^- \in \mathbb{R}_{\le 1}$ sowie
        $\eta^+ \in \mathbb{R}_{\ge 1}$. Für jedes Gewicht ist außerdem
        $\eta=1$ zu Beginn.

        Bei jedem Gewichtsupdate wird überprüft, ob sich das Vorzeichen des
        Gradienten für dieses Gewicht geändert hat. Falls ja, wird das Gewicht
        um $\eta \cdot \eta^+$ bzw $\eta \cdot \eta^-$ geändert. Außerdem
        kann eine minimale bzw. eine Maximale Änderung gesetzt werden.
        </dd>
    <dt><a href="https://en.wikipedia.org/wiki/Delta_rule"><dfn>Delta-Regel</dfn></a>, siehe <a href="http://www.neuronalesnetz.de/delta.html">neuronalesnetz.de</a></dt>
    <dd>Die Delta-Regel ist ein Lernalgorithmus für neuronale Netze mit nur
        einer Schicht. Sie ist ein Spezialfall des algemeineren
        Backpropagation-Algorithmus und lautet wie folgt:
        $$\Delta w_{ji} = \alpha (t_j - y_j) \varphi'(h_j) x_i$$
        wobei

        <ul>
        <li>$\Delta w_{ji} \in \mathbb{R}$ die Änderung des Gewichts von Input $i$
        zum Neuron $j$,</li>
        <li>$\alpha \in [0, 1]$ die Lernrate (typischerweise $\alpha \approx 0.1$),</li>
        <li>$t_j \in \mathbb{R}$ der Zielwert des Neurons $j$,</li>
        <li>$y_j \in \mathbb{R}$ die tatsächliche Ausgabe,</li>
        <li>$\varphi'$ die Ableitung der Aktivierungsfunktion des Neurons,</li>
        <li>$h_j \in \mathbb{R}$ die gewichtete Summe der Eingaben des Neurons und</li>
        <li>$x_i \in \mathbb{R}$ der $i$-te Input</li>
        </ul>

        ist.
    </dd>
    <dt><dfn>Gradient-Descent Algorithmus</dfn></dt>
    <dd>Der Gradient-Descent Algorithmus ist ein Optimierungsalgorithmus für
        differenzierbare Funktionen. Er startet an einer zufälligen Stelle $x_0$.
        Dann wird folgender Schritt mehrfach ausgeführt:
        $$x_0 \gets x_0 - \alpha \cdot \text(grad) f (x_0)$$
        wobei $\alpha \in (0, 1]$ die Lernrate ist und $f$ die zu
        optimierende Funktion. Dabei könnte $\alpha$ mit der Zeit auch
        kleiner gemacht werden.
    </dd>
    <dt><dfn>Backpropagation</dfn> (siehe <a href="http://neuralnetworksanddeeplearning.com/chap2.html">neuralnetworksanddeeplearning.com</a>)</dt>
    <dd>Der Backpropagation-Algorithmus ist eine Variante des Gradient-Descent
        Algorithmus, welche für <abbr title="multilayer Perceptrons">MLPs</abbr>
        angepasst wurde. Sie besteht aus drei Schritten:

        <ul>
            <li><b>Forward-Pass</b>: Lege die Input-Features an das Netz an und erhalte den Output</li>
            <li><b>Fehlerberechnung</b>: Mache das für alle Daten</li>
            <li><b>Backward-Pass</b>: Passe die Gewichte </li>
        </ul>

        Im Grunde ist Backpropagation nur eine Geschwindigkeitsoptimierte
        Variante des Gradient-Descent Algorithmus, da die Gradienten im
        Backpropagation-Algorithmus auf geschickte Weise berechnet werden.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Radiale_Basisfunktion"><dfn>Radiale Basisfunktion</dfn></a> (<dfn>Radial Basis Function</dfn>, <dfn>RBF</dfn>)</dt>
    <dd>Eine <i>radiale Basisfunktion</i> ist eine Funktion $f: D \rightarrow \mathbb{R}$,
        für die $f(x) = f(\|x\|)$ gilt bzw. allgemeiner, für die ein $c \in D$
        existiert, sodass $f(x, c) = f(\|x - c\|)$ gilt.

        Der Wert der Funktion hängt also nur von der Distanz zum Ursprung bzw.
        allgemeiner zu einem Punkt $c \in D$ ab.

        Ein typisches Beispiel sind gaußsche RBFs:
        $f(x) = e^{-(a (x - c)^2)}$, wobei $a, c$ Konstanten sind.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Radial_basis_function_network"><dfn>Radial-Basis Funktion Netz</dfn></a> (<dfn>RBF-Netz</dfn>)</dt>
    <dd>Ein <i>Radial-Basis Funktion Netz</i> ist eine neuronales Netz,
        welches als Aktivierungsfunktionen RBFs verwendet. Dabei gibt es dann
        für jedes Neuron im Grunde zwei Parameter: Der Radius und das Zentrum
        (vgl. Folie&nbsp;39 für die Gewichtsanpassung).
    </dd>
    <dt><a name="dda-algorithm"></a><dfn>Dynamic Decay Adjustment</dfn> (<dfn>DDA</dfn>)</dt>
    <dd>DDA ist ein konstruktiver Lernalgorithmus für RBF-Netze welcher
        in [<a href="#ref-ber95" name="ref-ber95-anchor">Ber95</a>] vorgestellt
        wird.

        Bei den Netzwerken, die DDA annimmt, gibt es sog. <i>Prototypen</i>.
        Das scheinen einfach Neuronen mit RBF-Aktivierungsfunktionen zu sein,
        welche für eine Klasse stehen.

        Zwei Schwellwerte, $\theta^+$ und $\theta^-$, werden eingeführt.
        Der Schwellwert $\theta^+$ muss beim Training eines Beispiels der
        Klasse $y_1$ von einem Neuron der Klasse $y_1$ überschritten
        werden. Falls das nicht der Fall ist, wird ein neues Neuron
        hinzugefügt.<br/>
        Der Schwellwert $\theta^-$ ist eine obere Grenze für die Aktivierung
        von Neuronen, die zu anderen Klassen gehören. Ist eine Aktivierung
        höher, wird der Radius des zugehörigen Neurons verringert.<br/>
        $\theta^+ = 0.4$ und $\theta^- = 0.2$ sind sinnvolle Werte.
        <br/>
        Laut einem Prüfungsprotokoll lernt DDA nach Vapnik korrekt.<br/>
        <br/>
        Siehe auch: <a href="http://www.ra.cs.uni-tuebingen.de/SNNS/UserManual/node193.html">The Dynamic Decay Adjustment Algorithm</a></dd>
</dl>

#### Siehe auch

* [Neuronale Netze - Vorlesung](//martin-thoma.com/neuronale-netze-vorlesung/)
* [What are prototypes in RBF networks?](http://datascience.stackexchange.com/q/9869/8820)


### Instanzbasiertes Lernen

Slide name: `MLI_06_InstanzbasiertesLernen_slides1.pdf`

<dl>
  <dt><dfn>Instanzenbasiertes Lernen</dfn> bzw. <dfn>Lazy Learning</dfn></dt>
  <dd><i>Instanzenbasiertes Lernen</i> ist ein Lernverfahren, welches einfach nur
      die Beispiele abspeichert, also faul (engl. lazy) ist. Soll der Lerner
      neue Daten klassifizieren, so wird die Klasse des ähnlichsten
      Datensatzes gewählt.</dd>
  <dt><dfn>Case-based Reasoning</dfn> bzw. kurz <dfn>CBR</dfn></dt>
  <dd><i>CBR</i> ist ein allgemeines, abstraktes Framework und kein direkt anwendbarer
      Algorithmus. Die Idee ist, dass nach ähnlichen, bekannten Fällen gesucht
      wird, auf die der aktuelle Fall übertragen werden kann.</dd>
  <dt><dfn>Fall</dfn> im Kontext des CBR</dt>
  <dd>Ein Fall ist eine Abstraktion eines Ereignisses, die in Zeit und Raum
      begrenzt ist. Ein Fall enthält eine Problembeschreibung, eine Lösung und
      ein Ergebnis. Zusätzlich kann ein Fall eine Erklärung enthalten warum
      das Ergebnis auftrat, Informationen über die Lösungsmethode, Verweise
      auf andere Fälle oder Güteinformationen enthalten.</dd>
</dl>

* Beispiel für Lazy Learning: <abbr title="k Nearest Neighbors">$k$-NN</abbr>,
  <abbr title="Case-based Reasoning">CBR</abbr>

* NODO: Folie 3: „Fleißige“ Lernalgorithmen mit dem gleichen Hypothesenraum sind
  eingeschränkter - was ist damit gemeint? Was sind fleißige Lernalgorithmen?
  Lernalgorithmen, welche den meisten Rechenaufwand beim Lernen investieren, wo
  aber das auswerten vergleichsweise billig ist?


### <a name="svm"></a> SVM

Slide name: `MLI_07_SVM_slides1.pdf`

Eine Erklärung von <abbr title="Support Vector Machines">SVMs</abbr>
findet sich im Artikel [Using SVMs with sklearn](//martin-thoma.com/svm-with-sklearn/).

* SVMs sind laut Vapnik die Lernmaschine mit der kleinsten möglichen VC-
  Dimension, falls die Klassen linear trennbar sind.
* Primäres Optimierungsproblem: Finde einen Sattelpunkt der Funktion<br/>
  $L_P = L(\vec{w}, b, \vec{\alpha}) = \frac{1}{2}\|\vec{w}\|^2 - \sum_{i=1}^N \alpha_i (y_i(\vec{w}\vec{x_i}+b)-1)$
  wobei $\alpha_1, \dots, \alpha_N \geq 0$ Lagrange-Multiplikatoren sind
* Soft Margin Hyperebene
* Der Parameter $C$ dient der Regularisierung. Ist $C$ groß gibt es wenige
  Missklassifikationen in der Trainingsdatenmenge. Ist $C$ klein, werden die
  Margins größer.
* Nichtlineare Kernelmethoden
* Kernel-Trick


<div class="alert alert-info"><h4><a name="fehlerabschaetzung"></a>Abschätzung des realen Fehlers</h4>
Der reale Fehler kann durch den empirischen Fehler und die VC-Dimension wie
folgt abgeschätzt werden:

Mit Wahrscheinlichkeit $P(1-\eta)$ gilt:
$$E(h_\alpha) \leq E_{emp}(h_\alpha) + \sqrt{\frac{VC(h_\alpha)}{N} \cdot (\log(2 N / VC(h_\alpha)) + 1) - \frac{\log(\eta  / 4)}{N}}$$

wobei gilt:

<ul>
    <li>$E(h_\alpha)$ ist der reale Fehler der mit der Hypothese $h_\alpha$
        gemacht wird</li>
    <li>$E_{emp}(h_\alpha)$ ist der empirische Fehler der mit der Hypothese $h_\alpha$
        gemacht wird</li>
    <li>$VC(h_\alpha)$ ist die VC-Dimension der Lernmaschine</li>
    <li>$N$ ist die Anzahl der Lernbeispiele</li>
    <li>$0 \leq \eta \leq 1$</li>
</ul>

Dieser Term wird in der <i>Structural Risc Minimization</i> minimiert.
</div>


### <a name="decision-trees"></a> Entscheidungsbäume

Slide name: `MLI_08_Entscheidungsbaeume_slides1.pdf`

<dl>
  <dt><dfn>Entscheidungsbaum</dfn> (<dfn>Decision Tree</dfn>)</dt>
  <dd>Ein Entscheidungsbaum ist ein Klassifikator in Baumstruktur. Die
      inneren Knoten des Entscheidungsbaumes sind Attributtests, die Blätter
      sind Klassen.<br/>
      <br/>
      Typischerweise wird ein Entscheidungsbaum aufgebaut, indem das jeweilige
      Attribut mit dem höchsten Information Gain als nächster Knoten hinzugefügt
      wird. Siehe
      <a href="https://en.wikipedia.org/wiki/Information_gain_in_decision_trees">Information gain in decision trees</a> für weitere Informationen.</dd>
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
  $Entropie(S) = - p_\oplus \log_2 p_\oplus - p_\ominus \log_2 p_\ominus$
  wobei $\oplus$ die positiven Beispiele und $\ominus$ die negativen Beispiele
  bezeichnet.
* Folie 41: Wo ist der Vorteil von ID5R im Vergleich zu ID3, wenn das
  Ergebnis äquivalent ist?<br/>
  → ID5R kann inkrementell verwendet werden. Es ist bei ID5R - im Gegensatz
  zu ID3 - also nicht nötig bei neuen Trainingsdaten neu zu trainieren.
* Random Forest: Erstelle mehrere Entscheidungsbäume mit einer zufälligen
  Wahl an Attributen. Jeder Baum stimmt für eine Klasse und die Klasse, für die
  die meisten Stimmen, wird gewählt.


### Bayes Lernen

Slide name: `MLI_09_BayesLernen_slides1.pdf`

Siehe auch:

* [Dynamische Bayesssche Netze](https://martin-thoma.com/machine-learning-2-course/#dynamic-bayes-networks) in ML2

<dl>
  <dt><dfn>Satz von Bayes</dfn></dt>
  <dd>Seien $A, B$ Ereignisse, $P(B) > 0$. Dann gilt:
      $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$<br/>
      Dabei wird $P(A)$ a priori Wahrscheinlichkeit, $P(B|A)$ likelihood,
      und $P(A|B)$ a posteriori Wahrscheinlichkeit genannt.</dd>
  <dt><dfn>Naiver Bayes-Klassifikator</dfn></dt>
  <dd>Ein Klassifizierer heißt naiver Bayes-Klassifikator, wenn er den
      Satz von Bayes unter der naiven Annahme der Unabhängigkeit der Features
      benutzt.</dd>
  <dt><dfn>Produktregel</dfn></dt>
  <dd>$P(A \land B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$</dd>
  <dt><dfn>Summenregel</dfn></dt>
  <dd>$P(A \lor B) = P(A) + P(B) - P(A \land P)$</dd>
  <dt><dfn>Theorem der totalen Wahrscheinlichkeit</dfn></dt>
  <dd>Es seien $A_1, \dots, A_n$ Ereignisse mit $i \neq j \Rightarrow A_i \cap A_j = \emptyset \;\;\;\forall i, j \in 1, \dots, n$ und $\sum_{i=1}^n A_i = 1$. Dann gilt:<br/>
      $P(B) = \sum_{i=1}^n P(B|A_i) P(A_i)$</dd>
  <dt><dfn>Maximum A Posteriori Hypothese</dfn> (MAP-Hypothese)</dt>
  <dd>Sei $H$ der Raum aller Hypothesen und $D$ die Menge der beobachteten
      Daten. Dann heißt<br/>
      $h_{MAP} = \text{arg max}_{h \in H} P(h|D) \cdot P(h)$<br/>
      die Menge der Maximum A Posteriori Hypothesen.</dd>
  <dt><dfn>Maximum Likelihood Hypothese</dfn> (ML-Hypothese)</dt>
  <dd>Sei $H$ der Raum aller Hypothesen und $D$ die Menge der beobachteten
      Daten. Dann heißt<br/>
      $h_{ML} = \text{arg max}_{h \in H} P(h|D)$<br/>
      die Menge der Maximum Likelihood Hypothesen.</dd>
  <dt><dfn>Normalverteilung</dfn></dt>
  <dd>Eine stetige Zufallsvariable $X$ mit der Wahrscheinlichkeitsdichte
      $f\colon\mathbb{R}\to\mathbb{R}$, gegeben durch<br/>
      $f(x) = \frac {1}{\sigma\sqrt{2\pi}} e^{-\frac {1}{2} \left(\frac{x-\mu}{\sigma}\right)^2}$<br/>
      heißt $\mathcal N\left(\mu, \sigma^2\right)$-verteilt, normalverteilt
      mit den Erwartungswert $\mu$ und Varianz $\sigma^2$.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Minimum_Description_Length"><dfn>Prinzip der minimalen Beschreibungslänge</dfn></a></dt>
  <dd>Das Prinzip der minimalen Beschreibungslänge ist eine formale
      Beschreibung von Ockhams Rasiermesser. Nach diesem Prinzip werden
      Hypothesen bevorzugt, die zur besten Kompression gegebener Daten führen.
  </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Gibbs-Sampling"><dfn>Gibbs-Algorithmus</dfn></a> (<a href="http://stats.stackexchange.com/a/10216/25741">stats.stackexchange</a>)</dt>
  <dd>Der Algorithmus von Gibbs ist eine Methode um Stichproben von bedingten
      Verteilungen zu erzeugen.
  </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Bedingte_Unabh%C3%A4ngigkeit"><dfn>Bedingte Unabhängigkeit</dfn></a></dt>
  <dd>Seien $X, Y, Z$ Zufallsvariablen. Dann heißt $X$ bedingt unabhängig
      von $Y$ gegeben $Z$, wenn $$P(X|Y,Z) = P(X|Z)$$ gilt.
  </dd>
  <dt><a href="https://en.wikipedia.org/wiki/Additive_smoothing"><dfn>Add $k$ smoothing</dfn></a></dt>
  <dd>Unter Add-$k$-smoothing versteht man eine Technik, durch die
      sichergestellt wird, dass die geschätzte Wahrscheinlichkeit für kein
      Ereignis gleich null ist. Wenn man $d \in \mathbb{N}$ mögliche
      Ergebnisse eines Experiments hat, $N \in \mathbb{N}$ experimente
      durchgeführt werden, dann schätzt man die Wahrscheinlichkeit von dem
      Ergebnis $i$ mit
      $$\hat{\theta_i} = \frac{x_i + k}{N+ kd}, $$
      wobei $x_i$ die Anzahl der Beobachtungen von $i$ ist und $k \geq 0$
      der Glättungsparameter ist.
  </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Bayessches_Netz" id="bayes-net"><dfn>Bayessches Netz</dfn></a> (Quelle: [<a href="#ref-dar09" name="ref-dar09-anchor">Dar09</a>])</dt>
  <dd>Ein bayessches Netz ist ein Tupel $(G, \Theta)$ mit:

  <ul>
      <li>$G = (\mathbf{X}, E)$ ist ein <abbr title="Directed Acyclical Graph">DAG</abbr>
          der <b>Struktur</b> des Bayesschen Netzwerks genant wird. Dabei
          ist $\mathbf{X} = \{X_1, X_2, \dots, X_n\}$ die Menge der Knoten.
          Jeder Knoten entspricht einer Zufallsvariablen (z.B. Attribut).<br/>
          <br/>
          Existiert eine gerichtete Kante $(X_i, X_j) \in E$, so existiert
          eine direkte Abhängigkeit zwischen $X_i$ und $X_j$.</li>
      <li>$\Theta$ ist die Menge der bedingten Wahrscheinlichkeitsverteilungen
          und heißt <b>Parametrisierung</b> des bayesschen Netzwerks. Es
          existiert für jedes $X_i$ genau eine Verteilung in $\Theta$,
          welche in Abhängigkeit der Elternknoten beschrieben wird.</li>
  </ul>

  In einem bayesschem Netz berechnet sich die gemeinsame Verteilung wie folgt:

  $$P(X_1, \dots, X_N) = \prod_{i=1}^N P(X_i | \text{Eltern}(X_i))$$

  Die Modelierung von Bayesschen Netzen erfolgt meist durch den Menschen mit
  Expertenwissen. Alternativ kann die Struktur durch
  <abbr title="Markov Chain Monte Carlo">MCMC</abbr> bestimmt werden.
  Sobald die Struktur gegeben ist wird die Menge der Verteilungen $\Theta$
  durch den Expectation Maximization Algorithmus bestimmt.
  </dd>
</dl>

Fragen:

* Folie 23: Warum ist $h_{MAP(x)}$ nicht die wahrscheinlichste
  Klassifikation?
* Folie 24: Was ist $V$?
* [Is there any domain where Bayesian Networks outperform neural networks?](http://datascience.stackexchange.com/q/9818/8820)


### <a name="hmm"></a> HMM

Slide name: `MLI_10_HMM_slides1.pdf`

<dl>
  <dt><dfn>Markov-Bedingung</dfn> (Beschränkter Horizont)</dt>
  <dd>$P(q_{t+1}=S_{t+1}|q_t = S_t, q_{t-1} = S_{t-1}, \dots) = P(q_{t+1}=S_{t+1}|q_t = S_t)$</dd>
  <dt><dfn>Hidden Markov Modell</dfn> (<dfn>HMM</dfn>)</dt>
  <dd>Eine HMM ist ein Tupel $\lambda = (S, V, A, B, \Pi)$:
      <ul>
          <li>$S = \{S_1, \dots, S_n\}$: Menge der Zustände</li>
          <li>$V = \{v_1, \dots, v_m\}$: Menge der Ausgabezeichen</li>
          <li>$A \in [0,1]^{n \times n}$ = (a_{ij}): Übergangsmatrix, die die Wahrscheinlichkeit von Zustand $i$ in Zustand $j$ zu kommen beinhaltet</li>
          <li>$B = (b_{ik})$ die Emissionswahrscheinlichkeit $v_k$ im Zustand $S_i$ zu beobachten</li>
          <li>$\Pi = (\pi_i) = P(q_1 = i)$: Die Startverteilung, wobei $q_t$ den Zustand zum Zeitpunkt $t$ bezeichnet</li>
      </ul></dd>
  <dt><a href="https://de.wikipedia.org/wiki/Forward-Algorithmus"><dfn>Vorwärts-Algorithmus</dfn></a></dt>
  <dd>Der Vorwärts-Algorithmus löst das Evaluierungsproblem. Er benutzt dazu
      dynamische Programmierung: Die Variablen $\alpha_t(i) = P(o_1 o_2 \dots o_t; q_t = s_i | \lambda)$ gibt die Wahrscheinlichkeit
      an zum Zeitpunkt $t \in 1 \leq t \leq T$ im Zustand $s_i \in S$ zu
      sein und die Sequenz $o_1 o_2 \dots o_t$ beobachtet zu haben. Diese
      werden rekursiv berechnet. Dabei beginnt man mit Zeitpunkt $t=1$, berechnet
      die Wahrscheinlichkeit $o_1$ beobachtet zu haben für jeden Zustand.
      <br/>
      Die Wahrscheinlichkeit der beobachteten Sequenz, gegeben die HMM $\lambda$,
      ist dann einfach die Summe der $\alpha_i$ des letzten Zeitschritts.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Backward-Algorithmus"><dfn>Rückwärts-Algorithmus</dfn></a></dt>
  <dd>Der Rückwärts-Algorithmus löst das Dekodierungsproblem. Er benutzt dazu
      dynamische Programmierung: Die Variablen $\beta_t(i) = P(o_{t+1} o_{t+2} \dots o_{T}|q_t = s_i, \lambda)$ geben
      die Wahrscheinlichkeit an, dass die Sequenz $o_{t+1} o_{t+2} \dots o_{T}$
      beobachtet werden wird, gegeben das HMM&nbsp;$\lambda$ und den
      Startzustand&nbsp;$s_i$.</dd>
  <dt><dfn>Forward-Backward Algorithm</dfn></dt>
  <dd>Der Forward-Backward Algorithmus berechnet für jeden Zeitpunkt die
      Wahrscheinlichkeitsverteilung der Zustände. Dafür glättet er die Werte
      des Vorwärts- und des Rückwärts-Algorithmus:
      $$\gamma_t(i) = \frac{\alpha_t(i) \beta_t(i)}{P(O|\lambda)}$$

      Er findet jedoch nicht die wahrscheinlichste Zustandssequenz.
      </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Viterbi-Algorithmus"><dfn>Viterbi-Algorithmus</dfn></a></dt>
  <dd>Löst P2:
      <br/>
  Siehe <a href="../apply-viterbi-algorithm/">How to apply the Viterbi algorithm</a></dd>
  <dt><a href="https://de.wikipedia.org/wiki/Baum-Welch-Algorithmus"><dfn>Baum-Welch-Algorithmus</dfn></a></dt>
  <dd>Löst P3:

      Gegeben sei eine Trainingssequenz $O_{\text{train}}$ und ein Modell
      $$\lambda = \{S, V, A, B, \Pi\}$$


      Gesucht ist ein Modell

      $$\bar \lambda = \text{arg max}_{\bar \lambda = \{S, V, \bar A, \bar B, \bar Pi\}} P(O_{\text{train}}|\lambda)$$

      Der Baum-Welch-Algorithmus geht wie folgt vor:

      <ol>
          <li>Bestimme $P(O_{\text{train}} | \lambda)$</li>
          <li>Schätze ein besseres Modell $\bar \lambda$: TODO - Genauer! (Folie 31 - 36)</li>
      </ol>

      Iteriere diese Schritte so lange, bis ein lokales Maximum gefunden wurde.
      </dd>
  <dt><dfn>Ergodisches Modell</dfn></dt>
  <dd>Unter dem <i>ergodischen Modell</i> versteht man im Kontext von
      <abbr title="Hidden Markov Models">HMMs</abbr> die vollverbundene
      Topologie inclusive Schleifen.</dd>
  <dt><dfn>Bakis-Modell</dfn> (<dfn>Links-nach-Rechts-Modell</dfn>)</dt>
  <dd>Unter dem <i>Bakis-Modell</i> versteht man im Kontext von
      <abbr title="Hidden Markov Models">HMMs</abbr> eine Links-nach-Rechts
      Topologie, bei der maximal ein Zustand übersprungen werden kann.
      Das bedeutet, es gibt eine Ordnung über den Zuständen. Von einem
      Zustand $i$ kommt man in die Zustände $i, i+1, i+2$.</dd>
</dl>

Die drei Probleme von HMMs sind

* **P1 - Evaluierungsproblem**: Wie wahrscheinlich ist eine Sequenz
  $\bf{o} = o_1 o_2 \dots o_T$
  gegeben ein HMM $\lambda$, also $P(\bf{o}|\lambda)$.
* **P2 - Dekodierungsproblem**: Finden der wahrscheinlichsten Zustandssequenz <span markdown="0">$s_1, \dots, s_T$</span>,
  gegeben eine Sequenz von Beobachtungen $\bf{o} = o_1 o_2 \dots o_T$.
* **P3 - Lernproblem**: Optimieren der Modellparameter


Anwendungen:

* Gestenerkennung
* Phonem-Erkennung


### Markov Logik Netze

Slides: `MLI_11-MLN_slides1`

Markov Logik Netze sind Sammlungen von Tupeln aus Gewichten $w_i$ und
prädikatenlogischen Formeln. Die Idee hinter Markov Logik Netzen ist ein
aufweichen der harten Bedingungen der Prädikatenlogik. Eine prädikatenlogische
Formel ist entweder wahr oder falsch. Eine Formel in MLNs kann auch "meistens"
erfüllt sein. Das wird durch das Gewicht repräsentiert.

<dl>
  <dt><a href="https://de.wikipedia.org/wiki/Markov_Logik_Netze"><dfn>Markov Logik Netze</dfn></a> (<dfn>MLN</dfn>)</dt>
  <dd>Ein Markov Logik Netz ist ein Menge aus Tupeln $L = (F_i, w_i)$, wobei $F_i$ eine Formel der Prädikatenlogik erster Ordnung und $w_i \in \mathbb{R}$ ein Gewicht ist.
      Ein MLN ist eine Schablone für ein MRF.</dd>
  <dt><a name="mrf-definition"></a><dfn>Markov Random Field</dfn> (<dfn>Markov Netzwerk</dfn>, <dfn>MRF</dfn>)</dt>
  <dd>Ein MRF ist ein ungerichtetes Probabilistisches Grafisches Modell.<br/>
      MRFs sind zur Modellierung von Korrelation geeignet.</dd>
  <dt><a name="mln-jpd"></a><dfn>Verbundwahrscheinlichkeit in MLNs</dfn></dt>
  <dd>$P(x) = \frac{1}{Z} \exp(\sum_{i} w_i f_i(x))$ wobei $f_i$ das $i$-te Feature und $w_i$ ein
           Gewicht ist. Beispielsweise könnte $$f_i(x) = f_i(\text{smoking}, \text{cancer}) = \begin{cases}1 &\text{if } \neg \text{smoking} \lor \text{cancer}\\ 0 &\text{otherwise}\end{cases}$$
           gelten.</dd>
  <dt><a name="mln-inference"></a><dfn>Inferenz in MLNs</dfn></dt>
  <dd><abbr title="Maximum a posteriori">MAP</abbr>:
      \begin{align}\text{arg max}_y P(y | x) &= \frac{1}{Z} \exp(\sum_{i} w_i n_i(x, y))\\
         &= \sum_{i} w_i n_i(x, y) \end{align}</dd>
</dl>


Siehe auch:

* Matthew Richardson, Pedro Domingos: [Markov logic networks](http://link.springer.com/article/10.1007/s10994-006-5833-1)
* Pedro Domingos, Matthew Richardson: [Markov Logic: A Unifying Framework for Statistical Relational Learning](http://homes.cs.washington.edu/~pedrod/papers/srl04.pdf), 2007.
* Coursera: [Probabilistic Graphical Models](https://www.coursera.org/course/pgm)
* Pedro Domingos: [Unifying Logical and Statistical AI](https://www.youtube.com/watch?v=bW5DzNZgGxY), September 2009.
* Software: [Alchemy](https://alchemy.cs.washington.edu/)
* YouTube: [11 4 M4 Markov Logic Formalism 11 39](https://www.youtube.com/watch?v=BLAoNJvQZQ4)


### Evolutionäre Algorithmen

Slides: `MLI_12_EvolutionaereAlgorithmen_slides1.pdf`

Siehe auch:

* [<a href="#ref-mit97" name="ref-mit97-anchor">Mit97</a>]
* [DEAP](http://deap.readthedocs.org/en/master/index.html) wenn du es
  ausprobieren willst.
* [Difference between genetic algorithms and evolution strategies?](http://stackoverflow.com/q/7787232/562769)

<dl>
    <dt><dfn>Individuum</dfn></dt>
    <dd>Eine mögliche Hypothese</dd>
    <dt><dfn>Population</dfn> (<dfn>Generation</dfn>)</dt>
    <dd>Hypothesenmenge</dd>
    <dt><dfn>Erzeugung von Nachkommen</dfn></dt>
    <dd>Generierung neuer Hypothesen durch Rekombination und Mutation</dd>
    <dt><dfn>Fitness-Funktion</dfn></dt>
    <dd>Die Fitness-Funktion ist das zu optimierende Kriterium. Sie beschreibt
        die Güte einer Hypothese.</dd>
    <dt><dfn>Selektion</dfn></dt>
    <dd>Auswahl der Hypothesen, welche die beste Problemlösung erzeugen.</dd>
    <dt><dfn>Evolutionäre Strategien</dfn></dt>
    <dd>Das Wissen wird durch reele Zahlen und Vektoren repräsentiert.</dd>
    <dt><dfn>Genetische Programmierung</dfn></dt>
    <dd>Das Wissen wird duch baumartige Strukturen repräsentiert.</dd>
    <dt><dfn>Mutation</dfn></dt>
    <dd>Unter <i>Mutation</i> versteht man die zufällige Änderung einzelner
        Gene.

        Beispiele:

        <ul>
            <li>Bit-Inversion: Zufällig Gleichverteilt pro Gen / Feste Anzahl,
                aber zufällige Gene</li>
            <li>Translation: Verschieben von Teilsequenzen</li>
            <li>Invertiertes Einfügen</li>
            <li>Spezielle Mutationsoperatoren sind anwendungsspezifisch</li>
        </ul>
    </dd>
    <dt><dfn>Rekombination</dfn></dt>
    <dd>Bei der <i>Rekombination</i> werden die Eigenschaften zweier Eltern
        gemischt. Dies kann Diskret passieren, wenn manche Gene von einem
        Elternteil übernommen werden und andere vom anderen Elternteil.
        Alternativ kann die Rekombination auch durch <i>intermediäre
        Rekombination</i> passieren. Das bedeutet, das ein Gen gemittelt
        wird.</dd>
</dl>

Grundalgorithmus:

```text
Fitness-Function f
Population p

while f(p) ≠ optimal:
    p_parents ← selection(p)
    p_children ← generate_children(p_parents)
    p ← p_parents + p_children
    fitness ← f(p)
    p ← selection_kill(p, fitness)
```

Probleme:

* Genetischer Drift: Manche Individuen vermehren sich zufällig mehr als andere.
  Diese sind nicht unbedingt besser für das Problem geeignet.
* Crowding, Ausreißerproblem: Fitte Individuen dominieren die Population. Das
  ist ein Problem wegen lokaler Maxima.


Mating:

* Inselmodell: Die Evolution läuft weitgehend getrennt. Es passiert nur
  vereinzelt, dass Individuen der Inseln ausgetauscht werden.
* Nachbarschaftsmodell: Nachkommen dürfen nur von Individuen erzeugt werden,
  die in ihrer Nachbarschaft die beste Fitness besitzen
* Globales Modell: Alle dürfen sich mit allen verbinden.

Evolution:

* Lamark'sche Evolution: Die Individuen ändern sich nach der Erzeugung. Sie
  lernen also. Dabei wird der Genotyp verändert und auch vererbt.
* Baldwin'sche Evolution: Die Individuen ändern sich nach der Erzeugung, aber
  der Genotyp bleibt gleich
* Hybride Verfahren: Es gibt sich verändernde und gleich bleibende Phänotypen.


Anwendungen:

* Traveling Salesman
* Flugplanoptimierung
* Mischung von Kaffesorten
* Cybermotten: Motten müssen optimales Muster finden, um sich vor einer Fläche
               weißen Rauschens zu verbergen.
* Snakebot (Ivan Tanev) [<a href="#ref-pro06" name="ref-pro06-anchor">Pro06</a>]


### Deduktives Lernen

Slides: `MLI_13_DeduktivesLernen_slides1.pdf`

Siehe auch: [Formale Systeme](//martin-thoma.com/formale-systeme/)

<dl>
    <dt><dfn>Modus Ponens</dfn></dt>
    <dd>$$\frac{A, A \rightarrow B}{B}$$</dd>
    <dt><dfn>Erklärungsbasiertes Lernen</dfn> (<dfn>EBL</dfn>, <dfn>Explanation Based Learning</dfn> by [<a href="#ref-mit97" name="ref-mit97-anchor">Mit97</a>])</dt>
    <dd>The key insight behind explanation-based generalization is that it is
        possible to form a justified generalization of a single positive
        training example provided the learning system is endowed with some
        <b>explanatory capabilitie</b>. In particular, the system must be able
        to explain to itself <b>why the training example is an example of the
        concept</b> under study. Thus, the generalizer is presumed to possess a
        definition of the concept under study as well as <b>domain
        knowledge</b> for constructing the required explanation.</dd>
    <dt><dfn>Explanation Based Generalization</dfn> (<dfn>EBG</dfn>)</dt>
    <dd>EBG ist ein Prozess, bei dem implizites Wissen in explizites
        umgewandelt wird.

        EBG geht wie folgt vor:

        <ol>
            <li>Explain: Finden einer Erklärung, warum das Beispiel die
                Definition des Zielkonzepts erfüllt. Dies ist einfaches
                Anwenden des Modus Ponens.</li>
            <li>Generalize: Generalisieren der Erklärung; bestimme also
                hinreichende Bedingungen unter denen die gefundene
                Erklärungsstruktur gültig ist.</li>
        </ol>

        Bei der EBG werden also Makro-Operatoren erzeugt.

        Ein Beispiel für Software welche EBG benutzt ist
        <abbr title="STanford Resarch Institute Problem Solver">STRIPS</abbr>.
    </dd>
    <dt><dfn>KBANN</dfn> (<dfn>Knowledge-Based Artificial Neural Networks</dfn>)</dt>
    <dd>KBANN ist ein hybrides Verfahren. Die Idee ist ein neuronales Netz
        geschickt zu konstruieren. Dieses wird dann wie gewohnt mit
        Gradient Descent durch Trainingsbeispiele verfeinert.

        Der Algorithmus gibt eine Netzarchtiktur vor:
        <ul>
             <li>Dabei wird pro Instanzattribut ein Netz-Input verwendet. Für
                 jede Klausel wird ein Neuron hinzugefügt.</li>
             <li>Dieses ist mit dem Instanzattribut durch das Gewicht $w$
                 verbunden wenn es nicht negiert ist, sonst durch das Gewicht
                 $-w$.</li>
             <li>Der Schwellwert der Aktivierungsfunktion wird auf
                 $-(n- 0.5)w$ gesetzt, wobei $n$ die Anzahl der nicht-negierten
                 Bedingungsteile ist.</li>
            <li>Verbinde die restlichen Neuronen von Schicht $i$ mit Schicht
                $i+1$ indem zufällige kleine Gewichte gesetzt werden.</li>
         </ul>

         Angewendet werden kann KBANN:
         <ul>
             <li>Lernen von physikalischen Objektklassen</li>
             <li>Erkennung von biologischen Konzepten in DNS-Sequenzen</li>
         </ul>
    </dd>
</dl>


### <a name="unsupervised-learning"></a> Unüberwachte Lernverfahren

Slides: `MLI_14_UnueberwachtesLernen_slides1.pdf`

<dl>
    <dt><dfn>$k$-means Clustering</dfn></dt>
    <dd>Der $k$-means Clustering Algorithmus finden $k$ Cluster in einem
        Datensatz. Dabei ist $k \in \mathbb{N}_{\geq 1}$ vom Benutzer zu
        wählen.

        Zuerst initialisert $k$-means die Zentroiden, also zentrale Punkte
        für Cluster, zufällig. Dann geht $k$-means geht iterativ vor:

        <ol>
            <li>Weise jeden Datenpunkt seinem nächsten Cluster zu.</li>
            <li>Verschiebe die $k$ Zentroide in ihr Clusterzentrum</li>
        </ol>

        Siehe auch: <a href="//martin-thoma.com/k-nearest-neighbor-classification-interactive-example/">Interaktives Beispiel</a>
    </dd>
    <dt><dfn>Fuzzy $k$-means</dfn></dt>
    <dd>Im Gegensatz zum $k$-means Algorithmus, wo jeder Datenpunkt in genau
        einem Cluster ist, weißt der Fuzzy $k$-means Algorithmus jedem
        Datenpunkte eine Zugehörigkeitswahrscheinlichkeit zu. Je weiter
        der Datenpunkt vom Zentroid entfernt ist, desto unwahrscheinlicher
        wird die Zugehörigkeit.

        Die Cluster-Zugehörigkeit des Datenpunktes $x_i$ zum Cluster $c_j$
        kann als Wahrscheinlichkeit in Abhängigkeit der Distanz
        $$d_{ij} = |x_i - z_j|^2$$
        zum Zentroiden
        $z_j$ ausgedrückt werden:
        $$P(c_j | x_i) = \frac{(\frac{1}{d_{ij}})^{\frac{1}{b-1}}}{\sum_{r=1}^k (\frac{1}{d_{ir}})^{\frac{1}{b-1}}}$$
        wobei $b \in \mathbb{R}_{\geq 1}$ ein frei zu wählender Parameter ist.

        Die Zentroide werden dann wie folgt neu berechnet:

        $$z_j = \frac{\sum_{i=1}^n [P(z_j|x_i)]^b \cdot x_i}{\sum_{i=1}^n [P(z_j | x_i)]^b}$$
    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Hierarchische_Clusteranalyse"><dfn>Hierarchisches Clustern</dfn></a></dt>
    <dd>Die Idee des hierarchischen Clusterns ist die iterative Vereinigung
        von Clustern zu größeren Clustern.

        Ergebisse können durch ein Dendrogramm beschrieben werden.

        Anwendung: Einordnung von Schrauben in ein Ordnungssystem
    </dd>
    <dt><dfn>Agglomerative Hierarchical Clustering</dfn> (<dfn>AHC</dfn>)</dt>
    <dd>AHC ist ein hierarchisches Clusteringverfahren.

    Dabei ist ein Clusterdistanz-Schwellwert $t \in \mathbb{R}$ und eine
    minimale Cluster-Anzahl $k \in \mathbb{N}$ zu wählen. Auch ein Distanzmaß
    für Cluster (nearest neighbor, farest neighor, mean distance, ...) ist
    als Hyperparameter zu wählen.

    Dann geht AHC wie folgt vor:

    <div class="highlight">
       <pre><code class="language-text" data-lang="text">
c ← k  # Minimale Anzahl an Clustern
c' ← n  # Anzahl der Datenpunkte

# Weise jedem Punkt sein eigenes Clusterzentrum zu
for i in range(1, n):
    D_i ← {x_i}

# Vereinige Clusterzentren
do:
    c' := c' -1
    find closest clusters D_i, D_j
    if d(D_i, D_j) ⩽ t:
        merge(D_i, Dj)
    else:
        break
until c = c'
    </code></pre>
    </div>
    </dd>
    <dt><a href="https://en.wikipedia.org/wiki/Conceptual_clustering"><dfn>Begriffliche Ballung</dfn></a></dt>
    <dd>Bei Algorithmen der Begrifflichen Ballung werden Konzeptbeschreibungen
        generiert.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Cobweb_(clustering)"><dfn>COBWEB</dfn></a></dt>
    <dd>Cobweb ist ein Algorithmus zur begrifflichen Ballung. Er lernt durch
        inkrementelles Aufbauen eines Strukturbaumes. Dabei sind nominale
        Attribute gestattet. Dabei wird ein Datenpunkt $x_i$ zum Cluster
        $c_j$ geclustert, wenn man die Attributwerte von $x_i$ durch die
        Kentniss von $c_j$ gut vorhersagen kann (<span markdown="0">$P(x_i | c_j)$</span>,
        predictability) und zugleich der Cluster gut vorhergesagt werden kann,
        wenn die Attributwerte gegeben sind (<span markdown="0">$P(c_j|x_i)$</span>, predictiveness).

        Es soll also in inter-Klassenähnlichkeit minimiert und die
        intra-Klassenähnlichkeit maximimiert werden. Dafür wird die
        Category Utility verwendet:

        <div>
        $$\text{CU} = \sum_{k=1}^K \sum_{i=1}^I \sum_{j=1}^{J(i)} P(A_i = V_{ij}) \cdot P(A_i = V_ij | C_k) \cdot P(C_k | A_i = V_{ij})$$
        </div>

        Dabei gilt:

        <ul>
            <li>$K$: Anzahl der Cluster</li>
            <li>$I$: Anzahl der Attribute</li>
            <li>$J(i)$: Anzahl der Attributwerte des $i$-ten Attributs</li>
            <li>$V_{ji}$: $j$-ter möglicher Wert für Attribut $i$</li>
            <li>$P(A_i = V_ij | C_k)$: Predictability</li>
            <li>$P(C_k | A_i = V_{ij}$: Predictiveness</li>
        </ul>

        Anwendung: Interpretation von <abbr title="Elektromyographie">EMGs</abbr>
    </dd>
</dl>



## Prüfungsfragen

<ul>
    <li>Was ist Induktives Lernen?<br/>
        → Eine große Menge an Beispielen wird gegeben. Der Lerner muss selbst
           das Konzept herausfinden.</li>
    <li>Was ist Deduktives Lernen?<br/>
        → Fakten werden gegeben. Der lernende bekommt das allgemeine Konzept
           gesagt und muss nur logische Schlussfolgerungen machen.</li>
    <li>SVMs
    <ul>
        <li>Wie funktioniert SRM bei SVMs?<br/>
            → Dualität zwischen Feature- und Hypothesenraum: Radius der Hyperkugel
               wird minimiert.</li>
        <li>Warum lernen SVMs "korrekt"?<br/>
            → Es gibt ein Theorem (TODO: Welches?) das besagt, dass die VC-Dimension
            eines Klassifiers, welcher Datenpunkte im $n$-Dimensionalen Raum
            innerhalb einer Kugel mit Radius $D$ durch eine Hyperebene mit
            mindestens Abstand $\Delta$ trennen will, durch $(\frac{D}{\Delta})^2$
            beschränkt ist. Die SVM minimiert genau diesen Quotienten, da sie den
            Margin maximiert.

            Alternativ: Erklärung durch Strukturierung des Hypothesenraumes (TODO).</li>
    </ul></li>
    <li>Reinforcement Learning
        <ul>
            <li>Wie lautet die Bellman-Gleichung?<br/>
                → $Q(s, a) = r + \gamma \max_{a'} Q(s', a')$ wobei $\gamma$ ein
                Diskontierungsfaktor ist, $s'$ der Zustand in den man kommt, wenn
                man $a$ ausführt und $r$ der Reward nach ausführen von $a$ in
                $s$ ist.</li>
            <li>Was ist Value Iteration und wie lautet die Formel?<br/>
                → Schätzen der Value-Funktion durch iteratives anwenden von $\hat{V}^*(s_t) \leftarrow r_t + \gamma \hat{V}^*(s_{t+1})$</li>
            <li>Was sind Eligibility Traces im Kontext von Reinforcement Learning?<br/>
                → Siehe <a href="#rl-eligibility-trace">oben</a></li>
            <li>Wie funktioniert Q-Learning?<br/>
                → Siehe <a href="#q-learning">Abschnitt Q-Learning</a></li>
        </ul>
    </li>
    <li>Evolutionäre Algorithmen: Was ist wichtig?
        <ul>
            <li>Population / Individuen: Wie Individuen darstellen<br/>
                → Durch Gene (Attribute), z.B. als Bitstring</li>
            <li>Gegebener Ablauf (Wahl der Eltern, Generierung der Individuen)</li>
            <li>Wie kann man Kombinieren?<br/>
                → vgl. <i>Rekombination</i></li>
            <li>Fitness Function</li>
            <li>Was sind die wichtigsten Elemente von evolutionären Algorithmen?<br/>
                → Mutation, Rekombination, Fittness-Funktion, Selektion</li>
            <li>Was ist Landmarksche / Baldwinsche Evolution?</li>
        </ul>
    </li>
    <li>Wie lautet die Fehlerabschätzung von Vapnik?<br/>
        → Siehe <a href="#fehlerabschaetzung">Abschätzung des realen Fehlers</a> durch den empirischen Fehler
           und die VC-Dimension.</li>
    <li>Was versteht man unter Cascade Correlation?<br/>
        → <a href="https://www.youtube.com/watch?v=1E3XZr-bzZ4">YouTube</a> (4:05 min)</li>
    <li>Welche übwerwachten Lernverfahren gibt es?<br/>
        → Neuronale Netze, SVMs</li>
    <li>Wie funktioniert Inferenz in Markov Logik Netzen?<br/>
        → Siehe <a href="#mln-inference">oben</a></li>
    <li>Wie wird die Verbundwahrscheinlichkeit / Weltwahrscheinlichkeit in Markov Logik Netzen berechnet?<br/>
        → Siehe <a href="#mln-jpd">oben</a></li>
    <li>Was ist Dynamic Decay Adjustment (DDA)?<br/>
        → Siehe <a href="#dda-algorithm">oben</a></li>
    <li>Was ist erklärungsbasierte Generalisierung (EBG)?<br/>
        → Der Agent lernt keine neuen Konzepte, aber er lernt über Verbindungen
           bekannter Konzepte.</li>
    <li>Wie lautet die Formel für Entropie / Information Gain?<br/>
        → $\text{Entropie} = - \sum_{i} p_i \log p_i$ und $KL(P, Q) = \sum_{x \in X} P(x) \cdot \log \frac{P(x)}{Q(x)}$</li>
    <li>Was ist Cobweb?<br/>
        → Siehe <a href="#unsupervised-learning">Unsupervised Learning</a></li>
</ul>


## Material und Links

* [Vorlesungswebsite](http://cg.ivd.kit.edu/lehre/ws2015/cg/index.php)
* [&Uuml;bungswebsite](http://cg.ivd.kit.edu/lehre/ws2015/cg/uebung.php)
* StackExchange
  * [What is the difference between concept learning and classification?](http://datascience.stackexchange.com/q/8642/8820)
   * [What is the difference between a (dynamic) Bayes network and a HMM?](http://datascience.stackexchange.com/q/10000/8820)
* [Zusammenfassung der Vorlesung ML 2](//martin-thoma.com/machine-learning-2-course/)
* Udacity
  * [Knowledge-Based AI: Cognitive Systems](https://www.udacity.com/course/knowledge-based-ai-cognitive-systems--ud409): Unter anderem gibt es eine Lektion zu Explanation-Based Learning (erklärungsbasierte Generalisierung)

## Literatur

* [<a href="#ref-mit97-anchor" name="ref-mit97">Mit97</a>] T. Mitchell.
  Machine Learning. McGraw-Hill, 1997.
* [<a href="#ref-dar09-anchor" name="ref-dar09">Dar09</a>] A. Darwiche.
  Modeling and reasoning with Bayesian networks. Cambridge University Press,
  Cambridge [u.a.], 2009.
* [<a href="#ref-ber95-anchor" name="ref-ber95">Ber95</a>] M.&nbsp;Berthold and
  J.&nbsp;Diamond. Boosting the Performance of RBF Networks with Dynamic Decay
  Adjustment. Advances in Neural Information Processing, 1995. [<a href="http://kops.uni-konstanz.de/handle/123456789/5427">Online</a>]
* [<a href="#ref-pro06-anchor" name="ref-pro06">Pro06</a>] Prokopenko, Mikhail and Gerasimov, Vadim and
  Tanev, Ivan. Evolving Spatiotemporal Coordination in a Modular Robotic
  System. Springer, 2006.


## Übungsbetrieb

Es gibt keine Übungsblätter, keine Übungen, keine Tutorien und keine
Bonuspunkte.


## Vorlesungsempfehlungen

Folgende Vorlesungen sind ähnlich:

* [Analysetechniken großer Datenbestände](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/)
* [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/)
* [Machine Learning 2](https://martin-thoma.com/machine-learning-2-course/)
* [Mustererkennung](https://martin-thoma.com/mustererkennung-klausur/)
* [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)


## Termine und Klausurablauf

**Datum**: Mündliche Prüfung (in Zukunft schriftlich)<br/>
**Ort**: nach Absprache<br/>
**Zeit**: 15&nbsp;min<br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Ergebnisse**: werden ca. 5&nbsp;-&nbsp;10&nbsp;min. nach der mündlichen Prüfung gesagt<br/>
**Erlaubte Hilfsmittel**: keine
