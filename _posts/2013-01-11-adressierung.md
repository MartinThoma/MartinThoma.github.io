---
layout: post
title: Adressierung
author: Martin Thoma
date: 2013-01-11 17:15:56.000000000 +01:00
categories:
- German posts
tags:
- OS
- Operating Systems
- TLB
- Cache
---
<div class="info">Dies ist eine Zusammenfassung von mir zu dem Themen Caches, Addressierung und TLB. Ich habe insbesondere bei dem letzem Teil (Cache-Typen und TLBs) das Gef&uuml;hl, dass ich das noch nicht richtig verstanden habe, deshalb ist der Inhalt hier mit Vorsicht zu genie&szlig;en. Bitte meldet mir Fehler oder Unstimmigkeiten (per Email an info@martin-thoma.de oder direkt als Kommentar).</div>

<h2>Allgemeines</h2>
CPU-Caches sind aus Cache-Zeilen aufgebaut. Diese sind die kleinsten adressierbaren Einheiten im Cache. Die L&auml;nge der Cache-Zeilen variiert, aber 32-64 Byte sind &uuml;blich.<small><sup><a href="#ref1" name="anchor1">[1]</a></sup></small> Nun ist der Cache deutlich kleiner als der Hauptspeicher und man muss eine schnelle M&ouml;glichkeit haben, Hauptspeicher-Adressen auf den Cache abzubilden. 

Eine M&ouml;glichkeit das zu machen, ist ein sog. &bdquo;direct mapped cache&ldquo;. Das ist im Prinzip eine Hash-Funktion, die zus&auml;tlich noch schnell von der Hardware umgesetzt werden k&ouml;nnen muss. Also unterteilt man gedanklich die Hauptspeicheradressen in 3 Teile:
<ul>
	<li>Tag</li>
	<li>Index</li>
	<li>Block-Offset</li>
</ul>

Der Index gibt direkt die Cache-Zeile an, in der die Daten einer Hauptspeicheradresse landen werden. Es w&auml;re also z.B. m&ouml;glich, die Pins des Adressbus, auf denen die Index-Bits liegen, auf einen Multiplexer zu legen, der die entsprechende Cache-Zeile durchschaltet.

Es gilt also: Index-L&auml;nge in Bit = $\log_2(\text{Cache-Zeilen})$

Nun kann es passieren, dass viele Hauptspeicher-Adressen in der selben Zeile landen. Um diese unterscheiden zu k&ouml;nnen, speichert man folgendes in einer Cache-Zeile:
<ul>
	<li>Tag</li>
	<li>Datenblock</li>
	<li>Flags</li>
</ul>

Der Datenblock beinhaltet die eigentlichen Daten aus dem Hauptspeicher. Ben&ouml;tigt nun ein Programm die Daten aus einer Hauptspeicheradresse, wird der Index dieser Adresse extrahiert und an dieser Cache-Zeile nachgeschaut. Wenn dann die Tags &uuml;bereinstimmen, ist es die richtige Adresse und man kann die Daten aus dem Cache entnehmen.

Da man durch den Block-Offset ja eine ganze Reihe von Hauptspeicher-Adressen zusammenfasst, muss gelten:

Gr&ouml;&szlig;e der Cache-Zeile $= 2^{\text{L&auml;nge des Block-offsets}} \cdot$ Gr&ouml;&szlig;e des Inhalts einer Hauptspeicheradresse

Der Block-Offset wird nicht weiter verwendet. Es wird schlicht ignoriert.

Der Tag muss aktiv im Cache gespeichert werden und die L&auml;nge des Tags im Cache muss mindestens so lang sein wie die Tag-L&auml;nge der Hauptspeicher-Adresse. Nat&uuml;rlich wird der Tag im Cache genau so lang sein wie der in der Hauptspeicher-Adresse. Man hat ja keinen Speicher zu verschenken.

Bei einem Voll-Assoziativem Cache w&uuml;rde es also keinen Index geben. Eine Hauptspeicher-Adresse w&uuml;rde dann nur in Tag und Block-Offset geteilt werden.

Bei einem $n$-fach Satzassoziativem Cache gibt es $\frac{\text{Cachzeilen}}{n}$ S&auml;tze mit jeweils $n$ Cachezeilen. Das Datenwort kann nur in einem Satz stehen, dort aber an einer beliebigen Stelle. Nun geht die CPU wie folgt vor:

<ol>
	<li>Datenwort mit Hauptspeicheradresse x = $x_\text{tag}$ | $x_\text{index}$ | $x_\text{blockoffset}$ wird ben&ouml;tigt</li>
	<li>$x_\text{index}$ = der zu durchsuchende Satz im Cache<br/>
	Dieser Satz wird zu den $n$ Vergleichern durchgeschaltet</li>
	<li>Jeder Vergleicher vergleich den $x_\text{tag}$ und den in der Cache-Zeile gespeicherten tag</li>
	<li>Wird die Adresse gefunden &rarr; Cache Hit<br/>
	Datenwort in keiner Cache-Zeile: Cache-Miss, Hauptspeicherzugriff</li>
</ol>

<h2>Physical address and virtual address</h2>
Die physische Adresse entspricht dem, womit man den Speicherbaustein anspricht. Nun kann es m&ouml;glich sein, dass man mehrere RAM-Bausteine hat oder dass das Programm theoretische mehr Speicher braucht als an Hauptspeicher zur verf&uuml;gung steht. Dennoch will man als Programmierer einheitlich adressieren. Also nutzt man im Userspace virtuelle Adressen (Im Kernel-Space k&ouml;nnen sowohl physische als auch virtuelle Adressen genutzt werden, siehe <a href="http://stackoverflow.com/a/6261020/562769">StackOverflow</a>). Au&szlig;erdem will man Speicherschutz herstellen.
Die virtuellen Adressen sind scheinbar zusammenh&auml;ngend und der Adressraum ist sehr gro&szlig;. Der virtuelle Adressraum ist in Bl&ouml;cke (Pages) unterteilt und die Pages werden von langsamen, aber gro&szlig;en auf schnelle, aber kleine Speichermedien je nach Bedarf aus- oder eingelagert.

Das passiert allerdings selten. Um zu sehen, wie h&auml;ufig das der Fall ist, sollte man sich folgendes anschauen:
<ul>
  <li>/proc/swaps</li>
  <li>/proc/meminfo - ein paar <a href="http://www.centos.org/docs/5/html/5.2/Deployment_Guide/s2-proc-meminfo.html">Erkl&auml;rungen zu meminfo</a></li>
  <li><code>vmstat -s</code></li>
</ul>

<h2>Cache-Modelle</h2>
Fordert nun ein Prozess die Daten einer virtuellen Adresse an, kommt es nun auf die verschiedenen Cache-Modelle (PIPT, VIPT, VIVIT) an. Es gilt jedoch immer: Die CPU schaut im TLB nach, ob sie direkt erfahren kann, wo die Daten sind. Falls das nicht funktiniert, geht es wie folgt weiter:

<h3>Physically Indexed, Physically Tagged</h3>
Hier wird der index und der tag aus der physischen Adresse gezogen. Damit muss zuerst die MMU die virtuelle Adresse in eine physische Adresse umwandeln, bevor man im Cache nachschauen kann.

<h3>Virtually indexed, physically tagged</h3>
Man bekommt den Index aus der virtuellen Adresse, kann im Cache nachschauen ob dort &uuml;berhaupt etwas steht, falls ja muss aber noch die MMU die physische Adresse nachschlagen damit man den tag &uuml;berpr&uuml;fen kann.

<div class="frage">Frage: Wieso steht in den Folien "No ambiguities"?
Annahme: Wir haben eine virtuelle Adresse 123456789. Der Index sind die Ziffern [4,6] also 456
Nun wird das auf die physische Adresse 123456789 gemappt. Der Tag sind die Ziffern [1,3] also 123
Nun haben wir eine zweite virtuelle Adresse 000456000. Der index sind die Ziffern [4,6] also 456
Die zugeh&ouml;rige phyische Adresse sein 123000000. Der Tag sind die Ziffern [1,3] also 123
Nun m&uuml;sste doch fehlerhaft ein Cache-Hit herauskommen, oder?</div>

<h3>Physically Indexed / Virtually Tagged</h3>
Macht keinen Sinn, weil man Probleme wegen Doppeldeutigkeiten bekommen kann und man auf jeden Fall immer zuerst die MMU nutzen kann.

<h3>Virtually Indexed / Virtually Tagged</h3>
Kein MMU-Zugriff ben&ouml;tigt, also schneller als die anderen Varianten. Birgt aber ein paar Probleme (Ambiguity, Alias)

<h2>Quellen</h2>
1. <a name="ref1" href="#anchor1">&uarr;</a>: <a href="http://alasir.com/articles/cache_principles/cache_line_tag_index.html">Functional Principles of Cache Memory</a>

<ul>
  <li><a href="http://people.cs.umass.edu/~emery/classes/cmpsci377/current/notes/lecture_15_vm.pdf">Page-Table Lookups</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Virtuelle_Adresse#Motivation">Virtuelle Adresse</a></li>
  <li><a href="http://en.wikipedia.org/wiki/CPU_cache">CPU cache</a></li>
  <li><a href="http://lwn.net/Articles/106177/">Four-level page tables</a></li>
  <li><a href="http://bottomupcs.sourceforge.net/csbu/x2816.htm">Linux Specifics: Address Space Layout</a></li>
  <li><a href="http://www.ecst.csuchico.edu/~hilzer/csci152/htm/EAT-TLB.htm">Some example assignments</a> (Memory access times, With and without TLBs)</li>
</ul>
