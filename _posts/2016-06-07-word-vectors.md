---
layout: post
title: Word Vectors
slug: word-vectors
author: Martin Thoma
status: draft
date: 2016-06-07 20:00
category: Code
tags: Machine Learning, Python
featured_image: logos/ml.png
---

The idea behind word vectors is to represent natural language words like "king"
in $\mathbb{R}^n$ in such a way, that you can do arithmetic. For example,

$$\text{vec}(\text{king}) - \text{vec}(\text{man}) + \text{vec}(\text{woman}) \approx \text{vec}(\text{queen})$$

The Python library [`gensim`](http://radimrehurek.com/gensim/) implements this.


## Requirements

```bash
pip install gensim --user
pip install nltk --user
```


## Example

An easy to use example is

```python
from gensim.models import Word2Vec
from nltk.corpus import brown
model = Word2Vec(brown.sents())
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=3)
```

which returns

```
[(u'scored', 0.9442702531814575), (u'calling', 0.9424217939376831), (u'native', 0.9412217736244202)]
```

So the corpus is not that good, but it should work with a bigger one.


## See also

* [The amazing power of word vectors](https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/)
* [Deep learning with word2vec and gensim](http://rare-technologies.com/deep-learning-with-word2vec-and-gensim/)