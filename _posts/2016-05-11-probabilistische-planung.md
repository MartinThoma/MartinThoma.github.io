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
    <td>Allais-Paradoxon, Nutzentheorie, Präferenzrelation, Nutzenfunktion</td>
</tr>
<tr>
    <td>06.05.2016</td>
    <td>Grundlagen</td>
    <td>Einführung in die Optimierungstheorie: Notwendige und Hinreichende
        Bedingungen, Konvexe Optimierung, Numerische Methoden</td>
</tr>
<tr>
    <td>11.05.2016</td>
    <td>MDPs</td>
    <td>Definition eines MDP, Plan vs. Strategie, <abbr title="Dynamische Programmierung">DP</abbr></td>
</tr>
<tr>
    <td id="2016-05-18">18.05.2016</td>
    <td>MDPs</td>
    <td>Endliche Planungsprobleme, Value- und Policy-Iteration</td>
</tr>
<tr>
    <td id="2016-05-25">25.05.2016</td>
    <td>MDPs</td>
    <td>Kürzeste-Wege Suche (Tiefensuche, Breitensuche, Dijkstra, A*, Branch &amp; Bound; Label-Korrektur-Algorithmus); Trellis-Diagramm; Differentialantrieb; Pontryagin's Minimumprinzip</td>
</tr>
<tr>
    <td id="2016-06-01">01.06.2016</td>
    <td>MDPs</td>
    <td>Pontryagin's Minimumprinzip, Hamilton-Funktion; LQR; Sicherheitsäquivalenz</td>
</tr>
<tr>
    <td id="2016-06-08">08.06.2016</td>
    <td>POMDPs</td>
    <td>Motivation und Definition von POMDP; Hinreichende Statistik; Bayes-Schätzer</td>
</tr>
<tr>
    <td id="2016-06-15">15.06.2016</td>
    <td>POMDPs</td>
    <td>Lineare Planungsprobleme (Kalman-Filter); Sperationsproblem</td>
</tr>
<tr>
    <td id="2016-06-22">22.06.2016</td>
    <td>POMDPs</td>
    <td>Endliche Planungsprobleme (Optimale Strategie); <a href="#ol-planung">OL</a>, <a href="#olf-planung">OLF</a>, Modellprädiktive Planung</td>
</tr>
<tr>
    <td id="2016-06-29">29.06.2016</td>
    <td>POMDPs</td>
    <td>Parametrische / Nichtparametrische approximative Planung (Sicherheitsäquivalenz bei deterministischen Problemen); Funktionsapproximatoren für Wertefunktion / Strategie; Sensoreinsatzplanung</td>
</tr>
<tr>
    <td id="2016-07-06">06.07.2016</td>
    <td>POMDPs, <abbr title="Reinforcement Learning">RL</abbr></td>
    <td>POMDPs: Sensoreinsatzplanung; Kovarianz- vs TODO-Kostenfunktionen</td>
</tr>
<tr>
    <td id="2016-07-13">13.07.2016</td>
    <td><abbr title="Reinforcement Learning">RL</abbr></td>
    <td>Monte Carlo Verfahren (Strategiebewerbtung); Temporal Difference</td>
</tr>
</table>

Folien:

* 25.05.2016: Folie 4 - Die Knoten sind Zustände und die Kanten sind Aktionen
* $g_{ij}^k = \infty$: Kein Übergang von $i$ nach $j$ in Schritt $k$.

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
          <li>$M_1, M_2 \in \mathcal{A} \land M_1 \cap M_2 = \emptyset \Rightarrow P(M_1 \cup M_2) = P(M_1) + P(M_2)$</li>
      </ul>

      </dd>
  <dt><dfn>Normalverteilung</dfn></dt>
  <dd>Die Normalverteilung $\mathcal{N}(\mu, \sigma^2)$ ist eine
      kontinuierliche Verteilung mit der Dichtefunktion

      $$f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{- \frac{(x - \mu)^2}{2\sigma^2}}$$


      </dd>
</dl>


### Markov'sche Entscheidungs&shy;probleme

Slides: `11.05.2016`

<dl>
  <dt><dfn id="mdp">Markov'sches Entscheidungsproblem</dfn> (<dfn>Markov Decision Process</dfn>, <dfn>MDP</dfn>)</dt>
  <dd>Ein MDP wird durch 8&nbsp;Eigenschaften gekennzeichnet:

      <ol>
          <li>Zustandsraum $X \subseteq \mathbb{R}^n$ mit Zuständen
              $x \in \mathcal{X}$.</li>
          <li>Diskrete Zeitschritte $k=0, 1, \dots, N$ mit Endzeitpunkt
              $N$. Dabei ist der 0-te Schritt gegeben.</li>
          <li>Initialzustand $x_o \in \mathcal{X}$ des Agenten zum Zeitpunkt $k=0$.</li>
          <li>Nichtleere Aktionsmenge $A_k(x_k) \subseteq A$ mit Aktion $a_k$.
              Häufig $A_k(x_k)=A$ für alle $k=0, \dots, N$ (Zeit- und Zustandsinvarianz)</li>
          <li>Übergangswahrscheinlichkeit $x_{k+1} \sim P_x(\cdot | x_k, a_k)$.<br/>
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
              $$g_N (x_N) + \sum_{k=0}^{N-1} g_k(x_k, a_k)$$
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
              $$J_{\pi_{0:N-1}}(x_0) := \mathbb{E} \left (g_N(x_k) + \sum_{k=0}^{N-1} g_k (x_k, \pi_k(x_k)) \right )$$
              bzgl. einer Strategie $\pi_{0:N-1} = (\pi_0, \pi_1, \dots, \pi_{N-1})$
              mit Funktionen $\pi_k(x_k) = a_k \in A_k(x_k)$.</li>
      </ol>
  </dd>
  <dt><dfn id="policy">Strategie</dfn> (<dfn>policy</dfn>)</dt>
  <dd>Eine Strategie ist ein Plan mit Zustandsrückführung.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Pr%C3%A4ferenzrelation"><dfn>Präferenzrelation</dfn></a></dt>
  <dd>Sei $\mathcal{X}$ eine Zustandsmenge und $\geq \subseteq \mathcal{X} \times \mathcal{X}$
      eine binäre Relation auf $\mathcal{X}$. $\geq$ heißt (schwache)
      Präferenzrelation, wenn gilt:
      <ul>
          <li>$\geq$ ist vollständig: $\forall x, y \in \mathcal{X}: x \geq y \lor y \geq x$</li>
          <li>$\geq$ ist transitiv: $\forall x, y, z \in \mathcal{X}: x \geq y \land y \geq z \Rightarrow x \leq z$</li>
      </ul></dd>
  <dt><a href="https://de.wikipedia.org/wiki/Nutzenfunktion"><dfn id="nutzenfunktion">Nutzenfunktion</dfn></a></dt>
  <dd>Sei $\mathcal{X}$ eine Zustandsmenge und $u: \mathcal{X} \rightarrow \mathbb{R}$
      eine Funktion. Sei außerdem $\geq$ eine Präferenzrelation. $u$ heißt
      eine Nutzenfunktion welche $\geq$ abbildet, wenn gilt:
      $$\forall x, y \in \mathcal{X}: x \geq y \Leftrightarrow u(x) \geq u(y)$$</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem#The_axioms"><dfn>Von-Neumann-Morgenstern Axiome</dfn></a></dt>
  <dd>Sei $\mathcal{X}$ eine Zustandsmenge und $\mathcal{P}$ die Menge aller
      Verteilungen $P: \mathcal{X} \rightarrow [0, 1]$.

        <ol>
            <li id="VNM-1">$\geq$ ist eine Präferenzrelation</li>
            <li id="VNM-2">Unabhängigkeitsaxiom: Gilt für $P, Q \in \mathcal{P}$ die
                Beziehung $P \geq Q$, dann gilt auch:
                $$\alpha \cdot P + (1 - \alpha) R \geq \alpha Q + (1 - \alpha) R$$
                für beliebiges $R \in \mathcal{P}$ und beliebiges $\alpha \in [0, 1]$.
                <br/>
                <u>Salopp:</u> Störungen $R$ beeinflussen die Präferenz von $P$
                und $Q$ nicht.
                </li>
            <li id="VNM-3">Stetigkeitsaxiom: Für beliebige
                           $P, Q, R \in \mathcal{P}$ mit
                           $P > Q > R$ gibt es $\alpha, \beta \in (0, 1)$
                           derart, dass
                           $$\alpha \cdot P + (1 - \alpha) \cdot R > Q > \beta \cdot P + (1-\beta)R$$
                           gilt.<br/>
                           <u>Salopp:</u> Präferenzrelationen sind nicht
                           anfällig gegenüber kleinen Änderungen.</li>
        </ol>

  </dd>
  <dt><dfn>Optimierungsproblem</dfn></dt>
  <dd>Ein allgemeines optimierungsproblem besteht aus einer Optimierungsvariable
      $x \in \mathbb{R}^n$, für welche ein "bester" Parameter gewählt werden
      soll. Dafür gibt es eine Bewertungsfunktion $f$ (Zielfunktion):

        $$
        \begin{align}
        &\underset{x}{\operatorname{minimize}}& & f(x) \\
        &\operatorname{subject\;to}
        & &g_i(x) \leq 0, \quad i = 1,\dots,m \\
        &&&h_i(x) = 0, \quad i = 1, \dots,p
        \end{align}
        $$

        Siehe auch: <a href="../optimization-basics">Optimization Basics</a>

      </dd>
  <dt><dfn>Notwendige Bedingung für optimale Lösung</dfn></dt>
  <dd>$\nabla f(x) \overset{!}{=} 0$</dd>
  <dt><dfn>Konvexe Optimierungsprobleme</dfn></dt>
  <dd>Ein Optimierungsproblem mit konvexer Zielfunktion $f$ hat folgende
      besonderen Eigenschaften

      <ul>
          <li>Jedes lokale Optimum ist ein globales Optimum</li>
          <li>Ein strikt konvexes Optimierungsproblem hat ein eindeutiges
              Optimum.</li>
          <li>Die notwendige Bedingung ist auch hinreichend:

              <ul>
                  <li>Ohne Nebenbedingungen: $\nabla f(x) \overset{!}{=} 0$</li>
                  <li>Mit Nebenbedingungen: $(\nabla f(x^*))^T \cdot (x - x^*) \geq 0 \quad \forall x \in \mathcal{F}$, wobei $\mathcal{F}$ eine konvexe Menge ist.</li>
              </ul>
          </li>
      </ul>

  </dd>
  <dt><a href="https://en.wikipedia.org/wiki/Bellman_equation"><dfn id="bellman-equation">Bellman-Gleichungen</dfn></a></dt>
  <dd>Eine Bellman-Gleichung stellt die Lösung eines Problems rekursiv dar.
      Sie zeigt, dass und wie man die Lösung eines komplexen Problems aus
      Lösungen von Teilproblemen aufbauen kann.<br/>
      Die Belmann-Gleichungen lauten:
      $$
      \begin{align}
J_N(x_n) &= g_N(x_N)\\
J_k(x_k) &= \min_{\mathclap{a_k \in A_k(x_k)}} \left (g_k(x_k, a_k) + \mathbb{E}(J_{k+1}(x_{k+1})| x_k, a_k) \right )
\end{align}
      $$
      <br/>
      Probleme, für die man eine Bellman-Gleichung aufstellen kann haben
      <b>optimale Substruktur</b>.
      <br/>
      Example with the value function:
      $$V(s) = \max_{a} (R(s, a) + \gamma \sum_{s'} T(s, a, s') V(s'))$$
      where $V(s)$ is the value of the state $s$, $R(s,a)$ is the reward
      you get when you apply action $a$ in state $s$, $\gamma \in [0, 1]$ is
      the discount factor, $T(s, a, s') \in [0, 1]$ is the transormation matrix
      which gives you the probability that you will end up in state $s'$ when
      you apply action $a$ in state $s$.</dd>
  <dt><dfn id="differentiation-rules">Differentiation Rules</dfn></dt>
  <dd>

      $$
      \begin{align}
          \frac{\partial x^T a}{\partial x} &= \frac{\partial a^T x}{\partial x} = a\\
          \frac{\partial x^T A}{\partial x} &= \frac{\partial A x}{\partial x} = A \qquad A \in \mathbb{R}^{n \times n}\\
          \frac{\partial x^T A x}{\partial x} &= 2 A x \qquad A \in \mathbb{R}^{n \times n}
      \end{align}
      $$

  </dd>
  <dt><dfn id="q-function">Q-Funktion</dfn></dt>
  <dd>Siehe <a href="../machine-learning-1-course/#q-function">ML 1</a>.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Dynamische_Programmierung"><dfn id="dynamic-programming">Dynamische Programmierung</dfn></a></dt>
  <dd>Dynamische Programmierung ist eine Methode zum Lösen von
      Optimierungsproblemen. Dabei wird die Tatsache genutzt, dass für jeden
      initialen Zustand $x_0 \in \mathcal{X}$ die optimalen Kosten $J^*(x_0)$
      in
      $$J^*(x_0) = \min_{\pi_{0:N-1}} J_{\pi_{0:N-1}} (x_0)$$
      gleich dem Wert $J_0(x_0)$, welcher sich aus dem letzten Schritt der
      Rekursion
      $$
      \begin{align}
          J_N(x_N) &= g_N (x_N)\\
          J_k(x_k) &= \min_{a_k \in A_k(x_k)} \{g_k (x_k, a_k) + \mathbb{E}(J_{k+1} (x_{k+1})|x_k, a_k)\}
          \text{ für } k = 0, \dots, N-1
      \end{align}
      $$
      ergibt.<br/>
      <br/>
      Laufzeitkomplexität: $\mathcal{O}(N |\mathcal{X}|^2 |A|)$

  </dd>
</dl>

18.05.2016

<dl>
    <dt><dfn>Endliche Planungsprobleme</dfn></dt>
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
            <li>A-priori-Abschätzung: $d(x_n,\xi)\le\frac{\lambda^n}{1-\lambda}d(x_0,x_1)$</li>
            <li>A-posteriori-Abschätzung: $d(x_n,\xi)\le\frac{\lambda}{1-\lambda}d(x_{n-1},x_n)$</li>
        </ul>

    </dd>
    <dt><dfn>T-Kontraktion</dfn></dt>
    <dd>Für beliebige Wertevektoren $J, J'$, eine beliebige Strategie $\pi$
        und für alle $k=0,1, \dots$ gilt:

        $$d(T^k J, T^k J') = \leq \alpha^k \cdot d(J, J')$$
        $$d(T^k_\pi J, T_T^k J') \leq \alpha^k \cdot d (TODO)$$
    </dd>
    <dt><dfn>Werte-Iteration</dfn> (<dfn id="value-iteration">Value iteration</dfn>)</dt>
    <dd>$$J^* = \lim_{N \rightarrow \infty} T^N J$$
        wobei $J^*$ die optimalen Kosten, $T$ der Bellman-Operator und $N$
        der Planungshorizont ist. $g$ ist die Schrittkostenfunktion.<br/>

        TODO: What is $\alpha$? What is $f_{xj}(a)$?<br/>

        <img src="../images/2016/07/Value-Iteration.png"
             alt="Value iteration algorithm"
             width="512px" />

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
    <dt><dfn>Strategie-Iteration</dfn> (<dfn id="policy-iteration">Policy iteration</dfn>)</dt>
    <dd>Man kann beobachten, dass bei der Werte-Iteration die Stategie schneller
        konvergiert als der Wertevektor. Außerdem ist die Anzahl der
        Strategien endlich, aber es gibt unendlich viele Wertevektoren.<br/>
        <br/>
        TODO: What is $\alpha$? What is $f_{xj}(a)$?<br/>

        <img src="../images/2016/07/Value-Iteration.png"
             alt="Value iteration algorithm"
             width="512px" />
        <br/>
        Die folgenden beiden Schritte werden alternierend ausgeführt:

        <ol>
            <li>Strategieauswertung:
                $$V^\pi(s) \gets R(s, \pi(s)) + \gamma \sum_{s'} T(s, \pi(s), s') V^\pi(s')$$
            </li>
            <li>Strategieverbesserung:
                $$\pi'(s) \gets \text{arg max}_a (R(s, a) + \gamma \sum_{s'} T(s, a, s') V^\pi(s'))$$
            </li>
        </ol>

        Siehe <a href="https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume4/kaelbling96a-html/node20.html">CMU</a>
    </dd>
    <dt><dfn>Value iteration vs Policy iteration</dfn></dt>
    <dd>
        <ul>
            <li>Strategieiteration konvergiert in weniger Schritten</li>
            <li>Jeder Schritt der Strategieiteration ist teurer als in der
                Werteoperation, da die Strategieauswertung die Lösung eines
                LGS ist (in $\mathcal{O}(n_x^3)$). Außerdem ist
                die Strategieiteration nie für $\alpha=1$ lösbar (kann auch
                sonst passieren).</li>
        </ul>
    </dd>
    <dt><dfn>Label-Korrektur-Algorithmus</dfn></dt>
    <dd>Der Label-Korrektur-Algorithmus ist ein Meta-Algorithmus zur
        kürzeste-Wege-Suche dient. Spezialfälle von diesem sind die
        Tiefen- und Breitensuche, der <a href="https://de.wikipedia.org/wiki/Dijkstra-Algorithmus">Dijkstra-Algorithmus</a>, der <a href="https://de.wikipedia.org/wiki/A*-Algorithmus">A*-Algorithmus</a> sowie
        Branch &amp; Bound.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Trellis-Code"><dfn id="trellis">Trellis-Diagramm</dfn></a></dt>
    <dd>Eine Diagramm welches anzeigt welche Zustände über die Zeit
        gewählt werden.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Pontryagin%27s_maximum_principle"><dfn id="pontryagins-minimum-principle">Pontryagin's Minimum-Prinzip</dfn></a></dt>
    <dd>Das Pontryagin'sche Minimum-Prinzip könnte als die russische
        Variante der Bellman-Gleichungen für deterministische MDPs bezeichnet
        werden.<br/>

        TODO</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Hamilton-Funktion_(Kontrolltheorie)"><dfn>Hamilton-Funktion</dfn></a></dt>
    <dd>Die Hamilton-Funktion der Kontrolltheorie stellt eine notwendige
        Bedingung für die optimale Lösung eines Steuerungsproblems ist. Damit
        eine Lösung eines Steuerungsprobelms optimal ist, muss die Lösung
        die Hamilton-Funktion minimieren.<br/>
        <br/>
        Die Steuerung $u(t)$ soll so gewählt werden, dass
        $$J(u)=\Psi(x(T))+\int^T_0 L(x,u,t) \mathrm{d}t$$
        minimiert wird. Dabei ist $x(t)$ der Systemzustand mit
        $$\dot{x}=f(x,u,t) \qquad x(0)=x_0 \quad t \in [0,T]$$
        In diesem Fall ist die Hamilton-Funktion
        $$H(x,\lambda,u,t)=\lambda^T(t)f(x,u,t)+L(x,u,t),$$
        wobei $\lambda(t)$ Lagrange-Multiplikatoren sind.</dd>
    <dt><dfn>Lineares Zustandsmodell</dfn></dt>
    <dd>$$x_{k+1} = A_k + x_k + B_k \cdot a_k + r_k^{(s)}$$</dd>
    <dt><a href="https://de.wikipedia.org/wiki/LQ-Regler"><dfn id="linear-quadratic-regulator">Linearer Quadratischer Regulator</dfn></a> (<dfn id="lqr">LQR</dfn>)</dt>
    <dd>Der LQR ist ein Regler (Regulator) für einen lineareren Zustandsraum
        mit quadratischer Kostenfunktion. Ein Regel will typischerweise den
        Zustand $x = \vec{0}$ erreichen, wohingegen ein Tracker den aktuellen
        Zustand bestmöglich schätzen will.

        TODO</dd>
    <dt><dfn>Sicherheitsäquivalenz</dfn> (<a href="https://en.wikipedia.org/wiki/Stochastic_control#Certainty_equivalence"><dfn id="certainty-equivalence">Certainty Equivalence</dfn></a>)</dt>
    <dd>Verstärkungsmatrix $l_k$ und somit die Strategie $\pi_k^*$
        sind unabhängig vom Rauschen $r_k^{(s)}$.<br/>
        <br/>
        Die selbe optimale Strategie ergibt sich bei Betrachtung des
        korrespondierendne deterministischen Zustandsraummodel

        $$x_{k+1} = A_k x_k + B_k a_k$$

        welchem das Rauschen $r_k^{(s)}$ durch dessen Erwartungswert $E(r_k^{(s)}) = 0$
        ersetzt ist.<br/>

        $\Rightarrow$ Deterministisches Problem

        TODO</dd>
</dl>


### POMDPs

<dl>
    <dt><a href="https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process"><dfn id="pomdp">Partially observable Markov decision process</dfn></a> (POMDP)</dt>
    <dd>Die Messungen sind unsicherheitsbehaftet.

        Das Planungsproblem ist wie folgt definiert:

        <ul>
            <li>Zustand: Der Agent erhält nur noch Beobachtungen / Messungen
                des Zustands. Probleme dabei sind:
                <ul>
                    <li>Rauschen von Sensoren</li>
                    <li>Indirekt: Position ist interessant, aber man kann
                        z.B. mit GPS nur die Laufzeiten ermitteln.</li>
                    <li>Niederdimensional: Messgröße ist niedrigdimensonaler
                        als die interessierte Größe. Erst durch mehrere
                        Messungen gelangt man an die interessante Größe.</li>
                </ul></li>
        </ul>

        Ein POMDP ist ein MDP mit folgenden Unterschieden:

        <ul>
            <li>Initialzustand $x_0$ ist Zufallsvariable mit Verteilung $P(x_0)$.</li>
            <li>Beobachtungen / Messungen $z_k \in Z$ gemäß der bedingten
                Verteilung
                $$z_k \sim P(\cdot | x_k, a_{k-1})$$
                (Beobachtungswahrscheinlichkeit)<br/>

                <ul>
                    <li>Diskrete Beobachtungen $\rightarrow$ bedingte Zähldichte
                $$f(z_k | x_k a_{k-1}) = P(z=z_k | x_k, a_{k-1})$$</li>
                    <li>Kontinuierliche Beobachtungen $\rightarrow$ bedingte Wahrscheinlichkeitsdichte
                    $$f(z_k | x_k, a_{k-1}) = \frac{\partial f(z | x_k, a_{k-1})}{\partial z} |_{z=z_k}$$</li>
                </ul>

                </li>
            <li id="pomdp-cost-function">Minimierung der erwarteten Kosten

                $$J_{\pi_{0:N-1}}(\square) = E(g_N (x_n) + \sum_{k=0}^{N-1} g_n(x_k, \pi_k(\square)))$$</li>
        </ul>

        Reformulierung als MDP:

        <ul>
            <li>Problem: keine vollständige Information über den Zustand $x_k$,
                aber Zugriff auf Beobachtungen</li>
            <li>Idee: Definieren eines neuen Zustands (Informationsvektor $\mathcal I$,
                engl. Information state), welcher

                <ul>
                    <li>direkt zugänglich ist,</li>
                    <li>alle verfügbaren Informationen über $x_k$ zum Zeitpunkt
                        $k$ enthält</li>
                </ul>

                Der Informationsvektor enthält alle Beobachtungen:

                $$\mathcal{I} = (z_0, \dots, z_k, a_{0}, \dots, a_{k-1}) \text{ für } k=0, \dots, N-1$$

                Der Informationsvektor beschreibt die zeitliche Entwicklung des
                Agenten. Mit $P(x_0)$ und $\mathcal{I}_k$ ist sämtliche
                Information gegeben um zum Zeitpunkt $k$ eine
                Planungsentscheidung zu treffen.

                Das korrespondierende MDP wird <b>Informations-MDP</b> genannt.

                Das zu lösende dynamische Programm lautet:

                $$J_N(\mathcal{I}_N) = E(g_N(x_N) | \mathcal{I}_N)$$

                $$J_k(\mathcal{I}_k) = \min_{a_k} (E_{x,z}(g_k(x_k, a_k) + J_{k+1}(\mathcal{I}_k, z_{k+1}, a_k)(\mathcal{I}_k, a_k))) \text{ für } k=0, 1, \dots, N-1$$

                Die Lösung ist eine öptimale Strategie $\pi_k^* (\mathcal{I}_k) = a_k^*$

                Nur in Ausnahmefällen geschlossen lösbar, z.B. lineare Modelle.

            </li>
        </ul>

    </dd>
    <dt><dfn id="statistik">Statistik</dfn></dt>
    <dd>Seien $S=\{z_1, \dots, z_n\}$ Stichproben (Samples) einer Zufallsvariablen
        $z \sim P(z | \Theta)$ mit unbkanntem Parameter $\Theta$. Eine
        Statistik ist eine Funktion $T(S)=t$, welche zwar von $S$, nicht aber
        von $\Theta$ abhängt.<br/>
        <br/>
        Konstante Funktionen, minimum, maximum, durschschnitt, median, ...</dd>
    <dt><dfn>Hinreichende Statistik</dfn> (engl. <dfn id="sufficient-statistic">sufficient statistic</dfn>)</dt>
    <dd>Ziel: Kompression, d.h. Darstellung von $\mathcal{I}_k$ von geringer
        Dimension.

        Eine Statistik $T$ heißt hinreichend für $\Theta$, wenn keine weitere
        Statstik auf $S$ existiert, welche zusätzliche Informationen über
        $\Theta$ liefert.

        Ist $T(S) = t$ gegeben, dann liefert die volle Kentnis von $S$ keine
        Zusatzinformation über $\Theta$.


        Beispiele:

        <ul>
            <li>Der Stichprobenmittelwert $\hat{z}$ von $n$ unabhängigen
                Stichproben $z_i$ einer normalverteilten Zuvallsvariabeln
                $z \sim \mathcal{N}(\mu, \sigma)$ ist eine hinreichende
                Statistik für $\mu$.</li>
            <li></li>
        </ul>
    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Bayes-Sch%C3%A4tzer"><dfn>Bayes'scher Schätzer</dfn></a></dt>
    <dd>Prädiktion + Filterschritt = Bayes-Schätzer.<br/>
        TODO (z.B. in GPS arbeitet eine Variante; Extended Kalman Filter)<br/>
        Der Bayes-Schätzer ist im Allgemeinen nciht geschlossen berechenbar.
        </dd>
    <dt><dfn>Verteilungs-MDP</dfn> (<dfn>Belief-state MDP</dfn>)</dt>
    <dd>Belief ist die Verteilung (TODO)</dd>
    <dt><dfn>Lineare Planungsprobleme in POMDPs</dfn></dt>
    <dd>Zustandsraummodell (Systemmodell):
        $$x_{k+1} = A_k \cdot x_k + B_k a_k + r_k^{(s)}$$

        Messmodell (Sensormodell):
        $$z_k = H_k x_k + v_k$$

        <ul>
            <li>$r_k^{(s)}, v_k$ sind normalverteilte Rauschterme:

                $$f_k^x(x_k) = N(x_k; \hat{x}_k, C_k^x) = \frac{1}{\sqrt{|2 \pi C_k^x|}} \exp(-1/2 (x_k - \hat{x}_k)^T (C_k^x)^{-1} (x_k - \hat{x}_k))$$

                mit Mittelwert $\hat{x}_k$ und Kovarianzmatrix $C_k^x$
            </li>
            <li>$X = \mathbb{R}^{n_x}, A=\mathbb{R}^{n_k}, Z=\mathbb{R}^{n_z}$</li>
            <li>Ziel: Überführung des Zustandes $x_0$ in Zielzustand $x_t = [0, ..., 0]^T$
                durch Minimierung der quatratischen Kostenfunktion
                $E(x_N^T Q_N x_n + \sum_{k=0}^{N-1} (x_k^T Q_k x_k + a_k^T R_k a_k) | I_N)$

                mit symmetrisch, positiv definiten Gewichtungsmatrizen
                $Q_N, Q_k, R_k$ und Informationsvektor $I_N$.


                Dies ist ein lineares, quadratisches Gauß'sches Planungsprobelm (LQG)</li>
        </ul>

        Planer besteht aus 2 Komponenten:

        <ul>
            <li>Zustandsschätzer</li>
            <li>Strategie</li>
        </ul>

        Zustandsschätzer:

        <ul>
            <li>Annahme: bel. Aktionsfolge $a_{0:N-1}$ gegeben: <a href="https://martin-thoma.com/kalman-filter/">Kalman-Filter</a> (Optimaler Schätzer für lineare Modelle mit normalverteilten Größen)</li>
        </ul>

        Prädiktion ($k \rightarrow k+1$)
        <ul>
            <li>Gegeben: A posteriori Wahrscheinlichkeitsdichte $f_a^e(x_k) = N(x_k; \hat{x}_k^e, C_k^e) = P(x_k | I_k)$</li>
            <li>Gesucht: prädizierte Wahrscheinlichkeitsdichte $f_{k+1}^p(x_{k+1}) = N(x_{k+1}; \hat{x}_k^P, C_k^P) = P(x_{k+1} | I_k, a_k)$</li>
            <li>Berechnung der Parameter:

                <ul>
                    <li>Mittelwert: $\hat{x}_{k+1}^P = A_k \hat{x}_k^e + B_k a_k$</li>
                    <li>Kovarianzmatrix: $C_k^P = A_k C_k^e A_k^T + C_k^w$</li>
                </ul>

            </li>
        </ul>

        Filterschritt ($k \overset{Z_k}{\rightarrow} k$)
        <ul>
            <li>Gegeben: prädizierte Dichte $f_k^P(x_k)$, Messung $z_k$</li>
            <li>Gesucht: a-posteriori Dichte $f_k^e(x_k)$</li>
            <li>Berechnung der Parameter:

            <ul>
                <li>Mittelwert: $\hat{x}_k^e = \hat{x}_k^P + K_k (z_k - H_k \hat{x}_k^P)$</li>
                <li>Kovarianzmatrix: $C_k^e = C_k^P - K_k H_k C_k^P$</li>
                <li>Kalman-Gain: $K_k = C_k^P H_k^T (H_k C_k^P H_k^T + C_k^v)^{-1}$</li>
            </ul>

            </li>
        </ul>

        Insgesamt:
        <ul>
            <li>Geschlossene Berechnung der Zustandsverteilung</li>
            <li>Kalman-Filter erfüllt <span id="blue">BLUE</span>-Eigenschaft:

            <ul>
                <li>Best Linear: Optimaler Schätzer für lineare Modelle und
                                 normalverteilte Größen; bester linearer
                                 Schätzer  wenn lineare Modelle aber beliebige
                                 Verteilungen (z.B. Partikelfilter ist
                                 nicht-linear); d.h. minimale Varianz</li>
                <li>Unbiased Estimator: Erwartungstreuer Schätzer</li>
            </ul>

            </li>
        </ul>
    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Regelkreis"><dfn>Regelkreis</dfn></a> (<dfn>Control system</dfn>)</dt>
    <dd>Ein Regelkreis ist ein technisches System, welches einen Zielzustand
        anstrebt.</dd>
    <dt><dfn id="ol-planung">Open-loop Planung</dfn> (<dfn>OL Planung</dfn>)</dt>
    <dd>Unter einem Open-loop Control system (offener Regelkreis) versteht man
        ein technisches System welches ohne Zustandsrückführung, also ohne
        Messung des Zustands nachdem die Regelung begonnen wurde, arbeitet.<br/>
        Beispiele sind Spühlmaschinen und Rasensprenger.<br/>
        In der Open-loop Planung wird ein optimaler Plan bestimmt.
    </dd>
    <dt><dfn>Closed-loop Planung</dfn> (<dfn>CL Planung</dfn>)</dt>
    <dd>Unter einem Closed-loop control system (geschlossenem Regelkreis)
        versteht man ein technisches System welches mit Zustandsrückführung, also
        mit Messung des Zustands während der Regelung, arbeitet.<br/>
        Beispiele sind System im Auto zum halten der Geschwindigkeit oder
        Rasensprenger welche die Feuchtigkeit überprüfen.<br/>
        Closed-loop Planung kann mit dynamischer Programmierung gelöst werden.
        Geschlossene Lösung nur in Ausnahmefällen, sonst numerische
        Lösungsverfahren.<br/>
        In der closed-loop Planung wird eine optimale Strategie bestimmt.
    </dd>
    <dt><dfn id="olf-planung">Open-Loop-Feedback Planung</dfn> (<dfn>OLF Planung</dfn>)</dt>
    <dd>TODO</dd>
    <dt><dfn>Modellprädiktive Planung</dfn></dt>
    <dd>OLF-Planung über kürzeren, aber wandernden Horizont $M << N$

        Ablauf (on-line):

        <ol>
            <li>Berechnung von $P(x_k | I_k)$</li>
            <li>TODO ($E(\sum_{i=k} g_i(x_i, a_i) | I_k)$)</li>
            <li>Anwendung von $a_k^*$, zurück zu 1.</li>
        </ol>

        Eigenschaften:

        <ul>
            <li>Effiziente Planung für große $N$, insbesondere für $N=a$</li>
            <li>Verlängerung von $N$ führt nicht notwendigerweise zu besseren
                Planungsergebnissen; d.h. $N$ ist <b>kein</b> Trade-off zwischen
                Qualität und Komplexität.</li>
        </ul>

        Hier wird der Plan aktualisiert; OLF minimiert die Kosten garantiert
        stärker als OL-Planung (gleichheit im deterministischen Fall)
    </dd>
    <dt><dfn id="linearization">Linearisierung</dfn> (<dfn>Extended Kalman Filter</dfn>, <dfn id="ekf">EKF</dfn>)</dt>
    <dd>Gegeben ist ein Nichtlineares Zustandsraummodell:

        $$x_{k+1} = p_k(x_k, a_k) + w_k\tag{Systemmodell}$$
        $$z_k = h_k(x_k) + v_k\tag{Messmodell}$$

        Idee: Verwendung von LQR + Kalman Filter<br/>
        Linearisierung mittels Taylorreihenentwicklung<br/>
        Annahmen: $p_k$ ist differenzierbar und nichtlinearer Anteil in Umgebung
        ist vernachlässigbar.<br/>
        Linearisierung um Nominalwerte $\bar{x}_k, \bar{a}_k$.
        $$p_k(x_k, a_k) \approx p_k(\bar{x}_k, \bar{a}_k) + A_k (\underbrace{x_k - \bar{x}_k}_{=: \Delta x_k}) + B_k (\underbrace{a_k - \bar{a}_k}_{\Delta a_k})$$
        mit Jakobi-Matrizen:
        $$A_k = \frac{\partial}{\partial x_k} p_k(x_k, a_k)|_{x_k = \bar{x}_k, a_k = \bar{a}_k}$$
        $$B_k = \frac{\partial}{\partial a_k} p_k(x_k, a_k)|_{x_k = \bar{x}_k, a_k = \bar{a}_k}$$
        $\Rightarrow$ Lineares Modell: $\Delta x_{k+1} \approx A_k \cdot \Delta x_k + B_k \Delta a_k$
        mit $\Delta x_{k+1} = p_k(x_k, a_k) - p_k(\bar{x}_k, \bar{a}_k)$<br/>
        <br/>
        Wahl der Nominalwerte $\bar{x}_k, \bar{a}_k$:
        <ul>
            <li>Strategie:
            <ul>
            <li>Zielzustand $\bar{x}_k = x_+ = [0, \dots, 0]^T, \bar{a}_k = [0, \dots, 0]^T \forall k$</li>
            <li>Zustandssolltrajektorien bei Verfolgungsproblem</li>
            <li>Prädiktiv: $\bar{x}_{k+1} = p_k(\bar{x}_k, \bar{a}_k)$ mit $\bar{x}_0 = E(x_0)$ und beliebig $\bar{a}_{0:N-1}$</li>
            <li>Iterativ: Starte mit beliebigem $\bar{a}_{0:N-1}$ und $\bar{x}_0 = E(x_0)$
                <ul>
                    <li>Bestimme $\bar{x}_{k+1} = p_k(\bar{x}_k, \bar{a}_k) \forall k$</li>
                    <li>Linearisiere und löse LQR $\Rightarrow \bar{a}_k = \pi_k(\bar{x}_k)$</li>
                    <li>zurück zu 1.</li>
                </ul>

            </li>
            </ul>
            </li>
            <li>Schätzer:
                <ul>
                    <li>Linearisierung um $\bar{x}_k = \hat{x}_k^l, \bar{a}_k=\pi_k(\hat{x}_k^l)$

                        $$\hat{x}^p_{k+1} = p_k(\hat{x}_k^l, \bar{a}_k)$$

                        $$C_{k+1}^P = A_k C_k^e A_k^T + C_k^w$$
                    </li>
                    <li>Filterschritt: Linearisierung um $\bar{x}_k = \hat{x}_k^p$

                        $$\hat{x}_k^e = \hat{x}_k^P + K_k (z_k - h_k(\hat{x}_k^P))$$
                        $$C_k^e = C_k^P - K_k H_k C_k^P$$
                    </li>
                </ul>
            </li>
        </ul>
    </dd>
    <dt><dfn>Bedingte Differentielle Entropie</dfn></dt>
    <dd>

        $$H(x|z, a) = - \int_z f(z|a) \cdot \int_{\mathcal{X}} f(x|z, a) \cdot \log (f(x|z, a)) \mathrm{d}x \mathrm{d} z$$

        Die differentielle Entropie erweitert die Schannon-Entropie auf den
        kontinuierlichen Fall. Unschön ist, dass sie negativ werden kann.<br/>
        <br/>
        Sie bewertet Unsicherheit anhand der "räumlichen" Konzentration von
        Wahrscheinlichkeitsmassen.

    </dd>
    <dt><dfn id="sensoreinsatzplanung">Sensoreinsatzplanung</dfn></dt>
    <dd>

        TODO

        Informationstheoretische Kosten gehen in Kovarianz-basierte Kosten
        wie z.B. Entropie über:

        TODO

        In der Sensoreinsatzplanung liefern Open-Loop und Closed Loop
        Verfahren, gegeben TODO, die selben Kosten. Daher wird
        Open-Loop-Planung verwendent. Das heißt, der optimale Plan
        $a_{0:N-1}^*$ wird mittels deterministischer Planung
        (Kürzeste-Wege-Suche), bestimmt.

        <ul>
            <li>$g_i(x_i, a)$: Schrittkosten</li>
        </ul>

        Der Suchbaum hat $|A|^N$ Pfade. (0-1 Programme)

    </dd>
    <dt><dfn>Monotonie der Riccarti-Gleichung</dfn></dt>
    <dd>

        Sei
        $$V_k(\Lambda, C) := C_k^w + (A_k - \Lambda \cdot H_k) C \cdot (A_k - \Lambda H_k)^T + \Lambda C_k^v V^T$$
        mit
        $$\Lambda = K_k = A_k C H_k^T (H_k C H_k^T)^{-1} \text{ und } C = C_k^P$$
        gilt $V_k = S_k$, da

        $$
        \begin{align}
            V(K, C^P) &= C^W + (A - KH) C^P (A-KH)^T + KC^V K^T\\
                      &= C^W + AC^P A^T - KH C^P A^T + KHC^P H^T K^T - A C^P H^T K^T KC^v K^T\\
                      &= C^W + AC^P A^T - KH C^P A^T - AC^P H^T K^T + K (HC^P H^T + C^v) K^T \cdot A^CP H {(H C^P H^T + C^V)}^{-1}\\
                      &= C^W + AC^P A^T - KH C^P A^T = S_k(C^P)
        \end{align}
        $$

        Weiterhin ist $\Lambda = K_k$ das Minimum von $V_k$ für gegebenes $C$,
        da der Kalman-Filter der optimale Schätzer für lineare Modelle ist.

        Mit $\tilde{K}_k = A_k \tilde{C} H_k^T {(H_k \bar{C} H_k^T + C_k^v)}^{-1}$
        gilt
        $$S_k(C) = V_k(K_k, C) \prec V_k(\bar{K}_k, C) \prec V_k(\bar{K}_k, \bar{C}) = S_k(\tilde{C})$$
    </dd>
    <dt><dfn id="approximative-planning">Approximative Planung</dfn></dt>
    <dd>

        Abbildung auf lineare Sensoreinsatzplanung mittels

        <ul>
            <li>Linearisierung und</li>
            <li>modellprädiktiver Planung</li>
        </ul>

        <u>Linearisierung</u>

        Hier werden Nominalwerte $\bar{x}_{k:N-1}$ benötigt. Da die Aktion nur
        die Messgleichung, nicht jedoch die Systemgleichung betrifft können die
        $$\bar{x}_k = \hat{x}_k^P; \qquad \bar{x}_{k+1} = p_k(\bar{x}_k, 0)$$
        Anschließend wird linearisiert.

        <u>Ablauf</u>

        <ol>
            <li>Nach Messung: (approximative) Berechnung ovn $P(x_k | I_k)$
                bzw. $P(x_{k+1} | I_k)$ z.B. mittels EKF.</li>
            <li>Berechnung der Nominalwerte $\bar{x}_{k+1:k+M}$ mit
                $\bar{x}_{k+1} = E(x_{k+1} | I_k) = \hat{x}_{k+1}^P$</li>
            <li>Linearisierung</li>
            <li>Berechnung des optimalen Plans $a_{k+1:k+M}^*$ für
                lineares Problem.</li>
            <li>Anwenden von $a_{k+1}^*$; zurück zu 1.</li>
        </ol>

        <u>Beispiel</u>: Steuerung eines mobilen Sensors
        <ul>
            <li>Objekt: $x_{k+1} = \begin{pmatrix}1 & T & 0 & 0\\
                                                  0 & 1 & 0 & 0\\
                                                  0 & 0 & 1 & T\\
                                                  0 & 0 & 0 & 1\end{pmatrix} \cdot x_k + w_k$
                mit $x_k = \begin{pmatrix}x_k\\ \dot{x}_k, y_k, \dot{y}_k\end{pmatrix}$</li>
            <li>Sensor: $z_k = \sqrt{(x_k - x_k^S(a_k))^2 + (y_k - y_k^S(a_k))^2} + v_k$</li>
            <li>Aktion $a_k$ ist Lenkwinkel</li>
            <li>Kinematisches Sensormodell:

                $$\begin{pmatrix}x_{k+1}^S\\
                                 y_{k+1}^S\\
                                 \phi_{k+1}^S\end{pmatrix}
                 = \begin{pmatrix}x_{k}^S\\
                                 y_{k}^S\\
                                 \phi_{k}^S\end{pmatrix} +
                   \begin{pmatrix}T v TODO\\
                                  TODO\\
                                  TODO\end{pmatrix}$$

            </li>
        </ul>

    </dd>
</dl>

TODO:

* Ausblendeigenschaft der Dirac-Delta-Funktion


### Reinforcement Learning

<dl>
    <dt><dfn id="rl">Reinforcement Learning</dfn> (<dfn>RL</dfn>)</dt>
    <dd>Reinforcement learning ist ein Subfeld des maschinellen Lernens,
        welches sich auf Probleme der optimalen Kontrolle fokusiert.<br/>
        <br/>
    Problem:

    <ul>
        <li>Was ist wenn die Kostenfunktion $g_k$ unbekannt ist?</li>
        <li>Was ist wenn das Modell, das heißt die Übergangswahrscheinlichkeiten
            $P(x_{k+1} | x_k, a_k)$ unbekannt sind?</li>
        <li></li>
    </ul>

    Dies wird durch ein Zusammenspiel aus lernen und Planen gelöst.

    (Agent-Umelt-Bild)

    Man lernt also aus Erfahrung und <b>Interaktion mit der Umwelt</b>.<br/>
    <br/>
    Eigenschaften und Besonderheiten:
    <ul>
        <li>Prinzipien des biologischen Lernens (Negatives / Positives Verstärken)

            <ul>
                <li>Intrinsische Motivation etwas erreichen zu wollen:
                    Abstraktion als Kosten- / Belohnungsfunktion, die es über
                    die Zeit zu min. / max. gilt.</li>
                <li>Exploratives Lernen</li>
            </ul>
        </li>
        <li>Unterschied zu "klassischen" Lernverfahren:
            <ul>
                <li>Lernen erfolgt unüberwacht und explorativ durch
                    aktive Interaktion mit der Umwelt.</li>
                <li>RL kombiniert Aspekte der Planung mit Lernmethodik.
                    Da RL unüberwacht ist erfolgt die Entscheidung aufgrund
                    eigener Erfahrung.</li>
            </ul>
        </li>
    </ul>

    <u>Definition:</u><br/>
    MDP mit folgenden Unterschieden:
    <ul>
        <li>2 Zeithorizont:

            <ul>
                <li>$N = \infty$ für fortlaufende Aufgaben</li>
                <li>$N < \infty$ für episodische Aufgaben (diese haben einen
                     terminaler Zustand)</li>
            </ul>

        </li>
        <li>5 Keine Übergangswahrscheinlichkeiten gegeben</li>
        <li>6 Belohnungen (reward) $r_k \in \mathbb{R}$ für Aktion
            $a_k$ in Zustand $x_k$ mit Nachfolgezustand $x_{k+1}$.<br/>
            $$r_k = g_k(x_k, a_k, x_{k+1})$$
            wobei $g_k$ unbekannt.</li>
        <li>8 Ziel: Maximierung der erwarteten Belohnung über die Zeit.
            $$J(x_k) = E(R_k | x_k)$$

            <ul>
                <li>Fortlaufender Zeithorizont: $R_k = \sum_{t=0}^\infty \gamma^t r_{k+t}$
                    mit Diskontierungsfaktor $\gamma \in [0, 1)$</li>
                <li>Episodischer Zeithorizont: $R_k = \sum_{i=0}^N r_{k+i},$
                    wobei $N$ unbekannt ist.</li>
            </ul>

        </li>
    </ul>

    Dynamisches Programmieren ist nicht anwendbar, da das Modell und die Kosten
    unbekannt sind. Die optimale Strategie wird aus Erfahrung approximiert.<br/>
    <br/>
    <u>Unterscheidungsmerkmale</u>:
    <ul>
        <li>Horizont:

            <ul>
                <li>fortlaufend, z.B. in Regelungstechnik das inverse Pendel</li>
                <li>episodisch in Spielen</li>
            </ul>

        </li>
        <li>Approximation / lernen:

            <ul>
                <li>on-policy: Dieselbe Strategie wird zugleich verbessert
                               und angewandt.</li>
                <li>off-policy: verwendet 2 Strategien
                              <ul>
                                  <li>Strategie 1: erzeugen von Aktionen</li>
                                  <li>Strategie 2: wird verbessert</li>
                              </ul>
                </li>
            </ul>
        </li>
        <li>Zustands- und Aktionsraum:

            <ul>
                <li>diskret</li>
                <li>kontinuierlich</li>
            </ul>

        </li>
        <li>Übergangswahrscheinlichkeiten / Kosten

            <ul>
                <li>Modellfreie Verfahren: Lernen nur die optimale Strategie</li>
                <li>Modelllernende Verfahren: Lernen von Strategie und Modell</li>
            </ul>

        </li>
    </ul>

    <u>Grundvarianten des RL</u>: (TODO: Grafiken)

    <ul>
        <li>Wertefunktionsbasiert: Schätzen die Wertefunktion / Q-Funktion aus
            Lernstichproben (Monte Carlo (MC); Temporal Difference (TD),
            Verantwortlichkeitsspur (eligibility trace, credit assignment);
            Verwendung von Funktionsapproximatoren)</li>
        <li>Modelllernende Methoden</li>
        <li>Strategiesuche (Policy search; Funktionsapproximatoren - neuronale
            Netze)</li>
    </ul>

    </dd>
    <dt><dfn id="monte-carlo-methods">Monte-Carlo Methoden</dfn></dt>
    <dd>

        <u>Idee</u>: Erlernen einer Strategie aus Beispielepisoden.

        <ul>
            <li>Approximation des Erwartungswertes durch Stichproben (Samples)<br/>
                $$E(R) = \frac{1}{N} \sum_{k=1}^N r_k =: \bar{R}_N,$$
                wobei $r_k$ die Belohnung im Zeitschritt $k$ ist.<br/>
                Rekursiv:
                $$\bar{R}_{N+1} = \bar{R}_N + \frac{1}{N+1} (r_{N+1} - \bar{R}_N) \text{ mit } \bar{R}_1 = r_1$$</li>
            <li>TODO</li>
        </ul>

        Funktionieren ausschließlich auf episodischen Problemen (d.h mit Ende),
        wie z.B. Spielen.

        <ul>
            <li>Gegeben: Strategie $\pi$</li>
            <li>Gesucht: Wertefunktion $J_\pi(x)$</li>
            <li>Ablauf:

            <ol>
                <li>Für beliebigen Initialzustand erzeuge Episode mittels $\pi$</li>
                <li>Für jeden Zustand $x$ in Episode:

                <ul>
                    <li>$R \gets$ kummulative Belohnung ab 1. Vorkommen von $x$ (First-visit, es gibt auch every-visit)</li>
                    <li>$n(x) \gets n(x) + 1$</li>
                    <li>$J_\pi(x) \overset{(*)}{\gets} J_\pi (x) + \frac{1}{n(x)} (R - J_\pi (x))$</li>
                </ul>

                </li>
            </ol>
            </li>
        </ul>

        Konvergiert für unendliche Anzahl an Episoden.

        Vorteile:

        <ul>
        <li>Aufwand ist unabhängig von der Anzahl der Zustände (genauso wie Partikelfilter).</li>
        <li>Einschränkungen auf Teilmenge von $\mathcal{X}$ möglich.</li>
        </ul>

        Nachteile / Einschränkungen:
        <ul>
          <li>Nur episodisch</li>
        </ul>
    </dd>
    <dt><dfn id="monte-carlo-rl">Monte Carlo RL</dfn></dt>
    <dd>Idee: Schätzen der Q-Funktion $Q(x, a)$.
        TODO: Diagramm

    Für gegebene Episode:
    <ul>
      <li>Aktualisierung der $Q$-Funktion für alle besuchten Zustände $x$ und gewählte Aktionen $a$</li>
      <li>Verbesserung der Strategie für alle besuchten Zustände</li>
    </ul>

    Problem: pro Zustand wird nur eine Aktion bewertet. Das führt nur auf sehr lokalen bereichen zu einer Strategieverbesserung.

    </dd>
    <dt><dfn id="exporation-exploitation">Exploration vs. Exploitation</dfn></dt>
    <dd>

        <blockquote>Exploit what is already known to obtain rewards, but explore in order to choose better actions in the future.</blockquote>

        <ul>
            <li>Exploring Starts:
            Jedes Zustands-Aktions-Paar gleichwahrscheinlich als Startwert für Episode. Vorteil: Führt zu einer deterministischen Strategie; für vile reale Systeme nicht realisierbar (z.B. Roboter kann nicht bei voller Kraft starten)
            </li>
        </ul>

        Verwendung probabilistischer Strategien:

        $$\pi: \mathcal{X} \times \mathcal{A} \rightarrow [0, 1]$$
        $$\pi(x, a) = P(a | x)$$

        <ul>
            <li><u>$\varepsilon$-gierige Strategien</u><br/>
                gierige Aktion: Aktion mit höchster erwarteter Belohnung:
                $$a^+ = \arg \max_a Q(x,a)$$
                erhält höchste Wahrscheinlichkeit:
                $$\pi(x, a^*) = 1 - \varepsilon + \frac{\varepsilon}{|A(x)|}$$
                nicht-gierige Aktionen: $\pi(x, a) = \frac{\varepsilon}{|A(x)|}$
                mit $0 < \varepsilon \ll 1$<br/>
                <br/>
                Vorteil: Kein Festlegen auf suboptimale Aktion<br/>
                Nachteil: Wahl von $\varepsilon$ problematisch<br/>
                <br/>
                $\varepsilon$-greedy MC Strategieiteration ist on-policy</li>
            <li><u>Softmax-Strategie</u><br/>

                Rangfolge entsprechend der Wertigkeit der Aktionen

                $$\pi(x, a) = \frac{e^{Q(x, a) / \tau}}{\sum_a e^{Q(x,a) / \tau}} \text{ mit "Temperatur"} \tau > 0$$

                Die generierte Verteilung nennt sich Gibbs- oder auch
                Boltzmann-Verteilung.

                $\tau$ groß: $Q(x,a) / \tau$ wird klein, d.h. die Aktionen
                werden ähnlich wahrscheinlich gewählt. (TODO: Was ist groß?)

                $\tau$ klein: Die Aktionen werden mit deutlich
                unterschiedlicher wahrscheinlichkeit gezogen

                $\tau \rightarrow 0$: nahezu deterministische, gierige
                Strategie.

                Vorteil gegenüber $\varepsilon$-greedy: Rangfolge bei Auswahl.
                Nachteil gegenüber $\varepsilon$-greedy: Wahl von $\tau wird
                of als schwieriger angesehen als die Wahl von $\varepsilon$.

            </li>
            <li><u>GLIE-Strategie</u><br/>

            <b>G</b>reedy in the <b>l</b>imit with <b>i</b>nfinite <b>e</b>xploration

            Damit eine Strategie GLIE ist, muss erfüllt sein:

            <ul>
                <li>Alle $(x, a)$-Paare werden unendlich oft besucht</li>
                <li>Strategie konvergiert zu einer gierigen Strategie, d.h.
                    $$\lim_{k \rightarrow \infty} \pi(x, a^*) = 1 \text{ für } \arg \max_a a(x, a)$$</li>
            </ul>

            Beispiel bei $\varepsilon$-greedy Strategie:

            <ul>
                <li>$\varepsilon$ mit Zeit abklingen lassen</li>
                <li>$\varepsilon(x) = \frac{\varepsilon}{n(x)}$ mit $\varepsilon \in (0, 1)$ und $n(x)$ zählt wie häufig der Zustand $x$ besucht wurde.</li>
            </ul>


            Fazit MC:

            Vorteile
            <ul>
                <li>Erlernen der optimalen Strategie ohne Modellwissen möglich,
                    sofern GLIE-Strategien verwendet werden</li>
                <li>Auch anwendbar, wenn die Markov-Annahme nicht gilt, da kein
                    Bootstrapping</li>
            </ul>

            Nachteile:
            <ul>
                <li>Allgemeine Konvergenzeigenschaften (noch) nicht formal
                    bewiesen. (Schon für Strategiebewrtung, nicht aber für RL)</li>
                <li>Funktioniert nur für episodische RL-Probleme</li>
            </ul>

            </li>
        </ul>
    </dd>
    <dt><dfn id="temporal-difference">Temporal Difference Verfahren</dfn> (<dfn>TD</dfn>)</dt>
    <dd>TD-Verfahren nutzen die zeitliche Differenz zweier Schätzungen
        eines Zustandwertes. Die Aktualisierungen sind nach jedem
        Zustandwechsel. Das heißt, im Gegesatz zu MC-Verfahren, sind
        TD-Verfahren für Episodische und fortlaufende RL-Probleme geignet.<br/>
        <br/>
        <u>Unterschiedliche Schätzung:</u><br/>
        $$
        \begin{align}
        J_\pi(x) &= E(R_k | x_k = x) \tag{(1)}\\
                 &= E(r_k + \gamma \sum_{i=0}^\infty \gamma^i \cdot r_{k+i+i} | x_k = x)\tag{(2)}
        \end{align}
        $$
        MC-Verfahren ganz (1) mittels Stichprobenfolge. TD-Verfahren schätzen
        die Summe in (2) durch eine Stichprobe $r_k$.

        <u>TD-Strategiebewertung</u><br/>
        Erinnerung an DP-Strategiebewertung:<br/>
        $$J_\pi(x_k) \gets r_k(x_k, \pi (x_k)) + \alpha \sum_{x_{k+1}} P(x_{k+1} | x_k, \pi(x_k)) \cdot J_\pi (x_{k+1})$$
            Allerdings ist $P( \cdot | x_k, a)$ unbekannt. Daher wird es mittels
            einer einzelnen Stichprobe $(x_k, r_k, x_{k+1})$ geschätztz und
            ein Mittelwert zwischen dem aktuellen Wert und der Schätzung erstellt.

            $$J_\pi(x_k) \gets (1-\alpha) \cdot \underbrace{J_\pi(x_k)}_{\text{aktueller Wert}} + \alpha \cdot \underbrace{(\underbrace{r_k + \gamma \cdot J_\pi(x_{k+1})}_{\text{erwarteter Wert}} - J_\pi(x_k))}_{\text{zeitliche Differenz}}$$

            Konvergenz bei variabler Schrittweiter $\alpha = \alpha_k$ falls

            $$\sum_{k=1}^\infty \alpha_k = \infty \text{ und } \sum_{k=1}^\infty \alpha_k^2 < \infty$$

            Typische Wahl für $\alpha$: $\alpha(x, a) = \frac{1}{1+ m(x, a)}$,
            wobei $m(x, a)$ die Anzahl der Besuche von $(x, a)$ ist.
        </dd>
    <dt><dfn>Einschritt-TD-Verfahren</dfn></dt>
    <dd>Strategiebewertung $Q$-Funktion

        $$Q(x_k, a_k) \gets Q(x_k, a_k) + \alpha \cdot [r_k + \gamma \cdot Q(x_{k+1}, a_{k+1}) - Q(x_k, a_k)]$$

        Aktualisierung nach Ausführung von $a_k$ liefert Belohnung $r_k$ und
        Nachfolgezustand $x_{k+1}$.

        <b>ABER</b> Folgeaktion $a_{k+1}$ wird benötigt.

    </dd>
    <dt><dfn>SARSA</dfn> (<dfn>State Action Reward State Action</dfn>)</dt>
    <dd>SARSA ist ein TD-Vefahren.

        Auswahl von $a_{k+1}$ gemäß Strategie $\pi$ $\rightarrow$ on-policy

    </dd>
    <dt><dfn>Q-Learning</dfn></dt>
    <dd>Q-Learning ist ein TD-Vefahren.

        $$Q(x_k, a_k) \gets Q(x_k, a_k) + \alpha \cdot [r_k + \gamma \cdot \underbrace{\max_a Q(x_{k+1}, a)}_{J(x_{k+1})} - Q(x_k, a_k)]$$

        $\Rightarrow$ Aktualisierung von $Q$ erfolgt unabhängig von $\pi$
        $\rightarrow$  Off-policy

        (Q-Learning hat sich im Gegensatz zu SARSA durchgesetzt)

        Wenn die Strategie eine GLIE-Strategie ist, kann man mit Q-Learning die
        Konvergenz beweisen
    </dd>
    <dt><dfn>Fazit TD-Learning</dfn></dt>
    <dd>

        Vorteile:

        <ul>
            <li>Beide Verfahren konvergieren sofern GLIE</li>
            <li>Einfach zu implementiernen, lernen pro Zeitschritt</li>
        </ul>

        Nachteile:

        <ul>
            <li>Bootstrapping problemantisch wenn Markov-Annahme nicht erfüllt.
            </li>
        </ul>

    </dd>
    <dt><dfn>Mehrschritt-TD-Verfahren</dfn></dt>
    <dd>$$
        \begin{align}
        R_k^{(n)} &= r_k + \gamma \cdot r_{k+1} + \dots + \gamma^{n-1} + \gamma^n J_\pi (x_{k+1})\\
        R_k^{(1)} &\hat{=} TD\\
        R_k^{(n)} &\hat{=} RL
        \end{align}
        $$

        Strategiebewertung

        $$J_\pi(x_k) \gets J_\pi (x_k) + \alpha \cdot [R_k^{(n)} - J_\pi(x_k)]$$


        Vorteile:

        <ul>
            <li>Schnellere Konvergenz als Einschritt-TD</li>
            <li>Flexible Verbindung von MC und TD</li>
        </ul>

        Nachteil: Unpraktisch für große $n$.
    </dd>
</dl>


## Overviews

### MDP vs POMDP vs RL

<table>
    <tr>
        <th>&nbsp;</th>
        <th>MDP</th>
        <th>POMDP</th>
        <th>RL</th>
    </tr>
    <tr>
        <td>Agent-Environment Diagram</td>
        <td><img src="../images/2016/07/agent-environment-diagram-mdp.png" alt="Agent-Environment Diagram of a MDP" /></td>
        <td><img src="../images/2016/07/agent-environment-diagram-pomdp.png" alt="Agent-Environment Diagram of a POMDP" /></td>
        <td><img src="../images/2016/07/agent-environment-diagram-rl.png" alt="Agent-Environment Diagram of a RL problem" /></td>
    </tr>
    <tr>
        <td>1</td>
        <td colspan="3" class="text-center">Zustandsraum $\mathcal{X} \subseteq \mathbb{R}^n$</td>
    </tr>
    <tr>
        <td>2</td>
        <td colspan="2">Diskrete Zeitschritte $k=0, \dots, N$</td>
        <td>Zeithorizont: $N = \infty$ für fortlaufende Probleme, $N < \infty$
            für episodische Probleme</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Initialzustand $x_0 \in \mathcal{X}$ zum Zeitpunkt $k=0$.</td>
        <td>Initialzustand $x_0$ ist Zufallsvariable</td>
        <td>Wie MDP (TODO?)</td>
    </tr>
    <tr>
        <td>4</td>
        <td colspan="3" class="text-center">Aktionsmenge $A_k(x_k) \neq \emptyset$</td>
    </tr>
    <tr>
        <td>5</td>
        <td colspan="2">Übergangswahrscheinlichkeiten $x_{k+1} \sim P_X (\cdot | x_k, a_k)$</td>
        <td>Keine Übergangswahrscheinlichkeiten gegeben</td>
    </tr>
    <tr>
        <td>6</td>
        <td colspan="2">Additive Kostenfunktion $g_N(x_N) + \sum_{k=0}^{N-1}$ g_k(x_k, a_k)</td>
        <td>Belohnung $r_k = g_k(x_k, a_k, x_{k+1})$ wobei $g_k(\cdot)$ unbekannt</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Zustand ist direkt beobachtbar nach Anwendung der Aktion</td>
        <td>Beobachtung / Messung $z_k$ gemäß der bedingten Verteilung
            $$z_k \sim P( \cdot | x_k, a_{k-1})$$</td>
        <td>Wie MDP (?)</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Minimiere $J_{\pi_{0:N-1}} (x_0) := E (g_N (x_N) + \sum_{k=0}^{N-1} g_k (x_k, \pi_k(x_k)))$</td>
        <td>Minimiere $J_{\pi_{0:N-1}} (\cdot) := E (g_N (x_N) + \sum_{k=0}^{N-1} g_k (x_k, \pi_k(\cdot)))$</td>
        <td>Maximimierung der Belohnung $J(x_k) = E (R_k | x_k)$. Im fortlaufenden
            Fall $$R_k = \sum_{t=0}^\infty \gamma^t r_{k+t}$$ mit
            Diskontierungsfaktor $\gamma \in [0, 1)$,
            im episodischen Fall
            $$R_k = \sum_{i=k}^{N} r_i,$$
            wobei $N$ unbekannt ist.</td>
    </tr>
    <tr>
        <td>Lösungs&shy;algorithmen</td>
        <td>Dynamic Programming</td>
        <td>

            <ul>
                <li>Policy Iteration</li>
                <li>Value Iteration</li>
            </ul>

        </td>
        <td>Temporal Difference</td>
    </tr>
</table>


## Prüfungsfragen

* Welche 3 Themengebiete wurden in der Vorlesung behandelt und was sind die
  Unterschiede?<br/>
  → <a href="#mdp">MDP</a>, <a href="#pomdp">POMDP</a>, <a href="#rl">RL</a>
* Wie ist eine Nutzenfunktion definiert?<br/>
  → Siehe <a href="#nutzenfunktion">oben</a>
* Wie löst man Optimierungsprobleme ohne Nebenbedingungen?<br/>
  → Iterativer Abstieg (z.B. Gradientenverfahren), Dynamische Programmierung (TODO)
* Beweisen Sie, dass der Gradient senkrecht auf die Höhenlinien steht.<br/>
  → TODO
* Wie löst man Optimierungsprobleme mit Nebenbedingungen?<br/>
  → Lagrange (TODO)
* Wann ist es leichter / schwerer das Optimierungsproblem zu lösen?<br/>
  → Keine Nebenbedingungen, in $\mathbb{R}^n$ oder kleiner diskreter Raum (TODO)
* Welche numerischen Methoden zur Optimierung kennen sie?<br/>
  → Iterativer Abstieg (Gradientenverfahren, Newton-Verfahren), Dynamische Programmierung(?) (TODO)

### MDP

* Wie lautet die Definition eines MDP?<br/>
  → Siehe <a href="#mdp">oben</a>.
* Wie viele Pläne gibt es?<br/>
  → Für diskrete $\mathcal{X}, A$ und $N$ Zeitschritte gibt es $|A|^N$
     mögliche Pläne. In jedem Zeitschritt gibt es eine mögliche Aktion.
* Wie viele Strategien gibt es?<br/>
  → Für diskrete $\mathcal{X}, A$ und $N$ Zeitschritte gibt es $|A|^{N \cdot |\mathcal{X}|}$
     Strategien, da für jede Kombination aus Zeitschritt und Zustand eine
     Aktion gewählt werden muss.
* Was versteht man unter dynamischer Programmierenung?<br/>
  → Siehe <a href="#dynamic-programming">oben</a>.
* Wie lauten die Bellman-Gleichungen?<br/>
  → Siehe <a href="#bellman-equation">oben</a>.
* Was ist an den Bellman-Gleichungen problematisch?<br/>
  → TODO

### POMDP

* Wie lautet die Definition eines POMDP?<br/>
  → Siehe <a href="#pomdp">oben</a>
* Wie lautet die Kostenfunktion eines POMDP?<br/>
  → Siehe <a href="#pomdp-cost-function">oben</a>
* Was ist der Unterschied des LQR beim MDP und POMDP?<br/>
  → TODO (POMDP hat Erwartungswert)
* Was ist PWLC?<br/>
  → Piece-wise linear and Concave / Convex


### RL

* Welche Arten von RL gibt es?<br/>
  → TODO


## Notation

Der Dozent nutzt folgende Notation:

* $J^*, \pi^*$: Das Asterisk `*` deutet an, dass die Kosten / Strategie optimal
  sind.
* $\underline{x}$: Der Unterstrich deutet an, dass es sich um einen Vektor
  handelt. Diese Notation wurde in diesem Artikel **nicht** übernommen.
* $\hat{x}$: Der Hut zeigt an, dass der Zustand $x$ geschätzt ist.


## Material und Links

* [Vorlesungswebsite](http://ies.anthropomatik.kit.edu/lehre_proplan.php)
* Dimitri Bertsekas: Dynamic Programming and Optimal Control: Volume 1 (POMDP)
* Emanuel Todorov: [Optimal Control Theory](https://homes.cs.washington.edu/~todorov/papers/TodorovChapter06.pdf) (für Pontryagins Minimum-Prinzip)
* Dan Simon: Optimal State Estimation (Kalman-Filter)


## Vorlesungs&shy;empfehlungen

Folgende Vorlesungen sind ähnlich:

* [Analysetechniken großer Datenbestände](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/)
* [Informationsfusion](https://martin-thoma.com/informationsfusion/)
* [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/)
* [Machine Learning 2](https://martin-thoma.com/machine-learning-2-course/)
* [Mustererkennung](https://martin-thoma.com/mustererkennung-klausur/)
* [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)
* [Lokalisierung Mobiler Agenten](https://martin-thoma.com/lma/)
* [Probabilistische Planung](https://martin-thoma.com/probabilistische-planung/)


## Termine und Klausurablauf

Die Veranstaltung wird mündlich geprüft.
