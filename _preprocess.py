#!/usr/bin/env python
import re, fnmatch, os

def replaceLatex(file_path):
    #read file content
    with open(file_path) as f:
        content = f.read()

    #replace $..$ by <div>$..$</div> and $$..$$ by <div>$$..$$</div>
    import re
    # first two dollar signs
    content = re.sub(r'(?<!\<span\>)\$\$([^\$]*)\$\$', "<div>$$\g<1>$$</div>", content)
    content = re.sub(r'(?<!\<span\>)(?<!\$)\$([^\$]+)\$', "<span>$\g<1>$</span>", content)

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
