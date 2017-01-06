---
layout: post
title: Wie berechnet man das charakteristische Polynom?
author: Martin Thoma
date: 2012-04-21 13:41:39.000000000 +02:00
category: German posts
tags: Wolfram|Alpha, mathematics, lecture-notes, Linear algebra
featured_image: 2012/04/determinante.png
---
Will man das charakteristische Polynom einer Abbildungsmatrix berechnen, so muss man zuerst sicher im Umgang mit Determinanten sein.

<h2>Rechenregeln f&uuml;r Determinanten</h2>
Man darf eine <strong>Zeile mit einer Konstanten a multiplizieren</strong>, muss dann aber die Determinante durch a teilen:
<a id="more"></a><a id="more-22721"></a>
$
det \begin{pmatrix}
3 & 2 & 12 & 5 \\ 
2 & 1 &  6 & 4 \\
2 & 0 &  2 & -3\\
2 & 2 &  7 & 4
\end{pmatrix}
\begin{array}{c} | \cdot 2 \\ | \cdot 3 \\ | \cdot 3 \\ | \cdot 3 \end{array}
 = \frac{1}{2} \cdot (\frac{1}{3})^3 \cdot
det \begin{pmatrix}
6 & 4 & 24 & 10 \\ 
6 & 3 & 18 & 12 \\
6 & 0 &  6 & -9\\
6 & 6 & 21 & 12
\end{pmatrix}
$

Man darf zwei <strong>Zeilen / Spalten tauschen</strong>, muss dann aber die Determinante mit (-1) multiplizieren:
$det \begin{pmatrix}
6 & 4 & 24 & 10 \\ 
6 & 3 & 18 & 12 \\
6 & 0 &  6 & -9\\
6 & 6 & 21 & 12
\end{pmatrix} \begin{array}{c} \cdot  \\  \cdot \\ \leftarrow \\ \leftarrow \end{array} = -
det \begin{pmatrix}
6 & 4 & 24 & 10 \\ 
6 & 3 & 18 & 12 \\
6 & 6 & 21 & 12 \\
6 & 0 &  6 & -9
\end{pmatrix} = 
det \begin{pmatrix}
6 & 24 & 4 & 10 \\ 
6 & 18 & 3 & 12 \\
6 & 21 & 6 & 12 \\
6 & 6  & 0 & -9
\end{pmatrix}$

Man darf eine <strong>Zeile mit einer Konstanten multiplizieren und auf eine beliebige <em>andere</em> Zeile addieren</strong> (wie beim Gauss-Verfahren)

Man darf eine <strong>Zeile und eine Spalte zugleich entfernen</strong> (Entwicklung nach Spalte / Zeile xy), muss dann aber folgenderma&szlig;en ausgleichen:
Entwicklung nach der k-ten Spalte: $D(a_1, ... , a_n) = \sum_{j=1}^{n}(-1)^{k+j}a_{jk}D_{jk}$
Entwicklung nach der i-ten Zeile: $det A = \sum_{k=1}^n (-1)^{i+k}a_{ik}D_{ik}$
Direkt entfernen, ohne etwas weiteres zu beachten, kann man die Zeile, wenn in dieser Zeile nur eine 1 steht und diese 1 an einer ungeraden Spalte (1, ..., n) ist.
Eine Spalte kann man direkt entfernen, wenn in der Spalte nur an einer Stelle eine 1 steht und diese 1 an einer ungeraden Zeile (1, ..., n) steht.

<h2>Berechnung des charakteristischen Polynoms</h2>
Das charakteristische Polynom einer Abbildungsmatrix A ist der Wert folgender Determinanten:
$det(\lambda \cdot E_n - A)$, wobei $E_n$ die Einheitsmatrix ist.

<h2>Beispiel</h2>
Siehe <a href="http://de.wikipedia.org/wiki/Charakteristisches_Polynom#Beispiel">Wikipedia</a>.

<h2>Berechnung am PC</h2>
Mit Wolfram|Alpha kann man das <a href="http://www.wolframalpha.com/widgets/view.jsp?id=27ddb8d522a2dc74e89687bd357db5a0">charakteristische Polynom</a> berechnen und auch direkt die <a href="http://www.wolframalpha.com/input/?i=Eigenvalues%7B%7B1%2C0%2C1%7D%2C%7B2%2C2%2C1%7D%2C%7B4%2C2%2C1%7D%7D">Eigenwerte</a>.

<h2>Wozu das Ganze?</h2>
An dem charakteristischem Polynom kann man direkt die Eigenwerte ablesen. Existiert eine Basis aus Eigenvektoren f&uuml;r den Vektorraum, dann ist eine Matrix diagonalsiierbar. Wenn eine Matrix in Diagonalform ist, dann kann man damit besonders gut rechnen.

<h2>Siehe auch</h2>
<ul>
  <li>Wikipedia: <a href="http://de.wikipedia.org/wiki/Determinante">Determinante</a>, <a href="http://de.wikipedia.org/wiki/Charakteristisches_Polynom">Charakteristisches Polynom</a>, <a href="http://de.wikipedia.org/wiki/Eigenwertproblem">Eigenwertproblem</a>, <a href="http://de.wikipedia.org/wiki/Diagonalmatrix">Diagonalmatrix</a></li>
  <li>Skript von Herrn Prof. Dr. Leuzinger, S. 131 - 142: Determinanten.</li>
</ul>
