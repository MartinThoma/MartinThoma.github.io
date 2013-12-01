---
layout: post
status: publish
published: true
title: Tribonacci-Folge
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 48961
wordpress_url: http://martin-thoma.com/?p=48961
date: 2012-11-19 20:52:00.000000000 +01:00
categories:
- Code
tags:
- Programming
- Java
comments:
- id: 393281
  author: Simon
  author_email: simon.schaefer4@student.kit.edu
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0xOSAyMjoyOTozMCArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xOSAyMDoyOTozMCArMDEwMA==
  content: ! "Rekursion muss nicht \"schwach\" sein wenn man es vern&uuml;nftig implementiert.
    Mit Akkumulatoren kann man tail-recursion realisieren, die vom Compiler komplett
    wegoptimiert werden kann (wobei weder der Java Compiler noch der Python Interpreter
    dies beherrschen) und somit keinen Stack ben&ouml;tigt bzw. Doppelberechnungen
    durchf&uuml;hrt.\r\n\r\nK&ouml;nnte in Haskell so aussehen: https://gist.github.com/4113654\r\n\r\nDurch
    corecursion+lazy evaluation kann man Code schreiben, der ebenfalls keinen Stack
    ben&ouml;tigt und auch nichts doppelt berechnet.\r\n\r\nIn Haskell w&uuml;rde
    dies so aussehen: https://gist.github.com/4113670\r\n\r\nWas nichts
    anderes als eine unendliche Liste ist, deren letzten 3 Elemente addiert werden
    und das resultierende Ergebnis als neues Element an die Liste geh&auml;ngt wird."
- id: 393291
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0xMS0xOSAyMjozMjowNyArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xOSAyMDozMjowNyArMDEwMA==
  content: Das Problem bei Rekursion ist, dass man deutlich mehr Wissen reinstecken
    muss, um eine &auml;hnlich gute L&ouml;sung zu bekommen wie mit einer iterativen
    L&ouml;sung.
- id: 393311
  author: Keba
  author_email: mariofuest@aol.com
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0xOSAyMjo1NDoxNiArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xOSAyMDo1NDoxNiArMDEwMA==
  content: Gibt es eigentlich auch Probleme, die iterativ deutlich schwerer/komplizierter
    sind  als ihre rekursiven Verwandten?
- id: 394341
  author: Simon
  author_email: simon.schaefer4@student.kit.edu
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0yMCAwMToyNToxNyArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xOSAyMzoyNToxNyArMDEwMA==
  content: Daf&uuml;r m&uuml;sste man vermutlich erst definieren was man unter "gute
    L&ouml;sung" versteht. Lernen muss man wahrscheinlich mehr, daf&uuml;r ben&ouml;tigt
    man dann wahrscheinlich weniger Zeit um die L&ouml;sung f&uuml;r ein Problem zu
    formulieren. Eine entscheidende Frage d&uuml;rfte sein ob der Zeitaufwand es Wert
    ist sich tiefer mit Rekursion zu besch&auml;ftigen als es die meisten Leute tun.
- id: 394351
  author: Simon
  author_email: simon.schaefer4@student.kit.edu
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0yMCAwMToyODo0MCArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xOSAyMzoyODo0MCArMDEwMA==
  content: ! "Kommt vermutlich darauf an wie du \"schwierig\" definierst. In Haskell
    kann ich dir in unter 10s die Fibonacci-Sequenz niederschreiben:\r\n\r\nfib =
    1 : scanl (+) 1 fib\r\n\r\nVergleichbares schaffst du in keiner imperativen Programmiersprache
    in dieser Zeit."
- id: 394611
  author: Simon
  author_email: simon.schaefer4@student.kit.edu
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0yMCAwMjozMTo0NSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0yMCAwMDozMTo0NSArMDEwMA==
  content: ! "Finde ich wichtig es noch zu erw&auml;hnen: Viel wichtiger als die Diskussion
    \"Was ist schneller/einfacher - iterativ oder rekursiv?\" ist sich bewusst
    zu werden, dass eine abstrakte L&ouml;sung, die die konkrete Implementierung offen
    l&auml;sst, das Optimale sein kann. Z.B. macht es Sinn &uuml;ber Funktionen wie
    map, filter, fold oder scan die Funtionsweise eines Algo zu beschreiben und dessen
    genauer Ablauf dem Implementierer dieser Funktionen zu &uuml;berlassen, der vermutlich
    eine weitaus bessere Implementierung erstellen kann als es den meisten Entwicklern
    m&ouml;glich w&auml;re.\r\n\r\nIn dem Haskell Beispiel zu Fibonacci z.B. ist nirgendwo
    vorgeschrieben ob scanl rekursiv oder iterativ implementiert ist, lediglich der
    Algo zur Berechnung der Zahlen ist rekursiv definiert was aber nicht hei&szlig;t,
    dass er auch rekursiv ausgef&uuml;hrt wird."
- id: 417071
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0xMS0yMiAyMzoyNToxMCArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0yMiAyMToyNToxMCArMDEwMA==
  content: Auf diesem Level davon zu reden, dass man nicht vorgibt, wie es ausgef&uuml;hrt
    wird, finde ich schwer. Am Ende wird es sowieso alles in GOTO-Code umgewandelt,
    oder? Kann man da noch von Rekursion reden?
- id: 417081
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0xMS0yMiAyMzoyNzowNSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0yMiAyMToyNzowNSArMDEwMA==
  content: ! "@Keba: Ich w&uuml;rde mich Simon anschlie&szlig;en. Die meisten Probleme,
    bei denen man &uuml;berhaupt auf den Gedanken kommt sie rekursiv anzupacken, sind
    rekursiv f&uuml;r den Programmierer (ohne weitere Betrachtung der Laufzeit) einfacher
    zu l&ouml;sen, d.h. schneller runter zu programmieren.\r\n\r\nAlso lautet die
    Antwort auf die Frage: Kommt drauf an ..."
---
Folgende Aufgabe gab es (sinngem&auml;&szlig;) f&uuml;r das Modul &bdquo;Programmieren&ldquo; im zweiten &Uuml;bungsblatt 2012:

Sei $(a_n)_{n \in \mathbb{N}}$ eine Folge und definiert durch:
$a_n := \begin{cases}
1 &\text{, falls } n \in \{0,1,2\}\\
a_{n-1} + a_{n-2} + a_{n-3} & \text{, falls } n \geq 3
\end{cases}$.

Ich werde im folgenden mal kurz m&ouml;gliche L&ouml;sungen in Python (und eine in Java) vorstellen. Python hat bei solchen Aufgaben den Vorteil, dass es viel kompakter ist und Ganzzahlen beliebig gro&szlig; werden k&ouml;nnen.

<h2>H&auml;ndische L&ouml;sung</h2>
Bevor man irgendwas programmiert, sollte man sicherstellen, dass man es testen kann. Was w&auml;ren also die ersten paar Folgenglieder?

$a_0 = a_1 = a_2 = 1, a_3 = 3, a_4 = 5, a_5 = 9, a_6 = 17, a_7 = 31, a_8 = 57$

<h2>Rekursive L&ouml;sung</h2>
Solche Aufgaben lassen sich h&auml;ufig sehr einfach rekursiv l&ouml;sen:

{% highlight python %}def tribonacci(n):
    if n < 3:
        return n
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3){% endhighlight %}

Allerdings hat diese rekursive L&ouml;sung den riesigen nachteil, dass viele Berechnungen redundant sind.
Angenommen, wir wollen <code>tribonacci(5)</code> berechnen. Dann l&auml;uft folgendes ab:

<ol>
  <li>Aufruf <code>tribonacci(5)</code>
    <ol>
      <li>Aufruf <code>tribonacci(4)</code>
        <ol>
          <li>Aufruf <code>tribonacci(3)</code>
            <ol>
              <li>Aufruf <code>tribonacci(2)</code>
              <li>Aufruf <code>tribonacci(1)</code>
              <li>Aufruf <code>tribonacci(0)</code>
            </ol>
          </li>
          <li>Aufruf <code>tribonacci(2)</code></li>
          <li>Aufruf <code>tribonacci(1)</code></li>
        </ol>
      </li>
      <li>Aufruf <code>tribonacci(3)</code>
        <ol>
          <li>Aufruf <code>tribonacci(2)</code>
          <li>Aufruf <code>tribonacci(1)</code>
          <li>Aufruf <code>tribonacci(0)</code>
        </ol>
      </li>
      <li>Aufruf <code>tribonacci(2)</code>
    </ol>
  </li>
</ol>

Man sieht deutlich, dass z.B. <code>tribonacci(3)</code> mehrfach berechnet werden muss.

Wie kann man so was verbessern?

<h2>Bottom-Up Ansatz</h2>
Wir ben&ouml;tigen f&uuml;r ein neues Folgenglied immer nur das vorhergehende. Das kann dann so aussehen:

{% highlight python %}def tribonacciBottomUp(n):
    last = 1
    secondLast = 1
    thirdLast = 1
    for i in range(2,n):
        new = last + secondLast + thirdLast
        thirdLast = secondLast
        secondLast = last
        last = new
    return last{% endhighlight %}

<h2>Fill it</h2>
Eine weitere M&ouml;glichkeit w&auml;re die schw&auml;che des rekursiven Ansatzes zu eliminieren, indem man alle bisher berechneten Werte in einem Array speichert.

<h2>Wertetabelle</h2>
<table>
<tr><th>i</th><th>a_i</th></tr>
<tr><td>0</td><td>1</td></tr>
<tr><td>1</td><td>1</td></tr>
<tr><td>2</td><td>1</td></tr>
<tr><td>3</td><td>3</td></tr>
<tr><td>4</td><td>5</td></tr>
<tr><td>5</td><td>9</td></tr>
<tr><td>6</td><td>17</td></tr>
<tr><td>7</td><td>31</td></tr>
<tr><td>8</td><td>57</td></tr>
<tr><td>9</td><td>105</td></tr>
<tr><td>10</td><td>193</td></tr>
<tr><td>11</td><td>355</td></tr>
<tr><td>12</td><td>653</td></tr>
<tr><td>13</td><td>1201</td></tr>
<tr><td>14</td><td>2209</td></tr>
<tr><td>15</td><td>4063</td></tr>
<tr><td>16</td><td>7473</td></tr>
<tr><td>17</td><td>13745</td></tr>
<tr><td>18</td><td>25281</td></tr>
<tr><td>19</td><td>46499</td></tr>
<tr><td>20</td><td>85525</td></tr>
<tr><td>21</td><td>157305</td></tr>
<tr><td>22</td><td>289329</td></tr>
<tr><td>23</td><td>532159</td></tr>
<tr><td>24</td><td>978793</td></tr>
<tr><td>25</td><td>1800281</td></tr>
<tr><td>26</td><td>3311233</td></tr>
<tr><td>27</td><td>6090307</td></tr>
<tr><td>28</td><td>11201821</td></tr>
<tr><td>29</td><td>20603361</td></tr>
<tr><td>30</td><td>37895489</td></tr>
<tr><td>31</td><td>69700671</td></tr>
<tr><td>32</td><td>128199521</td></tr>
<tr><td>33</td><td>235795681</td></tr>
<tr><td>34</td><td>433695873</td></tr>
<tr><td>35</td><td>797691075</td></tr>
<tr><td>36</td><td>1467182629</td></tr>
<tr><td>37</td><td>2698569577</td></tr>
<tr><td>38</td><td>4963443281</td></tr>
<tr><td>39</td><td>9129195487</td></tr>
<tr><td>40</td><td>16791208345</td></tr>
</table>

<h2>Java</h2>
Java-Nutzer m&uuml;ssen sich dar&uuml;ber im klaren sein, dass alle Elemente, die gr&ouml;&szlig;er als 36 sind, die <code>int</code>-Grenzen sprengen. Eine L&ouml;sung f&uuml;r das &Uuml;bungsblatt k&ouml;nnte ungef&auml;hr so aussehen:

{% highlight java %}/** This class calculates numbers of the Tribonacci sequence. */
public final class Tribonacci {
    /**
     * Utility classes should not have a public or default 
     * constructor.
     */
    private Tribonacci() {
    }

    /**
     * Calculate the n'th Element of the Tribonacci sequence (a_n). 
     * The sequence is defined as:
     *   a_0 = a_1 = a_2 = a
     *   a_n = a_(n-1) + a_(n-2) + a_(n-3)
     *
     * @param n the element of the Tribonacci sequence you want to
     *          calculate
     * @return the value of the n'th element in the Tribonacci
     *         sequence
     */
    public static long calculateTribonacci(final long n) {
        long last = 1;
        long secondLast = 1;
        long thirdLast = 1;

        for (int i = 2; i < n; i++) {
            long newTri = last + secondLast + thirdLast;
            thirdLast = secondLast;
            secondLast = last;
            last = newTri;
        }
        return last;
    }

    /**
     * Prints out the Tribonacci number a_36 
     * the (37th Tribonacci number)
     * @param args the command line arguments
     */
    public static void main(final String[] args) {
        System.out.println(calculateTribonacci(36));
    }

}
{% endhighlight %}
