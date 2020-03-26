---
layout: post
title: Defaults of Configuration Files
slug: cfg-files-defaults
author: Martin Thoma
date: 2017-05-14 20:00
category: Code
tags: Programming, Configuration, Python
featured_image: logos/star.png
---
I often need configuration files in the software I develop. In principle, I can
think of two ways to deal with configuration files:

* **Complete**: The configuration file has to have all values which will later
  be accessed by the application
* **Partial**: The configuration file might only define some values. In case
  the application needs a value which is not in the user defined configuration
  file, a default value is used.

The complete approach has the major drawback of making updates difficult. The
user(s) might have different configuration files for different usage scenarios.
In the worst case the user has to update his files manually, just because the
developer added a couple of possibilities to customize the application.

Hence I prefer the partial approach where a default configuration file is part
of the application. This default config file will not be overwritten. It
contains all values necessary for the user. But the user may define a user
config file which he may adjust. The user can peek at the default file to see
what he can customize, but he can keep his config file clean.

Here is a small example how you can do this with Python:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example how to load config file with defaults."""

import json


def load_config(cfg_filename):
    """Load a configuration file."""
    with open(cfg_filename) as data_file:
        data_loaded = json.load(data_file)
    return data_loaded


def merge_dicts(cfg_defaults, cfg_user):
    """
    Merge two dictionaries.

    Parameters
    ----------
    cfg_defaults : dict
        Iterate through this dict
    cfg_user : dict
        Update this dict so that it has all keys which the other file has.
    """
    for k, v in cfg_defaults.iteritems():
        if k not in cfg_user:
            cfg_user[k] = v
        elif isinstance(v, dict):
            merge_dicts(v, cfg_user[k])


def load_config_defaults(cfg_filename, cfg_default_filename):
    """Load a configuration file with defaults."""
    cfg_defaults = load_config(cfg_default_filename)
    cfg_user = load_config(cfg_filename)

    # Idea: Take the user config. If anything is missing, add it from the
    # defaults.
    # So iterate through the default dict and check if it is in the user dict,
    # too. Add it if not.
    cfg = cfg_user
    merge_dicts(cfg_defaults, cfg)
    return cfg


print(load_config_defaults("user_cfg.json", "default_cfg.json"))
```


## See also

* [Configuration files in Python](https://martin-thoma.com/configuration-files-in-python/)
