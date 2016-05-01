---
layout: post
title: Klausur Analysis I und II
author: Martin Thoma
date: 2012-08-14 17:13:24.000000000 +02:00
category: German posts
tags: Klausur
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Dieser Artikel richtet sich vor allem an Studenten, die im Sommersemester 2012 bei Herrn Prof. Dr. Schmoeger am KIT die Klausur &uuml;ber Analysis schreiben werden.</div>

<h2>Vorbereitung</h2>

<h3>Analysis I</h3>
<h4>Themen</h4>
<ul>
  <li><strong>Definitionen und Beispiele</strong>: Beschr&auml;nktheit, injektiv, surjektiv, bijektiv, endlich, unendlich, abz&auml;hlbar, &uuml;berabz&auml;hlbar</li>
  <li><a href="http://de.wikipedia.org/wiki/Bernoullische_Ungleichung">Bernoullische Ungleichung</a>: Ist $x \geq -1$, so gilt: $(1+x)^n \geq 1 + nx~~~\forall n \in \mathbb{N}^+$</li>
  <li><a href="http://de.wikipedia.org/wiki/Binomischer_Lehrsatz">Binomischer Lehrsatz</a>: $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$</li>
  <li><strong>Folgen</strong>:
    <ul>
      <li><a href="../konvergenz-von-folgen/">Konvergenz</a></li>
      <li>(strenge) Monotonie</li>
      <li>Grenzwert</li>
      <li>Divergenz</li>
      <li>Konvergenzkriterien: <a href="http://de.wikipedia.org/wiki/Wurzelkriterium">Wurzelkriterium</a>, <a href="http://de.wikipedia.org/wiki/Leibniz-Kriterium">Leibniz-Kriterium</a>, <a href="http://de.wikipedia.org/wiki/Cauchykriterium">Cauchy-Kriterium</a>, <a href="http://de.wikipedia.org/wiki/Majorantenkriterium">Majorantenkriterium</a>, Minorantenkriterium, <a href="http://de.wikipedia.org/wiki/Quotientenkriterium">Quotientenkriterium</a></li>
      <li><a href="http://de.wikipedia.org/wiki/Eulersche_Zahl">Eulersche Zahl</a>: $\displaystyle e := \lim_{n \rightarrow \infty}(1+\frac{1}{n})^n = \lim_{n \rightarrow \infty} \sum_{k=0}^n \frac{1}{n!}$</li>
      <li>H&auml;ufungswert vs. H&auml;ufungspunkt: &rarr; <a href="http://de.wikipedia.org/wiki/Diskussion:H%C3%A4ufungspunkt#H.C3.A4ufungspunkt_und_H.C3.A4ufungswert">Diskussion</a>
          <ul>
            <li>Oberer- und unterer Limes</li>
          </ul>
      </li>
    </ul>
  </li>
  <li>Unendliche Reihen</li>
  <li><a href="http://de.wikipedia.org/wiki/Potenzreihe">Potenzreihe</a></li>
  <li>Stetigkeit</li>
  <li><a href="http://de.wikipedia.org/wiki/Gleichm%C3%A4%C3%9Fige_Stetigkeit">Gleichm&auml;&szlig;ige Stetigkeit</a>: Definition, Beispiele</li>
  <li>H&ouml;here Ableitungen</li>
  <li><strong>Integrale</strong>
    <ul>
      <li>Riemann-Integral</li>
      <li>Uneigentliche Integrale</li>
      <li><a href="http://de.wikipedia.org/wiki/Riemann-Stieltjes-Integral">Riemann-Stieltjes-Integral</a></li>
      <li>Partielle Integration<br/>$\int_a^b f'(x)\cdot g(x)\,\mathrm{d}x 
= [f(x)\cdot g(x)]_{a}^{b} - \int_a^b f(x)\cdot g'(x)\,\mathrm{d}x.$</li>
    </ul>
  </li>
  <li><a href="http://de.wikipedia.org/wiki/Beschr%C3%A4nkte_Variation">Funktionen beschr&auml;nkter Variation</a>
    <ul>
      <li>Totalvariation</li>
    </ul>
  </li>
  <li><a href="http://de.wikipedia.org/wiki/Zwischenwertsatz">Zwischenwertsatz</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Mittelwertsatz_der_Differentialrechnung">Mittelwertsatz</a></li>
</ul>

<h4>Aufgabenstellungen</h4>
<ul>
  <li>Wahr/Falsch-Ankreuzaufgabe</li>
  <li>Grenzwert von Folgen bestimmen</li>
  <li>Konvergenzradius von Potenzreihen bestimmen</li>
  <li>Zeige, dass eine Funktion stetig ist. Ansatz: <br>
      $f \text{ ist stetig} :\Leftrightarrow \forall \varepsilon > 0 \ \exists \delta \ \forall x, z \text{ mit } |x - z| < \delta: |f(x)- f(z)| < \varepsilon$</li>
  <li>Zeige, dass eine Funktion differenzierbar ist. Ansatz: h-Methode<br/>
      $\displaystyle \lim_{h \rightarrow 0} \frac{f(x_0+h)-f(x_0)}{h}$</li>
  <li>Funktionenfolgen auf punktweise und gleichm&auml;&szlig;ige Konvergenz untersuchen</li>
  <li>Allgemeine Eigenschaften der e-Funktion und der Winkelfunktionen</li>
  <li>Wert von Integralen bestimmen</li>
</ul>

<h3>Analysis II</h3>
<h4>Themen und Schlagworte</h4>
<ul>
  <li>Quadratische Formen</li>
  <li>Umkehrsatz</li>
  <li>Implizit definierte Funktionen</li>
  <li>Wege
    <ul>
      <li>Wegl&auml;nge: $L(\gamma) = \int \| \gamma'(t) \| dt$</li>
      <li>Wegintegral: $\int_\gamma f(x, y, z) d(x,y,z) = \int f(\gamma(t)) \cdot \gamma'(t) dt$</li>
    </ul>
  </li>
  <li>Fixpunkte, Fixpunktsatz von Banach</li>
  <li><a href="http://de.wikipedia.org/wiki/Jacobi-Matrix">Jacobi-Matrix</a></li>
  <li>Extremwerte
    <ul>
      <li>... unter Nebenbedingungen</li>
      <li>Hessematrix</li>
    </ul>
  </li>
  <li><a href="http://de.wikipedia.org/wiki/Banachscher_Fixpunktsatz">Banachscher Fixpunktsatz</a></li>
  <li>Differentialgleichungen
    <ul>
      <li>Systeme linearer Differentialgleichungen</li>
      <li>Anfangswertprobleme</li>
      <li><a href="http://de.wikipedia.org/wiki/Fundamentalsystem_(Mathematik)">Fundamentalsystem</a></li>
      <li>Variation der Konstanten</li>
      <li><a href="http://de.wikipedia.org/wiki/Satz_von_Picard-Lindel%C3%B6f">Satz von Picard-Lindel&ouml;f</a></li>
    </ul>
  </li>
</ul>

<h4>Aufgabenstellungen</h4>
<ul>
  <li>Sind gegebene Mengen offen, abgeschlossen bzw. vollst&auml;ndig?</li>
  <li>Rand einer Menge besttimmen</li>
  <li>Lokale und globale Extrema einer Funktion $f$ bestimmen. Ansatz:<br/>
      Gradient $\nabla f$ bestimmen und gleich null setzen. Die Funktionswerte, die das erf&uuml;llen, sind die kritischen Punkte. In Hessematrix einsetzen und Definitheit pr&uuml;fen.</li>
  <li>L&ouml;sung von nichtlinearen Gleichungssystem</li>
  <li>Differenzierbarkeit zeigen &rarr; $\displaystyle \lim_{h \rightarrow 0} \frac{f(x_0+h)-f(x_0)- A \cdot h}{\|h\|}$</li>
  <li>L&ouml;sung eines Anfangswertproblems bestimmen</li>
  <li>&bdquo;Beweisen Sie Existenz und Eindeutigkeit einer L&ouml;sung&ldquo; &rarr; Picard-Lindel&ouml;f</li>
  <li>Zeigen Sie die rektifizierbarkeit eines Weges $\gamma$:<br/>
      &rarr; Differenzierbarkeit zeigen, ableiten, stetigkeit der Ableitung zeigen.</li>
</ul>

<h2>Lernplan</h2>
Man sollte die &Uuml;bungsbl&auml;tter nochmals machen, die relevanten Kapitel im <a href="http://mitschriebwiki.nomeata.de/Ana1.pdf">Skript f&uuml;r Analysis I</a> und im Skript f&uuml;r <a href="http://mitschriebwiki.nomeata.de/SS10/Ana2Bachelor.pdf">Analysis II (Bachelor)</a> durchlesen und Klausuren rechnen. (Aktuellere Skripte finden sich in meinem <a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/documents">GitHub Repository</a>. Allerdings muss man die PDF selbst erstellen.)

<h2>Termine und Klausurablauf</h2>
<strong>Datum</strong>: Dienstag, den 25. September 2012 von 08:00 bis 13:00 Uhr
<strong>Ort</strong>: <a href="http://www.math.kit.edu/iana3/~schmoeger/seite/einteilung/de">H&ouml;rsaaleinteilung</a> - Ich bin im <a href="https://maps.google.com/maps?q=49.009522,8.412978&ll=49.009522,8.412979&spn=0.000932,0.002642&num=1&t=m&z=19">Hetz-H&ouml;rsaal</a>.
<strong>Dauer</strong>: 2 h Analysis I, 1 h Pause, 2 h Analysis II
<strong>Punkte</strong>: 7 Aufgaben &agrave; 3 Punkte f&uuml;r Analysis I, 7 Aufgaben &agrave; 3 Punkte f&uuml;r Analysis II
<strong>Bestehensgrenze</strong>: Wohl bei ca. 21 Punkten
<strong>&Uuml;bungsschein</strong>: Ist im Studierendenportal eingetragen
<strong>Bonuspunkte</strong>: Gibt es nicht.

<h2>Ergebnisse</h2>
Die Klausureinsicht ist am 24.10.2012 von 14:00 - 16:30 Uhr (<a href="http://www.math.kit.edu/iana3/lehre/ana22012s/event/einsicht/">Quelle</a>).
