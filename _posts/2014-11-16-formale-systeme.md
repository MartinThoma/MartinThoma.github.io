---
layout: post
title: Formale Systeme Klausur
author: Martin Thoma
date: 2014-11-16 17:05
categories:
- German posts
tags:
- Klausur
- Formale Systeme
featured_image: 2012/02/klausur-test-thumbnail.jpg
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Formale Systeme&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei Herrn Prof. Dr. Beckert im Wintersemester 2014/2015 gehört.</div>

Der Artikel wird bis zur Klausur noch mehrfach bearbeitet werden.

## Behandelter Stoff ##

* [Aussagenlogik](https://de.wikipedia.org/wiki/Aussagenlogik)
  * Erfüllbarkeit, Unerfüllbarkeit, Allgemeingültigkeit
  * Normalformen: <abbr title="Konjunktive Normalform">KNF</abbr>, <abbr title="Disjuktive Normalform">DNF</abbr>, <abbr title="Kurze konjunktive Normalform">KKNF</abbr>
  * BDDs, Shannon Graphen
  * [Davis-Putnam-Verfahren](https://de.wikipedia.org/wiki/Davis-Putnam-Verfahren)

### Folien ###
<table>
  <tr>
    <th>Folien-<br/>satz</th>
    <th>Inhalt</th>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/01Organisatorisches-print.pdf" rel="nofollow">01</a></td>
    <td>Organisatorisches</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/02ALIntro-print.pdf" rel="nofollow">02</a></td>
    <td>Aussagenlogik: Modellierung von Sudoku; 8-Damen-Problem; Allgemeine Syntax und Semantik sowie Grundbegriffe, Tautologien und Sätze; Basis</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/03CraigInterpol-print.pdf" rel="nofollow">03</a></td>
    <td>Aussagenlogik: [Craig-Interpolation](https://de.wikipedia.org/wiki/Craig-Interpolation)</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/04ALNormalform-print.pdf" rel="nofollow">04</a></td>
    <td>Aussagenlogik: Normalformen (<abbr title="Konjunktive Normalform">KNF</abbr>, <abbr title="Disjuktive Normalform">DNF</abbr>, <abbr title="Kurze konjunktive Normalform">KKNF</abbr>)</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/05BDD-print.pdf" rel="nofollow">05</a></td>
    <td>Binary Decision Diagrams: (normierte) Shannon-Formeln, sh-Operator, Shannon-Graph, Reduzierte Shannon-Graphen</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/06SATsolver-print.pdf" rel="nofollow">06</a></td>
    <td>[SAT](https://de.wikipedia.org/wiki/Erf%C3%BCllbarkeitsproblem_der_Aussagenlogik); [Satz von Cook](https://de.wikipedia.org/wiki/Satz_von_Cook); [Horn-Formeln](https://de.wikipedia.org/wiki/Horn-Formel)</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/07PK1Intro-print.pdf" rel="nofollow">07</a></td>
    <td>Prädikatenlogik: Syntax (PL1); JML; (Kollisionsfreie) Substitutionen; [Unifikation](https://de.wikipedia.org/wiki/Unifikation_(Logik)) und der Algorithmus von Robinson; Unifikationstheorem</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/08Pk1Semantik-print.pdf" rel="nofollow">08</a></td>
    <td>Pradikatenlogik: Semantik; Interpretation; Koinzidenzlemma; Substitutionslemma für Terme (und das für Formeln); Hoare-Kalkül; Modell; (Logische) Folgerung; Allgemeingültigkeit; Folgerbarkeit</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/09PK1Normalform-print.pdf" rel="nofollow">09</a></td>
    <td>Pradikatenlogik: Normalformen; Negationsnormalform; Pränexe Normalform; Skolem-Normalform; Herbrand-Strukturen; Satz von Herbrand; Endlichkeitssatz der Aussagenlogik</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/10IntroBeweistheorie-print.pdf" rel="nofollow">10</a></td>
    <td>Beweistheorie (Einführung)</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/11Hilbert.pdf" rel="nofollow">11</a></td>
    <td>Hilbertkalkül; Deduktionstheorem; Vollständigkeit der PL1; Kompaktheitssatz; Endlichkeitssatz</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/12ALResolution-print.pdf" rel="nofollow">12</a></td>
    <td>Aussagenlogik: Resolutionskalkül; 1-Resolution</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/13PK1Resolution-print.pdf" rel="nofollow">13</a></td>
    <td>Prädikatenlogik: Resolutionskalkül; </td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/14Tableau-print.pdf" rel="nofollow">14</a></td>
    <td>Tableaukalkül</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/19PL1Sequenz-print.pdf" rel="nofollow">19</a></td>
    <td>Prädikatenlogik: Sequenzenkalül; </td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/21Peano-print.pdf" rel="nofollow">21</a></td>
    <td>Peano-Arithmetik; Unentscheidbarkeit</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/28JML.pdf" rel="nofollow">28</a></td>
    <td>JML</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/22Reduktion-print.pdf" rel="nofollow">22</a></td>
    <td>Reduktionssysteme: Gleichungslogik; Satz von Birkhoff; Termersetzungssysteme; Reduktionssysteme; Kanonische Reduktionssysteme; Noethersche Induktion; (lokale) Konfluenz</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/23Termersetzung-print.pdf" rel="nofollow">23</a></td>
    <td>Termersetzungssysteme; Kritische Paare; </td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/27Modal-print.pdf" rel="nofollow">27</a></td>
    <td>Modallogik; Kripke-Strukturen; Charakterisierungstheorie; Entscheidbarkeit modaler Logiken</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/41Automaten-print.pdf" rel="nofollow">41</a></td>
    <td>(Vollständige) endliche Automaten; <abbr title="Nichtdeterministische Endliche Automaten">NEAs</abbr>; Spontane Übergänge; Satz von Myhill und Büchi; Reguläre Ausdrücke; </td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/42buechiAut-print.pdf" rel="nofollow">42</a></td>
    <td>Büchi-Automaten</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/43LTL-print.pdf" rel="nofollow">43</a></td>
    <td>Lineare Temporale Logik; omega-Struktur; LTL-Formeln; LTL-Semantik; </td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/45LTL2Buechi-print.pdf" rel="nofollow">45</a></td>
    <td>LTL und Büchi-Automaten; </td>
  </tr>
</table>


### Übungsblätter ###
<table>
  <tr>
    <th>Übungsblatt</th>
    <th>Inhalt</th>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt1.pdf" rel="nofollow">ÜB 1</a>: Aussagenlogik</td>
    <td>Erfüllbarkeit, Unerfüllbarkeit, Allgemeingültigkeit, Tautologie, <abbr title="Konjunktive Normalform">KNF</abbr>, <abbr title="Disjuktive Normalform">DNF</abbr>, Interpolanten</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt2.pdf" rel="nofollow">ÜB 2</a>: Aussagenlogik</td>
    <td><abbr title="Kurze konjunktive Normalform">KKNF</abbr>, <abbr title="Binary decision diagram">BDD</abbr>, Shannon Graphen</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt3.pdf" rel="nofollow">ÜB 3</a>: Aussagenlogik, Prädikatenlogik</td>
    <td>DNF, KNF, DPLL</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt4.pdf" rel="nofollow">ÜB 4</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt5.pdf" rel="nofollow">ÜB 5</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt6.pdf" rel="nofollow">ÜB 6</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt7.pdf" rel="nofollow">ÜB 7</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt8.pdf" rel="nofollow">ÜB 8</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt9.pdf" rel="nofollow">ÜB 9</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt10.pdf" rel="nofollow">ÜB 10</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt11.pdf" rel="nofollow">ÜB 11</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt12.pdf" rel="nofollow">ÜB 12</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt13.pdf" rel="nofollow">ÜB 13</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt14.pdf" rel="nofollow">ÜB 14</a>: &nbsp;</td>
    <td>&nbsp;</td>
  </tr>
</table>


## Wissens-Check
Folgende Fragen sollte man für die Klausur schnell beantworten können:

* Nenne 3 Basen für die Aussagenlogik. Eine davon soll höchstens einen Operator
  haben.
* In welcher Komplexitätsklasse ist das Erfüllbarkeitsproblem für 3-KNF?
  In welcher 2-KNF? Wie sieht es mit dem Allgemeingültigkeitsproblemen aus?


## Material ##
* [Skript](http://formal.iti.kit.edu/teaching/FormSysWS1415/skriptum.pdf)
* [Vorlesungswebsite](http://formal.iti.kit.edu/teaching/FormSysWS1415/)
* Mein [Anki-Deck](https://ankiweb.net/shared/info/1222257840) (wird noch erweitert)


## Übungsbetrieb

* Wo sind die Übungsblätter: [Link](http://formal.iti.kit.edu/teaching/FormSysWS1415/)
* Abgabeform: Keine Abgabe
* Turnus: wöchentlich
* Lösungen: Die Lösungen von jeweils zwei Blättern werden dann in den 14-tägig stattfinden Übungen am Freitag besprochen.
* Übungsschein verpflichtend: Es gibt keinen Übungsschein.
* Bonus durch Übungsschein: Es gibt keinen Klausurbonus durch Übungsblätter.
* Anderer Klausurbonus: Man kann durch insgesammt 4 Zwischentests und 2 Praxisaufgaben für die wirkliche
  Klausur Punkte sammeln. Die Teilnahme an den Zwischentests und den Praxisaufgaben ist freiwillig. Die erzielten Übungspunkte werden im Verhältnis 1:10 als Bonuspunkte auf die bestandene Abschlussklausur angerechnet.

## Termine und Klausurablauf

Siehe [Klausurtermine-Seite](http://www.informatik.kit.edu/klausuren.php) für
zukünftige Termine.

**Datum**: Donnerstag, den 6. März 2015 von 11:00 bis 13:00 Uhr ([Quelle](http://formal.iti.kit.edu/teaching/FormSysWS1415))<br/>
**Ort**: ?<br/>
**Punkte**: ?<br/>
**Punkteverteilung**: ?<br/>
**Bestehensgrenze**: ?<br/>
**Übungsschein**: Gibt es nicht.<br/>
**Bonuspunkte**: Bis zu 8 (?)<br/>
**Ergebnisse**: Klausur wurde noch nicht geschrieben<br/>
**Einsicht**: steht noch nicht fest (Stand: 16.11.2014)<br/>
**Erlaubte Hilfsmittel**: Keine.

## Ergebnisse
Klausur wurde noch nicht geschrieben.