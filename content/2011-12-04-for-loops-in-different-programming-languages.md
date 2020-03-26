---
layout: post
title: for loops in different programming languages
author: Martin Thoma
date: 2011-12-04 11:19:54.000000000 +01:00
category: Code
tags: Programming, learning
featured_image: 2011/11/for-loop.png
---
If you have to learn a new programming language it is most of the time quite easy. You know the structures and the way you have to think if you want to solve a problem. The first time it might be hard, but the more languages you learn the more similarities you'll recognize.

I also have to learn a special variant of <a href="http://en.wikipedia.org/wiki/Pseudocode">pseudocode</a> at the moment. It is quite hard to know what pseudocode does if it isn't unambiguously defined. I had problems with for loops for example.

For loops have some properties you simply have to define:
<ul>
  <li><strong>Scoping</strong>: Does the loop counter still exist after the loop was executed?</li>
  <li><strong>Copy or reference</strong>: Does the loop statement work with a copy or with a reference of the variables in the loop body?</li>
  <li><strong>Last value of i</strong>: What is the last value of i?</li>
</ul>

<h2>General structure</h2>
A for loop usually consists of an initialization part, a condition and an iteration step:

<figure class="aligncenter">
            <a href="../images/2011/11/for-loop-structure1.png"><img src="../images/2011/11/for-loop-structure1.png" alt="for loop structure" style="max-width:285px;max-height:176px" class="size-full wp-image-9251"/></a>
            <figcaption class="text-center">The structure of a for loop.</figcaption>
        </figure>

<h2>Pythons special structure</h2>
Python uses a generator or lists to loop:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(0, 10):
	print("In loop: %i" % i)

print("Out of loop: %i" % i)
```

<h2>Scoping</h2>
Does the loop counter still exist after the loop was executed?
<ul>
    <li><strong>Yes</strong>: JavaScript, PHP, Python</li>
    <li><strong>No</strong>: C, C++, Java</li>
</ul>

<h2>Copy or reference</h2>
Does the loop statement work with a copy or with a reference of the variables in the loop body? Does the programming language use the same variable as in the for condition (reference) or does it use another one (copy)? You can test this if you add something to i in the body.
<ul>
    <li><strong>Copy</strong>: Python</li>
    <li><strong>Reference</strong>: C, C++, Java, JavaScript, PHP</li>
</ul>

Python iterates over a generator. This means that you can't really compare Pythons for-loop to other programming languages' for loops.

<h2>Last value of i</h2>
What is the last value of i?

<strong>9</strong>: C, C++, Java (Inside the loop), Python (Outside of the loop)
<strong>10</strong>: JavaScript, PHP (Outside of the loop)

<h2>foreach</h2>
Many languages provide a special for loop. This special for loop is sometimes called "foreach" as you iterate over each element in a collection (e.g. an array).

<h3>Java</h3>
```java
int[] array = new int[5];
array[0] = 0;
array[1] = 1;
array[2] = 2;
array[3] = 3;
array[4] = 4;

for (int item: array) {
    System.out.println("Foreach: " + item);
}
```

<h3>JavaScript</h3>
```javascript
var array = new Array(0, 1, 2, 3, 4);

for (var value in array) {
    document.write('Foreach: ' + value + '<br/>' );
}
```

<h3>PHP</h3>
```php
$array = array(0, 1, 2, 3, 4);

foreach ($array as $key=>$value) {
    echo "Foreach: $value<br/>";
}
```

<h3>Python</h3>
```python
array = [0, 1, 2, 3, 4]

for value in array:
    print "Foreach: %i" % value
```

<h2>More information</h2>
If you want to see the code, you can download this <a href='../images/2011/12/for-loops.zip'>zip archive</a>.

It is quite astonishing, but Wikipedia has a very long <a href="http://en.wikipedia.org/wiki/For_loop">article about for loops</a>.
