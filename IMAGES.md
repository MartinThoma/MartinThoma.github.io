# Images TODO

Two groups of articles that need a decision about illustrations:

* **(a)** articles that use **stock photos** — generic filler that could be
  replaced with a real diagram or screenshot, or dropped;
* **(b)** articles with **no images** — walls of text that might benefit from
  a diagram, screenshot, table or photo.

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
**275 of 902 published articles** have no image: 255 without one yet and 20 video posts.

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

## (b) Articles without images

History: on 2026-10-10/11, 242 articles of this list got an AI illustration. On
2026-11-07 the remaining ones got generated SVG title illustrations (one topic icon
plus a few related objects). Martin found them too generic, so they were removed
again the same day; only articles that got a real image kept one: Converting Files
with Linux (his own image), Winterbells (game screenshot, taken with headless Chrome
and Ruffle) and Benchmarking PHP (`scripts/ab_percentile_chart.py`).

What a new image should be: something that helps to understand the article, not
decoration. In order of preference:

* a **screenshot** for articles about a game, website, service or application;
* an **explanatory diagram or chart** (what a tool measures, how an algorithm
  works);
* a **comic scene with people** in the gruene-plattling.de style, especially for
  politics and everyday topics. Planned: Getting Hardware Information in Ubuntu,
  a person inspecting their computer like a detective or a doctor (needs image API
  credit; `scripts/title_image.py`).

No image is better than a generic one.

### Code (154)

* 2011-09-21 — [Tricks with .htaccess](content/2011-09-21-tricks-with-htaccess.md)
* 2011-09-22 — [Getting Hardware Information in Ubuntu](content/2011-09-22-getting-hardware-information-in-ubuntu.md)
* 2011-09-24 — [PHP: PEAR MDB2](content/2011-09-24-pear-db.md)
* 2011-09-24 — [Python: Check Wiki-references for citation template](content/2011-09-24-python-check-wiki-references-for-citation-template.md)
* 2011-09-30 — [Colorize Your Script Output](content/2011-09-30-colorize-your-scripts-output.md)
* 2011-10-04 — [Comparing Dates in PHP and MySQL](content/2011-10-04-comparing-dates-in-php-and-mysql.md)
* 2011-10-18 — [Create LaTeX timetable](content/2011-10-18-create-latex-timetable.md)
* 2011-10-22 — [Understanding Python Lists](content/2011-10-22-understanding-python-lists.md)
* 2011-11-10 — [Python Generators](content/2011-11-10-python-generators.md)
* 2011-12-17 — [How to use magic rescue](content/2011-12-17-how-to-use-magic-rescue.md)
* 2011-12-28 — [Surprising C errors](content/2011-12-28-surprising-c-errors.md)
* 2012-03-01 — [Get your programs assembly code and more information](content/2012-03-01-get-your-programs-assembly-code-and-more-information.md)
* 2012-04-12 — [PHP: A strange language](content/2012-04-12-php-a-strange-language.md)
* 2012-04-15 — [Google Code Jam 2012 - Qualification Round](content/2012-04-15-google-code-jam-2012-qualification-round.md)
* 2012-04-28 — [Google Code Jam 2012 – Round 1A 2012](content/2012-04-28-google-code-jam-2012-round-1a-2012.md)
* 2012-05-05 — [Google Code Jam 2012 – Round 1B 2012](content/2012-05-05-google-code-jam-2012-round-1b-2012.md)
* 2012-05-06 — [Google Code Jam 2012 – Round 1C 2012](content/2012-05-06-google-code-jam-2012-round-1c-2012.md)
* 2012-05-18 — [How do Bitmasks work?](content/2012-05-18-how-do-bitmasks-work.md)
* 2012-05-28 — [Sets in C++](content/2012-05-28-sets-in-cpp.md)
* 2012-05-28 — [Stacks in C++](content/2012-05-28-stacks-in-cpp.md)
* 2012-05-28 — [Vectors in C++](content/2012-05-28-vectors-in-cpp.md)
* 2012-06-08 — [Cool Features of Python](content/2012-06-08-cool-features-of-python.md)
* 2012-06-12 — [Functional Programming in Python](content/2012-06-12-functional-programming-in-python.md)
* 2012-06-16 — [Add MIPS syntax highlighting to gEdit](content/2012-06-16-add-mips-syntax-highlighting-gedit.md)
* 2012-06-18 — [Python Puzzle #1: List multiplication](content/2012-06-18-python-puzzle-1-list-multiplication.md)
* 2012-06-22 — [Perfect number check and ROT-13 encryption in MIPS-assembly code](content/2012-06-22-perfect-number-check-rot-13-encryption-mips-assembly-code.md)
* 2012-07-04 — [How to create your own Python module](content/2012-07-04-how-to-create-your-own-python-module.md)
* 2012-07-06 — [C++ Operator Overloading](content/2012-07-06-cpp-operator-overloading.md)
* 2012-07-07 — [My LaTeX Tikz Template](content/2012-07-07-my-latex-tikz-template.md)
* 2012-07-16 — [Java Puzzle #2: Integers and Floats](content/2012-07-16-java-puzzle-2-integers-and-floats.md)
* 2012-07-17 — [Java Puzzle #3: Rounding](content/2012-07-17-java-puzzle-3-rounding.md)
* 2012-07-18 — [How to parse command line arguments in Python](content/2012-07-18-how-to-parse-command-line-arguments-in-python.md)
* 2012-08-01 — [Python Puzzle #2: None and False](content/2012-08-01-python-puzzle-2-none-and-false.md)
* 2012-08-02 — [Java Puzzle #4: Parallel Programming](content/2012-08-02-java-puzzle-4-parallel-programming.md)
* 2012-08-03 — [Java Puzzle #5: Parallel Programming, Part 2](content/2012-08-03-java-puzzle-5-parallel-programming-part-2.md)
* 2012-08-04 — [Java Puzzle #6: Double Arithmetic](content/2012-08-04-java-puzzle-6-double-arithmetic.md)
* 2012-08-05 — [Java Puzzle #7: Inheritance and Visibility](content/2012-08-05-java-puzzle-7-inheritance-and-visibility.md)
* 2012-08-09 — [Java Puzzle #8: Interfaces and Visibility](content/2012-08-09-java-puzzle-8-interfaces-and-visibility.md)
* 2012-08-10 — [Java Puzzle #9: Template method pattern](content/2012-08-10-java-puzzle-9-template-method-pattern.md)
* 2012-08-16 — [Java Puzzle #10: Multiple Interfaces](content/2012-08-16-java-puzzle-10-multiple-interfaces.md)
* 2012-09-27 — [Code golf](content/2012-09-27-code-golf.md)
* 2012-10-02 — [Python Puzzle #3: Associativity](content/2012-10-02-python-puzzle-3-associativity.md)
* 2012-10-10 — [Java Generics](content/2012-10-10-java-generics.md)
* 2012-10-14 — [Java Puzzle #11: Change argument of foreach](content/2012-10-14-java-puzzle-11-change-argument-of-foreach.md)
* 2012-10-17 — [Java Puzzle #12: Control-flow](content/2012-10-17-java-puzzle-12-control-flow.md)
* 2012-10-19 — [Java Puzzle #13: Absolute Value Weirdness](content/2012-10-19-java-puzzle-13-absolute-value-weirdness.md)
* 2012-10-20 — [C Puzzle #2](content/2012-10-20-c-puzzle-2.md)
* 2012-10-22 — [Java Puzzle #14: Integers](content/2012-10-22-java-puzzle-14-integers.md)
* 2012-11-13 — [Project Euler: Problem 32](content/2012-11-13-project-euler-problem-32.md)
* 2012-11-14 — [Project Euler: Problem 33](content/2012-11-14-project-euler-problem-33.md)
* 2012-11-29 — [Make your Bash more useful](content/2012-11-29-make-your-bash-more-useful.md)
* 2012-12-25 — [C++ Preprocessor Snippets](content/2012-12-25-c-preprocessor-snippets.md)
* 2013-01-08 — [How to sort with Java](content/2013-01-08-how-to-sort-with-java.md)
* 2013-01-20 — [Cyclic references kill Nautilus](content/2013-01-20-cyclic-references-kill-nautilus.md)
* 2013-02-04 — [Basic Multithreading in Java](content/2013-02-04-basic-multithreading-in-java.md)
* 2013-02-04 — [What can ArrayList / LinkedList do what List can't?](content/2013-02-04-what-can-arraylist-linkedlist-do-what-list-cant.md)
* 2013-03-16 — [C Puzzle #3](content/2013-03-16-c-puzzle-3.md)
* 2013-03-20 — [What does volatile mean?](content/2013-03-20-what-does-volatile-mean.md)
* 2013-04-16 — [What does #!/usr/bin/env python mean?](content/2013-04-16-what-does-usrbinpython-mean.md)
* 2013-04-26 — [Google Code Jam Templates](content/2013-04-26-google-code-jam-templates.md)
* 2013-04-27 — [Google Code Jam – Round 1A 2013](content/2013-04-27-google-code-jam-round-1a-2013.md)
* 2013-05-12 — [Google Code Jam – Round 1C 2013](content/2013-05-12-google-code-jam-round-1c-2013.md)
* 2013-05-16 — [Maps in C++](content/2013-05-16-maps-in-cpp.md)
* 2013-05-19 — [Solving equations of lower unitriangular matrices](content/2013-05-19-solving-equations-of-unipotent-lower-triangular-matrices.md)
* 2013-05-20 — [Solving equations of upper triangular matrices](content/2013-05-20-solving-equations-of-upper-triangular-matrices.md)
* 2013-06-01 — [Fractions in C++](content/2013-06-01-fractions-in-cpp.md)
* 2013-06-02 — [Inverting matrices](content/2013-06-02-inverting-matrices.md)
* 2013-06-07 — [Structs in C++](content/2013-06-07-structs-in-c.md)
* 2013-06-22 — [Polynomial interpolation](content/2013-06-22-polynomial-interpolation.md)
* 2013-06-26 — [JavaScript: WTF?!?](content/2013-06-26-javascript-wtf.md)
* 2013-10-18 — [Part IV: How to multiply matrix with its transpose in Python and C++](content/2013-10-18-part-iv-multiply-matrix-transpose-python-cpp.md)
* 2013-10-21 — [Part III: Matrix multiplication on multiple cores in Python, Java and C++](content/2013-10-21-part-iii-matrix-multiplication-on-multiple-cores-in-python-java-and-c.md)
* 2013-10-31 — [Fibonacci, recursion and decorators](content/2013-10-31-fibonacci-recursion-decorators.md)
* 2013-11-07 — [Formatting Strings in Python](content/2013-11-07-formatting-strings-python.md)
* 2014-01-15 — [Ruby](content/2014-01-15-ruby.md)
* 2014-01-15 — [Sum of cubed digits riddle](content/2014-01-15-sum-of-cubed-digits-riddle.md)
* 2014-03-08 — [Interpreters and Shells](content/2014-03-08-interpreters-and-shells.md)
* 2014-03-20 — [How to use Sublime Text via SSH](content/2014-03-20-sublime-via-ssh.md)
* 2014-04-02 — [Prolog](content/2014-04-02-prolog.md)
* 2014-05-03 — [HTML5 Template](content/2014-05-03-html5-template.md)
* 2014-06-27 — [What are pfiles?](content/2014-06-27-what-are-pfiles.md)
* 2014-06-30 — [Linux Commands for Working from Home](content/2014-06-30-linux-commands-for-working-from-home.md)
* 2014-07-14 — [Fix zypper readline error](content/2014-07-14-fix-zypper-libreadline-error.md)
* 2014-07-18 — [Introduction to Octave](content/2014-07-18-introduction-to-octave.md)
* 2014-07-20 — [Append Python PATH](content/2014-07-20-append-python-path.md)
* 2014-07-27 — [Configuration files in Python](content/2014-07-27-configuration-files-in-python.md)
* 2014-08-01 — [Logging in Python](content/2014-08-01-logging-in-python.md)
* 2014-08-11 — [Start long-running processes via SSH](content/2014-08-11-start-long-running-processes-via-ssh.md)
* 2014-11-18 — [Nyquist–Shannon sampling theorem](content/2014-11-18-nyquist-shannon-sampling-theorem.md)
* 2014-12-29 — [Cronjobs](content/2014-12-29-cronjobs.md)
* 2014-12-29 — [Java Exceptions](content/2014-12-29-java-exceptions.md)
* 2014-12-29 — [Packaging with Python](content/2014-12-29-python-packaging.md)
* 2014-12-29 — [Subversion](content/2014-12-29-subversion.md)
* 2015-01-20 — [Regular Expressions with Python](content/2015-01-20-python-regex.md)
* 2015-02-01 — [Execute Python on Apache2](content/2015-02-01-execute-python-on-apache2.md)
* 2015-02-05 — [Python Shell autocomplete](content/2015-02-05-python-shell-autocomplete.md)
* 2015-02-08 — [Python and CSV](content/2015-02-08-python-csv.md)
* 2015-02-12 — [Reading and Writing Files with Python](content/2015-02-12-reading-files-with-python.md)
* 2015-02-14 — [Python and Encodings](content/2015-02-14-python-and-encodings.md)
* 2015-03-26 — [The Rust Programming Language](content/2015-03-26-rust.md)
* 2015-04-02 — [Python ctypes](content/2015-04-02-python-ctypes.md)
* 2015-04-08 — [Python Code Documentation](content/2015-04-08-python-code-documentation.md)
* 2016-07-05 — [Python's map, reduce and filter as list comprehensions](content/2016-07-05-pythons-map-reduce-filter.md)
* 2016-12-14 — [URL RegEx](content/2016-12-14-url-regex.md)
* 2016-12-28 — [Word Vectors](content/2016-12-28-word-vectors.md)
* 2017-01-06 — [How to use arXiv data](content/2017-01-06-arxiv-data.md)
* 2017-02-23 — [How to use GLPK](content/2017-02-23-glpk.md)
* 2017-04-02 — [Git Bundle](content/2017-04-02-git-bundle.md)
* 2017-05-14 — [Defaults of Configuration Files](content/2017-05-14-cfg-files-defaults.md)
* 2017-07-22 — [Docker](content/2017-07-22-docker.md)
* 2017-08-06 — [Strings](content/2017-08-06-strings.md)
* 2017-08-14 — [Critique of Python 3](content/2017-08-14-python-3-critique.md)
* 2018-01-18 — [Python Projects](content/2018-01-18-python-projects.md)
* 2018-01-27 — [Datetime](content/2018-01-27-datetime.md)
* 2018-03-14 — [Pandas: Merge, join, concatenate](content/2018-03-14-pandas-merge-join-concatenate.md)
* 2018-06-08 — [Stages of Software Development](content/2018-06-08-software-developmen-statges.md)
* 2018-06-27 — [Make Python Objects JSON serializable](content/2018-06-27-make-json-serializable.md)
* 2018-07-03 — [Testing in Python](content/2018-07-03-testing-python-code.md)
* 2018-07-08 — [Git - Version Control Done Right](content/2018-07-08-git.md)
* 2018-07-11 — [Flask and Gunicorn](content/2018-07-11-flask.md)
* 2018-08-21 — [Bugs](content/2018-08-21-bugs.md)
* 2018-10-03 — [How old am I?](content/2018-10-03-age-calculation.md)
* 2018-10-09 — [Command Line](content/2018-10-09-command-line.md)
* 2018-10-19 — [Closures](content/2018-10-19-closures.md)
* 2018-10-19 — [Python property](content/2018-10-19-python-property.md)
* 2018-10-28 — [Python's str vs repr](content/2018-10-28-str-vs-repr.md)
* 2018-11-13 — [Python Package Versions](content/2018-11-13-python-package-versions.md)
* 2018-11-26 — [Type Systems](content/2018-11-26-type-systems.md)
* 2018-12-30 — [Code Quality](content/2018-12-30-code-quality.md)
* 2019-02-25 — [Python Puzzle 4](content/2019-02-25-python-puzzle-4.md)
* 2019-05-24 — [Gunicorn](content/2019-05-24-gunicorn.md)
* 2019-06-02 — [SQL Connection Strings](content/2019-06-02-sql-connection-strings.md)
* 2019-09-29 — [Key-Value Stores](content/2019-09-29-key-value-stores.md)
* 2019-11-03 — [Ansible](content/2019-11-03-ansible.md)
* 2019-11-03 — [jq](content/2019-11-03-jq.md)
* 2019-11-28 — [Simulated Annealing](content/2019-11-28-simulated-annealing.md)
* 2019-12-09 — [Python Itertools](content/2019-12-09-itertools.md)
* 2019-12-31 — [How to Speed up Docker](content/2019-12-31-docker-speedup.md)
* 2019-12-31 — [Flask Plugins](content/2019-12-31-flask-plugins.md)
* 2019-12-31 — [Git Contribution Statistics](content/2019-12-31-git-contribution-statistics.md)
* 2019-12-31 — [Lynis](content/2019-12-31-lynis.md)
* 2020-01-12 — [pyproject.toml](content/2020-01-12-pyproject.md)
* 2020-02-08 — [Virtual Environments](content/2020-02-08-virtual-environments.md)
* 2020-03-13 — [Code Golf: Brackets Check](content/2020-03-13-brackets-check.md)
* 2020-04-30 — [How to build reliable Software](content/2020-04-30-reliable-software.md)
* 2020-05-10 — [File Encryption](content/2020-05-10-file-encryption.md)
* 2020-05-11 — [MongoDB](content/2020-05-11-mongodb.md)
* 2020-05-23 — [Python EEL](content/2020-05-23-eel.md)
* 2020-06-29 — [Unit Testing in Python — The Basics](content/2020-06-29-unit-testing-basics.md)
* 2020-07-09 — [Unit Testing in Python — Patching, Mocks and Dependency Injection](content/2020-07-09-unit-testing-patching.md)
* 2020-11-02 — [pydantic](content/2020-11-02-pydantic.md)
* 2020-11-22 — [Python's Scoping Rules](content/2020-11-22-python-scoping.md)
* 2021-03-09 — [Programming Interviews: Fizz Buzz](content/2021-03-09-fizz-buzz.md)
* 2021-10-17 — [9 Clean Code Patterns I wish I knew earlier](content/2021-10-17-clean-code-patterns.md)

### Machine Learning (23)

* 2014-06-16 — [Classification with PyBrain](content/2014-06-16-classification-with-pybrain.md)
* 2014-09-06 — [The Twiddle Algorithm](content/2014-09-06-twiddle.md)
* 2014-10-26 — [Gradient Descent, the Delta Rule and Backpropagation](content/2014-10-26-gradient-descent-delta-rule-backpropagation.md)
* 2015-04-17 — [Lasagne for Python Newbies](content/2015-04-17-lasagne-for-python-newbies.md)
* 2015-11-11 — [Tensor Flow - A quick impression](content/2015-11-11-tensor-flow-quick.md)
* 2016-01-14 — [Using SVMs with sklearn](content/2016-01-14-svm-with-sklearn.md)
* 2016-02-09 — [Softmax](content/2016-02-09-softmax.md)
* 2017-01-30 — [skdata](content/2017-01-30-skdata.md)
* 2017-03-06 — [How to download ImageNet](content/2017-03-06-download-data.md)
* 2017-03-29 — [ZCA Whitening](content/2017-03-29-zca-whitening.md)
* 2017-03-30 — [How to silence TensorFlow](content/2017-03-30-silence-tf.md)
* 2017-05-24 — [Natural Language Processing](content/2017-05-24-nlp.md)
* 2017-07-27 — [The Reuters Dataset](content/2017-07-27-nlp-reuters.md)
* 2017-10-08 — [ASR Services](content/2017-10-08-asr-services.md)
* 2017-11-07 — [RL Agents](content/2017-11-07-rl-agents.md)
* 2017-11-15 — [Best practice for Machine Learning Projects](content/2017-11-15-ml-best-practice.md)
* 2017-11-26 — [Q-Learning](content/2017-11-26-q-learning.md)
* 2017-11-30 — [DQN - Deep Q Networks](content/2017-11-30-dqn.md)
* 2017-12-13 — [Reproducibility in Machine Learning](content/2017-12-13-ml-reproducibility.md)
* 2017-12-29 — [Gradient Boosting](content/2017-12-29-gradient-boosting.md)
* 2018-06-05 — [Feature Importance](content/2018-06-05-feature-importance.md)
* 2018-12-30 — [SLAM](content/2018-12-30-slam.md)
* 2019-01-13 — [WiLI-2018](content/2019-01-13-wili.md)

### Security (5)

* 2020-10-12 — [SQL Injections 😈](content/2020-10-12-sql-injections.md)
* 2020-10-13 — [Leaking Secrets 😇](content/2020-10-13-leaking-secrets.md)
* 2020-10-28 — [ZIP Bombs 💣😈](content/2020-10-28-zip-bombs.md)
* 2020-12-07 — [XXE attacks 😈](content/2020-12-07-xxe.md)
* 2021-01-28 — [Insecure Deserialization 😈🐝](content/2021-01-28-insecure-deserialization.md)

### The Web (8)

* 2011-09-21 — [Setting up WordPress](content/2011-09-21-setting-up-wordpress.md)
* 2011-10-17 — [MD5 cracking](content/2011-10-17-md5-cracking.md)
* 2011-10-22 — [Improvements for my University's Website](content/2011-10-22-improvements-for-my-universitys-website.md)
* 2013-12-09 — [How to use Jekyll with GitHub](content/2013-12-09-jekyll-and-git.md)
* 2014-12-30 — [Why I prefer Linux over Windows](content/2014-12-30-why-i-prefer-linux-over-windows.md)
* 2018-03-07 — [API Design](content/2018-03-07-api-design.md)
* 2019-05-18 — [REST](content/2019-05-18-rest-api.md)
* 2019-12-28 — [HTML Quantities](content/2019-12-28-html-quantities.md)

### Mathematics (1)

* 2016-07-15 — [Estimating Demand](content/2016-07-15-estimating-demand.md)

### Cyberculture (21)

* 2011-12-24 — [Adding a ppa in Ubuntu](content/2011-12-24-adding-a-ppa-in-ubuntu.md)
* 2012-01-27 — [Check Computer / Hardware for Linux-compatibility](content/2012-01-27-check-computer-hardware-for-linux-compatibility.md)
* 2012-06-13 — [Python one-liners for Project Euler](content/2012-06-13-python-one-liners-for-project-euler.md)
* 2012-10-13 — [Manipulating PDF files](content/2012-10-13-manipulating-pdf-files.md)
* 2013-03-04 — [Linux access rights and attributes](content/2013-03-04-linux-access-rights-and-attributes.md)
* 2013-03-06 — [Add a new font to ImageMagick](content/2013-03-06-add-a-new-font-to-imagemagick.md)
* 2013-05-21 — [Generating many prime numbers](content/2013-05-21-generating-many-prime-numbers.md)
* 2013-10-07 — [How to install Arch Linux 2013.10.01](content/2013-10-07-install-arch-linux-2013-10-01.md)
* 2014-01-24 — [SLURM](content/2014-01-24-slurm.md)
* 2014-03-06 — [Internet at KIT](content/2014-03-06-internet-at-kit.md)
* 2014-12-29 — [Don't lose your stuff](content/2014-12-29-dont-lose-your-stuff.md)
* 2015-06-07 — [Increase the maximum file upload size in PHP](content/2015-06-07-increase-maximum-upload-size-in-php.md)
* 2015-09-16 — [Rename Script](content/2015-09-16-rename-script.md)
* 2016-02-29 — [Get PDF pages](content/2016-02-29-get-pdf-pages.md)
* 2016-03-04 — [Disable Caps Lock](content/2016-03-04-disable-caps-lock.md)
* 2016-03-15 — [Paid Reviews](content/2016-03-15-paid-reviews.md)
* 2016-03-31 — [Microsoft Vision API](content/2016-03-31-microsoft-vision-api.md)
* 2016-11-12 — [Constants as Music](content/2016-11-12-constants-as-music.md)
* 2016-11-20 — [Colors in LaTeX](content/2016-11-20-colors-in-latex.md)
* 2018-12-30 — [Domain Registration](content/2018-12-30-domain-registration.md)
* 2021-05-17 — [How to use GPG](content/2021-05-17-gpg.md)

### My bits and bytes (21)

* 2012-03-28 — [How to install the latest LaTeX Version](content/2012-03-28-how-to-install-the-latest-latex-version.md)
* 2013-08-10 — [Improving lecture notes: Job (almost) done!](content/2013-08-10-improving-lecture-notes-job-almost-done.md)
* 2015-12-31 — [New Year 2016](content/2015-12-31-new-year-2016.md)
* 2016-05-17 — [Tools for Academia](content/2016-05-17-tools-for-academia.md)
* 2017-04-01 — [Extraordinary Materials](content/2017-04-01-extraordinary-materials.md)
* 2017-04-09 — [Master Thesis](content/2017-04-09-msthesis.md)
* 2018-02-20 — [German Language](content/2018-02-20-german-language.md)
* 2018-03-27 — [Prague](content/2018-03-27-prague.md)
* 2019-01-11 — [Airlines](content/2019-01-11-airlines.md)
* 2019-05-19 — [Computer Temperature](content/2019-05-19-computer-temperature.md)
* 2019-07-10 — [Movielens Data Set](content/2019-07-10-movielens.md)
* 2019-11-01 — [Fitness Trackers](content/2019-11-01-fitness-trackers.md)
* 2019-11-24 — [Scientific Writing](content/2019-11-24-scientific-writing.md)
* 2019-12-31 — [Citations with LaTeX](content/2019-12-31-citations-with-latex.md)
* 2019-12-31 — [Funny Machine Learning](content/2019-12-31-funny-recommendations.md)
* 2020-02-22 — [File Compression](content/2020-02-22-file-compression.md)
* 2020-03-10 — [Migrate to Python 3](content/2020-03-10-move-to-python3.md)
* 2020-07-05 — [Killer Features by Python Version](content/2020-07-05-python-killer-features.md)
* 2020-07-06 — [Medium](content/2020-07-06-medium.md)
* 2023-09-30 — [Abandoned domains are a security issue](content/2023-09-30-abandoned-domains.md)
* 2026-09-27 — [How I use AI on this blog](content/2026-09-27-how-i-use-ai.md)

### German posts (22)

* 2012-02-07 — [Wahrscheinlichkeitstheorie - Klausur (Info)](content/2012-02-07-wt-klausur.md)
* 2012-03-03 — [Briefe mit LaTeX schreiben](content/2012-03-03-briefe-mit-latex-schreiben.md)
* 2012-03-10 — [Abschlussaufgaben Programmieren](content/2012-03-10-abschlussaufgaben-programmieren.md)
* 2012-03-20 — [Wie bestimme ich das Inverse einer Matrix?](content/2012-03-20-wie-bestimme-ich-das-inverse-einer-matrix.md)
* 2012-04-15 — [Lernkontrolle: Lineare Algebra I](content/2012-04-15-lernkontrolle-lineare-algebra-i.md)
* 2012-04-26 — [LaTeX-Vorlage für ein Lastenheft](content/2012-04-26-latex-vorlage-fur-ein-lastenheft.md)
* 2012-06-04 — [LaTeX-Vorlage für den Semesterbericht der Studienstiftung](content/2012-06-04-latex-vorlage-fur-den-semesterbericht-der-studienstiftung.md)
* 2012-08-11 — [Entwurfsmuster-Beispiele](content/2012-08-11-entwurfsmuster-beispiele.md)
* 2012-09-10 — [Jordansche Normalform: 4x4 Matrizen](content/2012-09-10-jordansche-normalform-4x4-matrizen.md)
* 2012-09-15 — [Partielle Integration](content/2012-09-15-partielle-integration.md)
* 2012-11-19 — [Tribonacci-Folge](content/2012-11-19-tribonacci-folge.md)
* 2013-10-24 — [Programmierparadigmen Klausur](content/2013-10-24-programmierparadigmen-klausur.md)
* 2014-11-16 — [Formale Systeme Klausur](content/2014-11-16-formale-systeme.md)
* 2014-12-29 — [SVN am KIT](content/2014-12-29-svn-am-kit.md)
* 2014-12-30 — [Hörspiele](content/2014-12-30-horspiele.md)
* 2015-11-02 — [Wo ist Hörsaal 9 am KIT?](content/2015-11-02-wo-ist-hs9.md)
* 2017-01-15 — [Statistik - Klausur](content/2017-01-15-statistik-klausur.md)
* 2017-03-28 — [Abschlussbericht der Studienstiftung](content/2017-03-28-abschlussbericht-studienstiftung.md)
* 2023-12-31 — [Haus-Projekte](content/2023-12-31-haus-projekte.md)
* 2024-08-12 — [Food Processors](content/2024-08-12-food-processor.md)
* 2024-08-16 — [Stein](content/2024-08-16-stein.md)
* 2024-12-29 — [Stromzähler](content/2024-12-29-stromzaehler.md)

### Video posts (20)

Left without an image on purpose: they consist of an embedded video, which already
is the picture.

* 2011-09-21 — [Animator vs. Animation](content/2011-09-21-animater-vs-animation.md)
* 2011-09-21 — [Funny Commercials](content/2011-09-21-funny-commercials.md)
* 2011-09-26 — [Lolcats: Hermes' Favorite Activity](content/2011-09-26-lolcats-hermes-favorite-activity.md)
* 2011-09-28 — [10 Great Videos on Vimeo](content/2011-09-28-10-great-videos-on-vimeo.md)
* 2011-09-30 — [If Computer Problems Were Real](content/2011-09-30-if-computer-problems-were-real.md)
* 2011-10-04 — [Clip: What Light](content/2011-10-04-clip-what-light.md)
* 2011-10-22 — [Clip: Bob the Hamster](content/2011-10-22-bob-the-hamste.md)
* 2011-10-23 — [Clip: Love Tap](content/2011-10-23-clip-love-tap.md)
* 2011-10-28 — [DVD menu in YouTube](content/2011-10-28-dvd-menu-in-youtube.md)
* 2012-02-23 — [Portal - Still Alive typography clip](content/2012-02-23-portal-still-alive-typography-clip.md)
* 2012-02-24 — [Stuxnet](content/2012-02-24-stuxnet.md)
* 2012-03-12 — [Typography: Word as Image](content/2012-03-12-typography-word-as-image.md)
* 2012-07-01 — [George Carlin](content/2012-07-01-george-carlin.md)
* 2012-08-02 — [Nature by Numbers](content/2012-08-02-nature-by-numbers.md)
* 2012-08-02 — [Shortfilms, Part II](content/2012-08-02-shortfilms-part-ii.md)
* 2012-08-08 — [Short Educational Clips](content/2012-08-08-short-educational-clips.md)
* 2012-09-01 — [Nobel Prize in Physics 2009](content/2012-09-01-nobel-prize-in-physics-2009.md)
* 2012-10-15 — [Learning Java](content/2012-10-15-learning-java.md)
* 2012-12-22 — [Blender Open Movies](content/2012-12-22-blender-open-movies.md)
* 2013-06-30 — [Music videos](content/2013-06-30-music-videos.md)
