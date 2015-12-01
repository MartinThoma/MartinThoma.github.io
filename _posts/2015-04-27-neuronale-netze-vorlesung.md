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
    <td><a href="https://ies.anthropomatik.kit.edu/ies/download/lehre/me/ME-Kap1_V33.pdf">Einleitung</a></td>
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
    <td>Denoising- und Sparse Autoencoder, Bottleneck-Features<a href="https://de.wikipedia.org/wiki/Kullback-Leibler-Divergenz">Kullback-Leibler-Divergenz</a>; <a href="https://de.wikipedia.org/wiki/Kettenregel#Mathematische_Formulierung">Kettenregel</a></td>
</tr>
<tr>
    <td>13.05.2015</td>
    <td>Deep Learning</td>
    <td>Momentum, Rprop, Newbob, L1/L2-Regularisierung ($|w|$, $w^2$), weight decay</td>
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
    <td>Paralleles Lernen; Quickprop; Alternative Fehlerfunktion (cross-entropy, <abbr title="Classification Figure of Merit">CFM</abbr>);
        weight elimination / regularization</td>
</tr>
<tr>
    <td>15.07.2015</td>
    <td>Summary</td>
    <td>When to use which objective function (cross entropy, MSE); Backpropagation; Weight initialization; Regularization (L2 weight decay, dropout); Time Delay NN; Recurrent Networks; Applications (Speech Recognition, Computer Vision)</td>
</tr>
</table>

### NN01-Intro.pdf

* Human Brain vs. Computer (Processing/Processors, Accuracy, Speed, Hardware, Design)
* Aufbau eines biologischen Neurons (vgl. [Wikipedia](https://de.wikipedia.org/wiki/Nervenzelle#.C3.9Cberblick_.C3.BCber_den_Aufbau_einer_Nervenzelle))


## NN02-Classification.pdf

{% caption align="aligncenter" width="500" alt="Rosenblatt-Perceptron which realizes logical or" text="Rosenblatt-Perceptron which realizes logical or" url="../images/2015/12/perceptron-or.png" %}

* McCullch-Pitts Neuron (weights, bias, activation function is step function)
* Rosenblatt Perceptron Algorithmus
* Backpropagation
* <abbr title="Principal Component Analysis">PCA</abbr>: TODO (Folie 45)
* Curse of Dimensionality
* [Parzen Window](https://de.wikipedia.org/wiki/Kerndichtesch%C3%A4tzer)
* Features: Nominal, Ordinal, Intervallskaliert, Verhältnisskaliert

<dl>
  <dt><dfn>Bayes-Rule</dfn> (Source: <a href="https://en.wikipedia.org/wiki/Bayes%27_rule">wikipedia</a>)</dt>
  <dd>Given events \(A_1\), $A_2$ and $B$, Bayes' rule states that the conditional odds of $A_1:A_2$ given $B$ are equal to the marginal odds of $A_1:A_2$ multiplied by the Bayes factor or likelihood ratio $\Lambda$:

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
  <dt><dfn>Multivariate Normalverteilung</dfn> (vgl. <a href="https://de.wikipedia.org/wiki/Mehrdimensionale_Normalverteilung">Wikipedia</a>)</dt>
  <dd>Eine \(p\)-dimensionale reelle Zufallsvariable \(X\) ist normalverteilt
      mit Erwartungswertvektor \(\mu\) und  (positiv definiter) Kovarianzmatrix
      \(\Sigma\), wenn sie eine Dichtefunktion der Form
      \[f_X(x)=\frac{1}{ \sqrt{(2\pi)^p \det(\Sigma)} } \exp \left( -\frac{1}{2}(x-\mu)^{T}\Sigma^{-1}(x-\mu) \right)\]
besitzt. Man schreibt
\[X\sim \mathcal N_p(\mu, \Sigma).\]</dd>
  <dt><dfn>Gauß'scher Klassifizierer</dfn></dt>
  <dd>Ein (naiver) Bayes-Klassifikator, welcher von normalverteilten Daten
      ausgeht heißt <i>Gauß'scher Klassifizierer</i>.</dd>
</dl>

## Material und Links

* [Vorlesungswebsite](http://ies.anthropomatik.kit.edu/lehre_mustererkennung.php)
* [NNPraktikum](https://github.com/thanhleha/NNPraktikum): Toolkit für die Übungsblätter
* StackExchange
  * [What is the difference in Bayesian estimate and maximum likelihood estimate?](http://stats.stackexchange.com/q/74082/25741)


## Übungsbetrieb

Übungsblätter sind freiwillig.


## Termine und Klausurablauf

**Datum**: nach Terminvereinbarung<br/>
**Ort**: <a href="http://www.kithub.de/map/2210">Gebäude 50.20</a><br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Erlaubte Hilfsmittel**: keine
