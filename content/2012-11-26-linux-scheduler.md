---
layout: post
title: Linux Scheduler
slug: linux-scheduler
lang: de
author: Martin Thoma
date: 2012-11-26 23:25:15.000000000 +01:00
category: German posts
tags: Linux, OS, Operating Systems, Scheduler, Computer Science
featured_image: 2012/11/scheduler.png
---
<div class="info">Der folgende Text wurde von <a href="http://klammler.eu/">Moritz Klammler</a>, einem Informatik-Studenten am KIT, als E-Mail an die interne Mailingliste der Vorlesung geschrieben. Ich habe nur ein paar Kleinigkeiten umformuliert und die Formattierung geändert.</div>

<h2>Mailinglisten-Beitrag</h2>
Der in der Vorlesung vorgestellte $\mathcal{O}(1)$ Scheduler<small><sup><a href="#ref1" name="anchor1">[1]</a></sup></small> wurde vom 2.6er Linux Kernel bis Version 2.6.23 verwendet und dann durch den sogenannten Completely Fair Scheduler (CFS)<small><sup><a href="#ref2" name="anchor2">[2]</a></sup></small> abgelöst, der Rot-Schwarz-Bäume verwendet, und daher in $\mathcal{O}(\log(n))$ läuft -- dafür aber komplett fair ist 😉 Beide Scheduler wurden von Ingo Moln&aacute;r entworfen und größtenteils implementiert. Abgesehen von den Wikipedia Artikeln fand ich auch Ingos eigene Beschreibung<small><sup><a href="#ref3" name="anchor1">[3]</a></sup></small> sehr interessant.  In der prä-2.6-Ära des Linux Kernels wurde ein Scheduler verwendet, zu dessen Effizienz ich keine Angaben gefunden habe.  Anhand der (ziemlich detaillierten) Beschreibung in Kapitel 10 von &bdquo;Understanding the Linux Kernel&ldquo;<small><sup><a href="#ref4" name="anchor4">[1]</a></sup></small> gehe ich jedoch davon aus, dass es $\mathcal{O}(n)$ gewesen sein muss.  Auch wenn die dort beschriebenen Algorithmen inzwischen mehrfach überholt sind, fand ich das Kapitel sehr lesenswert.

Wie in der Vorlesung vermutet wurde, kann man den Scheduler natürlich konfigurieren.  Dazu ist es aber nicht notwendig, neu zu kompilieren -- noch nicht einmal neu zu booten. Stattdessen kann man (beim CFS) einfach über das /proc Dateisystem in die verschiedenen Dateien in

  <code>/proc/sys/kernel/...</code>

schreiben. Die Änderungen werden instantan wirksam. (Und spätestens zum nächsten Reboot wieder zurückgesetzt, man kann also nicht viel kaputt machen.)  Permanente Änderungen kann man in <code>/etc/sysctl.conf</code> schreiben. (Habe ich noch nicht probiert.)

Ich habe ein kleines Programm geschrieben, das sehr viele Subprozesse erzeugt, die alle sinnlose Rechnungen auf der CPU ausführen und zwischendurch in regelmäßigen Intervallen eine (eigentlich zwei) Zellen auf dem Terminal umfärben.  Man kann anhand dessen, wie sich das Muster ändert, schön sehen, wie oft ein einzelner Prozess an die Reihe kommt, und wie lange er es bleibt, wenn er es einmal ist.  Das Programm kann von <a href="http://klammler.eu/data/computer-science/kit/os/blink-1.0.tar.gz">meiner Website</a> heruntergeladen werden.  In dem Archiv ist auch ein kleines Shell-Skript, <code>sched-tune.sh</code>, mit dem man die wichtigsten Parameter ändern kann.  Die README Datei in dem Archiv erklärt genauer, wie man das Programm benutzen kann.

Da der Bildschirm beim Ausführen des Programms (gewollt) stark flackert, muss ich Epileptikern und anderen empfindlichen Personen unter Umständen leider davon abraten.

Leider lässt der Kernel keine völlig unsinnigen Werte zu.  Man kann also nur bedingt ausprobieren, welchen Einfluss extreme Einstellungen haben / hätten.  Wie in Referenz 4 beschrieben, &bdquo;friert&ldquo; die grafische Oberfläche übrigens auch nicht ein, wenn man größere Scheduling Intervalle wählt, da jeder Tastendruck einen Interrupt auslöst, der -- egal wie geschedulet wird -- immer die Kontrolle an jenen Prozess übergibt, der gerade das Keyboard &bdquo;gegrabbt&ldquo; hat.


Grüße

Moritz

<h2>Video</h2>
Ich habe mal ein Video von Moritz' Programm gemacht:
<iframe width="420" height="315" src="//www.youtube.com/embed/DOOrbrcM3YU" frameborder="0" allowfullscreen></iframe>

<h2>Referenzen</h2>
[1] <a name="ref1" href="#anchor1">&uarr;</a>: &bdquo;<a href="http://en.wikipedia.org/wiki/O%281%29_scheduler">O(1) Scheduler</a>&ldquo; in: Wikipedia, the free encyclopedia.  Abgerufen am 13.&nbsp;November 2012.
[2] <a name="ref2" href="#anchor2">&uarr;</a>: &bdquo;<a href="http://en.wikipedia.org/wiki/Completely_Fair_Scheduler">Completely Fair Scheduler</a>&ldquo; in: Wikipedia, the free encyclopedia. Abgerufen am 13. November 2012.
[3] <a name="ref3" href="#anchor3">&uarr;</a>: Ingo Moln&aacute;r, &bdquo;<a href="http://people.redhat.com/mingo/cfs-scheduler/sched-design-CFS.txt">This is the CFS scheduler</a>&ldquo;.  Abgerufen am 13. November 2012.
[4] <a name="ref4" href="#anchor4">&uarr;</a>: Daniel P. Bovet und Marco Cesati, &bdquo;<a href="http://oreilly.com/catalog/linuxkernel/chapter/ch10.html">Understanding the Linux Kernel</a>&ldquo;. O'Reilly, 2000, abgerufen am 13. November 2012.
