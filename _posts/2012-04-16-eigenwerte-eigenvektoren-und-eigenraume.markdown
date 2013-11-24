---
layout: post
status: publish
published: true
title: Eigenwerte, Eigenvektoren und Eigenr&auml;ume
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 22311
wordpress_url: http://martin-thoma.com/?p=22311
date: 2012-04-16 08:15:32.000000000 +02:00
categories:
- German posts
tags:
- Linear algebra
- Eigenwert
- Eigenvektor
- Eigenraum
- Eigenwertproblem
comments:
- id: 110171
  author: Peter
  author_email: peter.merkert@gmx.de
  author_url: http://petermerkert.com
  date: !binary |-
    MjAxMi0wNC0xNiAwODozNDozNiArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNC0xNiAwNjozNDozNiArMDIwMA==
  content: Der 3. Satz (unter 'interessante S&auml;tze') ist etwas unklar. Muss diese
    Basis aus Eigenvektoren zu einem Eigenwert sein oder k&ouml;nnen dort Eigenvektoren
    gemixt werden?
- id: 110201
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wNC0xNiAwODo1NjozMSArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNC0xNiAwNjo1NjozMSArMDIwMA==
  content: ! "Hallo Peter,\r\n\r\ndie Eigenvektoren, die eine Basis von V bilden,
    k&ouml;nnen zu verschiedenen Eigenwerten geh&ouml;ren. Das kann man sich klar
    machen, indem man eine Abbildungsmatrix betrachtet, die bereits in Diagonalform
    ist (und somit offensichtlich diagonalisierbar ist). Siehe <a href=\"http://de.wikipedia.org/wiki/Diagonalisierbarkeit#Beispiel\"
    rel=\"nofollow\">Beispiel</a> auf Wikipedia."
---
<strong>Eigenwerte</strong> sind Elemente des K&ouml;rpers $\mathbb{K}$ zu einem Endomorphismus $\Phi:V \rightarrow V$, die folgende Eigenschaft erf&uuml;llen:
$\Phi(x) = \lambda x$ mit $x \in V$ und $x \neq 0$

Alle Vektoren x sind <strong>Eigenvektoren</strong> zu diesem Eigenwert.

Zusammen mit dem Null-Vektor bilden alle Eigenvektoren zu einem Eigenwert einer linearen Abbildung $\Phi$ einen <strong>Eigenraum</strong>. Diesen Eigenraum bezeichnet man mit $E_\lambda$.

<h2>Interessante S&auml;tze</h2>
<ul>
<li>$E_{\lambda_1} \cap E_{\lambda_2} = \emptyset$</li>
<li>Ein Endomorphismus $\Phi$ eines n-dimensionalen $\mathbb{K}$-Vektorraumes hat h&ouml;chstens n Eigenwerte.</li>
<li>Eine lineare Abbildung $\Phi$ ist genau dann diagonalisierbar, wenn es eine Basis von V aus Eigenvektoren gibt.</li>
<li>Wenn eine lineare Abbildung eines n-dimensionalen Vektorraums n verschiedene Eigenwerte hat, so ist sie diagonalisierbar.</li>
</ul>

<h2>Beispiele</h2>
<h3>Etwas einfaches</h3>
Sei $\Phi:\mathbb{R}^3 \rightarrow \mathbb{R}^3$ definiert durch $\Phi(x) := x $.
Dann ist $\lambda = 1$ der einzige Eigenwert. Der gesamte $\mathbb{R}^3 \setminus \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$ besteht ausschlie&szlig;lich aus Eigenvektoren zu diesem Eigenwert. Also ist der dazugeh&ouml;rige Eigenraum der gesamte $\mathbb{R}^3$.

<h3>Noch immer leicht</h3>
Sei $\Phi:\mathbb{R}^3 \rightarrow \mathbb{R}^3$ definiert durch $\Phi(x) := ax $ mit $a \in \mathbb{R} \setminus \{0\}$.
Dann ist $\lambda = a$ der einzige Eigenwert. Der gesamte $\mathbb{R}^3 \setminus \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$ besteht ausschlie&szlig;lich aus Eigenvektoren zu diesem Eigenwert. Also ist der dazugeh&ouml;rige Eigenraum der gesamte $\mathbb{R}^3$.

<h3>Etwas schwerer</h3>
Sei $\Phi:\mathbb{R}^3 \rightarrow \mathbb{R}^3$ definiert durch $\Phi(x) := \begin{pmatrix} 1 & 2 & 3\\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} x $.

Die Eigenwerte sind laut <a href="http://www.wolframalpha.com/input/?i=Eigenvalues+%7B%7B1%2C2%2C3%7D%2C%7B4%2C5%2C6%7D%2C%7B7%2C8%2C9%7D%7D">Wolfram|Alpha</a>:
$\lambda_1 = \frac{3}{2} (5+\sqrt{33})$, Eigenvektor: $v_1 = \begin{pmatrix}-\frac{13}{11}+\frac{1}{22} (15+3 \sqrt{33}) \\ -\frac{1}{11}+\frac{1}{44} (15+3 \sqrt{33}) \\ 1\end{pmatrix}$
$\lambda_2 = \frac{3}{2} (5-\sqrt{33})$, Eigenvektor: $v_2 = \begin{pmatrix}-\frac{13}{11}+\frac{1}{22} (15+3 \sqrt{33}) \\ -\frac{1}{11}+\frac{1}{44} (15-3 \sqrt{33}) \\ 1\end{pmatrix}$
$\lambda_3 = 0$, Eigenvektor: $v_3 = \begin{pmatrix}1 \\ -2 \\ 1\end{pmatrix}$ - der Kern von $\Phi$ (siehe <a href="http://www.wolframalpha.com/input/?i=NullSpace+%7B%7B1%2C2%2C3%7D%2C%7B4%2C5%2C6%7D%2C%7B7%2C8%2C9%7D%7D">Wolfram|Alpha</a>)

<h2>Wozu das Ganze?</h2>
Mit Eigenwerten (bzw. Vektoren) kann man &uuml;berpr&uuml;fen, ob eine lineare Abbildung diagonalisierbar ist. Eine lineare Abbildung in Form einer Diagonalmatrix ist besonders leicht zu berechnen. Es ist also w&uuml;nschenswert, die Abbildungsmatrix in Diagonalform zu bringen.

Kennt jemand noch weitere Gr&uuml;nde, warum Eigenwerte / Vektoren / R&auml;ume interessant sind?

<h2>Siehe auch</h2>
<ul>
  <li>Wikipedia: <a href="http://de.wikipedia.org/wiki/Eigenwertproblem">Eigenwertproblem</a></li>
  <li>Albrecht Beutelspacher: Lineare Algebra. 7 Auflage. Vieweg+Teubner Verlag, Wiesbaden 2010, ISBN 978-3-528-66508-1, S. 202-207.</li>
  <li>Enrico Leuzinger: Skript zur Linearen Algebra I. S. 143-147.</li>
</ul>
