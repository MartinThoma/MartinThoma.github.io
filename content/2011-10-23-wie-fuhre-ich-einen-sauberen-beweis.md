---
layout: post
title: Wie f&uuml;hre ich einen sauberen Beweis?
author: Martin Thoma
date: 2011-10-23 13:07:29.000000000 +02:00
category: German posts
tags: mathematics, lecture-notes, proof
featured_image: 2011/10/eulers-formula.png
---
In der Mathematik spielen Beweise eine zentrale Rolle. Es gibt verschiedene Beweisarten, aber im folgenden will ich nur einen direkten Beweis f&uuml;hren. Dieses Beispiel wurde in der &Uuml;bung zu Analysis I von Herrn Bolleyer gemacht.

<h2>Gliederung</h2>
Beweise kann man in drei Teile gliedern:

<strong>Voraussetzungen</strong>: Hier werden spezielle Objekte, die im Beweis ben&ouml;tigt werden, definiert.

<strong>Behauptung</strong>: Die Behauptung stellt eine Aussage &uuml;ber die Objekte in der Voraussetzung auf. Sie kann sehr kurz sein.

<strong>Beweis</strong>: Der Beweis zeigt durch eine folge von logischen Schlussfolgerungen aus den Voraussetzungen, dass die Behauptung wahr ist.

N&ouml;tig ist manchmal nur die Behauptung und der Beweis. Mit der Vorraussetzung ist der Beweis zwar vollst&auml;ndig, allerdings w&uuml;rde ich vor dem eigentlichem Beweis eine <strong>Beweisidee</strong> begr&uuml;&szlig;en. Die Beweisidee kann sehr kurz sein. Das ist der eine Satz, der einem Studenten, der sich mit der Aussage besch&auml;ftigt hat, sagt wie sie zu l&ouml;sen ist.

<h2>Beispiel eines direkten Beweises</h2>
<strong>Voraussetzung</strong>: Sei $M = \{ x \in \mathbb{R}: |x-3| \lt 2 \}$

<strong>Behauptung</strong>: $M = (1,5)$

<strong>Beweis</strong>: Per Definition gilt: $|x-3| : = 
\left \{ \begin{array}{ll}
x      & \text{, falls } x \geq 3 \\
-(x-3) & \text{, falls } x \lt 3
\end{array}
\right.$

$ M = \{x \in \mathbb{R} \lt 2 \} = \underbrace{\{x \in \mathbb{R} : |x-3| \lt 2 \land x \geq 3 \}}_{M_1} \cup \underbrace{\{x \in \mathbb{R}: |x -3| \lt 2 \land x \lt 3\}}_{M_2}$

Betrachte $M_1$:
$ x\in M_1 \Leftrightarrow |x-3| \lt 2 \land x \geq 3$
$\Leftrightarrow x-3 \lt 2 \land x \geq 3$
$\Leftrightarrow x \lt 5 \land x \geq 3$
$\Leftrightarrow 3 \leq x \lt 5$
Also gilt $M_1 = [3, 5)$

Betrachte $M_2$:
$ x\in M_2 \Leftrightarrow |x-3| \lt 2 \land x \lt 3$
$\Leftrightarrow -(x-3) \lt 2 \land x \lt 3$
$\Leftrightarrow -x + 3 \lt 2 \land x \lt 3$
$\Leftrightarrow 1 \lt x \land x \lt 3$
$\Leftrightarrow 1 \lt x \lt 3$
Also gilt $M_2 = (1,3)$

Es gilt $M = M_1 \cup M_2 = [3, 5) \cup (1,3) = (1,5)$
q.e.d.

<h2>Weitere Beweisformen</h2>
Der <a href="../wie-fuhre-ich-einen-induktionsbeweis/">Induktionsbeweis</a> ist sehr n&uuml;tzlich, wenn man eine Aussage f&uuml;r Elemente zeigen muss, die einen festen Abstand haben. Also z.B. eine Aussage f&uuml;r die Nat&uuml;rlichen Zahlen oder die ganzen Zahlen.

Der <a href="../pumping-lemma/">Widerspruchsbeweis</a> ist gut geeignet, wenn notwendige, aber nicht hinreichende Kriterien f&uuml;r das Gegenteil der Behauptung nicht erf&uuml;llt sind.

<h2>Siehe auch</h2>
<ul>
  <li>Wikipedia: <a href="http://de.wikipedia.org/wiki/Beweis_(Mathematik)">Beweis</a></li>
  <li><a href="http://mitschriebwiki.nomeata.de/WS07/Ana1.pdf">Inoffizielles Script</a></li>
</ul>
