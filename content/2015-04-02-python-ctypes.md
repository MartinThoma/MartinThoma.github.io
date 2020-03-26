---
layout: post
title: Python ctypes
author: Martin Thoma
date: 2015-04-02 22:06
category: Code
tags: Python, Rust
featured_image: logos/python.png
---

One pseudo-problem people often mention when talking about Python is that
Python is (too) slow. What they seem to forget or don't know is that you can
call C code from Python with [`ctypes`](https://docs.python.org/3/library/ctypes.html).
So you can get almost as fast as you can get with C; you're not limited by
the language in that respect. And most of the time your code has other issues
when it is too slow.

Now, you can also wrap Rust code with ctypes for Python ☺

## Motivation

As a very simple example, I prepared a dumb Fibonacci implementation written in
Python:

```python
def fib(n):
    """Calculate the n-th Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = 37
    print("The %ith Fibonacci number is %i." % (n, fib(n)))
```

and exactly the same for Rust

```rust
pub extern fn fib(n: u32) -> u32 {
    if n <= 1 {
        return n;
    } else {
        return fib(n-1) + fib(n-2);
    }
}

fn main() {
    let n = 37;
    println!("The {0}th Fibonacci number is {1}.", n, fib(n))
}
```

The execution times are quite different. Rust needs 0.40 seconds while Python 3
needs 15.7 seconds. That is almost 40× the time of Rust!

Wouldn't it be great if we could call the Rust function from Python?


## Example

I'll explain in the next chapters what is done, but at first you should see
that there are only minor changes / overhead:

**fibonacci.rt**:

```rust
#![crate_type = "dylib"]

#[no_mangle]
pub extern fn fib(n: u32) -> u32 {
    if n <= 1 {
        return n;
    } else {
        return fib(n-1) + fib(n-2);
    }
}
```

Call `rustc -O fibonacci.rt` to generate the library.


Python:

```rust
#!/usr/bin/env python

import ctypes

fiblib = ctypes.CDLL("./libfibonacci.so")
fib = fiblib.fib
n = 37
print("The %ith Fibonacci number is %i." % (n, fib(n)))

```

Now, taking the Python code, it takes only 0.44 seconds!

## What happens

The line `#![crate_type = "dylib"]` tells `rustc` that it has to create a
dynamic library.

The line `#[no_mangle]` tells the compiler not to mangle the name `fib`.
This is important so that we can later use it from Python. (I think names are
mangled to prevent name clashes ... so it's a kind of name-spacing.)

Then we load the C DLL with `ctypes.CDLL("./libfibonacci.so")` and use it
as expected. Pretty easy, isn't it?


## Caveats

Python makes some things very simple which are not that simple at all. Think
about numbers, for example. In Rust, you have integers with 64 bits. But in
Python you have arbitrary length integers. This might lead to problems.

## See also

* [Calling Rust from C (and Python!)](http://harkablog.com/calling-rust-from-c-and-python.html)
* [doc.rust-lang.org/book/ffi](http://doc.rust-lang.org/book/): Foreign Function Interface
* [doc.rust-lang.org](http://doc.rust-lang.org/reference.html#ffi-attributes): FFI attributes
* [rustbyexample.com](http://rustbyexample.com/attribute/crate.html): Crates
