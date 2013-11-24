---
layout: post
status: publish
published: true
title: LaTeX-Vorlage f&uuml;r ein Lastenheft
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 23211
wordpress_url: http://martin-thoma.com/?p=23211
date: 2012-04-26 13:51:07.000000000 +02:00
categories:
- German posts
tags:
- Software Development
- LaTeX
- KIT
- SWT I
- Lastenheft
- MetaUML
comments:
- id: 120661
  author: ano
  author_email: ano@ano.com
  author_url: ''
  date: !binary |-
    MjAxMi0wNC0yNyAxNToxNDozMiArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNC0yNyAxMzoxNDozMiArMDIwMA==
  content: merci!
- id: 120751
  author: Peter M.
  author_email: peter.merkert@gmx.de
  author_url: http://petermerkert.com
  date: !binary |-
    MjAxMi0wNC0yNyAxNjoxODo1MiArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNC0yNyAxNDoxODo1MiArMDIwMA==
  content: ! "Super! Hab ich endlich ne gute Vorlage. Meine war noch nicht ganz ausgereift.
    Gerade die  Tabellen sehen sehr gut aus!\r\n\r\nViele Gr&uuml;&szlig;e,\r\nPeter"
- id: 120791
  author: Niklas B.
  author_email: white57@gmx.net
  author_url: ''
  date: !binary |-
    MjAxMi0wNC0yNyAxODo0NTo0MiArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNC0yNyAxNjo0NTo0MiArMDIwMA==
  content: Great stuff.
- id: 1119951
  author: hasan
  author_email: hasan_koc0@yahoo.com
  author_url: ''
  date: !binary |-
    MjAxMy0wMS0xNSAxMjo1MDo0OCArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMS0xNSAxMTo1MDo0OCArMDEwMA==
  content: ! "Hey Martin,\r\n\r\nden Beitrag finde ich echt gut.\r\n\r\nIch habe Probleme
    beim Glossar, der taucht irgendwie in meinem Dokument nicht auf. Woran k&ouml;nnte
    das liegen?\r\n\r\nLG\r\nHasan"
- id: 1120861
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wMS0xNyAxMzozNDoyNyArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMS0xNyAxMjozNDoyNyArMDEwMA==
  content: ! "Hallo Hasan,\r\n\r\nsch&ouml;n, dass es dir gef&auml;llt. Wenn du dir
    die \"Makefile\" anschaust, siehst du, dass folgendes ausgef&uuml;hrt wird:\r\n\r\n<blockquote>\tmpost
    usecase.mp\r\n\tpdflatex Lastenheft.tex -output-format=pdf\r\n\tmakeglossaries
    Lastenheft\r\n\tpdflatex Lastenheft.tex -output-format=pdf\r\n\tpdflatex durchfuhrbarkeit.tex
    -output-format=pdf</blockquote>\r\n\r\n\r\n\r\nIch vermute mal, dass du die
    Makefile nicht benutzt hast und daher \"makeglossaries\" nicht ausgef&uuml;hrt
    hast. Oder eventuell hast du das Programm makeglossaries gar nicht.\r\n\r\nEventuell
    hilft dir folgender Link: <a href=\"http://tex.stackexchange.com/a/25961/5645\"
    rel=\"nofollow\">How to use 'makeglossaries'?</a>\r\n\r\nGr&uuml;&szlig;e,\r\nMartin"
---
Ich habe gerade mal schnell eine Vorlage f&uuml;r ein Lastenheft mit LaTeX erstellt. Dieses Lastenheft beinhaltet sogar ein kleines Use-Case Beispiel, das mit MetaUML realisiert wurde. Hier ist die <a href='http://martin-thoma.com/wp-content/uploads/2012/04/Lastenheft.pdf'>PDF</a>, hier der <a href='http://martin-thoma.com/wp-content/uploads/2012/04/Lastenheft.zip'>LaTeX-Code</a>. 

Das Lastenheft k&ouml;nnt ihr unter Linux einfach mit folgendem Befehl erstellen, wenn ihr in diesem Ordner seid:
[bash]make[/bash]


&Auml;nderungsvorschl&auml;ge sind willkommen! Ich werde die hier gespeicherte Version wohl noch einige male updaten.


<h2>Siehe auch</h2>
<ul>
  <li><a href="http://www.st.cs.uni-saarland.de/edu/se1/skript/notes.pdf">Softwaretechnik I</a>, S. 36</li>
  <li><a href="http://www2.cs.uni-paderborn.de/cs/ag-schaefer/Lehre/Lehrveranstaltungen/Praktika/Softwaretechnikpraktikum/SS06/Dokumentvorlagen/Lastenheft-Template.pdf">Beispiel der Uni Paderborn</a></li>
  <li><a href="http://next-internet.com/hauptstudium/texte/swt_summary.pdf">Jet Another SWT-I Resume</a>, ab S. 8</li>
</ul>
