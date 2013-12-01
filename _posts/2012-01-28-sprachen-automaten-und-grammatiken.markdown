---
layout: post
status: publish
published: true
title: ! 'Sprachen, Automaten und Grammatiken: Ein &Uuml;berblick'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 12901
wordpress_url: http://martin-thoma.com/?p=12901
date: 2012-01-28 10:52:34.000000000 +01:00
categories:
- German posts
tags:
- Formal language
- Abstract machine
- Formal grammar
- Chomsky hierarchy
- Theoretical computer science
- TGI
comments: []
---
Die folgende Tabelle gibt einen &Uuml;berblick &uuml;ber formale Sprachen, die Automaten die sie akzeptieren und die Grammatiken, die sie erzeugen. Dabei haben die Grammatiken die Form $G = (V, \Sigma, P, S)$:
<ul>
  <li>V: Die Menge der Nicht-Terminale. F&uuml;r sie benutze ich Gro&szlig;buchstaben.</li>
  <li>$\Sigma$: Die Menge der Terminale. F&uuml;r sie benutze ich Kleinbuchstaben.</li>
  <li>P: Die Produktion, also die Regeln mit denen die Grammatik die Sprache erzeugt. Nur diese hat unterschiedliche Bedingungen, je nach dem welchem Typ die Grammatik angeh&ouml;rt.</li>
  <li>S: Das Startsymbol aus $\Sigma$.</li>
</ul>

<table>
<tr>
<th rowspan="2">Typ</td>
<th rowspan="2">Bezeichnung</td>
<th rowspan="2">Regeln</td>
<th colspan="4">Abgeschlossen unter</td>
<th rowspan="2">Modell</td>
</tr>
<tr>
<th>$\cup$</th>
<th>$\cap$</th>
<th>$\cdot$</th>
<th>${}^C$</th>
</tr>
<tr>
<td style="background-color:#F08080;">0</td>
<td>semientscheidbar</td>
<td>alles</td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></td>
<td>D. <a href="http://de.wikipedia.org/wiki/Turingmaschine">Turingmaschine</a>, ND. Turingmaschine</td>
</tr>
<tr>
<td style="background-color:#90EE90;">1</td>
<td><a href="http://de.wikipedia.org/wiki/Kontextsensitive_Grammatik">kontextsensitiv</a></td>
<td>$u \rightarrow v, |a| \leq |v|$</td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td>(ND.?) L&auml;ngenbeschr&auml;nkter Automat</td>
</tr>
<tr>
<td style="background-color:#90EE90;">2</td>
<td><a href="http://de.wikipedia.org/wiki/Kontextfreie_Grammatik">kontextfrei</a></td>
<td>$A \rightarrow v$</td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></td>
<td>ND. <a href="http://de.wikipedia.org/wiki/Kellerautomat">Kellerautomat</a></td>
</tr>
<tr>
<td style="background-color:#90EE90;">3</td>
<td><a href="http://de.wikipedia.org/wiki/Regul%C3%A4re_Grammatik">regul&auml;r</a></td>
<td>$A \rightarrow \varepsilon, A \rightarrow aB$</td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
<td><a href="http://de.wikipedia.org/wiki/Endlicher_Automat">Endliche Automaten</a> (<a href="http://de.wikipedia.org/wiki/Moore-Automat">Moore</a>, <a href="http://de.wikipedia.org/wiki/Mealy-Automat">Mealy</a>, <a href="http://de.wikipedia.org/wiki/Akzeptor_(Informatik)">Akzeptoren</a>)</td>
</tr>
</table>

<strong>Legende:</strong>
Typ.: Der Typ der Grammatik in der <a href="http://de.wikipedia.org/wiki/Chomsky-Hierarchie">Chomsky-Hierarchie</a>
D.: "Deterministisch"
ND.: "Nicht Deterministisch"
<span style="background-color:#F08080;">semi-entscheidbar</span>
<span style="background-color:#90EE90;">entscheidbar</span>, es kann also in endlicher Zeit entschieden werden, ob ein Wort in der Sprache liegt (vgl. <a href="http://de.wikipedia.org/wiki/Wortproblem">Wortproblem</a>).

<strong>Nicht-Abeschlossenheit der Kontextfreien Sprachen:</strong>
$L_1 = \{a^jb^ic^i | j \in \mathbb{N}_0, i \in \mathbb{N}_0\}$
$L_2 = \{a^ib^ic^j | j \in \mathbb{N}_0, i \in \mathbb{N}_0\}$
$L_1 \cap L_2 = \{a^ib^ic^i | i \in \mathbb{N}_0\}$
$(L_1 \cup L_2)^C = L_1^C \cap L_2^C$

<h2>Weitere Aussagen</h2>
Sei L eine Sprache.
$L \in {\cal L_3} \Leftrightarrow$ Es existiert ein regul&auml;rer Ausdruck f&uuml;r L.
$L \in {\cal L_3} \Leftrightarrow$ Die Anzahl der &Auml;quivalenzklassen der <a href="http://de.wikipedia.org/wiki/Nerode-Relation">Nerode-Relation</a> bzgl. der Sprache ist endlich.
$L \in {\cal L_3} \Rightarrow$ Das <a href="http://martin-thoma.com/beweis-durch-widerspruch-eine-sprache-ist-nicht-regular-pumping-lemma/" title="Beweis durch Widerspruch: Eine Sprache ist nicht regul&auml;r (Pumping-Lemma)">Pumping-Lemma</a> ist erf&uuml;llt.

F&uuml;r regul&auml;re Sprachen ist das Leerheitsproblem ($L(G) \stackrel{?}{=} \emptyset$) entscheidbar.
F&uuml;r regul&auml;re Sprachen ist das Endlichkeitsproblem ($L(G) \stackrel{?}{<} \infty$) entscheidbar.

F&uuml;r kontextfreie Sprachen ist das Leerheitsproblem entscheidbar.
F&uuml;r kontextfreie Sprachen ist das Endlichkeitsproblem entscheidbar.

F&uuml;r Typ 0 und Typ 1 Sprachen ist das Leerheitsproblem nicht entscheidbar.

$L \in {\cal L_2} \Leftrightarrow L$ wird von einem nichtdeterministischem Kellerautomaten erkannt.

<h2>Quellen</h2>
<ul>
    <li>Uwe Sch&ouml;ning: <i>Theoretische Informatik- kurz gefasst</i>. 5.&nbsp;Auflage. Spektrum Akademischer Verlag, Heidelberg <span style="white-space:nowrap;">2008</span>, ISBN 978-3-8274-1824-1, <span class="plainlinks-print"><a rel="nofollow" class="external text" href="http://d-nb.info/986529222">DNB 986529222</a></span>.</li>
    <li>Tutorium, Skript, Vorlesung: Theoretische Grundlagen der Informatik am KIT bei Prof. Dr. Dorothea Wagner</li>
</ul>
