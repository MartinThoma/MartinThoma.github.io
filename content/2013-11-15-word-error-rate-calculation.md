---
layout: post
title: Word Error Rate Calculation
author: Martin Thoma
date: 2013-11-15 08:59:15.000000000 +01:00
category: Cyberculture
tags: algorithms, Levenshtein distance, ASR, WER
featured_image: 2013/11/wer-thumb.png
---
The Word Error Rate (short: WER) is a way to measure performance of an <abbr title="Automatic Speech Recognizer">ASR</abbr>. It compares a reference to an hypothesis and is defined like this:

$$\mathit{WER} = \frac{S+D+I}{N}$$

where
<ul>
  <li>S is the number of substitutions,</li>
  <li>D is the number of deletions,</li>
  <li>I is the number of insertions and</li>
  <li>N is the number of words in the reference</li>
</ul>

## Examples

<pre>REF: What a bright day
HYP: What a day</pre>

In this case, a deletion happened. "Bright" was deleted by the ASR.

<pre>REF: What a day
HYP: What a bright day</pre>

In this case, an insertion happened. "Bright" was inserted by the ASR.

<pre>REF: What a bright day
HYP: What a light day</pre>

In this case, an substitution happened. "Bright" was substituted by "light" by
the ASR.

## Range of values

As only addition and division with non-negative
numbers happen, WER cannot get negativ. It is 0 exactly when the hypothesis is
the same as the reference.

WER can get arbitrary large, because the ASR can insert an arbitrary amount of
words.

<h2>Calculation</h2>
Interestingly, the WER is just the Levenshtein distance for words.

I've understood it after I saw this on the German Wikipedia:

\begin{align}
m &= |r|\\
n &= |h|\\
\end{align}

\begin{align}
D_{0, 0} &= 0\\
D_{i, 0} &= i, 1 \leq i \leq m\\
D_{0, j} &= j, 1 \leq j \leq n
\end{align}

$$
\text{For } 1 \leq i\leq m, 1\leq j \leq n\\
D_{i, j} = \min \begin{cases}
D_{i - 1, j - 1}&+ 0 \ {\rm if}\ u_i = v_j\\
D_{i - 1, j - 1}&+ 1 \ {\rm(Replacement)} \\
D_{i, j - 1}&+ 1 \ {\rm(Insertion)} \\
D_{i - 1, j}&+ 1 \ {\rm(Deletion)}
\end{cases}
$$

But I have written a piece of pseudocode to make it even easier to code this algorithm:

<figure class="aligncenter">
    <img src="../images/2013/11/WER-calculation.png" style="max-width: 500px; max-height: 494px;" class="size-full" alt="WER calculation"/>
    <figcaption>WER calculation</figcaption>
</figure>


<h2>Python</h2>
```python
#!/usr/bin/env python


def wer(r, h):
    """
    Calculation of WER with Levenshtein distance.

    Works only for iterables up to 254 elements (uint8).
    O(nm) time ans space complexity.

    Parameters
    ----------
    r : list
    h : list

    Returns
    -------
    int

    Examples
    --------
    >>> wer("who is there".split(), "is there".split())
    1
    >>> wer("who is there".split(), "".split())
    3
    >>> wer("".split(), "who is there".split())
    3
    """
    # initialisation
    import numpy

    d = numpy.zeros((len(r) + 1) * (len(h) + 1), dtype=numpy.uint8)
    d = d.reshape((len(r) + 1, len(h) + 1))
    for i in range(len(r) + 1):
        for j in range(len(h) + 1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    # computation
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                substitution = d[i - 1][j - 1] + 1
                insertion = d[i][j - 1] + 1
                deletion = d[i - 1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)

    return d[len(r)][len(h)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

<h2>Explanation</h2>
No matter at what stage of the code you are, the following is always true:
<ul>
  <li>If <code>r[i]</code> equals <code>h[j]</code> you don't have to change anything. The error will be the same as it was for <code>r[:i-1]</code> and <code>h[:j-1]</code></li>
  <li>If its a substitution, you have the same number of errors as you had before when comparing the <code>r[:i-1]</code> and <code>h[:j-1]</code></li>
  <li>If it was an insertion, then the hypothesis will be longer than the reference. So you can delete one from the hypothesis and compare the rest. As this is the other way around for deletion, you don't have to worry when you have to delete something.</li>
</ul>
