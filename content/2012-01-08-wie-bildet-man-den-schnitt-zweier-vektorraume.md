---
layout: post
title: Wie bildet man den Schnitt zweier Vektorräume?
author: Martin Thoma
date: 2012-01-08 20:27:37.000000000 +01:00
category: German posts
tags: mathematics, Linear algebra
featured_image: 2012/01/vector-space.png
---
<h2>Angaben</h2>
Gegeben sind zwei Untervektorräume des $\mathbb{R}^4$:
$$U_1 := \left [\begin{pmatrix} 2 \\ 5 \\ 3 \\ 17 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}, \begin{pmatrix} 1 \\ 3 \\ 3 \\ 7 \end{pmatrix}, \begin{pmatrix} -1 \\ 1 \\ -1 \\ 1 \end{pmatrix} \right ]$$

$$U_2 := \left [\begin{pmatrix} 0 \\ 0 \\ 4 \\ 2 \end{pmatrix}, \begin{pmatrix} 3 \\ 1 \\ 4 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ 7 \\ 1 \\ 8 \end{pmatrix}, \begin{pmatrix} 36 \\ 126 \\ 8 \\ 139 \end{pmatrix} \right ]$$

<h2>Aufgabe</h2>
Finde eine Basis für $U_1 \cap U_2$.

Zusatzaufgabe: Finde eine Basis für $U_1 + U_2$.

<h2>Basis finden</h2>
Will man eine möglichst einfache Basis, also ein minimales Erzeugendensystem mit möglichst kleinen Zahlen zu einem gegebenem Vektorraum finden, so kann man das <a href="http://de.wikipedia.org/wiki/Gau%C3%9Fsches_Eliminationsverfahren">Gaußsche Eliminationsverfahren</a> auf die erzeugenden Vektoren anwenden. Dazu transponiert man die Vektoren:

$$\left( \begin{array}{c c c c | c}
  2 & 5 & 3 & 17 & 0\\
  1 & 2 & 3 & 4 & 0\\
  1 & 3 & 3 & 7 & 0\\
 -1 & 1 &-1 & 1 & 0
\end{array} \right)$$

Da im Gaußsche Eliminationsverfahren nur das Vertauschen von Zeilen, die Multiplikation einer Zeile mit einer Konstanten und die Addition von Zeilen zugelassen sind, bleibt die rechte Spalte immer Null. Sie kann also weggelassen werden:

$$\left( \begin{array}{c c c c}
  2 & 5 & 3 & 17\\
  1 & 2 & 3 & 4\\
  1 & 3 & 3 & 7\\
 -1 & 1 &-1 & 1
\end{array} \right) \rightsquigarrow
\left( \begin{array}{c c c c}
  1 &-1 & 1 &-1\\
  0 & 3 & 2 & 5\\
  0 & 4 & 2 & 8\\
  0 & 7 & 1 & 19
\end{array} \right) \rightsquigarrow
\left( \begin{array}{c c c c}
  1 &-1 & 1 &-1\\
  0 & 1 & \frac{1}{2} & 2\\
  0 & 0 & \frac{1}{2} & -1\\
  0 & 0 & -\frac{5}{2} & 5
\end{array} \right)  \rightsquigarrow
$$

$$\left( \begin{array}{c c c c}
  1 &-1 & 1 &-1\\
  0 & 1 & \frac{1}{2} & 2\\
  0 & 0 & 1 & -2\\
  0 & 0 & -5 & 10
\end{array} \right) \rightsquigarrow
\left( \begin{array}{c c c c}
  1 & 0 & 0 & 4\\
  0 & 1 & 0 & 3\\
  0 & 0 & 1 & -2\\
  0 & 0 & 0 & 0
\end{array} \right)$$

Die Basis für $U_1$ ist also $$\left \{\begin{pmatrix} 1 \\ 0 \\ 0 \\ 4 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 3 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ -2 \end{pmatrix} \right \}$$

Ich habe gerade keine Lust, das ganze für $U_2$ noch vorzurechnen. Es kommt
$$\left( \begin{array}{c c c c}
  1 & 0 & 0 & -\frac{29}{38}\\
  0 & 1 & 0 & \frac{49}{38}\\
  0 & 0 & 1 & \frac{1}{2}\\
  0 & 0 & 0 & 0
\end{array} \right)$$
heraus, siehe <a href="http://www.wolframalpha.com/input/?i=RowReduce%5B%7B%7B2%2C+7%2C+1%2C+8%7D%2C%7B3%2C+1%2C+4%2C+1%7D%2C%7B0%2C+0%2C+4%2C+2%7D%2C%7B36%2C+126%2C+8%2C+139%7D%7D%5D">Wolfram|Alpha</a>. 

Die Basis für $U_2$ ist also $$\left \{\begin{pmatrix} 1 \\ 0 \\ 0 \\ -\frac{29}{38} \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ \frac{49}{38} \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ \frac{1}{2} \end{pmatrix} \right \}$$

<h2>Zassenhaus-Algorithmus</h2>
Bemerkung: Ich habe für den Zassenhaus-Algorithmus leiter die falsche Basis genommen. Der Rechenfehler zieht sich bis zum Ende durch. Wenn ich mal Zeit habe, werde ich es korrigieren (Alternativ: Wenn es jemand von euch macht, kann er den TeX-Code ja als Kommentar bereitstellen).

Man transponiert die Basisvektoren von $U_1$ und $U_2$ und schreibt sie in eine Matrix:
$$\left( \begin{array}{c | c}
  U_1^T & U_1^T \\
  \hline
  U_2^T & 0
\end{array} \right)$$

Natürlich nimmt man für $U_1$ die einfachere der beiden Basen. Dann löst man das ganze wieder mit Gauß:

$$\left( \begin{array}{c c c c | c c c c}
  1 & 0 & 0 & 4 & 1 & 0 & 0 & 4 \\
  0 & 1 & 0 & 3 & 0 & 1 & 0 & 3 \\
  0 & 0 & 1 &-2 & 0 & 0 & 1 &-2 \\
  \hline
  1 & 0 & 0 & - \frac{29}{38} & 0 & 0 & 0 & 0 \\
  0 & 1 & 0 & \frac{49}{38} & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & \frac{1}{38} & 0 & 0 & 0 & 0
\end{array} \right) \rightsquigarrow 
\left( \begin{array}{c c c c | c c c c}
  1 & 0 & 0 & 4 & 1 & 0 & 0 & 4 \\
  0 & 1 & 0 & 3 & 0 & 1 & 0 & 3 \\
  0 & 0 & 1 &-2 & 0 & 0 & 1 &-2 \\
  \hline
  0 & 0 & 0 & - \frac{181}{38} & -1 & 0 & 0 & -4 \\
  0 & 0 & 0 & -  \frac{65}{38} & 0 & -1 & 0 & -3 \\
  0 & 0 & 0 & 1 & 0 & 0 & - \frac{38}{75} & \frac{76}{75}
\end{array} \right) \rightsquigarrow $$

$$\left( \begin{array}{c c c c | c c c c}
  1 & 0 & 0 & 4 & 1 & 0 & 0 & 4 \\
  0 & 1 & 0 & 3 & 0 & 1 & 0 & 3 \\
  0 & 0 & 1 &-2 & 0 & 0 & 1 &-2 \\
  0 & 0 & 0 & 1 & 0 & 0 & - \frac{38}{75} & \frac{76}{75} \\
  \hline
  0 & 0 & 0 & 0 & -1 & 0 & \frac{181}{75} & \frac{62}{75} \\
  0 & 0 & 0 & 0 & 0 & -1 & - \frac{13}{15} & \frac{26}{15}
\end{array} \right) \rightsquigarrow
\left( \begin{array}{c c c c | c c c c}
  1 & 0 & 0 & 4 & 1 & 0 & 0 & 4 \\
  0 & 1 & 0 & 3 & 0 & 1 & 0 & 3 \\
  0 & 0 & 1 &-2 & 0 & 0 & 1 &-2 \\
  0 & 0 & 0 & 1 & 0 & 0 & - \frac{38}{75} & \frac{76}{75} \\
  \hline
  0 & 0 & 0 & 0 & -1 & 0 & 181 & 62 \\
  0 & 0 & 0 & 0 & 0 & 1 &  13 & - 26
\end{array} \right)$$

Rechts unten steht nun die Basis für $U_1 \cap U_2 = \left [ \left \{ \begin{pmatrix} -1 \\ 0 \\ 181 \\ 62 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 13 \\ -26 \end{pmatrix}   \right \} \right ]$.
Zusätzlich steht links oben die Basis für $U_1 + U_2$. Wenn man das noch etwas umformt ist es die Standardbasis des $\mathbb{R}^4$.

<h2>Methode 2</h2>
<h3>Angabe</h3>
$$U_1 = \left [ 
\left \{\begin{pmatrix} 1 \\ 0 \\ 0 \\ 4 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 3 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ -2 \end{pmatrix} \right \}
\right ]$$

$$U_2 = \left [ 
\left \{\begin{pmatrix} 1 \\ 0 \\ 0 \\ -\frac{29}{38} \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ \frac{49}{38} \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ \frac{1}{38} \end{pmatrix} \right \}
\right ]$$

<h3>Rechnung</h3>
Es gilt:
$x \in U_1 \cap U_2$ 
$\Leftrightarrow x \in U_1 \land x \in U_2$ 
$\Leftrightarrow x = a \cdot x_1 + b \cdot x_2 + c \cdot x_3 = d \cdot y_1 + e \cdot y_2 + f \cdot y_3$ mit $a, b, c, d, e, f  \in \mathbb{R}$.
$$\begin{pmatrix}
1 & 0 & 0 & 1 & 0 & 0\\
0 & 1 & 0 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 0 & 1\\
4 & 3 & 2 & -\frac{29}{38} & \frac{49}{38} & \frac{1}{38}
\end{pmatrix} 
\rightsquigarrow 
\begin{pmatrix}
1 & 0 & 0 & 1 & 0 & 0\\
0 & 1 & 0 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 0 & 1\\
0 & 0 & 0 & -\frac{181}{38} & -\frac{65}{38} & -\frac{75}{38}
\end{pmatrix}$$
$$\rightsquigarrow  \begin{pmatrix}
1 & 0 & 0 & 1 & 0 & 0\\
0 & 1 & 0 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 0 & 1\\
0 & 0 & 0 & 1 & \frac{65}{181} & \frac{75}{181}
\end{pmatrix}
\rightsquigarrow
\begin{pmatrix}
1 & 0 & 0 & 0 & -\frac{65}{181} & -\frac{75}{181}\\
0 & 1 & 0 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 0 & 1\\
0 & 0 & 0 & 1 & \frac{65}{181} & \frac{75}{181}
\end{pmatrix}$$

Nun führt der $-1$ - Trick zu dieser Lösung:
$$\mathcal{L} = \left [ \left \{ \begin{pmatrix} -\frac{65}{181} \\ 1 \\ 0 \\ \frac{65}{181} \\ -1 \\ 0\end{pmatrix}, \begin{pmatrix} -\frac{75}{181} \\ 0 \\ 1 \\ \frac{75}{181} \\ 0 \\ -1 \end{pmatrix}   \right \} \right ] =
\left [ \left \{ \begin{pmatrix} -65 \\ 181 \\ 0 \\ 65 \\ -181 \\ 0\end{pmatrix}, \begin{pmatrix} -75 \\ 0 \\ 181 \\ 75 \\ 0 \\ -181 \end{pmatrix}   \right \} \right ]$$

Das ist also die Lösung für Belegungen von a, b, c, d, e, f, sodass der resultierende Vektor sowohl in $U_1$, als auch in $U_2$ ist.

Allerdings sieht es so aus, als hätte ich mich irgendwo verrechnet… Sieht jemand den Fehler?

<h2>Siehe auch</h2>
<a href="http://werkzeuge.wieschoo.com/zassenalgo.php">Interaktiver Zassenhaus-Algorithmus</a>
