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
  on the index page, never on the article itself, and 917 of 951 articles have
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
**48 of 951 articles** have neither an image nor code (two of them drafts).

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

On 2026-10-10/11, 242 articles of this list got an illustration.

### Over 1500 words (1)

| Date | Article | Words | Other |
| ---- | ------- | ----: | ----- |
| 2026-10-01 | [Kinderzimmer renovieren](content/2026-10-03-kinderzimmer-renovieren.md) (draft) | 3860 | table |

Before/after photos are planned (TODO in the article).

### 700–1499 words (1)

| Date | Article | Words | Other |
| ---- | ------- | ----: | ----- |
| 2026-10-10 | [Garage](content/2026-10-10-garage.md) (draft) | 1252 | table |

A sketch of the hatch railing or the stair would help.

### 300–699 words (1)

| Date | Article | Words | Other |
| ---- | ------- | ----: | ----- |
| 2026-09-27 | [How I use AI on this blog](content/2026-09-27-how-i-use-ai.md) | 639 | — |

### Under 300 words (45)

Mostly link collections, short notes and announcements. Listed for completeness;
most of these probably do not need an image.

* 2015-11-02 — [Wo ist Hörsaal 9 am KIT?](content/2015-11-02-wo-ist-hs9.md) (140 words, —)
* 2018-09-30 — [Abandoned domains are a security issue](content/2023-09-30-abandoned-domains.md) (136 words, —)
* 2024-08-12 — [Food Processors](content/2024-08-12-food-processor.md) (133 words, —)
* 2011-09-30 — [If Computer Problems Were Real](content/2011-09-30-if-computer-problems-were-real.md) (130 words, video)
* 2012-03-20 — [Wie bestimme ich das Inverse einer Matrix?](content/2012-03-20-wie-bestimme-ich-das-inverse-einer-matrix.md) (127 words, math)
* 2012-09-15 — [Partielle Integration](content/2012-09-15-partielle-integration.md) (127 words, math)
* 2014-10-26 — [Gradient Descent, the Delta Rule and Backpropagation](content/2014-10-26-gradient-descent-delta-rule-backpropagation.md) (118 words, —)
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
8 image references in 8 articles still point at a remote host:

| Article | Image |
| ------- | ----- |
| [Challenge Websites](content/2011-10-11-challenge-websites.md) | `http://projecteuler.net/profile/moose.png` (live profile badge) |
| [Password Changing Services](content/2011-10-17-password-chaning-services.md) | `http://imgs.xkcd.com/comics/password_strength.png` |
| [Computer Science Jokes](content/2012-03-11-computer-science-jokes.md) | `http://imgs.xkcd.com/comics/compiling.png` |
| [A.I. in Computer Games](content/2014-07-01-ai-in-computer-games.md) | `http://imgs.xkcd.com/comics/game_ais.png` |
| [Python Packaging Course](content/2020-02-09-python-packaging-course.md) | `https://imgs.xkcd.com/comics/python_environment.png` |
| [Python Requirements](content/2020-05-16-python-requirements.md) | `https://imgs.xkcd.com/comics/python_environment.png` |
| [Strom in Deutschland: Auf dem richtigen Weg in eine nachhaltige Zukunft](content/2025-01-09-strom-in-deutschland.md) | `https://cdn.statcdn.com/Infographic/images/normal/30706.jpeg` |
| [Ausländer in Deutschland](content/2025-02-01-auslaender-in-deutschland.md) | `https://cdn.statcdn.com/Infographic/images/normal/18439.jpeg` |

The blog's own `martin-thoma.com` images (NIPS 2016, Lidl Connect) are relative
`../images/…` links now. The rest would have to be downloaded — note that the
xkcd comics and the Statista infographics have their own licence terms, and the
Project Euler badge is meant to show the current score. The three XOR tutorial
images are stored locally now (see below for two follow-up issues).

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

Open (not decided yet):

| Article | Files | Problem |
| ------- | ----- | ------- |
| [XOR tutorial with TensorFlow](content/2016-07-19-tf-xor-tutorial.md) | `images/2016/07/gradient-descent-animation.gif` (714 KB) | Animated GIF above the limit; fewer frames or colours, or a video. |
| [XOR tutorial with TensorFlow](content/2016-07-19-tf-xor-tutorial.md) | `images/2016/07/neural-network.png` | Shown 512 px wide, but the file is only 320 px (`img-upscaled`). Show it at 320 px or find a larger version. |
