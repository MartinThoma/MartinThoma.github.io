---
layout: post
title: Sprachen, Automaten und Grammatiken: Ein Überblick
slug: sprachen-automaten-und-grammatiken
lang: de
author: Martin Thoma
date: 2012-01-28 10:52:34.000000000 +01:00
category: German posts
tags: Formal language, Abstract machine, Formal grammar, Chomsky hierarchy, Theoretical computer science, TGI
featured_image: 2011/10/deterministic-finite-state-machine-thumb.png
---
Die folgende Tabelle gibt einen Überblick über formale Sprachen, die Automaten die sie akzeptieren und die Grammatiken, die sie erzeugen. Dabei haben die Grammatiken die Form $G = (V, \Sigma, P, S)$:
<ul>
  <li>V: Die Menge der Nicht-Terminale. Für sie benutze ich Großbuchstaben.</li>
  <li>$\Sigma$: Die Menge der Terminale. Für sie benutze ich Kleinbuchstaben.</li>
  <li>P: Die Produktion, also die Regeln mit denen die Grammatik die Sprache erzeugt. Nur diese hat unterschiedliche Bedingungen, je nach dem welchem Typ die Grammatik angehört.</li>
  <li>S: Das Startsymbol aus $\Sigma$.</li>
</ul>

<table>
<tr>
<th rowspan="2">Typ</th>
<th rowspan="2">Bezeichnung</th>
<th rowspan="2">Regeln</th>
<th colspan="4">Abgeschlossen unter</th>
<th rowspan="2">Modell</th>
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
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:red;" title="No">&#10008;</span></td>
<td>D. <a href="http://de.wikipedia.org/wiki/Turingmaschine">Turingmaschine</a>, ND. Turingmaschine</td>
</tr>
<tr>
<td style="background-color:#90EE90;">1</td>
<td><a href="http://de.wikipedia.org/wiki/Kontextsensitive_Grammatik">kontextsensitiv</a></td>
<td>$u \rightarrow v, |a| \leq |v|$</td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td>(ND.?) Längenbeschränkter Automat</td>
</tr>
<tr>
<td style="background-color:#90EE90;">2</td>
<td><a href="http://de.wikipedia.org/wiki/Kontextfreie_Grammatik">kontextfrei</a></td>
<td>$A \rightarrow v$</td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:red;" title="No">&#10008;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:red;" title="No">&#10008;</span></td>
<td>ND. <a href="http://de.wikipedia.org/wiki/Kellerautomat">Kellerautomat</a></td>
</tr>
<tr>
<td style="background-color:#90EE90;">3</td>
<td><a href="http://de.wikipedia.org/wiki/Regul%C3%A4re_Grammatik">regulär</a></td>
<td>$A \rightarrow \varepsilon, A \rightarrow aB$</td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><span style="color:green;" title="Yes">&#10004;</span></td>
<td><a href="http://de.wikipedia.org/wiki/Endlicher_Automat">Endliche Automaten</a> (<a href="http://de.wikipedia.org/wiki/Moore-Automat">Moore</a>, <a href="http://de.wikipedia.org/wiki/Mealy-Automat">Mealy</a>, <a href="http://de.wikipedia.org/wiki/Akzeptor_(Informatik)">Akzeptoren</a>)</td>
</tr>
</table>

<strong>Legende:</strong>
Typ.: Der Typ der Grammatik in der <a href="http://de.wikipedia.org/wiki/Chomsky-Hierarchie">Chomsky-Hierarchie</a>
D.: "Deterministisch"
ND.: "Nicht Deterministisch"
<span style="background-color:#F08080;">semi-entscheidbar</span>
<span style="background-color:#90EE90;">entscheidbar</span>, es kann also in endlicher Zeit entschieden werden, ob ein Wort in der Sprache liegt (vgl. <a href="http://de.wikipedia.org/wiki/Wortproblem">Wortproblem</a>).
<br/>
<strong>Nicht-Abeschlossenheit der Kontextfreien Sprachen:</strong>
<span markdown="0">$$L_1 = \{a^jb^ic^i | j \in \mathbb{N}_0, i \in \mathbb{N}_0\}$$</span>
<span markdown="0">$$L_2 = \{a^ib^ic^j | j \in \mathbb{N}_0, i \in \mathbb{N}_0\}$$</span>
<span markdown="0">$$L_1 \cap L_2 = \{a^ib^ic^i | i \in \mathbb{N}_0\}$$</span>
<span markdown="0">$$(L_1 \cup L_2)^C = L_1^C \cap L_2^C$$</span>

<h2>Weitere Aussagen</h2>
Sei L eine Sprache.
$L \in {\cal L_3} \Leftrightarrow$ Es existiert ein regulärer Ausdruck für L.
$L \in {\cal L_3} \Leftrightarrow$ Die Anzahl der Äquivalenzklassen der <a href="http://de.wikipedia.org/wiki/Nerode-Relation">Nerode-Relation</a> bzgl. der Sprache ist endlich.
$L \in {\cal L_3} \Rightarrow$ Das <a href="../pumping-lemma/" title="Beweis durch Widerspruch: Eine Sprache ist nicht regulär (Pumping-Lemma)">Pumping-Lemma</a> ist erfüllt.

Für reguläre Sprachen ist das Leerheitsproblem ($L(G) \stackrel{?}{=} \emptyset$) entscheidbar.
Für reguläre Sprachen ist das Endlichkeitsproblem ($L(G) \stackrel{?}{<} \infty$) entscheidbar.

Für kontextfreie Sprachen ist das Leerheitsproblem entscheidbar.
Für kontextfreie Sprachen ist das Endlichkeitsproblem entscheidbar.

Für Typ 0 und Typ 1 Sprachen ist das Leerheitsproblem nicht entscheidbar.

$L \in {\cal L_2} \Leftrightarrow L$ wird von einem nichtdeterministischem Kellerautomaten erkannt.

<h2>Quellen</h2>
<ul>
    <li>Uwe Schöning: <i>Theoretische Informatik- kurz gefasst</i>. 5.&nbsp;Auflage. Spektrum Akademischer Verlag, Heidelberg <span style="white-space:nowrap;">2008</span>, ISBN 978-3-8274-1824-1, <span class="plainlinks-print"><a rel="nofollow" class="external text" href="http://d-nb.info/986529222">DNB 986529222</a></span>.</li>
    <li>Tutorium, Skript, Vorlesung: Theoretische Grundlagen der Informatik am KIT bei Prof. Dr. Dorothea Wagner</li>
</ul>
