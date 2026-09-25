"""Pelican plugin: two gaps in render_math's Markdown handling.

* ``\\$`` is a literal dollar sign. render_math turns ``$…$`` into math before
  Markdown handles backslash escapes, so ``\\$10 and \\$14`` would otherwise become
  the formula ``10 and \\``. The escape is passed through unchanged and MathJax
  (``processEscapes``) shows it as ``$``.
* Inline math may contain an environment: ``$A = \\begin{pmatrix}…\\end{pmatrix}$``.
  render_math matches ``\\begin{…}…\\end{…}`` first, as display math, and splits the
  formula in two.
"""

from xml.etree.ElementTree import Element

from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.util import AtomicString
from pelican import signals

INLINE_MATH_WITH_ENVIRONMENT = r"(?<![\\$])\$(?!\$)(?P<math>[^$]*?\\begin\{[^$]*?)(?<![\s\\])\$(?!\$)"


class EscapedDollarProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        return AtomicString("\\$"), m.start(0), m.end(0)


class InlineMathWithEnvironmentProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        node = Element("span")
        node.set("class", "math")
        node.text = AtomicString("\\(" + m.group("math") + "\\)")
        return node, m.start(0), m.end(0)


class RenderMathFixesExtension(Extension):
    def extendMarkdown(self, md):
        # after code spans (190), before render_math (186 display, 185 inline)
        md.inlinePatterns.register(EscapedDollarProcessor(r"\\\$", md), "escaped_dollar", 188)
        md.inlinePatterns.register(
            InlineMathWithEnvironmentProcessor(INLINE_MATH_WITH_ENVIRONMENT, md),
            "inline_math_with_environment",
            187,
        )


def add_extension(pelican):
    pelican.settings["MARKDOWN"].setdefault("extensions", []).append(RenderMathFixesExtension())


def register():
    signals.initialized.connect(add_extension)
