---
layout: post
title: LaTeX-Vorlage f&uuml;r den Semesterbericht der Studienstiftung
author: Martin Thoma
date: 2012-06-04 07:31:36.000000000 +02:00
categories:
- German posts
tags:
- LaTeX
- Studienstiftung
featured_image: 2012/06/Studienstiftung-Logo.png
---
Stipendiaten der Studienstiftung des deutschen Volkes m&uuml;ssen jedes Semester einen Studienbericht schreiben. 

Damit sich andere Stipendiaten nicht auch jedes mal die Vorlage erstellen m&uuml;ssen, stelle ich meine LaTeX-Vorlage hier bereit. Wenn ihr Verbesserungsvorschl&auml;ge habt, k&ouml;nnt ihr mir gerne eine Email schreiben (info@martin-thoma.de) oder einen Kommentar hinterlassen.

<h2>Wozu dient der Semesterbericht?</h2>
Im Daidalosnet steht dazu:

<blockquote>Der Studienbericht bietet Gelegenheit, &uuml;ber die wesentlichen Inhalte und Erfahrungen des letzten Semesters nachzudenken sowie die beiden Leser - den Vertrauensdozenten und den Referenten - zu informieren und an Reflexionen und Bewertungen teilnehmen zu lassen. Ohne die Berichte w&auml;re die Studienstiftung weniger oder kaum in der Lage, ein aktuelles Wissenschaftliches Programm zu bieten und die Stipendiaten verl&auml;sslich zu beraten.
Nach der Lekt&uuml;re des Berichtes sollten die Leser ein Bild vom Verlauf des Studiums und von fachlichen und au&szlig;erfachlichen Aktivit&auml;ten gewonnen haben. Ein Umfang von zwei bis drei Seiten ist angemessen.</blockquote>

<h2>Wer bekommt wann den Studienbericht?</h2>
<blockquote>Stipendiaten, die endg&uuml;ltig in die Studienstiftung aufgenommen worden sind, schreiben Jahresberichte jeweils zum <strong>1. August</strong>. Stipendiaten vor der endg&uuml;ltigen Aufnahme schreiben Semesterberichte, jeweils zum <strong>1. M&auml;rz</strong> und zum 1. August.</blockquote>

Mit dem Semesterbericht f&uuml;r das WS 2012/2013 soll der Bericht nicht mehr an den zust&auml;ndigen Referenten bzw. Vertrauensdozenten geschickt werden, sondern direkt ins Daidalosnet geladen werden: 

<blockquote>Bitte laden Sie Ihren Bericht als PDF-Dokument im Daidalosnet hoch. Sie finden die Eingabemaske in Ihrem eigenen Kurzprofil ("<strong>Meine Einstellungen</strong>" unten rechts) - hier ist in der unteren Bildschirmh&auml;lfte die Rubrik "<strong>Studienberichte</strong>" zu finden. Wenn Sie hier einen als "offen" gekennzeichneten Eintrag finden, m&uuml;ssen Sie uns einen Bericht zukommen lassen - bitte folgen Sie dem Link in der Zeile unter "offen", um zur Eingabemaske zu gelangen. Sowohl Ihr/e Referent/in als auch Ihr/e Vertrauensdozent/in erhalten automatisch eine Kopie des Berichts per E-Mail.</blockquote>

<h3>Wer ist mein zust&auml;ndiger Referent bzw. mein Vertrauensdozent?</h2>
<ol>
  <li>Logge dich im <a href="https://www.daidalosnet.de/">daidalosnet</a> ein.</li>
  <li>Klicke rechts unten auf "Meine Einstellungen".</li>
  <li>Klicke auf "Gespeicherte Daten".</li>
  <li>Nun sollte "Referent/in" sowie "aktueller Vertrauensdozent" dort stehen.</li>
</ol>

<h2>Die Vorlage</h2>
Hier ist die Vorlage mit Blindtext als <a href='../images/2012/06/semesterbericht-ws-2011.pdf'>PDF</a>.

Makefile:
{% highlight text %}DOKUMENT = semesterbericht-martin-thoma-ws-2011

make:
	pdflatex $(DOKUMENT).tex -output-format=pdf
	pdflatex $(DOKUMENT).tex -output-format=pdf
	make clean

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux *.out{% endhighlight %}

LaTeX:
{% highlight text %}\documentclass[a4paper,12pt]{article}
\usepackage{amssymb} % needed for math
\usepackage{amsmath} % needed for math
\usepackage[utf8]{inputenc} % this is needed for umlauts
\usepackage[ngerman]{babel} % this is needed for umlauts
\usepackage[T1]{fontenc}    % this is needed for correct output of umlauts in pdf
\usepackage[margin=2.5cm]{geometry} %layout
\usepackage{fancyhdr}  % needed for the footer
\usepackage{lastpage}  % needed for the footer
\usepackage{hyperref}  % links im text
\usepackage{color, colortbl}  % farbige Tabellenzellen
\usepackage{tabularx}
\clubpenalty  = 10000 % Schusterjungen verhindern
\widowpenalty = 10000 % Hurenkinder verhindern

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Hier eigene Daten einf&uuml;gen										%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Jahr}{2011/2012}          % Typ: "2011 / 2012" oder "2012"
\newcommand{\Semester}{Wintersemester} % "Wintersemester" oder "Sommersemester"
\newcommand{\Datum}{\today}            % Wann wurde der Bericht erstellt?
\newcommand{\Semesteranzahl}{1}        % Das Fachsemester als Zahl
\newcommand{\Gesamtsemesterzahl}{6}    % Die gesamte Anzahl an Semestern
\newcommand{\Abschluss}{Bachelor}
\newcommand{\Studienfach}{Informatik}
\newcommand{\University}{KIT}
\newcommand{\Nachname}{Thoma}
\newcommand{\Vorname}{Martin}
\newcommand{\Strasse}{Musterstra&szlig;e}
\newcommand{\Hausnummer}{123}
\newcommand{\PLZ}{76131}
\newcommand{\Ort}{Karlsruhe}
\newcommand{\Email}{info@martin-thoma.de}
\newcommand{\Vertrauensdozent}{Prof. Dr. <a href='../images/2012/06/semesterbericht-ws-2011.pdf'>Semesterbericht WS 2011</a>Mustermann}
\newcommand{\Referent}{Dr. Alice Brown}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\hypersetup{ 
  pdfauthor   = {\Vorname~\Nachname}, 
  pdfkeywords = {Studienstiftung; KIT; \Vorname~\Nachname}, 
  pdftitle    = {Semesterbericht von~\Vorname~\Nachname~-~\Semester~\Jahr} 
} 

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancyfoot[R]{Seite~\thepage~von \pageref{LastPage}}

\definecolor{LightCyan}{rgb}{0.88,1,1}

\pagenumbering{arabic}

\begin{document}

\title{Semesterbericht &uuml;ber das \Semester \Jahr}
\author{\Vorname \Nachname}
\date{\Datum}

\section*{Semesterbericht &uuml;ber das \Semester~\Jahr}
\begin{tabularx}{\textwidth}{@{}llllX}
Name, Vorname:   &amp; \Nachname, \Vorname &amp; Universit&auml;t         &amp; \University \\
Semesteradresse: &amp;\Strasse~\Hausnummer &amp; Studienfach         &amp; \Studienfach \\
                 &amp;\PLZ~\Ort~~~~~~~     &amp; Semesterzahl        &amp; \Semesteranzahl~von~\Gesamtsemesterzahl \\
                 &amp;                     &amp; Geplanter Abschluss &amp; \Abschluss \\
                 &amp;                     &amp; Vertrauensdozent    &amp; \Vertrauensdozent \\
E-Mail           &amp;\Email               &amp; Referent            &amp; \Referent \\
\end{tabularx}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Hier bitte Text einf&uuml;gen!										    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection*{Einleitende Zusammenfassung}
\subsubsection*{1. Auf diesem Stand ist jetzt mein Studium:}
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam 
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea 
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
ipsum dolor sit amet.

\subsubsection*{2. Das war f&uuml;r mich au&szlig;erhalb des Studiums von gro&szlig;er Bedeutung:}
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam 
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea 
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur 
sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore 
et dolore magna aliquyam erat, sed diam voluptua. At vero eos et 
accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum 
dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod 
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam 
voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum 
dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse 
molestie consequat, vel illum dolore eu feugiat nulla facilisis at 
vero eros et accumsan et iusto odio dignissim qui blandit praesent 
luptatum zzril delenit augue duis dolore te feugait nulla facilisi. 
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam 
nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat 
volutpat.   

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper 
suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem 
vel eum iriure dolor in hendrerit in vulputate velit esse molestie 
consequat, vel illum dolore eu feugiat nulla facilisis at vero eros 
et accumsan et iusto odio dignissim qui blandit praesent luptatum 
zzril delenit augue duis dolore te feugait nulla facilisi.   

Nam liber tempor cum soluta nobis eleifend option congue nihil 
imperdiet doming id quod mazim placerat facer

\subsubsection*{3. F&uuml;r das n&auml;chste Semester habe ich folgende Pl&auml;ne:}

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam 
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam 
erat, sed diam voluptua. At vero eos et accusam et justo duo 
dolores et ea rebum. Stet clita kasd gubergren, no sea takimata 
sanctus est Lorem ipsum dolor sit amet.

\newpage
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore 
magna aliquyam:

\begin{table}[h]
	\begin{tabular}{| l | c | c | l |}
	\hline
	\textbf{Modulbezeichnung} &amp; \textbf{SWS} &amp; \textbf{LP}  &amp; \textbf{Klausur} \\
	\hline
	\hline
	\rowcolor{yellow} Lineare Algebra und Analytische Geometrie      &amp; 8   &amp; 9   &amp; Im SS 2012 \\
	\rowcolor{yellow} Analysis I                                     &amp; 8   &amp; 9   &amp; Im SS 2012 \\
	\rowcolor{yellow} Grundbegriffe der Informatik                   &amp; 5   &amp; 4   &amp; Am 05. M&auml;rz 2012 \\
	\rowcolor{yellow} Programmieren                                  &amp; 4   &amp; 5   &amp; Abschlussaufgabe l&auml;uft \\
	\rowcolor{LightCyan} Betriebssysteme und Systemarchitektur       &amp; 6   &amp; 6   &amp; Am 26. M&auml;rz 2012 \\
	\rowcolor{LightCyan} Theoretische Grundlagen der Informatik      &amp; 6   &amp; 6   &amp; Benotung steht aus \\
	\rowcolor{LightCyan} Wahrscheinlichkeitstheorie f&uuml;r Informatiker &amp; 3   &amp; 4,5 &amp; mit 1,3 bestanden \\
	\hline
	\hline
	Gesamt                                                          &amp; 40  &amp; 43,5 &amp; \\
	\hline
	\end{tabular}

	\begin{tabular}{| l | l | l | l |}
	\hline
	\cellcolor{yellow} &amp; Teil der Orientierungspr&uuml;fung &amp; \cellcolor{LightCyan}  &amp; Pflichtmodul des 3. Semesters \\
	\hline
	\end{tabular}
\end{table}

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam 
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam 
erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea 
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur 
sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore 
et dolore magna aliquyam erat, sed diam voluptua. At vero eos et 
accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum 
dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod 
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam 
voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum 
dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse 
molestie consequat, vel illum dolore eu feugiat nulla facilisis at 
vero eros et accumsan et iusto odio dignissim qui blandit praesent 
luptatum zzril delenit augue duis dolore te feugait nulla facilisi. 
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam 
nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat 
volutpat.   

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper 
suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem 
vel eum iriure dolor in hendrerit in vulputate velit esse molestie 
consequat, vel illum dolore eu feugiat nulla facilisis at vero eros 
et accumsan et iusto odio dignissim qui blandit praesent luptatum 
zzril delenit augue duis dolore te feugait nulla facilisi.   

Nam liber tempor cum soluta nobis eleifend option congue nihil 
imperdiet doming id quod mazim placerat facer.\\
\\
\Ort, der \Datum\\
\\
\Vorname~\Nachname


\end{document}{% endhighlight %}
