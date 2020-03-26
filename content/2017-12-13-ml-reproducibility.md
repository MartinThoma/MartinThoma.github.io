---
layout: post
title: Reproducibility in Machine Learning
slug: ml-reproducibility
author: Martin Thoma
date: 2017-12-13 20:00
category: Machine Learning
tags: Machine Learning, Research
featured_image: logos/ml.png
---
Getting reproducible results is important because of trust: Why should somebody
else trust you, if you can get the same results repeatedly? Why do you trust
your results in the first place? People make errors. Making sure you can repeat
what you did before eliminates possibilities for human error.

Here are possible reasons why the results of machine learning projects are not
always the same. They are roughly ordered from most likely/easiest to fix to
most unlikely/hardest to fix. I also try to give a solution after the problem:

1. **Human error** - you missread a number / made a typo when you copied a result from one shell to the paper: Logging. Create an `2017-12-31-23-54-experiment-result.log` for every single experiment you run. Not manually,
 but the experiment creates it. Yes, the time stamp in the name for easier finding it again. All following should be logged to that file for each single experiment.
2. **Code** changed: Version control (e.g. git)
3. **Configuration file** changed: Version control
4. **Pseudorandom number** changed: set seed for random / tensorflow / numpy (yes, you might have to set more than one seed)
5. **Data loading** differently / in a different order: Version control + seed (is the preprocessing really the same?)
6. **Environment variables** changed: Docker
7. **Software (version)** changed: Docker
8. **Driver (version)** changed: Logging
9. **Hardware** changed: Logging
10. **Concurrency**: The fact that [floating point multiplication is not associative](https://en.wikipedia.org/wiki/Associative_property#Nonassociativity_of_floating_point_calculation) and different cores on a GPU might finish computations at different times
11. **Hardware has errors**

In any case, running the "same" thing multiple times might help to get a gut
feeling for how different things are.


## Writing a paper

If you write a paper, I think the following would be the best practice for reproducibility:

1. Add a link to a **repository** (e.g. git) where all code is
2. The code has to be **containerized** (e.g. Docker)
3. If there is Python code and a `requirements.txt` you have to give the **exact software version**, not something like `tensorflow>=1.0.0` but `tensorflow==1.2.3`
4. Add the **git hash** of the version you used for the experiments. It might be different hashes if you changed something in between.
5. Always log information about **drivers** (e.g. [like this for nVidia](https://stackoverflow.com/a/47781255/562769)) and **hardware**. Add this to the appendix of your paper. So in case of later changes one can at least check if there was a change which might cause numbers being different.

For logging the versions, you might want to use something like this:

```python
#!/usr/bin/env python

# core modules
import subprocess


def get_logstring():
    """
    Get important environment information that might influence experiments.

    Returns
    -------
    logstring : str
    """
    logstring = []
    with open("/proc/cpuinfo") as f:
        cpuinfo = f.readlines()
    for line in cpuinfo:
        if "model name" in line:
            logstring.append("CPU: {}".format(line.strip()))
            break

    with open("/proc/driver/nvidia/version") as f:
        version = f.read().strip()
    logstring.append("GPU driver: {}".format(version))
    logstring.append("VGA: {}".format(find_vga()))
    return "\n".join(logstring)


def find_vga():
    vga = subprocess.check_output(
        "lspci | grep -i 'vga\|3d\|2d'", shell=True, executable="/bin/bash"
    )
    return vga


print(get_logstring())
```

which gives something like

```text
CPU: model name    : Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz
GPU driver: NVRM version: NVIDIA UNIX x86_64 Kernel Module  384.90  Tue Sep 19 19:17:35 PDT 2017
GCC version:  gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.5)
VGA: 00:02.0 VGA compatible controller: Intel Corporation Skylake Integrated Graphics (rev 06)
02:00.0 3D controller: NVIDIA Corporation GM108M [GeForce 940MX] (rev a2)
```
