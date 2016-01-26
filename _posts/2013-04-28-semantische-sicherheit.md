---
layout: post
title: Semantische Sicherheit
author: Martin Thoma
date: 2013-04-28 15:06:53.000000000 +02:00
categories:
- German posts
tags:
- IT-Security
- Theoretical computer science
featured_image: 2013/04/cryptography-thumb.png
---
In der <a href="http://www.iks.kit.edu/fileadmin/User/Lectures/Sicherheit/SoSe13/Sicherheit_VL03.pdf">Vorlesung vom 25.04.2013</a> hat Prof. Hofheinz gesagt, dass man semantische Sicherheit praktisch nicht beweisen kann, da man zuerst <span markdown="0">\(\mathcal{P} \neq \mathcal{NP}\)</span> beweisen müsste. Warum das so ist, versuche ich nun zu erläutern.

<h2>Einwegfunktionen und <span markdown="0">\(\mathcal{P} \neq \mathcal{NP}\)</span></h2>
<div class="definition">
Sei <span markdown="0">\(f:X \rightarrow Y\)</span> eine Funktion.
<span markdown="0">\(f\)</span> hei&szlig;t eine Einwegfunktion, genau dann wenn für alle <span markdown="0">\(x \in X\)</span> gilt:
<ul>
  <li><span markdown="0">\(y := f(x)\)</span> kann in Polynomialzeit berechnet werden</li>
  <li>Für die Berechnung eines Urbildes <span markdown="0">\(x\)</span> aus <span markdown="0">\(y\)</span> existiert kein randomisierter Algorithmus, der in Polynomialzeit läuft.</li>
</ul>
</div>

Es gilt: Wenn eine Einwegfunktion <span markdown="0">\(f\)</span> existiert, dann gilt <span markdown="0">\(\mathcal{P} \neq \mathcal{NP}\)</span>.

Warum?

Nun, angenommen es gibt eine Einwegfunktion <span markdown="0">\(f\)</span>. Dann sei die formale Sprache <span markdown="0">\(L_f\)</span> definiert durch:

<span markdown="0">\(L_f := \{(\bar x, y) | \exists x: \bar x \text{ ist Präfix von } x \text{ und } y = f(x)\}\)</span>

Es gilt: <span markdown="0">\(L_f \notin \mathcal{P}\)</span>, da für ein gegebenes <span markdown="0">\(y\)</span> das zugehörige <span markdown="0">\(x\)</span> in polynomialzeit bestimmt werden könnte (wie will man sonst prüfen, ob <span markdown="0">\(\bar x\)</span> ein Präfix von <span markdown="0">\(x\)</span> ist?)

Falls jemanden diese Begründung nicht ausreicht ist hier noch ein Beweis von Prof. Hofheinz (Danke!)

<strong>Beh.:</strong> <span markdown="0">\(L_f \notin \mathcal{P}\)</span><br/>
<strong>Bew.:</strong> durch Widerspruch<br/>
<u>Annahme.:</u> <span markdown="0">\(L_f \in P\)</span><br/>
<span markdown="0">\(\Rightarrow\)</span> Es existiert ein Polyzeit-Algorithmus <span markdown="0">\(\mathcal{A}\)</span> für <span markdown="0">\(L_f\)</span>, der bei Eingabe <span markdown="0">\((\bar x, y)\)</span> entscheidet, ob ein <span markdown="0">\(x\)</span> mit <span markdown="0">\(f(x)=y\)</span> und Präfix <span markdown="0">\(\bar x\)</span> existiert oder nicht. Dann können wir einen Algorithmus <span markdown="0">\(\mathcal{B}\)</span> aus <span markdown="0">\(\mathcal{A}\)</span> bauen, der <span markdown="0">\(f\)</span> invertiert.

Gegeben <span markdown="0">\(y\)</span> verfährt <span markdown="0">\(\mathcal{B}\)</span> wie folgt:
<span markdown="0">\(\mathcal{B}\)</span> ruft <span markdown="0">\(\mathcal{A}(0,y)\)</span> auf und erfährt so, ob ein Urbild <span markdown="0">\(x\)</span> von <span markdown="0">\(y\)</span> mit Anfangsbit <span markdown="0">\(0\)</span> existiert. Wenn ja, ruft <span markdown="0">\(\mathcal{B}\)</span> den Algorithmus <span markdown="0">\(\mathcal{A}(00,y)\)</span> auf, wenn nein ruft <span markdown="0">\(\mathcal{B}\)</span> den Algorithmus <span markdown="0">\(\mathcal{A}(10,y)\)</span> auf usw.

So wird ein Urbild <span markdown="0">\(x\)</span> bitweise bestimmt. Ein solches <span markdown="0">\(\mathcal{B}\)</span> findet also effizient Urbilder, im Widerspruch zur Einwegannahme über <span markdown="0">\(f \blacksquare\)</span>

Aber: Wenn das <span markdown="0">\(x\)</span> gegeben ist, dann ist es einfach zu zeigen, dass <span markdown="0">\(y= f(x)\)</span> gilt und damit auch, ob <span markdown="0">\(\bar x\)</span> ein Präfix von <span markdown="0">\(x\)</span> ist. Damit ist <span markdown="0">\(L_f \in \mathcal{NP}\)</span>.

Damit gilt: <span markdown="0">\(L_f \in \mathcal{NP} \setminus \mathcal{P}\)</span>.
Wenn aber <span markdown="0">\(\mathcal{NP} \setminus \mathcal{P} \neq \emptyset\)</span>, dann gilt insbesondere <span markdown="0">\(\mathcal{P} \neq \mathcal{NP}\)</span>.

An dieser Stelle sollte man also einsehen, dass eine Einwegfunktion nach obiger Definition nur existieren kann, wenn <span markdown="0">\(\mathcal{P} \neq \mathcal{NP}\)</span> gilt.

<h2>Semantische Sicherheit</h2>
<a href="http://de.wikipedia.org/wiki/Sicherheitseigenschaften_kryptografischer_Verfahren#Semantische_Sicherheit">Wikipedia</a> gibt folgende Beschreibung von semantischer Sicherheit:

<blockquote>Ein Verschlüsselungsverfahren ist semantisch sicher, wenn jeder Angreifer jede Information, die er aus einem Chiffrat über die Nachricht ableiten kann, bereits dann ableiten kann, wenn er nur die Länge des Chiffrats kennt. Ein Chiffrat verrät also nichts über eine Nachricht als ihre Länge.</blockquote>



Herr Prof. Hofheinz hat folgende informelle Definition von Semantischer Sicherheit in der Vorlesung gegeben:

<div class="definition">
Ein symmetrisches Verschlüsselungsverfahren ist semantisch sicher, wenn es für jede <span markdown="0">\(M\)</span>-Verteilung, jede Funktion <span markdown="0">\(f\)</span> und jeden PPT-Algorithmus <span markdown="0">\(\mathcal{A}\)</span> einen PPT-Algorithmus <span markdown="0">\(\mathcal{B}\)</span> gibt, so dass

<span markdown="0">\(Pr \left [\mathcal{A}^{\text{Enc}(K, \cdot)}(\text{Enc}(K, M)) = f(M) \right ] - Pr [\mathcal{B}(\varepsilon) = f(M)]\)</span>

vernachlässigbar (als Funktion im Sicherheitsparameter <span markdown="0">\(K\)</span>) ist.
</div>

Hier ist 
<ul>
  <li><span markdown="0">\(M\)</span> eine Nachricht (Message),</li>
  <li><span markdown="0">\(\text{Enc(K, M)}\)</span>  die Verschlüsselung einer konkreten Nachricht <span markdown="0">\(M\)</span> mit dem Schlüssel <span markdown="0">\(K\)</span>,</li>
  <li><span markdown="0">\(\varepsilon\)</span> eine triviale Information (ich glaube das ist z.B. die Länge des Ciphertextes) und</li>
  <li><span markdown="0">\(f\)</span> extrahiert beliebige Informationen aus dem Plaintext</li>
</ul>

Die erste Wahrscheinlichkeit bezeichnet die Möglichkeit, aus dem Ciphertext Informationen der Art <span markdown="0">\(f\)</span> über den Plaintext <span markdown="0">\(M\)</span> zu erhalten.
Die zweite Wahrscheinlichkeit bezeichnet die Möglichkeit &bdquo;aus dem Nichts&ldquo; Informationen über eine Nachricht zu erhalten. Damit will man triviale Informationen eliminieren. Insgesamt gibt es also die Wahrscheinlichkeit an, nicht-triviale Informationen aus einer Verschlüsselten Nachricht zu erhalten. Mit effizient ist vermutlich in Polynomialzeit gemeint.

Wenn es nun mehrfach benutzbare semantisch sichere Verfahren gibt, dann kann man dieses Verfahren als Einwegfunktion nutzen. Wenn eine Einwegfunktion existiert, gilt <span markdown="0">\(\mathcal{P} \neq \mathcal{NP}\)</span>. Also folgt:

Wenn es nun mehrfach benutzbare semantisch sichere Verfahren existieren, gilt <span markdown="0">\(\mathcal{P} \neq \mathcal{NP}\)</span>. Dies ist aber eines der <a href="http://de.wikipedia.org/wiki/Millennium-Probleme">Millennium-Probleme</a> und noch nicht geklärt.
