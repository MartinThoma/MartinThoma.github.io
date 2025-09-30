---
layout: post
lang: de
title: Tribonacci-Folge
author: Martin Thoma
date: 2012-11-19 20:52:00.000000000 +01:00
category: Code
tags: Programming, Java
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

```python
def tribonacci(n):
    if n < 3:
        return n
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
```

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

```python
def tribonacciBottomUp(n):
    last = 1
    secondLast = 1
    thirdLast = 1
    for i in range(2, n):
        new = last + secondLast + thirdLast
        thirdLast = secondLast
        secondLast = last
        last = new
    return last
```

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

```java
/** This class calculates numbers of the Tribonacci sequence. */
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

```
