---
layout: post
title: Rechnernetze-Klausur
author: Martin Thoma
date: 2013-04-25 09:32:06.000000000 +02:00
category: German posts
tags: Klausur
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Einführung in Rechnernetze&ldquo; des Moduls &bdquo;Kommunikation und Datenhaltung&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei Herrn <a href="http://pcs.tm.kit.edu/21_beigl.php">Prof. Dr. Beigl</a> im Sommersemester 2013 gehört.</div>


## Behandelter Stoff

<table>
<tr>

<td>16.04.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Einleitung</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Vorlesungsunterlagen/Folien/01_Einfuehrung_Rechnernetze.pdf">Kapitel 1</a></td>
</tr>

<tr>
<td>24.04.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">E-Mail, <span class="hint" title="hochgradig gecachetes hirarchisches Datenbanksystem">DNS</span>, dig, nslookup, Peer-to-Peer-Netzwerke, Bootstrapping-Problem, ISO-/OSI-Schichtenmodell, <span class="hint" title="Service Access Points">SAPs</span>; Dienstgeber/-bringer, -funktionalität, -nehmer, -primitiv, -leistung; Request, Indication, Response, Confirm; <span class="hint" title="Quality of Service">QoS</span></td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Vorlesungsunterlagen/Folien/02_Architekturen_Rechnernetze.pdf">Kapitel 2</a>, Folie 18</td>
</tr>

<tr>
<td>30.04.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;"><span class="hint" title="Service Data Unit">SDU</span>, <span class="hint" title="Protocoll Data Unit">PDU</span>, ISO / OSI-Architektur</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Vorlesungsunterlagen/Folien/02_Architekturen_Rechnernetze.pdf">Kapitel 2</a> bis wohin?</td>
</tr>

<tr>
<td>21.05.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;"><a href="http://de.wikipedia.org/wiki/Zyklische_Redundanzpr%C3%BCfung">CRC</a>, Generatorpolynome, Vorwärtsfehlerkorrektur, Sequenznummern, Quittung, Stop-and-wait</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">?</td>
</tr>

<tr>
<td>28.05.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Protokollmechanismen und Verbindungen: Stop-and-wait; Go-Back-N <abbr title="Automatic Repeat Request">ARQ</abbr>, Flusskontrolle (Open Loop, Closed Loop); Kreditbasierte Flusskontrolle</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Vorlesungsunterlagen/Folien/04_Protokollmechanismen.pdf#page=36">Kapitel 4.5</a> - 4.8</td>
</tr>

<tr>
<td>04.06.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">?</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;"><a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Vorlesungsunterlagen/Folien/05_HDLC.pdf">Kapitel 5</a></td>
</tr>

<tr>
<td>12.06.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Übungsblatt 2: <abbr title="Automatic Repeat Request">ARQ</abbr>: Bestätigter Dienst (JA), Zuverlässiger Dienst (JA, wenn...); Stop-and-Wait;</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">?</td>
</tr>

<tr>
<td>18.06.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Paketvermittlung</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">7.2.2</td>
</tr>

<tr>
<td>25.06.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">Broadcast-Routing: Dateneinheit wird für jedes System erstellt; Hot-Potato; Potential des Missbrauchs (&rarr; <a href="https://www.youtube.com/watch?v=AOEQ9GteWbg">The Internet could crash. We need a Plan B.</a>); Outlaw-detection; Distanz-Vector-Routing; Link-State-Routing</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">7-44</td>
</tr>

<tr>
<td>02.07.2013</td>
<td rowspan="2" style="border-bottom:1px solid black;">IPv4 (Class A/B/C/D/E-Netze); <abbr title="Classless Inter-Domain Routing">CIDR</abbr>; Zuteilung von Adressen (<abbr title="Dynamic Host Configuration Protocol">DHCP</abbr>); Subnetze und Subnetz-Maskierung</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">7-44</td>
</tr>
</table>

Falls hier was fehlt, könnt ihr mich gerne in den Kommentaren oder per Mail (info@martin-thoma.de) darauf aufmerksam machen. Ich bin ja mal gespannt, ob ich das bis zum Ende aktuell halte.

<h3>Übersicht über Dienstprimitive</h3>
<table>
<tr>
 <th>Name</th>
 <th>Dienstleistung</th>
 <th>Grundtypen</th>
 <th>Parameter</th>
</tr>
<tr>
 <td>Physical (Ph)</td>
 <td>Connect (Con)</td>
 <td>Request (Req)</td>
 <td colspan="7">Abhängig vom Dienst</td>
</tr>
<tr>
 <td>Data Link (DL)</td>
 <td>Data (Dat)</td>
 <td>Indication (Ind)</td>
</tr>
<tr>
 <td>Network (N)</td>
 <td>Release (Rel)</td>
 <td>Response (Rsp)</td>
</tr>
<tr>
 <td>Transport (T)</td>
 <td>Abort (Abo)</td>
 <td>Confirmation (Cnf)</td>
</tr>
<tr>
 <td>HTTP</td>
 <td>Provider Abort (PAbo)</td>
 <td>&nbsp;</td>
</tr>
<tr>
 <td>FTP</td>
 <td>Disconnect (Dis)</td>
 <td>&nbsp;</td>
</tr>
<tr>
 <td>...</td>
 <td>...</td>
 <td>&nbsp;</td>
</tr>
</table>


## Fragen

<div class="question">
<span class="question">Welche Qualitätsparameter sind für Rechnernetze denkbar?</span>
<div class="answer">
<ul>
  <li>Angemessenheit</li>
  <li>Technische Leistung (Antwortzeit, Datenrate)</li>
  <li>Zuverlässigkeit</li>
  <li>Sicherheit</li>
  <li>Kosten</li>
</ul>
</div>
</div>


## Material

<ul>
  <li><a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Start/homepage.aspx">Vorlesungswebsite</a></li>
  <li><a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Lists/Forum/AllItems.aspx">Forum</a></li>
  <li><a href="https://ankiweb.net/shared/info/1739663871">Mein Anki-Deck</a></li>
  <li>Ein <a href="//www.youtube.com/watch?v=0apqZ4jsGmI">Video über CRC</a></li>
  <li>Der Wikipedia-Artikel <a href="http://de.wikipedia.org/wiki/Routing">Routing</a> beinhaltet viele wichtige Informationen.</li>
  <li><a href="http://packetcrafter.wordpress.com/2011/02/13/tcp-flags-hackers-playground/">TCP flags: Hackers Playground</a></li>
  <li><a href="http://www.work-at-google.com/curriculum-vitae.html">René Pickhardt</a> und weitere: <a href="https://en.wikiversity.org/wiki/Web_Science">Web Science MOOC</a> auf der Wikiversity.</li>
</ul>


## Aufbau der Klausur

Häufige Aufgabenstellungen sind:
<ul>
  <li>Berechnen einer Subnetzmaske bzw. ob eine IP-Adresse in einem gegebenem Subnetz enthalten ist</li>
  <li>CRC berechnen / überprüfen ob CRC korrekt ist</li>
  <li>Distanz-Vektor Algorithmus (Bellman-Ford) durchgehen</li>
  <li>Protokollablauf durchspielen</li>
</ul>


## Übungsbetrieb
Übungsblätter sind <a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Vorlesungsunterlagen/Forms/AllItems.aspx?RootFolder=%2fsites%2fvab%2f0x2E18BE2A290A424EB98916CA7A6FF3FD%2fVorlesungsunterlagen%2fUebung&FolderCTID=&View=%7bF9CB46E3-13F6-4910-9A2E-BF24D999D119%7d">hier</a>.


## Termine und Klausurablauf

<strong>Datum</strong>: Donnerstag, den 1. August 2013 von 14:00 bis 15:00 Uhr<br/>
<strong>Ort</strong>: Seit 28.07.2013 <a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Start/homepage.aspx">online</a>:<br/>
<table>
<tr>
  <th>Ort</th>
  <th>von</th>
  <th>bis</th>
</tr>
<tr>
  <td>Audimax A (30.95, EG)</td>
  <td>Abdullah</td>
  <td>Galler</td>
</tr>
<tr>
  <td>Audimax B (30.95, EG)</td>
  <td>Gassenschmidt</td>
  <td>Löffler</td>
</tr>
<tr>
  <td style="background-color:#cdcdcd">HSaF (50.35, EG)</td>
  <td>Loose</td>
  <td>Tobias</td>
</tr>
<tr>
  <td>Neue Chemie (30.46, EG)</td>
  <td>Traub</td>
  <td>Zumkeller</td>
</tr>
</table>

<strong>Einsicht</strong>: 17.09.2013<br/>
<strong>Punkte</strong>: 30<br/>
<strong>Bestehensgrenze</strong>: 13 Punkte<br/>
<strong>Notenskala</strong>:<br/>
<table>
<tr>
  <th>Note</th>
  <th>von</th>
  <th>bis</th>
  <th>Bereichsgrö&szlig;e</th>
</tr>
<tr>
  <th>1,0</th>
  <td>30,00</td>
  <td>26,50</td>
  <td>3,5</td>
</tr>
<tr>
  <th>1,3</th>
  <td>26,25</td>
  <td>25,00</td>
  <td>1,25</td>
</tr>
<tr>
  <th>1,7</th>
  <td>24,75</td>
  <td>23,50</td>
  <td>1,25</td>
</tr>
<tr>
  <th>2,0</th>
  <td>23,25</td>
  <td>22,00</td>
  <td>1,25</td>
</tr>
<tr>
  <th>2,3</th>
  <td>21,75</td>
  <td>20,50</td>
  <td>1,25</td>
</tr>
<tr>
  <th>2,7</th>
  <td>20,25</td>
  <td>19,00</td>
  <td>1,25</td>
</tr>
<tr>
  <th>3,0</th>
  <td>18,75</td>
  <td>17,50</td>
  <td>1,25</td>
</tr>
<tr>
  <th>3,3</th>
  <td>17,25</td>
  <td>16,00</td>
  <td>1,25</td>
</tr>
<tr>
  <th>3,7</th>
  <td>15,75</td>
  <td>14,50</td>
  <td>1,25</td>
</tr>
<tr>
  <th>4,0</th>
  <td>14,25</td>
  <td>13,00</td>
  <td>1,25</td>
</tr>
<tr>
  <th>5,0</th>
  <td>12,75</td>
  <td>00,00</td>
  <td>12,75</td>
</tr>
</table>
<strong>Übungsschein</strong>: Nein<br/>
<strong>Bonuspunkte</strong>: Nein


## Nicht vergessen
<ul>
  <li>Studentenausweis</li>
  <li>Kugelschreiber</li>
</ul>


## Ergebnisse
Sind nun <a href="https://studium.kit.edu/sites/vab/0x2E18BE2A290A424EB98916CA7A6FF3FD/Lists/Ankuendigungen/DispForm.aspx?ID=11">online</a>. Hier ist die Statistik:
<figure class="aligncenter">
            <a href="../images/2013/04/klausur-rechnernetze-2013-300x274.png"><img src="../images/2013/04/klausur-rechnernetze-2013-300x274.png" alt="Klausurergebnisse Rechnernetze 2013" style="max-width:300px;max-height:274px" class="size-medium wp-image-76302"/></a>
            <figcaption class="text-center">Klausurergebnisse Rechnernetze 2013</figcaption>
        </figure>
