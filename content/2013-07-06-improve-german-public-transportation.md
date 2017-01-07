---
layout: post
title: Improve German Public Transportation
author: Martin Thoma
date: 2013-07-06 20:45:32.000000000 +02:00
category: Cyberculture
tags: Google, Public Transportation, Google Maps
featured_image: 2013/07/bus.png
---
Public transportation in Germany is much worse than it could be. I've got quite angry today because of that and thought about ways to improve the situation.

<strong>A story from today:</strong>
I've bought two tickets to get from Karlsruhe to Augsburg (230 km) in about a month. I wanted to visit my dad in summer break just after an exam. I've bought a fixed connection to get there for "only" 35 Euro instead of 59 Euro. But I've made a mistake, my conenction started to early. Two hours after having bought the tickets, I wanted to exchange them for a connection that starts later. But I had to pay 15 Euro for exchanging them, 15 Euro for canceling the connection. And it got worse: I had to give them my home address to get at least some of the money back. For what the hell do they need my home address?

<h2>What could get improved?</h2>

<ul>
  <li>Most people basically choose one company: <a href="http://en.wikipedia.org/wiki/Deutsche_Bahn">Deutsche Bahn</a></li>
  <li>It's too expensive.</li>
  <li>Customer service of "Deutsche Bahn" is very bad.</li>
  <li>Delays of at least 10 minutes always happen VERY often, delays of more than 30 minutes happen from time to time; I already had delay of more than 2 hours.</li>
</ul>

<h2>Alternative companies</h2>
Most people choose "Deutsche Bahn" (short: DB) because it is the biggest company that provides public transportation when you want to travel between cities. DB is well known and connects all big cities. However, there are alternatives.

After a law (&sect; 13 Abs. 2 of the <a href="http://de.wikipedia.org/wiki/Personenbef%C3%B6rderungsgesetz_(Deutschland)">Personenbef&ouml;rderungsgesetz</a>) was annulled, bus companies provided alternatives to traveling by train. Some companies are:

<ul>
  <li><a href="http://meinfernbus.de/">MeinFernbus.de</a></li>
  <li><a href="http://www.univers-reisen.de/">univers-reisen.de</a></li>
  <li><a href="http://www.city2city.de/">City2City.de</a></li>
</ul>

But they are difficult to find and people maybe don't trust in them.

<h2>Informing people</h2>
<a href="https://www.google.com/intl/de/landing/transit/#dmy">Google Transit</a>, <a href="https://www.fahrtenfuchs.de/">FahrtenFuchs.de</a> and <a href="http://www.busliniensuche.de/">Busliniensuche.de</a> provide one possibility to inform people. But they all seem to have only a few bus companies.

Google Transit is interesting as they provide <a href="https://developers.google.com/transit/gtfs/reference?hl=en">format specification</a> for exchanging transit information.

<h2>What could be done</h2>
<ul>
  <li>Contact bus companies and ask them if they want to provide transit information to the public in Google Transit Feed Format. You might want to hint them to <a href="http://maps.google.com/help/maps/mapcontent/transit/index.html">Google Transit Partner Program</a>.
    <ul>
      <li>I've contacted "meinfernbus.de" (Saturday, 06.07.2013). Lets see if they answer.</li>
      <li>Contacted "KVV.de" (Saturday, 06.07.2013)</li>
      <li>Contacted "avv-augsburg.de" (Saturday, 06.07.2013)</li>
    </ul>
  </li>
  <li>Write software that allows bus companies to get their data into Google Transit Format
    <ol>
      <li>Write standard relational SQL database to store the required information</li>
      <li>Create <abbr title="user interface">UI</abbr> scribbles (e.g. with <a href="../how-can-i-sketch-an-application/" title="How can I sketch an application?">Balsamiq</a>)</li>
      <li>Write software</li>
    </ol>
  </li>
</ul>

<h2>Some reactions</h2>
<h3>AVV (Augsburg)</h3>
My email from 06.07.2013 to kundencenter@avv-augsburg.de:
<blockquote>Sehr geehrte Damen und Herren,

ich habe gerade gesehen, dass Google die M&ouml;glichkeit anbietet, die Fahrplaninformationen in Google Maps einzubinden:
http://maps.google.com/help/maps/mapcontent/transit/index.html

K&ouml;nnten Sie das anbieten? Es ist vermutlich deutlich einfacher, die Fahrplanauskunft von Google zu nutzen als auf die AVV-Seite zu gehen.

Mit freundlichen Gr&uuml;&szlig;en,
Martin Thoma</blockquote>



No reaction by now (21.07.2013)

<h3>KVV (Karlsruhe)</h3>
They have called me on 07.07.2013 and told me that they plan to bring the information to Google Maps, although they don't know how long it will take.

<h3>MeinFernbus.de</h3>
My email from 06.07.2013:


<blockquote>Sehr geehrte Damen und Herren,

ich habe mich heute sehr &uuml;ber die Deutsche Bahn ge&auml;rgert und auf der Suche
nach Alternativen meinfernbus.de gefunden. Allerdings habe ich zuerst &uuml;ber
Google Maps nach Busverbindungen zwischen Karlsruhe und Augsburg gesucht,
wo mir leider nur die Bahn angeboten wurde.

Haben Sie schon von Google
Transit<http://maps.google.com/help/maps/mapcontent/transit/index.html>geh&ouml;rt?
Was halten Sie davon, an diesem Programm teilzunehmen?

Mit freundlichen Gr&uuml;&szlig;en,
Martin Thoma</blockquote>



Answer from 08.07.2013:
<blockquote>Sehr geehrter Herr Thoma,
 
bitte entschuldigen Sie die sp&auml;te Antwort.
 
Vielen Dank f&uuml;r Ihre Email, Ihre Kooperationsanfrage ist bei uns eingegangen. Wir freuen uns sehr, dass Sie mit MeinFernbus.de, dem Marktf&uuml;hrer im deutschen Fernbusverkehr, zusammenarbeiten m&ouml;chten.
 
Wir pr&uuml;fen gerne eine entsprechende Zusammenarbeit. Zu gegebener Zeit setzt sich unser Kooperationsmanager mit Ihnen in Verbindung. Aufgrund der Vielzahl eingehender Anfragen bitten wir Sie zun&auml;chst noch um etwas Geduld.
 
Vielen Dank f&uuml;r Ihr Verst&auml;ndnis, herzliche Gr&uuml;&szlig;e aus der Hauptstadt
               
Friederike Freytag</blockquote>



<h2>See also</h2>
<ul>
  <li><a href="//www.youtube.com/watch?v=j6dCCq0XL6w">Reisetagebuch</a> (A German comedian)</li>
</ul>
