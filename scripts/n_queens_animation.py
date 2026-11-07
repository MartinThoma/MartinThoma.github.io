"""
Render an animated GIF of depth-first backtracking on the n-queens puzzle.

Used in content/2020-03-30-backtracking.md. Run from the repository root:

    python scripts/n_queens_animation.py

Left: the board. Right: the search tree of the valid partial solutions found so
far. The current path is highlighted, abandoned branches are grey.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from PIL import Image, ImageChops, ImageDraw, ImageFont

N = 4
OUT = Path("images/2020/03/n-queens-backtracking.gif")

SCALE = 2  # draw at 2x, then downscale for anti-aliasing
WIDTH, HEIGHT = 760, 520
CELL = 100
BOARD_X, BOARD_Y = 30, 30
TREE_X0, TREE_X1 = 545, 735
TREE_Y0, TREE_DY = 40, 85

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

BG = (255, 255, 255)
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
INK = (34, 34, 40)
MUTED = (140, 140, 150)
QUEEN = (30, 40, 70)
RED = (200, 40, 40)
ORANGE = (230, 130, 20)
GREEN = (30, 140, 60)
GREY = (200, 200, 205)

Solution = Tuple[int, ...]


@dataclass
class Event:
    kind: str  # start, place, conflict, deadend, backtrack, solution
    partial: Solution  # queens on the board (row i -> column partial[i])
    row: int = -1
    col: int = -1
    attacker: Optional[Tuple[int, int]] = None
    dead: List[Solution] = field(default_factory=list)


def is_threatening(x1: int, y1: int, x2: int, y2: int) -> bool:
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


def first_attacker(partial: Solution, x: int, y: int) -> Optional[Tuple[int, int]]:
    for x_old, y_old in enumerate(partial):
        if is_threatening(x_old, y_old, x, y):
            return (x_old, y_old)
    return None


def backtrack_events(n: int) -> List[Event]:
    """Run depth-first backtracking until the first solution, log each step."""
    events = [Event("start", ())]
    dead: List[Solution] = []

    def solve(partial: Solution) -> bool:
        row = len(partial)
        if row == n:
            events.append(Event("solution", partial, dead=list(dead)))
            return True
        for col in range(n):
            attacker = first_attacker(partial, row, col)
            if attacker is not None:
                events.append(
                    Event("conflict", partial, row, col, attacker, list(dead))
                )
                continue
            new = partial + (col,)
            events.append(Event("place", new, row, col, dead=list(dead)))
            if solve(new):
                return True
            dead.append(new)
            events.append(Event("backtrack", new, row, col, dead=list(dead)))
        if row > 0:
            events.append(Event("deadend", partial, row, dead=list(dead)))
        return False

    # A child's "deadend" is logged before the parent's "backtrack", which is
    # the order in which the animation shows them.
    solve(())
    return events


def tree_layout(events: List[Event]) -> Dict[Solution, Tuple[float, float]]:
    """Position every node of the final search tree (valid partial solutions)."""
    nodes: List[Solution] = [()]
    for event in events:
        if event.kind == "place":
            nodes.append(event.partial)
    children: Dict[Solution, List[Solution]] = {node: [] for node in nodes}
    for node in nodes[1:]:
        children[node[:-1]].append(node)

    leaves = [node for node in nodes if not children[node]]
    gap = (TREE_X1 - TREE_X0) / max(len(leaves) - 1, 1)
    pos: Dict[Solution, Tuple[float, float]] = {}

    def place(node: Solution) -> float:
        if not children[node]:
            x = TREE_X0 + leaves.index(node) * gap
        else:
            xs = [place(child) for child in children[node]]
            x = sum(xs) / len(xs)
        pos[node] = (x, TREE_Y0 + len(node) * TREE_DY)
        return x

    place(())
    return pos


def font(size: int, bold: bool = False, mono: bool = False):
    name = "DejaVuSansMono" if mono else "DejaVuSans"
    if bold:
        name += "-Bold"
    return ImageFont.truetype(str(FONT_DIR / f"{name}.ttf"), size * SCALE)


def status_text(event: Event) -> Tuple[str, Tuple[int, int, int]]:
    if event.kind == "start":
        return "Start with an empty board. Place one queen per row.", INK
    if event.kind == "place":
        return f"Row {event.row}: column {event.col} is free. Place a queen.", INK
    if event.kind == "conflict":
        ar, _ = event.attacker
        return (
            f"Row {event.row}, column {event.col}: attacked by the queen in row {ar}.",
            RED,
        )
    if event.kind == "deadend":
        return f"Row {event.row}: no free column left. Dead end!", RED
    if event.kind == "backtrack":
        return (
            f"Backtrack: remove the queen in row {event.row}, try the next column.",
            ORANGE,
        )
    return "All queens placed without threatening each other: solved!", GREEN


def render(event: Event, pos: Dict[Solution, Tuple[float, float]]) -> Image.Image:
    s = SCALE
    img = Image.new("RGB", (WIDTH * s, HEIGHT * s), BG)
    draw = ImageDraw.Draw(img)
    queen_font = font(72)
    label_font = font(15)
    node_font = font(15, bold=True)
    status_font = font(19)
    tuple_font = font(19, mono=True)

    def cell_box(row: int, col: int):
        x = (BOARD_X + col * CELL) * s
        y = (BOARD_Y + row * CELL) * s
        return x, y, x + CELL * s, y + CELL * s

    def cell_center(row: int, col: int):
        x0, y0, x1, y1 = cell_box(row, col)
        return (x0 + x1) / 2, (y0 + y1) / 2

    # Board
    for row in range(N):
        for col in range(N):
            draw.rectangle(cell_box(row, col), fill=LIGHT if (row + col) % 2 == 0 else DARK)
    draw.rectangle(
        (BOARD_X * s, BOARD_Y * s, (BOARD_X + N * CELL) * s, (BOARD_Y + N * CELL) * s),
        outline=INK,
        width=2 * s,
    )
    for i in range(N):
        cx, _ = cell_center(0, i)
        draw.text((cx, (BOARD_Y - 4) * s), str(i), font=label_font, fill=MUTED, anchor="md")
        _, cy = cell_center(i, 0)
        draw.text(((BOARD_X - 8) * s, cy), str(i), font=label_font, fill=MUTED, anchor="rm")

    # Highlight the square that is being looked at
    highlight = None
    if event.kind in ("place", "conflict", "backtrack"):
        highlight = (event.row, event.col)
        color = {"place": GREEN, "conflict": RED, "backtrack": ORANGE}[event.kind]
        x0, y0, x1, y1 = cell_box(*highlight)
        inset = 3 * s
        draw.rectangle((x0 + inset, y0 + inset, x1 - inset, y1 - inset), outline=color, width=5 * s)
    if event.kind == "deadend":
        x0, y0, _, _ = cell_box(event.row, 0)
        _, _, x1, y1 = cell_box(event.row, N - 1)
        inset = 3 * s
        draw.rectangle((x0 + inset, y0 + inset, x1 - inset, y1 - inset), outline=RED, width=5 * s)

    # Line from the attacking queen to the attacked square, under the queens
    if event.kind == "conflict":
        ax, ay = cell_center(*event.attacker)
        bx, by = cell_center(event.row, event.col)
        draw.line((ax, ay, bx, by), fill=RED, width=4 * s)

    # Queens
    for row, col in enumerate(event.partial):
        fill = QUEEN
        if event.kind == "backtrack" and row == event.row:
            fill = ORANGE
        elif event.kind == "solution":
            fill = GREEN
        draw.text(cell_center(row, col), "♛", font=queen_font, fill=fill, anchor="mm")
    if event.kind == "conflict":
        draw.text(cell_center(event.row, event.col), "♛", font=queen_font, fill=RED, anchor="mm")

    # Search tree
    tree_label_font = font(13)
    for depth in range(N + 1):
        y = (TREE_Y0 + depth * TREE_DY) * s
        text = "start" if depth == 0 else f"row {depth - 1}"
        draw.text(((BOARD_X + N * CELL + 22) * s, y), text, font=tree_label_font, fill=MUTED, anchor="lm")

    visible = {()} | set(event.dead)
    for i in range(1, len(event.partial) + 1):
        visible.add(event.partial[:i])
    # nodes that were visited before (their subtree is dead or they are on the path)
    visible |= {node for d in event.dead for node in (d[:i] for i in range(len(d) + 1))}
    on_path = {event.partial[:i] for i in range(len(event.partial) + 1)}
    if event.kind == "backtrack":
        on_path.discard(event.partial)

    def node_color(node: Solution):
        if event.kind == "solution" and node in on_path:
            return GREEN
        if event.kind == "backtrack" and node == event.partial:
            return ORANGE
        if node in on_path:
            return QUEEN
        return GREY

    for node in visible:
        if node == ():
            continue
        x0, y0 = pos[node[:-1]]
        x1, y1 = pos[node]
        color = node_color(node)
        draw.line((x0 * s, y0 * s, x1 * s, y1 * s), fill=color, width=(3 if color != GREY else 2) * s)
    radius = 15 * s
    for node in visible:
        x, y = pos[node]
        color = node_color(node)
        draw.ellipse(
            (x * s - radius, y * s - radius, x * s + radius, y * s + radius),
            fill=color if color != GREY else BG,
            outline=color,
            width=2 * s,
        )
        label = "()" if node == () else str(node[-1])
        draw.text((x * s, y * s), label, font=node_font, fill=BG if color != GREY else MUTED, anchor="mm")
    if event.kind == "deadend":
        x, y = pos[event.partial]
        draw.text((x * s, (y + 22) * s), "✗", font=font(22, bold=True), fill=RED, anchor="mt")

    # Partial solution and status line
    y = (BOARD_Y + N * CELL + 38) * s
    draw.text((BOARD_X * s, y), "partial solution:", font=status_font, fill=MUTED, anchor="lm")
    shown = event.partial
    tuple_str = "(" + ", ".join(map(str, shown)) + ("," if len(shown) == 1 else "") + ")"
    draw.text(((BOARD_X + 170) * s, y), tuple_str, font=tuple_font, fill=INK, anchor="lm")
    text, color = status_text(event)
    draw.text((BOARD_X * s, y + 36 * s), text, font=status_font, fill=color, anchor="lm")

    return img.resize((WIDTH, HEIGHT), Image.LANCZOS)


DURATIONS = {
    "start": 1800,
    "place": 900,
    "conflict": 700,
    "deadend": 1300,
    "backtrack": 1100,
    "solution": 4500,
}


def main() -> None:
    events = backtrack_events(N)
    pos = tree_layout(events)
    frames = [render(event, pos) for event in events]
    # One shared palette without dithering keeps the file small.
    sheet = Image.new("RGB", (WIDTH, HEIGHT * len(frames)))
    for i, frame in enumerate(frames):
        sheet.paste(frame, (0, i * HEIGHT))
    palette = sheet.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    # Pillow maps a pixel to the first close palette entry, not to the exact
    # one, so white would become #fcfcfc. Map the flat colours explicitly.
    flat = (BG, LIGHT, DARK, INK, QUEEN, RED, ORANGE, GREEN, GREY, MUTED)
    entries = palette.getpalette()[: 3 * 128]
    for i, color in enumerate(flat):
        entries[3 * i : 3 * i + 3] = color
    palette = Image.new("P", (1, 1))
    palette.putpalette(entries)
    palette_frames = []
    for frame in frames:
        indexed = frame.quantize(palette=palette, dither=Image.Dither.NONE)
        channels = frame.split()
        for i, color in enumerate(flat):
            masks = [
                ch.point(lambda v, c=c: 255 if v == c else 0).convert("1")
                for ch, c in zip(channels, color)
            ]
            mask = ImageChops.logical_and(ImageChops.logical_and(masks[0], masks[1]), masks[2])
            indexed.paste(i, mask=mask)
        palette_frames.append(indexed)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    palette_frames[0].save(
        OUT,
        save_all=True,
        append_images=palette_frames[1:],
        duration=[DURATIONS[event.kind] for event in events],
        loop=0,
        optimize=True,
    )
    print(f"{OUT}: {len(frames)} frames, {OUT.stat().st_size / 1024:.0f} KiB")


if __name__ == "__main__":
    main()
