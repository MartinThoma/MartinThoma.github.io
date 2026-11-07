---
layout: post
title: 3 Applications of garbled fonts most developers don’t know 😈
slug: 3-applications-of-garbled-fonts-most-developers-dont-know
lang: en
author: Martin Thoma
date: 2024-03-19 17:31
category: Code
tags: Security, Typography, Encoding
featured_image: logos/unicode.png
summary: Please don’t do it.
medium_url: https://medium.com/@martinthoma/3-applications-of-garbled-fonts-most-developers-dont-know-403b78b8107b
status: draft
---
<figure class="ai-generated">
    <a href="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-1.jpg"><img src="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-1.jpg" alt="A frustrated man pulling his hair and screaming at his desk" width="800" height="800"></a>
    <figcaption>Created with AI</figcaption>
</figure>

As the maintainer of pypdf I see a ton of weird PDF files. One type of issue people regularly complain about is PDFs with garbled fonts. When you copy-paste text from those documents you get a wild mix of characters instead of the text.

The reason for this mess is that people use some form of copy-paste protection in which the font is showing something different than it should.

Think about the Windings font:

<figure>
    <a href="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-2.png"><img src="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-2.png" alt="The glyphs of the Wingdings font: pictograms like a pencil, scissors, a telephone, envelopes, folders, hands, zodiac signs, stars, clocks and arrows instead of letters" width="800" height="589" loading="lazy"></a>
</figure>

Every character in this font is a symbol — not the character itself.

When text is displayed you have two aspects to it:

* **Semantics**: An `A` is the first letter of the Latin alphabet. It has a lowercase variant. It has a certain pronunciation which depends on the language, but is similar in each language.
* **Appearance**: three lines, two straight lines meeting at a point at the top, connected by a horizontal line across the middle. There are many variations on how this can be done, but the variations are recognized by most people who use the Latin alphabet.

A font format such as TrueType stores vector graphics as well as a table that maps Unicode code points (the semantics) to the glyph (the appearance).

Typically, people make fonts in which the Unicode code points match the glyph. But you don’t have to do that 😈

## Application #1: Copy protection

<figure class="ai-generated">
    <a href="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-3.jpg"><img src="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-3.jpg" alt="Comic drawing of a sheet of paper full of small icons and symbols instead of letters" width="800" height="800" loading="lazy"></a>
</figure>

The first idea is to create a PDF that people can easily read, but not easily copy with Python and the [fonttools](https://pypi.org/project/fonttools/) library as well as the [fpdf2](https://pypi.org/project/fpdf2/) library:

```python
import os
import random
import uuid

from fontTools.ttLib import TTFont  # pip install fonttools
from fpdf import FPDF  # pip install fpdf2


def find_font(name: str = "Helvetica") -> str:
    common_locations = [
        f"{name}.ttf",
        f"/Library/Fonts/{name}.ttf",  # macOS
        f"/usr/share/fonts/truetype/msttcorefonts/{name}.ttf",  # Linux
        f"/usr/local/share/fonts/{name}.ttf",  # Linux
        f"/usr/share/fonts/{name}.ttf",  # Linux
        f"C:\\Windows\\Fonts\\{name}.ttf",  # Windows
    ]

    for location in common_locations:
        if os.path.exists(location):
            return location
    raise RuntimeError(f"Font '{name}' not found")


def manipulate_font(font_name: str) -> str:
    # Load the original font
    location = find_font(name=font_name)
    font = TTFont(location)

    # Garble
    original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    rot = list(original)
    random.shuffle(rot)
    shuffled = "".join(rot)
    shuffle_mapping = dict(zip(original, shuffled))

    # Iterate through each glyph in the original font and apply mapping
    for char, rotated_char in shuffle_mapping.items():
        try:
            o_glyph = font["cmap"].getcmap(3, 1).cmap[ord(char)]
            r_glyph = font["cmap"].getcmap(3, 1).cmap[ord(rotated_char)]
            font["cmap"].getcmap(3, 1).cmap[ord(char)] = r_glyph
            font["cmap"].getcmap(3, 1).cmap[ord(rotated_char)] = o_glyph
        except KeyError:
            print(f"Glyph data not found for character '{char}'")

    # Change font name
    for record in font["name"].names:
        if record.nameID == 1:  # Font Family name
            record.string = "RotatedFont".encode("utf-16-be")

    # Save the modified font to a new font file
    out = f"rotated_font-{uuid.uuid4()}.ttf"
    font.save(out)
    return out


def generate_pdf(text: str, font_path: str) -> None:
    # Create a PDF instance
    pdf = FPDF()
    pdf.add_page()

    # Add the custom font
    pdf.add_font("RotatedFont", "", font_path, uni=True)
    pdf.set_font("RotatedFont", "", 16)

    # Add text using the custom font
    pdf.cell(
        200,
        10,
        txt="This text is written using the custom font!",
        ln=True,
        align="C",
    )

    # Output the PDF
    pdf_file_path = "output.pdf"
    pdf.output(pdf_file_path)


if __name__ == "__main__":
    font_path = manipulate_font("LibrestileExtBold")
    generate_pdf(
        text="This text is written using the custom font!",
        font_path=font_path,
    )
```

When you change this mapping on a character-basis you can make it impossible for machines to read. It’s a [one-time pad](https://en.wikipedia.org/wiki/One-time_pad). But machines can still apply OCR.

## Application #2: Hide a message in plain sight

<figure class="ai-generated">
    <a href="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-4.jpg"><img src="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-4.jpg" alt="Comic drawing of a confused man on his knees looking for his glasses" width="800" height="800" loading="lazy"></a>
</figure>

Instead of having a random mapping, we now want to have something meaningful. We have one message in human-readable form and another one in machine-readable (and copyable) form. [Here is an example PDF](https://github.com/MartinThoma/algorithms/blob/master/Python/font-stegano/2_example.pdf).

```python
import os
import uuid

from fontTools.ttLib import TTFont  # pip install fonttools
from fpdf import FPDF  # pip install fpdf2


def find_font(name: str = "Helvetica") -> str:
    common_locations = [
        f"{name}.ttf",
        f"/Library/Fonts/{name}.ttf",  # macOS
        f"/usr/share/fonts/truetype/msttcorefonts/{name}.ttf",  # Linux
        f"/usr/local/share/fonts/{name}.ttf",  # Linux
        f"/usr/share/fonts/{name}.ttf",  # Linux
        f"C:\\Windows\\Fonts\\{name}.ttf",  # Windows
    ]

    for location in common_locations:
        if os.path.exists(location):
            return location
    raise RuntimeError(f"Font '{name}' not found")


def partial_shuffle(mapping: list[tuple[str, str]]) -> dict[str, str]:
    original = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .:!?,"
    )
    shuffled = dict(mapping)

    # Add remaining characters not specified in the mapping
    remaining_chars = [
        char for char in original if char not in shuffled.keys()
    ]
    for char in remaining_chars:
        shuffled[char] = char

    return shuffled


def manipulate_font(
    font_name: str, mapping: tuple[str, str]
) -> tuple[str, str]:
    # Load the original font
    location = find_font(name=font_name)
    font = TTFont(location)

    # Iterate through each char in the original and apply mapping
    shuffle_mapping = partial_shuffle([mapping])
    for char, rotated_char in shuffle_mapping.items():
        try:
            o_glyph = font["cmap"].getcmap(3, 1).cmap[ord(char)]
            r_glyph = font["cmap"].getcmap(3, 1).cmap[ord(rotated_char)]
            font["cmap"].getcmap(3, 1).cmap[ord(char)] = r_glyph
            font["cmap"].getcmap(3, 1).cmap[ord(rotated_char)] = o_glyph
        except KeyError:
            print(f"Glyph data not found for character '{char}'")

    # Change font name
    new_name = str(uuid.uuid4())
    for record in font["name"].names:
        if record.nameID == 1:  # Font Family name
            record.string = new_name.encode("utf-16-be")

    # Save the modified font to a new font file
    out = f"rotated_font-{new_name}.ttf"
    font.save(out)
    return out, new_name


def generate_pdf(shown_message: str, hidden_message: str) -> None:
    # Pad the shorter message with spaces
    max_length = max(len(hidden_message), len(shown_message))
    hidden_message = hidden_message.ljust(max_length)
    shown_message = shown_message.ljust(max_length)

    # Create a PDF instance
    pdf = FPDF()
    pdf.add_page()

    x_position = 10  # Adjust this value as needed
    y_position = 10
    cell_width = 5

    for shown, hidden in zip(shown_message, hidden_message):
        # Add the custom font
        font_path, font_name = manipulate_font(
            "LibrestileExtBold", (shown, hidden)
        )
        pdf.add_font(font_name, "", font_path, uni=True)
        pdf.set_font(font_name, "", 16)

        # Add text using the custom font
        pdf.set_xy(x_position, y_position)  # Set x and y position
        pdf.cell(cell_width, 1, txt=hidden, ln=False, align="L")
        x_position += cell_width
        if x_position > 200:
            x_position = 10
            y_position += cell_width * 2

    # Output the PDF
    pdf_file_path = "2_example.pdf"
    pdf.output(pdf_file_path)


if __name__ == "__main__":
    generate_pdf(
        shown_message="This text is written using the custom font",
        hidden_message="Never gonna give you up, never gonna let you down",
    )
```

How could that be used?

* Craft a CV in which automatic parsers find all of the relevant keywords
* Exchange hidden messages
* Have copyright notes within the document — e.g. in whitespace. It’s a variation of the “white text on white background” trick.

Copy-pasted shell commands can be evil: An attacker can write a tutorial article in which they write:

```bash
# Intall the requirements
pip install fpdf2 fonttools
```

But when you copy that, you get a malicious command (likely something with `curl`).

## Application #3: Hidden messages within the embedded font specs

<figure class="ai-generated">
    <a href="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-5.jpg"><img src="../images/2024/03/3-applications-of-garbled-fonts-most-developers-dont-know-5.jpg" alt="Comic drawing of a boy with a tablet, surrounded by floating gears, documents and gadgets" width="800" height="800" loading="lazy"></a>
</figure>

It’s possible to embed a font within a PDF file that is never used. The name of the embedded font might be the message. Or a comment within the font declaration. The glyph could be something more than just one character. The code points “abcdefghijklmnopqrstuvwxyz” could have glyphs that are the message (potentially repeating some glyphs).

There are tons of possibilities to hide messages. Get creative 😁

## Summary

Having many different fonts within one document or wild changes of the applied font within a document (PDF, Word, HTML, …) can indicate that something more interesting is going on. It’s worth having a closer look at such basic concepts as fonts to understand how they can be (ab)used.
