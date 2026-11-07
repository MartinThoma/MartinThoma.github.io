---
layout: post
title: Unlocking the Power of Python’s Ecosystem via Plugins
slug: unlocking-the-power-of-pythons-ecosystem-via-plugins
lang: en
author: Martin Thoma
date: 2024-02-25 21:02
category: Code
tags: Python, Software Architecture
featured_image: logos/python.png
summary: How to build a plugin system in Python with entry points
medium_url: https://medium.com/@martinthoma/unlocking-the-power-of-pythons-ecosystem-via-plugins-18b58783b089
status: draft
---
<figure class="ai-generated">
    <a href="../images/2024/02/unlocking-the-power-of-pythons-ecosystem-via-plugins-1.jpg"><img src="../images/2024/02/unlocking-the-power-of-pythons-ecosystem-via-plugins-1.jpg" alt="Comic drawing of an office team cheering in front of their laptops, with light bulbs above their heads" width="800" height="800"></a>
</figure>

pytest and flake8 have tons of third-party packages. I’d argue that is one reason why they are so popular.

The idea is simple: pytest provides the core functions for running tests, but it also provides hooks that third-party developers can use. There are tons of pytest extensions, e.g. here are my highlights for output formatting:

[**Shiny pytest plugins** *Improve the output for better readability*](../shiny-pytest-plugins/)

The interesting part is that you typically only install the third-party package. No additional configuration of pytest is necessary. That made me wonder: **How does pytest discover its plugins?**

## The importlib.metadata package

`importlib.metadata` is one of the default Python packages. It provides access to the metadata of an installed package, such as its entry points. [Setuptools](https://setuptools.pypa.io/en/latest/pkg_resources.html#entry-points) explains the concept of entry points pretty well:

> **Entry points** are a simple way for [packages] to “advertise” Python objects (such as functions or classes) for use by other [packages]. [Applications] can search for entry points with a particular name or group […]and then inspect or load the advertised objects at will.

## Defining the plugin API with importlib.metadata

<figure class="ai-generated">
    <a href="../images/2024/02/unlocking-the-power-of-pythons-ecosystem-via-plugins-2.jpg"><img src="../images/2024/02/unlocking-the-power-of-pythons-ecosystem-via-plugins-2.jpg" alt="Illustration of a metallic socket with two slots in a swirl of silver lines" width="800" height="800" loading="lazy"></a>
</figure>

This is how you can get all entry points for pytest:

```python
from importlib.metadata import entry_points

for entry_point in entry_points().select(group="pytest11"):
    loaded_python_object = entry_point.load()
    print(entry_point)
```

Pytest defined the group name `pytest11`. I have no idea why they chose pytest11 instead of pytest. [I’ve asked](https://stackoverflow.com/q/77931545/562769).

If you run `pip install pytest-sugar` and run the code above, you will see:

```text
EntryPoint(name='sugar', value='pytest_sugar', group='pytest11')
```

The `loaded_python_object` can be used to execute the plugin code.

Let’s see which [flake8 plugins are registered](https://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html#registering-a-plugin-with-flake8) on my current system:

```pycon
>>> import importlib.metadata
>>> for el in importlib.metadata.entry_points().select(group="flake8.extension"):
...     print(el)
EntryPoint(name='B', value='bugbear:BugBearChecker', group='flake8.extension')
EntryPoint(name='T20', value='flake8_print:PrintChecker', group='flake8.extension')
EntryPoint(name='R70', value='radon.contrib.flake8:Flake8Checker', group='flake8.extension')
EntryPoint(name='ISC', value='flake8_implicit_str_concat:Checker', group='flake8.extension')
EntryPoint(name='C90', value='mccabe:McCabeChecker', group='flake8.extension')
EntryPoint(name='E', value='flake8.plugins.pycodestyle:pycodestyle_logical', group='flake8.extension')
EntryPoint(name='F', value='flake8.plugins.pyflakes:FlakesChecker', group='flake8.extension')
EntryPoint(name='W', value='flake8.plugins.pycodestyle:pycodestyle_physical', group='flake8.extension')
EntryPoint(name='DAR', value='darglint.flake8_entry:DarglintChecker', group='flake8.extension')
```

## Writing plugins by using entry-points

<figure class="ai-generated">
    <a href="../images/2024/02/unlocking-the-power-of-pythons-ecosystem-via-plugins-3.jpg"><img src="../images/2024/02/unlocking-the-power-of-pythons-ecosystem-via-plugins-3.jpg" alt="Illustration of a glowing USB plug in a field of colorful flowers and butterflies" width="800" height="800" loading="lazy"></a>
</figure>

People who want to write plugins need to provide the entry points. This can be done with `pyproject.toml`. In the case of my file-manager project flitz you would provide a context menu item called `flitz_compress` like this:

```toml
[project.entry-points."flitz"]
flitz_compress = "flitz_compress:context_menu_item"
```

Now you need to follow the [Python Package Creation User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

Looking at [the full minimal example](https://github.com/MartinThoma/flitz-compress) might be helpful.

## Summary

You can create a plugin system in Python using `importlib.metadata` to read entry-points defined in `pyproject.toml`.

**It’s crucial to document how to write plugins for your software!** You can take [pytest documentation on writing plugins](https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html) or the [flake8 documentation](https://flake8.pycqa.org/en/latest/plugin-development/) as an example.
