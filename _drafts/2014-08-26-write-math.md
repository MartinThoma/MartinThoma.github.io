---
layout: post
title: On-line Handwriting Recognition of Mathematical Symbols
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Python
- Project Management
featured_image: logos/write-math.png
---

On-line handwriting recognition systems get the information how a symbol is
written. In contrast, OCR only gets the pixel map.

I've created a system that can be used to work with handwriting recognition
systems in my bachelor's thesis.

## System Structure

The system has a configurable `PROJECT_ROOT`. The configuration file is
`~/.writemathrc`.


### Raw datasets
All raw datasets (pickle-files) are in `[PROJECT_ROOT]/archive/raw-datasets/`.

Every raw dataset must contain the following information:

* 'handwritings': A list of all handwritings. Those are objects that contain
  themselfes a lot of information.

### Preprocessed datasets
All preprocessed dataset are in `[PROJECT_ROOT]/archive/preprocessed/`.
Every preprocessed dataset should have its own folder. Every folder must contain
a preprocessing.yml.

Every preprocessed dataset pickle file must contain the following information:

* Source dataset
* Date / time when preprocessing was started (eventually git commit?)

### Models
All models are stored in their own folder. I assume that these model folders
are in `[PROJECT_ROOT]/archive/models/`. Every analysis that is made will place
the result in that folder (or a subfolder).

pfiles are also in this folder. When pfiles get created, there has to be a
tranlation file that maps from indices (as used for pfiles) to formula_ids.

There also has to be a `model.yml` in each model folder. It is a configuration
file that contains the following information:

* preprocessing: Which preprocessed pfile was used?

In that folder will also be:

* traindata.pfile
* validdata.pfile
* testdata.pfile