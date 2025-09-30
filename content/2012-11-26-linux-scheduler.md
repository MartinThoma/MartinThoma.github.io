---
layout: post
lang: de
title: Linux Scheduler
slug: linux-scheduler
author: Martin Thoma
date: 2012-11-26 23:25:15.000000000 +01:00
category: German posts
tags: Linux, OS, Operating Systems, Scheduler
featured_image: 2012/11/scheduler.png
---
<div class="info">Der folgende Text wurde von <a href="http://klammler.eu/">Moritz Klammler</a>, einem Informatik-Studenten am KIT, als E-Mail an die interne Mailingliste der Vorlesung geschrieben. Ich habe nur ein paar Kleinigkeiten umformuliert und die Formattierung ge&auml;ndert.</div>

<h2>Mailinglisten-Beitrag</h2>
Der in der Vorlesung vorgestellte $\mathcal{O}(1)$ Scheduler<small><sup><a href="#ref1" name="anchor1">[1]</a></sup></small> wurde vom 2.6er Linux Kernel bis Version 2.6.23 verwendet und dann durch den sogenannten Completely Fair Scheduler (CFS)<small><sup><a href="#ref2" name="anchor2">[2]</a></sup></small> abgel&ouml;st, der Rot-Schwarz-B&auml;ume verwendet, und daher in $\mathcal{O}(\log(n))$ l&auml;uft -- daf&uuml;r aber komplett fair ist 😉 Beide Scheduler wurden von Ingo Moln&aacute;r entworfen und gr&ouml;&szlig;tenteils implementiert. Abgesehen von den Wikipedia Artikeln fand ich auch Ingos eigene Beschreibung<small><sup><a href="#ref3" name="anchor1">[3]</a></sup></small> sehr interessant.  In der pr&auml;-2.6-&Auml;ra des Linux Kernels wurde ein Scheduler verwendet, zu dessen Effizienz ich keine Angaben gefunden habe.  Anhand der (ziemlich detaillierten) Beschreibung in Kapitel 10 von &bdquo;Understanding the Linux Kernel&ldquo;<small><sup><a href="#ref4" name="anchor4">[1]</a></sup></small> gehe ich jedoch davon aus, dass es $\mathcal{O}(n)$ gewesen sein muss.  Auch wenn die dort beschriebenen Algorithmen inzwischen mehrfach &uuml;berholt sind, fand ich das Kapitel sehr lesenswert.

Wie in der Vorlesung vermutet wurde, kann man den Scheduler nat&uuml;rlich konfigurieren.  Dazu ist es aber nicht notwendig, neu zu kompilieren -- noch nicht einmal neu zu booten. Stattdessen kann man (beim CFS) einfach &uuml;ber das /proc Dateisystem in die verschiedenen Dateien in

  <code>/proc/sys/kernel/...</code>

schreiben. Die &Auml;nderungen werden instantan wirksam. (Und sp&auml;testens zum n&auml;chsten Reboot wieder zur&uuml;ckgesetzt, man kann also nicht viel kaputt machen.)  Permanente &Auml;nderungen kann man in <code>/etc/sysctl.conf</code> schreiben. (Habe ich noch nicht probiert.)

Ich habe ein kleines Programm geschrieben, das sehr viele Subprozesse erzeugt, die alle sinnlose Rechnungen auf der CPU ausf&uuml;hren und zwischendurch in regelm&auml;&szlig;igen Intervallen eine (eigentlich zwei) Zellen auf dem Terminal umf&auml;rben.  Man kann anhand dessen, wie sich das Muster &auml;ndert, sch&ouml;n sehen, wie oft ein einzelner Prozess an die Reihe kommt, und wie lange er es bleibt, wenn er es einmal ist.  Das Programm kann von <a href="http://klammler.eu/data/computer-science/kit/os/blink-1.0.tar.gz">meiner Website</a> heruntergeladen werden.  In dem Archiv ist auch ein kleines Shell-Skript, <code>sched-tune.sh</code>, mit dem man die wichtigsten Parameter &auml;ndern kann.  Die README Datei in dem Archiv erkl&auml;rt genauer, wie man das Programm benutzen kann.

Da der Bildschirm beim Ausf&uuml;hren des Programms (gewollt) stark flackert, muss ich Epileptikern und anderen empfindlichen Personen unter Umst&auml;nden leider davon abraten.

Leider l&auml;sst der Kernel keine v&ouml;llig unsinnigen Werte zu.  Man kann also nur bedingt ausprobieren, welchen Einfluss extreme Einstellungen haben / h&auml;tten.  Wie in Referenz 4 beschrieben, &bdquo;friert&ldquo; die grafische Oberfl&auml;che &uuml;brigens auch nicht ein, wenn man gr&ouml;&szlig;ere Scheduling Intervalle w&auml;hlt, da jeder Tastendruck einen Interrupt ausl&ouml;st, der -- egal wie geschedulet wird -- immer die Kontrolle an jenen Prozess &uuml;bergibt, der gerade das Keyboard &bdquo;gegrabbt&ldquo; hat.


Gr&uuml;&szlig;e

Moritz

<h2>Video</h2>
Ich habe mal ein Video von Moritz' Programm gemacht:
<iframe width="420" height="315" src="//www.youtube.com/embed/DOOrbrcM3YU" frameborder="0" allowfullscreen></iframe>

<h2>Referenzen</h2>
[1] <a name="ref1" href="#anchor1">&uarr;</a>: &bdquo;<a href="http://en.wikipedia.org/wiki/O%281%29_scheduler">O(1) Scheduler</a>&ldquo; in: Wikipedia, the free encyclopedia.  Abgerufen am 13.&nbsp;November 2012.
[2] <a name="ref2" href="#anchor2">&uarr;</a>: &bdquo;<a href="http://en.wikipedia.org/wiki/Completely_Fair_Scheduler">Completely Fair Scheduler</a>&ldquo; in: Wikipedia, the free encyclopedia. Abgerufen am 13. November 2012.
[3] <a name="ref3" href="#anchor3">&uarr;</a>: Ingo Moln&aacute;r, &bdquo;<a href="http://people.redhat.com/mingo/cfs-scheduler/sched-design-CFS.txt">This is the CFS scheduler</a>&ldquo;.  Abgerufen am 13. November 2012.
[4] <a name="ref4" href="#anchor4">&uarr;</a>: Daniel P. Bovet und Marco Cesati, &bdquo;<a href="http://oreilly.com/catalog/linuxkernel/chapter/ch10.html">Understanding the Linux Kernel</a>&ldquo;. O'Reilly, 2000, abgerufen am 13. November 2012.
