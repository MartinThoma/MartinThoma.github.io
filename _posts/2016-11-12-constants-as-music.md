---
layout: post
title: Constants as Music
slug: constants-as-music
author: Martin Thoma
date: 2016-11-12 20:00
category: Cyberculture
tags: Python, music
featured_image: logos/music.png
---

I've just seen the following video

<iframe width="512" height="288" src="https://www.youtube-nocookie.com/embed/wK7tq7L0N8E?rel=0" frameborder="0" allowfullscreen></iframe>

and I wondered how hard it was to automatically generate this myself only with
software. Turns out, it is super easy.


## Python

You have to install `MIDIUtil`:

```bash
$ sudo pip install MIDIUtil
```

and then you can execute the following code:

```python
#!/usr/bin/env python

from midiutil.MidiFile import MIDIFile

# Just an example
try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp
mp.dps = 1000  # set number of digits

# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(1)

track = 0
channel = 0


pitch = 60
time = 0
duration = 1
volume = 100
for digit in str(mp.pi):
    if digit == '.':
        continue
    MyMIDI.addNote(track, channel, pitch + int(digit), time, duration, volume)
    time += 1
    if time == 180:
        break

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

```

This will make the first 180 digits of $\pi$ to a MIDI file.

See [MIDIUtil docs](http://midiutil.readthedocs.io/en/latest/) for more
information.


## Create MP3

I use `timidity` to create a `.wav` and then `lame` to convert it to mp3:

```
$ timidity -Ow -o output.wav output.mid
$ lame output.wav pi.mp3
```

For YouTube, I had to convert it to avi:

```
$ ffmpeg -loop 1 -r 1 -i pi.jpg -i pi.mp3 -c:a copy -shortest pi.avi
```


## Examples

$\pi$:

<iframe width="512" height="288" src="https://www.youtube-nocookie.com/embed/FQOcFjFdFWc?rel=0" frameborder="0" allowfullscreen></iframe>

It sounds much more intersting if you play two versions of it simultaneously, starting at different points:

<iframe width="512" height="288" src="https://www.youtube-nocookie.com/embed/-rRIg95QJHc?rel=0" frameborder="0" allowfullscreen></iframe>

$e$:

<iframe width="512" height="288" src="https://www.youtube-nocookie.com/embed/URnjSCYupu4?rel=0" frameborder="0" allowfullscreen></iframe>

$\sqrt{2}$

<iframe width="512" height="288" src="https://www.youtube-nocookie.com/embed/DKPSRozxUHA?rel=0" frameborder="0" allowfullscreen></iframe>

## Ideas

You could reserve one digit for meta-choices, e.g. making 0 a control character.
If 0 is followed by...

<ul>
     <li>... 0, all modifiers are reset</li>
     <li>... 1, the pitch is doubled all the time</li>
     <li>... 2, the pitch is doubled for 10 notes</li>
     <li>... 3, `time = time - 5.5`</li>
     <li>... 4, `tempo = tempo*2`</li>
     <li>... 5, `tempo = tempo*4</li>
     <li>... 6, `tempo = tempo - 10</li>
     <li>... 7, volume increases in as many beats as the next two digits indicate</li>
     <li>... 8, volume decreases by 10 in the next 2 seconds</li>
     <li>... 9, duration is doubled</li>
 </ul>

Let me know if you made something that sounds interesting :-)
