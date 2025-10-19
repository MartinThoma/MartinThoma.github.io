---
layout: post
title: TGI-Klausur
slug: tgi-klausur
lang: de
author: Martin Thoma
date: 2012-02-18 16:57:30.000000000 +01:00
category: German posts
tags: Klausur
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Ich habe im WS 2011/2012 bei Frau <a href="http://i11www.iti.uni-karlsruhe.de/en/members/dorothea_wagner/index">Prof. Dr. Wagner</a> die TGI-Klausur am KIT geschrieben. Hierfür entstand dieser Artikel.</div>

Für die Klausur in den Theoretischen Grundlagen der Informatik sollte man Folgendes auf jeden Fall wissen:

<ul>
    <li>Wie konstruiert man mittels <strong>Potenzmengen</strong> einen äquivalenten deterministischen endlichen Automaten zu einem Nichtdeterministischen? &rarr; <a href="../konstruktion-eines-deterministischen-endlichen-automaten-aus-einem-nicht-deterministischem/" title="Konstruktion eines deterministischen endlichen Automaten aus einem nicht-deterministischem">Antwort</a></li>
	<li>Wie bringt man eine Grammatik in <strong>Chomsky-Normalform</strong>? &rarr; <a href="../konstruktion-der-chomsky-normalform/" title="Konstruktion der Chomsky-Normalform">Antwort</a>.</li>
	<li>Was macht der <strong>CYK-Algorithmus</strong> und wie funktioniert er? &rarr; siehe <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/uebung7.pdf">Beispiel</a> ab Folie 15</li>
	<li>Was ist die <strong>Chomsky-Hirarchie</strong>, welche Grammatiken gibt es und mit welchen Operationen sind sie <strong>Abgeschlossen</strong>? &rarr; <a href="../sprachen-automaten-und-grammatiken/" title="Sprachen, Automaten und Grammatiken: Ein Überblick">Antwort</a>.</li>
	<li>Was ist das Post'sche Korrespondenzproblem?</li>
	<li>Welche <strong>Komplexitätsklassen</strong> sind $\cal P, NP, NPC, DTAPE, NTAPE, NPI$? &rarr; <a href="../komplexitatsklassen-in-der-informatik-ein-uberblick/" title="Komplexitätsklassen in der Informatik: Ein Überblick">Antwort</a></li>
	<li>Wie sind <strong>Kellerautomaten</strong> definiert, wann sind sie formal nicht-deterministisch und in welcher Beziehung stehen sie zur Greibach-Normalform? Wie formt man einen Kellerautomaten von einem akzeptierenden Endzustand in einen mit leerem Stack um? &rarr; <a href="../kellerautomat/" title="Kellerautomat">Antwort</a>.</li>
	<li>Wie lautet das <strong>Pumping-Lemma</strong> (für reguläre und kontextfreie Sprachen? Wie lautet <strong>Ogdens Lemma</strong>? Und wie benutzt man diese für Beweise? &rarr; <a href="../pumping-lemma/" title="Eine Sprache ist nicht regulär &ndash; Beweis mit dem Pumping-Lemma">Antwort</a></li>
	<li>Wie beweist man <strong>NP-Vollständigkeit</strong>?</li>
</ul>

<h2>Some Random Facts</h2>
<ul>
	<li>"aaa" ist in der Sprache aller Worter, die zwei mal "aa" enthalten. <small><sup><a href="#ref1" name="anchor1">[1]</a></sup></small></li>
	<li>Die Grammatik $G_1(\{S\}, \{\varepsilon\}, \{S \rightarrow \varepsilon\},S)$ erzeugt die Sprache $L(G_1) = \{\varepsilon\}$.<small><sup><a href="#ref2" name="anchor2">[2]</a></sup></small></li>
	<li>Die Grammatik $G_2(\{S\}, \{\varepsilon\}, \{\},S)$ erzeugt die Sprache $L(G_2) = \{\}$.</li>
	<li>$L_1 := \{aba, bab, ab\}, L_2 := \{bb,ab,ba\}$. Dann ist
$L_1 / L_2 = \{\varepsilon, a, b\}$ und
$L_1 \setminus L_2 = \{aba, bab\}$<small><sup><a href="#ref3" name="anchor3">[3]</a></sup></small></li>
	<li>$PKP \notin \cal NPC$<small><sup><a href="#ref4" name="anchor4">[4]</a></sup></small></li>
	<li>Es kann sein, dass die Ableitung eines Wortes nicht eindeutig ist, aber der Syntaxbaum eindeutig ist.</li>
	<li>Für jedes Wort w gibt es einen DEA, der w akzeptiert<small><sup><a href="#ref5" name="anchor5">[5]</a></sup></small></li>
	<li>$L' \alpha L$ bedeutet, dass L' polynomial transformierbar in L ist.</li>
	<li>$L' \alpha_T L$ bedeutet, dass L' Turing-reduzierbar in L ist.</li>

</ul>

<h2>Termin</h2>
<strong>Datum</strong>: Mittwoch, der 22.02.2012 um 14:00 Uhr (siehe <a href="http://i11www.iti.uni-karlsruhe.de/teaching/winter2011/tgi/index">Vorlesungswebsite</a>)<br/>
<strong>Ort</strong>: Steht <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/anmeldung.pdf">hier</a>. Ich schreibe im Tulla, manche noch im Gaede und andere im HS a. F., Daimler oder Benz. Laut dieser Liste schreiben 295 Personen diese Klausur!<br/>
<strong>Dauer</strong>: 120 min. (siehe <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/tgi1112-t1.pdf">erste Folie</a>)<br/>
<strong>Punkte</strong>: Bisher waren es meist ca. 60, von denen man 20 zum Bestehen benötigt hat.<br/>
<strong>Übungsschein</strong>: <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/scheine.pdf">Liste</a> der 195 Leute, die ihn bestanden haben. Der Übungsschein bringt einen Klausurbonus. Allerdings habe ich keine Ahnung, wie hoch dieser ist.
edit: +0,3 zur Klausurnot (Danke Alexander ☺)<br/>

Ach ja, ich habe "<a href="http://info.php-4.info/attachment.php?attachmentid=260&sid=dcc186e19164016b828792ff3c04a046">Yet Another Info 3 Resume</a>" noch gar nicht verlinkt. Das ist sehr kurz und hat viele wichtige Informationen.

<h2>Klausurergebnisse</h2>
Die Klausurergebnisse sind nun <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/notenhk.pdf">öffentlich</a>. Die Liste scheint nach Matrikelnummer sortiert zu sein ... tolle Anonymisierung, da wir ja auch im Saal nach Matrikelnummern sortiert waren. Und falls irgendjemand es vergessen hat: Hier ist die <a href="http://i11www.iti.uni-karlsruhe.de/_media/teaching/winter2011/tgi/anmeldung.pdf">öffentliche Liste der Matrikelnummern</a>. Tja, so werden wir verschaukelt was den Datenschutz angeht.

edit: Das Leck scheint ausgebessert worden zu sein. Nun sind die Noten nach Klausur-ID sortiert. Sehr schön ☺

<figure class="aligncenter">
            <a href="../images/2012/02/tgi-notenverteilung-300x257.png"><img src="../images/2012/02/tgi-notenverteilung-300x257.png" alt="Notenverteilung der TGI Klausur im WS 2011/2012 am KIT" style="max-width:300px;max-height:257px" class="size-medium wp-image-18881"/></a>
            <figcaption class="text-center">Notenverteilung der TGI Klausur im WS 2011/2012 am KIT</figcaption>
        </figure>


<h2>Einzelnachweise</h2>
1. <a name="ref1" href="#anchor1">&uarr;</a>: 2. Klausur WS 2003/2004, Aufgabe 1a
2. <a name="ref2" href="#anchor2">&uarr;</a>: 1. Klausur WS 2003/2004, Aufgabe 5
3. <a name="ref3" href="#anchor3">&uarr;</a>: 1. Klausur WS 2007/2008, Aufgabe 3c
4. <a name="ref4" href="#anchor4">&uarr;</a>: 1. Klausur WS 2007/2008, Aufgabe 5
5. <a name="ref5" href="#anchor5">&uarr;</a>: 1. Klausur WS 2010/2011, Aufgabe 5
