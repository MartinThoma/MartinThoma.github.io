---
layout: post
title: Improvements for my University's Website
author: Martin Thoma
date: 2011-10-22 20:55:05.000000000 +02:00
categories:
- The Web
tags:
- Web Development
- KIT
featured_image: 2011/10/KIT-Logo.png
---
I am now studying at the <a href="http://en.wikipedia.org/wiki/Karlsruhe_Institute_of_Technology">Karlsruhe Institute of Technology</a> (KIT). Although I think that the Websites of KIT is much better than the Website of most Universities,  I can imagine several possibilities how the online services could be improved:

<h2>Use OpenID</h2>
I have 9 different accounts with 7 different passwords for university. After my first week.

I guess it is impossible to use the same login system for all services of the university as we have many different teams of developers. But it is easily possible to get an OpenID provider. The students could have an URL like student.kit.edu/openid/u.... or something similar. The login would always happen at one place and this server could tell the other services that the right user is trying to get access. 

Some more information about OpenID is here:
<ul>
  <li><a href="http://en.wikipedia.org/wiki/OpenID">Wikipedia</a> (the <a href="http://de.wikipedia.org/wiki/OpenID">German article</a> is much better)</li>
  <li><a href="http://www.youtube.com/watch?v=xcmY8Pk-qEk">OpenID According to Dave</a> (4:35 min)</li>
  <li><a href="http://www.youtube.com/watch?v=DslTkwON1Bk">The Implications of OpenID</a> (51:19 min)</li>
</ul>

<h2>Customization</h2>
It would help me a lot if I could customize my start page at studium.kit.edu by adding some links / text.

<h2>Consistency</h2>
The university was called "University of Karlsruhe" ("Universit&auml;t Karlsruhe" in German) a few years ago. Then they thought it was time to rename the university as they made major structural changes.

<h3>URLs - one Top-level domain</h3>
They also got a new URL. Before the new one is kit.edu, but it seems as if many pages were still on the old <abbr title="top-level domain">TLD</abbr>:
<ul>
  <li>uni-karlsruhe.de:
    <ul>
  <li><a href="http://www.fsmi.uni-karlsruhe.de/">fsmi.uni-karlsruhe.de</a>: fsmi.kit.edu</li>
  <li><a href="http://www2.mach.uni-karlsruhe.de/srmach/srmach.php">mach.uni-karlsruhe.de</a>: should be mach.kit.edu</li>
    </ul>
  <li>http://www.ira.uka.de/: <a href="https://webinscribe.ira.uka.de/">webinscribe.ira.uka.de</a>: should be webinscribe.kit.edu. Additionally, a link from studium.kit.edu to this service should be created.</li>
  <li><a href="http://www.itas.fzk.de/">www.itas.fzk.de</a>: should be itas.kit.edu. (I guess fzk means "Forschungszentrum Karlsruhe" - research center Karlsruhe)</li>
</ul>

This could be fixed with the following steps:
<ul>
    <li>Find old URLs / Links (e.g. with <bbr title="Regular Expressions">RegEx</abbr> and a <a href="http://en.wikipedia.org/wiki/Web_crawler">crawler</a>)</li>
    <li>Introduce the new URL by one of those two possibilites:
        <ul>
          <li>Make HTML-redirections for the new ones (e.g. from fsmi.kit.edu to www.fsmi.uni-karlsruhe.de)</li>
          <li>Move the content from the old space to the new space. Make sure that nothing breaks by adding a <a href="http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#3xx_Redirection">301 status code</a>.</li>
        </ul>
    <li>Replace all links to the old URL by the new URL.</li>
    <li>Wait at least one, rather two semester. Check which internal Websites still use the old URL and try to fix those links.</li>
    <li>Completely remove the old URL</li>
</ul>

<h3>Services in one place</h3>
KIT offers quite a lot of online services, such as
<ul>
  <li><a href="http://www.bibliothek.kit.edu/cms/index.php">Search for books</a> in KIT-library
  <li><a href="https://www.rz.uni-karlsruhe.de/cgi-bin/bvprint">bvprint</a>: How much money is left on my printing-account?</li>
  <li>Webmail:
    <ul>
      <li>u....@student.kit.edu / prename.lastname@student.kit.edu / u....@stud.uni-karlsruhe.de: <a href="https://owa.kit.edu">owa.kit.edu</a> - with Microsofts <a href="http://en.wikipedia.org/wiki/Outlook_Web_App">OWA</a></li>
      <li>s_...@atis.uka.de: <a href="https://webmail.ira.uni-karlsruhe.de/imp/login.php">webmail.ira.uni-karlsruhe.de</a> - with <a href="http://en.wikipedia.org/wiki/Horde_(software)">Horde Groupware</a></li>
    </ul>
  </li>
  <li><a href="http://www.scc.kit.edu/dienste/3203.php">Web-Server</a> with <a href="http://www.scc.kit.edu/dienste/7881.php">MySQL databases</a> and <a href="https://www.rz.uni-karlsruhe.de/phpmyadmin/?server=5">phpMyAdmin</a></li>
  <li><a href="http://www.scc.kit.edu/dienste/3203.php">New Sites</a>: Create a site for you</li>
</ul>

For some services you need to login via <a href="https://vpn.kit.edu/">https://vpn.kit.edu</a>:
<ul>
  <li>Print preview: <a href="https://scc-print.scc.kit.edu/cgi-bin/preview/index.cgi?printer=bw600dpi&user=">https://scc-print.scc.kit.edu</a> and the (buggy) <a href="https://scc-print-06.scc.kit.edu/cgi-bin/print/index.cgi">newer version</a>.</li>
  <li><a href="https://print.rz.uni-karlsruhe.de/cgi-bin/pu">PrintUtil</a>: Which jobs are in the queue of the printer?</li>
  <li>Scanning: <a href="http://studscan.ira.uka.de/">studscan.ira.uka.de</a></li>
</ul>

I had to search for some services, like a SVN-Repository (<a href="http://www.atis.uka.de/1422.php">How do I get a SVN repository at KIT?</a>)

The important services should be available at studium.kit.edu. I think this would be a link to the Webmail, to the printing services and webinscribe.

<h2>Help the user to find what he needs</h2>
<h3>Redundancy</h3>
Sometimes it is good to provide several alternatives. I have one example:
One of the most important URLs at my university's website is studium.kit.edu. In the first week, I typed quite often student.kit.edu. Google corrected kit to mit and the MIT has such a page. I think it would be a good idea to look at the 404-error log and check, if this occurs often. If it does, a redirect should probable be added.

All redundant URLs should point to ONE target, of course. It's best to use a 301 redirection.

<h3>Short, but meaningful URLs</h3>
At the moment KIT makes use of such URLs:
<ul>
  <li>www.kit.edu/index.php should be kit.edu</li>
  <li>www.informatik.kit.edu/index.php should be informatik.kit.edu</li>
  <li><a href="http://www.informatik.kit.edu/883.php">www.informatik.kit.edu/883.php</a> should be informatik.kit.edu/informatik-bachelor</li>
  <li>www.informatik.kit.edu/interact.php should be informatik.kit.edu/interact</li>
</ul>

This can be done by modifying the .htaccess-file (for the decision to redirect calls prefixed with www to a non-www page).

In many cases you can use the URL which I would prefer, but you're redirected to the other one. This means if a professor is copying the ugly link to his presentation, all students will have to write it down. 

<h3>Helpfull 404 Page</h3>
At the moment I get only: "404 NOT FOUND". This is not very helpful. You should provide a <a href="../custom-404-error-pages/" title="Custom 404 error pages">custom 404 error page</a>.

<h3>Use Feeds</h3>
I would like to get the latest news about KIT, but I don't want to search for it. I also don't want to look at the homepage of KIT to check if I know the latest content. This should be done with a RSS feed.

The start page should have an auto-detectable RSS-Feed. It can be added with the following HTML-Tag in the head-section of the document:
[html]<link rel="alternate" type="application/rss+xml" 
  title="KIT News Feed" 
  href="/rss/" />[/html]

<h2>Use HTML5 input tags</h2>
HTML5 input tags can much more than the old ones. You can define <a href="http://www.w3schools.com/html5/att_input_autofocus.asp">autofocus</a> for the first element, <a href="http://www.w3schools.com/html5/att_input_placeholder.asp">placeholders</a>, <a href="http://www.w3schools.com/html5/att_input_autocomplete.asp">autocomplete</a>=off for password fields at the registration, <a href="http://www.w3schools.com/html5/att_input_pattern.asp">patterns</a> for clients side validation and <a href="http://www.w3schools.com/html5/att_input_type.asp">much more types</a> than text and password. Old browsers automatically fall back into a simple text input field.

Examples for pages that could be improved:
<ul>
  <li><a href="http://kit.edu">kit.edu</a>: Add <a href="../search-engine-autodiscovery/" title="Search Engine Autodiscovery">search engine autodiscovery</a></li>
  <li><a href="http://i3vloan.ubka.uni-karlsruhe.de/19466917473783462330/i3v_library/ausleihe/i3v_ausleihe.cgi?opacdb=UBKA_OPAC&session=19466917473783462330&Funktion=Ersterfassung&lang=DE">Register library account</a></li>
  <li><a href="https://studium.kit.edu">studium.kit.edu</a></li>
  <li><a href="http://www.kit.edu/index.php">kit.edu</a> (the search box)</li>
  <li><a href="http://www.kit.edu/studieren/6243.php">kit.edu/studieren/6243.php</a> (the contact form at the bottom)</li>
  <li><a href="http://www.kit.edu/markt/userlogin.php">kit.edu/markt/userlogin</a> (the login form)</li>
</ul>

If somebody had much free time he could try to get valid HTML5 for the whole website. This isn't really helpful for the user (by now), but it would be nice to have a standard conform website.

<h2>Payments</h2>
You have to pay with the "KIT-Card" for meals in the cafeteria and if you want to print something. But you have to transfer the money to the printing account from your cafeteria account, before you can print anything. This seems to be not logical for me. Why do we have to use two university "bank" accounts?
