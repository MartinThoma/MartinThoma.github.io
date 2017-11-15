---
layout: post
title: KogSys-Klausur
author: Martin Thoma
date: 2013-04-19 20:38:47.000000000 +02:00
category: German posts
tags: Klausur, KogSys, ASR
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Dieser Artikel besch&auml;ftigt sich mit der Vorlesung &bdquo;Kognitive Systeme&ldquo; am KIT. Er dient als Pr&uuml;fungsvorbereitung. Ich habe die Vorlesungen bei Herrn Dr. Waibel im Sommersemester 2013 geh&ouml;rt.</div>

<h2>Behandelter Stoff</h2>
<h3>Vorlesung</h3>
<table>
<tr>
<td style="border-bottom:1px solid black;">15.04.2013</td>
<td style="border-bottom:1px solid black;"><a href="https://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/save/KogSysSkript.pdf#page=5">Kapitel 1</a></td>
<td style="border-bottom:1px solid black;">Einf&uuml;hrung</td>
</tr>

<tr>
<td style="border-bottom:1px solid black;">17.04.2013</td>
<td style="border-bottom:1px solid black;">&nbsp;</td>
<td style="border-bottom:1px solid black;">Faltung, Fouriertransformation, Dirac-Funktion</td>
</tr>

<tr>
<td style="border-bottom:1px solid black;">29.04.2013</td>
<td style="border-bottom:1px solid black;"><a href="https://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/save/05_06-Classification_2013.pdf">Klassifikation I</a></td>
<td style="border-bottom:1px solid black;">Schablonenanpassung: <span class="hint" title="Skalierung, Perspektiven, Drehung, Verzerrung, Helligkeit">Probleme</span>, Statistische Auswertung immer wichtig da Signale ambig sind, Assoziative Netze, Bayes Decision Theorie, Gaussian Classificator - "Covarianzmatrix tut das Richtige [und eliminiert von einander Abh&auml;ngige Dimensionen]", Mahalanobis-Distanz; Gauss-Klassifikator ist quadratischer Form (Kreis, Ellipse, Linie), Overfitting = "Vorurteil" passiert, wenn man zu wenig Daten bzw. zu viele Dimensionen daf&uuml;r hat - "Fluch der Dimensionalit&auml;t"; Hauptachsentransformation reduziert Dimensionalit&auml;t</td>
</tr>

<tr>
<td style="border-bottom:1px solid black;">06.05.2013</td>
<td style="border-bottom:1px solid black;"><a href="https://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/save/07_08-MachineLearning_2013.pdf">Machine Lerning</a></td>
<td style="border-bottom:1px solid black;">Klassifikation: Risikobetrachtung bei Klassifikatoren, Gaussian Mixtures, Parzan Windows (nicht-parametrisiert, &uuml;berwacht), Fisher Linear Discriminant (scatter matrix), Linear seperable, <a href="https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm">K-nearest neighbors</a> (nicht-parametrisch, nicht-linear, &uuml;berwacht)</td>
</tr>

<tr>
<td style="border-bottom:1px solid black;">13.05.2013</td>
<td style="border-bottom:1px solid black;"><a href="https://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/save/07_08-MachineLearning_2013.pdf#page=25">Neural Nets</a></td>
<td style="border-bottom:1px solid black;">Perceptron Criterion Function; <abbr title="Multilevel Perceptron">MLP</abbr></td>
</tr>

<tr>
<td style="border-bottom:1px solid black;">27.05.2013</td>
<td style="border-bottom:1px solid black;"><a href="https://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/save/09_Bildverarbeitung1-2013.pdf">Bildverarbeitung I</a></td>
<td style="border-bottom:1px solid black;">Lochkartenmodell, HSI-Farbmodell, RGB2HSI, RGB2Graustufen, <a href="http://de.wikipedia.org/wiki/Punktoperator_(Bildverarbeitung)#Histogrammspreizung_und_-stauchung">Histogrammspreizung</a></td>
</tr>

<tr>
<td style="border-bottom:1px solid black;">29.05.2013</td>
<td style="border-bottom:1px solid black;"><a href="https://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/save/10_Bildverarbeitung2-2013.pdf">Bildverarbeitung II</a></td>
<td style="border-bottom:1px solid black;">Pixel-Transformation, Bildverarbeitung, Merkmalsextraktion, Form, Struktur, Klassifikation</td>

<tr>
<td style="border-bottom:1px solid black;">03.06.2013</td>
<td style="border-bottom:1px solid black;">(Nicht verf&uuml;gbar)</td>
<td style="border-bottom:1px solid black;">2D-Bildverarbeitung: Schwellwert, Graustufen, Segmentierung, Kanten-/Knotenerkennung; Hough-Tranformation; Harris-Corner-Detector; <a href="https://martin-thoma.com/kalman-filter/">Kalman-Filter</a>; Erosion / Dilatation; &Ouml;ffnen / Schlie&szlig;en</td>

<tr>
<td style="border-bottom:1px solid black;">10.06.2013</td>
<td style="border-bottom:1px solid black;">(Nicht verf&uuml;gbar)</td>
<td style="border-bottom:1px solid black;">Spracherkennung: Lautbildung, Vokale werden durch 1., 2. Formante bestimmt</td>
</tr>

<tr>
<td style="border-bottom:1px solid black;">24.06.2013</td>
<td style="border-bottom:1px solid black;">(Nicht verf&uuml;gbar)</td>
<td style="border-bottom:1px solid black;">3D-Bildverarbeitung: <a href="https://martin-thoma.com/kalman-filter/">Kalman-Filter</a>; Partikelfilter; homogene Koordinaten</td>
</tr>
</table>

Falls hier was fehlt, k&ouml;nnt ihr mich gerne in den Kommentaren oder per Mail (info@martin-thoma.de) darauf aufmerksam machen.

<h3>Folien</h3>
<h4>01: Einf&uuml;hrung</h4>
Nichts interessantes.

<h4>02, 03: Digital Signal Processing</h4>
<ul>
  <li><a href="http://de.wikipedia.org/wiki/Alias-Effekt">Alias-Effekt</a>, <a href="http://de.wikipedia.org/wiki/Nyquist-Shannon-Abtasttheorem">Abtasttheorem</a></li>
  <li>Digitalisierung: Zeit- und Wertdiskretisierung</li>
  <li><a href="http://de.wikipedia.org/wiki/Dirac-Funktion">Dirac-Funktion</a></li>
  <li>Faltung</li>
  <li>Fouriertransformation</li>
  <li>Korrelation: Autokorrelation, Kreuzkorrelation</li>
</ul>

<h4>04: Intelligente und Kognitive Systeme</h4>
Interessant, aber vermutlich nicht Klausurrelevant.

<h4>05, 06: Klassifikation</h4>
<ul>
  <li>Schablonenanpassung: Wie &auml;hnlich ist das Muster einer Schablone?</li>
  <li>Normalisierung der Helligkeit</li>
  <li>Gauss-Klassifikation: Parametrisch</li>
  <li>Parzen Window: Nicht parametrisch</li>
  <li>k-nearest-neighbor: nicht parametrisch</li>
  <li>Perceptron: nicht parametrisch</li>
  <li>Bayes-Regel</li>
  <li>Principal Component Analysis (PCA)</li>
  <li>Linear Discriminant Function, Fisher-Linear Discriminant</li>
</ul>

<h4>07, 08: Machine Learning</h4>
<figure class="aligncenter">
            <a href="../images/2013/04/pattern-recognition-classification-300x172.png"><img src="../images/2013/04/pattern-recognition-classification-300x172.png" alt="Pattern recognition classification" style="max-width:300px;max-height:172px" class="size-medium wp-image-76312"/></a>
            <figcaption class="text-center">Pattern recognition classification<br />Image Source: Folien von Prof. Waibel</figcaption>
        </figure>

<ul>
  <li>Perceptron<: <a href="http://de.wikipedia.org/wiki/Sigmoidfunktion">Sigmoidfunktion</a>/li>
  <li>Classifier Discriminant Functions</li>
  <li>Linear Discriminant Functions</li>
</ul>

<h4>09: Bildverarbeitung I</h4>
<ul>
  <li>Bildrepr&auml;sentation als Monochrombild</li>
  <li>RGB / HSI-Modell</li>
  <li>Bayer-Pattern</li>
  <li>Lochkamera-Modell</li>
  <li>Affine Punktoperatoren: $g := round(a \cdot I(u,v) + b)
I'(u,v) := 
\begin{cases}
0 &\text{, falls } g < 0\\
q &\text{, falls } g > q\\
g &\text{sonst}
\end{cases}$
    <ul> 
      <li>Kontrasterh&ouml;hung: $b=0; a > 1$</li>
      <li>Kontrastverminderung: $b=0; a < 1$</li>
      <li>Helligkeitserh&ouml;hung:  $b>0; a = 1$</li>
      <li>Helligkeitsverminderung:  $b<0; a = 1$</li>
      <li>Invertierung:  $b=q; a =-1$</li>
    </ul>
  </li>
  <li>Nicht-Affine Punktoperatoren</li>
  <li>Automatische Kontrastanpassung (Spreizung, Histogrammdehnung, Histogrammausgleich)</li>
</ul>

<h4>10: Bildverarbeitung II</h4>
<ul>
  <li>Fourier-Transformation</li>
  <li>2D Fourier-Transformation</li>
  <li>Fourier-R&uuml;cktransformation</li>
  <li>Ortsbereich / Frequenzbereich</li>
  <li>Tiefpassfilter
    <ul>
      <li>Mittelwertfilter: Rauschunterdr&uuml;ckung</li>
      <li><strong>Gau&szlig;-Filter</strong>: Rauschunterdr&uuml;ckung, Gl&auml;ttung</li>
    </ul>
  </li>
  <li>Hochpassfilter
    <ul>
      <li>Prewitt</li>
      <li>Sobel</li>
      <li>Laplace</li>
      <li>Roberts</li>
    </ul>
  </li>
  <li>KOmbinierte Operatoren
    <ul>
      <li>Laplacian of Gaussian</li>
    </ul>
  </li>
  <li>Canny-Kantendetektor</li>
</ul>

<h4>11: Bildverarbeitung III</h4>
<ul>
  <li>Segmentierung (Schwelltwert, Farbe)</li>
  <li>Morphologische Operatoren: Dilatation, Erosion</li>
  <li>&Ouml;ffnen, Schlie&szlig;en</li>
  <li>Hough-Transformation</li>
  <li>Sum of Squared Differences; Zero Mean Normalized Cross-Correlation</li>
  <li>Partikelfilter</li>
</ul>

<h4>12: Spracherkennung</h4>
<ul>
  <li>Faltung</li>
  <li>Formanten</li>
  <li>Spektogramm</li>
  <li>Akustisches Modell, Sprachmodell</li>
  <li>(Hidden-)Markov-Modell</li>
  <li><strong>Forward-, Forward-Backward- und Viterbi-Algorithmus</strong></li>
</ul>

<h4>13: ?</h4>
<h4>14: ?</h4>

<h4>15: Bildverarbeitung IV</h4>
<ul>
  <li>Geometrische 3D-Transformationen: Rotation um Achsen</li>
  <li>Quaternionen</li>
  <li>Erweitertes Lochkameramodell</li>
  <li>Kamerakalibrierung</li>
  <li>Diskrete Lineare Transformation</li>
  <li>Stereorekonstruktion</li>
  <li>Epipolargeometrie</li>
  <li>Fundamentalmatrix</li>
</ul>

<h4>16: Visuelle Wahrnehmung</h4>
Vermutlich nichts Klausurrelevantes (offiziell ab Folie 25)

<h4>17: Wissen und Planung I</h4>
<ul>
  <li>Satz, Wissensdatenbank, Deduktion</li>
  <li>Symbolmenge, Modellmenge, Syntax, Semantik</li>
  <li>Korrektheit und vollst&auml;ndigkeit eines Deduktions-Algorithmus</li>
  <li>Algorithmen: <strong>Resolution, Horn-Klauseln, DPLL</strong></li>
  <li>Planungssprachen: <strong><abbr title="STanford Research Institute Problem Solver">STRIPS</abbr>, <abbr title="Action Description Language">ADL</abbr></strong></li>
  <li><strong>A*-Suche, Partial-Order-Planning, Planungsgraphen</strong></li>
</ul>

<h4>18: Wissen und Planung II</h4>
<ul>
  <li>Partial-Order-Planning</li>
  <li>Planungsgraphen</li>
  <li>Kantenmodell, Oberfl&auml;chenmodell, Volumenmodell</li>
  <li>Freiraum, Hindernisraum, Konfigurationsraum</li>
  <li>Polygonzerlegung</li>
  <li>Sichtgraphen</li>
  <li>Quadtrees</li>
  <li>Voronoi-Diagramme</li>
  <li>Potentialfeldmethode</li>
</ul>

<h4>19: Robotik</h4>
Offiziell nicht Klausurrelevant.

<h2>Material</h2>
<ul>
  <li><a href="http://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/">Vorlesungswebsite</a></li>
  <li><a href="./anki/KogSys.apkg">Mein Anki-Deck</a></li>
  <li><a href="http://www.next-internet.com/hauptstudium/">Klausuren</a></li>
  <li><a href="https://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/save/vorlesungsfolien.php">Folien</a></li>
  <li><a href="https://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/save/KogSysSkript.pdf">Skript</a></li>
  <li><a href="https://github.com/elm/KogSys-Zusammenfassung">Zusammenfassung</a></li>
  <li>Videos
    <ul>
      <li><a href="//www.youtube.com/watch?v=aVId8KMsdUU">Neural network tutorial: The back-propagation algorithm</a></li>
      <li><a href="//www.youtube.com/watch?v=46Jzu-xWIBk">The backpropagation algorithm</a></li>
    </ul>
  </li>
  <li>Pseudocode f&uuml;r
    <ul>
      <li><a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/source-code/Pseudocode/DPLL">DPLL-Verfahren</a></li>
      <li><a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/source-code/Pseudocode/Resolutionsalgorithmus">Resolutions-Algorithmus</a></li>
    </ul>
  </li>
  <li><a href="http://colorizer.org/">Colorizer</a>: Hier kann man ein bisschen mit Farbr&auml;umen rumspielen und die Unterschiede interaktiv feststellen.</li>
  <li>StackOverflow:
    <ul>
      <li><a href="http://math.stackexchange.com/q/487245/6876">Why is $(-1) \cdot j = j \cdot (-1)$ for quaternions?</a></li>
    </ul>
  </li>
  <li>Artikel:
    <ul>
      <li><a href="../graphic-filters/">Graphic filters</a>: Mit einem interaktiven Beispiel aller Filter!</li>
      <li><a href="../k-nearest-neighbor-classification-interactive-example/">Clustering-Algorithmen</a>: Mit interaktivem Beispiel</li>
      <li><a href="../calculations-with-quaternions/">Calculations with quaternions</a></li>
      <li><a href="../calculate-histogram-equalization/">How do I calculate a histogram equalization?</a></li>
      <li><a href="../apply-viterbi-algorithm/">How to apply the Viterbi algorithm</a></li>
      <li><a href="../html5/route-planning/route-planning.htm">Interactive example for route planning</a></li>
      <li><a href="../word-error-rate-calculation/">Word Error Rate (WER) calculation</a></li>
    </ul>
  </li>
  <li>Grafische Faltung: 
    <ul>
      <li><a href="http://www.jhu.edu/signals/convolve/">John Hopkins University</a>, Java Applet</li>
      <li><a href="http://www.onmyphd.com/?p=convolution">onmyphd.com</a>, JavaScript</li>
    </ul>
  </li>
</ul>

Das Passwort f&uuml;r kogsys darf ich auch im Jahr 2013 nicht verraten.

<h2>Aufbau der Klausur</h2>
6 Aufgaben:
<ul>
  <li>Bildverarbeitung</li>
  <li>Bildverarbeitung, Filter und Transformation</li>
  <li>Logik, Wissensrepr&auml;sentation und Planung
    <ul>
      <li>Eine Aufgabe, in der man den Resolutionsalgorithmus / das DPLL-Verfahren anwenden muss</li>
      <li>A*-Algorithmus</li>
    </ul>
  </li>
  <li>Allgemeine Fragen</li>
  <li>Signal- und Sprachverarbeitung</li>
  <li>Klassifikation und Maschinelles Lernen</li>
</ul>

<h2>&Uuml;bungsbetrieb</h2>
<ul>
<li>Wo sind die &Uuml;bungsbl&auml;tter: <a href="http://his.anthropomatik.kit.edu/Teaching/VorlesungKognitiveSysteme/websubmit/student/blattuebersicht.php">Link</a></li>
<li>Abgabeform: nur Handschriftlich</li>
<li>Abgabe: teilweise online, teilweise offline, wenn offline m&uuml;ssen die &Uuml;bungsbl&auml;tter direkt vor der &Uuml;bung abgegeben werden, oder irgendwann davor im B&uuml;ro des &Uuml;bungsleiters in der Kinderklinik. Direkt im B&uuml;ro scheint ihm aber nicht so lieb zu sein.</li>
<li>R&uuml;cknahme: gar nicht, empfohlen wird eine Kopie des Originals zu behalten</li>
<li>Turnus: ? (6 Bl&auml;tter insgesammt)</li>
<li>&Uuml;bungsschein verpflichtend: es gibt keinen &Uuml;bungsschein soweit ich wei&szlig;</li>
<li>Bonus durch &Uuml;bungsschein: pro &Uuml;bungsblatt max. 1 Bonuspunkt &rarr; max. 6 Bonuspunkte (es gibt tats&auml;chlich 0,25-Punkte!)</li>
</ul>

<h2>Termine und Klausurablauf</h2>
<strong>Datum</strong>: Mittwoch, den 18. September 2013 von 11:00 bis 12:00 Uhr<br/>
<strong>Ort</strong>: steht noch nicht fest (Stand: 12.09.2013)<br/>
<strong>Punkte</strong>: 60<br/>
<strong>Bestehensgrenze</strong>: 20<br/>
<strong>&Uuml;bungsschein</strong>: Gibt es nicht<br/>
<strong>Bonuspunkte</strong>: Ja, max 6<br/>
<strong>Ergebnisse</strong>: ab 14.10.2013 im Websubmit und in 50.20. (Kinderklinik) am Eingang<br/>
<strong>Einsicht</strong>: 24.10.2013 von 13:30 bis 14:30 Uhr (Kinderklinik, Raum 148)<br/>

<h2>Nicht vergessen</h2>
<ul>
  <li>Studentenausweis</li>
  <li>Kugelschreiber</li>
</ul>

<h2>Ergebnisse</h2>
Sind noch nicht drau&szlig;en (Stand: 18.09.2013)
