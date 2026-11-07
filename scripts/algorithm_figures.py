"""
Generate the SVG figures for the articles tagged "Algorithms".

Run from the repository root:

    python scripts/algorithm_figures.py            # all figures
    python scripts/algorithm_figures.py kadane     # only figures whose name contains "kadane"

Every SVG carries its own light and dark palette (prefers-color-scheme), as
described in AGENTS.md. The numbers in the figures (DP matrices, Kadane, the
Kalman simulation, ...) are computed here, not typed in.
"""

import math
import random
import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

FONT = (
    'ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, '
    '"Helvetica Neue", Arial, sans-serif'
)
MONO = 'ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace'

# name: (light, dark)
COLORS: Dict[str, Tuple[str, str]] = {
    "ink": ("#1c2320", "#e7ede9"),
    "muted": ("#5b6660", "#9aa8a0"),
    "faint": ("#9aa39e", "#6b756f"),
    "hair": ("#d4d7da", "#3a3d44"),
    "sunk": ("#ebebed", "#26282e"),
    "bg": ("#ffffff", "#1b1d22"),
    "acc": ("#1f7a45", "#4fc07d"),
    "soft": ("#e0efe6", "#1f3d2b"),
    "warn": ("#b35c00", "#f0a050"),
    "softwarn": ("#fbe9d7", "#4a3420"),
    "bad": ("#b3261e", "#f07a70"),
    "softbad": ("#f8dedc", "#4a2422"),
    "blue": ("#2a78d6", "#3987e5"),
    "softblue": ("#dbe8f8", "#1d3150"),
    # categorical series, fixed order (dataviz reference palette)
    "c1": ("#2a78d6", "#3987e5"),
    "c2": ("#eb6834", "#d95926"),
    "c3": ("#1baf7a", "#199e70"),
    "c4": ("#eda100", "#c98500"),
    "c5": ("#e87ba4", "#d55181"),
}
MARKER_COLORS = ["ink", "muted", "acc", "warn", "bad", "blue"]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def num(x: float) -> str:
    return f"{x:.1f}".rstrip("0").rstrip(".")


class Svg:
    def __init__(self, width: int, height: int, title: str, desc: str):
        self.width = width
        self.height = height
        self.title = title
        self.desc = desc
        self.items: List[str] = []
        self.defs: List[str] = []

    # --- primitives -------------------------------------------------------
    @staticmethod
    def _cls(fill: Optional[str], stroke: Optional[str]) -> str:
        parts = []
        if fill:
            parts.append(f"f-{fill}")
        if stroke:
            parts.append(f"s-{stroke}")
        return " ".join(parts)

    def _paint(self, fill: Optional[str], stroke: Optional[str], sw: float) -> str:
        attrs = f'class="{self._cls(fill, stroke)}"'
        if not fill:
            attrs += ' fill="none"'
        if stroke:
            attrs += f' stroke-width="{num(sw)}"'
        return attrs

    def rect(self, x, y, w, h, fill=None, stroke=None, sw=1.5, rx=0, extra=""):
        self.items.append(
            f'<rect x="{num(x)}" y="{num(y)}" width="{num(w)}" height="{num(h)}" '
            f'rx="{num(rx)}" {self._paint(fill, stroke, sw)} {extra}/>'
        )

    def circle(self, cx, cy, r, fill=None, stroke=None, sw=1.5, extra=""):
        self.items.append(
            f'<circle cx="{num(cx)}" cy="{num(cy)}" r="{num(r)}" '
            f"{self._paint(fill, stroke, sw)} {extra}/>"
        )

    def line(self, x1, y1, x2, y2, stroke="ink", sw=2, arrow=False, dash=None, extra=""):
        marker = f' marker-end="url(#m-{stroke})"' if arrow else ""
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<line x1="{num(x1)}" y1="{num(y1)}" x2="{num(x2)}" y2="{num(y2)}" '
            f'class="s-{stroke}" stroke-width="{num(sw)}" stroke-linecap="round"'
            f"{dash_attr}{marker} {extra}/>"
        )

    def path(self, d, fill=None, stroke="ink", sw=2, arrow=False, dash=None, extra=""):
        marker = f' marker-end="url(#m-{stroke})"' if arrow and stroke else ""
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<path d="{d}" {self._paint(fill, stroke, sw)} stroke-linecap="round" '
            f'stroke-linejoin="round"{dash_attr}{marker} {extra}/>'
        )

    def text(
        self,
        x,
        y,
        s,
        size=15,
        fill="ink",
        anchor="start",
        weight=None,
        mono=False,
        italic=False,
        extra="",
    ):
        """Text that is vertically centred on y."""
        attrs = [
            f'x="{num(x)}"',
            f'y="{num(y)}"',
            f'class="f-{fill}{" mono" if mono else ""}"',
            f'font-size="{size}"',
            'dominant-baseline="central"',
        ]
        if anchor != "start":
            attrs.append(f'text-anchor="{anchor}"')
        if weight:
            attrs.append(f'font-weight="{weight}"')
        if italic:
            attrs.append('font-style="italic"')
        self.items.append(f"<text {' '.join(attrs)} {extra}>{esc(s)}</text>")

    def rich(self, x, y, parts, size=15, anchor="start", mono=False):
        """parts: list of (text, color, bold)."""
        spans = "".join(
            f'<tspan class="f-{c}"{" font-weight=\"700\"" if b else ""}>{esc(t)}</tspan>'
            for t, c, b in parts
        )
        anchor_attr = f' text-anchor="{anchor}"' if anchor != "start" else ""
        self.items.append(
            f'<text x="{num(x)}" y="{num(y)}" font-size="{size}" '
            f'dominant-baseline="central"{anchor_attr}'
            f'{" class=\"mono\"" if mono else ""} xml:space="preserve">{spans}</text>'
        )

    def raw(self, s: str):
        self.items.append(s)

    # --- output -----------------------------------------------------------
    def css(self) -> str:
        light = []
        dark = []
        for name, (lc, dc) in COLORS.items():
            light.append(f".f-{name}{{fill:{lc}}}.s-{name}{{stroke:{lc}}}")
            dark.append(f".f-{name}{{fill:{dc}}}.s-{name}{{stroke:{dc}}}")
        return (
            f"text{{font-family:{FONT}}}.mono,.mono tspan{{font-family:{MONO}}}\n"
            + "\n".join(light)
            + "\n@media (prefers-color-scheme: dark){\n"
            + "\n".join(dark)
            + "\n}"
        )

    def render(self) -> str:
        markers = "".join(
            f'<marker id="m-{c}" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" '
            f'orient="auto-start-reverse"><path class="f-{c}" d="M0 0 L10 5 L0 10 z"/></marker>'
            for c in MARKER_COLORS
        )
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="{self.width}" height="{self.height}" role="img" aria-labelledby="t d">\n'
            f'<title id="t">{esc(self.title)}</title>\n'
            f'<desc id="d">{esc(self.desc)}</desc>\n'
            f"<style>\n{self.css()}\n</style>\n"
            f"<defs>{markers}{''.join(self.defs)}</defs>\n"
            + "\n".join(self.items)
            + "\n</svg>\n"
        )


def arrow_between(svg: Svg, p, q, r1, r2, stroke="ink", sw=2, dash=None):
    """Arrow from circle around p (radius r1) to circle around q (radius r2)."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    svg.line(
        p[0] + ux * r1,
        p[1] + uy * r1,
        q[0] - ux * (r2 + 2),
        q[1] - uy * (r2 + 2),
        stroke=stroke,
        sw=sw,
        arrow=True,
        dash=dash,
    )


def tree_positions(children: Dict[str, List[str]], root: str, x0, x1, y0, dy):
    """Leaves evenly spread from x0 to x1, inner nodes centred over children."""
    leaves: List[str] = []

    def collect(n):
        if not children.get(n):
            leaves.append(n)
        for c in children.get(n, []):
            collect(c)

    collect(root)
    gap = (x1 - x0) / max(len(leaves) - 1, 1)
    pos = {}

    def place(n, depth):
        if not children.get(n):
            x = x0 + leaves.index(n) * gap
        else:
            xs = [place(c, depth + 1) for c in children[n]]
            x = (min(xs) + max(xs)) / 2
        pos[n] = (x, y0 + depth * dy)
        return x

    place(root, 0)
    return pos


# ---------------------------------------------------------------------------
# Project Euler 26: long division of 1/7
# ---------------------------------------------------------------------------
def project_euler_26() -> Svg:
    q = 7
    steps = []  # (dividend, digit, rest)
    seen = {}
    rest = 1
    while rest not in seen:
        seen[rest] = len(steps)
        dividend = rest * 10
        steps.append((dividend, dividend // q, dividend % q, rest))
        rest = dividend % q
    remainders = [s[3] for s in steps]
    digits = "".join(str(s[1]) for s in steps)

    svg = Svg(
        680,
        380,
        "Long division of 1/7 and its cycle of remainders",
        f"Dividing 1 by 7 by hand gives the remainders {', '.join(map(str, remainders))} "
        f"and then remainder 1 again. From there on, the digits {digits} repeat. "
        "The remainders form a cycle; each arrow is labelled with the digit it produces.",
    )
    svg.text(30, 36, "1 ÷ 7 with pen and paper", size=15, fill="muted")
    y = 76
    for dividend, digit, rest, _ in steps:
        svg.rich(
            30,
            y,
            [
                (f"{dividend:>2} = ", "ink", False),
                (str(digit), "acc", True),
                (f" · {q} + ", "ink", False),
                (str(rest), "warn", True),
            ],
            size=17,
            mono=True,
        )
        y += 36
    svg.text(190, y - 36, "← remainder 1 again", size=14, fill="muted")
    svg.rich(
        30,
        y + 16,
        [("1/7 = 0.", "ink", False), (digits, "acc", True), (" ", "ink", False),
         (digits, "acc", True), (" …", "ink", False)],
        size=17,
        mono=True,
    )

    cx, cy, radius, node_r = 505, 185, 118, 24
    pts = []
    for i in range(len(remainders)):
        a = math.radians(-90 + 360 / len(remainders) * i)
        pts.append((cx + radius * math.cos(a), cy + radius * math.sin(a)))
    for i in range(len(pts)):
        p, nxt = pts[i], pts[(i + 1) % len(pts)]
        arrow_between(svg, p, nxt, node_r, node_r, stroke="muted", sw=2)
        mx, my = (p[0] + nxt[0]) / 2, (p[1] + nxt[1]) / 2
        ox, oy = mx - cx, my - cy
        d = math.hypot(ox, oy)
        svg.text(mx + ox / d * 20, my + oy / d * 20, digits[i], size=18, fill="acc",
                 anchor="middle", weight="700")
    for p, r in zip(pts, remainders):
        svg.circle(p[0], p[1], node_r, fill="softwarn", stroke="warn", sw=2)
        svg.text(p[0], p[1], str(r), size=18, anchor="middle", weight="700")
    svg.text(cx, cy - 10, "remainders", size=14, fill="warn", anchor="middle")
    svg.text(cx, cy + 12, "arrows: digits", size=14, fill="acc", anchor="middle")
    return svg


# ---------------------------------------------------------------------------
# Landau symbols: growth of common functions
# ---------------------------------------------------------------------------
def landau_growth() -> Svg:
    svg = Svg(
        640,
        420,
        "Wachstum typischer Laufzeitfunktionen",
        "Die Funktionen log₂ n, n, n·log₂ n, n² und 2ⁿ für n von 1 bis 20. "
        "2ⁿ verlässt das Diagramm schon bei n ≈ 6.6, n² bei n = 10, "
        "n·log₂ n erreicht bei n = 20 etwa 86, n erreicht 20 und log₂ n nur etwa 4.3.",
    )
    x0, x1, y0, y1 = 64, 540, 34, 364
    n_max, f_max = 20, 100

    def px(n):
        return x0 + (x1 - x0) * n / n_max

    def py(v):
        return y1 - (y1 - y0) * v / f_max

    for v in range(0, f_max + 1, 25):
        svg.line(x0, py(v), x1, py(v), stroke="hair", sw=1)
        svg.text(x0 - 10, py(v), str(v), size=13, fill="muted", anchor="end")
    for n in range(0, n_max + 1, 5):
        svg.text(px(n), y1 + 18, str(n), size=13, fill="muted", anchor="middle")
    svg.line(x0, y1, x1, y1, stroke="muted", sw=1.5)
    svg.text((x0 + x1) / 2, y1 + 42, "Eingabegröße n", size=14, fill="muted", anchor="middle")
    svg.text(x0 - 10, y0 - 20, "f(n)", size=14, fill="muted", anchor="end")

    svg.defs.append(
        f'<clipPath id="plot"><rect x="{x0}" y="{y0 - 2}" width="{x1 - x0 + 2}" '
        f'height="{y1 - y0 + 2}"/></clipPath>'
    )
    series = [
        ("log₂ n", "c1", lambda n: math.log2(n)),
        ("n", "c2", lambda n: n),
        ("n · log₂ n", "c3", lambda n: n * math.log2(n)),
        ("n²", "c4", lambda n: n * n),
        ("2ⁿ", "c5", lambda n: 2**n),
    ]
    for label, color, f in series:
        pts = []
        n = 1.0
        while n <= n_max + 1e-9:
            v = f(n)
            pts.append((px(n), py(min(v, f_max * 1.2))))
            if v > f_max * 1.2:
                break
            n += 0.05
        d = "M" + " L".join(f"{num(x)} {num(y)}" for x, y in pts)
        svg.path(d, stroke=color, sw=2.5, extra='clip-path="url(#plot)"')
        if f(n_max) <= f_max:
            svg.text(x1 + 10, py(f(n_max)), label, size=15, anchor="start")
        else:
            # where the curve leaves the plot
            lo, hi = 1.0, float(n_max)
            for _ in range(50):
                mid = (lo + hi) / 2
                lo, hi = (mid, hi) if f(mid) < f_max else (lo, mid)
            svg.text(px(lo), y0 - 14, label, size=15, anchor="middle")
    return svg


# ---------------------------------------------------------------------------
# Point in polygon: triangulation
# ---------------------------------------------------------------------------
def _cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def _in_triangle(p, a, b, c):
    d1, d2, d3 = _cross(a, b, p), _cross(b, c, p), _cross(c, a, p)
    neg = d1 < 0 or d2 < 0 or d3 < 0
    pos = d1 > 0 or d2 > 0 or d3 > 0
    return not (neg and pos)


def ear_clipping(poly):
    pts = list(range(len(poly)))
    area = sum(_cross((0, 0), poly[i], poly[(i + 1) % len(poly)]) for i in pts)
    sign = 1 if area > 0 else -1
    triangles = []
    while len(pts) > 3:
        for k in range(len(pts)):
            i, j, l = pts[k - 1], pts[k], pts[(k + 1) % len(pts)]
            a, b, c = poly[i], poly[j], poly[l]
            if sign * _cross(a, b, c) <= 0:
                continue  # reflex corner
            if any(_in_triangle(poly[m], a, b, c) for m in pts if m not in (i, j, l)):
                continue
            triangles.append((i, j, l))
            pts.pop(k)
            break
        else:
            raise ValueError("polygon is not simple")
    triangles.append(tuple(pts))
    return triangles


def polygon_triangulation() -> Svg:
    poly = [(50, 280), (170, 330), (330, 300), (440, 200), (330, 160),
            (390, 50), (220, 95), (120, 40), (70, 150)]
    p = (255, 225)
    triangles = ear_clipping(poly)
    svg = Svg(
        480,
        370,
        "A polygon split into triangles",
        f"A non-convex polygon with {len(poly)} corners, split into {len(triangles)} "
        "triangles along dashed diagonals. The point P lies in exactly one of them, which "
        "is highlighted. Checking a triangle takes constant time.",
    )
    hit = None
    for t in triangles:
        a, b, c = (poly[i] for i in t)
        inside = _in_triangle(p, a, b, c)
        if inside:
            hit = t
        d = f"M{a[0]} {a[1]} L{b[0]} {b[1]} L{c[0]} {c[1]} Z"
        svg.path(d, fill="soft" if inside else "sunk", stroke="muted", sw=1.2, dash="5 4")
    outline = "M" + " L".join(f"{x} {y}" for x, y in poly) + " Z"
    svg.path(outline, stroke="ink", sw=2.5)
    a, b, c = (poly[i] for i in hit)
    svg.path(f"M{a[0]} {a[1]} L{b[0]} {b[1]} L{c[0]} {c[1]} Z", stroke="acc", sw=2.5)
    for i, (x, y) in enumerate(poly, start=1):
        svg.circle(x, y, 4, fill="ink")
    svg.circle(p[0], p[1], 6, fill="acc")
    svg.text(p[0] + 12, p[1] - 4, "P", size=18, weight="700", fill="acc")
    return svg


# ---------------------------------------------------------------------------
# Levenshtein / WER matrix
# ---------------------------------------------------------------------------
OPS = {
    "match": ("soft", "acc", "match"),
    "sub": ("softwarn", "warn", "substitution"),
    "ins": ("softblue", "blue", "insertion"),
    "del": ("softbad", "bad", "deletion"),
}


def levenshtein(r: Sequence[str], h: Sequence[str]):
    d = [[0] * (len(h) + 1) for _ in range(len(r) + 1)]
    for i in range(len(r) + 1):
        d[i][0] = i
    for j in range(len(h) + 1):
        d[0][j] = j
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i - 1][j - 1], d[i][j - 1], d[i - 1][j])
    # backtrace
    i, j = len(r), len(h)
    path = {(i, j): None}
    ops = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and r[i - 1] == h[j - 1] and d[i][j] == d[i - 1][j - 1]:
            op = "match"
            ni, nj = i - 1, j - 1
        elif i > 0 and j > 0 and d[i][j] == d[i - 1][j - 1] + 1:
            op = "sub"
            ni, nj = i - 1, j - 1
        elif j > 0 and d[i][j] == d[i][j - 1] + 1:
            op = "ins"
            ni, nj = i, j - 1
        else:
            op = "del"
            ni, nj = i - 1, j
        path[(i, j)] = op
        ops.append((op, r[i - 1] if op != "ins" else None, h[j - 1] if op != "del" else None))
        i, j = ni, nj
    path[(0, 0)] = None
    return d, path, ops[::-1]


def dp_matrix(r, h, cell_w, cell_h, title, desc, ref_label, hyp_label, token_size,
              summary: Callable[[int, int], str]) -> Svg:
    d, path, ops = levenshtein(r, h)
    label_w = cell_w
    x0, y0 = 40 + label_w, 66
    grid_w = (len(h) + 1) * cell_w
    grid_h = (len(r) + 1) * cell_h
    align_y = y0 + grid_h + 52
    legend_y = align_y + 3 * 30 + 20
    col_w = max(cell_w, 20 + token_size * 0.62 * max(len(t) for t in list(r) + list(h)))
    ax0 = 40 + 50
    summary_text = summary(sum(1 for op, _, _ in ops if op != "match"), len(r))
    width = max(x0 + grid_w + 40, ax0 + len(ops) * col_w + 16 + len(summary_text) * 8.2 + 24)
    svg = Svg(int(width), int(legend_y + 30), title, desc)

    svg.text(x0 + grid_w / 2, 22, f"{hyp_label} →", size=14, fill="muted", anchor="middle")
    svg.text(24, y0 + cell_h + (grid_h - cell_h) / 2, f"{ref_label} ↓", size=14,
             fill="muted", anchor="middle", extra=f'transform="rotate(-90 24 {num(y0 + cell_h + (grid_h - cell_h) / 2)})"')
    for j, tok in enumerate([""] + list(h)):
        svg.text(x0 + j * cell_w + cell_w / 2, y0 - 18, tok, size=token_size, anchor="middle",
                 weight="600")
    for i, tok in enumerate([""] + list(r)):
        svg.text(x0 - 10, y0 + i * cell_h + cell_h / 2, tok, size=token_size, anchor="end",
                 weight="600")
    for i in range(len(r) + 1):
        for j in range(len(h) + 1):
            x, y = x0 + j * cell_w, y0 + i * cell_h
            op = path.get((i, j), "none")
            if op == "none":
                fill = None
            elif op is None:
                fill = "soft"
            else:
                fill = OPS[op][0]
            svg.rect(x, y, cell_w, cell_h, fill=fill, stroke="hair", sw=1)
            on_path = (i, j) in path
            svg.text(x + cell_w / 2, y + cell_h / 2, str(d[i][j]), size=16,
                     anchor="middle", weight="700" if on_path else None,
                     fill="ink" if on_path else "muted")
    # path arrows (from cell to predecessor, drawn forward)
    cells = sorted(path)
    for (i, j) in cells:
        op = path[(i, j)]
        if op is None:
            continue
        pi, pj = (i - 1, j - 1) if op in ("match", "sub") else ((i, j - 1) if op == "ins" else (i - 1, j))
        ax = x0 + pj * cell_w + cell_w / 2
        ay = y0 + pi * cell_h + cell_h / 2
        bx = x0 + j * cell_w + cell_w / 2
        by = y0 + i * cell_h + cell_h / 2
        dx, dy = bx - ax, by - ay
        dist = math.hypot(dx, dy)
        sx, sy = ax + dx / dist * 13, ay + dy / dist * 13
        ex, ey = bx - dx / dist * 14, by - dy / dist * 14
        svg.line(sx, sy, ex, ey, stroke=OPS[op][1], sw=1.8, arrow=True)

    # alignment
    svg.text(40, align_y, ref_label, size=13, fill="muted")
    svg.text(40, align_y + 30, hyp_label, size=13, fill="muted")
    for k, (op, rt, ht) in enumerate(ops):
        cx = ax0 + k * col_w + col_w / 2
        fill, stroke, _ = OPS[op]
        svg.rect(cx - col_w / 2 + 2, align_y - 14, col_w - 4, 58, fill=fill, rx=4)
        svg.text(cx, align_y, rt if rt is not None else "–", size=token_size, anchor="middle",
                 fill="ink" if rt is not None else "faint")
        svg.text(cx, align_y + 30, ht if ht is not None else "–", size=token_size,
                 anchor="middle", fill="ink" if ht is not None else "faint")
        if op != "match":
            svg.text(cx, align_y + 58, {"sub": "S", "ins": "I", "del": "D"}[op], size=14,
                     anchor="middle", weight="700", fill=stroke)
    svg.text(ax0 + len(ops) * col_w + 16, align_y + 15, summary_text, size=15,
             fill="ink")

    x = 40
    for key in ("match", "sub", "ins", "del"):
        fill, stroke, label = OPS[key]
        svg.rect(x, legend_y - 8, 16, 16, fill=fill, stroke=stroke, sw=1.5, rx=3)
        svg.text(x + 22, legend_y, label, size=13, fill="muted")
        x += 34 + len(label) * 7.5
    return svg


def wer_matrix() -> Svg:
    ref = "what a bright day".split()
    hyp = "what the bright sunny day".split()
    return dp_matrix(
        ref, hyp, 74, 38,
        "Word error rate: Levenshtein matrix and alignment",
        "The Levenshtein matrix for the reference 'what a bright day' and the hypothesis "
        "'what the bright sunny day'. The cheapest path through the matrix keeps 'what', "
        "substitutes 'a' by 'the', keeps 'bright', inserts 'sunny' and keeps 'day'. "
        "Two errors on four reference words give a WER of 50%.",
        "REF", "HYP", 15,
        lambda e, n: f"WER = {e}/{n} = {100 * e // n}%",
    )


def edit_distance_matrix() -> Svg:
    return dp_matrix(
        list("kitten"), list("sitting"), 44, 36,
        "Edit distance matrix of kitten and sitting",
        "The matrix d for the edit distance between 'kitten' and 'sitting'. Each cell is the "
        "edit distance of two prefixes. The highlighted path substitutes k by s, keeps i, t, t, "
        "substitutes e by i, keeps n and inserts g: an edit distance of 3.",
        "w1", "w2", 16,
        lambda e, n: f"edit distance = {e}",
    )


# ---------------------------------------------------------------------------
# Label correction: the graph of sample_1()
# ---------------------------------------------------------------------------
def label_correction_graph() -> Svg:
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("C", "G"),
             ("D", "H"), ("D", "I"), ("E", "J"), ("G", "K"), ("H", "L"), ("J", "M")]
    children: Dict[str, List[str]] = {}
    for a, b in edges:
        children.setdefault(a, []).append(b)
    pos = tree_positions(children, "A", 50, 510, 36, 70)
    path = {("A", "C"), ("C", "F")}
    svg = Svg(
        560,
        360,
        "The search graph of sample_1",
        "An undirected graph with the nodes A to M where every edge has weight 1: "
        "A–B, A–C, B–D, B–E, C–F, C–G, D–H, D–I, E–J, G–K, H–L and J–M. "
        "The search goes from the start A to the target F; the shortest path A–C–F "
        "has length 2.",
    )
    for a, b in edges:
        on = (a, b) in path
        svg.line(*pos[a], *pos[b], stroke="acc" if on else "muted", sw=3 if on else 1.8)
    for n, (x, y) in pos.items():
        if n == "A":
            fill, stroke = "softblue", "blue"
        elif n == "F":
            fill, stroke = "soft", "acc"
        else:
            fill, stroke = "bg", "muted"
        svg.circle(x, y, 18, fill=fill, stroke=stroke, sw=2)
        svg.text(x, y, n, size=16, anchor="middle", weight="700")
    ax, ay = pos["A"]
    svg.text(ax + 26, ay, "start", size=14, fill="blue")
    fx, fy = pos["F"]
    svg.text(fx, fy + 32, "target", size=14, fill="acc", anchor="middle")
    return svg


# ---------------------------------------------------------------------------
# Kadane's algorithm
# ---------------------------------------------------------------------------
def kadane() -> Svg:
    nums = [9, -5, -5, -2, 1, 2, -1, 4, 5, 0, 1]
    current, best = [], []
    cur, mx = 0, float("-inf")
    start = best_l = best_r = 0
    restarts = []
    for i, v in enumerate(nums):
        if v > cur + v:
            cur = v
            start = i
            restarts.append(i)
        else:
            cur = cur + v
        if cur > mx:
            mx = cur
            best_l, best_r = start, i
        current.append(cur)
        best.append(mx)

    svg = Svg(
        660,
        400,
        "Kadane's algorithm on an example array",
        f"Bars show the array {nums}. The maximum subarray goes from index {best_l} to "
        f"{best_r} and has the sum {mx}. Below, the table lists current_sum and max_sum "
        "after each element. current_sum restarts at index "
        f"{', '.join(map(str, restarts[1:]))} because the element alone is bigger than "
        "the running sum plus the element.",
    )
    x0, bar_w, gap = 130, 40, 8
    zero_y, scale = 150, 9.5
    for i, v in enumerate(nums):
        x = x0 + i * (bar_w + gap)
        in_best = best_l <= i <= best_r
        top = zero_y - max(v, 0) * scale
        h = abs(v) * scale
        if h:
            svg.rect(x, top, bar_w, h, fill="acc" if in_best else "faint", rx=3)
        label_y = top - 12 if v >= 0 else zero_y + h + 12
        svg.text(x + bar_w / 2, label_y, str(v), size=14, anchor="middle")
        svg.text(x + bar_w / 2, 236, str(i), size=12, fill="muted", anchor="middle")
    x_end = x0 + len(nums) * (bar_w + gap) - gap
    svg.line(x0 - 6, zero_y, x_end + 6, zero_y, stroke="muted", sw=1.5)
    svg.text(x0 - 16, 236, "index", size=12, fill="muted", anchor="end")
    svg.text(x0 - 16, zero_y, "nums", size=14, fill="muted", anchor="end")
    bl = x0 + best_l * (bar_w + gap)
    br = x0 + best_r * (bar_w + gap) + bar_w
    svg.path(f"M{bl} 52 L{bl} 44 L{br} 44 L{br} 52", stroke="acc", sw=2)
    svg.text((bl + br) / 2, 28, f"maximum subarray: sum = {mx}", size=15, anchor="middle",
             weight="700")

    rows = [("current_sum", current, "ink"), ("max_sum", best, "ink")]
    y = 280
    for label, values, color in rows:
        svg.text(x0 - 16, y, label, size=14, fill="muted", anchor="end", mono=True)
        for i, v in enumerate(values):
            x = x0 + i * (bar_w + gap)
            hl = label == "current_sum" and i in restarts[1:]
            if hl:
                svg.rect(x + 2, y - 14, bar_w - 4, 28, fill="softwarn", stroke="warn", sw=1.5, rx=4)
            svg.text(x + bar_w / 2, y, str(v), size=15, anchor="middle", fill=color,
                     weight="700" if hl else None)
        y += 40
    r = restarts[1]
    rx = x0 + r * (bar_w + gap) + bar_w / 2
    svg.text(rx, y + 6, "↑ restart: nums[i] > current_sum + nums[i]", size=13, fill="warn",
             anchor="start", extra=f'dx="-6"')
    return svg


# ---------------------------------------------------------------------------
# Dynamic programming: Fibonacci call tree
# ---------------------------------------------------------------------------
def fibonacci_call_tree() -> Svg:
    n = 5
    children: Dict[str, List[str]] = {}
    labels: Dict[str, int] = {}
    counter = [0]

    def build(k):
        node = f"n{counter[0]}"
        counter[0] += 1
        labels[node] = k
        if k > 1:
            children[node] = [build(k - 1), build(k - 2)]
        return node

    root = build(n)
    # status with memoization, evaluating f(n-1) before f(n-2)
    status: Dict[str, str] = {}
    known = set()

    def evaluate(node, pruned):
        k = labels[node]
        if pruned:
            status[node] = "pruned"
            for c in children.get(node, []):
                evaluate(c, True)
            return
        if k in known:
            status[node] = "cached"
            for c in children.get(node, []):
                evaluate(c, True)
            return
        status[node] = "computed"
        for c in children.get(node, []):
            evaluate(c, False)
        known.add(k)

    evaluate(root, False)
    pos = tree_positions(children, root, 40, 620, 36, 62)
    computed = sum(1 for s in status.values() if s == "computed")
    cached = sum(1 for s in status.values() if s == "cached")
    svg = Svg(
        660,
        380,
        f"Call tree of the recursive Fibonacci function for f({n})",
        f"The naive recursion for f({n}) makes {len(labels)} calls. Many of them repeat: "
        f"f(3) is computed twice, f(2) three times. With memoization only {computed} calls "
        f"compute something, {cached} calls return a stored result, and the grey subtrees "
        "below them are never called.",
    )
    for node, kids in children.items():
        for c in kids:
            pruned = status[c] == "pruned"
            svg.line(*pos[node], *pos[c], stroke="faint" if pruned else "muted",
                     sw=1.5, dash="4 4" if pruned else None)
    style = {
        "computed": ("soft", "acc", "ink"),
        "cached": ("softwarn", "warn", "ink"),
        "pruned": ("bg", "faint", "faint"),
    }
    for node, (x, y) in pos.items():
        fill, stroke, ink = style[status[node]]
        svg.rect(x - 24, y - 15, 48, 30, fill=fill, stroke=stroke, sw=2, rx=15,
                 extra='stroke-dasharray="4 3"' if status[node] == "pruned" else "")
        svg.text(x, y, f"f({labels[node]})", size=14, anchor="middle", weight="600", fill=ink)
    ly = 352
    x = 40
    for key, label in [("computed", "computed once"), ("cached", "result from the cache"),
                       ("pruned", "never called with memoization")]:
        fill, stroke, _ = style[key]
        svg.rect(x, ly - 9, 30, 18, fill=fill, stroke=stroke, sw=2, rx=9,
                 extra='stroke-dasharray="4 3"' if key == "pruned" else "")
        svg.text(x + 38, ly, label, size=13, fill="muted")
        x += 60 + len(label) * 7.2
    return svg


# ---------------------------------------------------------------------------
# Kalman filter: 1D tracking
# ---------------------------------------------------------------------------
def kalman_1d() -> Svg:
    rng = random.Random(7)
    steps = 50
    sigma_m = 4.0
    truth, meas = [], []
    x, v = 0.0, 1.0
    for _ in range(steps):
        v += rng.gauss(0, 0.15)
        x += v
        truth.append(x)
        meas.append(x + rng.gauss(0, sigma_m))
    # constant-velocity Kalman filter, state (position, velocity)
    q = 0.06**2
    r = sigma_m**2
    est = []
    s = [meas[0], 0.0]
    p = [[r, 0.0], [0.0, 4.0]]
    for k, z in enumerate(meas):
        if k > 0:
            # predict: x = A x, P = A P A^T + Q with A = [[1, 1], [0, 1]]
            s = [s[0] + s[1], s[1]]
            p00 = p[0][0] + p[0][1] + p[1][0] + p[1][1]
            p01 = p[0][1] + p[1][1]
            p10 = p[1][0] + p[1][1]
            p11 = p[1][1] + q
            p = [[p00 + q / 4, p01 + q / 2], [p10 + q / 2, p11]]
            # update with H = [1, 0]
            y = z - s[0]
            S = p[0][0] + r
            k0, k1 = p[0][0] / S, p[1][0] / S
            s = [s[0] + k0 * y, s[1] + k1 * y]
            p = [[(1 - k0) * p[0][0], (1 - k0) * p[0][1]],
                 [p[1][0] - k1 * p[0][0], p[1][1] - k1 * p[0][1]]]
        est.append(s[0])

    rmse_m = math.sqrt(sum((a - b) ** 2 for a, b in zip(meas, truth)) / steps)
    rmse_e = math.sqrt(sum((a - b) ** 2 for a, b in zip(est[5:], truth[5:])) / (steps - 5))
    svg = Svg(
        640,
        400,
        "A Kalman filter tracking a position from noisy measurements",
        f"Simulated one-dimensional tracking over {steps} time steps. The true position "
        f"rises with a slowly changing speed. The measurements scatter around it with a "
        f"standard deviation of {sigma_m:g}. The Kalman filter estimate with a constant-velocity "
        f"model follows the true position closely: its root mean squared error is about "
        f"{rmse_e:.1f} after the first steps, compared to {rmse_m:.1f} for the raw measurements.",
    )
    x0, x1, y0, y1 = 64, 610, 70, 350
    lo = math.floor(min(meas + truth) / 10) * 10
    hi = math.ceil(max(meas + truth) / 10) * 10

    def px(k):
        return x0 + (x1 - x0) * k / (steps - 1)

    def py(val):
        return y1 - (y1 - y0) * (val - lo) / (hi - lo)

    tick = 20 if hi - lo > 80 else 10
    t = lo
    while t <= hi:
        svg.line(x0, py(t), x1, py(t), stroke="hair", sw=1)
        svg.text(x0 - 10, py(t), str(t), size=13, fill="muted", anchor="end")
        t += tick
    for k in range(0, steps, 10):
        svg.text(px(k), y1 + 18, str(k), size=13, fill="muted", anchor="middle")
    svg.text((x0 + x1) / 2, y1 + 40, "time step k", size=14, fill="muted", anchor="middle")
    svg.text(x0 - 10, y0 - 14, "position", size=14, fill="muted", anchor="end")

    def poly(vals):
        return "M" + " L".join(f"{num(px(k))} {num(py(v))}" for k, v in enumerate(vals))

    svg.path(poly(truth), stroke="ink", sw=2, dash="6 5")
    for k, m in enumerate(meas):
        svg.circle(px(k), py(m), 4, fill="c2", stroke="bg", sw=1.5)
    svg.path(poly(est), stroke="c1", sw=2.5)

    # legend
    lx, ly = x0, 24
    svg.line(lx, ly, lx + 28, ly, stroke="ink", sw=2, dash="6 5")
    svg.text(lx + 36, ly, "true position", size=14)
    lx += 160
    svg.circle(lx + 8, ly, 4, fill="c2", stroke="bg", sw=1.5)
    svg.text(lx + 20, ly, "measurement", size=14)
    lx += 150
    svg.line(lx, ly, lx + 28, ly, stroke="c1", sw=2.5)
    svg.text(lx + 36, ly, "Kalman filter estimate", size=14)
    return svg


# ---------------------------------------------------------------------------
# Sweep line
# ---------------------------------------------------------------------------
def _seg_intersection(s, t):
    (x1, y1), (x2, y2) = s
    (x3, y3), (x4, y4) = t
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0:
        return None
    a = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    b = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    if 0 <= a <= 1 and 0 <= b <= 1:
        return (x1 + a * (x2 - x1), y1 + a * (y2 - y1))
    return None


def sweep_line() -> Svg:
    segs = {
        "a": ((40, 90), (300, 250)),
        "b": ((80, 270), (420, 60)),
        "c": ((180, 170), (560, 210)),
        "d": ((260, 300), (520, 110)),
        "e": ((380, 270), (600, 300)),
        "f": ((470, 50), (610, 130)),
    }
    sweep_x = 330
    svg = Svg(
        660,
        400,
        "The sweep line algorithm",
        f"Six line segments a to f and a vertical sweep line at x = {sweep_x} that moves from "
        "left to right. Segments that the sweep line currently crosses are active and kept in a "
        "data structure ordered from top to bottom. Segments left of the line are done, those "
        "right of it are not reached yet. Intersections left of the sweep line are already "
        "found. The dots on the axis are the event points: the segment end points.",
    )
    top, bottom = 30, 330
    svg.rect(20, top, sweep_x - 20, bottom - top, fill="sunk", rx=6)
    svg.text(30, top + 16, "processed", size=13, fill="muted")
    svg.text(640, top + 16, "not reached yet", size=13, fill="muted", anchor="end")
    active = []
    for name, ((ax, ay), (bx, by)) in segs.items():
        is_active = ax <= sweep_x <= bx
        done = bx < sweep_x
        color = "blue" if is_active else ("muted" if done else "faint")
        svg.line(ax, ay, bx, by, stroke=color, sw=3 if is_active else 2)
        svg.circle(ax, ay, 3.5, fill=color)
        svg.circle(bx, by, 3.5, fill=color)
        lx, ly = (ax - 14, ay) if name != "c" else (ax - 14, ay)
        svg.text(lx, ly, name, size=16, anchor="middle", weight="700",
                 fill="blue" if is_active else "muted")
        if is_active:
            y_at = ay + (by - ay) * (sweep_x - ax) / (bx - ax)
            active.append((y_at, name))
    names = list(segs)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            p = _seg_intersection(segs[names[i]], segs[names[j]])
            if p:
                found = p[0] < sweep_x
                svg.circle(p[0], p[1], 6, fill="acc" if found else "bg",
                           stroke="acc" if found else "faint", sw=2)
    svg.line(sweep_x, top - 8, sweep_x, bottom + 8, stroke="bad", sw=2.5)
    svg.line(sweep_x + 6, top - 2, sweep_x + 44, top - 2, stroke="bad", sw=2, arrow=True)
    svg.text(sweep_x - 6, bottom + 22, "sweep line", size=14, fill="bad", anchor="end")
    for y_at, _ in active:
        svg.circle(sweep_x, y_at, 4, fill="bad")
    # event points on the x axis
    axis_y = bottom + 46
    svg.line(20, axis_y, 640, axis_y, stroke="muted", sw=1.2, arrow=True)
    for (ax, _), (bx, _) in segs.values():
        for ex in (ax, bx):
            svg.circle(ex, axis_y, 3.5, fill="muted" if ex < sweep_x else "faint")
    svg.text(640, axis_y - 14, "x", size=14, fill="muted", anchor="end", italic=True)
    order = ", ".join(n for _, n in sorted(active))
    svg.rich(sweep_x + 14, bottom - 14,
             [("active (top → bottom): ", "muted", False), (order, "blue", True)], size=14)
    return svg


# ---------------------------------------------------------------------------
# Strassen
# ---------------------------------------------------------------------------
def strassen_blocks() -> Svg:
    svg = Svg(
        680,
        420,
        "Block structure of the Strassen algorithm",
        "Both n×n matrices A and B are split into four n/2×n/2 blocks. Strassen computes "
        "seven products M1 to M7 of sums of these blocks and combines them into the four "
        "blocks of C = A·B. The usual block multiplication needs eight products.",
    )
    tints = ["softblue", "soft", "softwarn", "softbad"]
    strokes = ["blue", "acc", "warn", "bad"]

    def block_matrix(x, y, name, size=120):
        h = size / 2
        for idx, (i, j) in enumerate([(1, 1), (1, 2), (2, 1), (2, 2)]):
            bx, by = x + (j - 1) * h, y + (i - 1) * h
            svg.rect(bx, by, h, h, fill=tints[idx], stroke=strokes[idx], sw=1.5)
            sub = "₁₂"
            svg.text(bx + h / 2, by + h / 2, f"{name}{sub[i - 1]}{sub[j - 1]}", size=17,
                     anchor="middle", weight="600")
        svg.text(x + size / 2, y + size + 18, name, size=16, anchor="middle", weight="700",
                 fill="muted")

    block_matrix(80, 24, "A")
    svg.text(232, 84, "·", size=34, anchor="middle")
    block_matrix(264, 24, "B")
    svg.text(416, 84, "=", size=28, anchor="middle")
    block_matrix(450, 24, "C")

    products = [
        "M₁ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)",
        "M₂ = (A₂₁ + A₂₂) B₁₁",
        "M₃ = A₁₁ (B₁₂ − B₂₂)",
        "M₄ = A₂₂ (B₂₁ − B₁₁)",
        "M₅ = (A₁₁ + A₁₂) B₂₂",
        "M₆ = (A₂₁ − A₁₁)(B₁₁ + B₁₂)",
        "M₇ = (A₁₂ − A₂₂)(B₂₁ + B₂₂)",
    ]
    results = [
        "C₁₁ = M₁ + M₄ − M₅ + M₇",
        "C₁₂ = M₃ + M₅",
        "C₂₁ = M₂ + M₄",
        "C₂₂ = M₁ − M₂ + M₃ + M₆",
    ]
    svg.text(60, 194, "7 multiplications", size=14, fill="muted", weight="600")
    for k, s in enumerate(products):
        svg.text(60, 222 + k * 27, s, size=16)
    svg.text(410, 194, "additions only", size=14, fill="muted", weight="600")
    for k, s in enumerate(results):
        svg.rect(398, 210 + k * 27, 8, 22, fill=tints[k], stroke=strokes[k], sw=1, rx=2)
        svg.text(414, 222 + k * 27, s, size=16)
    return svg


# ---------------------------------------------------------------------------
# Datenstrukturen: hash table and queue (German)
# ---------------------------------------------------------------------------
def hashtabelle() -> Svg:
    m = 7
    keys = [15, 8, 22, 4, 11, 30]
    slots: Dict[int, List[int]] = {i: [] for i in range(m)}
    for k in keys:
        slots[k % m].append(k)
    longest = max(len(v) for v in slots.values())
    svg = Svg(
        600,
        40 + m * 42 + 14,
        "Hashtabelle mit Verkettung",
        f"Eine Hashtabelle mit m = {m} Slots und der Divisions-Rest-Methode h(k) = k mod {m}. "
        f"Die Schlüssel {', '.join(map(str, keys))} werden eingefügt. 15, 8 und 22 landen alle "
        "in Slot 1 und bilden dort eine verkettete Liste, 4 und 11 in Slot 4, 30 in Slot 2. "
        f"Der Belegungsfaktor ist α = {len(keys)}/{m}.",
    )
    sx, sy, sw_, sh = 210, 40, 60, 42
    svg.text(sx + sw_ / 2, 20, "Slots", size=13, fill="muted", anchor="middle")
    svg.text(40, 20, "Schlüssel k", size=13, fill="muted")
    for i in range(m):
        y = sy + i * sh
        svg.rect(sx, y, sw_, sh, fill="sunk", stroke="muted", sw=1.5)
        svg.text(sx - 12, y + sh / 2, str(i), size=14, fill="muted", anchor="end", mono=True)
        x = sx + sw_ + 34
        prev = (sx + sw_ / 2, y + sh / 2)
        if not slots[i]:
            svg.text(sx + sw_ / 2, y + sh / 2, "∅", size=16, fill="faint", anchor="middle")
        for j, k in enumerate(slots[i]):
            svg.circle(prev[0], prev[1], 3.5, fill="ink")
            svg.line(prev[0], prev[1], x - 2, y + sh / 2, stroke="ink", sw=1.6, arrow=True)
            svg.rect(x, y + 6, 54, sh - 12, fill="soft" if len(slots[i]) == 1 else "softwarn",
                     stroke="acc" if len(slots[i]) == 1 else "warn", sw=1.5, rx=4)
            svg.text(x + 27, y + sh / 2, str(k), size=15, anchor="middle", weight="600",
                     mono=True)
            prev = (x + 54 - 8, y + sh / 2)
            x += 90
    for idx, k in enumerate(keys):
        y = sy + 10 + idx * 40
        svg.text(40, y + 8, f"{k} mod {m} = {k % m}", size=14, mono=True)
    svg.text(40, sy + 10 + len(keys) * 40 + 8, f"α = {len(keys)}/{m}", size=14, fill="muted",
             mono=True)
    svg.text(sx + sw_ + 34 + (longest - 1) * 90 + 27, sy + 1 * sh + sh / 2 + 34,
             "Kollisionen", size=13, fill="warn", anchor="middle")
    return svg


def warteschlange() -> Svg:
    items = ["A", "B", "C", "D", "E"]
    svg = Svg(
        600,
        170,
        "Warteschlange (Queue)",
        "Eine Warteschlange mit den Elementen A bis E. ENQUEUE fügt ein neues Element F am "
        "Ende an, DEQUEUE entnimmt das älteste Element A am Anfang. Wer zuerst kommt, wird "
        "zuerst bedient (FIFO).",
    )
    x0, y0, w, h = 150, 50, 56, 56
    for i, it in enumerate(items):
        x = x0 + i * (w + 6)
        first = i == 0
        svg.rect(x, y0, w, h, fill="softwarn" if first else "sunk",
                 stroke="warn" if first else "muted", sw=1.5, rx=6)
        svg.text(x + w / 2, y0 + h / 2, it, size=20, anchor="middle", weight="700")
    svg.text(x0 + w / 2, y0 + h + 20, "Anfang", size=13, fill="muted", anchor="middle")
    end_x = x0 + (len(items) - 1) * (w + 6)
    svg.text(end_x + w / 2, y0 + h + 20, "Ende", size=13, fill="muted", anchor="middle")
    # dequeue on the left
    svg.line(x0 - 8, y0 + h / 2, x0 - 70, y0 + h / 2, stroke="warn", sw=2.5, arrow=True)
    svg.text(x0 - 40, y0 - 14, "DEQUEUE", size=14, fill="warn", anchor="middle", weight="700")
    # enqueue on the right
    nx = end_x + w + 80
    svg.rect(nx, y0, w, h, fill="soft", stroke="acc", sw=1.5, rx=6, extra='stroke-dasharray="5 4"')
    svg.text(nx + w / 2, y0 + h / 2, "F", size=20, anchor="middle", weight="700")
    svg.line(nx - 8, y0 + h / 2, end_x + w + 10, y0 + h / 2, stroke="acc", sw=2.5, arrow=True)
    svg.text(nx - 36, y0 - 14, "ENQUEUE", size=14, fill="acc", anchor="middle", weight="700")
    svg.text(300, 150, "First In – First Out", size=14, fill="muted", anchor="middle",
             italic=True)
    return svg


# ---------------------------------------------------------------------------
# Floyd's cycle detection
# ---------------------------------------------------------------------------
def floyd_rho() -> Svg:
    mu, lam = 3, 6
    n_nodes = mu + lam

    def nxt(k):
        return k + 1 if k + 1 < n_nodes else mu

    slow = fast = 0
    t = 0
    while True:
        slow = nxt(slow)
        fast = nxt(nxt(fast))
        t += 1
        if slow == fast:
            break
    meet = slow

    svg = Svg(
        720,
        330,
        "Floyd's tortoise and hare on a list with a loop",
        f"A linked list whose first {mu} nodes lead into a loop of {lam} nodes "
        f"(μ = {mu}, λ = {lam}). Tortoise and hare start at the head and meet after t = {t} "
        f"steps at node {meet}. In the second phase one pointer starts again at the head, the "
        f"other one at the meeting point; after μ = {mu} steps each, both reach node {mu}, "
        "the start of the loop.",
    )
    r = 20
    pos = {}
    y_tail = 165
    for k in range(mu):
        pos[k] = (60 + k * 85, y_tail)
    cx, cy, R = 60 + mu * 85 + 100, y_tail, 100
    for i in range(lam):
        a = math.radians(180 + 360 / lam * i)
        pos[mu + i] = (cx + R * math.cos(a), cy + R * math.sin(a))
    for k in range(n_nodes):
        arrow_between(svg, pos[k], pos[nxt(k)], r, r, stroke="muted", sw=2)
    for k, (x, y) in pos.items():
        if k == mu:
            fill, stroke = "soft", "acc"
        elif k == meet:
            fill, stroke = "softwarn", "warn"
        elif k == 0:
            fill, stroke = "softblue", "blue"
        else:
            fill, stroke = "bg", "muted"
        svg.circle(x, y, r, fill=fill, stroke=stroke, sw=2)
        svg.text(x, y, str(k), size=15, anchor="middle", weight="700")
    hx, hy = pos[0]
    svg.text(hx, hy + 36, "head", size=14, fill="blue", anchor="middle")
    sx, sy = pos[mu]
    svg.text(sx + 6, sy + 36, "loop start", size=14, fill="acc", anchor="end")
    mx, my = pos[meet]
    svg.text(mx + 32, my, f"meeting point (t = {t})", size=14, fill="warn")
    # braces / labels for mu and lambda
    svg.path(f"M{pos[0][0]} {y_tail - 40} L{pos[0][0]} {y_tail - 48} L{sx} {y_tail - 48} "
             f"L{sx} {y_tail - 40}", stroke="muted", sw=1.5)
    svg.text((pos[0][0] + sx) / 2, y_tail - 62, f"μ = {mu} steps", size=14, fill="muted",
             anchor="middle")
    svg.text(cx, cy, f"λ = {lam}", size=16, fill="muted", anchor="middle", italic=True)
    return svg


# ---------------------------------------------------------------------------
# Sorting big data: chunking strategies
# ---------------------------------------------------------------------------
def external_sorting() -> Svg:
    svg = Svg(
        700,
        400,
        "Two ways to sort a file that does not fit into memory",
        "Top: merge sort splits the file into chunks of arbitrary numbers, sorts each chunk in "
        "memory and then has to merge the sorted chunks. Bottom: radix sort splits the file by "
        "the prefix of the numbers, sorts each chunk in memory and then only pastes the "
        "chunks together in prefix order.",
    )
    cx0, cw = 70, 140  # chunk boxes
    sx0, sw_ = 248, 140  # sorted chunk boxes
    mx0, mw = 466, 224  # combined result
    rows = [
        ("Merge sort", 70, [["71", "13", "98"], ["24", "86", "35"], ["57", "42", "19"]],
         "merge", "k-way merge", None),
        ("Radix sort", 250, [["19", "13"], ["42", "24", "35"], ["98", "57", "86", "71"]],
         "cat", "paste together", ["1x", "2x–4x", "5x–9x"]),
    ]
    for x, label in [(cx0 + cw / 2, "1. Chunking"), (sx0 + sw_ / 2, "2. Sort each chunk"),
                     (mx0 + mw / 2, "3. Combine")]:
        svg.text(x, 20, label, size=14, fill="muted", anchor="middle", weight="600")
    for title, y, chunks, mode, combine_label, prefixes in rows:
        svg.text(20, y - 18, title, size=15, weight="700")
        color = "warn" if mode == "merge" else "acc"
        for c, chunk in enumerate(chunks):
            cy = y + c * 42
            svg.rect(cx0, cy, cw, 32, fill="sunk", stroke="muted", sw=1.2, rx=4)
            svg.text(cx0 + cw / 2, cy + 16, " ".join(chunk), size=14, anchor="middle", mono=True)
            svg.line(cx0 + cw + 6, cy + 16, sx0 - 6, cy + 16, stroke="muted", sw=1.5, arrow=True)
            svg.rect(sx0, cy, sw_, 32, fill="soft", stroke="acc", sw=1.2, rx=4)
            svg.text(sx0 + sw_ / 2, cy + 16, " ".join(sorted(chunk)), size=14, anchor="middle",
                     mono=True)
            if prefixes:
                svg.text(cx0 - 8, cy + 16, prefixes[c], size=12, fill="muted", anchor="end",
                         mono=True)
        svg.text((sx0 + sw_ + mx0) / 2, y + 3 * 42 + 4, combine_label, size=13, fill=color,
                 anchor="middle")
        if mode == "merge":
            mid = y + 42 + 16
            for c in range(3):
                cy = y + c * 42 + 16
                svg.path(f"M{sx0 + sw_ + 6} {cy} C{sx0 + sw_ + 40} {cy} {mx0 - 40} {mid} "
                         f"{mx0 - 8} {mid}", stroke="warn", sw=1.8)
            svg.line(mx0 - 10, mid, mx0 - 4, mid, stroke="warn", sw=1.8, arrow=True)
            merged = sorted(n for ch in chunks for n in ch)
            svg.rect(mx0, mid - 16, mw, 32, fill="softwarn", stroke="warn", sw=1.5, rx=4)
            svg.text(mx0 + mw / 2, mid, " ".join(merged), size=13, anchor="middle", mono=True)
        else:
            svg.rect(mx0, y - 4, mw, 3 * 42 - 2, fill="soft", stroke="acc", sw=1.5, rx=4)
            for c, chunk in enumerate(chunks):
                cy = y + c * 42 + 16
                svg.line(sx0 + sw_ + 6, cy, mx0 - 4, cy, stroke="acc", sw=1.8, arrow=True)
                svg.text(mx0 + 14, cy, " ".join(sorted(chunk)), size=14, mono=True)
    return svg


FIGURES: Dict[str, Tuple[Callable[[], Svg], str]] = {
    "project-euler-26": (project_euler_26, "images/2012/08/project-euler-26-long-division.svg"),
    "landau": (landau_growth, "images/2012/07/landau-wachstum.svg"),
    "polygon": (polygon_triangulation, "images/2013/11/polygon-triangulation.svg"),
    "wer": (wer_matrix, "images/2013/11/wer-levenshtein-matrix.svg"),
    "edit-distance": (edit_distance_matrix, "images/2020/03/edit-distance-matrix.svg"),
    "label-correction": (label_correction_graph, "images/2017/01/label-correction-sample-graph.svg"),
    "kadane": (kadane, "images/2020/05/kadane.svg"),
    "fibonacci": (fibonacci_call_tree, "images/2020/03/fibonacci-call-tree.svg"),
    "kalman": (kalman_1d, "images/2016/06/kalman-filter-1d.svg"),
    "sweep-line": (sweep_line, "images/2017/01/sweep-line.svg"),
    "strassen": (strassen_blocks, "images/2013/01/strassen-blocks.svg"),
    "hashtabelle": (hashtabelle, "images/2012/07/hashtabelle-verkettung.svg"),
    "warteschlange": (warteschlange, "images/2012/07/warteschlange.svg"),
    "floyd": (floyd_rho, "images/2020/05/floyd-tortoise-hare.svg"),
    "external-sorting": (external_sorting, "images/2020/05/external-sorting-strategies.svg"),
}


def main(args: List[str]) -> None:
    for name, (make, out) in FIGURES.items():
        if args and not any(a in name for a in args):
            continue
        svg = make()
        Path(out).write_text(svg.render(), encoding="utf-8")
        print(f"{out}: {svg.width}x{svg.height}")


if __name__ == "__main__":
    main(sys.argv[1:])
