#!/usr/bin/env python
# encoding: utf-8

"""Convert Markdown pages from Jekyll format to the Pelican format."""

import os


def categories_and_tags(filename):
    """
    Parse all Markdown files and overwrite them in the desired format.

    This script assumes your header looks like this (same order):

    ---
    layout: post
    title: Migrate from Jekyll to Pelican
    author: Martin Thoma
    date: 2014-11-22 17:19
    categories:
    - Cyberculture
    tags:
    - Jekyll
    - Blogging
    featured_image: logos/star.png
    ---
    """
    with open(filename) as f:
        lines = f.read().split("\n")
    tags_i = None
    category_i = None
    last_tag_i = None
    tags = []
    categories = []
    seen_dashes = 0
    categories_ended = False
    for i, line in enumerate(lines):
        line_ = line.strip()
        if line_ == "---":
            seen_dashes += 1
        if seen_dashes == 2:
            break
        if line_ == "category:" or line_ == "categories:":
            category_i = i
        elif line_.startswith("category:"):
            category_i = i
            categories = [line_[len("category:") :].strip()]
        if category_i and line_.startswith("-") and not categories_ended:
            categories.append(line_[1:].strip())  # Get right of leading '- '
        if line_ == "tags:":
            categories_ended = True
            tags_i = i
        elif line_.startswith("tags:"):
            tags = [line_[len("tags:") :].strip()]
        if tags_i and line_.startswith("-"):
            tags.append(line_[1:].strip())
            last_tag_i = i
    print(filename)

    tags_ = tags

    if len(categories) == 1:
        category = categories[0]
    else:
        print(
            "WARNING: '%s' has categories %i (%s)"
            % (filename, len(categories), categories)
        )

    txt = ""
    txt += "\n".join(lines[:category_i]) + "\n"
    txt += "category: %s\n" % category
    txt += "tags: %s\n" % ", ".join(tags_)

    if last_tag_i:
        txt += "\n".join(lines[last_tag_i + 1 :])
    else:
        txt += "\n".join(lines[category_i + len(categories) + 1 :])

    with open(filename, "w") as o:
        o.write(txt)


def math(filename):
    """
    Convert math mode indicators.

    \(...\) to $...$
    \[...\] to $$...$$$
    """
    import re

    with open(filename) as f:
        content = f.read()

    backslash = "\\\\"

    single_math = re.compile(2 * backslash + "\((.+?)" + 2 * backslash + "\)")
    content = single_math.sub(lambda m: "${math}$".format(math=m.group(1)), content)

    single_math = re.compile(backslash + "\((.+?)" + backslash + "\)")
    content = single_math.sub(lambda m: "${math}$".format(math=m.group(1)), content)

    single_math = re.compile(2 * backslash + "\[(.+?)" + 2 * backslash + "\]")
    content = single_math.sub(lambda m: "$${math}$$".format(math=m.group(1)), content)

    single_math = re.compile(backslash + "\[(.+?)" + backslash + "\]")
    content = single_math.sub(lambda m: "$${math}$$".format(math=m.group(1)), content)

    with open(filename, "w") as o:
        o.write(content)


def captiontag(filename):
    """
    Convert Liquid captiontags to HTML.

    {% caption align="aligncenter"
       width="512"
       caption="Let Diamonds slide down"
       url="../images/2013/05/falling-diamonds-slide.jpg"
       alt="Let Diamonds slide down"
       height="254"
       class="size-full wp-image-65441" %}


    """
    import re

    with open(filename) as f:
        content = f.read()

    captiontag = re.compile(
        '\{%\s+caption align="aligncenter"\s+'
        'width="(.+?)"\s+caption="(.+?)"\s+'
        'url="(.+?)"\s+alt="(.+?)"\s+'
        'height="(.+?)"\s+class="(.+?)"\s+%\}'
    )
    content = captiontag.sub(
        lambda m: """<figure class="aligncenter">
            <a href="{url}"><img src="{url}" alt="{alt}" style="max-width:{width}px;max-height:{height}px" class="{classl}"/></a>
            <figcaption class="text-center">{caption}</figcaption>
        </figure>""".format(
            classl=m.group(6),
            url=m.group(3),
            alt=m.group(4),
            caption=m.group(2),
            width=m.group(1),
            height=m.group(5),
        ),
        content,
    )

    captiontag = re.compile(
        '\{%\s+caption align="aligncenter"\s+'
        'width="(.+?)"\s+alt="(.+?)"\s+text="(.+?)"\s+'
        'url="(.+?)"\s+%\}'
    )
    content = captiontag.sub(
        lambda m: """<figure class="aligncenter">
            <a href="{url}"><img src="{url}" alt="{alt}" style="max-width:{width}px;" class=""/></a>
            <figcaption class="text-center">{caption}</figcaption>
        </figure>""".format(
            url=m.group(4), alt=m.group(2), caption=m.group(3), width=m.group(1)
        ),
        content,
    )

    captiontag = re.compile(
        '\{%\s+caption align="(.+?)"\s+'
        'width="(.+?)"\s+caption="(.+?)"\s+url="(.+?)"\s+'
        'alt="(.+?)"\s+height="(.+?)"\s+class="(.+?)"\s+%\}'
    )
    content = captiontag.sub(
        lambda m: """<figure class="{alignc}">
            <a href="{url}"><img src="{url}" alt="{alt}" style="max-width:{width}px;max-height:{height}px;" class="{classimg}"/></a>
            <figcaption class="text-center">{caption}</figcaption>
        </figure>""".format(
            alignc=m.group(1),
            url=m.group(4),
            alt=m.group(5),
            caption=m.group(3),
            width=m.group(2),
            height=m.group(6),
            classimg=m.group(7),
        ),
        content,
    )

    captiontag = re.compile(
        '\{%\s+caption align="(.+?)"\s+'
        'width="(.+?)"\s+caption="(.+?)"\s+url="(.+?)"\s+'
        'alt="(.+?)"\s+height="(.+?)"\s+class="(.+?)"\s+%\}'
    )
    content = captiontag.sub(
        lambda m: """<figure class="{alignc}">
            <a href="{url}"><img src="{url}" alt="{alt}" style="max-width:{width}px;max-height:{height}px;" class="{classimg}"/></a>
            <figcaption class="text-center">{caption}</figcaption>
        </figure>""".format(
            alignc=m.group(1),
            url=m.group(4),
            alt=m.group(5),
            caption=m.group(3),
            width=m.group(2),
            height=m.group(6),
            classimg=m.group(7),
        ),
        content,
    )

    captiontag = re.compile(
        "\{%\s+caption "
        'align="(.+?)"\s+'
        'width="(.+?)"\s+'
        'caption="(.+?)"\s+'
        'url="(.+?)"\s+'
        'alt="(.+?)"\s+'
        'height="(.+?)"\s+'
        'class="(.+?)"\s+%\}'
    )
    content = captiontag.sub(
        lambda m: """<figure class="{alignc}">
            <a href="{url}"><img src="{url}" alt="{alt}" style="max-width:{width}px;max-height:{height}px;" class="{classimg}"/></a>
            <figcaption class="text-center">{caption}</figcaption>
        </figure>""".format(
            alignc=m.group(1),
            url=m.group(4),
            alt=m.group(5),
            caption=m.group(3),
            width=m.group(2),
            height=m.group(6),
            classimg=m.group(7),
        ),
        content,
    )

    captiontag = re.compile(
        "\{%\s+caption "
        'align="(.+?)"\s+'
        'width="(.+?)"\s+'
        'text="(.+?)"\s+'
        'url="(.+?)"\s+'
        'alt="(.+?)"\s+'
        'title=".+?"\s+'
        'height="(.+?)"\s+'
        'class="(.+?)"\s+%\}'
    )
    content = captiontag.sub(
        lambda m: """<figure class="{alignc}">
            <a href="{url}"><img src="{url}" alt="{alt}" style="max-width:{width}px;max-height:{height}px;" class="{classimg}"/></a>
            <figcaption class="text-center">{caption}</figcaption>
        </figure>""".format(
            alignc=m.group(1),
            url=m.group(4),
            alt=m.group(5),
            caption=m.group(3),
            width=m.group(2),
            height=m.group(6),
            classimg=m.group(7),
        ),
        content,
    )

    captiontag = re.compile(
        "\{%\s+caption "
        'align="(.+?)"\s+'
        'width="(.+?)"\s+'
        'alt="(.+?)"\s+'
        'caption="(.+?)"\s+'
        'url="(.+?)"\s+'
        "%\}"
    )
    content = captiontag.sub(
        lambda m: """<figure class="{alignc}">
            <a href="{url}"><img src="{url}" alt="{alt}" style="max-width:{width}px;"/></a>
            <figcaption class="text-center">{caption}</figcaption>
        </figure>""".format(
            alignc=m.group(1),
            url=m.group(5),
            alt=m.group(3),
            caption=m.group(4),
            width=m.group(2),
        ),
        content,
    )

    with open(filename, "w") as o:
        o.write(content)


def codelisting(filename):
    """
    Convert Liquid captiontags to HTML.

    {% highlight bash %}packstrap -i /mnt base base base-dvl{% endhighlight %}


    """
    import re

    with open(filename) as f:
        content = f.read()

    captiontag = re.compile(
        "\{% highlight (.+?) %\}(.+?)" "{% endhighlight %}", re.DOTALL
    )
    content = captiontag.sub(
        lambda m: """```{language}
{content}
```""".format(
            language=m.group(1), content=m.group(2)
        ),
        content,
    )

    with open(filename, "w") as o:
        o.write(content)


def fixtitles(filename):
    """Fix titles such as "title: ! 'Tricks with .htaccess '"."""
    with open(filename) as f:
        lines = f.read().split("\n")

    counter = 0
    for i, line in enumerate(lines):
        if line == "---":
            counter += 1
        if line.startswith("title: ! "):
            lines[i] = "title: %s" % line[len("title: ! '") : -1].strip()
        if counter == 2:
            break

    with open(filename, "w") as o:
        o.write("\n".join(lines))


if __name__ == "__main__":
    filenames = filter(lambda x: x.endswith(".md"), os.listdir("."))
    for filename in sorted(filenames):
        categories_and_tags(filename)
        math(filename)
        captiontag(filename)
        codelisting(filename)
        fixtitles(filename)
