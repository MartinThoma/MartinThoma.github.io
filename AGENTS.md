# Rules for working on this blog

Pelican blog. Articles live in `content/YYYY-MM-DD-slug.md`. See `README.md` for
setup (`make html-local`, `make serve`). `ARTICLE_REVIEW_TODO.md` lists open review
findings per article; remove an entry once it is fixed.

## Front matter

* `slug` is lowercase with hyphens only (no spaces, URLs, trailing slash). It is the
  article URL (`{slug}/`).
* Never use `url:` or `URL:` in the front matter: Pelican treats them as the article's
  own URL. The original Medium address goes into `medium_url:`.
* `lang` is `en` or `de` and must match the language of the text.
* Every article with `lang: de` has `category: German posts`, and only those do. Check
  the actual language of the text: English articles get `lang: en` (or no `lang`).
* `tags` is a comma-separated list: `tags: Python, Testing, Unit Testing`.

## Tags

**Format**

* Title Case, one spelling per tag. Case variants and synonyms are merged:
  `mathematics` → `Mathematics`, `diy`/`do-it-yourself` → `DIY`,
  `Git` (not `git`), `NumPy`, `BWInf`, `Brute-Force`, `Lecture Notes`.
  Names that are lowercase by convention stay as they are (`pytest`, `mypy`, `tox`,
  `venv`, `virtualenv`, `arXiv`).
* Merged tags:
  * `Security` ← `IT-Security`, `IT Security`, `InfoSec`, `Cybersecurity`,
    `CyberSecurity`, `security`. `AppSec` stays a separate tag.
  * `CPP` ← `C++`, `cpp` (never use `C++` as a tag: the `+` characters break tag URLs and link
    generation). `AI` ← `A.I.`, `Artificial Intelligence`. `Politics` ← `Politik`.
  * `Software Engineering` ← `Software Development`, `Development`.
  * `Open Source` ← `foss`, `OpenSource`. `Bugs` ← `Bug`, `bug`. `Review` ← `Reviews`.
  * `Money` ← `finances`. `Data Structures` ← `datastructure`, `data structure`.
* Do not use tags that repeat the category (`Code`, `German posts`, `Cyberculture`)
  or that are meaningless (`Rating`). Category names are not tags.
* A tag must describe the article. Do not keep template defaults (drafts once had
  `Machine Learning` by default).
* Language tags: a Code, Machine Learning or The Web article with at least two fenced
  code blocks in one language gets that language tag (`Python`, `Java`, `CPP`, `PHP`,
  `JavaScript`). Do not add `Bash` for install snippets.

**Hierarchy**

* Tags form a hierarchy. An article with a child tag also has all its parent tags,
  transitively: `Matrix` → `Linear Algebra` → `Mathematics`, `Analysis` →
  `Mathematics`, `Flask` → `Python`, `Neural Networks` →
  `Machine Learning` → `AI`, `Klausur` → `University`.
* A tag is a parent only if the child is a *kind of* it. `Operating Systems` is only for
  articles about operating systems in general (scheduling, memory, file systems); it is
  not a parent of `Linux`, `Ubuntu` or `Windows`.
* Likewise, `Programming` is only for articles that are about programming (concepts,
  techniques, puzzles, code golf). Language and tool tags such as `Python`, `Bash` or `Flask`
  do not imply it: an article that merely uses a language or a script is not about
  programming.


**Video**

* An article that mainly consists of one or more videos (an embed plus a few
  sentences, collections of clips or short films) has the tag `Video`.
* `Clip` and `Shortfilm` are not used on their own. Use the general `Video` tag
  instead of `Clip`.
* `YouTube` and `Vimeo` are only for articles that are *about* YouTube or Vimeo
  (the platform, a playlist, a feature of it). Articles that merely embed a video
  from there get only `Video`.

**Games**

* `Flashgames` only if the linked game really is a Flash game (check the game
  page, e.g. Kongregate lists the technology). Games written in JavaScript get
  `JavaScript Game`.


## Links

* Link to other articles of this blog with relative links: `[text](../slug/)`.
  Not with `https://martin-thoma.com/slug/` and not with the Medium URL.
* Series (AppSec, unit testing, blockchain) end with an identical
  `## More in this series` section in every part. The current part is bold instead
  of a link; the outlook text is the same in all parts.
* Never show a bare URL as plain text: every URL in the text is a link. Prefer a
  descriptive link text; otherwise use the URL without scheme and `www.`
  (`[logotournament.com](http://logotournament.com/)`).
  `python scripts/link_bare_urls.py` does the latter. A URL that is the subject of the text
  (an example domain, an API endpoint, a metadata value) goes into a code span instead.
* Remove tracking parameters from links (`utm_*`, `fbclid`, Twitter `ref_src`,
  Amazon `/ref=…` and the like). Keep parameters that change the target, such as
  YouTube `t=` or Amazon `psc=`. Always keep YouTube's `si=` (in links and embeds):
  without it the video is not shown correctly.
* Cards that link to a blog article end with the subtitle only; do not append the
  domain name (`…levelup.gitconnected.com`).

## Images

* Store images locally in `images/<year>/<month>/`; never hotlink Medium's CDN.
  Downloaded Medium images are named `<slug>-<n>.<ext>`.
* Use `<figure>`, not Markdown `![]()`. Canonical form (CSS in `pelican-thoma/static/css/thoma.css`):

  ```html
  <figure class="figure-right ai-generated">
      <a href="../images/2024/01/x.png"><img src="../images/2024/01/x.png" alt="…" width="512" height="300" loading="lazy"></a>
      <figcaption>Caption</figcaption>
  </figure>
  ```

  * The `<a>` around the `<img>` opens the full-size file without JavaScript.
  * Size via `width`/`height` attributes, never inline `style`. Every local image has
    both (the page must not jump while loading), and a raster image is never shown wider
    than its pixel width.
  * The first image of an article has no `loading="lazy"` when it is near the top; all
    others are lazy. Tracking pixels (VG Wort) stay a bare 1×1 `<img>`: no figure, no lazy.
  * Optional classes on the `<figure>`: `figure-left` / `figure-right` (float; default
    is centered), `ai-generated` / `ai-modified` (corner badge on the image).
  * Images made by an AI tool (Claude, ChatGPT, Gemini, …) get `ai-generated`; a real
    photo that an AI tool changed gets `ai-modified`. The EU AI Act (Art. 50) requires the
    label only for deceptively real images; this blog marks every AI image except diagrams
    (charts, flow and network diagrams, pyramids, maps with data). The caption names the
    tool in every case, diagrams included.
  * No WordPress classes (`wp-caption`, `aligncenter`, `size-*`, `img-thumbnail`).
  * `python scripts/normalize_images.py` converts old markup to this form; it is idempotent.
* Several images in a grid (photo series, before/after comparisons, test cases) go into
  `<div class="gallery">` with one `<figure>` per image in the form above. Thumbnails
  get boxes of equal height, so captions line up. Three or more figures in a row with
  nothing but blank lines between them are a gallery, and a figure right next to a gallery
  joins it (`normalize_images.py` does both). Galleries directly after each other stay
  separate: they are rows of one collection (e.g. one row per category).
* A click on any figure opens the lightbox (`pelican-thoma/static/js/lightbox.js`): it shows
  the `<a href>` file with the figcaption. Left/right (buttons, arrow keys, swipe) page through
  the figures of the gallery; the up/down keys jump to the first figure of the previous/next
  gallery on the page, where a figure outside a gallery counts as a gallery of one. So the link
  must point to the full-size image file.
* Dark mode: transparent PNGs and GIFs get a white background from the CSS. An SVG sits on the
  theme surface, which is dark in dark mode, so it needs its own
  `prefers-color-scheme: dark` palette or a white background `<rect>`.
* Every image needs a meaningful alt text (`alt="…"`). Only invisible
  tracking pixels may use `alt=""`.
* Images must be smaller than 500 KB (pre-commit `check-added-large-files`).
  Convert PNG screenshots without transparency to JPG and scale to at most 1600–2000
  px width.

## Tables

* Large tables are handled by `pelican-thoma/static/js/tables.js`: a table wider than the
  text column scrolls in its own box with a sticky header row, a sticky first column (if it
  is narrow enough) and a "Maximieren" button; a table that is only long gets a header row
  that sticks below the site header. For this the header row must be a `<thead>` or a first
  row of `<th>` cells. Layout tables get `class="transparent"` and are left alone.

## Math

Math is rendered by MathJax 2. In Markdown, the `render_math` plugin (plus the local
`plugins/render_math_fixes.py`) protects it from Markdown, so `\\`, `\{` and `_` survive.

* Inline: `$…$`, with no whitespace before the closing `$`. Otherwise the plugin
  skips the formula and Markdown mangles it (`\{` becomes `{`, `_…_` becomes italics).
* Display: `$$…$$`, or an environment on its own (`\begin{align}…\end{align}`).
* Do not use `\(…\)` or `\[…\]` in Markdown: Markdown turns `\(` into `(`.
* A literal dollar sign in text is `\$` (prices, shell and PHP variables in prose);
  code spans and `<code>` need no escape. Two plain `$` in one paragraph become a formula.
* Function names and words get a backslash or `\text`: `\sin`, `\log`, `\det`, `\max`,
  `\gcd`, `I_{\max}`, `\text{rank}_i`.

## Questions and answers

* Exam questions whose answer is revealed on click use
  `<details class="question"><summary>Frage?</summary><div class="answer">…</div></details>`
  (styles in `static/custom.css`, no JavaScript).

## Footnotes and sources

* Cite with Markdown footnotes: `text[^1]` in the text, `[^1]: …` as one line per
  footnote. This also works inside raw HTML blocks (tables, lists, figures) thanks to
  `plugins/footnotes_in_html.py`. Never write footnote HTML (`<sup>`, `#fn:1`,
  `name="anchor1"`) by hand.
* A footnote text that starts like a list item becomes a nested list: write
  `[^1]: 2\. Klausur …`, not `[^1]: 2. Klausur …`.
* Footnotes render as `[1]`, numbered in the order of their first citation, with one ↩
  per citation. Number the labels in that order and list the definitions sorted.
* Sources of a German article go under a final `## Einzelnachweise` heading (English:
  `## Footnotes`), with nothing after the definitions: the list renders at the end of
  the article. Every footnote must be cited in the text; an uncited one gets a dead ↩.
* Format of a source: `Autor: [Titel](URL) via Website, TT.MM.JJJJ.` The author only if
  one is named (a person, or an agency like `dpa` that differs from the site); the date
  is the publication date, otherwise `abgerufen am TT.MM.JJJJ`. YouTube: the channel is
  the author, `via YouTube`.

## Facts and numbers

* If a number is corrected, add a source where reasonable and recompute everything
  that depends on it (tables, conclusions).
* Do not invent sources or URLs; only link pages that exist.
