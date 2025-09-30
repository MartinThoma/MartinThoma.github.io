---
layout: post
lang: de
title: Abschlussaufgaben Programmieren
author: Martin Thoma
date: 2012-03-10 16:00:13.000000000 +01:00
category: German posts
tags: KIT, Klausur
featured_image: 2011/11/java-programming.png
---
<strong>Hinweis</strong>: Dieser Blogpost ist vermutlich nur f&uuml;r Informatik-Studenten am KIT im WS 2011 / 2012 interessant!

Hier ein paar Hinweise zu den Abschlussaufgaben aus dem Forum. Dabei habe ich die Antworten von jgraf, mmohr und praktomat genommen.

<h2>Allgemeines</h2>
<ul>
  <li>Was wir absolut nicht sehen wollen sind grosse Methoden, die verstreut &uuml;ber den ganzen Code diverse returns enth&auml;lt. Eventuell sollte man diese Methode dann ohnehin in Hilfsmethoden aufteilen.</li>
  <li>Parameter: Die Anzahl der Parameter muss exakt stimmen. Sind zu &uuml;berz&auml;hlige Parameter vorhanden, muss ein Fehler ausgegeben werden.</li>
  <li>toString/equals: Sollte nur f&uuml;r Klassen geschrieben werden, bei denen es Sinn macht. Vor allem auf eins aufpassen: Wenn man equals &uuml;berschreibt, dann sollte man auch hashCode &uuml;berschreiben (siehe <a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/lang/Object.html#equals(java.lang.Object">docs.oracle.com</a>) bzw, beliebige suche nach "equals hashCode"). Mir fallen spontan wenige F&auml;lle ein, wo es keinen Sinn macht, equals()/hashCode() oder toString() zu &uuml;berschreiben. Die Shell ist vielleicht so ein Fall, oder auch Utility-Klassen. </li>
  <li>Verbergt die tats&auml;chlichen Typen, woimmer es m&ouml;glich ist! Also z.B. <code>private Map meineMap = new HashMap<Integer, Blub>();</code></li>
</ul>

<blockquote>Frage: D&uuml;rfen Strings direkt im Programmcode stehen, oder sollten diese gesammelt am Beginn einer Klasse stehen?</blockquote>

Antwort: Kommt darauf an, wenn Sie mehr als eimal verwendet werden, dann sollte man Konstanten daraus machen.

<blockquote>Frage: Soll die Shell nur korrekte Werte an den eigentlichen LittlePraktomat &uuml;bergeben, also alle Fehlerquellen bereits in der Shell-Klasse abgefangen werden oder soll der LittlePraktomat Exceptions werfen, die in der Shell dann gefangen werden? Oder soll beides gemacht werden?</blockquote>

Antwort: Die &ouml;ffentlichen Methoden einer Klasse sind deren Schnittstelle. In den Javadoc Kommentaren sollte stehen, wie diese Schnittstelle zu verwenden ist. Also welcher Art die Eingaben sein m&uuml;ssen und wie die Ausgaben aussehen. Wenn sich ein Aufrufer nicht and diese Vereinbarung h&auml;lt, dann sollte die Methode der Schnittstelle eine Exception werfen (IllegalArgument, NullPointer, ...). Diese Exceptions sollten normalerweise nie vom Aufrufer gefangen werden. Sie sollen das Program kontrolliert zum Absturz bringen. Die Logik dahinter ist folgende: Wenn eine IllegalArgumentException (oder &auml;hnliches) fliegt, dann wurde eine Schnittstelle falsch verwendet. Der Aufrufer der Schnittstelle hat aber vor dem Aufruf sicher zu stellen, dass alle Forderungen der Schnittstelle eingehalten werden. D.h. wenn eine solche Exception auftritt liegt ein Programmierfehler vor. Mit Hilfe des Exceptionstacktrace kann der Entwickler diesen realtiv bequem finden und beheben.

Es ist also beides zu machen, die Shell (der Aufrufer) hat vor dem Verwenden der Praktomat-Schnittstelle sicher zu stellen, dass alle Eingaben korrekt sind. Sind die Eingaben falsch, dann wird eine Fehlermeldung ausgegeben. Die Praktomat-Schnittstelle sch&uuml;tzt sich vor falscher Verwendung mit Hilfe von Exceptions.

<h2>Tests</h2>
Ihr <strong>m&uuml;sst</strong> eine Tests.txt mit abgeben. Die ist wie ein Beispiel aufgebaut und sollt wichtige Eingaben / Ausgaben enthalten, die eventuell zu Fehlern f&uuml;hren k&ouml;nnten.

Da ihr sie ja sowieso schreibt, k&ouml;nnt ihr euer Programm auch auf eure Tests.txt &uuml;berpr&uuml;fen. Ich habe mir dazu folgendes kleines <a href='../images/2012/03/programmieren-abschlussaufgabe.zip'>Python-Script zum Vergleichen</a> gebastelt und vergleiche dann den normalisierten realen Output mit hilfe von <a href="http://wiki.ubuntuusers.de/Meld">Meld</a> mit dem erwartetem Output.

Also folgendes in der Bash:
```bash
python checkTests.py
meld ../tmp/createdOutputNormalized.txt ../tmp/compareTo.txt
```

Ihr m&uuml;sst halt noch die Pfade anpassen.

<h2>Abschlussaufgabe 1</h2>
Folgendes zum LittlePraktomat:
<ul>
  <li>Falls die Namen von Personen etwas anderes als Kleinbuchstaben haben (also z.B. Gro&szlig;buchstaben!) soll ein Fehler ausgegeben werden. &auml;&ouml;&uuml; m&uuml;ssen nicht als Kleinbuchstaben erkannt werden, a-z reicht.</li>
</ul>

<h2>Abschlussaufgabe 2</h2>
Folgendes zu <a href="http://de.wikipedia.org/wiki/Othello_(Spiel)">Othello</a>:
<ul>
<li>Wer sehr schnell die Aufgabe erledigt hatte (also noch am ersten Tag), dem fehlen hier eventuell ein paar Sachen. Habt ihr den hole-Befehl? Falls ja, ist alles ok. Sonst solltet ihr nochmals rein schauen und eure L&ouml;sung nochmals hochladen, weil eine veraltete Aufgabenstellung zu beginn hochgeladen wurde.</li>
<li>Eine g&uuml;ltige Spielfeldgr&ouml;&szlig;e MUSS gerade breite / h&ouml;he haben, gr&ouml;&szlig;er als 0x0 sein und kleiner gleich 26x98 sein.</li>
<li>Ein g&uuml;ltiges Rechteck MUSS die erste Koordinate links oben und die zweite rechts unten haben!</li>
</ul>

Es gibt folgende Befehle:
<ul>
  <li>newGame <Breite> <H&ouml;he> [<Stellung>]</li>
  <li>hole <Rechteck></li>
  <li>move <Position></li>
  <li>print</li>
  <li>abort</li>
  <li>possibleMoves</li>
  <li>quit</li>
</ul>

<h2>Daten</h2>
<strong>Abschlussaufgabe 1</strong>: 01.02.2012 - 12.03.2012
Funktionalit&auml;t: 0 - 7 Punkte
Programmiermethodik: 0 - 7 Punkte
Endnote = (2 &middot; Funktionalit&auml;t + Programmiermethodik)

<strong>Abschlussaufgabe 2</strong>: 13.02.2012 - 26.03.2012, 13:00 Uhr
Funktionalit&auml;t: 0 - 7 Punkte
Programmiermethodik: 0 - 7 Punkte
Endnote = (2 &middot; Funktionalit&auml;t + Programmiermethodik)

<h2>Ergebnisse</h2>
Mir wird, wenn ich im Abschlussaufgaben-Praktomat auf "Home" klicke, bereits angezeigt, dass es anscheinend maximal 24 Punkte auf die "Abschlu&szlig;aufgabe 1: Little Praktomat" gibt. Bin ja mal gespannt, wann es Ergebnisse gibt.

Es gab jeweils auf Funktionalit&auml;t und Programmiermethodik 14 Punkte, wobei die Punktzahl der Funktionalit&auml;t verdoppelt wurde. Damit kommen wir insgesamt auf 2 * (14*2 + 14)= 84 Punkte. Der Notenschl&uuml;ssel ist wie folgt:

<table>
<tr><th>Bewertungspunkte</th><th>Gesamtnote</th></tr>
<tr><td>82,0 - 84,0</td><td>1,0</td></tr>
<tr><td>78,0 - 81,5</td><td>1,3</td></tr>
<tr><td>74,0 - 77,5</td><td>1,7</td></tr>
<tr><td>70,0 - 73,5</td><td>2,0</td></tr>
<tr><td>66,0 - 69,5</td><td>2,3</td></tr>
<tr><td>62,0 - 65,5</td><td>2,7</td></tr>
<tr><td>58,0 - 61,5</td><td>3,0</td></tr>
<tr><td>54,0 - 57,5</td><td>3,3</td></tr>
<tr><td>50,0 - 53,5</td><td>3,7</td></tr>
<tr><td>46,0 - 49,5</td><td>4,0</td></tr>
<tr><td>0 - 45,5</td><td>5,0 - nicht bestanden</td></tr>
</table>

<h2>Meine Abgabe</h2>
<ul>
  <li>LittlePraktomat: <a href="http://www.martin-thoma.de/programmieren-little-praktomat/class-diagram/class-diagram.pdf">Klassendiagramm</a> + <a href="http://www.martin-thoma.de/programmieren-little-praktomat/">JavaDoc</a> + <a href='../images/2012/03/little-praktomat.zip'>Java Source Code</a></li>
  <li>Othello: <a href="http://www.martin-thoma.de/programmieren-othello/">JavaDoc</a> + <a href='../images/2012/03/othello.zip'>Java Source Code</a></li>
</ul>

<h3>Fehlerquellen</h3>
Es wurde bem&auml;ngelt, dass ich wenig Kommentare hab. Ich finde, ich habe wahnsinnig viele ...

<h4>LittlePraktomat</h4>
<strong>Test 4</strong>:
Eingabe: list-solutions 99999999999999999999
Exception in thread "main" java.lang.NumberFormatException - die Zahl ist zu gro&szlig;
<strong>Test 7</strong>: Aus Bl&ouml;dheit nicht bestanden ... ich habe eine Funktion (das wechseln von Tutoren) nicht &uuml;berpr&uuml;ft.

<h4>Othello</h4>
<strong>Test 6 b</strong>: Direkt nach dem Start des Programms "hole A1:A1" hat eine (meiner eigenen) Exceptions geworfen ... bzw. mit korrekter Angabe, wo der Fehler liegt ... also auch Dummheit *argh*
