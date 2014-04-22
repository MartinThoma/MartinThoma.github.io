---
layout: post
title: Prüfungsverwaltung am KIT
author: Martin Thoma
date: 2014-04-08 16:09
categories:
- German posts
tags:
- KIT
featured_image: logos/kit.png
---

<!-- <div class="info">This article is about an idea how to give students the
possibility to proof that they were registered for an exam.</div> -->

Gerade ist mir aufgefallen, dass ich nicht zur Prüfung "Programmierparadigmen"
angemeldet bin. Dabei war ich mir relativ sicher, mich sogar am ersten Tag
angemeldet zu haben, als die Anmeldung freigeschaltet wurde.

Meiner Meinung nach sind wir Studenten hier in einer ungerechtfertigt
schlechten Position: Sollte tatsächlich ein Fehler passiert sein und meine
Anmeldung nicht funktioniert haben bzw. die Anmeldung (wie oder warum auch immer)
rückgängig gemacht worden sein, habe ich keinerlei Möglichkeit zu beweisen, 
dass ich angemeldet war und nicht etwa es einfach vergessen habe. Was ich in
meinem konkreten Fall nicht ausschließen will, schließlich ist das schon zwei
Monate her und ich habe mich für einige Prüfungen angemeldet und keine
automatische Bestätigung der Anmeldung erhalten.

## Verbesserungsvorschlag

Kurz und gut: Ich will, dass die Uni ein digitales Signaturverfahren einsetzt
und die technischen Möglichkeiten nutzt, um den Studenten zu helfen ihre Rechte
durchzusetzen. Wie das genau funktionieren soll, wird im Folgenden erklärt.

### Ausführlich
Zur Verbesserung dieser Situation schlage ich folgendes vor:

Studenten sollen die Möglichkeit bekommen, einen öffentlichen Schlüssel
hochzuladen:

{% caption align="aligncenter" width="500" alt="Einen Schlüssel hinzufügen" text="Einen Schlüssel hinzufügen" url="../images/2014/04/kit-pgp-personal-data.png" %}

{% caption align="aligncenter" width="500" alt="Einen Schlüssel hinzufügen" text="Einen Schlüssel hinzufügen" url="../images/2014/04/kit-pgp-personal-management.png" %}

Mit diesem signieren sie Prüfungsanmeldungen:

{% caption align="aligncenter" width="500" alt="Prüfungsanmeldung signieren" text="Prüfungsanmeldung signieren" url="../images/2014/04/kit-pgp-pruefungsanmeldung-signieren.png" %}

Bei jeder Prüfungsanmeldung soll innerhalb von 24h eine E-Mail in Textform
(keine PDF) an u****@student.kit.edu, also die KIT E-Mail-Adresse des Studenten,
geschickt werden, der sich angemeldet hat.

Diese E-Mail soll folgendes beinhalten:

* Alle Prüfungen (mit Name, Termin der Prüfung, letzter An- und Abmeldetermin),
  zu den der Student angemeldet ist.
* Der volle Name und die Matrikelnummer des Studenten.
* Das Datum der E-Mail.

Diese E-Mail soll mit einem offiziellen KIT Schlüssel signiert werden.
Dies könnte z.B. mit PGP gemacht werden und würde dann etwa so aussehen:

> -----BEGIN PGP SIGNED MESSAGE-----<br/>
> Hash: SHA1<br/>
> <br/>
> Student: Martin Thoma (Matrikelnummer: 1612345)<br/>
> Zeitpunkt: 08.04.2014, 12:34:56 Uhr<br/>
> Angemeldete Prüfungen:<br/>
> * Programmierparadigmen (Prüfungstermin: 10.04.2014; letzter Termin der Anmeldung: 31.03.2014; letzer Termin der Abmeldung: 08.04.2014)<br/>
> * Kognitive Systeme (Prüfungstermin: 11.04.2014; letzter Termin der Anmeldung: 15.03.2014; letzer Termin der Abmeldung: 10.04.2014)<br/>
> <br/>
> -----BEGIN PGP SIGNATURE-----<br/>
> Version: GnuPG v1.4.14 (GNU/Linux)<br/>
> <br/>
> iEYEARECAAYFAlNDzBoACgkQO3Q6GUuCW82z+ACfamkVC/S8HIpASH8F0ZGVbVW1<br/>
> rgwAn2cRvNeDN3pZVTpvNWV1vYK9f1fI<br/>
> =3DvZU7<br/>
> -----END PGP SIGNATURE-----

Der Student sollte jederzeit die Möglichkeit haben, eine wie oben beschriebene
signierte E-Mail mit der Liste der Prüfungen und einem Datum zu erhalten.

Nun sollen Studenten in der Klausur die Möglichkeit haben, diese E-Mail auf
einem USB-Stick mitzubringen. Die Aufsicht müsste also einen Computer haben,
mit dem sie die E-Mail anschauen und insbesondere die Signatur überprüfen
können. So könnte ein Student, der einmal zu einer Klausur angemeldet das auch
belegen.

### Abmeldungen
Die auf den ersten Blick sehr schöne Lösung hat einen wichtigen
Schönheitsfehler: Studenten können sich von Prüfungen abmelden. Daher ist es
möglich, dass ein Student eine signierte E-Mail hat, die ihm die Anmeldung
zur Prüfung bestätigt, er aber dennoch nicht zur Prüfung angemeldet ist, da
er sich abgemeldet hat.

Deshalb wäre es nötig, dass jeder Student ein eigenes Schlüsselpaar
aus einem öffentlichen und einem privaten Schlüssel erstellt. Wenn sich ein
Student von der Prüfung abmeldet, bekommt er einen Text, z. B. etwas in dieser
Richtung:

> Ich, Martin Thoma (Matrikelnummer: 1612345), melde mich hiermit 
> am 08.04.2014 um 12:34:56 Uhr von der Prüfung "Programmierparadigmen" 
> (Prüfungsdatum: 10.04.2014) ab.

Diese muss er mit seinem privaten Schlüssel signieren. Die Uni muss daher den
öffentlichen Schlüssel des Studenten kennen und diesem zugeordnet haben.
Sobald die Abmeldung eingegangen ist, wird innerhalb von 24h eine Bestätigung
an den Studenten verschickt, die von der oben beschriebenen Form ist.

oder auch eine Fehlermitteilung:

> Sehr geehrter Herr Thoma,<br/>
> die Signatur ihrer Nachricht war ungültig. Bitte überprüfen Sie, ob Sie den
> korrekten privaten Schlüssel verwendet haben.

Nun hätte auch die Klausuraufsicht die Möglichkeit zu belegen, dass ein
Student sich von der Prüfung abgemeldet hat.

### Technik-Afinität

Was ist mit Studenten, die es nicht schaffen ein Schlüsselpaar zu erzeugen bzw.
eine Nachricht zu signieren?

Nun, das ist einfach: Wer keinen öffentlichen Schlüssel hinterlegt, bekommt
auch keine signierten Nachrichten. Dennoch sollten diese Studenten die E-Mails,
wie sie oben beschrieben wurden, bekommen. Dann weiß man als Student, dass
vermutlich alles mit der Anmeldung geklappt hat bzw. wenn die E-Mail nicht kommt,
dass etwas nicht geklappt hat.

Bevor also die erste signierte E-Mail der Uni an den Studenten geschrieben wird,
muss der Student seinen öffentlichen Schlüssel der Uni mitgeteilt haben und
eine Nachricht mit dem privaten Schlüssel signiert haben. Damit wird
sichergestellt, dass der Student prinzipiell in der Lage ist sich von
Prüfungen abzumelden.

### Student verliert Schlüssel

Was macht man, wenn ein Student einmal einen Schlüssel eingericht hat, diesen
aber verliert?

Was passiert, wenn man seinen Studentenausweis verliert? Ich denke die Vorgehensweise
wäre dann ähnlich.

Vorstellbar wäre etwas in der Art:

* Der Student muss zum Studienbüro und Schriftlich bestätigen, dass der
  öffentliche Schlüssel aus dem KIT-System entfernt wird und damit ungültig wird.
* Der Student muss sich bei allen Professoren persönlich melden und unterschreiben,
  wenn er sich von der Klausur abmelden will.

## PGP - Was ist das?

Siehe [Wikpedia](https://de.wikipedia.org/wiki/Pretty_Good_Privacy).

Es ist für folgende Systeme verfügbar:

* Linux, siehe z.B. [Ubuntu mit GnuPG](http://wiki.ubuntuusers.de/GnuPG)
* Windows, siehe z.B. [GPG4Win](http://www.gpg4win.org/index-de.html)
* Mac, siehe z.B. [Mac GNU Privacy Guard](http://sourceforge.net/projects/macgpg/)

Eine weitere Erklärung ist im [Piratenwiki](https://wiki.piratenpartei.de/PGP).

## Einfügen ins System
Die Website [wechall.net](http://www.wechall.net/) bietet die Möglichkeit,
einen PGP-Schlüssel hochzuladen. Sobald man das gemacht hat, werden dort alle
Nachrichten mit dem öffentlichen Schlüssel verschlüsselt. Der Quellcode der
Seite ist [hier](https://www.wechall.net/de/wechall.zip) verfügbar.

Mit PHP scheint das ganze sehr einfach zu sein ([Quelle](http://stackoverflow.com/q/15969740/562769)).
Auch mit Python sieht die Sache sehr leicht aus ([Quelle](https://pythonhosted.org/python-gnupg/)).

Da ich keine Ahnung habe was für campus.kit.edu verwendet wird, kann ich hier
leider nicht mehr dazu sagen.

Dann würde man noch eine Tabelle in der Datenbank benötigen. Die würde etwa so
aussehen:

```sql
CREATE TABLE IF NOT EXISTS "openpgp_keys" (
  "id" int(11) NOT NULL AUTO_INCREMENT,
  "student_id" int(11) NOT NULL,
  "public_pgp_key" text NOT NULL,
  "upload_date" datetime NOT NULL,
  "confirmation_date" datetime DEFAULT NULL,
  "is_activated" tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY ("id")
) AUTO_INCREMENT=1;
```

oder graphisch:

{% caption align="aligncenter" width="188" alt="openpgp_keys Tabelle" text="openpgp_keys Tabelle" url="../images/2014/04/openpgp_keys.png" %}

### Ressourcen

Sollte jemand den Vorschlag modifizieren wollen, hier ist das HTML dazu:

```html
<div class="content_full_portal">
        <h1>PGP/GPG</h1>
        <h2>Neuen Schlüssel hinzufügen</h2>
        <div style="width: 100%;">
            <div class="gwf3_formY">
                <form action="/account" method="post" enctype="multipart/form-data">
                    <table>
                        <tbody>
                            <tr><td>Öffentlichen Schlüssel als Datei hochladen</td><td>
                            </td><td><input type="file" name="gpg_file"></td></tr>
                            <tr><td colspan="3">oder hier einfügen</td></tr>
                            <tr><td colspan="3"><textarea id="gpg_paste" name="gpg_paste" cols="80" rows="8"></textarea></td></tr>
                            <tr><td></td><td></td><td><input type="submit" name="setup_gpg" value="Schlüssel hochladen"></td></tr>
                            <tr><td colspan="3"><input type="hidden" name="gwf3_csrf" value="gp1yqWh4"></td></tr>
                        </tbody>
                    </table>
                </form>
            </div>
        </div>

        <h2>Liste bekannter Schlüssel</h2>
        <table style="width:100%">
            <tbody><tr>
                <th>Name des Schlüssels</th>
                <th>Datum des Uploads</th>
                <th>Bestätigt</th>
                <th>Aktiviert</th>
            </tr>
            <tr>
                <td>sdfasdf asdfasd asdf</td>
                <td>12.10.2013, 14:45 Uhr</td>
                <td>am 12.10.2014, 16:00 Uhr</td>
                <td>Ja (<a href="">Deaktivieren</a>)</td>
            </tr>
            <tr>
                <td>asdfasdf asdf asdfa sdf &nbsp;</td>
                <td>02.04.2014, 06:01 Uhr</td>
                <td><a href="">noch nicht</a></td>
                <td>Nein (<a href="">Aktivieren</a>)</td>
            </tr>
        </tbody></table>

        
    </div>
```

und

```html
<div class="content_full_portal">
    <h1>Prüfungsanmeldung</h1>
    Signieren Sie folgende Nachricht mit ihrem Schlüssel:<br>

    <a href="">Nachricht als Textdatei herunterladen</a><br>

    oder<br>

    Nachricht zum kopieren:<br>
    <textarea style="width: 800px;height: 60px;">Hiermit melde ich, Martin Thoma (Matrikelnummer: 1612345), mich heute (28.03.2014, 12:34:56 Uhr) zur Prüfung 'Programmierparadigmen', die am 10.04.2014 statt findet, an. Mir ist bekannt, dass der letzte Zeitpunkt der Abmeldung am 08.04.2014 ist.</textarea>
    <h2>Anmeldung durchführen</h2>
    <form>
        <label for="filet">Signierte Bestätigung als Textdatei hochladen:</label><br>
        <input type="file" id="filet"><br>

        <p>oder signierte Bestätigung direkt einfügen:<br></p>
        <label for="textareat"></label>
        <textarea id="textareat" style="width: 800px;height: 60px;"></textarea><br>
        <input type="submit">
    </form>
</div>
```

## Weitere Probleme der Prüfungsorganisation

In diesem Artikel will ich nur die Prüfungsverwaltung diskutieren. Dennoch
sollte darauf hingewiesen werden, dass Weiteres nicht gerade optimal gelöst ist:

* **Informationspolitik**: Bereits zu Semesterbegin sollte  folgendes bekannt sein:
  * Zeitpunkt der Prüfung
  * Letztmöglicher Zeitpunkt der Anmeldung
  * Letztmöglicher Zeitpunkt der Abmeldung
* Die **Anmeldungsfreischaltung** der Prüfungen finden zu sehr unterschiedlichen
  Zeitpunkten statt. Die Anmeldung sollte breits zu Semesterbegin für alle
  Klausuren möglich sein.
* Die **Einsicht** ist immer schlecht organisiert. Da sich die Prüfungstermine
  größtenteils in der vorlesungsfreien Zeit befinden und darin aber stark 
  gestreut sind (manche sind zu Beginn, manche in der Mitte, manche am Ende)
  sind die Zeitpunkte, zu denen
  man als Student Ferien hat sehr stark eingeschränkt. Wenn man dann erst nach
  der Klausur erfährt, wann die Einsicht sein wird, kann man Ferien komplett
  vergessen, weil man in Karlsruhe bleiben muss um auf den Termin der Einsicht
  zu warten.<br/>
  Bei den Physikern ist wenigstens die Korrektur immer sehr schnell, sodass man
  davon ausgehen kann, dass die Einsicht wenige Tage nach der Prüfung statt
  findet. Bei den Informatikern ... naja, da hat man ja noch Glück wenn sie im
  selben Monat ist. Und man es dann rechtzeitig erfährt.
* **Lösungen und Notengrenzen** sind nicht in jeder einsicht vorhanden bzw.
  klar. Gerade wenn nicht klar ist, mit welcher Punktzahl man welche Note
  bekommt könnte ein Fehler passieren, den man nicht überprüfen kann. Nach
  diesen Informationen sollte man nicht in der Einsicht fragen müssen. Sie
  sollten in der Einsicht direkt verfügbar sein.

## Schlusswort

Welche Vorteile hat das beschriebene Verfahren gegenüber der momentanen Situation?

* Studenten können beweisen, dass sie zur Prüfung angemeldet sind / nicht sind
* Prüfer können beweise, dass Studenten angemeldet sind / nicht sind

Selbst wenn man den Teil mit der asymmetrischen Verschlüsselung nicht macht, hätte man als Student
zumindest ein bisschen was in der Hand und einen Mechanismus, der automatisch
Feedback gibt, ob alles geklappt hat. Im Gegensatz zu der momentanen
Situation, wo wir absolut nichts belegen können und man sehr leicht übersehen
kann, wenn etwas bei der Anmeldung schief gegangen ist.

**Was haltet ihr davon? Hattet ihr auch schon solche Probleme mit der Prüfungsanmeldung?**