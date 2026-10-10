# Images TODO

Two groups of articles that need a decision about illustrations:

* **(a)** articles that use **stock photos** — generic filler that could be
  replaced with a real diagram or screenshot, or dropped;
* **(b)** articles with **no images and no code** — walls of text that might
  benefit from a diagram, screenshot, table or photo.

Remove an entry once it is dealt with. Regenerate the lists when articles are
added or images change.

## How the lists were built

* **Images** are `![…](…)` and `<img>` in the article body. `featured_image`
  does *not* count: it is only rendered as a 128×128 thumbnail with `alt=""`
  on the index page, never on the article itself, and 912 of 948 articles have
  one — almost always a generic `logos/*.png`. 1×1 tracking pixels (such as the
  PayPal pixel in `support-me`) and VG-Wort counting pixels are ignored.
* **Stock photo** means an image whose caption or alt text credits a stock
  library: Unsplash, Pexels, Pixabay, Freepik, Shutterstock, iStock, Getty,
  Depositphotos, StockSnap, Rawpixel, Kaboompics or Reshot. Articles that merely
  *mention* such a site are not listed — `make-a-webservice-2018` recommends
  stock sites as a resource and `sql-injections` mentions the Freepik breach.
* **Code** means a fenced ``` block or a `<pre>` block. Inline `` `code` ``
  spans and code inside HTML comments do not count (`e-autos` keeps a Python
  snippet in a comment to generate its table).
* **Words** counts prose only: front matter, code, HTML, math and link targets
  are stripped first.
* Every count was cross-checked against the rendered HTML in `output/`.

Totals: **0 articles** use stock photos (0 image files);
**279 of 948 articles** have neither an image nor code.

## (a) Articles with stock photos

**None left.** On 2026-09-22 all 48 stock photos were removed from the 26
Medium-era posts that carried them (2020-2021, all crediting Unsplash, Pexels
or Freepik).

In 20 of those articles the stock photo was decoration sitting beside diagrams
that already carried the content, so deleting it was the whole fix. The six
articles that would otherwise have been left with no illustration at all got
purpose-built SVG diagrams instead:

| Article | New figure | Shows |
| ------- | ---------- | ----- |
| [Client vs Customer](content/2020-09-16-client-vs-customer.md) | `2020/09/client-vs-customer.svg` | the two definitions side by side |
| [How Twitter's Image Choice is Biased](content/2020-09-25-twitter-image-choice-is-biased.md) | `2020/09/twitter-preview-crop.svg` | why a cropped preview leaves someone out |
| [Cross-site Scripting (XSS)](content/2020-10-16-xss.md) | `2020/10/xss-stored-cookie-theft.svg` | the four steps of a stored-XSS cookie theft |
| [The Cyber Security Triad](content/2020-12-11-cyber-security-triad-cia.md) | `2020/12/cia-triad.svg` | the CIA triangle |
| [Analyzing what I spend money on in 2020](content/2020-12-29-spent-money-2020.md) | `2020/12/spent-money-2020-top5.svg`<br>`2020/12/spent-money-2020-categories.svg`<br>`2020/12/spent-money-2020-amounts.svg` | the article's own numbers, as charts |
| [Credential Stuffing](content/2021-03-11-credential-stuffing.md) | `2021/03/credential-stuffing-flow.svg` | leaked credentials replayed across services |

The diagrams are hand-written SVG. Light-mode colours are plain presentation
attributes, so renderers that ignore CSS (feed readers, thumbnailers) still show
them correctly; a `prefers-color-scheme: dark` block supplies the dark palette.
Each is under 6 KB and carries a `<title>`, a `<desc>` and alt text.

## (b) Articles without images and without code

Longest first — the longer the article, the more a visual would help. "Other"
lists visual structure the article already has; `—` means plain running text.

### Over 1500 words (0)

**None left.**

### 700–1499 words (58)

| Date | Article | Words | Other |
| ---- | ------- | ----: | ----- |
| 2011-11-01 | [Wie führe ich einen Induktionsbeweis?](content/2011-11-01-wie-fuhre-ich-einen-induktionsbeweis.md) | 1492 | math |
| 2017-01-01 | [Korsika GR 20](content/2017-01-01-gr-20.md) | 1437 | table, video |
| 2014-12-02 | [The Impact of Strong AIs](content/2014-12-02-the-impact-of-strong-ais.md) | 1423 | video |
| 2014-05-10 | [Discussions with friends](content/2014-05-10-discussions-with-friends.md) | 1392 | — |
| 2016-11-17 | [Lectures on YouTube](content/2016-11-17-lectures-on-youtube.md) | 1359 | video |
| 2015-04-14 | [Echtzeitsysteme - Klausur](content/2015-04-14-echtzeitsysteme-klausur.md) | 1351 | table, math |
| 2012-10-17 | [Bürokratie am KIT](content/2012-10-17-burokratie-am-kit.md) | 1336 | — |
| 2018-12-30 | [German Politics](content/2018-12-30-german-politics.md) | 1329 | table |
| 2016-10-24 | [Machine Learning Glossary](content/2016-10-24-ml-glossary.md) | 1309 | math, video |
| 2014-09-10 | [One-on-One Tutoring](content/2014-09-10-one-to-one-tutoring.md) | 1294 | — |
| 2017-08-12 | [Ideen zur Verbesserung des KIT](content/2017-08-12-kit-thoughts.md) | 1239 | video |
| 2019-07-29 | [Working Remotely](content/2019-07-29-working-remotely.md) | 1212 | table |
| 2013-01-03 | [Web Engineering](content/2013-01-03-web-engineering.md) | 1192 | video |
| 2019-12-30 | [YouTube Playlist Cleanup 2019](content/2019-12-30-youtube-playlist-cleanup.md) | 1158 | table, video |
| 2017-07-26 | [Document Classification](content/2017-07-26-document-classification.md) | 1149 | math |
| 2016-12-15 | [Fake News: It's a symptom, not the problem](content/2016-12-15-fake-news.md) | 1136 | video |
| 2019-12-31 | [New Year 2020](content/2019-12-31-new-year-2020.md) | 1136 | table, video |
| 2012-11-08 | [Beweise aus der booleschen Algebra](content/2012-11-08-beweise-aus-der-booleschen-algebra.md) | 1135 | math |
| 2024-11-08 | [Hauswert bestimmen](content/2024-11-08-hauswert-bestimmen.md) | 1133 | table |
| 2023-08-12 | [Heizlastberechnung](content/2023-08-12-heizlastberechnung.md) | 1105 | video |
| 2017-02-06 | [State of the Art in ML](content/2017-02-06-sota.md) | 1089 | table, math, video |
| 2020-02-16 | [Matrix Multiplication: 2020 Update](content/2020-02-16-matrix-multiplication-update.md) | 1089 | table, video |
| 2012-08-08 | [Permutationen und Transpositionen](content/2012-08-08-permutationen-und-transpositionen.md) | 1086 | table, math |
| 2013-09-11 | [Bitcoin](content/2013-09-11-bitcoin.md) | 1073 | — |
| 2016-12-31 | [New Year 2017](content/2016-12-31-new-year-2017.md) | 1046 | video |
| 2024-08-18 | [Politik gegen Wohnungsmangel](content/2024-08-18-wohnungsmangel.md) | 1037 | — |
| 2013-06-16 | [Mathematische Strukturen](content/2013-06-16-mathematische-strukturen.md) | 1034 | — |
| 2012-08-07 | [Klausur Lineare Algebra I + II](content/2012-08-07-klausur-lineare-algebra-i-ii.md) | 1005 | math |
| 2020-05-17 | [Self-sustaining Space Colonies](content/2020-05-25-space-colonies.md) | 1000 | table, math |
| 2020-05-20 | [Python is interpreted](content/2020-05-20-python-is-interpreted.md) | 990 | video |
| 2012-01-08 | [Bachelor Informatik, 1. Semester: Was bisher geschah](content/2012-01-08-bachelor-informatik-1-semester-was-bisher-geschah.md) | 975 | — |
| 2012-02-17 | [Kellerautomat](content/2012-02-17-kellerautomat.md) | 972 | math |
| 2017-05-07 | [Amazons Power](content/2017-05-07-amazons-power.md) | 955 | — |
| 2023-03-31 | [Solaranlagen](content/2023-03-31-solarzellen.md) | 953 | video |
| 2015-11-26 | [OpenBCI](content/2015-11-26-openbci.md) | 950 | video |
| 2018-08-04 | [Education platform](content/2018-08-04-education-platform.md) | 934 | table, video |
| 2019-11-17 | [How to Give Good Presentations](content/2019-11-23-presentations.md) | 926 | video |
| 2020-12-04 | [Software Composition Analysis (SCA)](content/2020-12-04-sca.md) | 926 | — |
| 2022-03-23 | [Politische Forderungen](content/2022-03-23-politische-forderungen.md) | 924 | — |
| 2012-03-02 | [Definitionen aus GBI](content/2012-03-02-definitionen-aus-gbi.md) | 917 | — |
| 2013-07-23 | [Why everybody should know about conditional probability](content/2013-07-23-why-everybody-should-know-about-conditional-probability.md) | 913 | table, math |
| 2019-12-18 | [Financial Planning](content/2019-12-19-financial-planning.md) | 900 | table, math |
| 2024-12-26 | [Was mir Hoffnung macht](content/2024-12-26-was-mir-hoffnung-macht.md) | 892 | video |
| 2013-01-11 | [Adressierung](content/2013-01-11-adressierung.md) | 881 | — |
| 2023-11-21 | [Game Consoles](content/2023-11-21-game-consoles.md) | 872 | table, video |
| 2019-02-17 | [Monitors](content/2019-02-17-monitors.md) | 863 | table, video |
| 2012-03-26 | [Eigenschaften von Abbildungsmatrizen](content/2012-03-26-eigenschaften-von-abbildungsmatrizen.md) | 835 | math |
| 2012-08-08 | [Endliche Gruppen](content/2012-08-08-endliche-gruppen.md) | 805 | table |
| 2018-11-19 | [Down Jackets](content/2018-11-19-down-jackets.md) | 794 | table, video |
| 2018-12-25 | [Code Challenges in ML](content/2018-12-25-code-challenges-in-ml.md) | 791 | — |
| 2012-02-11 | [Konstruktion der Chomsky-Normalform](content/2012-02-11-konstruktion-der-chomsky-normalform.md) | 790 | — |
| 2016-03-07 | [The cost of fighting Terrorism with Bombs, Surveillance and Fear](content/2016-03-07-cost-of-fighting-terrorism.md) | 786 | — |
| 2018-12-31 | [New Year 2019](content/2018-12-31-new-year-2019.md) | 784 | video |
| 2012-10-07 | [PSE am KIT](content/2012-10-07-pse-am-kit.md) | 783 | table |
| 2017-08-25 | [Backpacking Tours by Month](content/2017-08-25-hiking-by-month.md) | 749 | — |
| 2017-12-31 | [New Year 2018](content/2017-12-31-new-year-2018.md) | 743 | table, video |
| 2023-03-11 | [Eisspeicher](content/2023-03-11-eisspeicher.md) | 733 | math |
| 2016-05-18 | [Lokalisierung Mobiler Agenten](content/2016-05-18-lma.md) | 705 | table, math, video |

### 300–699 words (99)

| Date | Article | Words | Other |
| ---- | ------- | ----: | ----- |
| 2019-02-16 | [Web Frameworks](content/2019-12-31-web-frameworks.md) | 674 | table, video |
| 2013-07-06 | [Improve German Public Transportation](content/2013-07-06-improve-german-public-transportation.md) | 658 | video |
| 2012-11-27 | [Karlsruhe: Oberbürgermeisterwahl 2012](content/2012-11-27-karlsruhe-oberburgermeisterwahl-2012.md) | 654 | table |
| 2024-12-07 | [Textilien](content/2024-12-07-textilien.md) | 642 | table |
| 2023-09-15 | [Earth to Moon](content/2023-09-15-earth-moon.md) | 639 | math |
| 2013-04-28 | [Semantische Sicherheit](content/2013-04-28-semantische-sicherheit.md) | 637 | — |
| 2019-12-31 | [Make a Webservice](content/2019-12-31-make-a-webservice-2018.md) | 635 | table, video |
| 2014-12-29 | [Replicators](content/2014-12-29-replicators.md) | 618 | — |
| 2013-08-27 | [How many Homomorphisms exist between Z/nZ and Z/mZ?](content/2013-08-27-how-many-homomorphisms-exist-between-znz-and-zmz.md) | 614 | table, math |
| 2014-12-29 | [Chatbots](content/2014-12-29-chatbots.md) | 610 | table |
| 2020-12-29 | [365 Main Dishes](content/2020-12-29-365-main-dishes.md) | 607 | — |
| 2016-02-20 | [Wasserrohrbruch in Karlsruhe](content/2016-02-20-wasserrohrbruch-karlsruhe.md) | 602 | — |
| 2011-10-29 | [Prädikatenlogik: Aussagen formalisieren](content/2011-10-29-pradikatenlogik-aussagen-formalisieren.md) | 594 | — |
| 2019-07-09 | [Roles in Software Development](content/2019-12-31-roles-in-software-development.md) | 591 | — |
| 2012-04-04 | [Wie berechne ich das multiplikativ Inverse einer komplexen Zahl?](content/2012-04-04-wie-berechne-ich-das-multiplikativ-inverse-einer-komplexen-zahl.md) | 587 | — |
| 2014-06-22 | [Awesome Robots](content/2014-06-22-awesome-robots.md) | 585 | video |
| 2013-09-09 | [Calculations with quaternions](content/2013-09-09-calculations-with-quaternions.md) | 580 | math |
| 2022-01-02 | [Nebenkosten](content/2022-01-02-nebenkosten.md) | 572 | video |
| 2024-12-22 | [Zeitdilatation](content/2024-12-22-zeitdilatation.md) | 569 | math |
| 2014-12-29 | [Scherzfragen](content/2014-12-29-scherzfragen.md) | 568 | — |
| 2011-10-18 | [Analysis I - Teil 1](content/2011-10-18-analysis-i-teil-1.md) | 566 | math |
| 2016-07-06 | [Optimization Basics](content/2016-07-06-optimization-basics.md) | 560 | table, math |
| 2018-12-30 | [Ways to store Data](content/2018-12-30-ways-to-store-data.md) | 551 | table, video |
| 2014-09-28 | [3D Printing](content/2014-09-28-3d-printing.md) | 546 | video |
| 2019-02-03 | [House Building](content/2020-03-26-house-building.md) | 530 | table, video |
| 2023-03-30 | [Wirtschaftlichkeit von effizienten Haushaltsgeräten](content/2023-03-30-wirtschaftlichkeit-effizienter-haushaltsgeraete.md) | 524 | table |
| 2012-08-26 | [Konvergenz von Folgen](content/2012-08-26-konvergenz-von-folgen.md) | 513 | math |
| 2012-11-26 | [Linux Scheduler](content/2012-11-26-linux-scheduler.md) | 513 | video |
| 2023-12-05 | [Innenputz](content/2023-12-05-innenputz.md) | 506 | table |
| 2011-10-24 | [Einführung in die abzählende Kombinatorik](content/2011-10-24-einfuhrung-in-die-abzahlende-kombinatorik.md) | 498 | table |
| 2014-12-26 | [How mathematics could change our future](content/2014-12-26-how-mathematics-could-change-our-future.md) | 493 | — |
| 2017-06-15 | [How to get Data for ML systems](content/2017-06-15-ml-get-data.md) | 491 | — |
| 2018-12-22 | [Sleeping Bags](content/2018-12-22-sleeping-bags.md) | 491 | table |
| 2018-07-18 | [Regression](content/2018-07-18-regression.md) | 490 | table, math |
| 2020-09-27 | [Safe vs Secure](content/2020-09-27-safe-vs-secure.md) | 486 | table |
| 2012-08-14 | [Klausur Analysis I und II](content/2012-08-14-klausur-analysis-i-und-ii.md) | 485 | — |
| 2015-04-13 | [Markovsche Ketten - Klausur](content/2015-04-13-markovketten-klausur.md) | 485 | table, math |
| 2024-03-03 | [Reichtum in Deutschland](content/2024-03-03-reichtum-in-deutschland.md) | 485 | — |
| 2014-12-30 | [Trickreiche Matheaufgaben](content/2014-12-30-trickreiche-matheaufgaben.md) | 481 | math |
| 2015-01-23 | [GUI programming with Python](content/2015-01-23-gui-programming-with-python.md) | 472 | table |
| 2016-06-11 | [US problems](content/2016-06-11-us-problems.md) | 471 | video |
| 2017-03-03 | [Umzug](content/2017-03-02-umzug.md) | 471 | table |
| 2016-12-30 | [Alpspitze via ferrata](content/2016-12-30-alpspitze.md) | 469 | video |
| 2020-06-21 | [Working Hours](content/2020-06-21-working-hours.md) | 455 | math |
| 2020-02-23 | [Computer Science](content/2020-05-23-computer-science.md) | 454 | table, video |
| 2018-12-03 | [Fleece](content/2018-12-03-fleece.md) | 432 | table |
| 2023-08-13 | [Betriebskosten: Wärmepumpe vs Ölheizung](content/2023-08-13-betriebskosten-waermepumpe-vs-oel.md) | 432 | — |
| 2013-01-17 | [Wie wende ich die Shannon-Zerlegung an?](content/2013-01-17-wie-wende-ich-die-shannon-zerlegung-an.md) | 431 | math |
| 2017-01-11 | [Paper List](content/2017-01-11-paper-list.md) | 431 | — |
| 2017-02-13 | [Best of ML](content/2017-02-13-best-of-ml.md) | 431 | video |
| 2023-12-30 | [Alternativen für die alte Ölheizung](content/2023-12-30-oelheizung-alternativen.md) | 425 | video |
| 2013-04-19 | [Numerik-Klausur](content/2013-04-19-numerik-klausur.md) | 424 | table, video |
| 2014-11-22 | [Universal Rating System](content/2014-11-22-universal-rating-system.md) | 423 | — |
| 2012-06-10 | [Warum kann der Mond keine Atmosphäre haben?](content/2012-06-10-warum-kann-der-mond-keine-atmosphare-haben.md) | 401 | — |
| 2012-11-07 | [Definitionen aus Digitaltechnik](content/2012-11-07-definitionen-aus-digitaltechnik.md) | 399 | table |
| 2019-09-01 | [Selling Stuff](content/2019-12-31-selling-stuff.md) | 399 | table |
| 2024-03-24 | [Rasenmäher](content/2024-03-24-rasenmaeher.md) | 399 | table |
| 2016-06-17 | [Thoughts about Language](content/2016-06-17-thoughts-about-language.md) | 398 | — |
| 2017-09-06 | [Git Repository Managers](content/2017-09-06-git-repository-managers.md) | 398 | table |
| 2011-11-10 | [Eine Sprache ist nicht regulär - Beweis mit dem Pumping-Lemma](content/2011-11-10-pumping-lemma.md) | 390 | — |
| 2023-10-25 | [Rasenmähroboter](content/2023-10-25-rasenmaehroboter.md) | 390 | video |
| 2016-12-29 | [Reinforcement Learning](content/2016-12-29-reinforcement-learning.md) | 385 | math |
| 2016-03-16 | [Support Me](content/2016-03-16-support-me.md) | 383 | table |
| 2018-06-22 | [Software Handover](content/2018-06-22-software-handover.md) | 382 | — |
| 2012-12-19 | [When advertising becomes spam](content/2012-12-19-when-advertising-becomes-spam.md) | 377 | — |
| 2021-05-31 | [Database Read Phenomena](content/2021-10-10-concurrency-read-phenomena.md) | 377 | table |
| 2011-10-23 | [Wie führe ich einen sauberen Beweis?](content/2011-10-23-wie-fuhre-ich-einen-sauberen-beweis.md) | 375 | math |
| 2012-04-16 | [Eigenwerte, Eigenvektoren und Eigenräume](content/2012-04-16-eigenwerte-eigenvektoren-und-eigenraume.md) | 373 | — |
| 2017-02-25 | [ML Review 3](content/2017-02-25-ml-review-3.md) | 367 | video |
| 2023-09-21 | [Politische Dimensionen](content/2023-09-21-politische-dimensionen.md) | 367 | — |
| 2012-01-08 | [Wie bildet man den Schnitt zweier Vektorräume?](content/2012-01-08-wie-bildet-man-den-schnitt-zweier-vektorraume.md) | 366 | math |
| 2020-02-12 | [Current Python Versions](content/2020-02-12-current-python-versions.md) | 361 | table |
| 2018-02-17 | [Online Banking](content/2018-02-17-online-banking.md) | 354 | table, video |
| 2011-09-28 | [Shortfilms](content/2011-09-28-shortfilms.md) | 351 | video |
| 2018-12-23 | [WhatsApp Data](content/2018-12-23-whatsapp-data.md) | 348 | table |
| 2024-11-07 | [Action Cams](content/2024-11-07-action-cams.md) | 348 | video |
| 2019-01-25 | [Insoles](content/2019-01-25-insoles.md) | 346 | table, video |
| 2013-04-23 | [E.i.d. Algebra und Zahlentheorie-Klausur](content/2013-04-23-eaz-klausur.md) | 345 | table |
| 2012-10-19 | [Review des Acer Travelmate 5744Z](content/2012-10-19-review-des-acer-travelmate-5744z.md) | 343 | — |
| 2017-01-07 | [This Blog - Technical Stuff](content/2017-01-07-this-blog.md) | 340 | table |
| 2012-07-14 | [When Is Matrix Multiplication Commutative?](content/2012-07-14-when-is-matrix-multiplication-commutative.md) | 337 | math |
| 2012-12-22 | [Wie wendet man den Transformationssatz an?](content/2012-12-22-wie-wendet-man-den-transformationssatz-an.md) | 329 | math |
| 2018-12-30 | [Expert Systems](content/2018-12-30-expert-systems.md) | 327 | video |
| 2018-06-14 | [Data Scientist Interviews](content/2018-06-11-data-scientist-interview.md) | 326 | — |
| 2018-12-18 | [Trekking Trousers](content/2018-12-18-trekking-trousers.md) | 325 | table, video |
| 2011-12-10 | [OpenID autodiscovery](content/2011-12-10-openid-autodiscovery.md) | 317 | — |
| 2017-08-07 | [Data Serialization](content/2017-08-07-data-serialization.md) | 314 | table |
| 2018-12-30 | [Why do we use references?](content/2018-12-30-why-references.md) | 313 | — |
| 2015-05-19 | [Getting a Feeling for Energy](content/2015-05-19-get-a-feeling-for-energy.md) | 311 | math |
| 2017-03-14 | [curl vs wget](content/2017-03-14-curl-vs-wget.md) | 311 | table |
| 2020-01-05 | [36C3](content/2020-01-05-36c3.md) | 310 | video |
| 2013-04-09 | [Colors in Vim](content/2013-04-09-colors-in-vim.md) | 309 | table |
| 2024-01-07 | [Heizungsvergleich](content/2024-01-07-heizungsvergleich.md) | 308 | table, math, video |
| 2017-08-31 | [ML Review 6](content/2017-08-05-ml-review-6.md) | 307 | video |
| 2012-09-20 | [Aufgaben zur Integralrechnung](content/2012-09-20-aufgaben-zur-integralrechnung.md) | 306 | math |
| 2012-07-26 | [Die Landau-Symbole](content/2012-07-26-die-landau-symbole.md) | 305 | math |
| 2013-08-25 | [Why is the intersection of two normal subgroups a normal subgroup?](content/2013-08-25-intersection-two-normal-subgroups-normal-subgroup.md) | 305 | — |
| 2017-02-21 | [The p value](content/2017-02-21-p-value.md) | 305 | math, video |
| 2019-12-28 | [Software Stacks](content/2019-12-28-software-stacks.md) | 303 | — |

### Under 300 words (122)

Mostly link collections, short notes and announcements. Listed for completeness;
most of these probably do not need an image.

* 2023-04-20 — [Printers](content/2023-04-20-printers.md) (298 words, table)
* 2017-01-02 — [MP3 Player](content/2017-01-02-mp3-player.md) (297 words, —)
* 2018-12-17 — [How to get foreign currencies](content/2018-12-17-foreign-money.md) (296 words, table)
* 2019-12-22 — [Semmelknödel](content/2019-12-22-semmelknoedel.md) (294 words, —)
* 2018-12-30 — [File Sizes](content/2018-12-30-file-sizes.md) (288 words, table)
* 2020-10-02 — [Identification vs Authentication vs Authorization](content/2020-10-02-identification-vs-authentication-vs-authorization.md) (287 words, —)
* 2012-01-28 — [Sprachen, Automaten und Grammatiken: Ein Überblick](content/2012-01-28-sprachen-automaten-und-grammatiken.md) (286 words, table, math)
* 2016-02-10 — [Collaborative Filtering](content/2016-02-10-collaborative-filtering.md) (286 words, video)
* 2013-07-23 — [Kollisionsresistente Hashfunktionen und Einwegfunktionen](content/2013-07-23-kollisionsresistente-hashfunktionen-und-einwegfunktionen.md) (285 words, —)
* 2017-08-30 — [Scrum](content/2017-08-30-scrum.md) (280 words, video)
* 2020-09-27 — [Localization vs Internationalization](content/2020-09-26-localization-vs-internationalization.md) (280 words, video)
* 2012-04-21 — [Wie berechnet man das charakteristische Polynom?](content/2012-04-21-wie-berechnet-man-das-charakteristische-polynom.md) (279 words, math)
* 2012-08-12 — [Ist die Funktion / Relation wohldefiniert?](content/2012-08-12-ist-die-funktion-relation-wohldefiniert.md) (275 words, —)
* 2024-08-31 — [DIY Bench](content/2024-08-31-diy-bench.md) (274 words, —)
* 2024-05-20 — [Pfannen](content/2024-05-20-pfannen.md) (265 words, table)
* 2012-07-04 — [Mathe Puzzle #1: Verschleierung](content/2012-07-04-mathe-puzzle-1-verschleierung.md) (263 words, video)
* 2018-03-21 — [Comparing Cameras](content/2018-03-21-comparing-cameras.md) (259 words, —)
* 2019-12-18 — [Chicken Fried Rice](content/2019-12-18-chicken-fried-rice.md) (257 words, —)
* 2019-01-17 — [Authentication vs Authorization](content/2020-04-13-authentication.md) (257 words, —)
* 2020-01-19 — [Werewolf Winning Probabilities](content/2020-03-28-werewolf.md) (255 words, math)
* 2012-09-21 — [Crash Course: World History](content/2012-09-21-crash-course-world-history.md) (251 words, video)
* 2019-01-25 — [Water Bottles](content/2019-01-26-water-bottles.md) (249 words, table, video)
* 2012-10-21 — [Programmieren Tutorium](content/2012-10-21-programmieren-tutorium.md) (242 words, video)
* 2018-05-17 — [Python Packages](content/2018-05-17-python-packages.md) (242 words, —)
* 2019-12-24 — [Carrot Soup](content/2019-12-24-carrot-soup.md) (242 words, —)
* 2012-09-16 — [Integration durch Substitution](content/2012-09-16-integration-durch-substitution.md) (238 words, math)
* 2012-06-01 — [How many IPv6 adresses exist?](content/2012-06-01-how-many-ipv6-adresses-exist.md) (236 words, video)
* 2019-12-24 — [Cantuccini](content/2019-12-24-cantuccini.md) (230 words, —)
* 2014-03-25 — [Project Gooseberry](content/2014-03-25-project-glooseberry.md) (222 words, video)
* 2018-12-30 — [Techniques for Analyzing ML models](content/2018-12-30-model-analysis.md) (222 words, —)
* 2012-08-16 — [Wie bestimme ich den Kern einer linearen Abbildung?](content/2012-08-16-wie-bestimme-ich-den-kern-einer-linearen-abbildung.md) (221 words, math)
* 2016-03-13 — [Voting](content/2016-03-13-voting.md) (220 words, —)
* 2023-11-01 — [Resolutions](content/2023-11-01-resolution.md) (214 words, table)
* 2023-03-12 — [Weißbrot](content/2023-03-12-weissbrot.md) (211 words, table)
* 2014-01-28 — [GeoTopo Klausur](content/2014-01-28-geotopo.md) (210 words, —)
* 2012-09-15 — [Konvergenz von Reihen](content/2012-09-15-konvergenz-von-reihen.md) (208 words, —)
* 2019-04-30 — [Schlagsahne vs Saure Sahne](content/2019-04-30-schlagsahne-saure-sahne.md) (205 words, —)
* 2019-05-01 — [Metrics](content/2020-05-01-metrics.md) (204 words, math)
* 2017-02-20 — [The Absolute Value Function](content/2017-02-20-abs-function.md) (200 words, math)
* 2017-09-24 — [Online Tools](content/2017-09-24-online-tools.md) (200 words, —)
* 2018-04-30 — [IKEA PAX](content/2018-04-30-ikea-pax.md) (196 words, —)
* 2023-08-06 — [Kühlmittel](content/2023-08-06-kuehlmittel.md) (193 words, table)
* 2012-07-15 — [Übersicht über Sortieralgorithmen](content/2012-07-15-ubersicht-uber-sortieralgorithmen.md) (192 words, table, video)
* 2012-08-14 — [Mathe-Aufgabe: Blutspende](content/2012-08-14-mathe-aufgabe-blutspende.md) (189 words, math)
* 2013-09-04 — [Gauß'sche Zahlen und verwandte Ringe](content/2013-09-04-gaussche-zahlen-und-verwandte-ringe.md) (189 words, —)
* 2014-12-07 — [Play Audio](content/2014-12-07-play-audio.md) (189 words, —)
* 2018-12-30 — [Trekking Poles](content/2018-12-30-trekking-poles.md) (188 words, table, video)
* 2013-08-26 — [Why is the stabilizer subgroup a subgroup?](content/2013-08-26-stabilizer-subgroup-subgroup.md) (186 words, —)
* 2016-11-19 — [Why Trump might be Good](content/2016-11-19-why-trump-might-be-good.md) (186 words, video)
* 2023-12-31 — [Brauchwasser-Wärmepumpe](content/2023-12-31-brauchwasser-waermepumpe.md) (186 words, —)
* 2017-06-26 — [Mindelheimer Klettersteig](content/2017-06-26-mindelheimer-klettersteig.md) (184 words, —)
* 2012-12-31 — [Unreal Tournament 2004](content/2012-12-31-unreal-tournament-2004.md) (180 words, —)
* 2019-01-02 — [Customer Segmentation](content/2020-07-02-customer-segmentation.md) (179 words, —)
* 2023-12-31 — [Beton](content/2023-12-31-beton.md) (179 words, video)
* 2019-08-04 — [APIs](content/2020-01-24-apis.md) (176 words, —)
* 2011-09-24 — [Using Wikipedia as a Newssstream](content/2011-09-24-using-wikipedia-as-a-newssstream.md) (175 words, —)
* 2017-08-08 — [The JavaScript World](content/2017-08-08-js-world.md) (175 words, —)
* 2023-05-06 — [Innenwände streichen](content/2023-05-06-innenwaende-streichen.md) (170 words, video)
* 2023-08-15 — [Betriebskosten einer Holz-Heizung](content/2023-08-15-holz-heizung.md) (170 words, table)
* 2019-08-30 — [Sandwich](content/2019-08-30-sandwich.md) (168 words, —)
* 2016-07-21 — [Diverging Gradient Descent](content/2016-07-21-gradient-descent-diverging.md) (167 words, math)
* 2014-08-20 — [GPUs - Supercomputers for your home](content/2014-08-20-gpu-supercomputers-for-your-home.md) (166 words, video)
* 2012-01-07 — [Frauenquote am KIT](content/2012-01-07-frauenquote-am-kit.md) (165 words, —)
* 2020-06-16 — [House Demolition](content/2020-06-16-house-demolition.md) (164 words, table, video)
* 2018-12-30 — [Academic Writing](content/2018-12-30-academic-writing.md) (162 words, —)
* 2019-12-20 — [Flask Chat - Part II](content/2020-03-29-flask-chat-2.md) (162 words, —)
* 2011-10-19 — [Community Chess](content/2011-10-19-community-chess.md) (159 words, —)
* 2020-11-14 — [E-book Readers](content/2020-11-14-ebook-readers.md) (159 words, table)
* 2014-12-11 — [Shortfilms, Part III](content/2014-12-11-shortfilms-part-iii.md) (153 words, video)
* 2012-12-05 — [Wie zeige ich Differenzierbarkeit?](content/2012-12-05-wie-zeige-ich-differenzierbarkeit.md) (151 words, —)
* 2011-09-21 — [Polyglots - Crazy Programming Stuff](content/2011-09-21-polyglots-crazy-programming-stuff.md) (146 words, —)
* 2013-09-11 — [How do I calculate a Histogram equalization?](content/2013-09-11-calculate-histogram-equalization.md) (145 words, —)
* 2011-09-23 — [Data Visualization](content/2011-09-23-data-visualization.md) (144 words, —)
* 2015-11-02 — [Wo ist Hörsaal 9 am KIT?](content/2015-11-02-wo-ist-hs9.md) (140 words, —)
* 2018-09-30 — [Abandoned domains are a security issue](content/2023-09-30-abandoned-domains.md) (136 words, —)
* 2012-03-16 — [Wie bestimme ich die Basiswechselmatrix?](content/2012-03-16-wie-bestimme-ich-die-basiswechselmatrix.md) (134 words, math)
* 2024-08-12 — [Food Processors](content/2024-08-12-food-processor.md) (133 words, —)
* 2011-09-30 — [If Computer Problems Were Real](content/2011-09-30-if-computer-problems-were-real.md) (130 words, video)
* 2012-03-20 — [Wie bestimme ich das Inverse einer Matrix?](content/2012-03-20-wie-bestimme-ich-das-inverse-einer-matrix.md) (127 words, math)
* 2012-09-15 — [Partielle Integration](content/2012-09-15-partielle-integration.md) (127 words, math)
* 2011-09-21 — [Freaky Wikipedia Articles](content/2011-09-21-freaky-wikipedia-articles.md) (126 words, —)
* 2014-10-26 — [Gradient Descent, the Delta Rule and Backpropagation](content/2014-10-26-gradient-descent-delta-rule-backpropagation.md) (118 words, —)
* 2020-05-09 — [XForms](content/2020-06-09-xforms.md) (118 words, video)
* 2020-05-14 — [Naming Styles](content/2020-05-14-naming-schemes.md) (117 words, table)
* 2014-12-30 — [Hörspiele](content/2014-12-30-horspiele.md) (104 words, video)
* 2012-02-07 — [Wahrscheinlichkeitstheorie - Klausur (Info)](content/2012-02-07-wt-klausur.md) (100 words, —)
* 2023-12-31 — [Haus-Projekte](content/2023-12-31-haus-projekte.md) (100 words, video)
* 2012-04-15 — [Lernkontrolle: Lineare Algebra I](content/2012-04-15-lernkontrolle-lineare-algebra-i.md) (99 words, —)
* 2024-08-16 — [Stein](content/2024-08-16-stein.md) (99 words, table)
* 2024-12-29 — [Stromzähler](content/2024-12-29-stromzaehler.md) (92 words, —)
* 2012-10-15 — [Learning Java](content/2012-10-15-learning-java.md) (88 words, video)
* 2012-04-26 — [LaTeX-Vorlage für ein Lastenheft](content/2012-04-26-latex-vorlage-fur-ein-lastenheft.md) (85 words, —)
* 2011-09-21 — [Animator vs. Animation](content/2011-09-21-animater-vs-animation.md) (75 words, video)
* 2019-01-11 — [Airlines](content/2019-01-11-airlines.md) (72 words, table)
* 2011-09-28 — [10 Great Videos on Vimeo](content/2011-09-28-10-great-videos-on-vimeo.md) (71 words, video)
* 2013-03-06 — [Add a new font to ImageMagick](content/2013-03-06-add-a-new-font-to-imagemagick.md) (71 words, —)
* 2017-04-28 — [Master Thesis](content/2017-04-09-msthesis.md) (70 words, —)
* 2013-06-30 — [Music videos](content/2013-06-30-music-videos.md) (69 words, video)
* 2019-07-19 — [Water Usage](content/2020-07-19-water-usage.md) (66 words, table)
* 2011-10-28 — [DVD menu in YouTube](content/2011-10-28-dvd-menu-in-youtube.md) (63 words, video)
* 2011-09-21 — [Funny Commercials](content/2011-09-21-funny-commercials.md) (61 words, video)
* 2012-02-24 — [Stuxnet](content/2012-02-24-stuxnet.md) (60 words, video)
* 2011-09-25 — [Game: Winterbells](content/2011-09-25-game-winterbells.md) (57 words, video)
* 2012-09-01 — [Nobel Prize in Physics 2009](content/2012-09-01-nobel-prize-in-physics-2009.md) (56 words, video)
* 2012-08-08 — [Short Educational Clips](content/2012-08-08-short-educational-clips.md) (55 words, video)
* 2017-04-01 — [Extraordinary Materials](content/2017-04-01-extraordinary-materials.md) (53 words, video)
* 2012-08-02 — [Shortfilms, Part II](content/2012-08-02-shortfilms-part-ii.md) (51 words, video)
* 2017-11-30 — [DQN - Deep Q Networks](content/2017-11-30-dqn.md) (51 words, table)
* 2014-11-18 — [Nyquist–Shannon sampling theorem](content/2014-11-18-nyquist-shannon-sampling-theorem.md) (33 words, video)
* 2017-12-29 — [Gradient Boosting](content/2017-12-29-gradient-boosting.md) (33 words, video)
* 2011-09-20 — [Subscribe via Email](content/2011-09-20-email-subscription.md) (31 words, —)
* 2011-10-22 — [Clip: Bob the Hamster](content/2011-10-22-bob-the-hamste.md) (31 words, video)
* 2012-03-12 — [Typography: Word as Image](content/2012-03-12-typography-word-as-image.md) (29 words, video)
* 2011-09-21 — [Imprint](content/2011-09-20-imprint.md) (21 words, —)
* 2011-10-23 — [Clip: Love Tap](content/2011-10-23-clip-love-tap.md) (21 words, video)
* 2011-09-26 — [Lolcats: Hermes'' Favorite Activity](content/2011-09-26-lolcats-hermes-favorite-activity.md) (19 words, video)
* 2012-07-01 — [George Carlin](content/2012-07-01-george-carlin.md) (19 words, video)
* 2012-12-22 — [Blender Open Movies](content/2012-12-22-blender-open-movies.md) (13 words, video)
* 2012-08-02 — [Nature by Numbers](content/2012-08-02-nature-by-numbers.md) (9 words, video)
* 2020-04-25 — [Offline First](content/2020-05-25-offline-first.md) (9 words, —)
* 2011-10-04 — [Clip: What Light](content/2011-10-04-clip-what-light.md) (0 words, video)
* 2012-02-23 — [Portal - Still Alive typography clip](content/2012-02-23-portal-still-alive-typography-clip.md) (0 words, video)

## Related: hotlinked images

Not part of (a) or (b), but found while building them. `AGENTS.md` says images
must be stored locally under `images/<year>/<month>/` and never hotlinked.
`python scripts/check_articles.py --only img-hotlink,img-markdown` lists them.
11 image references in 9 articles still point at a remote host:

| Article | Image |
| ------- | ----- |
| [Challenge Websites](content/2011-10-11-challenge-websites.md) | `http://projecteuler.net/profile/moose.png` (live profile badge) |
| [Password Changing Services](content/2011-10-17-password-chaning-services.md) | `http://imgs.xkcd.com/comics/password_strength.png` |
| [Computer Science Jokes](content/2012-03-11-computer-science-jokes.md) | `http://imgs.xkcd.com/comics/compiling.png` |
| [A.I. in Computer Games](content/2014-07-01-ai-in-computer-games.md) | `http://imgs.xkcd.com/comics/game_ais.png` |
| [XOR tutorial with TensorFlow](content/2016-07-19-tf-xor-tutorial.md) | `http://i.stack.imgur.com/YD9IS.png`, `awAz8.png`, `ocZHU.gif` (Markdown reference images) |
| [Python Packaging Course](content/2020-02-09-python-packaging-course.md) | `https://imgs.xkcd.com/comics/python_environment.png` |
| [Python Requirements](content/2020-05-16-python-requirements.md) | `https://imgs.xkcd.com/comics/python_environment.png` |
| [Strom in Deutschland: Auf dem richtigen Weg in eine nachhaltige Zukunft](content/2025-01-09-strom-in-deutschland.md) | `https://cdn.statcdn.com/Infographic/images/normal/30706.jpeg` |
| [Ausländer in Deutschland](content/2025-02-01-auslaender-in-deutschland.md) | `https://cdn.statcdn.com/Infographic/images/normal/18439.jpeg` |

The blog's own `martin-thoma.com` images (NIPS 2016, Lidl Connect) are relative
`../images/…` links now. The rest would have to be downloaded — note that the
xkcd comics and the Statista infographics have their own licence terms, and the
Project Euler badge is meant to show the current score. The Stack Exchange CDN
answers scripted downloads with 403, so the three XOR tutorial images have to be
saved by hand (their alt texts are written already).

## Related: images over 500 KB

`AGENTS.md` asks for images below 500 KB (pre-commit `check-added-large-files`)
and at most about 2000 px wide. In September 2026, 24 PNG screenshots without
transparency were converted to JPG and several JPGs were recompressed / scaled
down; PNGs with real transparency (`ml-ensemble-learning`, `soca-trail-2`,
`soca-trail-3`) were colour-quantized instead. `python scripts/check_articles.py
--only img-large` lists what is left. These were kept on purpose:

| Article | Files | Why kept |
| ------- | ----- | -------- |
| [Panasonic Lumix TZ41](content/2014-03-27-panasonic-lumix-tz41.md) | 24 camera samples in `images/2014/03/panasonic-lumix-dmc-tz-41/` and `casio-exilim-ex-z200/` (523 KB – 7.2 MB) | The article compares image quality of two cameras; recompressing the samples would falsify the comparison. Could be replaced by 1600 px previews that link to the originals. |
| [Bucketing in A/B testing](content/2019-11-28-bucketing-in-ab-testing.md) | 9 × `images/2019/11/1000-random-numbers-*.png` (716–978 KB) | Pixel-exact visualizations of random number generators; JPG artefacts would add structure that isn't in the data. |
| [Stromtarife](content/2023-03-31-stromtarife.md) | `images/2023/03/World_Map_of_Mains_Voltages_and_Frequencies,_Detailed.svg` (965 KB) | Wikimedia Commons SVG; a raster version would lose the detail. |
| [Sublime Text](content/2014-03-01-sublime-text.md) | `images/2014/03/sublime-align.gif` (511 KB) | Animated GIF; only slightly above the limit. |
