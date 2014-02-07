---
layout: post
title: Algorithmen II - Klausur
author: Martin Thoma
date: 2013-02-04 20:03:14.000000000 +01:00
categories:
- German posts
tags:
- Klausur
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesungen des Moduls &bdquo;Algorithmen II&ldquo; am KIT. Er dient als Pr&uuml;fungsvorbereitung. Ich habe die Vorlesungen bei Prof. Dr. Wagner gehört.</div>

<h2>Vorbereitung</h2>
<strong>Themen</strong>:
<ul>
  <li>Netzwerke und Fl&uuml;sse
    <ul>
      <li>Wert eines Flusses, s-t-Schnitt</li>
      <li>(Minimale) Schnitte, erhöhende Wege</li>
      <li>Max-Flow Min-Cut Theorem</li>
      <li>Ford-Fulkerson-Algorithmus: 
        <ul>
          <li>Erhöhende Wege, Vorwärts- und R&uuml;ckwärtskanten</li>
          <li>Spezialfall: Algorithmus von Edmonds und Karp
           <ul>
             <li>K&uuml;rzeste erhöhende Wege</li>
             <li>Laufzeit: $\mathcal{O}(|V| \cdot |E^2|)$</li>
           </ul>
          </li>
        </ul>
      <li>Flussproblem als Lineares Programm</li>
      <li>Dualität</li>
      <li>Algorithmus von Goldberg und Tarjan (Residualgraph, Push/Relabel)</li>
      <li>MINCOSTFLOW, erhöhende Kreise</li>
      <li>Cycle Canceling Algorithmus</li>
      <li>Algorithmus von Stoer & Wagner</li>
    </ul>
  </li>
  <li>Kreise
    <ul>
      <li>Definition: Kreis, einfacher Kreis</li>
      <li>Kreisbasen, Kreisraum</li>
      <li>Matroide</li>
      <li>Zertiﬁkat fur MCB</li>
    </ul>
  </li>
  <li>Randomisierte Algorithmen
    <ul>
      <li>Las Vegas Algorithmus / Monte Carlo Algorithmus</li>
      <li>Monte Carlo Algorithmus f&uuml;r MinCut</li>
      <li>Fast Random MinCut</li>
      <li>Maximum Satisﬁability Problem</li>
      <li>Random MaxCut</li>
      <li>Maximum Satisﬁability Problem</li>
      <li><abbr title="Integer Quadratic Program">IQP</abbr></li>
    </ul>
  </li>
  <li>Algorithmische Geometrie
    <ul>
      <li>Was ist ein einfaches Polygon, was ein konvexes Polygon?</li>
      <li>Sweep Line Algorithmus</li>
      <li>Konvexe H&uuml;lle: 
        <ul>
          <li>Graham Scan</li>
          <li>Gift Wrapping Algorithmus (Jarvis March) &rarr; <a href="http://codegolf.stackexchange.com/q/11035/5240">Code Golf</a></li>
        </ul>
    </ul>
  </li>
  <li>String-Matching
    <ul>
      <li>Rabin & Karp</li>
      <li>Endlichen Automaten</li>
      <li>Vorberechnungen f&uuml;r viele Suchanfragen: 
        <ul>
          <li>Suffixbäume</li>
          <li>Suffixarray</li>
          <li><abbr title="longest common prefix">LCP</abbr>-Array</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Approximierende Algorithmen
    <ul>
      <li>Multiprozessor-Scheduling
        <ul>
          <li>List Scheduling Algorithm</li>
        </ul>
      </li>
      <li>Bin Packing
        <ul>
          <li><span class="smallCaps">Next Fit</span> Algorithm</li>
          <li><span class="smallCaps">First Fit</span> Algorithm</li>
          <li><abbr title="Asymptotic PAS">APAS</abbr></li>
          <li>Restricted Bin Packing</li>
          <li>APAS und FAPAS</li>
        </ul>
      </li>
      <li><abbr title="Polynomielles Approximationsschema">PAS</abbr></li>
      <li><abbr title="Fully Polynomial Approximation Scheme">FPAS</abbr></li>
    </ul>
  </li>
  <li>Parametrisierte Algorithmen &rarr; <a href="http://de.wikipedia.org/wiki/Parametrisierter_Algorithmus">Wiki</a>
    <ul>
      <li>Fixed Parameter Tractable</li>
      <li>Kernbildung (Vertex Cover)</li>
      <li>Tiefenbeschrankte Suchbäume</li>
    </ul>
  </li>
  <li>Online Algorithmen
    <ul>
      <li>Job Scheudling</li>
      <li>c-kompetitivität</li>
      <li>Ski-Verleih Beispiel</li>
      <li>Paging (<abbr title="Longest Forward Distance">LFD</abbr>, Kompetitive Paging-Algorithmen, <span class="hint" title="FIFO, LRU">Konservative Paging-Algorithmen</span>, <a href="http://de.wikipedia.org/wiki/FIFO-Anomalie">B&eacute;l&aacute;dys Anomalie</a>)</li>
    </ul>
  </li>
  <li>Parallele Algorithmen
    <ul>
     <li><abbr title="Parallel Random Access Machine">PRAM</abbr> Modell</li>
     <li>Berechnung von Summen</li>
     <li>Präfxsumme</li>
     <li>List Ranking</li>
     <li>Binaroperationen einer partitionierten Menge</li>
     <li>Zusammenhangskomponenten</li>
     <li>Minimaler Spannbaum</li>
    </ul>
  </li>
  <li>Algorithmen fur externen Speicher
    <ul>
      <li>Einfaches Rechnermodell</li>
      <li>Interner Stack / Externer Stack / Externe Warteschlange</li>
      <li>Multiway Merge Sort</li>
      <li>Tournament-Bäume</li>
    </ul>
  </li>
</ul>

<h2>Algorithmen und Laufzeiten</h2>
<table>
<thead>
<tr>
<th>Algorithmus</th><th>Laufzeit</th>
</tr>
</thead>
<tbody>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung2.pdf#page=18">Algorithmus von Ford und Fulkerson
</a></td><td>-</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung2.pdf#page=21">Algorithmus von Edmonds und Karp
</a></td><td>$\mathcal{O}(|V| \cdot |E|^2)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung3.pdf#page=23">Algorithmus von Stoer und Wagner</a></td><td>$\mathcal{O}(|V|^3)$ oder besser, je nach Wahl des aktiven Knotens</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung5.pdf#page=7">Algorithmus von Stoer und Wagner</a></td><td>$\mathcal{O}(|V|^2 \log |V| + |V| |E|)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung7.pdf#page=12">Algorithmus von Horton</a></td><td>$\mathcal{O}(|E|^3 |V|)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung7.pdf#page=14">Algorithmus von de Pina</a></td><td>$\mathcal{O}(|E|^3 + |E| |V|^2 \log |V|)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung10.pdf#page=27">Sweep-Line-Algorithmus</a></td><td>$\mathcal{O}(n \cdot \log n)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung11.pdf#page=22">Graham-Scan</a></td><td>$\mathcal{O}(n \cdot \log n)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung11.pdf#page=22">Gift-Wrapping (Jarvis' March)</a></td><td>$\mathcal{O}(h \cdot n)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung12.pdf#page=23">Algorithmus von Rabin und Karp</a></td><td>$\mathcal{O}((n-m) \cdot m)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung12.pdf#page=28">String-Matching-Automat</a></td><td>Vorbereitung: $\mathcal{O}(|\Sigma| \cdot m^3)$<br/>Matching: $\mathcal{O}(n)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung13.pdf#page=5">Suffix-Bäume</a></td><td>Vorbereitung: $\mathcal{O}(n^2)$<br/>Matching: $\mathcal{O}(m \cdot \log |\Sigma|)$</td></tr>
<tr><td><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung13.pdf#page=26">Suffix-Arrays</a></td><td>Vorbereitung: $\mathcal{O}(n)$<br/>Matching: $\mathcal{O}(m \cdot \log |n|)$</td></tr>
</tbody>
</table>

<h2>Komplexitätsklassen</h2>
<div class="definition">Die Klasse $\mathcal{PP}$ (probabilistic polynomial) enthält alle Entscheidungsprobleme $\Pi$, f&uuml;r die es einen polynomialen, randomisierten Algorithmus $A$ gibt, so dass f&uuml;r alle Instanzen $I$ von $\Pi$ gilt:
$
\begin{cases} 
I    \in Y_\Pi & Pr[A(I) \text{ ist "Ja"}] \ge \frac{1}{2} \\
I \notin Y_\Pi & Pr[A(I) \text{ ist "Ja"}] \le \frac{1}{2}
\end{cases}$
</div>

<div class="definition">Die Klasse $\mathcal{BPP}$ (bounded error PP) enthält alle Entscheidungsprobleme $\Pi$, f&uuml;r die es einen polynomialen, randomisierten Algorithmus $A$ gibt, so dass f&uuml;r alle Instanzen $I$ von $\Pi$ gilt:
$
\begin{cases} 
I    \in Y_\Pi & Pr[A(I) \text{ ist "Ja"}] \geq \frac{3}{4} \\
I \notin Y_\Pi & Pr[A(I) \text{ ist "Ja"}] \leq \frac{1}{4}
\end{cases}$
</div>

<div class="definition">Die Klasse $\mathcal{RP}$ (randomisiert polynomial) enthält alle Entscheidungsprobleme $\Pi$, f&uuml;r die es einen polynomialen, randomisierten Algorithmus $A$ gibt, so dass f&uuml;r alle Instanzen $I$ von $\Pi$ gilt:
$
\begin{cases} 
I    \in Y_\Pi & Pr[A(I) \text{ ist "Ja"}] \geq \frac{1}{2} \\
I \notin Y_\Pi & Pr[A(I) \text{ ist "Ja"}] = 0
\end{cases}$
</div>

Es gilt: $\mathcal{RP} \subseteq \mathcal{BPP} \subseteq \mathcal{PP}$

<div class="definition">Die Klasse $\mathcal{NC}$ (Nick's Class) ist die Klasse der Probleme, die durch einen parallelen Algorithmus $A$ mit polylogarithmischer Laufzeit und polynomieller Prozessorenzahl gelöst werden können, d.h. $T_A(n) \in \mathcal{O}((\log n)^k_1)$ mit Konstante $k_1$ und $P_A(n) \in \mathcal{O}(n^{k_2})$ mit Konstante $k_2$.
</div>

<div class="definition">Die Klasse $\mathcal{SC}$ (Steve's Class) ist die Klasse der Probleme, die durch einen sequentiellen Algorithmus mit polylogarithmischem Speicherplatzbedarf und polynomieller Laufzeit gelöst werden können.
</div>

<h2>Übungsblätter</h2>
<a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebungsblatt1.pdf">Übungsblatt 1</a>, 06.02.2013: <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebung1.pdf">Lösung</a>
<ul>
  <li>Amortisierte Laufzeitanalyse: Buchungsmethode</li>
  <li>Was ist ein Netzwerk? Was ist ein Fluss? Was sind die Kapazitätsbedingung und die Flusserhaltung?</li>
</ul>

<a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebungsblatt2.pdf">Übungsblatt 2</a>, 13.02.2013: <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebung2.pdf">Lösung</a>
<ul>
  <li>Wie bekommt man aus dem maximalen Fluss den minimalen Schnitt mit Push-Relabel?</li>
  <li>Berechnung eines Matchings mit hilfe eines MAX-FLOW-Algorithmus.</li>
  <li>Wie benutze ich den Algorithmus von Stoer und Wagner?
    <ul>
      <li>Funktioniert f&uuml;r negative Kantengewichte nicht, z.B. Graph mit 3 Knoten und 2 negativen Kanten.</li>
    </ul>
  </li>
</ul>

<a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebungsblatt3.pdf">Übungsblatt 3</a>, 20.02.2013: <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebung3.pdf">Lösung</a>
<ul>
  <li>Algorithmus von de Pina ausf&uuml;hren (<a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung7.pdf">Vorlesung Nr 7</a>)</li>
  <li>Einiges zu Kreisbasen</li>
  <li>Wie bekomme ich mit einem nicht-perfektem M&uuml;nzwurf eine 50%-Wahrscheinlichkeit? &rarr; <a href="http://math.stackexchange.com/q/309003/6876">Antwort</a></li>
</ul>

<a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebungsblatt4.pdf">Übungsblatt 4</a>, 20.02.2013: <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebung4.pdf">Lösung</a>
<ul>
  <li>Wie finde ich heraus, ob sich zwei gegebene Strecken schneiden? &rarr; <a href="../how-to-check-if-two-line-segments-intersect/" title="How to check if two line segments intersect">Antwort</a></li>
</ul>

<a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebungsblatt5.pdf">Übungsblatt 5</a>, 22.02.2013: <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebung5.pdf">Lösung</a>
<ul>
  <li>Wie berechnet man den Suffix-Baum und das Suffix-Array von mississippi? &rarr; <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/vorlesung13.pdf">Vorlesung Nr 13</a></li>
  <li>Wie funktioniert der Rabin-Karp-Algorithmus zum String-Matching?</li>
  <li>Wie erstellt man einen String-Matching-Automaten?</li>
</ul>

<a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebungsblatt6.pdf">Übungsblatt 6</a>, 24.02.2013: <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/uebung6.pdf">Lösung</a>
<ul>
  <li>Welcher Algorithmus f&uuml;r <span class="smallCaps">Vertex Cover</span> hat eine Approximationsg&uuml;te von 2?</li>
</ul>

<h2>Fakten und interessante Fragen</h2>
<ul>
  <li>Algorithmus ist konservativ $\Rightarrow$ Algorithmus ist k-kompetitiv. (Quelle: <a href="http://ls2-www.cs.uni-dortmund.de/~sieling/online07/material/online.pdf#page=5">Begleitmaterial zur Vorlesung Online-Algorihmen</a>, Uni Dortmund)</li>
  <li>$c(S, V \setminus S) := \sum_{(i,j) \in E,\\i \in S, j \in V \setminus S} c(i,j)$</li>
</ul>

<div class="question">
<span class="question">Was ist der Worst-Case f&uuml;r <span class="smallCaps">List Scheduling</span> mit $m$ Maschinen?</span>
<div class="answer">
Gegeben seien $n \cdot (m-1)$ Jobs &agrave; 1 Sekunde und ein Job mit $n$ Sekunden. Die Gesamtlaufzeit beträgt dann $2 \cdot n - 1$ Sekunden, die beste Laufzeit ist jedoch $n$ Sekunden.
</div>
</div>

<div class="question">
<span class="question">Was ist der Worst-Case f&uuml;r <span class="smallCaps">Next Fit</span>?</span>
<div class="answer">
$n$ Elemente mit dem Gewicht $\frac{1}{2}$ und $2n$ Elemente mit dem Gewicht $\frac{1}{2}$ und $2n$ Elemente mit dem Gewicht $\frac{1}{2 \cdot n}$.
</div>
</div>

<h2>Termine und Klausurablauf</h2>
<strong>Datum</strong>: Freitag, den 1. März 2013 von 11:00 bis 13:00 (<a href="http://www.informatik.kit.edu/klausuren.php?kid=422.35">Quelle</a>)
<strong>Ort</strong>: Tulla-Hörsaal (Siehe <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/0225raumlisten.pdf">Liste</a>)
<strong>Dauer</strong>: 2 Stunden
<strong>Punkte</strong>: 60
<strong>Bestehensgrenze</strong>: 20
<strong>Übungsschein</strong>: Gibt es nicht.
<strong>Bonuspunkte</strong>: Gibt es nicht.
<strong>Nicht vergessen</strong>:
<ul>
  <li>Studentenausweis</li>
  <li>Kugelschreiber</li>
</ul>

<h2>Ergebnisse</h2>
Der Termin f&uuml;r die Klausureinsicht ist noch nicht bekannt (Stand: 01.03.2013)

Seit heute (07.03.2013) sind die Ergebnisse da:
<ul>
  <li><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/klausurid-note.pdf">Ergebnisse</a></li>
  <li><a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2012/algo2/ws1213-1-loesung.pdf">Musterlösung</a></li>
  <li>Termin der Einsicht ist noch nicht bekannt (Stand: 07.03.2013)<br/>
Update vom 09.03.2013: Einsicht ist am Dienstag, den 19. März von 15:00 bis 17:00 Uhr
und am Donnerstag, den 4. April von 15:00 bis 17:00 jeweils in Raum 301 im Infobau 50.34</li>
</ul>

{% caption align="aligncenter" width="300" caption="Algorithmen II - Ergebnis-Statistik" url="../images/2013/02/algorithmen-2-stats-300x190.png" alt="Algorithmen II - Ergebnis-Statistik"  height="190" class="size-medium wp-image-62061" %}
