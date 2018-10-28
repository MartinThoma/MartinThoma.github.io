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
Python has a built-in decorator `@property`. In this article, you will learn
why and how to use it.

The following super basic `Location` class is used:

```
def Location(object):

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
```


## Getters and Setters

Let's say, you want to add a range check for the properties of the class. You
could make something like:

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

This is what Java developers would do. Note that there is only the convention
that tells you that the `latitude` property has a `set_latitude` setter and
a `get_latitude` getter.


## Property class

With Python 2.2, the `property` class was added to simplify it ([source](https://www.python.org/download/releases/2.2.2/descrintro/#property)).

With that, you can change the class to

```
class Location(object):
    """Representation of a point on Earth."""

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

Here is how the `help` of this class looks like:

```
Help on class Location in module __main__:

class Location(builtins.object)
 |  Representation of a point on Earth.
 |
 |  Methods defined here:
 |
 |  __init__(self, longitude, latitude)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  get_latitude(self)
 |
 |  get_longitude(self)
 |
 |  set_latitude(self, latitude)
 |
 |  set_longitude(self, longitude)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  latitude
 |
 |  longitude
```

<div class="info">You should note the single leading underscore - that is Pythons way to denote private properties. It is not meant as the public interface of the class.<br/>
<br/>
There is also a leading double underscore. The interpreter changes the name of the attribute to prevent naming colisions. Just have a look at `dir(some_example_class)`. See also: [What's the meaning of underscores (_ & __) in Python variable names?](https://www.youtube.com/watch?v=ALZmCy2u0jQ)</div>

And then note how the objects attribte `latitude` now is not a float anymore, but a class!

This makes use of [`__setattr__`](https://docs.python.org/3/reference/datamodel.html#object.__setattr__) and [`__getattr__`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__). So by using this, there is a strong relationship
between the getter/setter and the attribute!

So we simplified using the class, but the class itself now looks not so nice
anymore. Also, the `help` is polluted by the getters and setters.


## Property decorator

The property decorator is what should be used in Python ([source](https://stackoverflow.com/a/52947521/562769)).
It makes the behaviour less error-prone when you inherit from such a class.

Here is how it is used:

```
class Location(object):
    """Representation of a point on Earth."""

    def __init__(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = latitude

    @property
    def latitude(self):
        """Latitude of the location. North is positive, south is negative."""
        return self._latitude

    @property
    def longitude(self):
        """Longitude of the location. East is positive, west is negative."""
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

Here is how the `help` of this class looks like:

```
Help on class Location in module __main__:

class Location(builtins.object)
 |  Representation of a point on Earth.
 |
 |  Methods defined here:
 |
 |  __init__(self, longitude, latitude)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  latitude
 |      Latitude of the location. North is positive, south is negative.
 |
 |  longitude
 |      Longitude of the location. East is positive, west is negative.
```


## See also

* [Is there an advantage of using the property decorator compared to the property class?](https://stackoverflow.com/q/52899509/562769)
