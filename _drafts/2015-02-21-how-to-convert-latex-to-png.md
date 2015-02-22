---
layout: post
title: How to Convert LaTeX to PNG
author: Martin Thoma
date: 2014-11-22 17:19
categories: 
- Code
tags: 
- Python
- LaTeX
featured_image: logos/latex.png
---

I recently had to find a way to convert single-line LaTeX formulas to PNG.
To test it, I've used:

```text
\int x^a\,dx = \frac{x^{a+1}}{a+1} + C \qquad\text{(for } a\neq -1\text{)}\,\!
\bold H = \begin{bmatrix}
  \dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1\,\partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1\,\partial x_n} \\[2.2ex]
  \dfrac{\partial^2 f}{\partial x_2\,\partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2\,\partial x_n} \\[2.2ex]
  \vdots & \vdots & \ddots & \vdots \\[2.2ex]
  \dfrac{\partial^2 f}{\partial x_n\,\partial x_1} & \dfrac{\partial^2 f}{\partial x_n\,\partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}.
```


## Using a web service

Using another website for creating the PNG is probably the easiest way:

```python
    #!/usr/bin/env python

    import requests


    def formula_as_file(formula, file_path):
        """Contact a web service to convert ``formula`` into a PNG which will be
           stored in ``file_path.
        """
        url = "http://latex.codecogs.com/png.latex"
        r = requests.get('%s?\dpi{300} \huge %s' % (url, formula))
        with open(file_path, 'wb') as f:
            f.write(r.content)


    def main():
        """Run examples."""
        formulas = []
        formula = (r"\bold H = \begin{bmatrix}"
                   r"\dfrac{\partial^2 f}{\partial x_1^2} & "
                   r"\dfrac{\partial^2 f}{\partial x_1\,\partial x_2} & "
                   r"\cdots & "
                   r"\dfrac{\partial^2 f}{\partial x_1\,\partial x_n} \\[2.2ex]"
                   r"\dfrac{\partial^2 f}{\partial x_2\,\partial x_1} & "
                   r"\dfrac{\partial^2 f}{\partial x_2^2} & "
                   r"\cdots & "
                   r"\dfrac{\partial^2 f}{\partial x_2\,\partial x_n} \\[2.2ex]"
                   r"\vdots & \vdots & \ddots & \vdots \\[2.2ex]"
                   r"\dfrac{\partial^2 f}{\partial x_n\,\partial x_1} & "
                   r"\dfrac{\partial^2 f}{\partial x_n\,\partial x_2} & "
                   r"\cdots & \dfrac{\partial^2 f}{\partial x_n^2}"
                   r"\end{bmatrix}.")
        formulas.append(("hesse-matrix.png", formula))
        formula = (r"\int x^a\,dx = \frac{x^{a+1}}{a+1} + "
                   r"C \qquad\text{(for } a\neq -1\text{)}\,\!")
        formulas.append(("cavalieri-quadrature-formula.png", formula))
        for file_path, formula in formulas:
            formula_as_file(formula, file_path)

    if __name__ == '__main__':
        main()

```

However, this approach has two problems:

* You are dependant on somebody else.
  * You have a problem if the service gets down.
  * If the service changes the API, you have to adjust your code.
  * Your service gets slow when their service is slow.
  * If something doesn't work, you are not free to adjust it.
* The result is a PNG. This might not be the proper size for your document.

[mathurl.com](http://mathurl.com/) is a similar web service. They use
[mathtex](http://www.forkosh.com/mathtex.html).


## Using LaTeX

Another possibility is to let `pdflatex` render it and convert the pdf to a
svg.

LaTeX `formula.template.tex`:

```text
\documentclass[varwidth=true, border=2pt]{standalone}
\usepackage[utf8]{inputenc}

%Math packages
\usepackage{amsmath}
\usepackage{amssymb}

{{packages}}


%document
\begin{document}{{formula}}
\end{document}
```

and the Python code:

```python
#!/usr/bin/env python

import os


def formula_as_file(formula, file_path, packages=""):
    # assert file_path.endswith(".svg")
    with open("formula.template.tex") as f:
        template = f.read()

    template = template.replace("{{formula}}", formula)
    template = template.replace("{{packages}}", packages)
    print(template)

    with open("formulatmp.tex", "w") as f:
        f.write(template)

    os.system("pdflatex formulatmp.tex -output-format=pdf")
    os.system("pdf2svg formulatmp.pdf formulatmp.svg")
    os.system("inkscape formulatmp.svg -h 40 --export-png=%s" % file_path)


def main():
    """Run examples."""
    formulas = []
    formula = (r"\bold H = \begin{bmatrix}"
               r"\dfrac{\partial^2 f}{\partial x_1^2} & "
               r"\dfrac{\partial^2 f}{\partial x_1\,\partial x_2} & "
               r"\cdots & "
               r"\dfrac{\partial^2 f}{\partial x_1\,\partial x_n} \\[2.2ex]"
               r"\dfrac{\partial^2 f}{\partial x_2\,\partial x_1} & "
               r"\dfrac{\partial^2 f}{\partial x_2^2} & "
               r"\cdots & "
               r"\dfrac{\partial^2 f}{\partial x_2\,\partial x_n} \\[2.2ex]"
               r"\vdots & \vdots & \ddots & \vdots \\[2.2ex]"
               r"\dfrac{\partial^2 f}{\partial x_n\,\partial x_1} & "
               r"\dfrac{\partial^2 f}{\partial x_n\,\partial x_2} & "
               r"\cdots & \dfrac{\partial^2 f}{\partial x_n^2}"
               r"\end{bmatrix}.")
    formulas.append(("hesse-matrix.png", formula))
    formula = (r"\int x^a\,dx = \frac{x^{a+1}}{a+1} + "
               r"C \qquad\text{(for } a\neq -1\text{)}\,\!")
    formulas.append(("cavalieri-quadrature-formula.png", formula))
    for file_path, formula in formulas:
        formula_as_file(formula, file_path)

if __name__ == '__main__':
    main()

```


## MathTeX

[MathTeX](http://www.forkosh.com/mathtex.html) is a 6622 LOC pure C in a
single file monster. It requires a Linux system and LaTeX.


## PlasTeX

[PlasTeX](http://plastex.sourceforge.net/plastex/) seems to be a quite big
project.

MyRenderer.py:

```python
import string
from plasTeX.Renderers import Renderer


class Renderer(Renderer):
    def default(self, node):
        """ Rendering method for all non-text nodes """
        s = []

        # Handle characters like \&, \$, \%, etc.
        if len(node.nodeName) == 1 and node.nodeName not in string.letters:
            return self.textDefault(node.nodeName)

        # Start tag
        s.append('<%s>' % node.nodeName)

        # See if we have any attributes to render
        if node.hasAttributes():
            s.append('<attributes>')
            for key, value in node.attributes.items():
                # If the key is 'self', don't render it
                # these nodes are the same as the child nodes
                if key == 'self':
                    continue
                s.append('<%s>%s</%s>' % (key, unicode(value), key))
            s.append('</attributes>')

        # Invoke rendering on child nodes
        s.append(unicode(node))

        # End tag
        s.append('</%s>' % node.nodeName)

        return u'\n'.join(s)

    def textDefault(self, node):
        """ Rendering method for all text nodes """
        return node.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
```

main.py

```python
# Import renderer from first renderer example
from MyRenderer import Renderer

from plasTeX.TeX import TeX


def handle_equation(node):
    return u'<div><img src="%s"/></div>' % node.image.url

# Instantiate a TeX processor and parse the input text
tex = TeX()
tex.input(r'''
\documentclass{book}
\begin{document}

Previous paragraph.

\begin{equation}
\Sigma_{x=0}^{x+n} = \beta^2
\end{equation}

Next paragraph.

\end{document}
''')
document = tex.parse()

# Instantiate the renderer
renderer = Renderer()

# Insert the rendering method into all of the environments that might need it
renderer['equation'] = handle_equation
renderer['displaymath'] = handle_equation
renderer['eqnarray'] = handle_equation

# Render the document
renderer.render(document)
```

## PyX
[PyX](http://pyx.sourceforge.net/) seems to be dead. It is not on PyPI and the
last update was in 2013.