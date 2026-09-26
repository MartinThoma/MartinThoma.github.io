# Blog scripts

Scripts for checking and fixing the articles in `content/`. Run them from the
repository root with the project environment (see the main [README](../README.md)):

```bash
uv run python scripts/<script>.py --help
```

Scripts that change files accept `--dry-run`. Without file arguments they process all
articles.

| Script | What it does |
| ------ | ------------ |
| `check_articles.py` | Checks the rules from `AGENTS.md` and reports problems; changes nothing. |
| `normalize_images.py` | Converts image markup to the canonical `<figure>` form, adds `width`/`height`, groups figures into galleries. Idempotent. |
| `link_bare_urls.py` | Turns bare URLs in the text into links (`[example.com](https://www.example.com/)`). |
| `auto_fix_blog.py` | Pre-commit hook: number formatting, missing `lang` and `slug`, trailing whitespace. Processes staged files; `--all` for all articles. |
| `analyze_tags.py` | Tag statistics (writes `tag_analysis_report.txt`). |
| `temperatur_cost_heating.py` | Heating load and annual heating cost calculation (German). |

## check_articles.py

```bash
uv run python scripts/check_articles.py                           # all published articles
uv run python scripts/check_articles.py content/2026-09-30-x.md   # single files
uv run python scripts/check_articles.py --only img,math           # only some checks
uv run python scripts/check_articles.py --drafts                  # include status: draft
```

Checks are grouped by prefix; `--only` takes full names or prefixes:

* `fm-*`: front matter (slug, `url:`, `lang` vs. category and text language, tag
  spelling, merged and banned tags, tag hierarchy, featured image).
* `link-*`: absolute links to the blog, links to the own Medium posts, broken relative
  links, tracking parameters.
* `img-*`: Markdown images, hotlinks, inline styles, WordPress classes, alt text, missing
  or oversized files, missing `width`/`height`, upscaled images.
* `math-*`: `\(…\)` delimiters, whitespace before the closing `$`, unescaped dollar
  signs, function names without backslash.
* `text-*`: doubled words, space before punctuation, lowercase "i".
* `out-*`: problems in the generated HTML (unrendered Markdown, stray `$`, empty
  links); needs a current build in `output/` (`make html-local`).

The remaining findings on the current content are deliberate; `IMAGES.md` explains the
hotlinked and oversized images.

## Pre-commit

`.pre-commit-config.yaml` runs `auto_fix_blog.py`, the standard pre-commit hooks (500 KB
file size limit, whitespace, YAML/JSON syntax) and `blacken-docs`.

```bash
uv run pre-commit run --all-files   # run all hooks on all files
uv run pre-commit run auto-fix-blog # run one hook
```
