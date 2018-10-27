---
layout: post
title: Python property
slug: python-property
author: Martin Thoma
date: 2018-10-19 20:00
category: Code
tags: Python
featured_image: logos/python.png
---
Python has a built-in decorator `@property`. It was introduced as a way to add
getters / setters in a backwards-compatible way to simple attributes of a
class.

For example, you could have a class

```
def Location(object):

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
```


## Getters and Setters

Let's say, you want to add a range check. So you could make something like:

```
class Location(object):

    def __init__(self, longitude, latitude):
        self.set_latitude(latitude)
        self.set_longitude(longitude)

    def set_latitude(self, latitude):
        if not (-90 <= latitude <= 90):
            raise ValueError('latitude was {}, but has to be in [-90, 90]'
                             .format(latitude))
        self.latitude = latitude

    def set_longitude(self, longitude):
        if not (-180 <= longitude <= 180):
            raise ValueError('longitude was {}, but has to be in [-180, 180]'
                             .format(longitude))
        self.longitude = longitude

```

which would then be called like this:

```
my_position = Location(48.137222222222, 11.575555555556)

# Update after a while
my_position.set_latitude(48.2)
my_position.set_longitude(42.6)
```

This is what Java developers would do and it feels rather weird to Python.


## Property class

With Python 2.2, the `property` class was added to simplify it ([source](https://www.python.org/download/releases/2.2.2/descrintro/#property)).

With that, you can change the class to

```
class Location(object):

    def __init__(self, longitude, latitude):
        self.set_latitude(latitude)
        self.set_longitude(longitude)

    def set_latitude(self, latitude):
        if not (-90 <= latitude <= 90):
            raise ValueError('latitude was {}, but has to be in [-90, 90]'
                             .format(latitude))
        self._latitude = latitude

    def set_longitude(self, longitude):
        if not (-180 <= longitude <= 180):
            raise ValueError('longitude was {}, but has to be in [-180, 180]'
                             .format(longitude))
        self._longitude = longitude

    def get_longitude(self):
        return self._latitude

    def get_latitude(self):
        return self._longitude

    latitude = property(get_latitude, set_latitude)
    longitude = property(get_latitude, set_latitude)


# Usage
my_position = Location(48.137222222222, 11.575555555556)

my_position.latitude = 48.2
my_position.longitude = 42.6

my_position.latitude = 123  # Fails

```

<div class="info">You should note the single leading underscore - that is Pythons way to denote private properties. It is not meant as the public interface of the class.

There is also a leading double underscore. The interpreter changes the name of the attribute to prevent naming colisions. Just have a look at `dir(some_example_class)`. See also: [What's the meaning of underscores (_ & __) in Python variable names?](https://www.youtube.com/watch?v=ALZmCy2u0jQ)</div>

And then note how the objects attribte `latitude` now is not a float anymore, but a class!

This makes use of [`__setattr__`](https://docs.python.org/3/reference/datamodel.html#object.__setattr__) and [`__getattr__`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__).

So we simplified using the class, but the class itself now looks not so nice
anymore.


## Property decorator

```
class Location(object):

    def __init__(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = latitude

    @property
    def latitude(self):
        """I'm the 'x' property."""
        return self._latitude

    @property
    def longitude(self):
        """I'm the 'x' property."""
        return self._longitude

    @latitude.setter
    def latitude(self, latitude):
        if not (-90 <= latitude <= 90):
            raise ValueError('latitude was {}, but has to be in [-90, 90]'
                             .format(latitude))
        self._latitude = latitude

    @longitude.setter
    def longitude(self, longitude):
        if not (-180 <= longitude <= 180):
            raise ValueError('longitude was {}, but has to be in [-180, 180]'
                             .format(longitude))
        self._longitude = longitude


# Usage
my_position = Location(48.137222222222, 11.575555555556)

my_position.latitude = 48.2
my_position.longitude = 42.6

my_position.latitude = 123  # Fails
```


## See also

* [Is there an advantage of using the property decorator compared to the property class?](https://stackoverflow.com/q/52899509/562769)
