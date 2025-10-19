---
layout: post
title: Web Engineering
slug: web-engineering
lang: de
author: Martin Thoma
date: 2013-01-03 13:57:06.000000000 +01:00
category: German posts
tags: Web Development, Klausur
featured_image: 2012/07/web-graph-thumb.jpg
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Web Engineering&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe Web Engineering bei Dr. Nussbaumer gehört.</div>

<h2>Über die Vorlesung</h2>
In der Vorlesung &bdquo;Web Engineering&ldquo; lernt man, welche besonderen Herausforderungen Web-Projekte beinhalten und wie man damit umgehen kann. Es wird zwar auch über technische Aspekte geredet (siehe Part 1), aber es geht vor allem um Projektplanung und -management. Insbesondere wird hier nichts konkret entwickelt. Dafür gibt es vermutlich das Praktikum, das aber unabhängig von der Vorlesung ist.

Herr Dr. Nussbaumer hält die Vorlesung sehr interaktiv. Er stellt viele Fragen, über die man in der Vorlesung diskutieren kann und ist auch immer nach der Vorlesung bereit etwas genauer zu erklären.

Die Struktur unter &bdquo;Vorbereitung&ldquo; richtet sich nach dem Aufbau der Folien.

<h2>Vorbereitung</h2>
Prüfungsprotokolle sind bei der <a href="http://www.fsmi.uni-karlsruhe.de/Studium/Pruefungsprotokolle/">Fachschaft Informatik</a> zu erhalten. <a href="../images/2013/01/muendlich-we-2013-martin-thoma.pdf">Mein Prüfungsprotokoll</a> ist hier und die <a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/kit-muendlich-info">TeX-Quelldateien</a> bekommt ihr natürlich auch.

Im Folgenden sind einige Stichpunkte aufgelistet, die jedem etwas sagen sollten.

<h3>Geschichte</h3>
<ul>
  <li>1945: <a href="http://de.wikipedia.org/wiki/Vannevar_Bush">Vannevar Bush</a>, <a href="http://de.wikipedia.org/wiki/Memex">Memex</a></li>
  <li>1965: <a href="http://de.wikipedia.org/wiki/Ted_Nelson">Ted Nelson</a>, Hypertext und Xanadu</li>
  <li>1969: ARPANET</li>
  <li>1985: Bill Atkinson (Apple), <a href="//www.youtube.com/watch?v=BeMRoYDc2z8">HyperCard</a></li>
  <li>1989: Tim Berners-Lee, World Wide Web</li>
  <li>1993: <a href="http://de.wikipedia.org/wiki/NCSA_Mosaic">Mosaic</a></li>
</ul>

<h3>PART 1: Technologies</h3>
<ul>
  <li>Markup, HTML, Ressources, Cookies, <abbr title="Multipurpose Internet Mail Extensions"><a href="http://de.wikipedia.org/wiki/MIME-Type">MIME</a></abbr></li>
  <li>Host, Server, Client, User Agent</li>
  <li>Hypertext Paradigm</li>
  <li>HTTP, HTTPS, FTP, SMTP, UDDI</li>
  <li>CGI</li>
  <li><a href="http://de.wikipedia.org/wiki/SOAP">SOAP</a>, <a href="http://de.wikipedia.org/wiki/WebDAV">WebDAV</a></li>
  <li>Moore's Law, Nielson's Law</li>
  <li>Was ist der Unterschied zwischen Software Engineering und Web Engineering? &rarr; Antwort auf Folie 47ff, part0-1</li>
  <li><a href="http://de.wikipedia.org/wiki/Paretoprinzip">Paretoprinzip</a></li>
  <li>Was ist das W3C? Was sind die Ziele des W3C? Wer ist Teil des W3C?</li>
  <li><a href="http://de.wikipedia.org/wiki/Zonendatei">Zone File</a></li>
  <li>Uniform addressing &rarr; Was ist das?</li>
  <li>URI, URL, URN, URC, RFC1630</li>
</ul>

<h3>PART 2: Project Management</h3>
<ul>
  <li><a href="http://de.wikipedia.org/wiki/Chaos-Studie">Chaos-Report</a> der Standish Group (25%, 45%, 30%)
    <ul>
      <li>Bad: Very high budget</li>
      <li>Good: Executive Management, User Involvement, Experienced Project Manager, Clear Business Objectives, Minimizing Scope, Requirements Process, Standard Software Infrastructure, Formal Methology, Reliable Estimates, Skilled Staff</li>
      <li>&bdquo;When projects fail, it's rarely technical.&ldquo;</li>
    </ul>
  </li>
  <li>Outsource, Find&Buy, Develop new solution</li>
</ul>

<strong>Teams:</strong>
<ul>
  <li>< 6 Entwickler</li>
  <li>< 6 Monate</li>
  <li><abbr title="Release early, release often">RERO</abbr></li>
  <li>Verantwortungsbereiche:
    <ul>
      <li>Product Management: Wie verkaufe ich die Software?</li>
      <li>Program Management: Wie bringe ich das Projekt zu einem erfolgreichem Abschluss?</li>
      <li>Architekture: Wie halte ich die Software erweiterbar, anpassbar und wartbar?</li>
      <li>Development: Wie schreibe ich den Code von Methode abc in Klasse xyz?</li>
      <li>Test: Sind alle funktionalen und qualitativen Anforderungen erfüllt? Ist das System robust?</li>
      <li>User Experience: Passiert das, was der Nutzer erwartet? Kann man dem User die Bedienung der Software erleichtern?</li>
      <li>Release / Operations: Wie halte ich die Software über Jahre am laufen?</li>
    </ul>
  </li>
  <li>Aufsplitten der Teams nach Funktionen oder Features
    <ul>
      <li>Wo ist der Unterschied?</li>
    </ul>
  </li>
</ul>

<strong>Tasks & Tools</strong>
<ul>
  <li><a href="http://de.wikipedia.org/wiki/Work_Breakdown_Structure">Work Breakdown Structure</a></li>
  <li>GANTT chart</li>
  <li><a href="http://de.wikipedia.org/wiki/Program_Evaluation_and_Review_Technique">PERT</a></li>
  <li><a href="http://en.wikipedia.org/wiki/SWOT_analysis">SWOT Analysis</a></li>
</ul>

<strong>Risiken</strong>
<ul>
  <li>Cost-reduction expectations</li>
  <li>Data security / protection (IPR)</li>
  <li>Process discipline (Was ist das?)</li>
  <li>Loss of business knowledge</li>
  <li>Vendor failure to deliver</li>
  <li>Scope creep</li>
  <li>Government oversight / regulation</li>
  <li>Culture (language and callcenters)</li>
  <li>Turnover of key personnel</li>
  <li>Knowledge transfer</li>
</ul>

<strong>Process Models</strong>
<ul>
  <li><a href="http://en.wikipedia.org/wiki/Code_and_fix#Code_and_fix">Code and fix</a></li>
  <li>Waterfall model</li>
  <li>Prototyping model</li>
  <li>Evolutionary Development model: Only for small, scientific projects where project goal is unclear</li>
  <li>Spiral model: Risk-driven</li>
  <li><abbr title="Rational Unified Process model">RUP</abbr> von SAP</li>
  <li><abbr title="Microsoft Solution Framework">MSF</abbr> &rarr; <a href="http://msdn.microsoft.com/de-de/library/bb979125.aspx">msdn Artikel</a>
    <ul>
     <li>Rollen:
       <ul>
         <li>Product Management: Anwalt des Kunden, teamübergreifende Projekt-Vision, betriebswirtschaftliche Sicht auf das Projekt</li>
         <li>Program Management: &bdquo;Projektleiter&ldquo;, Teamkommunikation, technische Sicht auf das Projekt</li>
         <li>Architecture, Development, Testing, Release / Operations</li>
         <li>User Experience: Anwalt des Benutzers</li>
       </ul>
     </li>
     <li>Skalierung: Feature-Teams vs. Functional Teams</li>
     <li>Meilensteine: Extern sichtbare und Interim-Meilensteine</li>
    </ul>
  </li>
  <li>Reuse-Oriented Approaches</li>
  <li>Agile Methoden:
    <ul>
      <li>Scrum:
        <ul>
          <li>Rollen: Scrum Master, Product Owner, Development Team</li>
          <li>Iterations, Sprints, User Stories</li>
          <li><a href="http://if-blog.de/scrum-plakat">Scrum Plakat</a></li>
          <li><a href="//www.youtube.com/watch?v=r6brn76hDec">Video: What is Scrum?</a>, <a href="//www.youtube.com/watch?v=XU0llRltyFM#t=32s">Scrum in 8 minutes</a>, <a href="http://refcardz.dzone.com/refcardz/scrum">Scrum Refcard</a>, <a href="http://sendspace.com/pro/dl/qh5zug">Scrum Master Checklist</a></li>
        </ul>
      </li>
      <li><abbr title="Extreme Programming">XP</abbr>: Paarprogrammierung, <a href="//www.youtube.com/watch?v=XP4o0ArkP4s">Lecture 24: Richard Buckland</a> (45 minutes)</li>
      <li><a href="http://agilemanifesto.org/">Agile manifesto</a></li>
    </ul>
  </li>
</ul>

<h3>PART 3: Requirements Engineering</h3>
<ul>
  <li>Ablauf:
    <ol>
      <li>Initiate: Project Charter, Identify business opportunity, gather business requirements, <abbr title="target customer">FOR</abbr> WHO <abbr title="product name">THE</abbr> <abbr title="product category">IS</abbr> <abbr title="key benefit">THAT</abbr> <abbr title="primary competition">UNLIKE</abbr> <abbr title="primary difference">OUR PRODUCT</abbr></li>
      <li>Elicitation: Refine requirements (Busines requirements, functional requirements, non-functional requirements), Coopers Persona-Ansatz (<a href="http://de.wikipedia.org/wiki/Persona_(Mensch-Computer-Interaktion)#Beispiel">Beispiele</a>)</li>
      <li>Asses: Understand and organize requirements, features and feature sets</li>
      <li>Specification: <a href="http://en.wikipedia.org/wiki/Software_Requirements_Specification">Software requirements specification</a></li>
      <li>Validation</li>
    </ol>
  </li>
  <li>Gather requirements (Interviewing, <a href="http://en.wikipedia.org/wiki/Job_shadowing">Shadowing</a>, surveys, brainstorming, user instructions - z.B. bei Atomkraftwerken gibt es wohl schon Prozessabläufe)</li>
  <li><a href="http://dropsafe.crypticide.com/article/1006">A11Y, L10N, I18N, G11N</a>: <a href="http://de.wikipedia.org/wiki/BITV">BITV</a></li>
  <li>RNA: Relationship-Navigation Analysis</li>
  <li><a href="http://de.wikipedia.org/wiki/Web_Accessibility_Initiative">WAI</a></li>
</ul>

<h3>PART 4: Entwurf</h3>
Logischer Entwurf (Abstrakt: Wireframes, Navigation patterns) &harr; Physikalischer Entwurf (Konkret: UI Frameworks, Services)

<h4>Content Management Aspects</h4>
<ul>
  <li>Content-Typen müssen definiert werden, um Inhalte von der Darstellung trennen zu können</li>
  <li>Content-Typen sind auch für die Suche relevant</li>
  <li>Templates müssen erstellt werden</li>
  <li>Welche Metadaten liegen vor?</li>
  <li>Wie können Metadaten weitergegeben werden? &rarr; <a href="http://support.google.com/webmasters/bin/answer.py?hl=en&answer=99170">Rich Snippets</a></li>
  <li>Welche <abbr title="Denglisch: Workflows">Arbeitsabläufe</abbr> habe ich?</li>
  <li>Inhalt kann in flachen/strukturierten Dateien oder in Datenbanken liegen.</li>
  <li>Strukturierte Dateien: XML, RDF (&rarr; <a href="//www.youtube.com/watch?v=ldl0m-5zLz4">Video</a>), Microformats</li>
</ul>


<h4>Software Interface Aspects</h4>
<div class="definition"><em>Usability</em> is the extent to which a product can be used by specified users to achieve specified goals with effectiveness, efficiency and satisfaction in a specified context of use. - ISO 9241-11</div>
<div class="definition">User Experience is a person's perception and responses that result from the use or anticipated use of a product, system or service. - ISO 9241-210</div>

<ul>
  <li>User-centered design &rarr; <a href="http://en.wikipedia.org/wiki/User-centered_design">Wiki</a></li>
  <li>Mentale Modelle: Taschenrechner, Explorer, Start-Vorgang, Einkaufssysteme, Hyperlinks, Tastatur</li>
  <li>Metaphern</li>
  <li>User-Modelle: Rollen, Markt-Anteile, Personas</li>
</ul>

<h4>Hypertext Systm Aspects</h4>
<ul>
  <li>Known-item search / exploratory search</li>
</ul>

<h4>Business Process Aspects</h4>
Kommt noch

<h3>Weiteres</h3>
<ul>
  <li><a href="http://en.wikipedia.org/wiki/Web_Services_Description_Language">WSDL</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Microsoft_Solutions_Framework">MSF</a> vs. <a href="http://en.wikipedia.org/wiki/Scrum_(development)">Scrum</a> - <a href="http://pm.stackexchange.com/a/8493/5195">Roles in Scrum</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol">HTTP</a></li>
</ul>

<h3>Weitere Informationen</h3>
Folgende Artikel sollte man lesen:
<ul>
  <li><a href="http://de.wikipedia.org/wiki/Internet">Internet</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Geschichte_des_Internets">Geschichte des Internets</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Chronologie_des_Internets">Chronologie des Internets</a></li>
</ul>

Diese Tutorials sollte man machen:
<ul>
    <li><a href="http://www.w3schools.com/xml/xml_whatis.asp">XML Tutorial</a> - <a href="http://www.w3schools.com/quiztest/quiztest.asp?qtest=XML">XML Quiz</a></li>
    <li><a href="http://www.w3schools.com/xml/xml_soap.asp">SOAP Tutorial</a></li>
</ul>

<h2>Typische Fragen</h2>
<div class="question">
<span class="question">Was ist Web Engineering?</span>
<div class="answer">
<ul>
  <li>It's not science, and it isn't exactly engineering, either.</li>
  <li>Disziplin aus Disziplinen (Software Engineering, Hypermedia, Information Systems, Network Engineering)</li>
  <li>Teilweise ist es wie Software Engineering (Requirements engineering, reproduzierbare Erfolge durch strukturierte Herangehensweise), teilweise hat es typische Problemquellen, die im Software Engineering weniger verbreitet sind (Skalierbarkeit, Load balancing, Hypermedia).</li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Was ist eine Ressource?</span>
<div class="answer">Eine Ressource ist ein Objekt, dass von einem Webserver oder Websystem mittels eines standardisierten Protokolls ausgeliefert wird und durch einen MIME-Typen spezifiziert wird.</div>
</div>

<div class="question">
<span class="question">Wie werden Ressourcen adressiert?</span>
<div class="answer">Durch URIs, meist URLs aber auch URNs.</div>
</div>

<div class="question">
<span class="question">Was ist ein Webservice?</span>
<div class="answer">Ein Webservice ist eine Software-Anwendung, die mit einem URI eindeutig identifizierbar ist und deren Schnittstelle als XML-Artefakt definiert, beschrieben und gefunden werden kann. Diese Schnittstelle kann mit WSDL beschrieben werden.
</div>
</div>

<div class="question">
<span class="question">Was ist das Endpoint-ABC?</span>
<div class="answer">
Wurde durch die WCF geprägt und ist <a href="http://stackoverflow.com/q/8893128/562769">z.B. so in der Web.config</a>. Das ABC steht für ...
<ul>
  <li>Address (Wo ist der Endpoint?)</li>
  <li>Binding (Wie verbinde ich? Protokoll? Encoding?)</li>
  <li>Contract (Welche Informationen will ich übertragen?)</li>
</ul>
Siehe auch: <a href="http://fczaja.blogspot.de/2010/10/wcf-endpoint-abc.html">Filip's Technical Blog</a>
</div>
</div>

<div class="question">
<span class="question">Welche Ziele verfolgt das W3C?</span>
<div class="answer">
<ul>
  <li>Web for Everyone</li>
  <li>Web on Everything</li>
  <li>Knowledge Base</li>
  <li>Trust and Confidence</li>
</ul>
</div>
</div>

<div class="question">
<span class="question">Wie ist der Arbeitsprozess beim W3C?</span>
<div class="answer">
Workshops &rarr; Notes from members &rarr; Briefing package with membership vote &rarr; Requirements Document &rarr; Working Draft &rarr; Candidate Recommendation &rarr; Proposed Recommendation &rarr; W3C Recommendation (<a href="http://en.wikipedia.org/wiki/W3C_recommendation">source</a>)
</div>
</div>

<h2>Interessante Fragen</h2>
<div class="question">
<span class="question">Vergleichen Sie RPCs und Web Services</span>
<div class="answer">
<ul>
  <li>Web Services sind leichter skalierbar.</li>
</ul>

(Siehe auch: <a href="http://stackoverflow.com/a/1350982/562769">StackOverflow</a>)
</div>
</div>

<div class="question">
<span class="question">Wie läuft ein HTTP-Request ab?</span>
<div class="answer">Siehe <a href="http://www.tecchannel.de/netzwerk/management/401210/hypertext_transfer_protocol/index2.html">TechChannel.de</a>
</div>
</div>


<h2>Hintergrundwissen</h2>
<a href="http://igoro.com/archive/what-really-happens-when-you-navigate-to-a-url/">What really happens when you navigate to a URL</a>
<ul>
  <li><a href="http://stackoverflow.com/a/11021207/562769">OS-DNS-Cache on Linux</a></li>
  <li><a href="http://superuser.com/a/31691/64857">What exactly happens when you browse a website in your browser?</a> (fun to read)</li>
  <li><a href="http://stackoverflow.com/a/2092602/562769">What happens when you type in a URL in browser?</a> (well structured)</li>
</ul>

<h2>Termine</h2>
Web Engineering wird mündlich geprüft. Dazu muss man sich bei Herrn Matthias Keller (matthias.keller@kit.edu) melden und einen Termin ausmachen. Zusätzlich muss man sich über QISPOS anmelden.

<strong>Datum</strong>: Dienstag, der 19. Februar 2013 um 14:30 Uhr (individuell, siehe Organisation)<br/>
<strong>Ort</strong>: Geb. 20.21 (SCC), Raum 303 (individuell, siehe Organisation)<br/>
<strong>Dauer</strong>: 15 Minuten<br/>
<strong>Punkte</strong>: 4 ECTS
