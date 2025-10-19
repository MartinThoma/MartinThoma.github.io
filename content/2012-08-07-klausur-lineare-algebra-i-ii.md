---
layout: post
title: Klausur Lineare Algebra I + II
slug: klausur-lineare-algebra-i-ii
lang: de
author: Martin Thoma
date: 2012-08-07 09:35:33.000000000 +02:00
category: German posts
tags: Klausur
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
Dieser Artikel richtet sich vor allem an Studenten, die im Sommersemester 2012 bei Herrn Prof. Dr. Leuzinger am KIT die Klausur über Lineare Algebra und analytische Geometrie schreiben werden.

Was ich im folgenden unter "Themen" schreibe, wurde von Prof. Dr. Leuzinger in der letzten Stunde aufgeschrieben. Das habe ich als Grundlage genommen und ergänzt. Er gab folgende Tipps:
<ul>
  <li>Zeitplan aufstellen</li>
  <li>Aktiv lernen</li>
</ul>

Ich kann als Tipp für die Klausur noch sagen:
Wenn du eine Aufgabe (b) machst, überleg dir, ob dir die Ergebnisse aus (a) helfen können!
In den LA-Klausuren, die ich bisher gesehen habe, hat die vorangehende Teilaufgabe sehr häufig eine Hilfestellung geboten.

## Vorbereitung

### Lineare Algebra I
Ihr solltet auf jeden Fall die <a href="../lernkontrolle-lineare-algebra-i/" title="Lernkontrolle: Lineare Algebra I">Lernkontrolle: Lineare Algebra I</a> machen.

#### Themen
<ul>
  <li><strong>Gruppen</strong>: Untergruppe, Homomorphismus/Isomorphismus, $GL(n, \mathbb{K})$</li>
  <li><strong>Körper</strong>: $\mathbb{R}, \mathbb{C}, \mathbb{Z}/p\mathbb{Z}$ (insbesondere $p=2$)</li>
  <li><strong>Vektorräume</strong>: Basis, Basisergänzungssatz, Dimension, Basiswechsel, $V \cong \mathbb{K}^n$ (für $\dim V = n$); $\dim (U_1 \oplus U_2) = \dim U_1 + \dim U_2$</li>
  <li><strong>Lineare Abblidungen</strong> (Definitionen, Beispiele):
    <ul>
      <li>Lineare Fortsetzung, $\phi: V \rightarrow W$</li>
      <li>Dimensionssatz $\dim \text{Bild} \phi = \dim V - \dim \phi^2$</li>
      <li>$\text{Hom}(V, W) \cong \mathbb{K}^{m \times n}$ Abbildungsmatrix</li>
      <li><b>Dualraum</b>: $W = \mathbb{R}$, $V^* = \text{Hom}(V, \mathbb{K})$</li>
      <li>$\phi: V \rightarrow W$ A</li>
      <li>$\phi: W* \rightarrow V*$ $A^T$</li>
      <li>duale Basis, duale Abbildung</li>
      <li>Basiswechsel für Endomorphismen, Formel</li>
      <li>$\tilde{A} = S^{-1} A S$, S = Matrix des Basiswechsels</li>
    </ul>
  </li>
  <li><strong>Determinante</strong>:
     <ul>
       <li>Laplacesche Entwicklungsformel (z.B. nach i-ter Spalte)</li>
       <li>$\det A^T = \det A$</li>
       <li>$\det(A \cdot B) = \det A \cdot \det B$</li>
       <li>$\det(A^{-1}) = \frac{1}{\det A}$</li>
       <li>$$\det \begin{pmatrix}A & * \\0 & B\end{pmatrix} = \det A \cdot det(B)$$ ("Kästchensatz")</li>
       <li>Bei beliebig großen Matrizen &agrave; la $A \in \mathbb{R}^{n \times n}$ gibt es ein paar Dinge, die beim Suchen der Determinante hilfreich sein können:
         <ul>
           <li>Ist die Matrix symmetrisch? Falls ja, muss man sich nur die Zeilen anschauen. Falls nein, können die folgenden Tipps sowohl für die Zeilen als auch für die Spalten überprüft werden.</li>
           <li>Nützt es etwas, wenn ich auf die letzte Zeile alle vorherigen Zeilen addiere?</li>
           <li>Was passiert, wenn ich Zeile $i$ auf Zeile $(i+1)$ addiere für $i \in 1, ..., (n-1)$?</li>
         </ul>
       </li>
     </ul>
  </li>
  <li><a href="../wie-bestimme-ich-das-inverse-einer-matrix/">Wie bestimme ich das Inverse einer Matrix?</a></li>
  <li><strong>Lösungstheorie von LGSen</strong> (Gauß-Algorithmus)</li>
  <li><strong>Eigenwerte</strong>, Eigenvektoren  ($\phi(x) = \lambda x, x \neq 0$)</li>
  <li>charakteristisches Polynom $\phi|_{[x]} = \lambda_{id_{[x]}}$ - <a href="../wie-berechnet-man-das-charakteristische-polynom/">Wie berechnet man das charakteristische Polynom?</a></li>
  <li>$\mathbb{K} = \mathbb{C} \leadsto$ <strong>Jordansche Normalform</strong> (Algorithmus)</li>
</ul>

<h4>Aufgabenstellungen</h4>
Mit diesen Aufgabentypen sollte man rechnen:
<ul>
  <li>Gegeben sind zwei Untervektorräume $U, V$ des $\mathbb{R}^4$. Finden Sie jeweils eine Basis von $U, V, U \cap V, U + V$. &rarr; <a href="../wie-bildet-man-den-schnitt-zweier-vektorraume/">Erklärung</a></li>
  <li>Bestimmen Sie alle Lösungen eines Gleichungssystems (auch in endlichen Körpern wie $\mathbb{Z} / 5 \mathbb{Z}$!).</li>
  <li>Bestimmen Sie die Jordansche Normalform einter Matrix A. &rarr; <a href="../wie-berechnet-man-die-jordansche-normalform/">Erklärung</a></li>
</ul>

<h4>Good to know</h4>
Ähnlichkeitsinvariante Matrizeneigenschaften:
<ul>
  <li>Rang</li>
  <li>Spur</li>
  <li>Determinante</li>
  <li>Jordansche Normalform</li>
  <li>Charakteristisches Polynom</li>
</ul>

<ul>
  <li><a href="http://math.stackexchange.com/a/14079/6876">Wie findet man heraus, ob zwei Matrizen ähnlich sind?</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Regul%C3%A4re_Matrix#Invertierbare_Matrizen_.C3.BCber_einem_K.C3.B6rper">Wann sind Matrizen regulär?</a></li>
</ul>

<h4>Siehe auch</h4>
<ul>
  <li><a href="http://commons.wikimedia.org/wiki/File:Venn-diagramm-algebraische-strukturen.svg">Übersicht über algebraische Strukturen</a></li>
  <li><a href="http://next-internet.com/la/texte/la_zusammenfassung.pdf">Zusammenfassung auf next-indernet.com</a></li>
</ul>

<h3>Lineare Algebra II</h3>
<h4>Themen</h4>
<ul>
  <li><strong>Vektorräume mit Skalarprodukt</strong> (Definition, Beispiele, $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$)</li>
  <li>$G = G^T$ ($\mathbb{K} = \mathbb{R}$)</li>
  <li>$G = \bar{G}^T$ ($\mathbb{K} = \mathbb{C}$)</li>
  <li>Basiswechsel $\tilde{G} = S^T G S$ (allgemeiner Basiswechsel)</li>
  <li>Basiswechsel $\tilde{G} = S^{-1} G S$ (für ONB, da $S^{-1} = S^T$)</li>
  <li>Skalarprodukt induziert eine Norm, $\| x \| = \sqrt{\langle x, x \rangle}$</li>
  <li>Parallelogramm-Identität: $\|a+b\|^2 + \|a-b\|^2 = 2 \cdot (\|a\|^2 + \|b\|^2)$</li>
  <li>$\cos \omega(a,b) = \frac{\langle a, b \rangle}{\|a\| \cdot \| b \|}$</li>
  <li>Orthogonal, ONB, Orthogonal-Komplement</li>
  <li>$x \perp y$, $\langle x, y \rangle = 0$</li>
  <li>orthogonale / unitäre Matrizen:
     <ul>
       <li>$S \cdot S^T = E$</li>
       <li>$\det S \cdot \det S^T = \det E = 1$</li>
       <li>$U \cdot \bar U^T = E$</li>
     </ul>
  </li>
  <li><a href="http://de.wikipedia.org/wiki/Gram-Schmidtsches_Orthogonalisierungsverfahren">Gram-Schmidtsches Orthogonalisierungsverfahren</a>: $w_j = v_j - \sum_{i=1}^{j-1} \frac{\langle v_j, w_i \rangle}{\langle w_i, w_i \rangle} \cdot w_i$</li>
  <li>Projektion eines Vektors auf eine Ebene (ÜB 4, A3)</li>
  <li>"Gute" Abbildungen bzgl. $\langle, \rangle: \phi: V \rightarrow V$</li>
  <li>(Selbst-)adjungierte: $\langle \phi(x), y \rangle = \langle x, \phi*(y) \rangle \rightarrow A = A^T$</li>
  <li>Lineare Isometrien $\langle \phi(x), \phi(y) \rangle \rightarrow A$ orthogonal<br/>$\varphi$ heißt lineare Isometrie $:\Leftrightarrow \langle \varphi(x), \varphi(y) \rangle = \langle x, y \rangle$</li>
  <li>Abbildungsmatrizen bzgl. ONB</li>
  <li>Spektralsatz: $\phi s.a. \Rightarrow \phi \text{ diagonalisierbar}, \exists S \in O(n) \text{ mit } S^{-1} A S = D$.</li>
  <li>Abbildungsmatrizen bzgl. ONB</li>
  <li>$\phi$ s.a. Basis: ONB $\Rightarrow$ Abb. Matrix symmetrisch, aber noch mehr: $\exists$ ONB aus EV mit Abb. Matrix = Diagonalmatrix (Spektralsatz)</li>
  <li>$\phi$ lin. Isometrie, Basis ONB $\Rightarrow$ Abb. Matrix ist orthogonal / unitär, aber noch mehr: $\exists$ ONB mit Abb. in euklid NF</li>
  <li><strong><a href="../berechnung-der-euklidischen-normalform/">Berechnung der euklidischen Normalform</a></strong></li>
  <li>Kiterien für pos. definit (Ist geg. BF $\beta$ ein SP?)</li>
  <li><a href="http://de.wikipedia.org/wiki/Hauptachsentransformation">Hauptachsentransformation</a></li>
  <li>$(V, \langle , \rangle)$ VR mit SP. $\beta = $ Bilinearform  kann man simultan diagonalisieren $\exists$ ONB von $V$, so dass Matrix von $\langle, \rangle E_n$  (nach Definition von ONB)</li>
  <li><a href="http://de.wikipedia.org/wiki/Hurwitzpolynom#Hurwitz-Kriterium">Hurwitz-Kriterium</a></li>
</ul>

Affine / Euklidische Geometrie
$\operatorname{Aff}(\mathbb{R}^n), \mathrm{Iso}(\mathbb{R}^n)$ Gruppe der Affinität bzgl. Isometrie

<h2>Lernplan</h2>
Es empfiehlt sich, einen Lernplan aufzustellen. Wenn ich die Übungsblätter mache, dann lese ich mir zuerst die relevanten Kapitel im <a href="https://studium.kit.edu/sites/vab/0x40F0348A9ACDCE49A96EEE39EB076112/Vorlesungsunterlagen/Forms/AllItems.aspx">Skript</a> durch.

<h2>Termine und Klausurablauf</h2>
<strong>Datum</strong>: Donnerstag, den 13. September 2012 von 08:00 bis 13:00 Uhr<br/>
<strong>Ort</strong>: bei mir: <strike>Neue Chemie</strike> Hörsaal am Fasanengarten (&rarr; <a href="http://www.math.kit.edu/iag2/lehre/la2mathe20122012s/media/hoersaele-1.pdf">Hörsaaleinteilung</a>)<br/>
<strong>Dauer</strong>: 2 h LA I, 1 h Pause, 2 h LA II<br/>
<strong>Punkte</strong>: 6 Aufgaben &agrave; 4 Punkte für LA I, 6 Aufgaben &agrave; 4 Punkte für LA II<br/>
<strong>Geschwindigkeit</strong>: $\frac{5 \text{ Minuten}}{\text{Punkt}}$<br/>
<strong>Übungsschein</strong>: Noch nicht im Studierendenportal (Stand: 11.09.2012)<br/>
<strong>Bonuspunkte</strong>: Gibt es nicht.<br/>

<strong>Nicht vergessen</strong>:
<ul>
  <li>Studentenausweis</li>
  <li>Leere Blätter</li>
  <li>Essen und Trinken (4h Klausur!!!)</li>
</ul>

Ein paar interessante Aussagen:
<blockquote>In den letzten Jahren reichten 20 Punkte zum bestehen</blockquote>
<blockquote>In den letzten Jahren wurde jeweils im LA I und in LA II der beste Teil doppelt bepunktet</blockquote>
<blockquote>Es gab bisher nur eine Gesamtnote für LA I und II, man musste die beiden Tests also nicht einzeln bestehen.</blockquote>

## Ergebnisse
Ich habe den Übungsleiter mal angeschrieben. Das war seine Antwort:
<blockquote>
Der Termin ist normalerweise in der ersten Vorlesungswoche. Er wird auf der Kurshomepage rechtzeitig bekannt gegeben.
</blockquote>

<blockquote>Die Ergebnisse der Klausur werden am Freitag, den 05.10.2012, im Allianzgebäude am schwarzen Brett neben 4A-09 ausgehängt.</blockquote>
Das ist vermutlich im Allianzbau.

Die Klausureinsicht findet am Montag, den 15.10.2012 von 15:00 - 16:30 Uhr im Raum 1C-03 im Allianzgebäude statt.
