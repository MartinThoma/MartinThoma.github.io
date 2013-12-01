---
layout: post
status: publish
published: true
title: Betriebssysteme Klausur
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 17391
wordpress_url: http://martin-thoma.com/?p=17391
date: 2013-03-02 19:06:15.000000000 +01:00
categories:
- German posts
tags:
- Klausur
comments:
- id: 1170091
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNC0wOCAxNTo0NDo1MiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0wOCAxMzo0NDo1MiArMDIwMA==
  content: Die Ergebnisse sind nun online. Ein Link ist oben zu finden.
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Dieser Artikel besch&auml;ftigt sich mit der Vorlesungen des Moduls &bdquo;Betriebssysteme&ldquo; am KIT. Er dient als Pr&uuml;fungsvorbereitung. Ich habe die Vorlesungen bei Prof. Dr. Belosa und sp&auml;ter bei Prof. Dr. Beigl geh&ouml;rt.</div>

Wenn ich im Folgenden eine Seitenzahl angebe, dann ist damit "Operating System Concepts" von Silberschatz gemeint (ISBN 0-471-69466-5):

<h2>Themen</h2>
<ul>
  <li>Process Coordination:
    <ul>
      <li>Shared Memory</li>
      <li>Critical-Section Problem: <a href="http://de.wikipedia.org/wiki/Algorithmus_von_Peterson">Peterson's Solution</a>, Synchronisation</li>
      <li><a href="http://de.wikipedia.org/wiki/Deadlock">Deadlock</a>, <a href="http://en.wikipedia.org/wiki/Resource_starvation">Starvation</a></li>
    </ul>
  </li>
  <li>Process Management
    <ul>
      <li>Process Sheduling</li>
      <li>Process States: new, ready, running, waiting, terminated</li>
      <li>Process Control Block: Folie 6/65 slide_proc_management</li>
    </ul>
  </li>
  <li>Memory Management
    <ul>
      <li>Globale / lokale Seitenersetzungsstrategie</li>
      <li>Equal allocation</li>
      <li><a href="http://de.wikipedia.org/wiki/Slab_allocator">Slab allocator</a></li>
    </ul>
  </li>
</ul>

<h2>Begriffe</h2>
Folgende Begriffe muss man kennen und erkl&auml;ren k&ouml;nnen:
<ul>
  <li>Critical Section und Race Condition</li>
  <li><a href="http://de.wikipedia.org/wiki/Semaphor_(Informatik)">Semaphor</a>: counting Semaphores, binary Semaphores und Mutex Locks &rarr; Antwort auf S. 200f</li>
  <li>Dining-Philosophers Problem &rarr; Antwort auf S. 207f</li>
  <li>Deadlock, Starvation</li>
  <li>Safe State</li>
</ul>

<h2>FAQ</h2>
<ul>
  <li>Wie funktionieren Bitmasken und insbesondere ~, &, |?</li>
  <li>Nenne ein reales Beispiel, bei dem eine Race-Condition auftreten k&ouml;nnte.</li>
  <li>Welche Probleme hat Contiguous Allocation? &rarr; <span class="hint" title="Man muss sich entscheiden, wo auf der Festplatte eine neue Datei begonnen werden soll; Externe Fragmentierung. Strategien: First Fit, Best Fit, Worst Fit">Antwort</span></li>
</ul>

<div class="question">
<span class="question">Welche Scheduling-Verfahren gibt es?</span>
<div class="answer">
<ul>
  <li>Priority Scheduling</li>
  <li>Round Robin</li>
  <li>Multilevel Feedback Queue</li>
  <li>Lottery Scheduling</li>
  <li><abbr title="Preemtitive Shortest Job First">PSJF</abbr></li>
  <li><abbr title="First Come, First Serve">FCFS</abbr></li>
</ul></div>
</div>

<div class="question">
<span class="question">What is the difference between Page and Frame?</span>
<div class="answer">In a paging system, programs and data stored on disk are divided into equal, fixed sized blocks called pages, and main memory is divided into blocks of the same size called frames. Exactly one page can fit in one frame.

Physical memory is divided into parts called &bdquo;frame&ldquo; and logical memory is divided into parts called &bdquo;page&ldquo;.</div>
Quelle: <a href="http://wiki.answers.com/Q/What_is_the_difference_between_Page_and_Frame">wiki.answers.com</a>
</div>

<div class="question">
<span class="question">Nennen und erl&auml;utern Sie die drei notwendigen Bedingungen f&uuml;r eine g&uuml;ltige L&ouml;sung des Problems kritischer Abschnitte.</span>
<div class="answer">
<ul>
<li>Mutual exclusion: Only one thread can be in the CS at a time.</li>
<li>Progress: 
  <ul>
    <li>If no thread is in the CS one of the threads trying to enter will eventually get in</li>
    <li>Threads that are not trying to enter do not hinder processes that try to enter from getting in</li>
  </ul>
</li>
<li>Bounded waiting: Once a thread starts trying to enter the critical section, there is a bound on the number of times other threads get in.</li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Wie kann man das Problem kritischer Abschnitte l&ouml;sen?</span>
<div class="answer">
<ul>
  <li>Interrupts deaktivieren (nur im Kernel-Space, nur Single-Core)</li>
  <li>Spezielle atomare Instruktionen:
    <ul>
      <li><a href="http://en.wikipedia.org/wiki/Test-and-set">Test-and-set</a></li>
      <li><a href="http://en.wikipedia.org/wiki/Compare-and-swap">Compare-and-swap</a></li>
      <li><a href="http://en.wikipedia.org/wiki/Fetch-and-add">Fetch-and-add</a></li>
      <li><a href="http://en.wikipedia.org/wiki/Swap_(computer_science)#Dedicated_instructions">swap</a></li>
    </ul>
  </li>
  <li><a href="http://de.wikipedia.org/wiki/Semaphor_(Informatik)">Semaphor</a> (wait und signal)</li>
  <li><a href="http://de.wikipedia.org/wiki/Monitor_(Informatik)">Monitor</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Algorithmus_von_Peterson">Algorithmus von Peterson</a></li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Nennen und erkl&auml;ren Sie die ver notwendigen Bedingungen f&uuml;r Deadlocks.</span>
<div class="answer">
<ul>
<li>Mutual exclusion: Eine Ressource kann nicht gleichzeitig von mehreren Prozessen benutzt werden</li>
<li>Hold and wait: Ein Prozess, der bereits mindestens eine Ressource h&auml;lt, wartet auf mindestens eine andere Ressource</li>
<li>No preemption: Zugeteilte Ressourcen k&ouml;nnen einem Prozess nicht wieder entzogen werden. Er muss diese selbst freigeben.</li>
<li>Circular wait: Es gibt eine Menge von Prozessen $\{P_0, P_1, \dots, P_n\}$, wobei $P_0$ auf eine Ressource wartet, die $P_1$ h&auml;lt, $P_1$ auf eine Ressource wartet, die $P_2$ h&auml;lt, ..., $P_n$ auf eine Ressource wartet, die $P_0$ h&auml;lt.</li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Was kann man in Bezug auf das Deadlock-Problem machen?</span>
<div class="answer">
<ul>
  <li>Prevention</li>
  <li>Avoidance</li>
  <li>Detection:
    <ul>
      <li>Prozess abschie&szlig;en</li>
      <li>Rollback</li>
    </ul>
  </li>
  <li><a href="http://de.wikipedia.org/wiki/Vogel-Strau%C3%9F-Algorithmus">Vogel-Strau&szlig;-Algorithmus</a>: Der User wird sich schon drum k&uuml;mmern, z.B. indem er einen Prozess abschie&szlig;t (<code>kill -9</code>) oder indem er den PC vom Strom nimmt.</li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Erkl&auml;ren Sie Raid 0 - 5.</span>
<div class="answer">
<ul>
  <li>Raid 0: Striping. Platten werden "aneinandergeh&auml;ngt".</li>
  <li>Raid 1: Mirroring. Daten werden auf mehrere Platten gespiegelt.</li>
  <li>Raid 2: Fehlerkorrigierender Hamming-code.</li>
  <li>Raid 3: Byteweise Parit&auml;t.</li>
  <li>Raid 4: Blockweise Parit&auml;t.</li>
  <li>Raid 5: Blockweise, verteilte Parit&auml;t.</li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Warum verwenden wir Seitentabellen? K&ouml;nnte man nicht einfach im Hauptspeicher je zwei Datenw&ouml;rter kombinieren, wobei das erste die Metainformationen (z.B. Zugriffsrechte, Prozess-ID) und das zweite die Daten enth&auml;lt?</span>
<div class="answer">
Prinzipiell wollen wir in einer x86-Architektur, dass sich die Hardware um das Paging k&uuml;mmert. Bei MIPS sieht das wohl anders aus (<a href="http://stackoverflow.com/q/10671147/562769">Quelle</a>).

Wenn man sich f&uuml;r jedes Datenwort ein Datenwort mit Metainformationen merken w&uuml;rde, h&auml;tte man sehr viel Overhead. Diese Informationen hat man bei Paging auf IA-32 nur jede 4096 Byte! (Allgemein ist Overhead &uuml;brigens eine Begr&uuml;ndung, die h&auml;ufig stimmt.)

Falls man es wirklich genau wissen will, sollte man wohl die <a href="http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html">IA-32 Architectures Software Developer&rsquo;s Manuals</a> lesen. Das sind ja nur 3044 Seiten.
</div>
</div>

<div class="question">
<span class="question">Einstufige Seitentabellen sind deutlich einfacher zu verstehen und zu implementieren. Warum verwendet man sie nicht auf 64 Bit Systemen?</span>
<div class="answer">Sie w&uuml;rden zu viel Speicher ben&ouml;tigen. Es wird eine Seitentabelle pro Prozess ben&ouml;tigt. Die Gr&ouml;&szlig;e einer einstufigen Seitentabelle berechnet sich wie folgt:

Sei $m$ die Gr&ouml;&szlig;e des Hauptspeichers in Byte, $p$ die Gr&ouml;&szlig;e einer Seite in Byte und $a$ die Anzahl der zus&auml;tzlichen Bit pro Seite (Access Control bits, validity. Siehe <a href="http://unix.stackexchange.com/q/68148/4784">StackExchange</a>). 
Dann gilt:

Gr&ouml;&szlig;e der Seitentabelle = Gr&ouml;&szlig;e eines Seiteneintrages &middot; Anzahl der Seiten
$= \lceil \frac{\log_2(\frac{m}{p}) + a}{8}\rceil \text{Byte} \cdot \frac{2^{64} \text{ Byte}}{p \text{ Byte}}$

Typischerweise gilt: $m = 4 GB = 4 \cdot 2^{30} \text{ Byte} = 2^{32} \text{ Byte}$, $p = 4096 \text{ Byte}$ und $a = 8$. Daraus folgt eine Seitengr&ouml;&szlig;e von 4 Byte und 4.503.599.627.370.496 Seiten. Das ergibt eine Seitentabellengr&ouml;&szlig;e von 16 Petabyte.
</div>
</div>

<div class="question">
<span class="question">Wenn man nur Segmentierung nutzt, wie kommt man dann von der logischen Adresse auf die physische?</span>
<div class="answer">
[caption id="attachment_61751" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/segmentation-logical-to-linear-address.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/segmentation-logical-to-linear-address-300x176.png" alt="Segmentation: Logical to linear address" width="300" height="176" class="size-medium wp-image-61751" /></a> Segmentation: Logical to linear address (<a href="http://download.intel.com/products/processor/manual/325462.pdf">source</a>)[/caption]
</div>
</div>

<div class="question">
<span class="question">Wie ist ein Inode aufgebaut?</span>
<div class="answer">
[caption id="attachment_61871" align="aligncenter" width="256"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/inode-struktur.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/inode-struktur-256x300.png" alt="Struktur eines Inodes" width="256" height="300" class="size-medium wp-image-61871" /></a> Struktur eines Inodes[/caption]
</div>
</div>

<div class="question">
<span class="question">Wie gro&szlig; kann eine Datei maximal werden, wenn man Inodes mit jeweils einem indirekten, doppelt indirektem und dreifach indirektem Block hat?</span>
<div class="answer">
Sei $b$ die Gr&ouml;&szlig;e eines Blocks in Byte und ein Zeiger belege 4 Byte.
Dann berechnet sich die maximale Dateigr&ouml;&szlig;e in Byte wie folgt:
$12 \cdot b + \frac{b}{4} \cdot b+ \frac{\frac{b}{4} \cdot b}{4} \cdot b + \frac{\frac{\frac{b}{4} \cdot b}{4} \cdot b}{4} \cdot b = 12 \cdot b + \frac{b^2}{4} + \frac{b^3}{16} + \frac{b^4}{64}$

Bei einer Blockgr&ouml;&szlig;e von 1024 Byte sind das 17,25 GB (<a href="http://www.wolframalpha.com/input/?i=12*1024%2B1024%5E2%2F4%2B1024%5E3%2F16%2B1024%5E4%2F64+byte">Rechnung</a>), bei einer Blockgr&ouml;&szlig;e von 4096 Byte sogar 4,40 TB (<a href="http://www.wolframalpha.com/input/?i=12*4096%2B4096%5E2%2F4%2B4096%5E3%2F16%2B4096%5E4%2F64+byte">Rechnung</a>)!

Wenn ihr Linux habt, k&ouml;nnt ihr diese Werte so herausfinden:
{% highlight bash %}moose@pc08 ~ $ df
Filesystem     1K-blocks     Used Available Use% Mounted on
/dev/sda1      303869280 16418288 272015268   6% /
udev             1889040        4   1889036   1% /dev
tmpfs             758712      988    757724   1% /run
none                5120        0      5120   0% /run/lock
none             1896772      772   1896000   1% /run/shm
none              102400        8    102392   1% /run/user
moose@pc08 ~ $ sudo tune2fs -l /dev/sda1 | grep 'Block size'
Block size:               4096
{% endhighlight %}
</div>
</div>

<div class="question">
<span class="question">Depict the common memory layout of a process. Give an example of the data that is stored in each section.</span>
<div class="answer">
[caption id="attachment_61931" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/process-memory-layout.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/process-memory-layout-300x165.jpg" alt="Common process memory layout" width="300" height="165" class="size-medium wp-image-61931" /></a> Common process memory layout[/caption]

Ich sehe gerade, dass bei rodata wohl das Schl&uuml;sselwort <code>const</code> mit dabei stehen sollte. Statische Variablen k&ouml;nnen nat&uuml;rlich ge&auml;ndert werden.
</div>
</div>

<div class="question">
<span class="question">What is anonymous memory?</span>
<div class="answer">
Anonymous memory is memory, that is not backed by a file. Examples are stack and heap.
</div>
</div>

<h2>Material</h2>
Material zum &Uuml;ben (also <a href="http://os.ibds.kit.edu/1556.php">alte Klausuren</a>) gibts wie immer entweder online oder bei der Fachschaft.

Die L&ouml;sungen zu den Klausuren sind Passwortgesch&uuml;tzt, aber wenn ihr euch einmal &uuml;ber VPN einloggt, stehen ganz unten auf der Seite die Zugangsdaten.

Das Skript / die Folien sind im <a href="https://studium.kit.edu/sites/vab/0x8763DF03F4275B4F908D321A58479E61/vorlesungsunterlagen_pwg/Forms/AllItems.aspx?RootFolder=%2fsites%2fvab%2f0x8763DF03F4275B4F908D321A58479E61%2fvorlesungsunterlagen_pwg%2fVorlesung&FolderCTID=&View=%7b2672A6DD-CB1A-408E-888B-441716F3F757%7d">VAB</a>.

Folgende Wiki-Artikel und manpages sollte man sich durchlesen:
<ul>
  <li><a href="http://de.wikipedia.org/wiki/Unix-Dateirechte">Unix-Dateirechte</a> und <code>chmod</code> sowie <a href="http://martin-thoma.com/linux-access-rights-and-attributes/" title="Linux access rights and attributes">mein Artikel</a>.</li>
</ul>

Als Buch kann ich neben dem Silberschatz folgendes Empfehlen:
LPIC-1 - Vorbereitung auf die Pr&uuml;fung des Linux Professinal Institute. ISBN 978-3-937514-81-9

<h2>Some Random Facts</h2>
<ul>
  <li><code>subl $16, %esp</code> allokiert 16 Byte auf dem Stack.</li>
</ul>

<h2>Termine und Klausurablauf</h2>
<strong>Datum</strong>: 18.03.2012 um 14:00 Uhr.
<strong>Ort</strong>: ich bin im <a href="http://kit.carstengriesheimer.de/map/1459">30.21 Gerthsen</a> (<a href="https://studium.kit.edu/sites/vab/0xC1937D6957186A468FE059ECE05D74B8/Start/homepage.aspx">H&ouml;rsaalverteilung</a>)
<strong>Dauer</strong>: 60 Minuten
<strong>Punkte</strong>: 60
<strong>Benuspunkte</strong>: Abh&auml;ngig von den Punkten im &Uuml;bungsschein:
<ul>
  <li>110 - 129 Punkte: 1 Bonuspunkt</li>
  <li>130 - 149 Punkte: 2 Bonuspunkte</li>
  <li>150 - 169 Punkte: 3 Bonuspunkte</li>
  <li>170 - x Punkte: 4 Bonuspunkte</li>
</ul>
<a href="https://studium.kit.edu/sites/vab/0xC1937D6957186A468FE059ECE05D74B8/Vorlesungsunterlagen/BS-WS1213-00aOrga.pdf">Quelle</a>
<strong>Nicht vergessen</strong>: Studentenausweis
<strong>Einsicht</strong>: 09.04.2013 (war seit sp&auml;testens 13.02.2013 bekannt)
<strong>Ort der Einsicht</strong>: 07.07 (<a href="https://maps.google.com/maps?q=Vincenz-Prie%C3%9Fnitz-Stra%C3%9Fe+1,+Forschungsstelle+f%C3%BCr+Brandschutztechnik+am+KIT,+Oststadt+76131+Karlsruhe,+Baden-W%C3%BCrttemberg,+Deutschland&hl=de&ie=UTF8&ll=49.012738,8.423853&spn=0.015622,0.042272&geocode=FYXh6wIdLouAAA&hnear=Vincenz-Prie%C3%9Fnitz-Stra%C3%9Fe+1,+Oststadt+76131+Karlsruhe,+Baden-W%C3%BCrttemberg,+Deutschland&t=m&z=15">Vincenz-Priessnitz-Str. 1</a>, 2.OG, links), Raum 215
<strong>Zeit der Einsicht</strong>: Je nach Matrikelnummer unterschiedlich.

<h2>Ergebnisse</h2>
<strike>H&auml;ngen noch nicht aus (Stand: 15.03.2013)</strike>
H&auml;ngen nun aus (Stand: 08.04.2013) und <a href="https://studium.kit.edu/sites/vab/0xC1937D6957186A468FE059ECE05D74B8/vorlesungsunterlagen_pwg/Ergebnisse/klausur__18_03_2013.pdf">sind im VAB</a>

[caption id="attachment_63331" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/os-klausur-ws201213-ergebnisse.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/os-klausur-ws201213-ergebnisse-300x227.png" alt="Ergebnisse der OS-Klausur vom WS 2012 / 2013" width="300" height="227" class="size-medium wp-image-63331" /></a> Ergebnisse der OS-Klausur vom WS 2012 / 2013[/caption]
