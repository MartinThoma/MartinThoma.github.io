# martin-thoma.com

Source of [martin-thoma.com](https://martin-thoma.com/), a static blog built with
[Pelican](https://getpelican.com/). The `pelican` branch holds the sources; `make github`
publishes the generated site to the `master` branch (GitHub Pages).

| Path | Content |
| ---- | ------- |
| `content/YYYY-MM-DD-slug.md` | Articles (Markdown with front matter) |
| `_drafts/` | Drafts that Pelican does not read |
| `images/<year>/<month>/` | Images used by the articles |
| `pelican-thoma/` | Theme (templates, CSS, JavaScript) |
| `plugins/` | Local Pelican plugins (search index, summaries, math fixes, …) |
| `pelican-toc/`, `pelican-sitemap/` | Plugins included as git submodules |
| `scripts/` | Checks and fix-up scripts, see [`scripts/README.md`](scripts/README.md) |
| `sublime/` | Sublime Text snippets for new articles, figures, galleries and math |
| `AGENTS.md` | Writing rules: front matter, tags, links, images, math |
| `ARTICLE_REVIEW_TODO.md` | Open review findings per article |
| `IMAGES.md` | Articles that could use an image, hotlinked and oversized images |

## Setup

The Python environment is managed by [uv](https://docs.astral.sh/uv/)
(`pyproject.toml`, `uv.lock`). Install uv once, e.g. with
`curl -LsSf https://astral.sh/uv/install.sh | sh`, then:

```bash
git clone --recursive git@github.com:MartinThoma/MartinThoma.github.io.git
cd MartinThoma.github.io
make install    # uv sync, git submodule update, pre-commit install
```

uv reads `.python-version` and installs that Python itself. If `uv` on your `PATH` is a
pyenv shim that points to a different Python, call the real binary instead, e.g.
`make UV=~/.local/bin/uv html-local`. Every Makefile target accepts `UV=…`.

## Writing and previewing

1. Create `content/YYYY-MM-DD-slug.md` (the Sublime snippet `---` inserts the front matter)
   and follow the rules in [`AGENTS.md`](AGENTS.md).
2. `make html-local` builds the site into `output/` with local URLs;
   `make serve` then serves `output/` at <http://127.0.0.1:8000/>.
3. Check the article before committing:

   ```bash
   uv run python scripts/check_articles.py content/2026-09-30-my-article.md
   uv run python scripts/normalize_images.py content/2026-09-30-my-article.md
   ```

   `check_articles.py` reports front matter, tag, link, image and math problems;
   `normalize_images.py` converts images to the canonical `<figure>` markup and adds
   `width`/`height`. Some checks look at the generated HTML, so build first.

The pre-commit hooks (`auto_fix_blog.py`, file size limit of 500 KB, whitespace) run on
every commit.

An article from Medium can be imported with
`uv run python mediumexporter.py -H <medium-url> > content/YYYY-MM-DD-slug.md`; afterwards
download its images into `images/<year>/<month>/` (see `AGENTS.md`).

## Publishing

```bash
make github    # build with publishconf.py, push the result to the master branch
```

## Maintenance

```bash
make maint     # uv lock --upgrade, uv sync, pre-commit autoupdate
make clean     # remove output/
make help      # all targets
```
