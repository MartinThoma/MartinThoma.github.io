---
layout: post
title: Make Python Objects JSON serializable
slug: make-json-serializable
author: Martin Thoma
date: 2018-06-27 20:00
category: Code
tags: Python, Software Development, JSON
featured_image: logos/python.png
---
When you're developing a service which has to communicate with a REST endpoint,
it is very likely that it will come in handy if you can convert some of your
objects to JSON (and back). Until recently, I always created a dictionary and
used `json.dumps` in that case. Also, when I wanted to log an object to
AWS Cloudwatch which has structured logs (json logs).


Instead of doing it completely manually, you should use a pattern described
by [jaraco](https://github.com/simplejson/simplejson/issues/52#issuecomment-23667961)
(and fixed by me):


```
class MyCustom(object):
    def __json__(self):
        return {
            'a': self.a,
            'b': self.b,
            '__python__': 'mymodule.submodule:MyCustom.from_json',
        }

    for_json = __json__  # supported by simplejson

    @classmethod
    def from_json(cls, json):
        obj = cls()
        obj.a = json['a']
        obj.b = json['b']
        return obj
```

With that, the following workflow is possible:

```
import simplejson

obj = MyCustom()
obj.a = 3
obj.b = 4

json = simplejson.dumps(obj, for_json=True)

# Two-step loading
obj2_dict = simplejson.loads(json)
obj2 = MyCustom.from_json(obj2_dict)

# Make sure we have the correct thing
assert isinstance(obj2, MyCustom)
assert obj2.__dict__ == obj.__dict__
```

Note that we need two steps for loading. For now, the `__python__` property
is not used.
