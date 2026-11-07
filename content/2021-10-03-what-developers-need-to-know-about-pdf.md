---
layout: post
title: What developers need to know about PDF
slug: what-developers-need-to-know-about-pdf
lang: en
author: Martin Thoma
date: 2021-10-03 12:01
category: Code
tags: PDF, Python
featured_image: logos/pdf.png
summary: Standards, functions, usage, terminology
medium_url: https://medium.com/@martinthoma/what-developers-need-to-know-about-pdf-ca7f267785d
---
PDF is a file format that was created to print in exactly the same way everywhere. It was not intended to be a format for data exchange. Nowadays, it is used in all organizations. You can create presentations with it, you can save documents like your thesis, you can create bills and forms.

Throughout my career, I had the dubious pleasure of reading PDF files multiple times. In this article, I’ll share some learnings with you. Let’s go!

## PDF Format Versions

PDF is an evolving format. Adobe started developing the format in 1991, released it in 1993, and it became an ISO standard in 2008. Some important versions are:

* PDF 1.3: [JavaScript Actions](https://stackoverflow.com/q/9640141/562769), [Digital signatures](https://www.pdfa.org/pdf-and-digital-signatures/)
* PDF 1.4: Transparency, JBIG2Decode was introduced
* PDF 1.5: JPXDecode, [XFA](https://en.wikipedia.org/wiki/XFA) was introduced, HTML 4 Form format
* PDF 1.6: OpenType font support, interactive 3D documents
* PDF 1.7: Basis for parts of PDF/A-2
* PDF 2.0: XFA was deprecated

## Image-Only vs Searchable vs Digitally-created

When you use a scanner, you get an image. The format of the image file could be JPG or PDF. However, the PDF simply contains the image. You cannot copy the text and you cannot search within the document. Search engines will have a harder time finding the contents. Such PDFs are called **image-only PDFs**.

You can apply optical character recognition (OCR) to an image. Machine Learning algorithms try to recognize the characters and put them behind the image. The resulting PDF still looks the same as the image-only PDF, but now you can search for content. The OCR algorithm might have made a mistake, so you might not be able to copy everything and some things you copy might be wrong. Such PDFs are called **searchable PDFs**. Many scanners can directly create searchable PDFs.

You can create a PDF via Microsoft Word or other document writing tools. When you do this, then the resulting PDF will have text which others can copy. It is easy to search content within the PDF with standard PDF viewers. The reason for that is that the data is directly within the PDF. The **digitally-created PDF** is sometimes also called *digitally-born* or a [*True PDF*](https://pdf.abbyy.com/pdf-types/).

## Archivability: PDF/A

PDF is perceived as static content, similar to a piece of paper. However, there are two reasons why one PDF might look different on different devices or at different times:

1. Active Content: PDF can contain JavaScript and PostScript
1. Attachments: The attachments could contain anything

To fix this issue, the standards PDF/A-1, PDF/A-2, and PDF/A-3 were developed. All of them are PDF files, but they are restricted to be suitable for long-term archives.

PDF/A-1 is based on PDF 1.4 and parts of PDF/A-2 are based on PDF 1.7.

There is software that can automatically convert files to PDF/A, but it is not possible to guarantee for all cases that the resulting file looks exactly the same as the original. It’s a good idea to check if the software vendor you are using is a member of the [PDF Association](https://en.wikipedia.org/wiki/PDF_Association).

## Universal Accessibility: PDF/UA

People with disabilities also want to read PDF files. To help assistive tools like screen readers, semantics need to be added. The PDF/UA (universal accessibility) standard is similar to the [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines). For example, images need to have alternative text which describes their content. PDF tags should group the content of the PDF file into semantic sections.

If you want to know more, I recommend reading [A Technical Introduction to PDF/UA](https://www.pdflib.com/fileadmin/pdflib/pdf/whitepaper/Whitepaper-Technical-Introduction-to-PDFUA.pdf).

## Printing: PDF/X

PDF/X is a standard based on PDF, restricting it to make it more useful for printing.

* PDF/X-1a was based on PDF 1.3
* PDF/X-3: Color management
* PDF/X-4: Transparency
* PDF/X-5: More flexibility
* PDF/X-6: Based on PDF 2.0

A good explanation is given in [PDF/X in a Nutshell](https://www.pdfa.org/wp-content/uploads/2017/05/PDFX-in-a-Nutshell.pdf).

## Variable Data and Transactional Printing: PDF/VT

PDF/VT is based on PDF/X and is good for invoices and advertisement. Imagine a PDF with complex graphics, but one part is just your name in it. Instead of re-creating the PDF all the time with only this string changing, the PDF just contains a variable for it.

The best explanation I have seen is by [prepressure.com](https://www.prepressure.com/pdf/basics/pdfvt-file-format-specifications) and by Dov Isaacs in his talk “[A Technical Introduction to PDF/VT](https://www.youtube.com/watch?v=vqC6KFQTfZI&t=471s)”.

## Engineering: PDF/E

PDF/E is for Engineering and pretty specialized as you can see with this quote [from Wikipedia](https://en.wikipedia.org/wiki/PDF/E):

> [PDF/E is] for the creation of documents used in geospatial, construction and manufacturing workflows and is based on the PDF Reference version 1.6 […].

## PDF and Python

I spent a lot of time diving into the various libraries to interact with PDF files in Python. The following should give you a brief overview of the libraries I have worked with.

### Reading PDF files with Python

Do you want to know [how to extract text from a PDF file](https://stackoverflow.com/a/63518022/562769)? I got you:

[PyMuPDF](https://pypi.org/project/PyMuPDF/) is based on the C-library [MuPDF](https://en.wikipedia.org/wiki/MuPDF) which is dual-licensed under the [GNU Affero General Public License](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License) and commercial permissive license.

You can read the text of a PDF like this:

```python
import fitz  # this is pymupdf

with fitz.open("my.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

print(text)
```

Acceptable alternatives might be:

* [pdfminer.six](https://pypi.org/project/pdfminer.six/): It’s a pure Python module
* [PyPDF3](https://pypi.org/project/PyPDF3/) ([GitHub](https://github.com/sfneal/PyPDF3)): Although the last uploaded version is from 2021, I’m uncertain if this is more maintenance or actually actively developed🤔 I also don’t know anybody who uses this, and the number of GitHub stars are suspiciously low.

The following are projects I recommend NOT to use for text extraction:

* [PyPDF2](https://pypi.org/project/PyPDF2/): A lot of tutorials still use this, but the project was dead: the last update was from 2016. *Update:* In April 2022, I became the maintainer of PyPDF2 and in December 2022 we moved it back to [pypdf](https://pypi.org/project/pypdf/). Use pypdf (see [The Python PDF Ecosystem in 2024](../the-python-pdf-ecosystem-in-2024/)).
* [PyPDF4](https://pypi.org/project/PyPDF4/): This project never really started. There was just one release and it was in 2018.
* [pdfminer](https://pypi.org/project/pdfminer): The last updated version is from 2019. The project is dead.
* [pikepdf](https://github.com/pikepdf/pikepdf) is based on the C++ library [qpdf](https://github.com/qpdf/qpdf) which is Apache 2.0 licensed. The project makes a pretty good impression, but [pikepdf doesn’t support reading text from PDF files](https://pikepdf.readthedocs.io/en/latest/topics/content_streams.html#extracting-text-from-pdfs).

### Reading Tables from PDF files

I’ve spent quite some time with this problem and it’s ridiculously hard. You have to know that tables are not a single semantic object in PDF. They are rather absolutely positioned text. In the worst case, every single letter could be absolutely positioned. That’s just a nightmare, especially if you have non-trivial structures like tables within tables, merged cells, invisible borders, text overflowing a column, …

Having said that, there is [Camelot](https://pypi.org/project/camelot-py/) and the Java project [Tabula](https://tabula.technology/) with the Python wrapper [tabula-py](https://pypi.org/project/tabula-py/). I’ve found examples for both where it worked well, examples where either of them or both failed. It’s simply a hard problem 🤷

### Creating PDF files with Python

There are a couple of different ways and I cannot say that I’m really happy with any of them.

When it comes to the quality of the produced PDF, I was most happy with going over **LaTeX to PDF**. The results LaTeX can generate are simply beautiful; have a look at my [LaTeX examples](https://github.com/MartinThoma/latex-examples). However, calling `pdflatex` via a subprocess just feels wrong. It is a pain to set LaTeX up when you want the full TeX Live support. It worked well, though.

A simpler approach converts **HTML to PDF**. I was reasonably happy with [wkhtmltopdf](https://pypi.org/project/wkhtmltopdf/). I’ve also seen [pdfkit](https://pypi.org/project/pdfkit/) to make using wkhtmltopdf easier. I’ve also stumbled a couple of years ago over [weasyprint](https://pypi.org/project/weasyprint/), but that didn’t work for me. I don’t remember why.

[Reportlab](https://pypi.org/project/reportlab/) is a common approach to **generate PDF files directly from Python**. As an alternative, I would give [pikepdf](https://github.com/pikepdf/pikepdf) a shot if I needed to do this again.
