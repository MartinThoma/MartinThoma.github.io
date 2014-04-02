#!/usr/bin/env python
import re, fnmatch, os

def replaceLatex(file_path):
    #read file content
    with open(file_path) as f:
        content = f.read()

    """Replace $..$ by `$..$` and $$..$$ by `$$..$$`, but
        * Don't replace \$ (\ should escape)
        * Don't replace if one of the patterns above is in code blocks:
            ```
            ....
            ...   $...$
            ```
          or
            {% highlight [some language] %}
            ... 
            ...  $...$
            {% endhighlight %}
    """
    import re
    # first two dollar signs environment
    content = re.sub(r'(?<![\\])\$\$([^\$]+)\$\$', "`\n$$\g<1>$$`", content)
    # then one dollar sign environment
    content = re.sub(r'(?<!\<span\>)(?<!\$)\$([^\$]+)\$', "`$\g<1>$`", content)

    content = content.split("\n")
    is_in_codeblock = False

    for i, line in enumerate(content):
        if line.startswith("```"):
            is_in_codeblock = not is_in_codeblock
        elif is_in_codeblock:
            content[i] = content[i].replace("`$", "$")
            content[i] = content[i].replace("$`", "$")

    content = "\n".join(content)

    #write without whitespace
    with open(file_path,'w') as f:
        f.write(content)

# Get all HTML files
files = []
for root, dirnames, filenames in os.walk('./_posts/'):
  for filename in fnmatch.filter(filenames, '*'):
      files.append(os.path.join(root, filename))

for filename in files:
    replaceLatex(filename)
