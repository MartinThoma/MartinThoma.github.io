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
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Formale Systeme&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei Herrn Prof. Dr. Beckert im Wintersemester 2014/2015 gehört.</div>

Der Artikel wird bis zur Klausur noch mehrfach bearbeitet werden.

## Behandelter Stoff ##

* [Aussagenlogik](https://de.wikipedia.org/wiki/Aussagenlogik)
  * Erfüllbarkeit, Unerfüllbarkeit, Allgemeingültigkeit
  * Normalformen: <abbr title="Konjunktive Normalform">KNF</abbr>, <abbr title="Disjuktive Normalform">DNF</abbr>, <abbr title="Kurze konjunktive Normalform">KKNF</abbr>
  * BDDs, Shannon Graphen
  * [Davis-Putnam-Verfahren](https://de.wikipedia.org/wiki/Davis-Putnam-Verfahren)


### Kurz und Gut

Die folgenden Stichpunkte sollte man (größtenteils nur sinngemäß) auswendig
können und verstehen:

* Eine Signatur $\Sigma$ ist eine abzählbare Menge von Symbolen. Die Elemente
  der Signatur heißen "Aussagevariablen".
* Eine Interpretation ist eine Abbildung $I: \Sigma \rightarrow \{W, F\}$
* Ein Modell einer Formel $A \in For0_\Sigma$ ist eine Interpretation $I$ mit
  $val_I(A) = W$.<br/>
  Ein Modell einer Formel ist also einfach eine Variablenbelegung, welche die
  Formel erfüllt.
* Für $M \subseteq For0_\Sigma, A \in For0_\Sigma$ gilt: $M \models A$ (lies:
  aus M folgt A), falls jede Variablenbelegung, welche $M$ erfüllt, auch $A$
  erfüllt.
* $A \rightarrow B \equiv \neg A \lor B$
* $A \models B$ gdw. $\models A \rightarrow B$
* Der shannon-Operator $sh(a,b,c)$ ist if(a) {c} else {b}.
* Die Craig-Interpolation von $A \rightarrow B$ ersetzt alle
  Aussagevariablen $\{\text{Aussagevariable} a \in A | a \notin B\}$ mit
  $c_i$ ($i=1,\dots,n$). Die Interpolante ist dann
  $C := \bigvee_{(c_1, \dots, c_n) \in \{0,1\}^n} A[c_1, \dots, c_n]$.
* Eine DNF heißt "vollständig" bzgl. einer Signatur $\Sigma$, wenn
  falls für jedes $P \in \Sigma$ in jeder Klausel entweder $P$ oder $\neg P$
  vorkommt.
* Eine DNF heißt "minimal", wenn jede kürzere Formel nicht äquivalent ist.
* KKNF-Konstruktion: (1) Shortcuts $Q_1, \dots, Q_n$ für binäre Operatoren
  erstellen. Diese Shortcuts dürfen auch andere Shortcuts verwenden
  (2) Äquivalenzen auflösen (3) In KNF umformen.
* $sh(P_i, A, B)$ heißt normiert, wenn $A$ und $B$ normiert sind und jede in
  $A \cup B$ vorkommende Variable $P_j$ gilt $i < j$.
* Ein Shannon-Graph heißt reduziert, wenn es keine zwei Knoten $v,w$ gibt,
  sodass die beiden in $v$ und $w$ verwurzelten Teilbäume isomorph sind und es
  auch keinen Knoten gibt, bei dem beide ausgehenden Kanten in den selben
  Nachfolger führen.
* Reduzierter Shannon-Graph = OBDD = BDD = ordered binary decisio diagram
* Bei gegebener Indizierung sind reduzierte Shannon-Graphen bis auf Isomorphie
  eindeutig. Ist die Indizierung nicht gegeben, macht die Variablenanordnung
  einen großen Unterschied in der Größe (Knotenmenge) des reduzierten
  Shannon-Graphen.
* Multiplikation $k$-stelliger Binärzahlen: Für jede Ordnung $<$ der Variablen
  in $X=\{x_0, \dots, x_{k-1}, y_0, \dots, y_{k-1}\}$ gibt es einen Index
  $0 \leq i < 2k$, sodass der BDD $B_{Mult_i,<} mindestens $2^{k/8}$ Knoten
  besitzt.
* Horn-Formel: Formel in KNF, wobei jede Klausel höchstens ein positives
  Literal enthält.
* Negationsnormalform: Negationen nur vor Atomen.
* Bereinigte Formel: (1) $Frei(A) \cap Bd(A) = \emptyset$ (2) Die hinter
  Quantoren stehenden Variablen sind paarweise verschieden.
* Pränexe Normalform: $A = Q_1 x_1 Q_2 x_2 Q_3 x_3 \dots Q_n x_n B$, wobei $B$
  quantorenfrei sein muss. Dann heißt $B$ die Matrix von $A$.
* Die Pränexe Normalform ist nicht eindeutig.
* Skolem-Normalform: (1) geschlossene Formel (2) $\forall x_1 \dots \forall x_n B$ (3) Matrix $B$ ist in KNF
* [Gödelscher Vollständigkeitssatz](https://de.wikipedia.org/wiki/G%C3%B6delscher_Vollst%C3%A4ndigkeitssatz):
  Es gibt einen Kalkül der PL1 derart, dass für jede Formelmenge $\Gamma$ und
  für jede Formel $\varphi$ gilt: $\varphi$ folgt genau dann aus $\Gamma$, wenn
  $\varphi$ im Kalkül aus $\Gamma$ hergeleitet werden kann. In Zeichen:
  $\Gamma \models \varphi \Leftrightarrow \Gamma \vdash \varphi$.
* Kompaktheitssatz: Wenn A aus einer unendlichen Teilmenge der Formelmenge
  folgt, dann auch aus einer endlichen.
* Endlichkeitssatz: Eine Menge $M \subseteq For_\Sigma$ hat genau dann ein
  Modell, wenn jede endliche Teilmenge von $M$ ein Modell hat.
* Der Resolutionskalkül arbeitet nur mit Formeln in Skolemnormalform.


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
    <td>Aussagenlogik: <a href="https://de.wikipedia.org/wiki/Craig-Interpolation">Craig-Interpolation</a></td>
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
    <td><a href="https://de.wikipedia.org/wiki/Erf%C3%BCllbarkeitsproblem_der_Aussagenlogik">SAT</a>; <a href="https://de.wikipedia.org/wiki/Satz_von_Cook">Satz von Cook</a>; <a href="https://de.wikipedia.org/wiki/Horn-Formel">Horn-Formeln</a>; DPLL</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/07PK1Intro-print.pdf" rel="nofollow">07</a></td>
    <td>Prädikatenlogik: Syntax (PL1); JML; (Kollisionsfreie) Substitutionen; <a href="https://de.wikipedia.org/wiki/Unifikation_(Logik)">Unifikation</a> und der Algorithmus von Robinson; Unifikationstheorem</td>
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
    <th>Lsg</th>
    <th>Inhalt</th>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt1.pdf" rel="nofollow">ÜB 1</a>: Aussagenlogik</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt1-lsg.pdf">Lsg</a></td>
    <td>Erfüllbarkeit, Unerfüllbarkeit, Allgemeingültigkeit, Tautologie, <abbr title="Konjunktive Normalform">KNF</abbr>, <abbr title="Disjuktive Normalform">DNF</abbr>, Interpolanten</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt2.pdf" rel="nofollow">ÜB 2</a>: Aussagenlogik</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt2-lsg.pdf">Lsg</a></td>
    <td><abbr title="Kurze konjunktive Normalform">KKNF</abbr>, <abbr title="Binary decision diagram">BDD</abbr>, Shannon Graphen</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt3.pdf" rel="nofollow">ÜB 3</a>: Aussagenlogik, PL1</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt3-lsg.pdf">Lsg</a></td>
    <td>DNF, KNF, DPLL</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt4.pdf" rel="nofollow">ÜB 4</a>: PL1</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt4-lsg.pdf">Lsg</a></td>
    <td>PL1 (Variante des Zebrarätsels); Unifikation</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt5.pdf" rel="nofollow">ÜB 5</a>: PL1</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt5-lsg.pdf">Lsg</a></td>
    <td>Verwandschaftsbeziehungen; (Java) Integer; Interpretation/Modell/Formel; Erfüllbar / allgemeingültig / unerfüllbar</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt6.pdf" rel="nofollow">ÜB 6</a>: PL1</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt6-lsg.pdf">Lsg</a></td>
    <td>Pränexnormalform; Skolemnormalform (<a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/09PK1Normalform-print.pdf" rel="nofollow">09</a>)</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt7.pdf" rel="nofollow">ÜB 7</a>: PL1</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt7-lsg.pdf">Lsg</a></td>
    <td>Hilbertkalkül (<a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/11Hilbert.pdf">11</a>); Resolutionskalkül (<a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/12ALResolution-print.pdf">12</a>, <a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/13PK1Resolution-print.pdf">13</a>)</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt8.pdf" rel="nofollow">ÜB 8</a>: &nbsp;</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt8-lsg.pdf">Lsg</a></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt9.pdf" rel="nofollow">ÜB 9</a>: &nbsp;</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt9-lsg.pdf">Lsg</a></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt10.pdf" rel="nofollow">ÜB 10</a>: &nbsp;</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt10-lsg.pdf">Lsg</a></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt11.pdf" rel="nofollow">ÜB 11</a>: &nbsp;</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt11-lsg.pdf">Lsg</a></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt12.pdf" rel="nofollow">ÜB 12</a>: &nbsp;</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt12-lsg.pdf">Lsg</a></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt13.pdf" rel="nofollow">ÜB 13</a>: &nbsp;</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt13-lsg.pdf">Lsg</a></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt14.pdf" rel="nofollow">ÜB 14</a>: &nbsp;</td>
    <td><a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt14-lsg.pdf">Lsg</a></td>
    <td>&nbsp;</td>
  </tr>
</table>

### Erklärungen

* 08Pk1Semantik-print.pdf, Folie 34/37: QxB steht für "Quantor x B", wobei der
  Quantor entweder $\exists$ oder $\forall$ ist, $x$ eine Variable ist und $B$
  eine Formel ist.


## Wissens-Check
Folgende Fragen sollte man für die Klausur schnell beantworten können:

* Nenne 3 Basen für die Aussagenlogik. Eine davon soll höchstens einen Operator
  haben.
* In welcher Komplexitätsklasse ist das Erfüllbarkeitsproblem für 3-KNF?
  In welcher 2-KNF? Wie sieht es mit dem Allgemeingültigkeitsproblemen aus?


## Meine Fragen
* <a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/02ALIntro-print.pdf">02, Folie 19/29</a>:
  Warum wird einmal $\models$ und dann $\models_\Sigma$ geschrieben?
* <a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/09PK1Normalform-print.pdf">Folie 8/30</a>:
  Wieso stimmt diese Umformung?
* <a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/09PK1Normalform-print.pdf#page=23">Folie 23/30</a>: Was ist eine Grundinstanz? Wo ist der Unterschied zwischen "Grundinstanz" und "Instanz"? Was sind "Grundterme"?
* <a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/09PK1Normalform-print.pdf#page=24">Folie 24/30</a>: Was ist ein Beispiel für $D = Term_\Sigma^0 \neq$ Menge der Grundterme? Wo gilt 2. nicht?
* <a href="http://formal.iti.kit.edu/teaching/FormSysWS1415/blatt6-lsg.pdf">Blatt 6, Lösung zu Aufgabe 4</a>: Den Teil mit der Umwandlung einer Aussagenlogischen Formel verstehe ich nicht. Kann das jemand bitte für $a \land \neg b \lor c \lor d$ erklären?


## Material ##
* [Skript](http://formal.iti.kit.edu/teaching/FormSysWS1415/skriptum.pdf)
* [Vorlesungswebsite](http://formal.iti.kit.edu/teaching/FormSysWS1415/)

StackExchange:

* [What is the operator precedence for quantifiers?](http://math.stackexchange.com/q/1150746/6876)
* [How do you bring quantors to the front of a formula?](http://math.stackexchange.com/q/1150826/6876)
* [How to convert to conjunctive normal form?](http://math.stackexchange.com/a/214352/6876)


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

**Datum**: Donnerstag, den 6. März 2015 von 11:00 bis 12:00 Uhr ([Quelle](http://formal.iti.kit.edu/teaching/FormSysWS1415)).<br/>
**Ort**: ?<br/>
**Punkte**: 60<br/>
**Punkteverteilung**: ?<br/>
**Bestehensgrenze**: ?<br/>
**Übungsschein**: Gibt es nicht.<br/>
**Bonuspunkte**: Bis zu 8. Die Punkte aus den 4 Zwischenprüfungen und 2 Praxisaufgaben werden addiert, dann durch 10 geteilt und schließlich kaufmännisch gerundet.<br/>
**Ergebnisse**: Klausur wurde noch nicht geschrieben<br/>
**Einsicht**: steht noch nicht fest (Stand: 17.02.2015)<br/>
**Erlaubte Hilfsmittel**: Keine.


## Ergebnisse
Klausur wurde noch nicht geschrieben.