---
layout: post
title: Briefe mit LaTeX schreiben
author: Martin Thoma
date: 2012-03-03 17:48:38.000000000 +01:00
category: German posts
tags: LaTeX, scrlttr2
featured_image: 2012/01/latex-logo.png
---
Ich muss immer wieder mal Kündigungsschreiben aufsetzen. Dafür will ich eigentlich keine Zeit verschwenden, aber es sollte schon gut aussehen. Also habe ich mir gerade mal eine Vorlage für Kündigungsschreiben mit LaTeX und dem scrlttr2 Paket erstellt. Allerdings benutze ich noch die alten KOMA-Variablen. Ich finde mit KOMAold (siehe Beispiel-PDF <a href='../images/2012/03/kuendigung.pdf'>alt</a> und <a href='../images/2012/03/kuendigung-scrlttr2.pdf'>neu</a>) sieht es einfach besser aus als mit dem neuen. Obwohl der Unterschied nicht wirklich gro&szlig; ist.

Hier ist das <a href='../images/2012/03/kuendigung-archiv.zip'>Archiv</a> mit beiden LaTeX-Dateien, einer Make-Datei und beiden PDF-Dateien.

<h2>LaTeX</h2>
```latex
\documentclass[a4paper, 12pt, KOMAold]{scrlttr2}
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
\newcommand{\Empfaenger}{DB Fernverkehr AG} % Der Empfänger         %
\newcommand{\EStrasse}{BahnCard-Service}    % Stra&szlig;e des Empfängers %
\newcommand{\EPLZ}{60643}                   % PLZ des Empfängers    %
\newcommand{\EOrt}{Frankfurt am Main}       % Ort des Empfängers    %
                                                                    %
\newcommand{\DocTitle}{Kündigung des Bahn-Abos} %Titel des Dokuments%
% Datum der Kündigung                                               %
\newcommand{\Kuendigungsdatum}{nächstmöglichen Termin}              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% pdfinfo
\pdfinfo{
   /Author (\Nachname, \Vorname)
   /Title  (\DocTitle)
   /Subject (\DocTitle)
   /Keywords (Kündigung)
}

% set letter variables
\signature{\Vorname~\Nachname}
\customer{\Kundennr}
\backaddress{\Vorname~\Nachname, \Strasse~\Hausnummer, \PLZ~\Ort}

% Begin document %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{document}
    \begin{letter}{\Empfaenger \\ \EStrasse \\ \EPLZ~\EOrt}
    \date{\today}%Change this if you want a different date than today
    \subject{Kündigung}
    \opening{Sehr geehrte Damen und Herren,}
    hiermit kündige ich meinen Vertrag für die Kundennummer
	\Kundennr~ zum \Kuendigungsdatum.\\

    \noindent Ich bitte um eine Bestätigung der Kündigung.
    \closing{Mit freundlichen Grü&szlig;en,}
    \end{letter}
\end{document}
```

Ach ja, wei&szlig; jemand wie man die Einrückung der Unterschrift verhindert?
