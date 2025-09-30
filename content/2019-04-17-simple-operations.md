---
layout: post
lang: en
title: Simple Operations and Basic Numbers
slug: simple-operations
author: Martin Thoma
date: 2019-04-17 20:00
category: Code
tags: Python, Network, speed, Internet, Traffic
featured_image: logos/python.png
---
I just wondered how fast some simple operations are (in Python). Like the lookup of an
element in a dictionary. Here you have some, tested on my ThinkPad T460p ([i7-6700HQ](https://ark.intel.com/content/www/de/de/ark/products/88967/intel-core-i7-6700hq-processor-6m-cache-up-to-3-50-ghz.html)).


## Arithmethic

I added/subtracted/multiplied/divided a thousand pairs of numbers to test the
speed of basic arithmetic operations. I expected them to be FAST; essentially

Let's have a look at the adding function:

```python
def add(numbers):
    return [a + b for a, b in numbers]
```

The disassembled cPython Byte-Code looks like this:

```python-prompt
>>> import dis
>>> dis.dis(add)
  2           0 LOAD_CONST               1 (<code object <listcomp> at 0x7feabba81300, file "<stdin>", line 2>)
              2 LOAD_CONST               2 ('add.<locals>.<listcomp>')
              4 MAKE_FUNCTION            0
              6 LOAD_FAST                0 (numbers)
              8 GET_ITER
             10 CALL_FUNCTION            1
             12 RETURN_VALUE
```

So you can see that it does more than `BINARY_ADD`. Still, the basic arithmetic
operations are FAST. I think the tuple unpacking might actually have dominated
the time here.

Here are the results:

```text
add                 : min: 177.3μs, mean: 200.3μs, max:  522.2μs
subtract            : min: 168.4μs, mean: 190.9μs, max:  538.8μs
multiply            : min: 165.4μs, mean: 199.7μs, max:  515.8μs
divide              : min: 176.3μs, mean: 213.7μs, max:  518.9μs

2**int (0..20)      : min: 546.4μs, mean: 597.5μs, max:  945.3μs
3**int (0..20)      : min: 591.4μs, mean: 648.8μs, max: 1091.0μs <- BigInt
3.131**int (0..20)  : min: 295.0μs, mean: 304.2μs, max:  602.3μs
2**float            : min: 343.1μs, mean: 371.9μs, max:  769.7μs
3**float            : min: 347.3μs, mean: 375.0μs, max:  748.9μs
3.131**float        : min: 275.3μs, mean: 299.3μs, max:  586.4μs

add_vectors         : min:   3.5μs, mean:   4.0μs, max:   34.8μs
subtract_vectors    : min:   3.4μs, mean:   4.1μs, max:   28.5μs
multiply_vectors    : min:   4.0μs, mean:   4.3μs, max:   30.7μs
divide_vectors      : min:  17.2μs, mean:  18.2μs, max:   71.9μs
```

You can see how bad this measure is with something like

```python
durations = np.array(timeit.repeat("4+500000", repeat=5000, number=1))
```

which gives

```text
add                 : min: 0.08μs, mean: 0.15μs, max:   1.38μs
subtract            : min: 0.08μs, mean: 0.15μs, max:   1.51μs
multiply            : min: 0.06μs, mean: 0.14μs, max:   1.77μs
divide              : min: 0.06μs, mean: 0.13μs, max:   1.36μs
modulo              : min: 0.08μs, mean: 0.15μs, max:   1.59μs
```

I'm not sure if this test "suffers" from caching, especially as the max is way
higher than the min and mean, but I guess it is save to say that all four
basic arithmetic operations are about the same execution time and are less than
2μs. That would be about 5200 CPU cycles of my machine.


## Element lookup

Timing how quickly one can retrieve the element from a [direct access](https://en.wikipedia.org/wiki/Random_access)
data structure by index. Not very surprisingly, lists are fastest. A bit surprising
is that numpy arrays are quite a bit worse.

```text
lookup(list)        : min: 134.0μs, mean: 157.0μs, max:  482.0μs
lookup(dict)        : min: 355.8μs, mean: 407.3μs, max: 1895.2μs
lookup(np array)    : min: 711.1μs, mean: 855.7μs, max: 1665.5μs
```

## Algorithms

### Sorting

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/04/sorting-speed.png"><img src="../images/2019/04/sorting-speed.png" alt="Sorting speed in Python" style="width: 512px;"/></a>
    <figcaption class="text-center">Sorting speed in Python</figcaption>
</figure>

<table class="table">
    <tr>
        <th>Samples</th>
        <th>min</th>
        <th>median</th>
        <th>max</th>
    </tr>
    <tr>
        <td>10</td>
        <td>1.6μs</td>
        <td>2.1μs</td>
        <td>191.7μs</td>
    </tr>
    <tr>
        <td>100</td>
        <td>16.6μs</td>
        <td>24.9μs</td>
        <td>121.7μs</td>
    </tr>
    <tr>
        <td>500</td>
        <td>110.6μs</td>
        <td>115.2μs</td>
        <td>467.9μs</td>
    </tr>
    <tr>
        <td>1000</td>
        <td>246.1μs</td>
        <td>258.6μs</td>
        <td>1133.4μs</td>
    </tr>
    <tr>
        <td>2000</td>
        <td>543.1μs</td>
        <td>562.6μs</td>
        <td>934.5μs</td>
    </tr>
    <tr>
        <td>3000</td>
        <td>859.8μs</td>
        <td>913.8μs</td>
        <td>2933.8μs</td>
    </tr>
    <tr>
        <td>4000</td>
        <td>1188.0μs</td>
        <td>1258.0μs</td>
        <td>2859.0μs</td>
    </tr>
    <tr>
        <td>5000</td>
        <td>1519.6μs</td>
        <td>1631.4μs</td>
        <td>2828.4μs</td>
    </tr>
</table>

```python
import timeit
import numpy as np

durations = np.array(
    timeit.repeat(
        "sorted(arr)",
        setup="import numpy as np;arr = np.random.random(100_000)",
        repeat=5000,
        number=1,
    )
)
print(
    "min: {min:5.1f}μs, mean: {mean:5.1f}μs, max: {max:6.1f}μs".format(
        min=min(durations) * 10 ** 6,
        mean=np.mean(durations) * 10 ** 6,
        max=max(durations) * 10 ** 6,
    )
)
```

## Networks

When you talk about "speed" in a network context, there are two important values:

<dl>
    <dt><a href="https://en.wikipedia.org/wiki/Network_delay">Latency</a></dt>
    <dd>Latency is measured in milli-seconds (ms) and answers the question: How long does it take for the first bit to be transmitted?</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Throughput">Throughput</a> (Bandwidth)</dt>
    <dd>Throughput is measured in kB/s and answers the question: If the first bit already arrived, how quickly will the rest be transfered?</dd>
</dl>



### Latency

Typical values:

* Accessing a CPU register: Less than 1ns!
* Accessing L1 / L2 CPU caches: 1ns - 10ns
* Accessing L3 CPU cache: 10ns - 100ns
* Ethernet Switch Latency: 50μs - 125μs
* Cable: Essentially non-existant as the signal travels with the speed of light

And some other corner stones:

* Ping (via WLAN) in average
    * My router: 2.3ms
    * joyn.de: 19.4ms
    * twitter.com: 25.7ms
    * google.de: 26.3ms
    * wikipedia.org: 29.1ms
    * martin-thoma.de: 29.4ms
    * martin-thoma.com: 30.3ms
    * netflix.com: 50.8ms
    * write-math.com: 248.0ms
* Static pages with network:
    * [http://martin-thoma.de via hosting.de](http://martin-thoma.de): 52ms - 61ms
    * [https://google.de](https://google.de): 110ms - 170ms
    * [https://joyn.de](https://joyn.de/): 130ms - 190ms
    * [https://blog.fefe.de](https://blog.fefe.de/): 150ms - 180ms
    * [https://martin-thoma.com](https://martin-thoma.com/) via GitHub: 320ms - 420ms
    * [https://netflix.com](https://netflix.com/): 230ms - 500ms
* API request with network:
    * [https://write-math.com](https://write-math.com) via namecheap; a symbol classification request: 550ms - 820ms

### Throughput

And some throughput values (partially measured, partially looked up / calculated):

<table class="table">
    <tr>
        <th rowspan="2">Connection</th>
        <th colspan="2">Throughput</th>
    </tr>
    <tr>
        <th>Download</th>
        <th>Upload</th>
    </tr>
    <tr>
        <td>Gigabit Ethernet</td>
        <td>1000 MBit/s</td>
        <td>1000 MBit/s</td>
    </tr>
    <tr>
        <td>My Internet Connection</td>
        <td>&nbsp;285 MBit/s</td>
        <td>&nbsp;25 MBit/s</td>
    </tr>
    <tr>
        <td>My Internet Connection (<a href="https://www.speedtest.net/result/9272895784">2020-04-12</a>)</td>
        <td>&nbsp;96 MBit/s</td>
        <td>&nbsp;7 MBit/s</td>
    </tr>
    <tr>
        <td>LTE (peak)</td>
        <td>&nbsp;37 MB/s</td>
        <td>&nbsp;&nbsp;9 MB/s</td>
    </tr>
    <tr>
        <td>LTE (measured)</td>
        <td>&nbsp;14 MB/s</td>
        <td>&nbsp;&nbsp;2 MB/s</td>
    </tr>
    <tr>
        <td>Audio Streaming (Low,&nbsp;96kbps)</td>
        <td colspan="2">&nbsp;&nbsp;0.012 MB/s</td>
    </tr>
    <tr>
        <td>Audio Streaming (Normal,&nbsp;160kbps)</td>
        <td colspan="2">&nbsp;&nbsp;0.020 MB/s</td>
    </tr>
    <tr>
        <td>Audio Streaming (High,&nbsp;320kbps)</td>
        <td colspan="2">&nbsp;&nbsp;0.040 MB/s</td>
    </tr>
    <tr>
        <td>Video Streaming (Low, 360)</td>
        <td colspan="2">0.083 MB/s</td>
    </tr>
    <tr>
        <td>Video Streaming (Normal, 720p)</td>
        <td colspan="2">0.250 MB/s (2.0 MBit/s)</td>
    </tr>
    <tr>
        <td>Video Streaming (High, 1080p)</td>
        <td colspan="2">0.417 MB/s (3.3 MBit/s)</td>
    </tr>
</table>


When you think about which internet contract to get, you might be wondering
which speed is acceptable. The highest speed is probably necessary for video
streaming:

<table class="table">
    <thead>
        <tr>
            <th>Speed</th>
            <th>Comment</th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td>0.5 Mbit/s</td>
        <td>Minimum required for Netfix<sup><a href="#fn-1" name="fnref-1">[1]</a></sup></td>
    </tr>
    <tr>
        <td>1.5 Mbit/s</td>
        <td>Recommended speed for Netflix<sup><a href="#fn-1" name="fnref-1">[1]</a></sup></td>
    </tr>
    <tr>
        <td>3.0 Mbit/s</td>
        <td>Recommended speed for Netflix with standard resolution<sup><a href="#fn-1" name="fnref-1">[1]</a></sup></td>
    </tr>
    <tr>
        <td>5.0 Mbit/s</td>
        <td>Recommended speed for Netflix with HD resolution<sup><a href="#fn-1" name="fnref-1">[1]</a></sup></td>
    </tr>
    <tr>
        <td>25.0 Mbit/s</td>
        <td>Recommended speed for Netflix with Ultra-HD resolution<sup><a href="#fn-1" name="fnref-1">[1]</a></sup></td>
    </tr>
    </tbody>
</table>


### Combinations

Some measurements how quickly I get web pages:

```text
get_webpage (martin-thoma.de,     2.3kB): min:  353ms, mean:  367ms, max:  390ms
get_webpage (google.de,          11.3kB): min:  532ms, mean:  548ms, max:  574ms
get_webpage (stackoverflow.com, 273.5kB): min: 1331ms, mean: 1686ms, max: 2462ms
```


### See also

* [Enhanced Data Rates for GSM Evolution](https://en.wikipedia.org/wiki/Enhanced_Data_Rates_for_GSM_Evolution)
* [UMTS](https://en.wikipedia.org/wiki/UMTS)


## Code

See [Github](https://github.com/MartinThoma/algorithms/blob/master/Python/timing/lookup.py) for the snippet.


## Footnotes

[^1]: Netflix: <a href="https://help.netflix.com/en/node/306">Internet Connection Speed Recommendations</a>, read 2019-08-30.
