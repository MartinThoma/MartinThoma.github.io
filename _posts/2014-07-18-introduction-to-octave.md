---
layout: post
title: Introduction to Octave
author: Martin Thoma
date: 2014-07-18 17:40
categories:
- Code
tags:
- Octave
- ML
featured_image: logos/octave.png
---

[GNU Octave](https://en.wikipedia.org/wiki/GNU_Octave) is a really neat
prototyping language for machine learning tasks. It is dynamically typed.

## Installation

Octave is in the package repositories, so it can be installed by

```bash
$ sudo apt-get install octave gnuplot-x11 octave-epstk
```

and started with

```bash
$ octave
```

## Configuration

Create a file `~/.octaverc` in your home folder. Write 

```text
PS1('>>');
setenv("GNUTERM","x11");
```
in it to get a nicer prompt and make sure that plots will work.

## The Language

### Vectors and Matrices

Octave has a lot of neat matrix manipulation features. You can create a matrix
$A = \begin{pmatrix} 1 & 2\\ 3 & 4\end{pmatrix}$ with

```octave
>> A = [1 2; 3 4];
```

When you want to transpose a vector / a matrix, you simply add an apostrophe:

```octave
>> A = [1 2; 3 4];
>> A'
ans =

   1   3
   2   4
```

You can multiply two matrices with `A*B` or use the dot product with `A .* B`.

The identity matrix $I \in \mathbb{R}^{n \times n}$ can be created with

```octave
>> I = eye(n);
```

You can get a part of the matrix by slicing:

```octave
>> I = eye(n);
>> I(:, 1:2);
```

But be careful: Vectors and matrices are 1-indexed, not 0-indexed as you might
expect!

You can get the size of a matrix with the function `size` which returns a matrix:

```octave
>> a = [1 2 3; 4 5 6];
>> size(a)
ans =

   2   3

```

If you simple want the "length" you can directly access the first element:

```octave
>> size(a)(1)
ans =  2
```

### Sequences
The sequence `0 1 2 3 4 5` can be created with `[0:5]`.

The sequence `0.2 0.3 0.4 0.5` can be created with `[0.2:0.1:0.5]`.
In general: `[<start>:<step>:<end>]` where `<start>` and `<end>` are included.

You can also very simple apply functions to each element:

```octave
>> t = [0.2:0.1:0.5];
>> sin(t)
ans =

   0.19867   0.29552   0.38942   0.47943
```

The output can be suppressed with `;`.

### Plotting

I have never seen a language where plotting is so easy:

```octave
>> x = [0:0.01:pi];
>> y = sin(x);
>> plot(x, y);
```

You can add labels and a legend to it, too:

```octave
>> xlabel = "x";
>> ylabel = "value";
>> legend('sin', 'cos')
>> title("sin and cos")
```

And finally, you can store the image:

```octave
print -dpng 'my_plot.png'
```

### Control statements

#### for

```octave
for i=1:10;
    printf("%i: %i\n", i, i^2)
end
```

#### while

```octave
i=1;
while i <= 10,
    printf("%i: %i\n", i, i^2)
end;
```

#### if

```octave
if 2 == 1+1,
    printf("True\n");
elseif 3 == 2+1,
    printf("Else true");
else
    printf("else");
end;
```

### Functions

Functions have to be saved in a file called `[filename].m`. One other special
thing about functions is that you define the variable with the output at the
beginning:

```octave
function y = fibonacci(n)
    if n < 2,
        y = 1;
    else
        y = fibonacci(n-1) + fibonacci(n-2);
    end;
```

You can also group values you want to give back like this:

```octave
function [succ, pred] = succ_and_pred(n)
    succ = n+1;
    pred = n-1;
```

## Resources

* [GNU Octave](https://en.wikipedia.org/wiki/GNU_Octave)
* [stackoverflow.com](http://stackoverflow.com/questions/tagged/octave?sort=votes)
* [Documentation](https://www.gnu.org/software/octave/doc/interpreter/)