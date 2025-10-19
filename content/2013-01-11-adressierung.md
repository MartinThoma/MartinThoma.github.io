---
layout: post
title: Adressierung
slug: adressierung
lang: de
author: Martin Thoma
date: 2013-01-11 17:15:56.000000000 +01:00
category: German posts
tags: OS, Operating Systems, TLB, Cache
---
<div class="info">Dies ist eine Zusammenfassung von mir zu dem Themen Caches, Addressierung und TLB. Ich habe insbesondere bei dem letzem Teil (Cache-Typen und TLBs) das Gefühl, dass ich das noch nicht richtig verstanden habe, deshalb ist der Inhalt hier mit Vorsicht zu genießen. Bitte meldet mir Fehler oder Unstimmigkeiten (per E-Mail an info@martin-thoma.de oder direkt als Kommentar).</div>

## Allgemeines
CPU-Caches sind aus Cache-Zeilen aufgebaut. Diese sind die kleinsten adressierbaren Einheiten im Cache. Die Länge der Cache-Zeilen variiert, aber 32-64 Byte sind üblich.<small><sup><a href="#ref1" name="anchor1">[1]</a></sup></small> Nun ist der Cache deutlich kleiner als der Hauptspeicher und man muss eine schnelle Möglichkeit haben, Hauptspeicher-Adressen auf den Cache abzubilden.

Eine Möglichkeit das zu machen, ist ein sog. &bdquo;direct mapped
cache&ldquo;. Das ist im Prinzip eine Hash-Funktion, die zusätlich noch
schnell von der Hardware umgesetzt werden können muss. Also unterteilt man
gedanklich die Hauptspeicheradressen in 3 Teile:
<ul>
	<li>Tag</li>
	<li>Index</li>
	<li>Block-Offset</li>
</ul>

Der Index gibt direkt die Cache-Zeile an, in der die Daten einer
Hauptspeicheradresse landen werden. Es wäre also z.B. möglich, die
Pins des Adressbus, auf denen die Index-Bits liegen, auf einen Multiplexer zu
legen, der die entsprechende Cache-Zeile durchschaltet.

Es gilt also: Index-Länge in Bit = $\log_2(\text{Cache-Zeilen})$

Nun kann es passieren, dass viele Hauptspeicher-Adressen in der selben Zeile
landen. Um diese unterscheiden zu können, speichert man folgendes in einer
Cache-Zeile:
<ul>
	<li>Tag</li>
	<li>Datenblock</li>
	<li>Flags</li>
</ul>

Der Datenblock beinhaltet die eigentlichen Daten aus dem Hauptspeicher.
Benötigt nun ein Programm die Daten aus einer Hauptspeicheradresse, wird
der Index dieser Adresse extrahiert und an dieser Cache-Zeile nachgeschaut.
Wenn dann die Tags übereinstimmen, ist es die richtige Adresse und man
kann die Daten aus dem Cache entnehmen.

Da man durch den Block-Offset ja eine ganze Reihe von Hauptspeicher-Adressen
zusammenfasst, muss gelten:

Größe der Cache-Zeile $= 2^{\text{Länge des Block-offsets}} \cdot$
Größe des Inhalts einer Hauptspeicheradresse

Der Block-Offset wird nicht weiter verwendet. Es wird schlicht ignoriert.

Der Tag muss aktiv im Cache gespeichert werden und die Länge des Tags im
Cache muss mindestens so lang sein wie die Tag-Länge der Hauptspeicher-
Adresse. Natürlich wird der Tag im Cache genau so lang sein wie der in der
Hauptspeicher-Adresse. Man hat ja keinen Speicher zu verschenken.

Bei einem Voll-Assoziativem Cache würde es also keinen Index geben. Eine
Hauptspeicher-Adresse würde dann nur in Tag und Block-Offset geteilt
werden.

Bei einem $n$-fach Satzassoziativem Cache gibt es $\frac{\text{Cachzeilen}}{n}$ Sätze mit jeweils $n$ Cachezeilen. Das Datenwort kann nur in einem Satz stehen, dort aber an einer beliebigen Stelle. Nun geht die CPU wie folgt vor:

<ol>
	<li>Datenwort mit Hauptspeicheradresse x = $x_\text{tag}$ | $x_\text{index}$ | $x_\text{blockoffset}$ wird benötigt</li>
	<li>$x_\text{index}$ = der zu durchsuchende Satz im Cache<br/>
	Dieser Satz wird zu den $n$ Vergleichern durchgeschaltet</li>
	<li>Jeder Vergleicher vergleich den $x_\text{tag}$ und den in der Cache-Zeile gespeicherten tag</li>
	<li>Wird die Adresse gefunden &rarr; Cache Hit<br/>
	Datenwort in keiner Cache-Zeile: Cache-Miss, Hauptspeicherzugriff</li>
</ol>

<h2>Physical address and virtual address</h2>
Die physische Adresse entspricht dem, womit man den Speicherbaustein anspricht. Nun kann es möglich sein, dass man mehrere RAM-Bausteine hat oder dass das Programm theoretische mehr Speicher braucht als an Hauptspeicher zur verfügung steht. Dennoch will man als Programmierer einheitlich adressieren. Also nutzt man im Userspace virtuelle Adressen (Im Kernel-Space können sowohl physische als auch virtuelle Adressen genutzt werden, siehe <a href="http://stackoverflow.com/a/6261020/562769">StackOverflow</a>). Außerdem will man Speicherschutz herstellen.
Die virtuellen Adressen sind scheinbar zusammenhängend und der Adressraum ist sehr groß. Der virtuelle Adressraum ist in Blöcke (Pages) unterteilt und die Pages werden von langsamen, aber großen auf schnelle, aber kleine Speichermedien je nach Bedarf aus- oder eingelagert.

Das passiert allerdings selten. Um zu sehen, wie häufig das der Fall ist, sollte man sich folgendes anschauen:
<ul>
  <li>/proc/swaps</li>
  <li>/proc/meminfo - ein paar <a href="http://www.centos.org/docs/5/html/5.2/Deployment_Guide/s2-proc-meminfo.html">Erklärungen zu meminfo</a></li>
  <li><code>vmstat -s</code></li>
</ul>

## Cache-Modelle
Fordert nun ein Prozess die Daten einer virtuellen Adresse an, kommt es nun auf die verschiedenen Cache-Modelle (PIPT, VIPT, VIVIT) an. Es gilt jedoch immer: Die CPU schaut im TLB nach, ob sie direkt erfahren kann, wo die Daten sind. Falls das nicht funktiniert, geht es wie folgt weiter:

### Physically Indexed, Physically Tagged
Hier wird der index und der tag aus der physischen Adresse gezogen. Damit muss zuerst die MMU die virtuelle Adresse in eine physische Adresse umwandeln, bevor man im Cache nachschauen kann.

### Virtually indexed, physically tagged
Man bekommt den Index aus der virtuellen Adresse, kann im Cache nachschauen ob dort überhaupt etwas steht, falls ja muss aber noch die MMU die physische Adresse nachschlagen damit man den tag überprüfen kann.

<div class="frage">Frage: Wieso steht in den Folien "No ambiguities"?<br/>Annahme: Wir haben eine virtuelle Adresse 123456789. Der Index sind die Ziffern [4,6] also 456. Nun wird das auf die physische Adresse 123456789 gemappt. Der Tag sind die Ziffern [1,3] also 123.<br/>Nun haben wir eine zweite virtuelle Adresse 000456000. Der index sind die Ziffern [4,6] also 456. Die zugehörige phyische Adresse sein 123000000. Der Tag sind die Ziffern [1,3] also 123.<br/>Nun müsste doch fehlerhaft ein Cache-Hit herauskommen, oder?</div>

### Physically Indexed / Virtually Tagged
Macht keinen Sinn, weil man Probleme wegen Doppeldeutigkeiten bekommen kann und man auf jeden Fall immer zuerst die MMU nutzen kann.

### Virtually Indexed / Virtually Tagged
Kein MMU-Zugriff benötigt, also schneller als die anderen Varianten. Birgt aber ein paar Probleme (Ambiguity, Alias)

## Quellen

 [^1]: <a href="http://alasir.com/articles/cache_principles/cache_line_tag_index.html">Functional Principles of Cache Memory</a>

<ul>
  <li><a href="http://people.cs.umass.edu/~emery/classes/cmpsci377/current/notes/lecture_15_vm.pdf">Page-Table Lookups</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Virtuelle_Adresse#Motivation">Virtuelle Adresse</a></li>
  <li><a href="http://en.wikipedia.org/wiki/CPU_cache">CPU cache</a></li>
  <li><a href="http://lwn.net/Articles/106177/">Four-level page tables</a></li>
  <li><a href="http://bottomupcs.sourceforge.net/csbu/x2816.htm">Linux Specifics: Address Space Layout</a></li>
  <li><a href="http://www.ecst.csuchico.edu/~hilzer/csci152/htm/EAT-TLB.htm">Some example assignments</a> (Memory access times, With and without TLBs)</li>
</ul>
