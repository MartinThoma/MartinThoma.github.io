---
layout: post
title: Data Visualization with Python
slug: python-data-visualization
author: Martin Thoma
date: 2017-08-02 20:00
category: Machine Learning
tags: Data Visualization, Python, Vega, Matplotlib
featured_image: logos/ml.png
---
Python has a lot of libraries for data visualization and I recently stumbled
over an awesome talk from PyCon 2017 by Jake VanderPlas titled "The Python
Visualization Landscape" which gives an overview over them:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/FytuB8nFHPQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

* Matplotlib
    * [seaborn](https://seaborn.pydata.org/): statistical data visualization
    * [Pandas](http://pandas.pydata.org/): Dataframes
    * [networkx](https://networkx.github.io/): Graphs
    * [ggpy](https://github.com/yhat/ggpy): Python implementation of the grammar of graphics
    * [Yellow Brick](https://github.com/DistrictDataLabs/yellowbrick)
    * [scikit-plot](https://github.com/reiinakano/scikit-plot)
* [Datashader](https://github.com/bokeh/datashader): Turns even the largest data into images
* [Vaex](https://github.com/maartenbreddels/vaex): visualize and explore large (~billion rows/objects) tabular datasets interactively
* [Holoviews](http://holoviews.org/)
* Javascript
    * [plotly](https://plot.ly/python/)
    * [bokeh](http://bokeh.pydata.org/en/latest/)
    * [cufflinks](https://github.com/santosjorge/cufflinks)
    * [bqplot](https://github.com/bloomberg/bqplot): Plotting library for IPython/Jupyter Notebooks
    * [pythreejs](https://github.com/jovyan/pythreejs): A Jupyter - ThreeJS bridge
    * [ipyleaflet](https://github.com/ellisonbg/ipyleaflet): IPython Widget for Leaflet Maps
    * [ipyvolume](https://github.com/maartenbreddels/ipyvolume)
* OpenGL
    * [Vispy](http://vispy.org/): interactive scientific visualization
    * [Glumpy](https://glumpy.github.io/): scientific visualization
* Specification languages:
    * [Vega](https://github.com/vega/vega)
    * [Vincent](https://vincent.readthedocs.io/en/latest/): A Python to Vega Translator
    * [Vega Lite](https://vega.github.io/vega-lite/)
    * [Altair](https://altair-viz.github.io/)
    * [d3po](https://github.com/information-field-theory/d3po): Denoising, Deconvolving, and Decomposing Photon Observations