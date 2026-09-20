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
* Remove tracking parameters from links (`utm_*`, `fbclid`, YouTube `si=`, Twitter
  `ref_src`, Amazon `/ref=…` and the like). Keep parameters that change the
  target, such as YouTube `t=` or Amazon `psc=`.
* Cards that link to a blog article end with the subtitle only; do not append the
  domain name (`…levelup.gitconnected.com`).

## Images

* Store images locally in `images/<year>/<month>/`; never hotlink Medium's CDN.
  Downloaded Medium images are named `<slug>-<n>.<ext>`.
* Every image needs a meaningful alt text (`![alt](…)` or `alt="…"`). Only invisible
  tracking pixels may use `alt=""`.
* Images must be smaller than 500 KB (pre-commit `check-added-large-files`).
  Convert PNG screenshots without transparency to JPG and scale to at most 1600–2000
  px width.

## Facts and numbers

* If a number is corrected, add a source where reasonable and recompute everything
  that depends on it (tables, conclusions).
* Do not invent sources or URLs; only link pages that exist.
