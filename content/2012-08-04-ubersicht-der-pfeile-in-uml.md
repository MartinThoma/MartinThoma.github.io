---
layout: post
lang: de
title: &Uuml;bersicht der Pfeile in UML
slug: ubersicht-der-pfeile-in-uml
author: Martin Thoma
date: 2012-08-04 09:23:29.000000000 +02:00
category: German posts
tags: SWT I, UML
featured_image: 2012/05/UML-thumb.png
---
Folgende Pfeile werden in UML verwendet:
<h2>Klassendiagramme</h2>
<h3>Vererbung</h3>
<figure class="alignright">
            <a href="../images/2012/07/UML-vererbung.png"><img src="../images/2012/07/UML-vererbung.png" alt="Class B erbt von Class A; Class A ist die Oberklasse" style="max-width:77px;max-height:135px;" class="size-full wp-image-32841 "/></a>
            <figcaption class="text-center">Class B erbt von Class A; Class A ist die Oberklasse</figcaption>
        </figure>
Die <a href="http://de.wikipedia.org/wiki/Vererbung_(Programmierung)">Vererbung</a> ist eines der wichtigsten Prinzipien der objektorientierten Programmierung. Sie zeigt eine "ist ein"-Beziehung an.

Beispiele sind:
<ul>
  <li><code>Tiger</code> ist eine <code>Gro&szlig;katze</code> ist eine <code>Katze</code> ist ein <code>Raubtier</code> ist ein <code>Tier</code>.</li>
  <li><code>Auto</code> ist ein <code>Fortbewegungsmittel</code>.</li>
  <li><code>Auto</code> ist ein <code>Luxusgut</code>.</li>
</ul>

Beachte dass <code>Auto</code> hier sowohl von <code>Luxusgut</code>, als auch von <code>Fortbewegungsmittel</code> erbt. Das geht in manchen Programmiersprachen (C++, Python), in anderen nicht (Java).

<h3>Assoziation</h3>
<figure class="alignright">
            <a href="../images/2012/07/UML-assoziation.png"><img src="../images/2012/07/UML-assoziation.png" alt="Assoziation" style="max-width:77px;max-height:154px;" class="size-full wp-image-32901 "/></a>
            <figcaption class="text-center">Assoziation</figcaption>
        </figure>

Die <a href="http://de.wikipedia.org/wiki/Assoziation_(UML)">Assoziation</a>zeigt eine Verbindung an, z.B.:
<ul>
	<li>Person - Termin: Eine Person hat Termine; Termine geh&ouml;ren zu einer Person.</li>
	<li>Lehrer - Sch&uuml;ler: Ein Sch&uuml;ler hat Lehrer; Lehrer haben Sch&uuml;ler.</li>
	<li>Auto - Fahrer: Ein Auto hat einen Fahrer; ein Fahrer hat ein Auto.</li>
</ul>
In einer Datenbank w&uuml;rde man f&uuml;r diese Relationen eine weitere Tabelle erstellen. Also eine Tabelle f&uuml;r Personen, eine f&uuml;r Termine und eine f&uuml;r Person-Termin-Verkn&uuml;pfungen.
<h3>Aggregation</h3>
<figure class="alignright">
            <a href="../images/2012/07/UML-aggregation.png"><img src="../images/2012/07/UML-aggregation.png" alt="Aggregation" style="max-width:77px;max-height:155px;" class="size-full wp-image-32871 "/></a>
            <figcaption class="text-center">Aggregation</figcaption>
        </figure>

Die <a href="http://de.wikipedia.org/wiki/Assoziation_(UML)#Aggregation">Aggregation</a> ist eine spezielle Assoziation. Sie zeigt eine "hat"-Beziehung an. Dabei ist die Richtung wichtig und sollte angezeigt werden.

Aggregationen sind z.B.:
<ul>
	<li>PKW hat R&auml;der</li>
	<li>Eltern haben Kinder</li>
	<li>Buchladen hat B&uuml;cher</li>
</ul>
<h3>Komposition</h3>
<figure class="alignright">
            <a href="../images/2012/07/UML-komposition.png"><img src="../images/2012/07/UML-komposition.png" alt="Komposition" style="max-width:77px;max-height:155px;" class="size-full wp-image-32891 "/></a>
            <figcaption class="text-center">Komposition</figcaption>
        </figure>

Die <a href="http://de.wikipedia.org/wiki/Komposition_(UML)#Komposition">Komposition</a> zeigt eine notwendige "ist-Teil-von" Beziehung an. Das Teil kann also nicht ohne das Ganze existieren.

Beispiele sind:
<ul>
	<li>Buch hat Buchseiten (Buchseiten gibt es nicht ohne Buch)</li>
	<li>Rechnung hat Posten (Rechnungsposten gibt es nicht ohne Rechnung)</li>
	<li>Graph hat Knoten (Knoten gibt es nicht ohne Graph)</li>
</ul>

<h3>Weitere</h3>
<ul>
  <li>Die Benutzt-Relation wird als gestrichelter Pfeil mit nicht-ausgef&uuml;lltem Kopf dargestellt.</li>
  <li>Eine Implementierung wird als gestrichelter Pfeil mit rundem, nicht ausgef&uuml;lltem Kopf dargestellt.</li>
</ul>

<h2>Objektdiagramme</h2>
<figure class="aligncenter">
            <a href="../images/2012/07/objektdiagramm-instance-of.png"><img src="../images/2012/07/objektdiagramm-instance-of.png" alt="UML: instanceOf beziehung in einem Objektdiagramm" style="max-width:404px;max-height:77px" class="size-full wp-image-36561"/></a>
            <figcaption class="text-center">UML: instanceOf beziehung in einem Objektdiagramm</figcaption>
        </figure>

<h2>Sequenzdiagramme</h2>
<a href="http://de.wikipedia.org/wiki/Sequenzdiagramm">Sequenzdiagramme</a> haben wieder eigene Pfeile.
<figure class="aligncenter">
            <a href="../images/2012/07/sequenzdiagram.png"><img src="../images/2012/07/sequenzdiagram.png" alt="UML Sequenzdiagramm" style="max-width:421px;max-height:259px" class="size-full wp-image-32951"/></a>
            <figcaption class="text-center">UML Sequenzdiagramm</figcaption>
        </figure>
Der Pfeil mit der ausgef&uuml;llten Spitze ist eine Synchrone Nachricht, der gestrichelte mit der nicht-ausgef&uuml;llten Spitze ist eine Antwort  und der durchgezogenen Pfeil mit der nicht-ausgef&uuml;llten Spitze ist eine asynchrone Nachricht.
<strong>ACHTUNG</strong>: In der Vorlesung bei Herrn Prof. Tichy hat die Antwort (Folie 42) auch keinen ausgef&uuml;llten Kopf, im gegensatz zu dem hier gezeigtem Bild!

<h2>Siehe auch</h2>
<ul>
	<li><a title="How to create UML class diagrams" href="../how-to-create-uml-class-diagrams/">How to create UML class diagrams</a></li>
</ul>
