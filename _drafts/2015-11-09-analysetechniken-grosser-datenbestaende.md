---
layout: post
title: Analysetechniken für große Datenbestände - Klausur
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- German posts
tags:
- Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Analysetechniken für große Datenbestände&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="https://dbis.ipd.kit.edu/english/336.php">Herrn Prof. Dr.-Ing. Klemens Böhm</a> im Wintersemester 2015/2016 gehört. Der Artikel ist noch am Entstehen.</div>

## Behandelter Stoff

### Übersicht

<table>
<tr>
    <th>Datum</th>
    <th>Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
    <td>20.10.2015, 08:00</td>
    <td>Einleitung (Folie 1-26)</td>
    <td>Overfitting, Entscheidungsbäume, 1-Rules (→ Decision Strump), Outliers<br/>
        Mengenwertige Attribute, Kategorische Attribute, Zeitreihen<br/>
        Clustering<br/>
        Market Basket Analysis: Zusammenhang zwischen Waren<br/>
        Association rules (A priory Algorithmus)
    </td>
</tr>
<tr>
    <td>20.10.2015, 11:30</td>
    <td>Einleitung (Folie 27-)</td>
    <td>Predictive Maintenance
    </td>
</tr>
<tr>
    <td>27.10.2015, 08:00</td>
    <td>&nbsp;</td>
    <td>$\chi^2$-Test, $\chi^2 = \sum_{i=1}^{m_1} \sum_{j=1}^{m_2} \frac{(h_{ij}- e_{ij})^2}{e_{ij}}$ mit erwartetem Wert $e$ (Sind zwei Zufallsvariablen unabhängig)<br/>
    Kolmogorov-Smirnov-Test (Sind 2 Verteilungen unabhängig; bei kontinuierlichen Zufallsvariablen)<br/>
    Wilcoxon-Wann-Whitney Test<br/>
    Bernoulli-Experiment (Folie 53?)<br/>
    Datenreduktion (Attribute entfernen, z.B. PCA; Datensätze entfernen, z.B. Clustering; Attributsgenauigkeit reduzieren)<br/>
    Diskretisierung: Zielfunktion ist Information Gain. Dieser soll minimiert werden.
    </td>
</tr>
<tr>
    <td>08.12.2015, 08:00</td>
    <td>R-Übung</td>
    <td>-</td>
</tr>
<tr>
    <td>26.01.2016, 08:00</td>
    <td>Übung</td>
    <td>-</td>
</tr>
</table>


### Einleitung

Slides: `1-Einleitung.pdf`

* 3 Aufgabentypen: Klassifikation, Clustering und finden von [Association Rules](https://de.wikipedia.org/wiki/Assoziationsanalyse)


<dl>
  <dt><a href="https://en.wikipedia.org/wiki/Decision_stump"><dfn>1-Rule</dfn></a> (<dfn>Decision stump</dfn>)</dt>
  <dd>1-Rules ist ein Klassifikationsverfahren. Jedes Attribut wird für sich
      betrachtet. Es wird anhand von dem Attribut gesplittet, bei dem die
      Fehlerquote am geringsten ist.</dd>
  <dt><dfn>Clustering</dfn></dt>
  <dd>Suchen von Punkten, die nahe bei einander liegen.

      Unterschiede:

      <ul>
          <li>Attribute: Abstandsmaße</li>
          <li>Form</li>
          <li>Dichte</li>
          <li>Größe</li>
          <li>Zeitlicher Aspekt: Alte Daten weniger wichtig</li>
          <li>Alternate Clustering</li>
      </ul>
  </dd>
  <dt><dfn>Association Rules</dfn></dt>
  <dd>z.B. in Market Basket Analysis. Frequent item sets

      A priori Algorithmus zum finden von Association Rules. TODO
  </dd>
  <dt><dfn>Predictive Maintenance</dfn></dt>
  <dd>Ziel: Für Motoren will man vorhersagen, wann diese einen Fehler aufweisen
      und damit gewartet werden müssen.

      Dabei gibt es zwei Fehlerarten, die unterschiedliche hohe Kosten
      aufweisen:
      <ul>
          <li>Ausfall wird vorhergesagt, tritt aber nicht ein: Unnötige Wartung</li>
          <li>Ausfall wird nicht vorhergesagt, tritt aber ein: Teurer Ausfall</li>
      </ul>
  </dd>

  <dt><dfn>Subspace Search</dfn></dt>
  <dd>TODO</dd>

  <dt><dfn>Change detection</dfn></dt>
  <dd>TODO</dd>
</dl>


### Prüfungsfragen

Kommt noch.

### Übungen

Kommt noch.

## Material und Links

Die Vorlesung wurde gestreamt und ist unter
[mml-streamdb01.ira.uka.de](http://mml-streamdb01.ira.uka.de/) verfügbar.

* [Vorlesungswebsite](https://dbis.ipd.kit.edu/2261.php)
* [Ilias](https://ilias.studium.kit.edu/goto_produktiv_crs_477914.html)


## Übungsbetrieb

?


## Termine und Klausurablauf

Es ist noch nicht klar, ob es eine mündliche oder eine schriftliche Prüfung
wird.

Falls es mündlich ist, soll es mindestens einen Termin pro Monat geben.

**Datum**: Noch nicht bekannt (Stand: 09.11.2015)<br/>
**Ort**: Noch nicht bekannt (Stand: 09.11.2015)<br/>
**Punkte**: ?<br/>
**Zeit**: ?<br/>
**Punkteverteilung**: ?<br/>
**Bestehensgrenze**: ?<br/>
**Übungsschein**: ?<br/>
**Bonuspunkte**: ?<br/>
**Ergebnisse**: ?<br/>
**Einsicht**: Noch nicht bekannt (Stand: 09.11.2015)<br/>
**Erlaubte Hilfsmittel**: keine
