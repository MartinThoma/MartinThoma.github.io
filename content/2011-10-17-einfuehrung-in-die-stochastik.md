---
layout: post
lang: de
title: Einf&uuml;hrung in die Stochastik
author: Martin Thoma
date: 2011-10-17 21:19:55.000000000 +02:00
category: German posts
tags: Visualization, mathematics, Stochastic, lecture-notes
---
In diesem Artikel werde ich ein paar einfache Definitionen, die f&uuml;r die Stochastik wichtig sind, einf&uuml;hren.
<h2>Basisdefinitionen bei Zufallsexperimenten</h2>
<strong>Was ist ein ideales Zufallsexperiment?</strong>
Ein ideales <a href="http://de.wikipedia.org/wiki/Zufallsexperiment">Zufallsexperiment</a> sollte
<ul>
    <li>gut beschrieben,</li>
    <li>wiederholbar und</li>
    <li>mit mehreren m&ouml;glichen Ausg&auml;ngen (also zuf&auml;llig),</li>
</ul>
sein.
Die Zufallsgr&ouml;&szlig;e, wie beispielsweise die erw&uuml;rfelte Zahl, nennt man <a href="http://de.wikipedia.org/wiki/Zufallsvariable">Zufallsvariable</a>. Es gibt auch noch die <a href="http://de.wikipedia.org/wiki/Statistische_Variable">Statistische Variable</a>. Wo der Unterschied ist, kann ich nicht sagen. Allerdings habe ich auf Wikipedia eine <a href="http://de.wikipedia.org/wiki/Diskussion:Statistische_Variable#Abgrenzung_Zufallsvariable_und_Statistische_Variable">Diskussion</a> ge&ouml;ffnet und hoffe auf baldige Kl&auml;rung.

<strong>Was sind Merkmale?</strong>
Merkmale sind die Ausg&auml;nge eines Zufallsexperiments. Sie k&ouml;nnen folgenderma&szlig;en gegliedert werden:
<ul>
  <li>quantitativ <small>(Die Zufallsgr&ouml;&szlig;e(n) haben nat&uuml;rlicherweise eine Ordnung)</small>
    <ul>
	<li>stetig <small>(Es k&ouml;nnen in einem Intervall beliebige Werte angenommen werden, z.B. die Gr&ouml;&szlig;e eines Menschen.)</small></li>
        <li>diskret <small>(Es k&ouml;nnen nur bestimmte Gr&ouml;&szlig;en angenommen werden, z.B. die Gr&ouml;&szlig;e eines Menschen in ganzen Zentimetern.)</small></li>
    </ul>
  </li>
  <li>qualitativ <small>(Es gibt keine nat&uuml;rliche Ordnung.)</small>
    <ul>
      <li>ordinal <small>(Es geht um Zahlengr&ouml;&szlig;en, z.B. Noten.)</small></li>
      <li>nominal <small>(Etwas v&ouml;llig anderes, z.B. Geschlecht.)</small></li>
    </ul>
  </li>
</ul>

<strong>Urliste / Stichprobe</strong> vom Umfang n: $x := (x_1, x_2, ..., x_n)$
$H_x (a_j) := \text{Anzahl der Stichprobenelemente in x, die gleich} a_j \text{sind}$
$H_x (a_j)$ : <strong>Absolute H&auml;ufigkeit</strong>
$h_x(a_j) := \frac{H_x (a_j)}{n}$ : <strong>Relative H&auml;ufigkeit</strong>
<strong>Empirische Verteilungsfunktion</strong>
$t \mapsto \underbrace{F_x(t)}_{\text{empirische Verteilungsfunktion}} := \sum \limits_{j: a_j \le t} {h_x (a_j)}, t \in \mathbb{R}$
Eine alternative Definition der <a href="http://de.wikipedia.org/wiki/Empirische_Verteilungsfunktion">empirischen Verteilungsfunktion</a> ist
$F_x(t) := \frac{1}{n} \sum \limits_{i=1}^n 1 \{ x_i \le t \}$

<strong>Arithmetisches Mittel</strong> ("Durchschnitt"): $\overline x = \frac{1}{n} \sum \limits_{i=1}^n x_i = \frac{x_1 + ... + x_n}{n}$
Welcher Wert liegt in der Mitte?

<strong>Stichproben-Varianz</strong>: $s_x^2 := \frac{1}{n-1} \sum \limits_{i = 1}^n (x_i - \overline x)^2$
<strong>Stichproben-Standardabweichung</strong>: $s_x := + \sqrt{s_x^2}$
Wie stark weichen die Werte von einander ab?

<strong>Stichproben-Variationskoeffizient</strong>: $v_x := \frac{s_x}{\overline x}$
Wie gro&szlig; ist die Schwankung relativ zum Durchschnitt?

<strong>Stichproben-Median / Zentralwert</strong>: W&uuml;rde mal alle Werte einer Stichprobe sortieren, sollte der Median der Wert in der Mitte sein. Das ist <em>nicht</em> der Durchschnitt!

$$\tilde x := \begin{cases} x_{\frac{n+1}{2}}, & \mbox{wenn }   n \mbox{ ungerade} \\
                                 \frac{1}{2} (x_\frac{n}{2} + x_{\frac{n}{2} + 1}), & \mbox{wenn } n \mbox{ gerade} \end{cases}$$

<strong>Quantil</strong>: Das $p$-Quantil unterteilt die Verteilung der Werte der Zufallsvariablen in zwei Bereiche: Links vom $p$-Quantil liegen $100 \cdot p$ Prozent aller Beobachtungswerte bzw. $100 \cdot p$ Prozent der Gesamtzahl der Zufallswerte. Rechts davon liegen $100 \cdot (1-p)$ Prozent aller Beobachtungswerte bzw. $100 \cdot (1-p)$ Prozent der Gesamtzahl der Zufallswerte.

Die Quartile sind die 0,25- und 0,75-Quantile.

$\alpha$-getrimmtes Stichprobenmittel: $\overline x_\alpha := \frac{1}{n-2k} \cdot (x_{n+1} + ... + x_{n-k})$
Spezialfall: $\overline x = \overline x_0$

Quartilsabstand: $\tilde x_{0,75} - \tilde x_{0,25}$
Spannweite: $x_n - x_1$

<h2>Visualisierungen</h2>
<figure class="aligncenter">
            <a href="../images/2011/10/boxplot-300x119.png"><img src="../images/2011/10/boxplot-300x119.png" alt="Boxplot" style="max-width:300px;max-height:119px" class="size-medium wp-image-5981"/></a>
            <figcaption class="text-center"><a href='http://de.wikipedia.org/wiki/Boxplot'>Boxplot</a></figcaption>
        </figure>

Weitere Visualisierungsm&ouml;glichkeiten:
<ul>
  <li>Punktwolke</li>
  <li><a href="http://de.wikipedia.org/wiki/Streudiagramm">Streudiagramm</a></li>
</ul>

<h2>Ann&auml;herungen</h2>
Durch eine <a href="http://de.wikipedia.org/wiki/Regressionsanalyse">Regressionsanalyse</a> kann man ein Regressionsmodell erstellen. Es legt den Typ einer Regressionsfunktion fest. Eine Regressionsfunktion kann z.B. die <a href="http://de.wikipedia.org/wiki/Regressionsfunktion">Methode der kleinsten Quadrate</a> sein:

$$\sum \limits_{j=1}^{n}\overbrace{(\underbrace{y_i -a -b \cdot x_j}_{\text{Residuum}})^2}^{
\begin{array}{l}
\text{Damit sich negative positive}\\
\text{Abweichungen nicht gegenseitig}\\
\text{aufheben}
\end{array}
}$$

<h3>Geradenparameter errechnen</h3>
Tja, hier hat er die Folien viel zu schnell durchgeschaltet ... ich habe nur folgendes:

Regressionsgerade: $y = a^* + b^* \cdot x$ (eindeutig bestimmbar)
$b^* = \frac{\sum \limits_{j=1}^n (x_j - \overline x) (y_j - \overline y)} {\sum \limits_{j = 1}^n (x_j - \overline x)^2}$

und $a^* = \overline y - b^* \cdot \overline x$

mit $r_{xy} = \frac{\frac{1}{n-1} \sum \limits_{j=1}^n (x_i - \overline x)(y_j - \overline y)}
{b_x \cdot b_y}$ (Korrelationskoeffizient der Daten)

gilt $b^* = r_{xy} \cdot \frac{s_y}{s_x}$

Irgendwas war noch mit der <a href="http://de.wikipedia.org/wiki/Cauchy-Schwarzsche_Ungleichung">Cauchy-Schwarz Ungleichung</a>.

Falls jemand Anmerkungen hat, mehr mitgeschrieben hat oder einfach Fragen aufkommen: Postet doch einen Kommentar!
