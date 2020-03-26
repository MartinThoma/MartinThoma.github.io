---
layout: post
title: Microsoft Vision API
author: Martin Thoma
date: 2016-03-31 14:49
category: Cyberculture
tags: Machine Learning, Microsoft
featured_image: logos/ml.png
---
Microsoft just released a Computer Vision API. I tried it with a couple of
[Unidentified objects](https://commons.wikimedia.org/wiki/Category:Unidentified_objects)
of Wikipedia and was not really impressed.

Here is how to use it:

```python
#!/usr/bin/env python

"""Example how to use the Microsoft Vision API."""

import httplib
import urllib
import json

headers = {
    "Content-type": "application/json",
}

params = urllib.urlencode(
    {
        # Specify your subscription key
        "subscription-key": "yourhexadecimalone11111111111111",
        # Specify values for optional parameters, as needed
        "visualFeatures": "All",
    }
)

try:
    image_url = "http://www.martin-thoma.de/bilder/Martin_Thoma_web_thumb.jpg"

    conn = httplib.HTTPSConnection("api.projectoxford.ai")
    conn.request(
        "POST", "/vision/v1/analyses?%s" % params, "{'Url': '%s'}" % image_url, headers
    )
    response = conn.getresponse()
    data = response.read()
    data = json.loads(data)
    print(json.dumps(data, sort_keys=True, indent=2))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
```

which gives

```text
{
  "adult": {
    "adultScore": 0.01073759701102972,
    "isAdultContent": false,
    "isRacyContent": false,
    "racyScore": 0.015348214656114578
  },
  "categories": [
    {
      "name": "people_",
      "score": 0.8359375
    }
  ],
  "color": {
    "accentColor": "4C5F37",
    "dominantColorBackground": "Green",
    "dominantColorForeground": "Green",
    "dominantColors": [
      "Green"
    ],
    "isBWImg": false
  },
  "faces": [
    {
      "age": 28,
      "faceRectangle": {
        "height": 49,
        "left": 53,
        "top": 42,
        "width": 49
      },
      "gender": "Male"
    }
  ],
  "imageType": {
    "clipArtType": 0,
    "lineDrawingType": 0
  },
  "metadata": {
    "format": "Jpeg",
    "height": 200,
    "width": 134
  },
  "requestId": "7f0af611-1750-4fa2-aa47-a03db286f6a7"
}
```

## See also

* [Cognitive Services](https://www.microsoft.com/cognitive-services/en-us/subscriptions): You have to apply there. 5,000 transactions per month, 20 per minute is for free.
* [The 86-category concept](https://www.microsoft.com/cognitive-services/en-us/computer-vision-api/documentation/analyzeimage)
* [Computer Vision API - v1.0](https://dev.projectoxford.ai/docs/services/56f91f2d778daf23d8ec6739/operations/56f91f2e778daf14a499e1fa)