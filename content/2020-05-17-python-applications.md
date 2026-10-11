---
layout: post
title: Shipping Python Applications
slug: python-applications
lang: en
author: Martin Thoma
date: 2020-05-17 20:00
category: Code
tags: Python, Software Engineering, Packaging
featured_image: logos/star.png
status: draft
---
Publishing a Python *library* is well understood: build a wheel, upload it to
PyPI, done. Shipping an *application* to people who just want to run it is a
different problem. They might not have Python installed, or not the right
version, and they certainly don't want to deal with virtual environments.

There are three families of solutions, depending on what you can expect on the
target machine.


## Make it installable as a command

If the users are developers, the easiest way is still a normal package with an
entry point. In `pyproject.toml`:

```toml
[project.scripts]
mytool = "mytool.cli:main"
```

`mytool.cli:main` is a normal function:

```python
import sys


def main() -> int:
    print("Hello from mytool")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Users install it with [pipx](https://pipx.pypa.io/) or
[uv](https://docs.astral.sh/uv/guides/tools/), which put every tool into its own
virtual environment and the command on the `PATH`:

```text
pipx install mytool
uv tool install mytool
```

This needs Python on the target machine, but no knowledge about virtual
environments.


## One file that contains the dependencies

Python can run ZIP files that contain a `__main__.py`. That is the basis of
several tools that bundle an application and its dependencies into a single
file. The target machine still needs a Python interpreter.

**zipapp** is part of the standard library
([docs](https://docs.python.org/3/library/zipapp.html)):

```text
python -m pip install . --target build/
python -m zipapp build -m "mytool.cli:main" -p "/usr/bin/env python3" -o mytool.pyz
./mytool.pyz
```

It has one limitation: packages with compiled extensions can't be imported from
a ZIP file.

**[shiv](https://shiv.readthedocs.io/)** (by LinkedIn) builds the same kind of
file, but unpacks the dependencies into `~/.shiv/` on the first start, so
compiled extensions work:

```text
shiv -c mytool -o mytool.pyz .
```

**[pex](https://docs.pex-tool.org/)** provides a general-purpose Python
environment virtualization solution similar in spirit to virtualenv. PEX files
have been used by Twitter to deploy Python applications to production since
2011. It can also bundle wheels for several platforms into one file:

```text
pip install pex
pex -r requirements.txt -e modulename --python-shebang="/usr/bin/env python3" -o fooexecutable
```


## A real executable

If the users don't have Python, the interpreter has to be shipped as well.

**[PyInstaller](https://pyinstaller.org/)** collects the interpreter, your code
and all dependencies into a folder or a single executable:

```text
pyinstaller --onefile mytool/cli.py
```

The result is in `dist/`. PyInstaller doesn't cross-compile: you build the
Windows executable on Windows, the macOS one on macOS. A CI pipeline with one
job per operating system solves that. The single-file variant unpacks itself to
a temporary directory on every start, which makes it slower to start than the
folder variant.

**[Nuitka](https://nuitka.net/)** translates Python to C and compiles it. The
result is often a bit faster and harder to decompile:

```text
python -m nuitka --onefile mytool/cli.py
```

**[Briefcase](https://briefcase.readthedocs.io/)** (from the BeeWare project)
goes one step further and creates real installers: an MSI for Windows, a DMG
for macOS, AppImage/Flatpak or system packages for Linux, and even Android and
iOS apps.


## Which one to choose?

| Approach | Python needed on the target? | One file? | Compiled dependencies |
| -------- | ---------------------------- | --------- | --------------------- |
| pipx / uv tool | yes | no | yes |
| zipapp | yes | yes | no |
| shiv | yes | yes | yes (unpacked on first start) |
| pex | yes | yes | yes |
| PyInstaller | no | optional | yes, build per OS |
| Nuitka | no | optional | yes, build per OS |
| Briefcase | no | installer | yes, build per OS |

My rule of thumb:

* Developer tools: a package with an entry point, installed via pipx or uv.
* Deployment to servers you control: a container image, or pex/shiv if you
  don't want containers.
* Desktop applications for non-developers: Briefcase or PyInstaller.


## See also

* Python Packaging User Guide: [An Overview of Packaging for Python](https://packaging.python.org/en/latest/overview/)
* [Python Packaging Course](../python-packaging-course/)
