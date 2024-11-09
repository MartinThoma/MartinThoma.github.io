---
layout: post
title: Hauswert Bestimmen
slug: hauswert-bestimmen
author: Martin Thoma
date: 2024-11-08 20:00
category: My bits and bytes
tags: house,finances
featured_image: logos/star.png
---
Es gibt ein paar Eckdaten, die den Wert eines Einfamilienhauses samt Grundstück
bestimmen. Hier im Artikel gehe ich auf die wichtigsten ein.

# Fundamentale Daten

* **Grundstücksfläche**: Die steht im Grundbuch.
* **Wohnfläche**: Da gibts leider verschiedene Standard
  ([WoFlV](https://de.wikipedia.org/wiki/Wohnfl%C3%A4chenverordnung) und [DIN
  277](https://de.wikipedia.org/wiki/DIN_277)).
* **Baujahr**: Das Alter des Gebäudes lässt einfache Rückschlüsse auf den Zustand zu.

# Lage

Der Bodenrichtwert (in EUR/m²) gibt an, wie viel ein Quadratmeter Bauland in
einer bestimmten Lage wert ist. Er wird von den Gutachterausschüssen für
Grundstückswerte ermittelt und ist ein wichtiger Indikator für den Wert einer
Immobilie.

Auf verschiedenen Portalen wie [immoportal.com](https://www.immoportal.com/immobilienpreise/hamburg)
kann man nachschauen, wie sich die Preise in der Umgebung entwickelt haben (in EUR/m² Wohnfläche).


# Energieeffizienz

Die Energieeffizienzklasse gibt dem Käufer eine Vorstellung davon, wie viel
Energie zum Heizen des Hauses benötigt wird. Die Skala reicht von A+ (sehr
effizient) bis H (sehr ineffizient).

Dabei gibt es drei relevante Faktoren:

* **Dichtheit** (Lüftungsverluste): Wenn der Wind durch das Haus pfeift, wird es teuer.
* **Dämmung** (Transmissionsverluste): Wenn man heißes Essen in eine Plastiktüte
  packt, wird es dennoch schnell kalt. Genauso ist es mit einem Haus. Eine hohe
  Dichtheit ist nicht alles, weil die Wärme auch durch abgestrahlt wird.
* **Heizsystem**: Lüftungs- und Transmissionswärmeverluste müssen ausgeglichen
  werden. Sie definieren die Heizlast. Die benötigten kWh an Wärme kann man
  durch unterschiedliche Heizsysteme bereitstellen. Die kosten pro kWh Wärme
  sind dabei massiv unterschiedlich. Aktuell in meiner Region bei angenommenen
  20.000 kWh pro Jahr:
    * Wärmepumpe mit <abbr title="bis zu 6 ist möglich">SCOP=3.5</abbr> (0.2407 €/kWh): 1375€/Jahr
    * Gas (0.08 €/kWh + 84€/Jahr): 1684€/Jahr
    * Super Heizöl (0.9804 €/L): 2000€/Jahr
    * Direkt-Strom, z.B. Infrarot oder Nachtspeicher (0.2407 €/kWh + <abbr title="Da man sowieso Strom benötigt, lasse ich den Grundpreis weg">200€/Jahr</abbr>): 4814€/Jahr


# Ausstattung

Hier ein Auszug aus dem [Bewertungsgesetz (BewG)](https://www.gesetze-im-internet.de/bewg/anlage_24.html):

<table width="100%"
  style="border-collapse: collapse;border-top: 0.5pt solid ; border-bottom: 0.5pt solid ; border-left: 0.5pt solid ; border-right: 0.5pt solid ; ">
  <colgroup>
    <col align="left" width="12%">
    <col align="left" width="16%">
    <col align="left" width="16%">
    <col align="left" width="16%">
    <col align="left" width="16%">
    <col align="left" width="16%">
    <col align="center" width="7%">
  </colgroup>
  <thead valign="bottom">
    <tr style="border-bottom: 0.5pt solid ; " valign="middle">
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" rowspan="4" align="left"
        valign="middle" charoff="50">&nbsp;</th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" colspan="5"
        align="center" valign="middle" charoff="50"><span style=";font-weight:bold">Standardstufe</span></th>
      <th style="border-bottom: 0.5pt solid ;  font-weight:normal;" rowspan="4" align="center" valign="middle"
        charoff="50"><span style=";font-weight:bold">Wägungsanteil</span></th>
    </tr>
    <tr valign="middle">
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">1</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">2</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">3</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">4</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">5</span></th>
    </tr>
    <tr valign="middle">
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" colspan="2"
        align="center" valign="middle" charoff="50"><span style=";font-weight:bold">nicht zeitgemäß</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" colspan="3"
        align="center" valign="middle" charoff="50"><span style=";font-weight:bold">zeitgemäß</span></th>
    </tr>
    <tr valign="middle">
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">einfachst</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">einfach</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">Basis</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">gehoben</span></th>
      <th style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ;  font-weight:normal;" align="center"
        valign="middle" charoff="50"><span style=";font-weight:bold">aufwendig</span></th>
    </tr>
  </thead>
  <tbody valign="top">
    <tr>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="middle" charoff="50">
        <span style=";font-weight:bold">Außenwände</span></td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Holzfachwerk, Ziegelmauerwerk;<br> Fugenglattstrich, Putz, Verkleidung mit Faserzementplatten, Bitumenschindeln
        oder einfachen Kunststoffplatten; kein oder deutlich nicht zeitgemäßer Wärmeschutz (vor ca. 1980)</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        ein-/zweischaliges Mauerwerk, z. B. Gitterziegel oder Hohlblocksteine; verputzt und gestrichen oder
        Holzverkleidung;<br> nicht zeitgemäßer Wärmeschutz (vor ca. 1995)</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        ein-/zweischaliges Mauerwerk, z. B. aus Leichtziegeln, Kalksandsteinen, Gasbetonsteinen;<br> Edelputz;<br>
        Wärmedämmverbundsystem oder Wärmedämmputz (nach ca. 1995)</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Verblendmauerwerk, zweischalig, hinterlüftet, Vorhangfassade (z. B. Naturschiefer);<br> Wärmedämmung (nach ca.
        2005)</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        aufwendig gestaltete Fassaden mit konstruktiver Gliederung (Säulenstellungen, Erker etc.),
        Sichtbeton-Fertigteile, Natursteinfassade, Elemente aus Kupfer-/<br> Eloxalblech, mehrgeschossige Glasfassaden;
        hochwertigste Dämmung (z. B. Passivhausstandard)</td>
      <td style="border-bottom: 0.5pt solid ; " align="center" valign="middle" charoff="50">23</td>
    </tr>
    <tr>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="middle" charoff="50">
        <span style=";font-weight:bold">Dach</span></td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Dachpappe, Faserzementplatten/Wellplatten;<br> keine bis geringe Dachdämmung</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        einfache Betondachsteine oder Tondachziegel, Bitumenschindeln;<br> nicht zeitgemäße Dachdämmung (vor ca. 1995)
      </td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Faserzement-Schindeln, beschichtete Betondachsteine und Tondachziegel, Folienabdichtung;<br> Dachdämmung (nach
        ca. 1995);<br> Rinnen und Fallrohre aus Zinkblech;</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        glasierte Tondachziegel, Flachdachausbildung tlw. als Dachterrassen; Konstruktion in Brettschichtholz, schweres
        Massivflachdach; besondere Dachformen, z. B. Mansarden-, Walmdach; Aufsparrendämmung, überdurchschnittliche
        Dämmung (nach ca. 2005)</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        hochwertige Eindeckung, z. B. aus Schiefer oder Kupfer, Dachbegrünung, befahrbares Flachdach; hochwertigste
        Dämmung (z. B. Passivhausstandard); Rinnen und Fallrohre aus Kupfer<br><span class="Formel">➀</span>aufwendig
        gegliederte Dachlandschaft, sichtbare Bogendach-konstruktionen</td>
      <td style="border-bottom: 0.5pt solid ; " align="center" valign="middle" charoff="50">15</td>
    </tr>
    <tr>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="middle" charoff="50">
        <span style=";font-weight:bold">Fenster und Außentüren</span></td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Einfachverglasung;<br> einfache Holztüren</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Zweifachverglasung (vor ca. 1995);<br> Haustür mit nicht zeitgemäßem Wärmeschutz (vor ca. 1995)</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Zweifachverglasung (nach ca. 1995), Rollläden (manuell); Haustür mit zeitgemäßem Wärmeschutz (nach ca. 1995)
      </td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Dreifachverglasung, Sonnenschutzglas, aufwendigere Rahmen, Rollläden (elektr.);<br> höherwertige Türanlage z. B.
        mit Seitenteil, besonderer Einbruchschutz</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        große, feststehende Fensterflächen, Spezialverglasung (Schall- und Sonnenschutz);<br> Außentüren in hochwertigen
        Materialien</td>
      <td style="border-bottom: 0.5pt solid ; " align="center" valign="middle" charoff="50">11</td>
    </tr>
    <tr>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="middle" charoff="50">
        <span style=";font-weight:bold">Innenwände und -türen</span></td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Fachwerkwände, einfache Putze/Lehmputze, einfache Kalkanstriche;<br> Füllungstüren, gestrichen, mit einfachen
        Beschlägen ohne Dichtungen</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        massive tragende Innenwände, nicht tragende Wände in Leichtbauweise (z. B. Holzständerwände mit Gipskarton),
        Gipsdielen;<br> leichte Türen, Stahlzargen</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">nicht
        tragende Innenwände in massiver Ausführung bzw. mit Dämmmaterial gefüllte Ständerkonstruktionen;<br> schwere
        Türen<br><span class="Formel">➀</span>Holzzargen</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Sichtmauerwerk; Massivholztüren, Schiebetürelemente, Glastüren, strukturierte Türblätter<br><span
          class="Formel">➀</span>Wandvertäfelungen (Holzpaneele)</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        gestaltete Wandabläufe (z. B. Pfeilervorlagen, abgesetzte oder geschwungene Wandpartien);
        Brandschutzverkleidung; raumhohe aufwendige Türelemente<br><span class="Formel">➀</span>Vertäfelungen (Edelholz,
        Metall), Akustikputz</td>
      <td style="border-bottom: 0.5pt solid ; " align="center" valign="middle" charoff="50">11</td>
    </tr>
    <tr>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="middle" charoff="50">
        <span style=";font-weight:bold">Deckenkonstruktion und Treppen</span></td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Holzbalkendecken ohne Füllung, Spalierputz;<br> Weichholztreppen in einfacher Art und Ausführung;<br> kein
        Trittschallschutz<br><span class="Formel">➀</span>Weichholztreppen in einfacher Art und Ausführung;<br> kein
        Trittschallschutz</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Holzbalkendecken mit Füllung, Kappendecken;<br> Stahl- oder Hartholztreppen in einfacher Art und
        Ausführung<br><span class="Formel">➀</span>Stahl- oder Hartholztreppen in einfacher Art und Ausführung</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50"><span
          class="Formel">➀</span>Beton- und Holzbalkendecken mit Tritt- und Luftschallschutz (z. B. schwimmender
        Estrich); geradläufige Treppen aus Stahlbeton oder Stahl, Harfentreppe, Trittschallschutz<br><span
          class="Formel">➁</span>Betondecken mit Tritt- und Luftschallschutz (z. B. schwimmender Estrich); einfacher
        Putz</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50"><span
          class="Formel">➀</span>Decken mit größerer Spannweite, Deckenverkleidung (Holzpaneele/Kassetten);<br>
        gewendelte Treppen aus Stahlbeton oder Stahl, Hartholztreppenanlage in besserer Art und Ausführung<br><span
          class="Formel">➁</span>zusätzlich Deckenverkleidung</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Deckenvertäfelungen (Edelholz, Metall)<br><span class="Formel">➀</span>Decken mit großen Spannweiten,
        gegliedert;<br> breite Stahlbeton-, Metall- oder Hartholztreppenanlage mit hochwertigem Geländer</td>
      <td style="border-bottom: 0.5pt solid ; " align="center" valign="middle" charoff="50">11</td>
    </tr>
    <tr>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="middle" charoff="50">
        <span style=";font-weight:bold">Fußböden</span></td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">ohne
        Belag</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Linoleum-, Teppich-, Laminat- und <a href="https://de.wikipedia.org/wiki/Polyvinylchlorid">PVC</a>-Böden
        einfacher Art und Ausführung</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Linoleum-, Teppich-, Laminat- und PVC-Böden besserer Art und Ausführung, Fliesen, Kunststeinplatten</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Natursteinplatten, Fertigparkett, hochwertige/großformatige Fliesen, Terrazzobelag, hochwertige Massivholzböden
        auf gedämmter Unterkonstruktion; aufwendige Verlegung</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        hochwertiges Parkett, hochwertige Natursteinplatten, hochwertige Edelholzböden auf gedämmter Unterkonstruktion
      </td>
      <td style="border-bottom: 0.5pt solid ; " align="center" valign="middle" charoff="50">5</td>
    </tr>
    <tr>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="middle" charoff="50">
        <span style=";font-weight:bold">Sanitäreinrichtungen</span></td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        einfaches Bad mit Stand-WC;<br> Installation auf Putz; Ölfarbenanstrich, einfache PVC-Bodenbeläge</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">1 Bad
        mit WC, Dusche oder Badewanne;<br> einfache Wand- und Bodenfliesen, teilweise gefliest</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">Wand-
        und Bodenfliesen, raumhoch gefliest; Dusche und Badewanne<br><span class="Formel">➀</span>1 Bad mit WC,
        Gäste-WC<br><span class="Formel">➁</span>1 Bad mit WC je Wohneinheit</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">1–2
        Bäder (<span class="Formel">➁</span>je Wohneinheit) mit tlw. zwei Waschbecken, tlw. Bidet/Urinal, Gäste-WC,
        bodengleiche Dusche; Wand- und Bodenfliesen;<br> jeweils in gehobener Qualität</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        hochwertige Wand- und Bodenplatten (oberflächenstrukturiert, Einzel- und Flächendekors)<br><span
          class="Formel">➀</span>mehrere großzügige, hochwertige Bäder, Gäste-WC; <span class="Formel">➁</span>2 und
        mehr Bäder je Wohneinheit</td>
      <td style="border-bottom: 0.5pt solid ; " align="center" valign="middle" charoff="50">9</td>
    </tr>
    <tr>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="middle" charoff="50">
        <span style=";font-weight:bold">Heizung</span></td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Einzelöfen, Schwerkraftheizung</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">Fern-
        oder Zentralheizung, einfache Warmluftheizung, einzelne Gasaußenwandthermen, Nachtstromspeicher-,
        Fußbodenheizung (vor ca. 1995)</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        elektronisch gesteuerte Fern- oder Zentralheizung, Niedertemperatur- oder Brennwertkessel</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Fußbodenheizung, Solarkollektoren für Warmwassererzeugung<br><span class="Formel">➀</span>zusätzlicher
        Kaminanschluss</td>
      <td style="border-right: 0.5pt solid ; border-bottom: 0.5pt solid ; " align="left" valign="top" charoff="50">
        Solarkollektoren für Warmwassererzeugung und Heizung, Blockheizkraftwerk, Wärmepumpe, Hybrid-Systeme<br><span
          class="Formel">➀</span>aufwendige zusätzliche Kaminanlage</td>
      <td style="border-bottom: 0.5pt solid ; " align="center" valign="middle" charoff="50">9</td>
    </tr>
    <tr>
      <td style="border-right: 0.5pt solid ; " align="left" valign="middle" charoff="50"><span
          style=";font-weight:bold">Sonstige technische Ausstattung</span></td>
      <td style="border-right: 0.5pt solid ; " align="left" valign="top" charoff="50">sehr wenige Steckdosen, Schalter
        und Sicherungen, kein Fehlerstromschutzschalter (FI-Schalter), Leitungen teilweise auf Putz</td>
      <td style="border-right: 0.5pt solid ; " align="left" valign="top" charoff="50">wenige Steckdosen, Schalter und
        Sicherungen</td>
      <td style="border-right: 0.5pt solid ; " align="left" valign="top" charoff="50">zeitgemäße Anzahl an Steckdosen
        und Lichtauslässen, Zählerschrank (ab ca. 1985) mit Unterverteilung und Kippsicherungen</td>
      <td style="border-right: 0.5pt solid ; " align="left" valign="top" charoff="50">zahlreiche Steckdosen und
        Lichtauslässe, hochwertige Abdeckungen, dezentrale Lüftung mit Wärmetauscher, mehrere LAN- und
        Fernsehanschlüsse<br><span class="Formel">➁</span>Personenaufzugsanlagen</td>
      <td style="border-right: 0.5pt solid ; " align="left" valign="top" charoff="50">Video- und zentrale Alarmanlage,
        zentrale Lüftung mit Wärmetauscher, Klimaanlage, Bussystem<br><span class="Formel">➁</span>aufwendige
        Personenaufzugsanlagen</td>
      <td align="center" valign="middle" charoff="50">6</td>
    </tr>
  </tbody>
</table>

Und noch ein paar weitere aus anderen Quellen:

<table border="1">
  <tr>
    <th>Bereich</th>
    <th>Standard / Durchschnittlich</th>
    <th>Mittelklasse</th>
    <th>Hochwertig</th>
    <th>Luxus / Exklusiv</th>
  </tr>
  <tr>
    <td>Wände</td>
    <td>Raufasertapete, gestrichen</td>
    <td>Glatte Wände, Vliestapete</td>
    <td>Hochwertige Tapeten, Glattputz</td>
    <td>Edler Wandputz, Naturmaterialien</td>
  </tr>
  <tr>
    <td>Küche</td>
    <td>Einfache Einbauküche</td>
    <td>Marken-Einbauküche</td>
    <td>Hochwertige Einbauküche mit Markengeräten</td>
    <td>Designer-Küche, Profi-Ausstattung</td>
  </tr>
  <tr>
    <td>Innentüren</td>
    <td>Füllungstüren, Türblätter und Zargen gestrichen, Stahlzargen</td>
    <td>Kunststoff-/Holztürblätter, Holzzargen, Glastürausschnitte</td>
    <td>Türblätter mit Edelholzfurnier, Glastüren, Holzzargen</td>
    <td>massivere Ausführung, Einbruchschutz</td>
  </tr>
  <tr>
    <td>Elektroinstallation</td>
    <td>je Raum 1 Lichtauslass und 1–2 Steckdosen, Installation tlw. auf Putz</td>
    <td>je Raum 1–2 Lichtauslässe und 2–3 Steckdosen, Installation unter Putz</td>
    <td>je Raum mehrere Lichtauslässe und Steckdosen, informationstechnische Anlagen</td>
    <td>aufwendige Installation, Sicherheitseinrichtungen</td>
  </tr>
  <tr>
    <td>Beleuchtung</td>
    <td>Standard-Lampen</td>
    <td>Einbaustrahler, LED</td>
    <td>LED-Spots, Design-Leuchten</td>
    <td>Designer-Beleuchtung, Lichtkonzepte</td>
  </tr>
  <tr>
    <td>Außenbereich</td>
    <td>Einfacher Garten</td>
    <td>Gartengestaltung, Terrasse</td>
    <td>Hochwertiger Garten mit Pflasterung</td>
    <td>Landschaftsgarten, Pool, Beleuchtung</td>
  </tr>
</table>

Das will die Bank auch wissen wenn sie die Finanzierung prüft.

## Einzelnachweise

* "Ausstattungsstandard" auf [immobilienbewertung-info.de](https://www.immobilienbewertung-info.de/themen/fachbegriffe/ausstattungsstandard/), abgerufen am 2024-11-09
* "Wohnung und Haus – was zählt alles zu einer gehobenen Ausstattung?" auf [edle-bauelemente.de](https://www.edle-bauelemente.de/wohnung-und-haus-was-zaehlt-alles-zu-einer-gehobenen-ausstattung/), abgerufen am 2024-11-09
* "Was ist eigentlich eine gehobene Gebäudeausstattung aus Sicht der Gebäudeversicherung?" auf [versicherungsmakler-guetersloh.de](https://versicherungsmakler-guetersloh.de/was-ist-eigentlich-eine-gehobene-gebaeudeausstattung-aus-sicht-der-gebaeudeversicherung/), abgerufen am 2024-11-09
* "Ausstattungsmerkmale und Lage beim Hausverkauf" auf [praxiswissen-immobilien.de](https://www.praxiswissen-immobilien.de/ausstattung-lage-immobilie/), abgerufen am 2024-11-09
