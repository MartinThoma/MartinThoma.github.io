---
layout: post
title: Probabilistische Planung
slug: probabilistische-planung
author: Martin Thoma
date: 2016-05-11 20:00
category: German posts
tags: Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Probabilistische Planung&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://ies.anthropomatik.kit.edu/mitarbeiter.php?person=huber">Herrn Dr.-Ing. Marco Huber</a> im Sommersemester 2015 und 2016 gehört. Der Artikel dient als Prüfungsvorbereitung und ist noch am Entstehen.</div>

In der Vorlesung 'Probabilistische Planung' werden drei Themen besprochen:

* Markov'sche Entscheidungsprobleme (MDPs)
* Planung bei Messunsicherheiten
* Reinforcement Learning (RL)


## Behandelter Stoff

### Übersicht

<table>
<tr>
    <th>Datum</th>
    <th>Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
    <td>26.04.2016</td>
    <td>Grundlagen</td>
    <td>Wahrscheinlichkeitsraum, Grundraum, Ereignis&shy;raum, Resultate,
        Elementar&shy;ereignis, $\sigma$-Algebra, Wahrscheinlichkeits&shy;maß,
        Bedingte Wahrscheinlichkeit, Ziegenproblem, Dichtefunktion</td>
</tr>
<tr>
    <td>28.04.2016</td>
    <td>Grundlagen</td>
    <td>Allais-Paradoxon, TODO</td>
</tr>
<tr>
    <td>06.05.2016</td>
    <td>Grundlagen</td>
    <td>TODO</td>
</tr>
<tr>
    <td>11.05.2016</td>
    <td>MDPs</td>
    <td>Definition eines MDP, Plan vs. Strategie, <abbr title="Dynamische Programmierung">DP</abbr></td>
</tr>
<tr>
    <td>18.05.2016</td>
    <td>MDPs</td>
    <td>Endliche Planungsprobleme, Value- und Policy-Iteration</td>
</tr>
</table>


### Grundlagen

Slides: `ProPlan-1-Anschrieb.pdf`

<dl>
  <dt><dfn>$\sigma$-Algebra</dfn></dt>
  <dd>Sei $S$ eine Menge und $\mathcal{A}$ ein Menge aus Teilmengen von $S$.
      $\mathcal{A}$ heißt eine $\sigma$-Algebra über $S$, genau dann, wenn
      gilt:

      <ul>
          <li>$S \in \mathcal{A}$</li>
          <li>$\forall M \in \mathcal{A} \Rightarrow (S \setminus M) \in \mathcal{A}$</li>
          <li>$M_1, M_2, \dots \in \mathcal{A} \Rightarrow \bigcup_{n \in \mathbb{N}} M_n \in \mathcal{A}$</li>
      </ul>

      </dd>
  <dt><dfn>Wahrscheinlichkeitsmaß</dfn></dt>
  <dd>Eine Funktion $P: A \rightarrow \mathbb{R}$ heißt Wahrscheinlichkeitsmaß,
      wenn die Kolmogorov'schen Axiome gelten:

      <ul>
          <li>$\forall M \in \mathcal{A}: P(M) \geq 0$</li>
          <li>$\forall P(S) = 1$</li>
          <li>$M_1, M_2, \in \mathcal{A} \land M_1 \cap M_2 = \emptyset \Rightarrow P(M_1 \cup M_2) = P(M_1) + P(M_2)$</li>
      </ul>

      </dd>
  <dt><dfn>Normalverteilung</dfn></dt>
  <dd>Die Normalverteilung $\mathcal{N}(\mu, \sigma^2)$ ist eine
      kontinuierliche Verteilung mit der Dichtefunktion

      $$f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{- \frac{(x - \mu)^2}{2\sigma^2}}$$


      </dd>
</dl>


### Markov'sche Entscheidungs&shy;probleme

Slides: `11.05.2016 - TODO`

<dl>
  <dt><dfn id="mdp">Markov'sches Entscheidungsproblem</dfn> (<dfn>Markov Decision Process</dfn>, <dfn>MDP</dfn>)</dt>
  <dd>Ein MDP wird durch 8&nbsp;Eigenschaften gekennzeichnet:

      <ol>
          <li>Zustandsraum $X \subseteq \mathbb{R}^n$ mit Zuständen
              $x \in \mathcal{X}$.</li>
          <li>Diskrete Zeitschritte $k=0, 1, \dots, N$ mit Endzeitpunkt
              $N$. Dabei ist der 0-te Schritt gegeben.</li>
          <li>Initialzustand $x_o \in \mathcal{X}$ des Agenten zum Zeitpunkt $k=0$.</li>
          <li>Nichtleere Aktionsmenge $A_k(x_0) \subseteq A$ mit Aktion $a_k$.
              Häufig $A_k(x_k)=A$ für alle $k=0, \dots, N$ (Zeit- und Zustandsinvarianz)</li>
          <li>Übergangswahrscheinlichkeit $x_{k+1} \leadsto P_x(\cdot | x_k, a_k)$.<br/>
              Markov-Annahme: $P_x(\cdot | x_k, a_k) = P(\cdot | x_{0:k}, a_{0:k})$,
              wobei die Notation $x_{0:k} = x_0, x_1, \dots, x_k$ bedeutet.
              Das heißt, der Folgezustand ist nur vom Zustand $x_k$ und
              der gewählten Aktion $a_k$ abhängig.<br/>
              Im Fall diskreter Zustände ist die
              Übergangs&shy;wahrscheinlichkeit eine bedingte Zähldichte:
              $$f(x_{k+1} | x_k, a_k) = P_x(x=x_{k+1} | x_k, a_k)$$<br/>
              Bei kontinuierlichen Zuständen eine bedingte Wahrscheinlichkeits&shy;dichte:
              $$f(x_{k+1} | x_k, a_k) = \frac{\partial F(x | x_k, a_k)}{\partial x} |_{x=x_{k+1}}$$</li>
          <li>Additive Kostenfunktion
              $$g_N (x_N) + L_{k=0}^{N-1} g_k(x_k, a_k)$$
              wobei $g_N$ die terminalen Kosten und $g_k$ Schrittkosten genannt
              werden.</li>
          <li>Der Zustand ist für jedes $k$ <strong>direkt beobachtbar</strong>.

              <ul>
                  <li><strong>Vor</strong> Anwendung bzw Auswahl einer Aktion
                      $a_k$ zum Zeitpunkt $k$
                      $$x_{k+1} \sim P_x(\cdot | x_k, a_k)$$
                      wobei $x_k, a_k$ exakt bekannt sind.</li>
                  <li><strong>Nach</strong> Anwendung der Aktion $a_k$ zum
                      Zeitpunkt $k+1$ ist $x_{k+1}$ exakt bekannt.</li>
              </ul>
          </li>
          <li><strong>Ziel</strong>: Minimierung der erwarteten Kosten
              $$J_{\pi_{0:N-1}}(x_0) := \mathbb{E}(g_N(x_k) + \sum_{k=0}^{N-1} g_k (x_k, \pi_k(x_k))$$
              bzgl. einer Strategie $\pi_{0:N-1} = (\pi_0, \pi_1, \dots, \pi_{N-1})$
              mit Funktionen $\pi_k(x_k) = a_k \in A_k(x_k)$.</li>
      </ol>
  </dd>
  <dt><dfn>Strategie</dfn></dt>
  <dd>Eine Strategie ist ein Plan mit Zustandsrückführung</dd>
  <dt><dfn id="nutzenfunktion">Nutzenfunktion</dfn></dt>
  <dd>TODO</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Bellman_equation"><dfn id="bellman-equation">Bellman-Gleichungen</dfn></a></dt>
  <dd>TODO</dd>
  <dt><dfn id="q-function">Q-Funktion</dfn></dt>
  <dd>TODO</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Dynamische_Programmierung"><dfn id="dynamic-programming">Dynamische Programmierung</dfn></a></dt>
  <dd>TODO

      Laufzeitkomplexität $\mathcal{O}(N |\mathcal{X}|^2 |A|)$

  </dd>
</dl>

18.05.2016

<dl>
    <dt><dfn>Endliche Planungsproblem</dfn></dt>
    <dd>Hat man einen endlichen Zustandsraum $\mathcal{X} = \{1, 2, \dots, n_x\} \subsetneq \mathbb{N}$ und eine endliche Aktionsmenge $A = \{1, 2, \dots, n_a\} \subsetneq \mathbb{N}$,
        in einem Planungsproblem, so spricht man von einem endlichen
        Planungsproblem.</dd>
    <dt><dfn>Markov-Kette</dfn></dt>
    <dd>Übergangswahrscheinlichkeiten in einem endlichen Planungsproblem
        sind gegeben.

        Die naive Lösung mit Brute-Force ist in $\mathcal{O}(|A|^{N \cdot |X|})$.

    </dd>
    <dt><dfn>Planungsprobleme nach Horizont</dfn></dt>
    <dd>

        <ul>
            <li>$N=1$: Gierige Planung, ein einschrittiges Planungsproblem.
                       Hat geringe Komplexität, aber zukünftige Effekte werden
                       nicht berücksichtig. Bei submodularen Kostenfunktionen
                       kann man die Kosten, die durch die gierige Planung
                       entstehen, abschätzen.</li>
            <li>$N<\infty$: Wurde bisher betrachtet und betrifft die meisten
                       Planungsprobleme. Nachteil ist, dass die Strategie $\pi_k$
                       zeitinvariant ist.</li>
            <li>$N = \infty$: Bei Planungsproblemen mit sehr langem Horizont,
                       wenn ein Ende nicht abzulesen ist. Beispiele sind die
                       kürzeste-Wege-Suche sowie bei Reinforcement Learning.
                       Probleme sind unendliche Kosten und die Zeitabhängigkeit
                       der Schrittkosten und Übergangswahrscheinlichkeiten.</li>
        </ul>

    </dd>
    <dt><dfn>Diskontiertes Planungsproblem</dfn></dt>
    <dd>

        <ol>
            <li>Übergangswahrscheinlichkeiten und Schrittkosten sind
                Zeitinvariant, dh. $f_{ij}^k(a) = f_{ij}(a)$ und
                $g_k(i,a) = g(i, a) \forall k$.</li>
            <li>Es gilt die optimale Wertefunktion $J^*$ zu finden, welche
                durch
                $$J^*(x_0) = \min_{\pi_0, \pi_1, \dots} (J_{\pi_0}(x_0))$$

                definiert ist. Diese minimiert die erwarteten <i>diskontierten
                Kosten</i>

                $$J_{\pi_0} (x_0) = \lim_{N \rightarrow \infty} \mathbb{E}(\alpha^N g(x_N)+ \sum_{k=0}^{N-1} \alpha^k \cdot g(x_k, \pi_k(x_k)))$$

                Dabei heißt $\alpha \in (0, 1)$ ein <i>Diskontierungsfaktor</i>.
                Er verhindert, dass die Kosten unendlich werden.
            </li>
        </ol>

        Dies kann man mit DP lösen, indem man eine Vorwärtsrekursion macht:

        $$
        \begin{align}
        J_k(1) &= \min_{a \in A(i)}(g(i, a) + \alpha \sum_{j=1}^{n_x} f_{ij}(a) \cdot J_{k-1}(j))\\
        J_0(i) &= g(i)
        \end{align}
        $$

        Das ist möglich, da das Problem zeitinvariant ist. Dies kann man durch
        Indexverschiebung zeigen.
    </dd>
    <dt><dfn>Bellman-Operator</dfn></dt>
    <dd>$$(T J) (i) = \min_{a \in A(i)} (g(i,a) + \alpha \cdot \sum_j f_{ij}(a) \cdot J(j))$$

        $$T^k J = \begin{cases}(T(T^{k-1} J)) &\text{if } k \geq 1\\
                               J              &\text{otherwise}
                  \end{cases}$$

        Es gilt: $$J^* = \lim_{N \rightarrow \infty} T^N J \text{ für beliebiges } J$$
    </dd>
    <dt><dfn>Strategiebewertung</dfn></dt>
    <dd>$$(T_\pi J)(i) = g(i, \pi(i)) + \alpha \cdot \sum_j f_{ij} (\pi(i)) \cdot J(j)$$

        Für eine optimale Strategie $\pi^*$ gilt:

        $$(T J)(i) = (T_{\pi^*} J)(i)$$
    </dd>
    <dt><dfn>Wertevektor</dfn></dt>
    <dd>$$J = (J(1), \dots, J(nx))^T$$</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Kontraktion_(Mathematik)"><dfn>Kontraktion</dfn></a></dt>
    <dd>Eine Funktion $f: M \rightarrow M$ in einem metrischen Raum $(M, d)$
        heißt Kontraktion genau dann, wenn
        $$\exists \lambda \in [0, 1) \forall x, y \in M: d(f(x), f(y)) \leq \lambda d(x, y)$$
        gilt.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Fixpunktsatz_von_Banach"><dfn>Banach'scher Fixpunktsatz</dfn></a></dt>
    <dd>

        Sei $(M, d)$ ein vollständig metrischer Raum und $f$ eine Kontraktion,
        welche Lipschitz-Stetig ist mit Konstante $0 \leq \lambda < 1$.
        Dann gilt:

        <ul>
            <li>Es gibt genau einen Fixpunkt $\xi \in M$ mit $f(\xi) = \xi$.</li>
            <li>TODO (Abschätzung)</li>
        </ul>

    </dd>
    <dt><dfn>T-Kontraktion</dfn></dt>
    <dd>Für beliebige Wertevektoren $J, J'$, eine beliebige Strategie $\pi$
        und für alle $k=0,1, \dots$ gilt:

        $$d(T^k J, T^k J') = \leq \alpha^k \cdot d(J, J')$$
        $$d(T^k_\pi J, T_T^k J') \leq \alpha^k \cdot d (TODO)$$
    </dd>
    <dt><dfn id="value-iteration">Werteiteration</dfn> (<dfn>Value Iteration</dfn>)</dt>
    <dd>$$J^* = \lim_{N \rightarrow \infty} T^N J$$
        wobei $J^*$ die optimalen Kosten, $T$ der Bellman-Operator und $N$
        der Planungshorizont ist.

        TODO: Pseudocode

        </dd>
    <dt><dfn>Satz von der Sationären Strategie</dfn></dt>
    <dd>

        <ol>
            <li>Für jede stationäre Strategie $\pi = \pi_{0:N-1}$ erfüllt der
                dazugehörige Wertevektor $J_\pi$ die Fixpunktgleichung
                $J_\pi = T_\pi J_\pi$.
                Dabei ist $J_\pi$ der eindeutige Fixpunkt.</li>
            <li>Eine sationäre Strategie $\pi^*$ ist genau dann optimal, wenn
                $\pi^*$

                $$T J^* = T_{\pi^*} J^*$$

                erfüllt. (Also: Die optimale Strategie ist eine stationäre Strategie)</li>
        </ol>

        Der Beweis für (1) folgt aus dem Banach'schen Fixpunktsatz.
    </dd>
    <dt><dfn id="policy-iteration">Strategieiteration</dfn></dt>
    <dd>Man kann beobachten, dass bei der Werteiteration die Stategie schneller
        konvergiert als der Wertevektor. Außerdem ist die Anzahl der
        Strategien endlich, aber es gibt unendlich viele Wertevektoren.<br/>
        <br/>
        (TODO: Pseudocode)
        <br/>
        Die folgenden beiden Schritte werden alternierend ausgeführt:

        <ol>
            <li>Strategieauswertung</li>
            <li>Strategieverbesserung</li>
        </ol>

        Vergleich zwischen Werte- und Strategieiteration:

        <ul>
            <li>Strategieiteration konvergiert in weniger Schritten</li>
            <li>Jeder Schritt der Strategieiteration ist teurer als in der
                Werteoperation, da die Strategieauswertung die Lösung eines
                LGS ist (in $\mathcal{O}(n_x^3)$). Außerdem ist
                die Strategieiteration nie für $\alpha=1$ lösbar (kann auch
                sonst passieren).</li>
        </ul>
    </dd>
</dl>

### POMDPs

<dl>
    <dt><a href="https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process"><dfn id="pomdp">Partially observable Markov decision process</dfn></a> (POMDP)</dt>
    <dd>TODO</dd>
</dl>


### Reinforcement Learning

<dl>
    <dt><dfn id="rl">Reinforcement Learning</dfn></dt>
    <dd>TODO</dd>
</dl>


## Prüfungsfragen

* Welche 3 Themengebiete wurden in der Vorlesung behandelt und was sind die
  Unterschiede?<br/>
  → <a href="#mdp">MDP</a>, <a href="#pomdp">POMDP</a>, <a href="#rl">RL</a> (TODO: Agent-Umfeld-Diagram)
* Wie ist eine Nutzenfunktion definiert?<br/>
  → TODO
* Wie löst man Optimierungsprobleme ohne Nebenbedingungen?<br/>
  → TODO
* Beweisen Sie, dass der Gradient senkrecht auf die Höhenlinien steht.<br/>
  → TODO
* Wie löst man Optimierungsprobleme mit Nebenbedingungen?<br/>
  → Lagrange (TODO)
* Wann ist es leichter / schwerer das Optimierungsproblem zu lösen?<br/>
  → TODO
* Welche numerischen Methoden zur Optimierung kennen sie?<br/>
  → TODO

### MDP

* Wie lautet die Definition eines MDP?<br/>
  → Siehe <a href="#mdp">oben</a>.
* Was versteht man unter dynamischer Programmierenung?<br/>
  → Siehe <a href="#dynamic-programming">oben</a>.
* Wie lauten die Bellman-Gleichungen?<br/>
  → Siehe <a href="#bellman-equation">oben</a>.
* Was ist an den Bellman-Gleichungen problematisch?<br/>
  → TODO

### POMDP

* Wie lautet die Definition eines POMDP?<br/>
  → TODO
* Wie lautet die Kostenfunktion eines POMDP?<br/>
  → TODO
* Was ist PWLC?<br/>
  → TODO


### RL

* Welche Arten von RL gibt es?<br/>
  → TODO


## Material und Links

* [Vorlesungswebsite](http://ies.anthropomatik.kit.edu/lehre_proplan.php)


## Vorlesungsempfehlungen

Folgende Vorlesungen sind ähnlich:

* [Analysetechniken großer Datenbestände](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/)
* [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/)
* [Machine Learning 2](https://martin-thoma.com/machine-learning-2-course/)
* [Mustererkennung](https://martin-thoma.com/mustererkennung-klausur/)
* [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)
* Lokalisierung Mobiler Agenten
* [Probabilistische Planung](https://martin-thoma.com/probabilistische-planung/)


## Termine und Klausurablauf

Die Veranstaltung wird mündlich geprüft.
