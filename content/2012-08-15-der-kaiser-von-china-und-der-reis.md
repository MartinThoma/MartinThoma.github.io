---
layout: post
lang: de
title: Der Kaiser von China und der Reis
slug: der-kaiser-von-china-und-der-reis
author: Martin Thoma
date: 2012-08-15 17:00:54.000000000 +02:00
category: German posts
tags: mathematics, chess
featured_image: 2012/08/chess-thumbnail.png
---
<a href="../images/2012/08/chessboard-rice.png"><img src="../images/2012/08/chessboard-rice.png" alt="" title="Schachbrett mit Reis" width="191" height="128" class="alignright size-full wp-image-46151" /></a>
<h2>Aufgabenstellung</h2>
Der Kaiser von China spielt mit einem Bauern Schach. Nachdem er das Spiel verloren hat, ist der Kaiser gro&szlig;z&uuml;gig und will dem Bauern jeden Wunsch erf&uuml;llen. Der Bauer gibt sich bescheiden und verlangt f&uuml;r das erste Schachfeld ein Reiskorn, f&uuml;r das zweite zwei Reisk&ouml;rner, usw.

Allgemein formuliert verlangt er f&uuml;r jedes Schachfeld doppelt so viele Reisk&ouml;rner wie f&uuml;r das Vorhergehende.

Wieviel Reis muss der Kaiser von China abtreten?

<h2>L&ouml;sung</h2>
Ein Schachbrett hat $8 \cdot 8 = 64$ Felder. F&uuml;r das $i$-te Feld, $1 \le i \le 64$, muss der Kaiser $2^{i-1}$ Reisk&ouml;rner abgeben.
Insgesamt muss er also $\sum_{i=1}^{64} 2^{i-1}$ Reisk&ouml;rner abgeben.
Das sind $2^{64} - 1 = 18446744073709551615 \approx 1{,}84 \cdot 10^{19}$ Reisk&ouml;rner.

<h2>Beweis</h2>

<b>Behauptung: </b> $\sum_{i=1}^{n} 2^{i-1} = 2^n -1$

<b>Beweis:</b>

<b>Induktionsanfang:</b> Für $n=1$ gilt $\sum_{i=0}^{n-1} 2^i = 2^0 = 1 = 2^1 - 1$

<b>Induktionsvorraussetzung:</b> Sei $n \in \mathbb{N}_{\geq 1}$ beliebig, aber fest und es gelte $\sum_{i=1}^{n} 2^{i-1} = 2^n -1$.

<b>Induktionsschluss</b>:

\begin{align}
\sum_{i=1}^{n+1} 2^{i-1} &= \sum_{i=0}^{n} 2^i\\
&= 2^n + \sum_{i=0}^{n-1} 2^i\\
&\stackrel{IV}{=} 2^n + (2^n -1)\\
&=2 \cdot 2^n - 1\\
&= 2^{n+1} - 1
\end{align}

<h2>Vergleiche</h2>
Wie viel sind 18.446.744.073.709.551.615 Reisk&ouml;rner?

<h3>Erdabdeckung</h3>
W&uuml;rde man die Erde gleichm&auml;&szlig;ig mit Reisk&ouml;rnern abdecken, wie hoch w&auml;re diese Schicht?

Die Erde hat eine Oberfl&auml;che von ca. 510 Millionen $\text{km}^2$, ein Basmati-Reiskorn ist ca 6,5 mm lang, hat einen Durchmesser von ca. 1,5 mm und hat vereinfacht eine Kreiszylinderform.

Daraus ergibt sich folgende Gleichung, bei der $x$ die H&ouml;he der Reisschicht ist:

\begin{align}
    x \cdot A_{Erde} &= (2^{64}-1) \cdot 6,5\text{mm} \cdot (1,5\text{mm})^2 \cdot \pi \\
    x &= \frac{(2^{64}-1) \cdot 6,5\text{mm} \cdot (1,5\text{mm})^2 \cdot \pi}{A_{Erde}} \\
    x &= \frac{(2^{64}-1) \cdot 45,9458\text{mm}^3}{510 \cdot 10^6 \cdot 10^{12} \text{mm}^2} \\
    x &= \frac{8,47550 \cdot 10^{20} \text{mm}^3}{510 \cdot 10^{18} \text{mm}^2} \\
    x &= 1,662\text{mm}
\end{align}

Die Erde k&ouml;nnte also komplett mit ca. 1,662 mm Reis, also etwas mehr als einem Reiskorn, bedeckt werden.

<h3>Reispackungen</h3>
Den vorhergehenden Vergleich finde ich noch etwas unpraktisch. Wieviele Reispackungen w&auml;ren das?

Eine handels&uuml;bliche Packung Reis beinhaltet ca. 1 kg Reis. Ein Reiskorn wiegt ca. 65 mg.

\begin{align}
    x &:= \text{Reispackungen} \\
    x \cdot 1\text{kg}     &= 65\text{mg} \cdot (2^{64}-1) \\
    x \cdot 10^6\text{mg} &= 1199038364791120854975\text{mg} \\
    x &\approx 1,2 \cdot 10^{15}
\end{align}

<h3>Reispackungen pro Person</h3>
Auch $1,2 \cdot 10^{15}$ ist noch zu gro&szlig;, um sich etwas darunter vorstellen zu k&ouml;nnen.
Wie viele Reispackungen w&auml;ren das pro Person auf der Erde?

\begin{align}
    x &:= \text{Reispackungen pro Mensch} \\
    x &= \frac{1,2 \cdot 10^{15}}{6,93 \cdot 10^9} \\
    x &\approx 1,7 \cdot 10^5
\end{align}

Jeder Mensch w&uuml;rde also 170.000 Packungen Reis von Kaiser von China bekommen. Um den t&auml;glichen Kalorienbedarf zu decken werden ca. 1,1 kg Reis ben&ouml;tigt. Es k&ouml;nnten also alle Menschen der Erde ca. 154.545 Tage, das sind &uuml;ber 423 Jahre, ern&auml;hrt werden!

<h3>Marktwert</h3>
Reis kostet auf dem Weltmarkt ca. 600 US-Dollar pro metrischer Tonne (<a href="http://www.markt-daten.de/charts/imf/imf014.htm">Quelle</a>).

\begin{align}
    x &:= \text{Marktwert} \\
    x &= \frac{1,2 \cdot 10^{15}}{1000} \cdot 600 \text{ US-Dollar}\\
    x &= 720000000000000
\end{align}

Der Reis h&auml;tte also einen Marktwert von 720 Billionen US-Dollar.

Zum Vergleich: Das BIP der gesamten Welt, also die Summe der Werte aller G&uuml;ter und Dienstleistung, lag 2007 bei ca. 54 Billionen US-Dollar (<a href="http://www.bpb.de/wissen/I6PFEV,0,WeltBruttoinlandsprodukt.html">Quelle</a>).
