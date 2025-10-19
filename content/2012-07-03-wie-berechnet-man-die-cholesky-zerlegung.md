---
layout: post
title: Wie berechnet man die Cholesky-Zerlegung?
slug: wie-berechnet-man-die-cholesky-zerlegung
lang: de
author: Martin Thoma
date: 2012-07-03 19:09:22.000000000 +02:00
category: German posts
tags: Python, Wolfram|Alpha, mathematics, Linear algebra, NumPy
featured_image: 2012/01/vector-space.png
---
Sei $A \in \mathbb{R}^{n \times n}$ eine symmetrische, positiv definite Matrix. Dann existiert eine Zerlegung $A = S \cdot D \cdot S^T$, wobei $S$ eine <a href="http://de.wikipedia.org/wiki/Dreiecksmatrix#Unipotente_Dreiecksmatrizen">unipotente Dreiecksmatrix</a> ist und D eine positiv definite Diagonalmatrix.

<h2>Berechnung der Cholesky-Zerlegung</h2>
Hier ein paar Ausschnitte, aus der englischen Wikipedia:

Einfach von links oben nach rechts unten die Werte nach folgender Formel berechnen:
$D_j = A_{jj} - \sum_{k=1}^{j-1} S_{jk}^2 D_k$
$S_{ij} = \frac{1}{D_j} \left( A_{ij} - \sum_{k=1}^{j-1} S_{ik} S_{jk} D_k \right), \qquad\text{for } i>j$


<h2>Programmierer-Hinweise</h2>
<h3>Implementierung</h3>
Eine Python-Implementierung sieht so aus:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getSD(A):
    """ @param A: eine quadratische, reele, positiv definite Matrix
        @return: Die Matrizen S und D, für die gilt:
                 A = S * D * S^T
    """
    n = len(A)
    S = [[0 for j in range(n)] for i in range(n)]
    D = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        S[i][i] = 1.0

    for j in range(n):
        _summe = sum(S[j][k] ** 2 * D[k][k] for k in range(j))
        D[j][j] = A[j][j] - _summe
        _summe = sum(S[i][k] * S[j][k] * D[k][k] for k in range(j))
        S[i][j] = 1.0 / D[j][j] * (A[i][j] - _summe)
    return S, D
```

<h3>Bibliotheken</h3>
Ich habe mich mal nach Bibliotheken umgesehen, die die Cholesky-Zerlegung direkt beherrschen. NumPy kann es natürlich:
```python
from numpy import linalg

print(linalg.cholesky([[5, 1], [1, 1]]))
```
Gibt aus:
```bash
array([[ 2.23606798,  0.        ],
       [ 0.4472136 ,  0.89442719]])
```

Das ist NICHT die Zerlegung $A = S \cdot D \cdot S^T$, sondern $A = G \cdot G^T$.

Interessanterweise hat NumPy das nicht direkt selbst implementiert (<a href="https://github.com/numpy/numpy/blob/master/numpy/linalg/linalg.py#L448">NumPy-Quelle</a>). Man greift auf <a href="http://de.wikipedia.org/wiki/LAPACK">LAPACK</a> zurück, was in FORTRAN 90 programmiert wurde (<a href="http://www.netlib.org/lapack/double/dpotrf.f">LAPACK-Quelle</a>)!

<h3>Wolfram|Alpha</h3>
Auch Wolfram|Alpha kennt "cholesky decomposition": <a href="http://www.wolframalpha.com/input/?i=cholesky+decomposition+%7B%7B5%2C2%7D%2C%7B2%2C1%7D%7D">Beispiel</a>. Allerdings sieht es schon bei $3 \times 3$-Matrizen schlecht aus.

<h2>Numerik</h2>
In Numerik haben wir bei Herrn Dr. Weiß folgendes als Cholesky-Zerlegung kennen gelernt:

Sei $A \in \mathbb{R}^{n \times n}$ eine symmetrische, positiv definite Matrix. Dann existiert eine Zerlegung $A = \bar L \cdot \bar{L}^T$, wobei $\bar L$ eine untere Dreiecksmatrix ist.

Wenn man wie gewohnt eine LR-Zerlegung der Matrix $A$ durchführt, erhält man zwei Matrizen $L, R \in \mathbb{R}^{n \times n}$, wobei gilt: $R = D \cdot L^T$, wobei $D$ eine positiv definite Diagonalmatrix ist.

Offensichtlich gilt: $\bar L = L \cdot D^{\frac{1}{2}}$.

Die Cholesky-Zerlegung kann man folgendermaßen berechnen:

<figure class="aligncenter">
            <a href="../images/2012/07/cholesky-zerlegung-numerik.png"><img src="../images/2012/07/cholesky-zerlegung-numerik.png" alt="Berechnung der Cholesky-Zerlegung in Pseudocode" style="max-width:512px;max-height:390px" class="size-full wp-image-67881"/></a>
            <figcaption class="text-center">Berechnung der Cholesky-Zerlegung in Pseudocode</figcaption>
        </figure>

In Python sieht das dann so aus:

```python
def getL(A):
    n = len(A)
    L = [[0 for i in range(n)] for j in range(n)]
    print(L)
    print("")

    for k in range(n):
        L[k][k] = (A[k][k] - sum([L[k][i] ** 2 for i in range(k)])) ** 0.5
        for i in range(k + 1, n):
            L[i][k] = (A[i][k] - sum([L[i][j] * L[k][j] for j in range(k)])) / L[k][k]
    return L
```

<h2>Siehe auch</h2>
<ul>
  <li><a href="http://en.wikipedia.org/wiki/Cholesky_decomposition">Cholesky decomposition</a> (Englisch)</li>
  <li><a href="http://de.wikipedia.org/wiki/Cholesky-Zerlegung">Cholesky-Zerlegung</a></li>
</ul>
