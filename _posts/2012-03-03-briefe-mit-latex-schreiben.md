---
layout: post
title: Briefe mit LaTeX schreiben
author: Martin Thoma
date: 2012-03-03 17:48:38.000000000 +01:00
categories:
- German posts
tags:
- LaTeX
- scrlttr2
featured_image: 2012/01/latex-logo.png
---
Ich muss immer wieder mal K&uuml;ndigungsschreiben aufsetzen. Daf&uuml;r will ich eigentlich keine Zeit verschwenden, aber es sollte schon gut aussehen. Also habe ich mir gerade mal eine Vorlage f&uuml;r K&uuml;ndigungsschreiben mit LaTeX und dem scrlttr2 Paket erstellt. Allerdings benutze ich noch die alten KOMA-Variablen. Ich finde mit KOMAold (siehe Beispiel-PDF <a href='../images/2012/03/kuendigung.pdf'>alt</a> und <a href='../images/2012/03/kuendigung-scrlttr2.pdf'>neu</a>) sieht es einfach besser aus als mit dem neuen. Obwohl der Unterschied nicht wirklich gro&szlig; ist.

Hier ist das <a href='../images/2012/03/kuendigung-archiv.zip'>Archiv</a> mit beiden LaTeX-Dateien, einer Make-Datei und beiden PDF-Dateien.

<h2>LaTeX</h2>
{% highlight text %}\documentclass[a4paper, 12pt, KOMAold]{scrlttr2}
\usepackage[utf8]{inputenc} % this is needed for umlauts
\usepackage[ngerman]{babel} % this is needed for umlauts
\usepackage[T1]{fontenc}    % needed for right umlaut output in pdf
\usepackage[ngerman, num]{isodate} % get DD.MM.YYYY dates

% Anpassen %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Vorname}{Martin}     % Vorname                         %
\newcommand{\Nachname}{Thoma}     % Nachname                        %
\newcommand{\Strasse}{Parkstra&szlig;e} % Deine Stra&szlig;e                    %
\newcommand{\Hausnummer}{17}      % Deine Hausnummer                %
\newcommand{\PLZ}{76131}          % Deine PLZ                       %
\newcommand{\Ort}{Karlsruhe}      % Dein Ort                        %
\newcommand{\Kundennr}{123456}    % Deine Kundennummer              %
                                                                    %
\newcommand{\Empfaenger}{DB Fernverkehr AG} % Der Empf&auml;nger         %
\newcommand{\EStrasse}{BahnCard-Service}    % Stra&szlig;e des Empf&auml;ngers %
\newcommand{\EPLZ}{60643}                   % PLZ des Empf&auml;ngers    %
\newcommand{\EOrt}{Frankfurt am Main}       % Ort des Empf&auml;ngers    %
                                                                    %
\newcommand{\DocTitle}{K&uuml;ndigung des Bahn-Abos} %Titel des Dokuments%
% Datum der K&uuml;ndigung                                               %
\newcommand{\Kuendigungsdatum}{n&auml;chstm&ouml;glichen Termin}              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% pdfinfo
\pdfinfo{
   /Author (\Nachname, \Vorname)
   /Title  (\DocTitle)
   /Subject (\DocTitle)
   /Keywords (K&uuml;ndigung)
}

% set letter variables
\signature{\Vorname~\Nachname}
\customer{\Kundennr}
\backaddress{\Vorname~\Nachname, \Strasse~\Hausnummer, \PLZ~\Ort}

% Begin document %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{document}
    \begin{letter}{\Empfaenger \\ \EStrasse \\ \EPLZ~\EOrt}
    \date{\today}%Change this if you want a different date than today
    \subject{K&uuml;ndigung}
    \opening{Sehr geehrte Damen und Herren,}
    hiermit k&uuml;ndige ich meinen Vertrag f&uuml;r die Kundennummer 
	\Kundennr~ zum \Kuendigungsdatum.\\

    \noindent Ich bitte um eine Best&auml;tigung der K&uuml;ndigung.
    \closing{Mit freundlichen Gr&uuml;&szlig;en,}
    \end{letter}
\end{document}{% endhighlight %}

Ach ja, wei&szlig; jemand wie man die Einr&uuml;ckung der Unterschrift verhindert?
