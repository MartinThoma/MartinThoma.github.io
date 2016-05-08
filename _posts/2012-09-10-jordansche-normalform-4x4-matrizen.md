---
layout: post
title: Jordansche Normalform: 4x4 Matrizen
author: Martin Thoma
date: 2012-09-10 11:28:08.000000000 +02:00
category: German posts
tags: mathematics, Linear algebra, Matrix
featured_image: 2012/08/jordan-normal-form-block1.png
---
<div class="info">Hier sind

\begin{align}
\dim \text{Eig}(-1) &= \dim \text{Kern}(A +1 \cdot I) \\
&= \dim \text{Kern} \begin{pmatrix}
2 & 2 & 47 & 11\\
3 & 3 &  8 & 15\\
0 & 0 &  4 &  1\\
0 & 0 &  8 & 2
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
1 & 1 & 1.5 &  0\\
1 & 1 & -3 & 13\\
0 & 0 &  1 &  \frac{1}{4}\\
0 & 0 &  0 & 0
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
1 & 1 & 1.5 &  0\\
0 & 0 & -4.5 & 13\\
0 & 0 &  1 &  \frac{1}{4}\\
0 & 0 &  0 & 0
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
1 & 1 & 1.5 &  0\\
0 & 0 &  0 & 14 \frac{1}{8}\\
0 & 0 &  1 &  \frac{1}{4}\\
0 & 0 &  0 & 0
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
1 & 1 &  0 & 0\\
0 & 0 &  0 & 0\\
0 & 0 &  1 & 0\\
0 & 0 &  0 & 1
\end{pmatrix} = \dim \left [ \begin{pmatrix}1\\-1\\0\\0 \end{pmatrix}\right ]\\
&= 1
\end{align}

Es gibt im Jordanblock zu \begin{align}
\dim \text{Eig}(1) &= \dim \text{Kern}(A-E)\\
 &= \dim \text{Kern }\begin{pmatrix}
-2 & -2 &  2 &  2\\
 2 & -1 &  1 &  1\\
 2 &  1 & -1 & -1\\
 0 & -2 &  2 &  0 \end{pmatrix}\\
 &= \dim \text{Kern }\begin{pmatrix}
 1 &  1 & -1 & -1\\
 0 & -3 &  3 &  3\\
 0 & -1 &  1 &  1\\
 0 &  1 & -1 &  0 \end{pmatrix}\\
 &= \dim \text{Kern }\begin{pmatrix}
 1 &  0 &  0 & -1\\
 0 &  1 & -1 &  0\\
 0 &  0 &  0 &  0\\
 0 &  0 &  0 &  1 \end{pmatrix}
\\
 &= \dim \left [\begin{pmatrix}0\\1\\1\\0\end{pmatrix} \right ] = 1
\end{align}J_B = 
\begin{pmatrix}
-1 &  0 & 0 & 0\\
 0 & -1 & 0 & 0\\
 0 &  0 & 1 & 1\\
 0 &  0 & 0 & 1
\end{pmatrix}\begin{align}
K_2(1) &= \text{Kern}(\Omega(1)^2) \\
       &= \text{Kern }\begin{pmatrix}
-2 & -2 &  2 &  2\\
 2 & -1 &  1 &  1\\
 2 &  1 & -1 & -1\\
 0 & -2 &  2 &  0 \end{pmatrix}^2 \\
       &= \text{Kern }\begin{pmatrix}
 4 &  4 & -4 & -4\\
-4 &  0 &  0 &  4\\
-4 & -4 &  4 &  4\\
 0 &  4 & -4 &  0 \end{pmatrix}\\
       &= \text{Kern }\begin{pmatrix}\\
 1 &  0 &  0 & -1\\
 0 &  1 & -1 &  0\\
 0 &  0 &  0 &  0\\
 0 &  0 &  0 &  0 \end{pmatrix} \\
       &= \left [ \begin{pmatrix}0\\1\\1\\0\end{pmatrix}, \begin{pmatrix}1\\0\\0\\1\end{pmatrix} \right ]
\end{align}K_2(1)\begin{align}
\Omega &= \begin{pmatrix}
0  &  0 & -1 & -1\\
-1 & -1 &  0 &  0\\
 0 &  0 &  1 &  1\\
 1 &  1 &  0 &  0
\end{pmatrix}\\
\Omega^2 &= \begin{pmatrix}
-1 & -1 & -1 & -1\\
 1 &  1 &  1 &  1\\
 1 &  1 &  1 &  1\\
-1 & -1 & -1 & -1
\end{pmatrix}\\
\Omega^3 &= \begin{pmatrix}
 0 & 0 & 0 & 0\\
 0 & 0 & 0 & 0\\
 0 & 0 & 0 & 0\\
 0 & 0 & 0 & 0
\end{pmatrix}
\end{align}.

\begin{align}
  \text{Eig}(1) &= K_1(1) = \text{Kern}(\Omega) \\
  &= \text{Kern} \begin{pmatrix}
     1 & 1 & 0 & 0\\
     0 & 0 & 0 & 0\\
     0 & 0 & 1 & 1\\
     0 & 0 & 0 & 0
   \end{pmatrix}\\
  &= \left [ \begin{pmatrix}1\\-1\\0\\0\end{pmatrix}, \begin{pmatrix}0\\0\\1\\-1\end{pmatrix} \right ]
\end{align}
\begin{align}
  K_2(1) &= \text{Kern}(\Omega^2) \\
  &= \text{Kern} \begin{pmatrix}
     1 & 1 & 1 & 1\\
     0 & 0 & 0 & 0\\
     0 & 0 & 0 & 0\\
     0 & 0 & 0 & 0
   \end{pmatrix}\\
  &= \left [ \begin{pmatrix}1\\-1\\0\\0\end{pmatrix}, \begin{pmatrix}1\\0\\-1\\0\end{pmatrix}, \begin{pmatrix}1\\0\\0\\-1\end{pmatrix} \right ]\\
  K_3(1) &= \text{Kern}(\Omega^3) = \mathbb{R}^4\\
\end{align}K_3(1) = \mathbb{R}^4$ ist das gr&ouml;&szlig;te Jordank&auml;stchen von der Gr&ouml;&szlig;e 3. Damit ergibt sich folgende Jordannormalform:

$J = 
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 1 & 0\\
0 & 0 & 1 & 1\\
0 & 0 & 0 & 1
   \end{pmatrix}$

<h3>Basiswechselmatrix bestimmen</h3>
F&uuml;r jedes Jordank&auml;stchen der L&auml;nge $i$ muss nun 1 Vektor gew&auml;hlt werden und $i-1$ Vektoren m&uuml;ssen bestimmt werden. Daf&uuml;r muss $\Omega(\lambda) := C - \lambda \cdot E$ bestimmt werden. 

<strong>Eigenwert 1:</strong>
<strong>K&auml;stchengr&ouml;&szlig;e 3</strong>
$b_1 \in K_3(1) \land b_1 \notin K_2(1) \Rightarrow b_1 \in \left [ \begin{pmatrix}1\\0\\0\\0\end{pmatrix} \right ]$. W&auml;hle $b_1 = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}$.

$b_2 = \Omega(b_1) = \begin{pmatrix}0\\-1\\0\\1\end{pmatrix}$.

$b_3 = \Omega^2(b_1) = \Omega(b_2)= \begin{pmatrix}-1\\1\\1\\-1\end{pmatrix}$

<strong>K&auml;stchengr&ouml;&szlig;e 1</strong>
$b_4 = \begin{pmatrix}1\\-1\\0\\0\end{pmatrix}$

Das 1-er K&auml;stchen soll zuerst kommen, also muss $b_4$ zuerst in die Basiswechselmatrix.
Unsere gesuchte Matrix $S$ f&uuml;r die oben angegebene JNF ist also:
$S = \begin{pmatrix}
b_4 & b_3 & b_2 & b_1
\end{pmatrix} = \begin{pmatrix}
1  & -1 &  0 & 1\\
-1 &  1 & -1 & 0\\
 0 &  1 &  0 & 0\\
 0 & -1 &  1 & 0
\end{pmatrix} $

Nun sollte
$J = S^{-1} \cdot C \cdot S$ gelten. Also, Schritt f&uuml;r Schritt:

\begin{align}
S^{-1} \cdot C \cdot S &= \begin{pmatrix}
0 & -1 & 0 & -1\\
0 &  0 & 1 &  0\\
0 &  0 & 1 &  1\\
1 &  1 & 1 &  1
\end{pmatrix} \cdot \begin{pmatrix}
 1 & 0 & -1 & -1\\
-1 & 0 &  0 &  0\\
 0 & 0 &  2 &  1\\
 1 & 1 &  0 &  1
\end{pmatrix} \cdot 
\begin{pmatrix}
1  & -1 &  0 & 1\\
-1 &  1 & -1 & 0\\
 0 &  1 &  0 & 0\\
 0 & -1 &  1 & 0
\end{pmatrix}\\
&=
\begin{pmatrix}
0 & -1 & 0 & -1\\
0 &  0 & 2 &  1\\
1 &  1 & 2 &  2\\
1 &  1 & 1 &  1
\end{pmatrix} \cdot
\begin{pmatrix}
1  & -1 &  0 & 1\\
-1 &  1 & -1 & 0\\
 0 &  1 &  0 & 0\\
 0 & -1 &  1 & 0
\end{pmatrix}
\\
&= \begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 1 & 0\\
0 & 0 & 1 & 1\\
0 & 0 & 0 & 1
   \end{pmatrix}
\end{align}

<h3>Programmierung</h3>
Hier habe ich mal f&uuml;r Leute, die kein Python haben, als Kommentar das Ergebnis pr&auml;sentiert. Ich denke damit ist klar, welchen Einfluss die Reihenfolge der Basisvektoren hat.
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import numpy
from numpy import linalg
numpy.set_printoptions(precision=2, suppress=True, linewidth=120)
 
C  = [[1,0,-1,-1],[-1,0,0,0],[0,0,2,1],[1,1,0,1]]
C = numpy.matrix(C)
b1 = [1,0,0,0]
b2 = [0,-1,0,1]
b3 = [-1,1,1,-1]
b4 = [1,-1,0,0]

S = numpy.matrix([b4,b1,b2,b3]).transpose() # [[ 1  0  0  0]
print("4123")                               #  [ 0  1  0  0]
print(linalg.inv(S) * C * S)                #  [ 0  1  1  0]
                                            #  [ 0  0  1  1]]

S = numpy.matrix([b4,b1,b3,b2]).transpose() #[[ 1  0  0  0]
print("4132")                               # [ 0  1  0  0]
print(linalg.inv(S) * C * S)                # [ 0  0  1  1]
                                            # [ 0  1  0  1]]

S = numpy.matrix([b4,b2,b1,b3]).transpose() # [[ 1  0  0  0]
print("4213")                               #  [ 0  1  1  0]
print(linalg.inv(S) * C * S)                #  [ 0  0  1  0]
                                            #  [ 0  1  0  1]]

S = numpy.matrix([b4,b2,b3,b1]).transpose() # [[ 1  0  0  0]
print("4231")                               #  [ 0  1  0  1]
print(linalg.inv(S) * C * S)                #  [ 0  1  1  0]
                                            #  [ 0  0  0  1]]

S = numpy.matrix([b4,b3,b1,b2]).transpose() # [[ 1  0  0  0]
print("4312")                               #  [ 0  1  0  1]
print(linalg.inv(S) * C * S)                #  [ 0  0  1  0]
                                            #  [ 0  0  1  1]]

S = numpy.matrix([b4,b3,b2,b1]).transpose() # [[ 1  0  0  0]
print("4321")                               #  [ 0  1  1  0]
print(linalg.inv(S) * C * S)                #  [ 0  0  1  1]
                                            #  [ 0  0  0  1]]

S = numpy.matrix([b3,b2,b1,b4]).transpose() # [[ 1  1  0  0]
print("3214")                               #  [ 0  1  1  0]
print(linalg.inv(S) * C * S)                #  [ 0  0  1  0]
                                            #  [ 0  0  0  1]]

```
