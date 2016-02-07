---
layout: post
title: Neuronale Netze - Klausur
author: Martin Thoma
date: 2015-04-27 21:15
categories:
- German posts
tags:
- Klausur
- Machine Learning
- Neural Networks
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Neuronale Netze&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://isl.anthropomatik.kit.edu/english/21_74.php">Herrn Prof. Dr. Alexander Waibel</a> im Sommersemester 2015 gehört. Der Artikel wird bis zur mündlichen Prüfung laufend erweitert.</div>

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
    <td><a href="#intro">Einleitung</a></td>
    <td>-</td>
</tr>
<tr>
    <td>21.04.2015</td>
    <td>LVQ and related Techiques</td>
    <td>k-Means, OLVQ1, kompetitives Lernen, Mode Seeker, PCA</td>
</tr>
<tr>
    <td>22.04.2015</td>
    <td>-</td>
    <td>Übung</td>
</tr>
<tr>
    <td>28.04.2015</td>
    <td>Perceptron</td>
    <td>-</td>
</tr>
<tr>
    <td>12.05.2015</td>
    <td>Auto-Encoder</td>
    <td>Denoising- und Sparse Autoencoder, Bottleneck-Features, <a href="https://de.wikipedia.org/wiki/Kullback-Leibler-Divergenz">Kullback-Leibler-Divergenz</a>; <a href="https://de.wikipedia.org/wiki/Kettenregel#Mathematische_Formulierung">Kettenregel</a></td>
</tr>
<tr>
    <td>13.05.2015</td>
    <td>Deep Learning</td>
    <td>Momentum, Rprop, Newbob, L1/L2-Regularisierung (\(|w|\), \(w^2\)), weight decay</td>
</tr>
<tr>
    <td>19.05.2015</td>
    <td>Übung</td>
    <td>-</td>
</tr>
<tr>
    <td>20.05.2015</td>
    <td>Übung</td>
    <td>-</td>
</tr>
<tr>
    <td>26.05.2015</td>
    <td><abbr title="Self Organizing Map">SOM</abbr></td>
    <td>Hebbian Learning, "<abbr title="Vector Quantization">VQ</abbr>" mit SOM</td>
</tr>
<tr>
    <td>09.06.2015</td>
    <td>Effizientes Lernen</td>
    <td>Paralleles Lernen; Quickprop; Alternative Fehlerfunktion (cross entropy, <abbr title="Classification Figure of Merit">CFM</abbr>);
        weight elimination / regularization</td>
</tr>
<tr>
    <td>15.07.2015</td>
    <td>Summary</td>
    <td>When to use which objective function (cross entropy, MSE); Backpropagation; Weight initialization; Regularization (L2 weight decay, dropout); Time Delay NN; Recurrent Networks; Applications (Speech Recognition, Computer Vision)</td>
</tr>
</table>

### <a name="intro"></a> NN01-Intro.pdf

* Human Brain vs. Computer (Processing/Processors, Accuracy, Speed, Hardware, Design)
* Aufbau eines biologischen Neurons (vgl. [Wikipedia](https://de.wikipedia.org/wiki/Nervenzelle#.C3.9Cberblick_.C3.BCber_den_Aufbau_einer_Nervenzelle))


### NN02-Classification.pdf

{% caption align="aligncenter" width="500" alt="Rosenblatt-Perceptron which realizes logical or" text="Rosenblatt-Perceptron which realizes logical or" url="../images/2015/12/perceptron-or.png" %}

* McCullch-Pitts Neuron (weights, bias, activation function is step function)
* Rosenblatt Perceptron Algorithmus
* Backpropagation
* Curse of Dimensionality
* [Parzen Window](https://de.wikipedia.org/wiki/Kerndichtesch%C3%A4tzer)
* Features: Nominal, Ordinal, Intervallskaliert, Verhältnisskaliert

<dl>
  <dt><a href="https://en.wikipedia.org/wiki/Bayes%27_rule"><dfn>Bayes-Rule</dfn></a></dt>
  <dd>Given events \(A_1\), \(A_2\) and \(B\), Bayes' rule states that the conditional odds of \(A_1:A_2\) given \(B\) are equal to the marginal odds of \(A_1:A_2\) multiplied by the Bayes factor or likelihood ratio \(\Lambda\):

\[O(A_1:A_2|B) = \Lambda(A_1:A_2|B) \cdot O(A_1:A_2) ,\]

where

\[\Lambda(A_1:A_2|B) = \frac{P(B|A_1)}{P(B|A_2)}.\]</dd>
  <dt><dfn>Parametrischer Klassifizierer</dfn></dt>
  <dd>Ein Klassifizierer heißt <i>parametrisch</i>, wenn er eine Wahrscheinlichkeitsverteilungsannahme macht.</dd>
  <dt><dfn>Naiver Bayes-Klassifikator</dfn></dt>
  <dd>Ein Klassifizierer heißt naiver Bayes-Klassifikator, wenn er den
      Satz von Bayes unter der naiven Annahme der Unabhängigkeit der Features
      benutzt.</dd>
  <dt><dfn>Normalverteilung</dfn></dt>
  <dd>Eine stetige Zufallsvariable \(X\) mit der Wahrscheinlichkeitsdichte
      \(f\colon\mathbb{R}\to\mathbb{R}\), gegeben durch<br/>
      \(f(x) = \frac {1}{\sigma\sqrt{2\pi}} e^{-\frac {1}{2} \left(\frac{x-\mu}{\sigma}\right)^2}\)<br/>
      heißt \(\mathcal N\left(\mu, \sigma^2\right)\)-verteilt, normalverteilt
      mit den Erwartungswert \(\mu\) und Varianz \(\sigma^2\).</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Mehrdimensionale_Normalverteilung"><dfn>Multivariate Normalverteilung</dfn></a></dt>
  <dd>Eine \(p\)-dimensionale reelle Zufallsvariable \(X\) ist normalverteilt
      mit Erwartungswertvektor \(\mu\) und  (positiv definiter) Kovarianzmatrix
      \(\Sigma\), wenn sie eine Dichtefunktion der Form
      \[f_X(x)=\frac{1}{ \sqrt{(2\pi)^p \det(\Sigma)} } \exp \left( -\frac{1}{2}(x-\mu)^{T}\Sigma^{-1}(x-\mu) \right)\]
besitzt. Man schreibt
\[X\sim \mathcal N_p(\mu, \Sigma).\]</dd>
  <dt><dfn>Gauß'scher Klassifizierer</dfn></dt>
  <dd>Ein (naiver) Bayes-Klassifikator, welcher von normalverteilten Daten
      ausgeht heißt <i>Gauß'scher Klassifizierer</i>.</dd>
  <dt><a href="https://en.wikipedia.org/wiki/Principal_component_analysis"><dfn>Principal Component Analysis</dfn></a> (<dfn>PCA</dfn>, <dfn>Hauptkomponentenanalyse</dfn>)</dt>
  <dd>Die Hauptkomponentenanalyse ist ein Verfahren zur
      Dimensionalitätsreduktion von ungelabelten Daten im \(\mathbb{R}^n\).
      Sie projeziert die Daten auf diejenige Hyperebene im
      \(\mathbb{R}^d\), die den durch die Projektion stattfindenden
      Datenverlust minimal hält.
      Dabei ist \(d \in 1, \dots, n\) beliebig wählbar.

      Die Transformation der Daten \(X\) findet durch eine Matrixmultiplikation
      \(Y = P \cdot X\) statt. Die Matrix \(P\) besteht aus den ersten \(d\)
      Eigenvektoren der Kovarianzmatrix der Features \(X\):

      \(P = (v_1, \dots, v_d)\) mit
      \(\lambda_j v_j = C_X v_j\) für \(j=1,\dots,d\)

      Außerdem gilt: \(C_X = \frac{1}{n-1} X X^T\) </dd>
</dl>

### V03: LVQ

Slide name: `V03_2015-04-21_LVQ.pdf`

* k-Means
* Fuzzy k-Means
* Vector Quantization (VQ) is an unsupervised clustering algorithm
* Learning Vector Quantization is supervised.


### V04: Perceptron

Slide name: `V04_2015-04-28_Perceptron.pdf`

<dl>
  <dt><dfn>McCulloch–Pitts (MCP) Neuron</dfn></dt>
  <dd>Ein MLP-Neuron is ein Algorithmus zur binären Klassifizierung. Er hat
      \(m+1\), mit \(m \in \mathbb{N}_{> 0}\) inputs \(x_i \in \{0, 1\}\). Davon
      ist der erste (nullte) Konstant gleich Eins und wird <i>Bias</i> genannt.
      Jeder Input wird mit eingem Gewicht \(w_i \in \mathbb{R}\) multipliziert,
      alle gewichteten Inputs werden addiert und schließlich wird die
      Stufenfunktion
      \(\varphi(x) = \begin{cases}1 &\text{falls } x > 0\\0 &\text{sonst} \end{cases}\)
      angewendet.
  </dd>
  <dt><dfn>Rosenblatt-Perzeptron</dfn></dt>
  <dd>Wie das McCulloch–Pitts (MCP) Neuron, nur ist \(x_i \in \mathbb{R}\) und
      ein Lernalgorithmus ist gegeben. Dieser addiert den
      \(\lambda \in (0, 1)\) gewichteten, fehlklassifizierten Vektor auf die
      Gewichte \(w_i\). \(\lambda\) heißt die <i>Lernrate</i>.
  </dd>
  <dt><dfn>Pocket Perceptron Algorithm</dfn></dt>
  <dd>Ein Lernalgorithmus für ein Rosenblatt-Perzeptron. Dieser konvergiert zu
      Gewichten, welche die wenigsten Beispiele falsch klassifiziert.
  </dd>
  <dt><dfn>Sigmoid-Funktion</dfn></dt>
  <dd>\(\varphi(x) = \frac{1}{1+e^{-x}}\)</dd>
  <dt><dfn>Softmax-Funktion</dfn></dt>
  <dd>\(\varphi(a_i) = \frac{e^{a_i}}{\sum_{k} e^{a_k}}\) wobei \(a_i\) die
      Aktivierung des \(i\)-ten Neurons der selben Schicht ist.</dd>
  <dt><dfn>Perzeptron</dfn> / <dfn>Logistic Neuron</dfn></dt>
  <dd><abbr title="Mean Squared Error">MSE</abbr> + Sigmoid activation function</dd>
</dl>

Fakten:

* Das Rosenblatt-Perzeptron findet eine lineare Trenngrenze, wenn sie
  existiert.
* Probleme vom Rosenblatt-Perzeptron:
  * XOR
  * Nicht-linear trennbare Daten
  * Nicht-trennbare Daten
  * Wahl der Lernrate und der Startgewichte
* Aufbau eines biologischen Neurons (Axon, Dendriten, Zellkörper, Ranviersche
  Schnürringe, Synapsen)
* Glia-Zellen

Fragen:

* Folie 6: Ist der Input nicht in [0, 1]?

### V05: Features

Slide name: `V05_2015-04-29_Features.pdf`

<dl>
  <dt><dfn>Rectified Linear Unit</dfn> (<dfn>ReLU</dfn>)</dt>
  <dd>\(\varphi(x) = \max(0, x)\)</dd>
  <dt><dfn>Softplus</dfn></dt>
  <dd>\(\varphi(x) = \log(1 + e^x)\)</dd>
  <dt><dfn>Feed Forward Neural Network</dfn></dt>
  <dd>A Feed Forward Neural Network is a learning algorithm which takes
      a fixed-size input feature vector, applies varous matrix multiplications
      and point-wise non-linear functions to obtain a fixed-size output
      vector.</dd>
  <dt><dfn>Multilayer Perceptron</dfn></dt>
  <dd>A Multilayer Perceptron is a special type of Feed Forward Neural Network.
      It consists of fully connected layers only.</dd>
  <dt><a href="https://de.wikipedia.org/wiki/Metrischer_Raum#Formale_Definition"><dfn>Metrik</dfn></a></dt>
  <dd>Sei \(X\) eine Menge und \(d:X \times X \rightarrow \mathbb{R}\) eine
      Abbildung. \(d\) heißt Metrik auf \(X\), wenn gilt:
      <ul>
          <li>\(d(x, y) = 0 \geq x=y \;\;\; \forall x, y \in X\)</li>
          <li>\(d(x,y)=d(y,x=\)</li>
          <li>\(d(x,y) \leq d(x,z) + d(z,y)\)</li>
      </ul>
  </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Jaccard-Koeffizient#Jaccard-Metrik"><dfn>Jaccard-Metrik</dfn></a></dt>
  <dd>Es seien \(A, B\) Mengen und \(J(A, B) := \frac{|A \cup B| - |A \cap B|}{|A \cup B|}\).
      Dann heißt \(J\) die Jaccard-Metrik.
  </dd>
  <dt><a href="https://de.wikipedia.org/wiki/Levenshtein-Distanz"><dfn>Levenshtein-Distanz</dfn></a></dt>
  <dd>Es seien \(a, b\) Zeichenketten, \(|a|\) die Länge der Zeichenkette \(a\)
      und \(\delta_{a_i \neq b_j}\) genau dann 1, wenn das \(i\)-te Zeichen von
      \(a\) und das \(j\)-te Zeichen von \(b\) sich unterscheiden.

      Dann heißt \(d_L(a, b)\) die Levenshtein-Distanz:
      \[d_L(a,b) := lev_{a,b}(|a|, |b|)\]
      \[\text{lev}_{a,b}(i, j) = \begin{cases}\max(i,j) &\text{falls} \min(i,j) = 0,\\
        \min \begin{cases}\text{lev}_{a,b}(i-1,j)+1\\
                          \text{lev}_{a,b}(i,j-1)+1\\
                          \text{lev}_{a,b}(i-1,j-1)+\delta_{(a_i \neq b_j)}\\\end{cases} &\text{sonst}\end{cases}\]
  </dd>
</dl>

Fragen:

* Welche Feed Forward Neuronalen Netze existieren, die keine Multilayer
  Perceptronen sind?
* Welche Skalentypen gibt es für Merkmale (Features)?
    * Nominale Merkmale: Nur Gleichheit kann überprüft werden
    * Ordinale Merkmale: Es existiert eine "kleiner gleich"-Relation
    * Intervallskalierte Merkmale:
        * Die Differenz der Merkmale hat eine Semantik
        * Es existiert jedoch kein "wirklicher" Nullpunkt
    * Verhältnisskalierte Merkmale: Wie Intervallskaliert, aber mit absolutem
      Nullpunkt.

### V06: Backpropagation

Slide name: `V06_2015-05-05_Backpropagation.pdf`

<dl>
    <dt><a href="https://de.wikipedia.org/wiki/Kreuzentropie"><dfn>Kreuzentropie Fehlerfunktion</dfn></a>
        (<dfn>Cross-Entropy</dfn>)</dt>
    <dd>\[E_{-x} = - \sum_{k}[t_k^x \log(o_k^x) + (1-t_k^x) \log (1- o_k^x)]\]
        wobei \(x\) der Feature-Vektor ist, \(k\) ein Neuron des letzen
        Layers, \(t\) der wahre Wert (d.h. der gewünschte Output),
        \(o\) der tatsächliche Output ist.</dd>
</dl>

* Stochastic Gradient Descent
* Batch Gradient Descent


### V07: Feature Learning

Slide name: `V07_12-05-2015_Feature_Learning.pdf`

<dl>
    <dt><a href="https://en.wikipedia.org/wiki/Autoencoder"><dfn>Autoencoder</dfn></a></dt>
    <dd>Ein Autoencoder ist ein neuronales Netz, welches darauf trainiert wird
        die Input-Daten am Output wieder zu replizieren.</dd>
    <dt><dfn>Bottleneck Features</dfn></dt>
    <dd>Unter Bottleneck-Features versteht man eine Schicht in einem
        neuronalem Netz, welche wesentlich kleiner ist als die vorhergehende
        und nachfolgende Schicht.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence"><dfn>Kullback-Leibler-Divergenz</dfn></a></dt>
    <dd>Die Kullback-Leibler-Divergenz ist ein Maß für die Unterschiedlichkeit
        zweier Wahrscheinlichkeitsverteilungen \(P, Q\). Für
        diskrete Verteilungen ist sie definiert als:
        \[KL(P||Q) := \sum_{x \in X} P(x) \cdot \log \frac{P(x)}{Q(x)}\]</dd>
    <dt><dfn>Denoising Autoencoder</dfn></dt>
    <dd>Ein Autoencoder, welcher trainiert wird rauschen zu entfernen.</dd>
</dl>

Fakten:

* Eine lineare Aktivierungsfunktion wird in einer Repräsentation im
  Bottleneck-Feature resultieren, die PCA ähnelt.
* Fehlerfunktion:
  * <abbr title="Cross Entropy">CE</abbr> bei binären Ausgaben (d.h. Input-Features)
  * <abbr title="Mean squared error">MSE</abbr> bei reelen Ausgaben (d.h. Input-Features)

Fragen:

* Wie muss man die Grafik zu Stacked Denoising Autoencodern verstehen?


### V08: Deep Learning

Slide name: `V08_2015-05-13_Deep_Learning.pdf`

<dl>
    <dt><dfn>Deep Neural Networks</dfn></dt>
    <dd>Neural Networks with at least two hidden layers with nonlinear
        activation functions.</dd>
    <dt><dfn>Hyperparameter</dfn></dt>
    <dd>Hyperparameter \(\theta\) eines neuronalen Netzes sind Parameter,
        welche nicht gelernt werden.</dd>
    <dt><dfn>Learnin Rate Scheduling</dfn></dt>
    <dd>Start with a learning rate \(\eta\) and reduce it while training</dd>
    <dt><dfn>Exponential Decay Learning Rate</dfn></dt>
    <dd>\(\eta_t = \eta_{t-1} \cdot \alpha = \eta_0 \cdot \alpha^t\) mit \(\alpha \in (0, 1)\)</dd>
    <dt><dfn>Performance Scheduling</dfn></dt>
    <dd>Measure the error on the cross validation set and decrease the learning
        rate when the algorithm stops improving.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Rprop"><dfn>RProp</dfn></a></dt>
    <dd>RProp is a learning rate scheduling method which is only based on the
        sign of the gradient. It increases the learning rate when the sign of
        the gradient doesn't change and increases it when the sign of the
        gradient changes.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad"><dfn><abbr title="adaptive gradient">AdaGrad</abbr></dfn></a></dt>
    <dd>\[\eta_{tij} = \frac{\eta_0}{\sqrt{1 + \sum_k {(\frac{\partial E^{t-k}}{\partial w_{ij}})}^2}}\]</dd>
    <dt><dfn>Newbob Scheduling</dfn></dt>
    <dd>Newbob scheduling is a combination of Exponential decay learning rate
        scheduling and performance scheduling. It starts with a learning rate
        \(\eta_0\). When the validation error stops decreasing, switch to
        exponentially decaying learning rate. Terminate when the validation
        error stops decreasing again.</dd>
    <dt><dfn>Cross Entropy Error function</dfn> (CE)</dt>
    <dd>\[E_{CE}(w) = - \sum_{x \in X} \sum_{k} [t_k^x \log(o_k^x + (1-t_k^x) \log(1-o_k^x))]\]
        where \(w\) is the weight vector, \(X\) is the set of training
        examples (feature vectors),
        \(t_k^x = \begin{cases}1 &\text{if } x \text{ is of class }k\\0&\text{otherwise}\end{cases}\)
        and \(o_k^x\) is the output at neuron \(k\) of the network for the
        feature vector \(x\).</dd>
    <dt><dfn>Mean Squared Error function</dfn> (MSE)</dt>
    <dd>\[E_{MSE}(w) = \frac{1}{2}\sum_{x \in X} \sum_{k} (t_k^x - o_k^x)^2\]
        where \(w\) is the weight vector, \(X\) is the set of training
        examples (feature vectors), \(t_k^x = \begin{cases}1 &\text{if } x \text{ is of class }k\\0&\text{otherwise}\end{cases}\) and \(o_k^x\) is the output
        at neuron \(k\) of the network for the feature vector \(x\).</dd>
</dl>

{% caption align="aligncenter" width="500" alt="RProp by Ryan Harris" text="RProp by Ryan Harris (<a href='https://www.youtube.com/watch?v=Cy2g9_hR-5Y'>source</a>). Rot ist der Gradientenabstieg, blau ist mit momentum, rosa ist RProp" url="../images/2016/02/visualizing-opt-algorithms-rprop-gradient-descent-momentum.png" %}

* Pretraining
* <abbr title="Time Delay Neural Networks">TDNNs</abbr>, <abbr title="Convolutional Neural Networks">CNNs</abbr>
* Design choices (hyperparameters):
    * Topology (Width of layers, number of layers)
    * Activation functions
    * Error function
    * Mini-Batch size
    * Training function
    * Preprocessing
    * Initial Weights
* MSE vs <abbr title="Cross Entropy">CE</abbr>:
    * MSE penetalizes large differences much more than small ones
    * MSE works well for function approximation
    * CE works well on classification tasks


Fragen:

* AdaGrad (Folie 34)
* Optimal drain damage (Folie 36)


### V09: Reinforcement Learning

Slide name: `V09_2015-05-26-Reinforcement-Learning.pdf`

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
    <dt><dfn>Diskontierungsfaktor</dfn></dt>
    <dd>Ein Diskontierungsfaktor
        <span markdown="0">\(\gamma \in [0, 1]\)</span> encodiert
        den Bedeutungsverlust zwischen einer direkten Belohnung und
        einer späteren Belohnung. Es sollte
        <span markdown="0">\(\gamma &lt; 1\)</span> gelten um
        unendliche Belohnungen zu vermeiden.</dd>
    <dt><dfn>Strategie</dfn> (engl. <dfn>Policy</dfn>)</dt>
    <dd>Eine Strategie \(\pi:S \rightarrow A\) sagt einem Agenten welche
        Aktion er in welchem Zustand ausführen soll.</dd>
    <dt><dfn>Q-Funktion</dfn> (Action-Value function)</dt>
    <dd>Die Q-Funktion \(Q^\pi: S \times A \rightarrow \mathbb{R}\) weißt jeder
        Aktion in jedem Zustand einen Wert zu unter der Annahme, dass
        die Strategie \(\pi\) genutzt wird.</dd>
    <dt><dfn>V-Funktion</dfn> (State-Value function)</dt>
    <dd>Die V-Funktion \(V^\pi: S \rightarrow \mathbb{R}\) weißt jeder
        jedem Zustand die Erwartete Belohnung zu unter der Annahme, dass
        die Strategie \(\pi\) genutzt wird.</dd>
    <dt><dfn>\(\varepsilon\)-Greedy Strategy</dfn></dt>
    <dd>Explore \(\varepsilon\)% of the time. Otherwise, follow what you
        currently believe is best.</dd>
    <dt><dfn>\(\varepsilon\)-decreasing Strategy</dfn></dt>
    <dd>Explore \(\varepsilon\)% of the time. Otherwise, follow what you
        currently believe is best. Reduce \(\varepsilon\) over time.</dd>
    <dt><dfn>\(\varepsilon\)-first Strategy</dfn></dt>
    <dd>Explore for \(\varepsilon\) steps and then do what you think is best.</dd>
    <dt><dfn>Adaptive \(\varepsilon\)-greedy Strategy</dfn></dt>
    <dd>Explore \(\varepsilon\)% of the time. Otherwise, follow what you
        currently believe is best. Reduce \(\varepsilon\) based on what you
        learn.</dd>
    <dt><dfn>Episode</dfn></dt>
    <dd>A run through an <abbr title="Markov Decision Process">MDP</abbr> from
        a start state to an end state.</dd>
    <dt><dfn>Monte Carlo Policy Evaluation</dfn></dt>
    <dd>Initialize state values \(V^\pi\) and iterate:
        <ol>
            <li>Generate an episode</li>
            <li>foreach state \(s\) in episode:
            <ol>
                <li>Get the reward \(\hat{R}\) from that state on</li>
                <li>\(\hat{R} = \sum_{j=0}^\infty \gamma^j r_j\)</li>
                <li>\(V_{k+1}^\pi (s) \leftarrow V_k^pi (s) (1-\alpha)+\alpha \hat{R}\)</li>
            </ol>
            </li>
        </ol>
        where \(\alpha\) is the learning rate.
    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Temporal_Difference_Learning"><dfn>Temporal Difference Learning</dfn></a></dt>
    <dd>TODO?</dd>
</dl>

Konvention:

* Eine optimale Strategie wird mit <span markdown="0">\(\pi^*\)</span> bezeichnet.


Fragen:

* Was bedeutet es, wenn in einem MDP der Diskontierungsfaktor
  <span markdown="0">\(\gamma = 0\)</span>
  ist? → Nur der aktuelle Reward ist wichtig. Effektiv nimmt der Agent immer
  das nächste Feld, welche den höchsten Reward bietet (bzw. die Aktion, die
  den größten 1-Aktion Erwartungswert liefert).
* Was bedeutet es, wenn in einem MDP der Diskontierungsfaktor
  <span markdown="0">\(\gamma = 1\)</span>
  ist? → Der Agent versucht die Summe der Belohnungen insgesamt zu maximieren.

TODOs:

* What is Policy Iteration?
* SARSA - State-Action-Reward-State-Action
* Q-Learning


### V10: SOM

Slide name: `V10_2015-05-26_SOM.pdf`

<dl>
    <dt><dfn>Hebbsche Lernregel</dfn></dt>
    <dd>what fires together, wires together</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Selbstorganisierende_Karte"><dfn>Selbstorganisierende Karten</dfn></a> (<dfn>SOM</dfn>, <dfn>Kohonennetze</dfn>)</dt>
    <dd>SOMs sind eine Art von Neuronalen Netzen. Die neuronen von SOMs sind
    auf einem Gitter angeordnet. Es gibt nur zwei Schichten: Die Input-Neuronen
    und die Neuronen auf dem Gitter. Jedes Input-Neuron ist mit jedem Neuron
    auf dem Gitter verbunden.

    Training:
    <ol>
        <li><b>Initialisierung</b>: Die Gewichte
            <span markdown="0">\(w_{ji}\)</span> von dem
            <span markdown="0">\(i\)</span>-ten Input-Neuron zum Neuron (<span markdown="0">\(i = 1, ..., n\)</span>)
            <span markdown="0">\(j\)</span> auf dem Gitter werden zufällig
            initialisiert.</li>
        <li><b>Sampling</b>: Nehme ein zufälliges Beispiel
            <span markdown="0">\(x\)</span> der Trainingsdaten.</li>
        <li><b>Matching</b>: Finde das Neuron
            <span markdown="0">\(j_{\text{min}}\)</span>, für das die Gewichte
            dem Input am ähnlichsten sind:
            <div>\[j_{\text{min}} = \text{arg min}_j \sum_{i=1}^n (x_i - w_{ji})^2\]</div></li>
        <li><b>Update</b>: Passe die Gewichte des gewinnenden Neurons sowie der Nachbarschaft an.</li>
        <li><b>Repeat</b>: Und zurück zu Schritt 2.</li>
    </ol>

    Siehe auch:

    <ul>
        <li>Uwe Schneider: <a href="http://www2.htw-dresden.de/~iwe/Belege/Schneider/som.html">Self Organizing Map -- ein Demonstrationsbeispiel</a>, 2001.</li>
        <li><a href="https://codesachin.wordpress.com/2015/11/28/self-organizing-maps-with-googles-tensorflow/">Self-Organizing Maps with Google’s TensorFlow</a></li>
        <li>J. A. Bullinaria: <a href="http://www.cs.bham.ac.uk/~jxb/NN/l16.pdf">Self Organizing Maps: Fundamentals</a>, 2004.</li>
    </ul>
    </dd>
</dl>

Siehe auch:

* [Self-Organizing Maps with Google’s TensorFlow](https://codesachin.wordpress.com/2015/11/28/self-organizing-maps-with-googles-tensorflow/)
* [Kohonen's Self Organizing Feature Maps](http://www.ai-junkie.com/ann/som/som1.html) by ai-junkie

### V11: RBMs

Slide name: `V11_2015-05-27_RBMs`

<dl>
    <dt><a href="https://de.wikipedia.org/wiki/Hopfield-Netz"><dfn>Hopfield-Netz</dfn></a></dt>
    <dd>Ein Hopfield-Netz besteht nur aus einer Schicht von McCulloch-Pitts
        Neuronen. Jedes Neuron ist mit jedem anderen Neuron (also nicht sich
        selbst) und allen Inputs verbunden. Die Schicht funktioniert
        gleichzeitig als Ein- und Ausgabeschicht.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Boltzmann-Maschine"><dfn>Boltzmann-Maschine</dfn></a></dt>
    <dd>Boltzmann-Maschinen sind stochastische neuronale Netzwerke, welche
        duch belibige ungerichtete Graphen repräsentiert werden können. Die
        neuronen sind binär; sie feuern also entweder oder nicht. Es gibt
        insbesondere keine Unterschiede in der Stärke mit der sie feuern.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine"><dfn>Restricted Boltzmann machine</dfn></a> (<dfn>RBM</dfn>)</dt>
    <dd>Im Gegensatz zur Boltzmann-Maschine muss die Restricted
        Boltzmann-Machine (RBM) aus einem bipartitem Graph bestehen. Dies
        erlaubt ein effizienteres Trainingsverfahren.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Simulated_annealing"><dfn>Simulated annealing</dfn></a></dt>
    <dd>Simulated annealing ist ein heuristisches Optimierungsverfahren.

        Sei \(D\) ein Wertebereich einer Funktion \(f: D \rightarrow \mathbb{R}\)
        und \(U: D \rightarrow \mathcal{P}(D)\) eine Funktion, welche die
        Umgebung eines Punktes angibt. Sei \(T: \mathbb{N}_0 \rightarrow \mathbb{R}_{> 0}\)
        die Temperatur zum Zeitpunkt \(t \in \mathbb{N}_0\).

        Gesucht ist \(\text{arg min}_{x \in D} f(x)\).

        Wähle zum Zeitpunkt \(t=0\) einen zufälligen Startwert \(x \in D\).

        Gehe nun iterativ vor und jeweils einen Zeitschritt weiter:

        Nehme einen Punkt aus der Umgebung \(y \in U(x)\). Wenn
        \(f(y) \leq f(x)\), dann überschreibe \(x \leftarrow y\). Falls nicht,
        dann überschreibe es mit der Wahrscheinlichkeit \(\exp \left (-\frac{f(y)-f(x)}{T(t)} \right )\).

        Speichere in jedem Schritt den bisher besten Wert.
        </dd>
</dl>

Anwendungen:

* RBMs:
    * Collaborative Filtering: User-rating prediction for movie database. The
      problem is that not every user has rated all movies.

Fragen:

* Hopfield-Netze:
    * Wie trainiert man sie?
    * Wo werden / wurden sie benutzt?

Siehe auch:

* Deeplearning.net: [Restricted Boltzmann Machines (RBM)](http://deeplearning.net/tutorial/rbm.html)
* A. Barra, A. Bernacchia, E. Santucci und P. Contucci: [On the equivalence of Hopfield networks and Boltzmann Machines](http://www.sciencedirect.com/science/article/pii/S0893608012001608)in *Neural Networks*, 2012.


### V12: RNNs
Slide name: `V12_2015-06-02_RNNs.pdf`

<dl>
    <dt><a href="https://de.wikipedia.org/wiki/Elman-Netz"><dfn>Elman-Netz</dfn></a></dt>
    <dd>Ein rekurrentes neuronales Netzwerk, bei dem die Ausgabe eines
        hidden layers im nächsten Zeitschritt als Eingabe verwendet wird.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Jordan-Netz"><dfn>Jordan-Netz</dfn></a></dt>
    <dd>Ein rekurrentes neuronales Netzwerk, bei dem die Ausgabe der
        Ausgabeschicht im nächsten Zeitschritt als Eingabe verwendet wird.</dd>
    <dt><dfn>Backpropagation through Time</dfn> (<dfn>BPTT</dfn>)</dt>
    <dd>Ein Trainingsalgorithmus für rekurrente neuronale Netze, bei dem
        das Netz "ausgerollt" wird. Das rekurrente Netz wird also als unendlich
        großes nicht-rekurrentes Netz behandelt.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Vanishing_gradient_problem"><dfn>Vanishing gradient problem</dfn></a></dt>
    <dd>Das Problem des verschwindenden Gradienten ist eine Herausforderung im
        Kontext neuronaler Netze, welche mit Backpropagation trainiert
        werden. Insbesondere bei sehr tiefen oder rekurrenten Netzen
        kann es passieren, dass der Gradient bei den ersten Schichten sehr
        niedrig ist, sodass das Netz sehr langsam lernt. Aufgrund numerischer
        Ungenauigkeit kann dies sogar dazu führen, dass das Netz in den
        ersten Schichten nicht lernen kann.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Long_short-term_memory"><dfn>Long short-term memory</dfn></a> (vgl. <dfn>LSTM</dfn>)</dt>
    <dd>Ein LSTM ist ein Typ eines neuronalen Netzwerks. Das besondere an
        LSTM Netzen sind "intelligente" Neuronen, welche über Gates bestimmen
        ob ein Wert gespeichert wird und wie lange.</dd>
</dl>


Siehe auch:

* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [Char-Predictor online Demo](http://www.cs.toronto.edu/~ilya/fourth.cgi?prefix=E%3D&numChars=300)
* [Recurrent Neural Networks Tutorial, Part 1 – Introduction to RNNs](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)
* YouTube: [Vanishing Gradient](https://www.youtube.com/watch?v=SKMpmAOUa2Q) (5:24 min)
* [Where does the name 'LSTM' come from?](http://datascience.stackexchange.com/q/9510/8820)


### V13: NN learning tricks
Slide name: `V13_2015-06-09_NNlearning-tricks.pdf`

<dl>
    <dt><dfn>Momentum</dfn></dt>
    <dd>In der Update-Regel \(\Delta w_{ij}^* (t+1) = \Delta w_{ij} (t+1) + \alpha \Delta w_{ij}(t)\) wird der Term \(\Delta w_{ij}(t)\) als <i>Momentum</i> bezeichnet.
        Der Skalar \(\alpha \in [0, 1]\) gewichtet diesen und ist ein
        Hyperparameter.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Quickprop"><dfn>Quickprop</dfn></a></dt>
    <dd>Quickprop ist ein Trainingsverfahren für neuronale Netze. TODO: Wie funktioniert es?</dd>
    <dt><dfn>Weight Decay</dfn></dt>
    <dd>Passe die Fehlerfunktion an: \(E = MSE + \lambda \sum_{i,j} w_{ij}^2\)</dd>
    <dt><dfn>Weight Elimination</dfn></dt>
    <dd>Passe die Fehlerfunktion an: \(E = MSE + \lambda \sum_{i,j} \frac{w_{ij}^2}{1+w_{ij}^2}\)</dd>
    <dt><dfn>Optimal Brain Damage</dfn></dt>
    <dd>Optimal Brain Damage entfernt nach dem Training Verbindungen die
        sehr kleine \(|w_{ij}|\) haben.

        Besser: Entferne Verbindungen, die geringen Einfluss auf die
        Fehlerfunktion haben.</dd>
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
    <dt><dfn>Meiosis Netzwerke</dfn> (siehe Stephen Jose Hanson: [Meiosis Networks ](http://papers.nips.cc/paper/227-meiosis-networks.pdf))</dt>
    <dd>Meiosis Netzwerke bauen ein neuronales Netz auf. Sie beginnen mit einer
        einzelnen hidden Unit. Diese hidden Unit wird aufgespalten, wenn die
        "unsicherheit" zu groß ist. (TODO)</dd>
</dl>

Speed-ups des Trainings sind möglich durch:

* Momentum
* Überspringen von bereits gut gelernten Beispielen
* Dynamische Anpassung der Lernrate `$\eta$`
* Quickprop
* Gute Initialisierung

Lernen kann getweakt werden:

* Fehlerfunktion anpassen
    * <abbr title="Mean Squared Error">MSE</abbr>
    * Cross-Entropy
    * <abbr title="Classification Figure of Merit">CFM</abbr>
* Overfitting verhindern
    * Weight decay
    * Weight elimination
    * Optimal Brain Damage
    * Optimal Brain Surgeon
* Schrittweise Netzkonstruktion
    * Cascade Correlation
    * Meiosis Netzwerke
    * <abbr title="Automativ Structure Optimalization">ASO</abbr>: TODO - wie
      funktioniert das?

Fragen:

* Folie 19: Was passiert hier? (TODO)


### V14: DNN CV
Slide name: `V14_2015-06-10_DNN_CV .pdf`

<dl>
    <dt><a href="https://en.wikipedia.org/wiki/Scale-invariant_feature_transform"><dfn>SIFT</dfn></a> (<dfn>Scale-invariant feature transform</dfn>)</dt>
    <dd>Unter SIFT versteht man bestimmte Features in der Bildverarbeitung,
        welche invariant unter skalierung sind.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Texton"><dfn>Texton</dfn></a> (siehe <a href="http://vcla.stat.ucla.edu/old/Chengen_Research/texton.htm">UCLA</a>)</dt>
    <dd>Unter einem Texton versteht man grundlegende, kleine Features eines
        Bildes. Diese Bilden die kleinsten als unterschiedlich wahrnehmbaren
        Einheiten.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Convolutional_neural_network"><dfn>Convolutional Neural Network</dfn></a> (<dfn>CNN</dfn>)</dt>
    <dd>Ein CNN ist ein Neuronales Netzwerk, welches mindestens eine Schicht
        hat, welche die Parameter eines Kernels für eine Faltung lernt.</dd>
    <dt><dfn>Feature Map</dfn></dt>
    <dd>Im Kontext von CNNs versteht man unter einer Feature-Map die Ausgabe
        eines Kernels in einem Convolutional Layer.</dd>
</dl>

Facts:

* Pooling: Max, Mean, Probabilistic


### V15: Speech-Independence

Slide name: `V15_2015-06-17_Speech-Independence.pdf`


## Visualisierung von Netzen

Häufig wird die Architektur neuronaler Netze grafisch dargestellt. Dabei ist
mir folgendes aufgefallen:

* Im Innenren von Neuronen wird die Aktivierungsfunktion "geplottet". Das heißt
  bei der Sigmoidfunktion wird etwas S-Förmiges dargestellt, bei der
  sign-Funktion etwas eckiges, bei ReLU ein horizontaler Strich gefolgt von
  einem Strich im 45-Grad Winkel ... (TODO: Beispiele aufzeichnen)
* Typischerweise ist der Input links (oder alternativ unten) und der Output
  rechts (oder alternativ oben)


## Einordnung

Neuronale netze kann man durch folgende Kriterien mit einander vergleichen:

* **Deterministisch / Stochastisch**: Ist die Aktivierung der neuronen
  stochastische oder deterministisch?
* **Auswertung**: Feed-Forward oder Rekurrent?
* **Training**: Wie lernt man?
* **Verwendung**: Wo wird das Netzwerk typischerweise eingesetzt?

<table class="table">
  <thead>
    <tr>
        <th>Netzwerk</th>
        <th>Determinitisch</th>
        <th>Auswertung</th>
        <th>Training</th>
        <th>Verwendung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <th>McCullch-Pitts Neuron</th>
        <td>Yes</td>
        <td>Feed-Forward</td>
        <td>Supervised</td>
        <td>Classification of linear separable data</td>
    </tr>
    <tr>
        <th>Rosenblatt Perceptron</th>
        <td>Yes</td>
        <td>Feed-Forward</td>
        <td>Supervised</td>
        <td>Classification of linear separable data</td>
    </tr>
    <tr>
        <th>Multilayer Perceptron</th>
        <td>Yes</td>
        <td>Feed-Forward</td>
        <td>Supervised (Backkpropagation)</td>
        <td>Classification</td>
    </tr>
    <tr>
        <th>CNN</th>
        <td>Yes</td>
        <td>Feed-Forward</td>
        <td>Supervised (Backkpropagation + weight sharing)</td>
        <td>Computer Vision</td>
    </tr>
    <tr>
        <th><abbr title="Time Delay Neural Networks">TDNNs</abbr></th>
        <td>Yes</td>
        <td>Feed-Forward</td>
        <td>Supervised (Backkpropagation + weight sharing)</td>
        <td><abbr title="Automatic Speech Recognition">ASR</abbr></td>
    </tr>
    <tr>
        <th>LSTM</th>
        <td>Yes</td>
        <td>Recurrent</td>
        <td>BPTT</td>
        <td>Mapping sequences (Generating texts, machine translation)</td>
    </tr>
    <tr>
        <th>SOM</th>
        <td>Yes</td>
        <td>Feed-Forward</td>
        <td>Unsupervised (competitive learning)</td>
        <td>Mapping of high-dimensional data on 2D</td>
    </tr>
    <tr>
        <th>Hopfield networks</th>
        <td>Yes</td>
        <td>Recurrent</td>
        <td>Hebbsche Lernregel</td>
        <td>TODO</td>
    </tr>
    <tr>
        <th>Helmholtz machines</th>
        <td>stochastic</td>
        <td>TODO</td>
        <td>wake-sleep algorithm</td>
        <td>TODO</td>
    </tr>
    <tr>
        <th>Boltzman machines</th>
        <td>stochastic</td>
        <td>TODO</td>
        <td>TODO</td>
        <td>TODO</td>
    </tr>
    <tr>
        <th>RBMs</th>
        <td>stochastic</td>
        <td>TODO</td>
        <td>Contrastive Divergence&nbsp;(CD-k)</td>
        <td>TODO</td>
    </tr>
  </tbody>
</table>


## Deutsch ↔ Englisch

Da Englisch und Deutsch in der Informatik immer wieder wild gemischt wird,
habe ich hier mal eine kleine Liste mit Übersetzungen begonnen:

* Gitter: Lattice
* Gradientenabstieg: Gradient descent
* Mittlerer quadratischer Fehler: Mean Squared Error (MSE)


## Prüfungsfragen

<ul>
    <li>Was ist der Unterschied zwischen Backpropagation und Gradient descent?<br/>
        → Backpropagation ist eine geschickte Umsetzung des Gradientenabstiegs,
           bei der es vermieden wird Berechnungen mehrfach durchzuführen.</li>
    <li>Welche Typen von Neuronalen Netzen gibt es?<br/>
        → Hopfield-Netze,
           <abbr title="Restricted Boltzmann Machines">RBMs</abbr>,
           Feed-Forward Netze,
           Perceptrons (McCullch-Pitts, Rosenblatt,
           <abbr title="Multilayer Peceptrons">MLPs</abbr>),
           <abbr title="Convolutional Neural Networks">CNNs</abbr>,
           rekurrente Netze (LSTM),
           <abbr title="Self-Organizing Maps">SOMs</abbr>,
           <abbr title="Time Delay Neural Networks">TDNNs</abbr></li>
</ul>


## Material und Links

* [Vorlesungswebsite](http://ies.anthropomatik.kit.edu/lehre_mustererkennung.php)
* [NNPraktikum](https://github.com/thanhleha/NNPraktikum): Toolkit für die Übungsblätter
* StackExchange
  * ✓ [What is the difference in Bayesian estimate and maximum likelihood estimate?](http://stats.stackexchange.com/q/74082/25741)
  * ✓ [Can k-means clustering get shells as clusters?](http://datascience.stackexchange.com/q/9172/8820)
  * [How is the Schwarz Criterion defined?](http://datascience.stackexchange.com/q/9177/8820)
  * [Are there studies which examine dropout vs other regularizations?](http://datascience.stackexchange.com/q/9195/8820)
  * [How do subsequent convolution layers work?](http://datascience.stackexchange.com/q/9175/8820)
  * ✓ [Is Maxout the same as max pooling?](http://datascience.stackexchange.com/q/9212/8820)
  * [What is \\(\alpha \sin(\theta) + \beta \frac{d \theta}{d t}\\) in the inverted pole problem?](http://robotics.stackexchange.com/q/8617/11257)
  * ✓ [(Why) do activation functions have to be monotonic?](http://datascience.stackexchange.com/q/9233/8820)
  * [The cross-entropy error function in neural networks](http://datascience.stackexchange.com/q/9302/8820)
* [Visualizing Optimization Algos](http://imgur.com/a/Hqolp)
* [Neural Network demo](http://phiresky.github.io/kogsys-demos/neural-network/)
* [Skript von Marvin Ritter](https://github.com/Marvin182/NeuralNets)
* [Machine Learning 1](//martin-thoma.com/machine-learning-1-course/) und [Machine Learning 2](//martin-thoma.com/machine-learning-2-course/) am KIT
* Coursera: [Neural Networks for Machine Learning](https://class.coursera.org/neuralnets-2012-001/lecture) by Geoffrey Hinton


## Übungsbetrieb

Übungsblätter sind freiwillig.


## Termine und Klausurablauf

**Datum**: nach Terminvereinbarung<br/>
**Ort**: <a href="http://www.kithub.de/map/2210">Gebäude 50.20</a><br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Erlaubte Hilfsmittel**: keine
