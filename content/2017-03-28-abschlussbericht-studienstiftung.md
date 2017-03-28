---
layout: post
title: Abschlussbericht der Studienstiftung
slug: abschlussbericht-studienstiftung
author: Martin Thoma
date: 2017-03-28 20:00
category: Cyberculture
tags: LaTeX, Studienstiftung
featured_image: 2012/06/Studienstiftung-Logo.png
---
Stipendiaten der Studienstiftung des deutschen Volkes müssen am Ende ihres
Studiums einen Abschlussbericht schreiben.

Damit sich andere Stipendiaten nicht auch jedes mal die Vorlage erstellen
müssen, stelle ich meine LaTeX-Vorlage hier bereit. Wenn ihr
Verbesserungsvorschläge habt, könnt ihr mir gerne eine E-Mail schreiben
(info@martin-thoma.de) oder einen Kommentar hinterlassen.

## Vorlage

```
\documentclass[a4paper,12pt]{article}
\usepackage{amssymb} % needed for math
\usepackage{amsmath} % needed for math
\usepackage[utf8]{inputenc} % this is needed for umlauts
\usepackage[ngerman]{babel} % this is needed for umlauts
\usepackage[T1]{fontenc}    % this is needed for correct output of umlauts in pdf
\usepackage[margin=2.5cm,headheight=40pt]{geometry} %layout
\usepackage{fancyhdr}  % needed for the footer
\usepackage{lastpage}  % needed for the footer
\usepackage{hyperref}  % links im text
\usepackage{graphicx}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Hier eigene Daten einfügen                                        %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Name}{Martin Thoma}
\newcommand{\Datum}{\today}        % Wann wurde der Bericht erstellt?
\newcommand{\Ort}{Karlsruhe}
\newcommand{\Uni}{KIT}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\hypersetup{
  pdfauthor   = {\Name},
  pdfkeywords = {Studienstiftung; \Uni; \Name},
  pdftitle    = {Abschlussbericht von \Name}
}

\pagestyle{fancy}
\fancyhead[CO,CE]{Abschlussbericht von \Name}
% \renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancyfoot[C]{}
\fancyfoot[R]{Seite~\thepage~von \pageref{LastPage}}

\pagenumbering{arabic}

\begin{document}

\title{Abschlussbericht von \Name}
\author{\Name}
\date{\Datum}

Was waren die wichtigsten Ereignisse in Ihrem Studium? Was hätten Sie im
Rückblick lieber anders gemacht, was hat sich bewährt?

Welche Bedeutung hatte die Förderung durch die Studienstiftung für Ihr Studium
und Ihre persönliche Entwicklung?

Welche Angebote der Studienstiftung waren für Sie hilfreich, welche weniger?
Denken Sie dabei bitte neben den Veranstaltungen (Sommerakademie, Sprachkurs)
auch an die Sprechstunden der Referenten, die Vertrauensdozentengruppe, das
Intranet und die Auslandsförderung.

Was haben Sie unter den Angeboten der Studienstiftung vermisst? Wo sehen Sie
Verbesserungsmöglichkeiten für unsere Förderung von Stipendiaten?

Wie sehen Ihre Zukunftspläne aus? In welche Richtung orientieren Sie sich
zurzeit?
\vspace{1cm}\\
\Ort, der \Datum\\
\\% see https://martin-thoma.com/how-to-create-a-digital-signature/
Martin Thoma


\end{document}

```

und Makefile

```
DOKUMENT = abschlussbericht

make:
    pdflatex $(DOKUMENT).tex -output-format=pdf
    pdflatex $(DOKUMENT).tex -output-format=pdf
    make clean

clean:
    rm -rf  $(TARGET) *.class *.html *.log *.aux *.out
```


## FAQ

<ul>
    <li>Wozu dient der Bericht?<br/>
        → "Ein Rückblick auf Ihr Studium hilft uns unter anderem bei der Beratung jüngerer Stipendiaten." (vgl. Daidalosnet, Abschlussbericht)</li>
    <li>Welche Form soll der Bericht haben?<br/>
        → Es gibt keine Vorgabe. 2 - 3 Seiten Umfang sind angemessen.</li>
    <li>Was soll inhaltlich rein?<br/>
        → vgl. Daidalosnet
    <ol>
        <li>Was waren die wichtigsten Ereignisse in Ihrem Studium? Was hätten Sie im Rückblick lieber anders gemacht, was hat sich bewährt?</li>
        <li>Welche Bedeutung hatte die Förderung durch die Studienstiftung für Ihr Studium und Ihre persönliche Entwicklung?</li>
        <li>Welche Angebote der Studienstiftung waren für Sie hilfreich, welche weniger? Denken Sie dabei bitte neben den Veranstaltungen (Sommerakademie, Sprachkurs) auch an die Sprechstunden der Referenten, die Vertrauensdozentengruppe, das Intranet und die Auslandsförderung.</li>
        <li>Was haben Sie unter den Angeboten der Studienstiftung vermisst? Wo sehen Sie Verbesserungsmöglichkeiten für unsere Förderung von Stipendiaten?</li>
        <li>Wie sehen Ihre Zukunftspläne aus? In welche Richtung orientieren Sie sich zurzeit?</li>
    </ol>

    </li>
    <li>Wer liest den Bericht?<br/>
        → Nur der/die VertrauensdozentIn und ReferentIn. Die Berichte werden
        wohl sehr vertraulich behandelt. Zum Beispiel hat die Studienstiftung
        auch die jeweiligen Berichte im Laufe der Ermittlungen gegen die
        RAF-Mitglieder nicht rausgerückt.</li>
</ul>
