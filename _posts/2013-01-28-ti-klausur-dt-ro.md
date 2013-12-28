---
layout: post
status: publish
published: true
title: TI-Klausur (DT & RO)
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 55191
wordpress_url: http://martin-thoma.com/?p=55191
date: 2013-01-28 00:25:14.000000000 +01:00
categories:
- German posts
tags:
- Klausur
- Digitaltechnik
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Dieser Artikel besch&auml;ftigt sich mit der Vorlesungen &bdquo;Digitaltechnik und Entwurfsverfahren&ldquo; sowie &bdquo;Rechnerorganisation&ldquo; des Moduls &bdquo;Technische Informatik&ldquo; am KIT. Er dient als Pr&uuml;fungsvorbereitung. Ich habe die Vorlesungen bei Herrn Prof. Dr. Asfour geh&ouml;rt.</div>

<h2>Vorbereitung DT</h2>
<strong>Themen</strong>:
<ul>
  <li>Zahlensysteme: Horner-Schema, Euklidischer Algorithmus</li>
  <li>Zahlendarstellungen: Wie wandle ich eine Zahl von 10-er-System ins Zahlensystem xy um und umgekehrt?
   <ul>
    <li>Vorzeichen</li>
    <ul>
     <li>Betrag-Vorzeichen &rarr; <span class="hint" title="Erstes Bit ist 1, wenn die Zahl negativ ist. Sonst wird die Zahl einfach bin&auml;r dargestellt.">Antwort</span></li>
     <li>Einer-Komplement &rarr; <span class="hint" title="Betrag der Zahl dual darstellen, bits invertieren">Antwort</span></li>
     <li>Zweier-Komplement &rarr; <span class="hint" title="Wie Einer-Komplement, 1 addieren">Antwort</span></li>
     <li>Exzess-q &rarr; <span class="hint" title="Man fasst die durch Exzess-q dargestellte Zahl als Bin&auml;rzahl auf, addiert -q darauf und erh&auml;lt so die dargestellte Zahl">Antwort</span></li>
    </ul>
    </li>
    <li>Komma
     <ul>
       <li>Festkomma &rarr; <span class="hint" title="int, long, char">Beispiele</span></li>
       <li>Gleitkomma &rarr; <span class="hint" title="float, double">Beispiele</span> ($\pm \text{Mantisse} \cdot b^\text{Exponent}$)</li>
     </ul>
    </li>
    </ul>
  </li>
  <li>IEEE 754 Format
    <ul>
      <li><a href="http://martin-thoma.com/a-practical-approach-to-floats/">A practical approach to floats</a></li>
      <li>Wie wird NaN dargestellt? Wie wird $-\infty$ und $+\infty$ dargestellt?</li>
      <li>Was ist eine normalisierte Zahl, was eine denormalisierte?</li>
    </ul>
  </li>
  <li>Was ist <span class="hint" title="Alle Ziffern von 0-9 werden im 2er-System dargestellt.">BCD</span>, <span class="hint" title="Die Ziffern von 0-4 werden im 2er-System dargestellt. Dann geht es bei (B)_16 = 1011 weiter.">AIKEN</span> und <span class="hint" title="+3 auf jede Ziffer, dann wie BCD">STIBITZ</span>? Wie werden die Ziffern von 0 - 9 dort dargestellt?</li>
  <li>Was sind Hamming-Codes? &rarr; <a href="http://martin-thoma.com/error-correcting-codes/">Antwort</a></li>
  <li>Wie lauten die Huntingtonschen Axiome? &rarr; <a href="http://martin-thoma.com/beweise-aus-der-booleschen-algebra/">Antwort</a></li>
  <li>Nenne 3 verschiedene vollst&auml;ndige Operatorensysteme. &rarr; <span class="hint" title="(UND, ODER, NOT), (NAND), (NOR)">Antwort</span></li>
  <li>Was sind Primterme, Primimplikanten, Primimplikate, Minterme und Maxterme?</li>
  <li>Was sind DMF, DNF, KMF, KNF?</li>
  <li>Wie wende ich die Shannon-Zerlegung an? &rarr; <a href="http://martin-thoma.com/wie-wende-ich-die-shannon-zerlegung-an/">Antwort</a></li>
  <li>Wie minimiere ich Funktionen mit KV-Diagrammen?</li>
  <li>Wie funktioniert das Quine-McCluskey Verfahren? &rarr; <a href="http://martin-thoma.com/das-quine-mccluskey-verfahren/">Antwort</a></li>
  <li>Was macht das Consensus-Verfahren? &rarr; <a href="http://martin-thoma.com/das-consensus-verfahren/">Antwort</a></li>
  <li>Wie funktioniert das Nelson-Verfahren?</li>
  <li>Was bedeutet selbstleitend und selbstsperrend?</li>
  <li>Was ist <abbr title="metal-oxide-semiconductor field-effect transistor">MOSFET</abbr>? &rarr; <a href="http://commons.wikimedia.org/wiki/File:N-Kanal-MOSFET_(Schema).svg">Aufbau</a></li>
  <li><abbr title="Complementary Metal Oxide Semiconductor">CMOS</abbr>, N-MOS, P-MOS</li>
  <li>Was ist der Unterschied zwischen einem Hasard und einem Hasard-Fehler?</li>
  <li>Woran erkennt man Funktionshasards, woran Strukturhasards?</li>
  <li>Wie lauten die Ansteuertabellen von D-, T-, JK- und RS-Flipflops? &rarr; <a href="http://martin-thoma.com/flipflops-und-latches/">Antwort</a></li>
  <li>Was macht ein Carry-ripple-Addierer? &rarr; <span class="hint" title="Nutzt zur Addition zweier n-Stelliger Zahlen (n-1) Volladdierer und einen Halbaddierer.">Antwort</span></li>
  <li>Inwiefern stellt der Carry-lookahead-Addierer eine Verbesserung des Carry-ripple-Addierers dar? &rarr; <span class="hint" title="Der Carry-ripple-Addierer rechnet von dem LSB zu dem MSB Schritt f&uuml;r Schritt. Der Carry-Lookahead-Addierer versucht dies zu beschleunigen, indem er die &Uuml;bertr&auml;ge direkt aus den Eingangsvariablen berechnet.">Antwort</span></li>
  <li>Was macht man, wenn bei der Addition zweier BCD-Zahlen eine Pseudotetrade auftritt? &rarr; <span class="hint" title="6 auf die betroffene Tetrade addieren.">Antwort</span></li>
  <li>Was macht man, wenn bei der Addition zweier BCD-Zahlen ein &Uuml;bertrag in die n&auml;chste BCD-Ziffer auftritt? &rarr; <span class="hint" title="6 auf die Stelle addieren, die den &Uuml;bertrag auf die n&auml;chste Stelle verursachte.">Antwort</span></li>
  <li>Was macht man, wenn bei der Addition zweier BCD-Zahlen bei der Korrekturaddition ein &Uuml;bertrag auftrat? &rarr; <span class="hint" title="Nichts.">Antwort</span></li>
  <li>Was ist die PPS-Methode? &rarr; <span class="hint" title="Eine Multiplikationsmethode (Partial Product sum). Siehe DT-VL21.pdf">Antwort</span></li>
</ul>

<h2>Vorbereitung RO</h2>
<strong>Themen</strong>:
<ul>
  <li>Y-Diagramm</li>
  <li>Aufbau eines Mikroprozessors</li>
  <li>Umrechnen von Zahlensystemen</li>
  <li>RAM-Typen (DRAM, FPM-DRAM, EDO-RAM, SDRAM, DDRAM, DDR-SDRAM, RDRAM)</li>
  <li>Cache-Speicher</li>
</ul>

<strong>Begriffe</strong>
<ul>
  <li>Was sind Tristate-Treiber? &rarr; <span class="hint" title="Gatterform, die nicht nur Hi und Lo weiterleiten kann, sondern auch einen dritten, gegen Spannungen beider Polarit&auml;ten, hochohmigen Zustand haben k&ouml;nnen. Dadurch kann z.B. ein Baustein vom Bus abgetrennt werden. Sie dienen zum Abschalten des gleichzeitigen Zugriffs mehrerer Komponenten auf Systembusse.">Antwort</span></li>
  <li>Was ist der Unterschied zwischen <span class="hint" title="Symbolische Repr&auml;sentation der Maschinensprache, die f&uuml;r den Menschen verst&auml;ndlich und anschaulich ist, z.B. add $s2, $s1, $s0">Assembler</span>, <span class="hint" title="Repr&auml;sentation von Anweisungen, die f&uuml;r einen Mikroprozessor unmittelbar verst&auml;ndlich sind, z.B. 00000000110000100011000000100001">Maschinensprache</span> und Mikrobefehlen?</li>
  <li>Wof&uuml;r stehen RISC und CISC und was sind Beispiele? &rarr; <span class="hint" title="Reduced Instruction Set Computer (z.B. MIPS), Complex Instruction Set Computer (z.B. x86)">Antwort</span></li>
  <li>Was ist ein User/System Bit, was ein Trace Bit und was ein Decimal bit? &rarr; <span class="hint" title="Das User/System bit bestimmt, ob sich das System im eingeschr&auml;nkten User-Modus oder im uneingeschr&auml;nktem Systemmodus befindet. Das Trace Bit erlaubt Befehlsabarbeitung im Einzelschritt-Modus zum Debuggen und das Decimal Bit entscheidet, ob Dual oder BCD gerechnet wird.">Antwort</span></li>
  <li>Welche Informationen k&ouml;nnen im Statusregister des Rechnewerkes stehen? &rarr; <span class="hint" title="Carry, Overflow, Zero, Sign, ...">Antwort</span></li>
  <li>Welche Informationen k&ouml;nnen im Akkumulator stehen? &rarr; <span class="hint" title="alle ALU Ergebisse">Antwort</span></li>
  <li>Warum ben&ouml;tigt die ALU Hilfsregister? &rarr; <span class="hint" title="Ohne die Hilfsregister w&uuml;rden w&auml;hrend der ALU-Rechenzeit durch Hasards und Wettl&auml;ufe Schwankungen am Ausgang entstehen.">Antwort</span></li>
  <li>Entspricht das logische Rechtsschieben der Division durch zwei? &rarr; <span class="hint" title="Nein, da bei negativen Zahlen die 1 im MSB erhalten werden muss.">Antwort</span></li>
  <li>Was ist ein superskalarer Prozessor? &rarr; <span class="hint" title="Ein Prozessor, der pro Takt mehrere allgemeine Register schreiben und lesen kann.">Antwort</span></li>
  <li>Was ist ein little Endian und was ist big Endian? &rarr; <span class="hint" title="Das MSB bei little Endian ist ganz links, bei big Endian ganz rechts.">Antwort</span></li>
  <li>Was versteht man unter dem Nulladressformat? &rarr; <span class="hint" title="Die Befehlss&auml;tze, die nur aus dem Opcode bestehen. Das Einadressformat hat z.B. zus&auml;tzlich noch die Src.">Antwort</span></li>
  <li>Was ist eine &bdquo;effektive Adresse&ldquo;? &rarr; <span class="hint" title="Die Effektive Adresse ist die durch die Addressierungsart spezifizierte Adresse im Hauptspeicher. Sie entsteht im Prozessor nach Ausf&uuml;hrung der Adressierung.">Antwort</span></li>
  <li>Was bedeutet <span class="hint" title="Zero flag; Wichtig f&uuml;r Schleifen">ZF</span>, <span class="hint" title="Carry flag; set if an arithmetic operation generats a carry or a borrow out of the MSB of the result">CF</span>, <span class="hint" title="Sign flag; set equal to the MSB">SF</span>, <span class="hint" title="Overflow flag; set if the integer result is too large a positive number or too small a negative number to fit in the destination operand">OF</span> und wozu sind sie jeweils gut?</li>
  <li>Was ist eine Load/Store-Architektur? &rarr; <abbr title="Eine Load/Store Architektur ist eine Computerarchitektur, deren Befehlssatz Daten-Speicherzugriffe ausschlie&szlig;lich mit speziellen Lade- und Speicher-Befehlen erlaubt.">Antwort</abbr></li>
  <li>Was sind die f&uuml;nf Schritte in der DLX-Pipeline-Verarbeitung? &rarr; <abbr title="IF: Instruction fetch; ID/RF: Instruction decode/Register fetch; EX: Execute / address calculation; MEM: Memory access; WB: Write Back">Antwort</abbr></li>
  <li>In welcher Pipeline-Phase werden die Operanden aus dem memory geholt? &rarr; <abbr title="Tja, das war fies. Es ist nicht die MEM-Phase. In der MEM-Phase wird der Speicherzugriff von Lade- und Speicherbefehlen durchgef&uuml;hrt. Richtig ist: Die zweite Takth&auml;lfte der ID-Phase.">Antwort</abbr></li>
  <li>Durch welche Abh&auml;ngigkeiten entstehen Verz&ouml;gerungen in der DLX-Pipeline und wann treten diese auf? &rarr; <abbr title="Daten-, Struktur- und Steuerflussabh&auml;ngigkeiten. Datenabh&auml;ngigkeiten treten auf, wenn ein Operand noch nicht verf&uuml;gbar ist. Strukturkonflikte treten auf, wenn zwei Pipeline-Stufen dieselbe Ressource ben&ouml;tigen, auf diese aber nur einmal zugegriffen werden kann. Steuerflusskonflikte treten bei Programmsteuerbefehlen auf. Dies kann z.B. der Fall sein wenn in der Holphase die Zieladresse des als n&auml;chstes auszuf&uuml;hrenden Befehls noch nicht berechnet ist oder wenn bei einem bedingtem Sprung noch nicht klar ist, ob dieser &uuml;berhaupt umgesetzt werden wird.">Antwort</abbr></li>
  <li>Was ist eine echte Datenabh&auml;ngigkeit, was eine Gegenabh&auml;ngigkeit und was eine Ausgabeabh&auml;ngigkeit? &rarr; <abbr title="Echte Datenabh&auml;ngigkeit: a = b + c; d = a + e. Gegenabh&auml;ngigkeit: b = a + c; a = d + e. Ausgabeabh&auml;ngigkeit: a = b + c; a = d + e">Antwort</abbr></li>
  <li>Was ist eine falsche Abh&auml;ngigkeit? &rarr; <abbr title="Eine Gegen- oder Ausgabeabh&auml;ngigkeit.">Antwort</abbr></li>
  <li>Treten bei echten Abh&auml;ngigkeiten immer Konflikte auf? &rarr; <abbr title="Nein. Es k&ouml;nnen z.B. gen&uuml;gend Befehle zwischen den beiden Abh&auml;ngigen sein.">Antwort</abbr></li>
  <li>Welche Konflikte gibt es und wann k&ouml;nnen sie auftreten? &rarr; <abbr title="Read-after-Write: Echte Abh&auml;ngigkeit; Write-after-Read: Gegenabh&auml;ngigkeit; Write-after-Write: Ausgabeabh&auml;ngigkeit">Antwort</abbr></li>
  <li>Welche Abh&auml;ngigkeiten k&ouml;nnen bei der DLX-Pipeline zu Konflikten f&uuml;hren? &rarr; <abbr title="Nur echte Abh&auml;ngigkeiten k&ouml;nnen in der DLX-Pipeline zu Konflikten f&uuml;hren.">Antwort</abbr></li>
  <li>Wie kann man Datenkonflikte durch Software l&ouml;sen? &rarr; <abbr title="Entweder durch einf&uuml;gen von nops (Leeroperationen) oder durch Umordnung der Befehle (Optimierung)">Antwort</abbr></li>
  <li>Wie kann man Datenkonflikte durch Hardware l&ouml;sen? &rarr; <abbr title="Interlocking oder stalling (Pipeline-Sperrung oder Pipeline-Leerlauf); Forwarding, ben&ouml;tigt aber noch interlocking">Antwort</abbr></li>
  <li>Nennen Sie ein Beispiel f&uuml;r einen Konflikt, der nicht durch Forwarding l&ouml;stbar ist? &rarr; <abbr title="load r2, B; add r2, r1, r2">Antwort</abbr></li>
  <li>Wie kann man Ressourcenkonflikte l&ouml;sen? &rarr; <abbr title="Arbitrierung mit Interlocking; &Uuml;bertaktung; Ressourcenreplizierung">Antwort</abbr></li>
  <li>Was bedeutet <span class="hint" title="Minimale Zeitdauer, die zwischen der fallenden Flanke von RAS bis zur Ausgabe der gew&uuml;nschten Daten vergeht">t<sub>RAC</sub></span>, <span class="hint" title="Minimale Zeitdauer von Beginn eines Zeilenzugriffs bis zum n&auml;chsten Zeilenzugriff (Zykluszeit)">t<sub>RC</sub></span>, <span class="hint" title="Minimale Zeitdauer, die zwischen der fallenden Flanke von CAS bis zur Ausgabe der gew&uuml;nschten Daten vergeht">t<sub>CAC</sub></span> und <span class="hint" title="Minimale Zeitdauer vom Beginn eines Spaltenzugriffs bis zum n&auml;chsten Spaltenzugriff (page mode cycle).">t<sub>PC</sub></span>?</li>
  <li>Wie versteht man unter Bus-Schn&uuml;ffeln? &rarr; <abbr title="Jeder Prozessor kontrolliert st&auml;ndig alle Adressen auf dem Bus um Speicherinkonsistenzen zu vermeiden. Siehe Bus snooping.">Antwort</abbr></li>
</ul>

<h3>MIPS</h3>
<h4>Befehlsformate</h4>
{% caption align="aligncenter" width="300" caption="MIPS Befehlsformate<br />Quelle: <a href='http://ti.ira.uka.de/TI-2/Vorlesung/Vorlesung.php'>Folien von Prof. Dr. Asfour</a>" url="../images/2013/01/mips-befehlsformate-300x136.png" alt="MIPS Befehlsformate" title="" height="136" class="size-medium wp-image-62151" %}

Typ-R Befehle sind arithmetisch-logische Befehle wie add, sub, and, or sowie Vergleichsbefehle wie <abbr title="set on less than">slt</abbr>.

Typ-I Befehle sind Lade- und Speicherbefehle sowie Verzweigungsbefehle:
<code>lw $rt, imm($rs)</code>
<code>sw $rt, imm($rs)</code>
<code>beq $rs, $rt, immediate</code>: Hier wird immediate als 16-Bit vorzeichenbehaftete Zahl interpretiert und als Offset benutzt. Die Basisadresse ist dabei im PC. Also lautet die Zieladresse: (PC zum Zeitpunkt des Befehls + 4) + immediate

<h4>Grundlegende Befehle</h4>
<table>
  <thead>
    <tr>
      <th>Syntax</th>
      <th>Erkl&auml;rung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>li $t0, 9</td>
      <td>load immediate: L&auml;dt eine Konstante in ein Register</td>
    </tr>
    <tr>
      <td>sll $rd, $rd, shamt</td>
      <td>shift left logical: $rd = $rs << shamt</td>
    </tr>
    <tr>
      <td>ble Rsrc1, Src2, label</td>
      <td>Branch on Less Than Equal: Rsrc1 &le; Src2</td>
    </tr>
    <tr>
      <td>bne $rs, $rt, imm</td>
      <td>Branch on not equal: if($rs!=$rt) PC = PC + imm  (imm could also be a label)</td>
    </tr>
    <tr>
      <td>slti $rt, $rs, imm</td>
      <td>Store less than immediate: if($rs < imm) {$rt = 1;} else {$rt = 0}</td>
    </tr>
    <tr>
      <td>la Rdest, address</td>
      <td>Load computed address, not the contents of the location, into register Rdest</td>
    </tr>
  </tbody>
</table>

<h3>MiMa</h3>

{% caption align="aligncenter" width="300" caption="Mikrobefehlsformat der MiMa<br />Quelle: <a href='http://ti.ira.uka.de/TI-2/Vorlesung/RO-U01.pdf#page=15'>Folien von Prof. Dr. Asfour</a>" url="../images/2013/01/mima-microbefehlsformat-300x35.png" alt="Mikrobefehlsformat der MiMa" title="" height="35" class="size-medium wp-image-62571" %}

<h4>Fetch-Phase</h4>
In der Fetch-Phase muss das die neue Instruktion ins <abbr title="Instruktionsregister">IR</abbr> geladen werden und der <abbr title="Program counter">PC</abbr> um eins erh&ouml;ht werden:

<ol>
  <li>Takt: IAR &rarr; SAR; IAR &rarr; X; R = 1</li>
  <li>Takt: Eins &rarr; Y; ALU auf addieren; R = 1</li>
  <li>Takt: ALU auf addieren; R = 1</li>
  <li>Takt: Z &rarr; IAR</li>
  <li>Takt: SDR &rarr; IR</li>
</ol>

Das zugeh&ouml;rige Mikroprogramm ist:
{% highlight text %}0010 0001 0000 1000 1000 0000 0001
0001 0100 0000 0000 1000 0000 0010
0000 0000 0000 0001 1000 0000 0011
0000 1010 0000 0000 0000 0000 0100
0000 0000 1001 0000 0000 0000 0101{% endhighlight %}

<h2>Fragen</h2>
<div class="question">
<span class="question">Zeichnen Sie ein Y-Diagramm.</span>
<div class="answer">
{% caption align="aligncenter" width="300" caption="Y-Diagramm<br />Quelle: <a href='http://ti.ira.uka.de/TI-2/Vorlesung/Vorlesung.php'>Folien von Prof. Dr. Asfour</a>" url="../images/2013/01/y-diagramm-300x206.png" alt="Y-Diagramm" title="" height="206" class="size-medium wp-image-61531" %}
</div>
</div>

<div class="question">
<span class="question">Wie ist ein Von-Neumann-Rechner aufgebaut?</span>
<div class="answer">
{% caption align="aligncenter" width="300" caption="Von-Neumann-Architektur" url="../images/2013/01/von-neumann-architektur-300x228.png" alt="Von-Neumann-Architektur" title="" height="228" class="size-medium wp-image-61711" %}

Das Steuerwerk wird auch &bdquo;Leitwerk&ldquo; genannt, das Rechenwerk auch &bdquo;<strong>A</strong>rithmetic <strong>L</strong>ogic <strong>U</strong>nit&ldquo;.

Der BUS beinhaltet Adress-, Daten- und Steuerleitungen.

Im Gegensatz zur Harvard-Architektur wird beim Speicher in der Von-Neumann-Architektur nicht zwischen Daten und Programmen unterschieden.
</div>
</div>

<div class="question">
<span class="question">Wie ist ein Mikroprozessor aufgebaut?</span>
<div class="answer">
{% caption align="aligncenter" width="300" caption="Aufbau eines Mikroprozessors<br />Quelle: <a href='http://ti.ira.uka.de/TI-2/Vorlesung/RO-VL06.pdf#page=10'>Folien von Prof. Dr. Asfour</a>" url="../images/2013/01/aufbau-mikroprozessor-300x212.png" alt="Aufbau eines Mikroprozessors" title="" height="212" class="size-medium wp-image-61841" %}
</div>
</div>

<div class="question">
<span class="question">Aus welchen Phasen besteht die Befehlsausf&uuml;hrung?</span>
<div class="answer">
<ul>
  <li>Holphase</li>
  <li>Dekodierphase</li>
  <li>Ausf&uuml;hrungsphase</li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Warum gibt es mehr als ein Befehlsregister?</span>
<div class="answer">
<ul>
  <li>Die Befehlsformate sind unterschiedlich lang</li>
  <li>Opcode-Prefetching</li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Was ist der Unterschied zwischen BCD in gepackter Darstellung und BCD in ungepackter Darstellung?</span>
<div class="answer">
Bei BCD in gepackter Darstellung werden in einem Byte (8 Bit) zwei BCD-Zahlen dargestellt.
In der ungepackten Darstellung wird in einem Byte nur eine BCD-Zahl dargestellt.
</div>
</div>

<div class="question">
<span class="question">Pipeline-Konflikte: Welche Forwarding-Techniken gibt es und wie werden sie umgesetzt?</span>
<div class="answer">
{% caption align="aligncenter" width="300" caption="Forwarding-Techniken<br />Quelle: Quelle: <a href='http://ti.ira.uka.de/TI-2/Vorlesung/RO-VL06.pdf#page=10'>Folien von Prof. Dr. Asfour</a>" url="../images/2013/01/forwarding-techniken2-300x249.png" alt="Forwarding-Techniken" title="" height="249" class="size-medium wp-image-62451" %}
</div>
</div>

<div class="question">
<span class="question">Welche Halbleiterspeichertypen gibt es?</span>
<div class="answer">
{% caption align="aligncenter" width="300" caption="Klassifizierung von Halbleiterspeicher" url="../images/2013/01/halbleiterspeicher-klassifizierung-300x77.png" alt="Klassifizierung von Halbleiterspeicher" title="" height="77" class="size-medium wp-image-62511" %}
</div>
</div>

<div class="question">
<span class="question">Skizzieren Sie eine SRAM-Zelle.</span>
<div class="answer">
{% caption align="aligncenter" width="300" caption="CMOS SRAM Zelle" url="../images/2013/01/cmos-sram-cell-300x300.png" alt="CMOS SRAM Zelle" title="" height="300" class="size-medium wp-image-62521" %}
</div>
</div>

<div class="question">
<span class="question">Wie unterscheiden sich RISC- und CISC-Architekturen?</span>
<div class="answer">
<table>
  <thead>
    <tr>
      <th>CISC</th>
      <th>RISC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Komplexe Befehle, die in mehreren Taktzyklen ausgef&uuml;hrt werden</td>
      <td>Einfache Befehle, die in einem Taktzyklus ausgef&uuml;hrt werden</td>
    </tr>
    <tr>
      <td>Jeder Befehl kann auf den Speicher zugreifen</td>
      <td>Nur Lade- und Speicherbefehle greifen auf den Speicher zu</td>
    </tr>
    <tr>
      <td>Wenig Pipelining</td>
      <td>Intensives Pipelining</td>
    </tr>
    <tr>
      <td>Befehle werden von einem Mikroprogramm interpretiert</td>
      <td>Befehle werden durch festverdrahtete Hardware ausgef&uuml;hrt</td>
    </tr>
    <tr>
      <td>Befehlsformat variabler L&auml;nge</td>
      <td>Befehlsformat fester L&auml;nge</td>
    </tr>
    <tr>
      <td>Die Komplexit&auml;t liegt im Mikroprogramm</td>
      <td>Die Komplexit&auml;t liegt im Compiler</td>
    </tr>
    <tr>
      <td>Einfacher Registersatz</td>
      <td>Mehrere Registers&auml;tze</td>
    </tr>
  </tbody>
</table>
</div>
</div>

<div class="question">
<span class="question">Wie sieht das Schaltsymbol eines Halbaddierers aus?</span>
<div class="answer">
{% caption align="aligncenter" width="288" caption="Schaltsymbol eines Halbaddierers" url="../images/2013/01/addierer-schaltsymbol.png" alt="Schaltsymbol eines Halbaddierers" title="" height="184" class="size-full wp-image-62671" %}
</div>
</div>

<div class="question">
<span class="question">Wie kann man die Datenabh&auml;ngigkeiten einer Pipeline spezifizieren und erkennen?</span>
<div class="answer">
{% caption align="aligncenter" width="300" caption="Datenabhaengigkeiten in einer Pipeline" url="../images/2013/01/ti-pipeline-datenabhaengigkeit-300x121.jpg" alt="Datenabhaengigkeiten in einer Pipeline" title="" height="121" class="size-medium wp-image-62791" %}

Erkennen kann man sie sehr schnell, indem man eine Tabelle mit den Spalten Befehl, Ziel-Register und Operanden-Register macht. Dabei muss man insbesondere bei der Multiplikation, <code>sw</code> und <code>lw</code> aufpassen. Folgendes (sehr gekrizeltes) Beispiel f&uuml;r die <a href="http://ti.ira.uka.de/Klausur/AlteKlausuren/k_ss_12.pdf#page=11">Klausur vom 26. Juli 2012</a>:
{% caption align="alignnone" width="512" caption="Datenabh&auml;ngigkeiten schnell erkennen" url="../images/2013/01/datenabhaengigkeiten-erkennen.jpg" alt="Datenabh&auml;ngigkeiten schnell erkennen" title="" height="249" class="size-full wp-image-63101" %}
</div>
</div>

<h2>Material</h2>
<ul>
  <li><a href="http://ti.ira.uka.de/">TI-Website</a>
    <ul>
      <li><a href="http://ti.ira.uka.de/Klausur/AlteKlausuren/AlteKlausuren.php">alte Klausuren</a></li>
      <li><a href="http://ti.ira.uka.de/Adressierungsarten/">Flash-Animation zur Adressierung</a></li>
    </ul>
  </li>
  <li><a href="https://ankiweb.net/shared/info/144985236">Meine Karteikarten</a> (Siehe Anki auf <a href="http://de.wikipedia.org/wiki/Anki">Wikipedia</a> und <a href="http://wiki.ubuntuusers.de/Anki">UbuntuUsers</a> f&uuml;r mehr Informationen)</li>
  <li><a href="http://www.titut.de/">titut.de</a>, <a href="http://tutorium.chrismandery.de/">tutorium.chrismandery.de</a></li>
</ul>

StackOverflow:
<ul>
  <li><a href="http://stackoverflow.com/q/4115847/562769">Strange jump in MIPS assembly</a></li>
</ul>

<h2>Aufbau der Klausur</h2>
Die Klausuren sind alle sehr &auml;hnlich aufgebaut. Eine typische Klausur hat 10 Aufgaben zu diesen Themen:

<ol>
  <li><strong>Schaltfunktionen</strong></li>
  <li><strong>Spezielle Bausteine</strong></li>
  <li><strong>Laufzeiteffekte</strong></li>
  <li><strong>Schaltwerke</strong></li>
  <li><strong>Rechnerarithmetik und Codes</strong></li>
  <li><strong>Allgemeines</strong>: Ankreuzaufgaben</li>
  <li><strong>MIPS-Assembler</strong>: C-Code in MIPS umwandeln und umgekehrt</li>
  <li><strong>Pipelining</strong>: Datenkonflikte erkennen und mit NOPs beheben, eventuell gibts noch Forwarding</li>
  <li><strong>Cache-Speicher</strong></li>
  <li><strong>Speicher</strong></li>
</ol>

<h2>Termine und Klausurablauf</h2>
<strong>Datum</strong>: Mittwoch, den 3. April 2013 von 14:00 bis 16:00 Uhr
<strong>Ort</strong>: <a href="http://kit.carstengriesheimer.de/map/1458">Gaede</a> (bei mir; siehe <a href="http://ti.ira.uka.de/Klausur/Hoersaalverteilung.htm">H&ouml;rsaaleinteilung</a>, die seit dem 2. April 2013 drau&szlig;en ist)
<strong>Dauer</strong>: 1 h DT, 1 h RO
<strong>Punkte</strong>: (vermutlich) 90
<strong>Bestehensgrenze</strong>: (vermutlich) 40
<strong>&Uuml;bungsschein</strong>: Wird nicht ins Studienportal eingetragen
<strong>Bonuspunkte</strong>: 
<ul>
  <li>&Uuml;bungsschein RO: 1 Bonuspunkt</li>
  <li>&Uuml;bungsschein DT: 1 Bonuspunkt</li>
  <li>F&uuml;r die Probeklausuren jeweils:
    <ul>
      <li>Note &bdquo;Sehr gut&ldquo;: 2 Bonuspunkte</li>
      <li>Note &bdquo;Gut&ldquo;: 1,5 Bonuspunkte</li>
      <li>Note &bdquo;Befriedigend&ldquo;: 1 Bonuspunkt</li>
      <li>Note &bdquo;Ausreichend&ldquo;: 0,5 Bonuspunkte</li>
    </ul>
  </li>
</ul>

<h2>Nicht vergessen</h2>
<ul>
  <li>Studentenausweis</li>
  <li>Kugelschreiber</li>
</ul>

<h2>Ergebnisse</h2>
Die Klausureinsicht ist am Montag, den 29. April 2013. F&uuml;r die Einsicht muss man sich <a href="http://ti.ira.uka.de/Klausur/Einsicht/">hier</a> anmelden.
