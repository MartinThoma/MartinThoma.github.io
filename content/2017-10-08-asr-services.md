---
layout: post
title: ASR Services
slug: asr-services
author: Martin Thoma
date: 2017-10-08 20:00
category: Machine Learning
tags: Machine Learning, ASR, Service
featured_image: logos/ml.png
---
Automatic Speech Recognition (ASR) is really difficult to set up yourself.
There are some toolkits like [CMU Sphinx](https://en.wikipedia.org/wiki/CMU_Sphinx)
and [others](https://en.wikipedia.org/wiki/List_of_speech_recognition_software),
but the last time I checked (some years ago) they either didn't really work or
I couldn't manage to get them running.


## How does ASR work?

One way to do ASR is the following:

* Lets say you have an audio file of 5 minutes
* You split them into frames, e.g. 30ms per frame. Those frames overlap e.g. 5ms.
* You extract features for each frame, e.g. Cepstral features
* You calculate the probability of phonemes / subphonemes for each frame, e.g.
  with a Gausian model. This part is called the **acoustic model**.
* **Pronounication models** (e.g. HMMs) are applied to find possible word
  sequences.
* The most likely word sequence is calculated. Here the **language model**
  comes into play. That is basically only a counter some important
  details (out of vocabulary, backoff)


The acoustic model "maps" the sounds to phonemes. One can build an acoustic
model for each speaker / environment to improve the recognition quality.

The language model rather depends on the context. It contains the information
which words exist at all, how often they occur and which words are likely to
appear together.

## Why is ASR hard?

There is much variability in a single sentence:

* Differences in the speaker:
    * Intonation
    * Volume: It sounds completely different when you whisper something compared to
              normal speech compared to yelling.
    * Speed: You can speak extra slow / fast
    * Mumbling
* Different microphones
* Different environment:
    * Background noises
    * Small vs big room
    * Echo
    * Other speakers (the [cocktail party problem](https://en.wikipedia.org/wiki/Cocktail_party_effect))
* Other
    * Noise vs speech vs "silence"
    * Speech vs sneezing vs clearing the throat vs drinking

If you want to recognize speech in real time (e.g. only 3 seconds after the
utterance) it is much more harder. The reason is that you can't use the
context.

Think of [homophones](https://en.wikipedia.org/wiki/Homophone). For example,
when a person says

> Whole grain food

compared to

> Hole!

If you stop after "whole" / "hole" it is almost impossible to know which one
is meant. If you know the next word ("grain") then "hole" does not make any
sense anymore. So: Context matters. A lot.


## What are related tasks?

Besides simple speech to text, there are a couple of other interesting related
tasks:

* **Language identification**: Sometimes it is clear from the context, but
  for other applications you might not know which language the speaker(s) is/are
  using.
* **Speaker identification**: Who said what? How many speakers do we have in the
  first place?
* **Emotion recognition**: How does the speaker feel? Excited? Angry?
  By comparing the voice with the words used one can also try to recognize
  sarcasm.

A question which has to be answered in each task is how close the transcript should
be to the speech. For example, is the transcript

> I <SILENCE> think you <throat clearing> you're very smart.

or rather the transcript

> I think you're very smart.

wanted? The first one is closer to the utterance, the second one much easier to
read. It is also likely that follow-up sysystem work better with the second
one.


## ASR Services

I looked for a short piece of German discussion and found one with 1 minutes
and 17 seconds from the TV series *King of Queens* ("Messerscharfe Logik")
between the characers Arthur and Spence.

I created the following transcript from it:

> 0:00 - 0:03, background: &lt;MUSIC&gt;
>
> 0:03 - 0:07, Spence: "Hey Arthur, was ist? Haben Sie Lust mit ins Kino zu kommen?"
>
> 0:07 - 0:09, Arthur: "Was soll das? Ich könnte dem Film gar nicht folgen."
>
> 0:09 - 0:13, background: &lt;LAUGHING&gt;
>
> 0:14 - 0:14, Spence: "Was? "
>
> 0:14 - 0:15, Arthur: "Ich verlier meinen Verstand, schon vergessen?"
>
> 0:15 - 0:18, Arthur: "Dieser hübsche Comic da könnte ebenso in Griechisch sein"
>
> 0:18 - 0:20, background: &lt;LAUGHING&gt;
>
> 0:19 - 0:23, Spence: "Arthur, Sie verlieren nicht den Verstand. Sie reden das nur ein!"
>
> 0:23 - 0:25, Arthur: "Dann werden wir das jetzt mal Testen!"
>
> 0:25 - 0:26, Spence: "Wie?"
>
> 0:26 - 0:32, Arthur: "Ich war immer in der Lage über jedes Thema zu diskutieren und konnte gegnerische Argumente mit messerscharfer Logik abwehren."
>
> 0:32 - 0:34, Spence: "Sie wollen, dass ich mit ihnen diskutiere?"
>
> 0:33 - 0:34, Arthur: "Ganz genau!"
>
> 0:34 - 0:37, Arthur: "Wir werden uns ein Thema aussuchen und dann sehen wir ob ich meinen Mann stehen kann."
>
> 0:37 - 0:40, Spence: "Ok, und wie lautet das Thema?"
>
> 0:41 - 0:46, Arthur: "Wie wär es damit: Sollten die Vereinigten Staaten die Beziehung zu Kuba normalisieren?"
>
> 0:46 - 0:47, Arthur: "Du bist dafür!"
>
> 0:47 - 0:47, Spence: "Na schön."
>
> 0:47 - 0:48, Spence: "Ääääh"
>
> 0:48 - 0:56, Spence: "Der kalte Krieg ist seit 10 Jahren vorbei, Kuba ist keine Bedrohung mehr, könnte stattdessen aber ein Verbündeter und guter Handelspartner werden."
>
> 0:56 - 0:59, Spence: "Es wäre also vernünftig die Beziehung zu Kuba zu normalisieren."
>
> 1:00 - 1:04, Arthur (angry): "Du verdammter Blödmann, was weißt du denn schon?"
>
> 1:04 - 1:05, Background: &lt;LAUGHING&gt;
>
> 1:04 - 1:08, Arthur (angry): "Du bist ein elender Schmarotzer, der nicht mal eine Frau kriegen kann."
>
> 1:08 - 1:10, Background: &lt;LAUGHING&gt;
>
> 1:08 - 1:09, Arthur (angry): "Wenn du unbedingt etwas normalisieren willst, warum fängst du dann nicht mit deinem Gesicht an!"
>
> 1:11 - 1:17, Background: &lt;LAUGHING&gt;
>
> 1:14 - 1:15, Arthur (happy): "Ich kann es noch!"

By the way, a good example for the question how close one should be to the
original is "Ich verlier meinen Verstand". That is colloquial language. Correct
would be "Ich verliere meinen Verstand".

It is also an example that people interrupt each other. Sometimes Arthur and
Spence speak at the same time although it does not sound to us as if it is the
case. In fact, I only noticed it when I created the transcript.

### Pythons SpeechRecognition Package

I will use the [SpeechRecognition package](https://pypi.python.org/pypi/SpeechRecognition/)
in the latest version (3.7.1) to interact with services. I will use Python&nbsp;3
for the rest.

To install it, run

```shell
$ sudo -H pip install SpeechRecognition --upgrade
$ sudo -H pip install pocketsphinx
```

### Pocketsphinx

Installation:

Now follow [this guide](https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst#notes-on-the-structure-of-the-language-data) to get support
for German. You only have to download some files from Sourceforge and add them
to the right directory with the right name. At the end, the folder
`/usr/local/lib/python3.5/dist-packages/speech_recognition/pocketsphinx-data/de-DE`
should contain the following files:

```text
.
├── acoustic-model
│   ├── feat.params
│   ├── feature_transform
│   ├── mdef
│   ├── means
│   ├── mixture_weights
│   ├── noisedict
│   ├── transition_matrices
│   └── variances
├── language-model.lm.bin
└── pronounciation-dictionary.dict
```

Script:

```python
#!/usr/bin/env python3

"""Recognize speech using CMU Sphinx (local)."""

# 3rd party modules
import speech_recognition as sr


def recognize(filepath, language=None):
    """
    Transcribe an audio file to text.

    Parameters
    ----------
    filepath : str
        Path to a WAV file
    language : str, optional (default: English)

    Returns
    -------
    text : str
    """
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source)  # read the entire audio file

    return r.recognize_sphinx(audio, language=language)


def main():
    try:
        text = recognize("input.wav", language="de-DE")
        print(text)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


if __name__ == "__main__":
    main()
```

which results in:

```text
hätten und ländern der erwerb des handels mit ins kino zu beantragen was soll
ich ich könnte mit dem land folgen gehabt das heißt die für mein verstand schon
vergessen gürtel kommentare und ebenso in sicher schaffen erhard war sie
verlieren nicht den verstand sie reden sich das nein dann werden wir das
weitesten die ich war immer in der lage über jedes thema zu diskutieren konnte
gegnerische argument in das verfasser logik abwehr sie wollen dass ich mit
ihnen diskutieren flora gegenseitigen aussuchen und dann sehen wir auch ich
mein mann stehen kann und den verlauf des themen widerstand sollten die
vereinigten staaten den beziehungen zu kuba normalisierung brüssel für erstellt
der der kalte krieg ist seit zehn jahren vorbei in sobald keine bedrohung mehr
könnte statt dessen ein verbündeter oder handels partner werden es mir also
vernünftig die beziehungen zu kuba zu normalisierung so sei dank der
arbeitsleistung es um gewinne durch eine länder schwarze eigentlich war es auch
die anderer wenn dominiert das normalisiert ins auge sechs landwirte angesichts
allgemeine haltung ich kann es noch für europa
```

This is bad for many reasons:

* The transcript is utterly wrong: For some parts you can notice that it does
  something right, but overall the result is not usable.
* No punctuation
* No speaker recognition
* (No background noises)
* It takes 38s on a Thinkpad T460p with Ubuntu 16.04 and Python&nbsp;3.


### Microsoft Cognitive Services

Starting at the [start page](https://azure.microsoft.com/de-de/services/cognitive-services/speech/),
I first had to [create an Azure account](https://portal.azure.com). You
will need a credit card (pre-paid credit cards are not accepted).

Microsoft knows the following 10 languages for conversation mode ([source](https://docs.microsoft.com/en-us/azure/cognitive-services/speech/api-reference-rest/bingvoicerecognition)):

<table class="table">
<thead>
<tr>
<th>Code</th>
<th>Language</th>
<th>Code</th>
<th>Language</th>
</tr>
</thead>
<tbody>
<tr>
<td>ar-EG</td>
<td>Arabic (Egypt), modern standard</td>
<td>It-IT</td>
<td>Italian (Italy)</td>
</tr>
<tr>
<td>de-DE</td>
<td>German (Germany)</td>
<td>ja-JP</td>
<td>Japanese (Japan)</td>
</tr>
<tr>
<td>en-US</td>
<td>English (United States)</td>
<td>pt-BR</td>
<td>Portuguese (Brazil)</td>
</tr>
<tr>
<td>es-ES</td>
<td>Spanish (Spain)</td>
<td>ru-RU</td>
<td>Russian (Russia)</td>
</tr>
<tr>
<td>fr-FR</td>
<td>French (France)</td>
<td>zh-CN</td>
<td>Chinese (Mandarin, simplified)</td>
</tr>
</tbody>
</table>

Please note that there are many more for interactive and dictation mode.

The following code is used to create a transcript:

```python
#!/usr/bin/env python3

"""Recognize speech using Microsoft Bing Voice Recognition."""

# 3rd party modules
import speech_recognition as sr


def recognize_bing(filepath, bing_key, language=None):
    """
    Transcribe an audio file to text.

    Parameters
    ----------
    filepath : str
        Path to a WAV file
    bing_key : str
        32-character lowercase hexadecimal string from https://portal.azure.com
    language : str, optional (default: English)

    Returns
    -------
    text : str
    """
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source)  # read the entire audio file

    return r.recognize_bing(audio, key=bing_key, language=language)


def main():
    # Microsoft Bing Voice Recognition API uses keys which are
    # 32-character lowercase hexadecimal strings
    bing_key = "INSERT YOUR BING KEY HERE"
    try:
        text = recognize_bing("input.wav", bing_key=bing_key, language="de-DE")
        print(text)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


if __name__ == "__main__":
    main()
```

This resulted in

```text
Reaser Was ist haben sie Lust mit dem Kino zu kommen war schon dass ich könnte
den Film gar nicht folgen.
```

and took only 2.6s. It only recognized the first part because the
SpeechRecognition package uses the REST interface instead of the WebSocket
interface. The REST interface is limited to 15 seconds of audio ([source](https://docs.microsoft.com/de-de/azure/cognitive-services/speech/home)).

By default, SpeechRecognition package uses the endpoint

> https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1

Changing this to `conversation` changes the result to

```text
Die erster Was ist haben sie Lust mit dem Kino zu kommen war schon dass ich
könnte den Film gar nicht folgen
```

### Google

The script

```python
#!/usr/bin/env python3

"""Recognize speech using Googles ASR Service."""

# 3rd party modules
import speech_recognition as sr


def recognize_google(filepath, language=None):
    """
    Transcribe an audio file to text.

    Parameters
    ----------
    filepath : str
        Path to a WAV file
    language : str, optional (default: English)

    Returns
    -------
    text : str
    """
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source)  # read the entire audio file

    return r.recognize_google(audio, language=language)


def main():
    try:
        text = recognize_google("input.wav", language="de-DE")
        print(text)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


if __name__ == "__main__":
    main()
```

results in

```text
Sphinx error; recognition connection failed: [Errno 32] Broken pipe
```


### Google Cloud

See [documentation of Google cloud speech API](https://cloud.google.com/speech/)
and the [developers page](https://developers.google.com/apis-explorer/?hl=de#p/speech/v1/).

It can only be used for commerical purposes, so I can't try it right now.
The command is

```python
r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
```


### IBM

IBM has a speech recognition service, see [starting page](https://www.ibm.com/watson/services/speech-to-text/).
But looking at [this page](https://speech-to-text-demo.mybluemix.net), it seems
as if it only supports

* Arabic
* English (GB and US)
* French
* Japanese
* Mandarin
* Portuguese
* Spanish

As it doesn't support German, I didn't continue here.


### Wit.ai

The service [wit.ai](https://wit.ai/) seems to be much simpler to use. You set
the language over the web interface.


```python
#!/usr/bin/env python3

"""Recognize speech using wit.ai ASR Service."""

# 3rd party modules
import speech_recognition as sr


def recognize_wit(filepath, key):
    """
    Transcribe an audio file to text.

    Parameters
    ----------
    filepath : str
        Path to a WAV file
    key : str

    Returns
    -------
    text : str
    """
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source)  # read the entire audio file

    return r.recognize_wit(audio, key=key)


def main():
    server_access_token = "12ABCDEFGHIJKLMNOPQRSTUVWXYZABCD"
    try:
        text = recognize_wit("input.wav", key=server_access_token)
        print(text)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


if __name__ == "__main__":
    main()
```

results in

```text
ey Alter was ist haben Sie Lust mit dem Kino zu kommen ich könnte den Film gar
nicht folgen ich verliere meinen Verstand schon vergessen dieser Hitze komme
ich da könnte ebenso in Griechisch sie verlieren den Verstand die reden dann
werden wir das jetzt
```

What is good:

* The transcript is mostly right.

What is ok:

* It took 19s for this. This is about the same time as playing the audio takes.

What is bad:

* No punctuation
* No speaker recognition
* (No background noises)


### Houndify

Houndify has a [Python SDK](https://docs.houndify.com/sdks/docs/python). It
seems not to be possible to change the language. It reminds me very much of
Alexa Skills.

Trying it with the SpeechRecognition package yields

```text
Sphinx error; recognition request failed: Bad Gateway
```

I don't think I'll put more time in that one.


## Related

* KIT Lecture [Grundlagen der Automatischen Spracherkennung](https://www.youtube.com/watch?v=umzIFcf6IX0&list=PLfk0Dfh13pBNTFz-RnOlgYIPv3UbJ3upf) WS 2016/17 as a YouTube playlist