---
layout: post
title: Datenbanksysteme-Klausur
author: Martin Thoma
date: 2013-04-20 13:35:01.000000000 +02:00
category: German posts
tags: Klausur
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Dieser Artikel besch&auml;ftigt sich mit der Vorlesung &bdquo;Datenbanksysteme&ldquo; des Moduls &bdquo;Kommunikation und Datenhaltung&ldquo; am KIT. Er dient als Pr&uuml;fungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://dbis.ipd.uni-karlsruhe.de/336.php">Herrn Prof. Dr. B&ouml;hm</a> im Sommersemester 2013 geh&ouml;rt.</div>

An diesem Artikel wird nat&uuml;rlich noch gearbeitet.


## Behandelter Stoff
<table>

<tr>
<td>15.04.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;"><span class="hint" title="Sie lagern Komplexit&auml;t aus: Keine redundante Speicherung von Daten, verhindern Inkonsistenzen">Warum Datenbanken toll sind</span>; <span class="hint" title="Atomarit&auml;t und Isolation">Transaktionseigenschaften</span>; Datenschutz; Datensicherheit; Relationsmodell; Integrit&auml;tsbedingungen; Schl&uuml;ssel; Fremdschl&uuml;ssel; SQL; View; <span class="hint" title="Zeile ausw&auml;hlen">Selektion</span>; <span class="hint" title="Spalte ausw&auml;hlen">Projektion</span>; <span class="hint" title="Beliebige Kombination der Operationen Verbund, Vereinigung, Differenz, Durchschnitt, Umbennenung, Projektion, Selektion">Query-Algebra</span>; <span class="hint" title="Zwei Selektionen k&ouml;nnen deutlich unterschiedlich gro&szlig;e Ergebnismengen haben. Werden sie hintereinander ausgef&uuml;hrt, empfiehlt es sich die st&auml;rker einschr&auml;nkende Selektion zuerst auszuf&uuml;hren.">Anfrage-Optimierer</span>; <span class="hint" title="Der Anwender sagt nur welches Ergebnis er will, nicht wie es ermittelt werden soll.">Anfragen sind deklarativ</span>; 3-Ebenen-Architektur; Trennung zwischen Schema und Instanz, <a href="https://de.wikipedia.org/wiki/Online_Analytical_Processing#12_Regeln_nach_Codd">9 Codd'sche Regeln</a></td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1272879/Kap1-Einleitung.pdf">Kapitel 1</a></td>
</tr>

<tr>
<td>18.04.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Datentyp, Instanz, Polymorphes Typsystem, Typkonstruktoren, ... (TODO)</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1274077/Kap2-Datenmodellierung.pdf">Kapitel 2</a> - <a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1274086/Kap3-DDL.pdf">Kapitel 3</a>, Folie 32</td>
</tr>

<tr>
<td>22.04.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">SQL (alter, drop, index, unique); Index; ER-Diagramm; UML; Tr&auml;germenge $\mu$, Aktueller Zustand einer Variablen $\sigma$</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1274086/Kap3-DDL.pdf">Kapitel 3</a>, Folie 32 - <a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1274693/Kap4-ERModell.pdf">Kapitel 4</a>, Folie 33</td>
</tr>

<tr>
<td>29.04.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Systemunabh&auml;ngige Modellierung - Strukturelle Seite; <span class="hint" title="keine Instanzen, aber Ableitungen">abstrakte Klassen</span>, <span class="hint" title="Enthalten Methoden zur Erzeugung von Klassen">Metaklassen</span>, Parametrisierte Klassen; <span class="hint" title="Auto: R&auml;der, Lenkrad, Motor, Karosserie, ...">Aggregation</span> und <span class="hint" title="Fu&szlig;ballmanschaft besteht aus Spielern">Assoziation</span></td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1275725/Kap5-DMfuerRealis.pdf">Kapitel 5</a>, Folie 1 - <a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1275734/Kap6-Abb-ER2RDM.pdf">Kapitel 6</a>, Folie 24</td>
</tr>

<tr>
<td>06.06.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;"><abbr title="functional dependency">FD</abbr>, Reflexivit&auml;t, Projektivit&auml;t, Akkumulation, RAP-Regeln, Einf&uuml;geanomalie, L&ouml;schanomalie; Abh&auml;ngigkeitstreue / Verbundtreue; 1. - 4. Normalform</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1282295/Kap7-relEntwurf-Teil1.pdf">Kapitel 7</a></td>
</tr>

<tr>
<td>13.06.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Nebenl&auml;ufigkeitsprobleme: Lost update, dirty read, non-repeatable read; Serielle Ausf&uuml;hrung beseitigt Probleme, aber IO/Kommunikation machts ineffizient; History,  Prefix Commit-Closed, commited projection; Transaktionen</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1289715/Kap11-ConcurrencyControl.pdf">Kapitel 11</a></td>
</tr>

<tr>
<td>24.06.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Serialisierbarkeitsgraph; Synthese-Verfahren; BCNF; Histories: <abbr title="Recoverability">RC</abbr>, <abbr title="Avoids Cascading Aborts: Lesen nur von commiteten Transaktionen">ACA</abbr>, <abbr title="Strict (einfach RC+ACA, oder?)">ST</abbr>; <span class="hint" title="Wenn ich eine Eigenschaft habe, dann gilt sie auch vor dem letzten commit">prefix commit-closed</span></td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1289715/Kap11-ConcurrencyControl.pdf">Kapitel 11</a></td>
</tr>

<tr>
<td>27.06.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Kapitel 8: Relationale Algebra, Bereichskalk&uuml;l; Syntaktisch sicher $\Rightarrow$ Semantisch sicher; Kapitel 12: Anwendungsprogrammierung</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1291006/Kap8-relAlg.pdf">Kapitel 8</a>, <a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1294925/Kap12-Schnittstellen.pdf">12</a></td>
</tr>
</table>

Falls hier was fehlt, k&ouml;nnt ihr mich gerne in den Kommentaren oder per Mail (info@martin-thoma.de) darauf aufmerksam machen. Ich bin ja mal gespannt, ob ich das bis zum Ende aktuell halte.


## SQL

```sql
create view MG as
select Mitarbeiter, Gehalt
from MGA
where Gehalt > 70
```

```sql
insert into MG
values ('Alice', 90)
```


## Fragen
<div class="question">
<span class="question">Was ist der Unterschied zwischen einem DBS und einem DBMS?</span>
<div class="answer">
Ein <abbr title="Datenbankmanagementsystem">DBMS</abbr> ist eine Software zur Datenverwaltung. Die eigentlichen Daten sind in der Datenbank.
Ein <abbr title="Datenbanksystem">DBS</abbr> ist eine DBMS und eine Datenbank.

Ein DBMS kann mehrere Datenbanken verwalten.
</div>
</div>

<div class="question">
<span class="question">Sei $H = r_1[y] w_1[x] r_3[x] w_1[z] r_2[z] w_3[y] r_2[x] w_2[y] c1 r_3[y] c_3 w_2[z] c_2$.<br/>Welche Transaktionen sind in dieser History?</span>
<div class="answer">
<ul>
  <li>Ein Eintrag $r_i[x]$ bedeutet, dass die Transaktion $i$ die Ressource $x$ liest.</li>
  <li>Ein Eintrag $w_i[x]$ bedeutet, dass die Transaktion $i$ die Ressource $x$ schreibt.</li>
  <li>$c_i$ bedeutet, dass die $i$-te Transaktion commitet wird</li>
</ul>

Es gibt also die Transaktion $T_1, T_2 \text{ und } T_3$ mit
$T_1 = r_1[y] w_1[x] c_1$
</div>
</div>


## Material
<ul>
  <li><a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/1272509?client_size=1366x655">Folien</a></li>
  <li><a href="http://dbis.ipd.uni-karlsruhe.de/1969.php">Vorlesungswebsite</a></li>
  <li><a href="https://ankiweb.net/shared/info/3786791111">Mein Anki-Deck</a> (digitale Karteikarten)</li>
  <li><a href="http://mitschriebwiki.nomeata.de/Datenhaltung.pdf.4.pdf">Mitschrieb-Wiki</a></li>
</ul>

In der Fachschaft gibt es folgende Altklausuren:

<ul>
  <li>25. Februar 2011</li>
  <li>30. Juli 2010 (DB + Rechnernetze, mit L&ouml;sung)</li>
</ul>


## Aufbau der Klausur
H&auml;ufige Aufgabenstellungen sind:

<ul>
  <li>Histories und Transaktionen: Ist eine gegebene History RC, ACA, Strict?</li>
  <li>Modellierung</li>
  <li>SQL-Abfragen formulieren</li>
</ul>

In der Klausur vom SS 2013 wurde das in 4 Aufgaben &agrave; 15 Punkte aufgeteilt. Unter anderem war diesmal der RAP-Algorithmus und der Dekompositionsalgorithmus relevant.


## &Uuml;bungsbetrieb
Es gibt nur ein "&Uuml;bungsblatt" mit Bonuspunkten f&uuml;r die Klausur. Auf dieses beziehe ich mich.

<ul>
<li>Wo sind die &Uuml;bungsbl&auml;tter: <a href="https://dalaran.ipd.kit.edu">Portal</a> - <a href="https://bscw.ira.uni-karlsruhe.de/pub/bscw.cgi/d1289127/SQL-%C3%9Cbungsblatt%20%28relevant%20f%C3%BCr%20Klausurbonus%29.pdf">Aufgaben</a></li>
<li>Abgabeform: Online</li>
<li>Abgabe: 07.07.2013</li>
<li>R&uuml;cknahme: ?</li>
<li>Turnus: Einmalig</li>
<li>&Uuml;bungsschein verpflichtend: Nein</li>
<li>Bonus durch &Uuml;bungsschein: Ja</li>
</ul>

Ein paar interessante Informationen zum Blatt:

<div class="question">
<span class="question">Was ist mit "Brute-Force-Ans&auml;tze" in der Aufgabenstellung gemeint?</span>
<div class="answer">
Antwort von Herrn Keller:

Bei Anfragen, die nur eine Anzahl in der Projektionsliste erwarten, k&ouml;nnen sie mit einer Query

<code>SELECT <korrekte_Anzahl> FROM <irgendeiner_Tabelle></code>

das korrekte Ergebnistupel durch ausprobieren herausbekommen. Im Portal wird das zun&auml;chst als "korrekt" bewertet, allerdings werden wir das im Nachhinein filtern.
</div>
</div>

<div class="question">
<span class="question">Wie kann man bei der ORACLE-Datenbank die Anzahl der ausgegebenen Zeilen beschr&auml;nken (LIMIT)?</span>
<div class="answer">

{% highlight sql %}
SELECT *
FROM
( your selection )
WHERE ROWNUM <= 5
{% endhighlight %}

</div>
</div>

Ein bisschen was zu <a href="http://en.wikipedia.org/wiki/Join_(SQL)">JOIN</a> sollte man sich durchlesen.

Ich habe &uuml;brigens das folgende Captcha bekomme:

<figure class="aligncenter">
            <a href="../images/2013/04/captcha-db.png"><img src="../images/2013/04/captcha-db.png" alt="Datenbanksysteme - Captcha" style="max-width:293px;max-height:221px" class="size-full wp-image-70581"/></a>
            <figcaption class="text-center">Datenbanksysteme - Captcha</figcaption>
        </figure>

Wie zur H&ouml;lle soll man das l&ouml;sen? Ich hatte auf &bdquo;448444&ldquo; getippt, aber das war falsch.


## Termine und Klausurablauf
<strong>Datum</strong>: Mittwoch, den 31. Juli 2013 von 11:00 bis 13:00 Uhr
<strong>Ort</strong>: seit 29.07.2013 online:

<table>
  <tr>
    <th>Wer</th>
    <th>Wo</th>
  </tr>
  <tr>
    <td>Nachnamen A-G</td>
    <td>Gerthsen H&ouml;rsaal</td>
  </tr>
  <tr>
    <td>Nachnamen H-J</td>
    <td>Nusselt H&ouml;rsaal</td>
  </tr>
  <tr>
    <td>Nachnamen K-L</td>
    <td>H&ouml;rsaal Neue Chemie</td>
  </tr>
  <tr>
    <td>Nachnamen M-R</td>
    <td>Daimler H&ouml;rsaal</td>
  </tr>
  <tr>
    <td>Nachnamen S</td>
    <td>Gaede H&ouml;rsaal</td>
  </tr>
  <tr>
    <td>Nachnamen T-Z</td>
    <td style="background-color:#cdcdcd">Benz H&ouml;rsaal</td>
  </tr>
</table>

<strong>Punkte</strong>: 60
<strong>Bestehensgrenze</strong>: ?
<strong>&Uuml;bungsschein</strong>: ?
<strong>Bonuspunkte</strong>: ?


## Nicht vergessen
<ul>
  <li>Studentenausweis</li>
  <li>Kugelschreiber</li>
</ul>


## Ergebnisse
Sind noch nicht drau&szlig;en (Stand: 20.04.2013)
