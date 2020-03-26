---
layout: post
title: Colors in LaTeX
slug: colors-in-latex
author: Martin Thoma
date: 2016-11-20 20:00
category: Cyberculture
tags: LaTeX
featured_image: logos/latex.png
---

LaTeX knows the following colors without any packages:

<table>
    <tr>
        <td style="background-color:black;color:white;">black</td>
        <td style="background-color:blue;color:white;">blue</td>
        <td style="background-color:brown;color:white;">brown</td>
        <td style="background-color:cyan;color:black;">cyan</td>
    </tr>
    <tr>
        <td style="background-color:darkgray;color:black;">darkgray</td>
        <td style="background-color:gray;color:black;">gray</td>
        <td style="background-color:green;color:black;">green</td>
        <td style="background-color:lime;color:black;">lime</td>
    </tr>
    <tr>
        <td style="background-color:magenta;color:black;">magenta</td>
        <td style="background-color:olive;color:black;">olive</td>
        <td style="background-color:orange;color:black;">orange</td>
        <td style="background-color:pink;color:black;">pink</td>
    </tr>
    <tr>
        <td style="background-color:purple;color:black;">purple</td>
        <td style="background-color:red;color:black;">red</td>
        <td style="background-color:teal;color:black;">teal</td>
        <td style="background-color:violet;color:black;">violet</td>
    </tr>
    <tr>
        <td style="background-color:white;color:black;">white</td>
        <td style="background-color:yellow;color:black;">yellow</td>
        <td></td>
        <td></td>
    </tr>
</table>

If you want other colors, you can define them with `\usepackage{xcolor}`
and `\definecolor{name}{model}{color-spec}` where:

<ul>
    <li>name is the name of the color you want to define,</li>
    <li>model is the color space (gray, rgb, RGB, HTML, cmyk)</li>
    <li>color-spec is the definition of the color in the chosen model</li>
</ul>

For example:

```tex
\definecolor{orange}{HTML}{FF7F00}
\definecolor{orange}{rgb}{1,0.5,0}
\definecolor{orange}{RGB}{255,127,0}
\definecolor{orange}{cmyk}{0,0.5,1,0}
```

You can find suitable colors with a [color picker](http://www.colorpicker.com/)


## See also

* Wikibooks: [LaTeX/Colors](https://en.wikibooks.org/wiki/LaTeX/Colors)
