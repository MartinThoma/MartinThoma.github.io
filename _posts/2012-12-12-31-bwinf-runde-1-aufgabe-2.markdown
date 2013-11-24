---
layout: post
status: publish
published: true
title: 31. BwInf - Runde 1, Aufgabe 2
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 46841
wordpress_url: http://martin-thoma.com/?p=46841
date: 2012-12-12 12:12:58.000000000 +01:00
categories:
- German posts
tags:
- BWInf
- ! '#glpk'
comments: []
---
<h2>Die Aufgabenstellung</h2>
<blockquote>Zum Transport von Geld werden schwer bewachte Geldtransporter eingesetzt. In einem solchen Geldtransporter k&ouml;nnen Koffer mit M&uuml;nzen transportiert werden. Die Koffer enthalten M&uuml;nzen in unterschiedlicher Menge und mit unterschiedlichem Gesamtwert. Entsprechend unterscheiden sich die Koffer in Gewicht und Wert.

Da kommt so einiges an Gewicht zusammen. Es ist daher notwendig, den Transporter gleichm&auml;&szlig;ig zu beladen, so dass er nicht zu einer Seite umkippen kann.

Unser Transporter hat links und rechts je einen Kofferraum. F&uuml;r jeden Kofferraum lassen sich Gesamtwert und Gesamtgewicht der darin enthaltenen Koffer bestimmen. Damit der Transporter keine Schlagseite bekommt, m&uuml;ssen die Koffer so einger&auml;umt werden, dass die Differenz zwischen den beiden Gesamtgewichten minimal ist. Aus versicherungstechnischen Gr&uuml;nden d&uuml;rfen die beiden Gesamtwerte sich au&szlig;erdem um h&ouml;chstens 10.000 Euro unterscheiden.</blockquote>

<blockquote>Schreibe ein Programm zur Verteilung der Geldkoffer auf die beiden Kofferr&auml;ume. &Uuml;berpr&uuml;fe dein Programm mit den auf <a href="http://www.bundeswettbewerb-informatik.de/index.php?id=1168">www.bundeswettbewerb-informatik.de</a> abgelegten Beispielen mit Angaben zu Werten und Gewichten der einzelnen Koffer.</blockquote>

Quelle: <a href="http://www.bundeswettbewerb-informatik.de/fileadmin/templates/bwinf/aufgaben/bwinf31/Aufgabenblatt311_Aufgaben.pdf">www.bundeswettbewerb-informatik.de</a>

<h2>Vollst&auml;ndiger Pseudocode</h2>
[caption id="attachment_46861" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/12/pseudocode-31.1.2-bwinf.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/12/pseudocode-31.1.2-bwinf.png" alt="Pseudocode zum 31. BwInf, Runde 1, Aufgabe 2" title="Pseudocode zum 31. BwInf, Runde 1, Aufgabe 2" width="512" height="412" class="size-full wp-image-46861" /></a> Pseudocode zum 31. BwInf, Runde 1, Aufgabe 2[/caption]

<h2>L&ouml;sung mit GLPK</h2>
Der folgende Code muss als partition.mod gespeichert werden:

[text]
/* PARTITION */

/* Written in GNU MathProg by Martin Thoma <info@martin-thoma.de> */

/* Given a set of items I = {1,...,m} with weight w[i] > 0, the 
   PARTITION problem is to split the set of items into two sets
   such that the absolute value of the difference of the sum of 
   weights of the two sets is minimal */

param m, integer, > 0;
/* number of items */

set I := 1..m;
/* set of items */

param w{i in 1..m}, > 0;
/* w[i] is weight of item i */

param v{i in 1..m}, > 0;
/* v[i] is value of item i */

param c, > 0;
/* maximum value difference */

param z{i in I, j in 1..m} :=
/* z[i,j] = 1 if item i is in bin j, otherwise z[i,j] = 0 */

   if i = 1 and j = 1 then 1
   /* put item 1 into bin 1 */

   else if exists{jj in 1..j-1} z[i,jj] then 0
   /* if item i is already in some bin, do not put it into bin j */

   else if sum{ii in 1..i-1} w[ii] * z[ii,j] + w[i] > c then 0
   /* if item i does not fit into bin j, do not put it into bin j */

   else 1;
   /* otherwise put item i into bin j */

check{i in I}: sum{j in 1..2} z[i,j] = 1;
/* each item must be exactly in one bin */

param n := 2;
display n;

set J := 1..n;
/* set of bins */

var x{i in I, j in J}, binary;
/* x[i,j] = 1 means item i is in bin j */

s.t. one{i in I}: sum{j in J} x[i,j] = 1;
/* each item must be exactly in one bin */

/* analog zu http://lists.gnu.org/archive/html/help-glpk/2007-08/msg00036.html */
s.t. lim1{j in J}: (sum{i in I} v[i] * x[i,1]) - (sum{i in I} v[i] * x[i,2]) <= c;
s.t. lim2{j in J}: (sum{i in I} v[i] * x[i,2]) - (sum{i in I} v[i] * x[i,1]) <= c;
/* the difference of the values may not be more than 10000 */

s.t. lim3{j in J}: (sum{i in I} w[i] * x[i,1]) - (sum{i in I} w[i] * x[i,2]) >= 0;

minimize obj: (sum{i in I} w[i] * x[i,1]) - (sum{i in I} w[i] * x[i,2]);
/* No abs because of linearity: http://old.nabble.com/How-to-get-a-variable's-absolute-value-with-GNU-mathprog-tt22241565.html*/
/* objective is to minimize the difference of weights */

data;

/* The optimal solution is 3 bins */

/*param m := 15;
param v := 1 96000, 2 126000, 3 115000, 4 125000, 5 123000, 6 123000, 7 112000, 8 111000, 9 110000, 10 110000, 11 120000, 12 98000, 13 130000, 14 87000, 15 97000;
param w := 1 27, 2 21, 3 27, 4 15, 5 19, 6 46, 7 47, 8 32, 9 14, 10 20, 11 50, 12 19, 13 22, 14 50, 15 46;

param m := 20;
param w := 1 27, 2 50, 3 19, 4 19, 5 22, 6 79, 7 32, 8 19, 9 75, 10 32, 11 43, 12 82, 13 18, 14 24, 15 20, 16 30, 17 24, 18 80, 19 49, 20 15;
param v := 1 276000, 2 745000, 3 585000, 4 585000, 5 723000, 6 808000, 7 552000, 8 584000, 9 626000, 10 551000, 11 423000, 12 944000, 13 496000, 14 133000, 15 633000, 16 461000, 17 813000, 18 855000, 19 695000, 20 406000;

param m := 30;
param w := 1 103, 2 100, 3 95, 4 119, 5 148, 6 165, 7 721, 8 89, 9 89, 10 156, 11 181, 12 93, 13 239, 14 173, 15 87, 16 113, 17 1816, 18 107, 19 128, 20 102, 21 102, 22 115, 23 118, 24 124, 25 244, 26 394, 27 100, 28 92, 29 103, 30 126;
param v := 1 42000, 2 31000, 3 20000, 4 20000, 5 20000, 6 20000, 7 180000, 8 9000, 9 9000, 10 18000, 11 18000, 12 28000, 13 28000, 14 17000, 15 121000, 16 14000, 17 579000, 18 13000, 19 13000, 20 12000, 21 12000, 22 12000, 23 12000, 24 12000, 25 33000, 26 65000, 27 22000, 28 11000, 29 11000, 30 11000;
*/

param m := 40;
param w := 1 3512, 2 87, 3 87, 4 90, 5 91, 6 91, 7 99, 8 218, 9 89, 10 91, 11 91, 12 92, 13 92, 14 93, 15 95, 16 99, 17 100, 18 263, 19 88, 20 89, 21 91, 22 92, 23 93, 24 97, 25 99, 26 99, 27 90, 28 97, 29 399, 30 298, 31 160, 32 854, 33 132, 34 986, 35 255, 36 88, 37 89, 38 92, 39 97, 40 98;
param v := 1 672000, 2 10000, 3 10000, 4 10000, 5 10000, 6 10000, 7 10000, 8 244000, 9 73000, 10 9000, 11 9000, 12 9000, 13 9000, 14 9000, 15 9000, 16 9000, 17 9000, 18 83000, 19 8000, 20 8000, 21 8000, 22 8000, 23 8000, 24 8000, 25 8000, 26 8000, 27 7000, 28 7000, 29 103000, 30 144000, 31 58000, 32 399000, 33 15000, 34 472000, 35 120000, 36 12000, 37 12000, 38 11000, 39 11000, 40 11000;

param c := 10000;

end;
[/text]

Jetzt muss man folgendes ausf&uuml;hren:
[bash]glpsol --output example.out --log example.log --math partition.mod[/bash]

Das ben&ouml;tigt f&uuml;r die gr&ouml;&szlig;te Eingabe etwa 18 Sekunden.

Wenn man nun in die example.out schaut, sieht man unter anderem folgendes:

[text]
Problem:    partition
Rows:       47
Columns:    80 (80 integer, 80 binary)
Non-zeros:  640
Status:     INTEGER OPTIMAL
Objective:  obj = 5 (MINimum)
[/text]

Die interessante Zahl ist die 5. Das ist das Minimum, das in dieser Aufgabe gesucht war. Wie es zu erreichen ist, sieht  man in der Ausgabe darunter.

<h2>Weiteres</h2>
Man kann das Problem auch als MULTIPROCESSOR SCHEDULING mit zwei Maschinen betrachten (und nicht als PARTITION). Vor ein paar Tagen habe ich gelernt, dass es f&uuml;r MULTIPROCESSOR SCHEDULING auch ein <a href="http://de.wikipedia.org/wiki/Approximationsalgorithmus#PTAS.2FPAS">PAS</a> gibt. Dabei bestimmt man f&uuml;r eine konstante Anzahl an Koffern die optimale aufteilung und verteilt den rest mittels LIST SCHEDULING.
