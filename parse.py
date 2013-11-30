def parse(text):
    splitpoints = []

    # parse
    isOpen = False
    for i, char in enumerate(text):
        if char == '"':
            isOpen = not isOpen
        if char == " " and not isOpen:
            splitpoints.append(i)

    # build data structure
    dictionary = {}
    last = 0
    for i in splitpoints:
        key, value = text[last:i].split('=')
        last = i+1
        dictionary[key] = value[1:-1] # remove delimiter
    return dictionary

print(parse('align="aligncenter" width="500" alt="WER calculation" text="WER calculation" url="../images/2013/11/WER-calculation.png"'))
