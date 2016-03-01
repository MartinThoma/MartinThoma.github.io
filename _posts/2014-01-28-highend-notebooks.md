---
layout: post
title: Highend Notebooks
author: Martin Thoma
date: 2014-01-28 16:00
categories:
- Cyberculture
tags:
- Notebook
- Hardware
- Review
featured_image: 2014/01/samsung-series-9-thumbnail.png
---
My [Acer Travelmate 5744Z](../review-des-acer-travelmate-5744z/)
seems to get broken in soon, so I'm currently looking for a new
notebook. As I use my notebook quite often and as this is the third
notebook within three years that is not usable any longer
(the screen of the first is defect and the graphic card / WLAN of the
second does not work propperly with the new Linux kernel), I'm would like to have
a high end notebook this time. I hope that I not have to think about
notebooks for at least 5 years after that.

## Requirements ##
I work quite a lot with the computer, so the keyboard and the display
have to be good. What does good mean? Well, the display has to be
**at least 15"** and as I don't want to see my pixels any longer it
has to have a **higher resolution than 1366×768**. But it has to be
**smaller than 30cm × 38cm** to fit into my knapsack. A reason why
I do not always have my current notebook with me is that it is
too heavy with about 2.5kg and does only run for about 3.5h. The new
one should be **lighter than 2.5kg** and **run at least 4h**.

**Ubuntu** has to be supported completely, especially WLAN, sound and
Bluetooth. Speaking of Bluetooth, I want **Bluetooth 4.0**, because
it introduced a low energy protocol that might be usefull for notebooks.
As I live in a city and as I access the internet via my neighbors
WLAN (thank you!), I need a good connection: **Dual band and 802.11a/b/g/n**
need to be supported by the notebook. (Dual band is sometimes also called 2x2).

I use it mainly for writing blog articles, LaTeX stuff and some
Python programming and watching movies. I download movies via
Online TV Recorder which sums up quite soon. Transfering this to my
external HDD always takes a lot of time. The new notebook should
support **USB 3.0** to speed this up. As I don't have to store
anything large, **80 GB SSD** is enough. It should be a SSD, because
they consume less power, are more durable and are more silent.

I need at least **4GB RAM** because ... well, did you ever try to
use Eclipse for Java+JBoss programming with less than 4GB? I don't
want to have that again.

It would be nice if I could use the notebook outside in the summer
which means it has to have a **bright matte display**.

I want a silent notebook, because I'm very sensitive to noise.
My current notebook has **less than 30 dB in normal mode** (no heavy load).
That should set the mark.

A SD-Card Reader would be nice, but it is not required. Just like
a RJ-45 for network cables and a DVD drive you can get it via USB.

I robust case is also important. I had troubles working in the train,
because the screen was whipping as hell. But this is not a hard
requirement for me as I don't work in trains that often.

## Current Favorites ##
I've looked at a lot of notebooks and I did mainly focus on the
technical specification and not at the price (I guess I might work
about 10h every day in front of this machine. A good, working
notebook is very important to me). However, when I see some notebooks
that are ok according to the specs from above, I will take the cheaper
one.

By the way, while searching for notebooks I discovered that much of
the data on Amazon is wrong. See for example the dimensions of
the HP EliteBook 8570p-B6Q03EA-ABD (51.6 x 34.2 x 7.8 cm according to Amazon).

|                    | Asus Zenbook       | Samsung Notebook Serie 9            |
|--------------------|--------------------|-------------------------------------|
| Model              | UX51VZ-DB114H      | 900X4D K01                          |
| Price              | 1380 Euro          |  995 Euro                           |
| Dimensions (B × D × H)| 380 × 254 × 20  | 356.9 × 237 × 14.9 mm               |
| Weight             | 2.2 kg             | 1.58 kg                             |
| CPU                | Intel Core i7 3632QM | [Intel Core i5-3337U](http://ark.intel.com/products/72055) |
| Display Size       | 15.6"              | 15"                                 |
| Display Resolution | 2880×1620          | 1600×900                            |
| Display more       |                    | LED-Display, 400 Nit                |
| Matte display      | ✘                  | ✔                                  |
| RAM                | 8 GB DDR3, 1600 MHz| 2× 4 GB DDR3  SDRAM1.600 MHz        |
| Disk               | 256 SSD            | 128 GB SSD                          |
| Network            | ?                  | RJ45 with adapter and 1.000 Mbit/s  |
| Wireless           | 802.11a/g/n, WiDi  | 802.11a/b/g/n (2×2), WiDi           |
| WLAN-Chip          | ?                  | Intel Wireless-N 7260               |
| Bluetooth          | 4.0                | 4.0                                 |
| Akku               | 4750 mAh           | 8200 mAh, up to 10h                 |
| USB                | 3× USB 3.0         | 2× USB 3.0, 1× USB 2.0              |
| SD Card Reader     | ✔                  | ✔                                  |
| Linux-Support      | ?                  | partially ([^1],[^2], [^3])         |
| Keyboard           | ?                  | Chiclet-keyboard without numblock   |
| Noise              | ?                  | 29.5 dB in normal mode, 40 dB max   |

{% gallery columns="2" %}
   ../images/2014/01/samsung-serie-9-keyboard-layout.png   "Samsung Series 9"
   ../images/2014/01/macbook-pro-retina-keyboard-layout.jpg   "Macbook Pro"
{% endgallery %}

The WLAN chipset of the Samsung Serie 9 seems to cause trouble with
Linux, but it also seems to be solved by a firmware update.[^5]
But one hint seems to be important:

> Before you install Linux on a Samsung Serie 9, make sure you update the firmware,
> because that's only possible with Windows.


Asus Zenbook seems also to work almost out of the box.[^6]
I've just learned that you can use

```bash
sudo dmidecode -s system-product-name
```

to determine your exact laptop product name.

In the following, I will give you an overview of the notebooks I took
a look at. I think all of them are very good.

In many cases I will need some more equipment:

* MicroHDMI 2 VGA adapter: Samsung AA-AH2NMHB/E for 29.90 Euro
* USB Ethernet adapter: "Cable Matters - SuperSpeed USB 3.0" for 16 Euro
* External DVD burner: Samsung SE-208DB for 30 Euro works with DVD±R Dual layer disks and DVD±RW disks. Is there anything more important to look at?


Others:

* Lenovo Thinkpad T450s (20BWS1UT00 with i5-5200U, Nvidia GeForce 940M). See [notebookcheck](http://www.notebookcheck.com/Test-Lenovo-ThinkPad-T450s-940M-Ultrabook.142299.0.html)
* TUXEDO Book BU1505
* Samsung ATIV Book 9 2014 Edition
* Lenovo ThinkPad X1
* [Notebook for developers](http://hardwarerecs.stackexchange.com/questions/1495/notebook-for-developers)


## Acer ##

|                    | Acer Aspire            |
|--------------------|------------------------|
| Model              | V5-573G-54208G50aii    |
| Price              | 649  Euro              |
| Dimensions (B × D × H)| 382 × 256 × 18      |
| Weight             | 2.04 kg                |
| CPU                | Intel Core i5-4200U    |
| Display Size       | 15.6"                  |
| Display Resolution | 1920 × 1080            |
| Matte display      | ✔                      |
| RAM                | 8 GB DDR3, 1600 MHz    |
| Disk               | 1000 GB HDD            |
| Network            | 10/100/1000MBit        |
| Wireless           |                        |
| WLAN-Chip          | Atheros AR5BWB222      |
| Bluetooth          | 4.0                    |
| Akku               | 3560 mAh               |
| USB                | 1× USB 3.0, 2× USB 2.0 |
| SD Card Reader     | ✔                      |
| Linux-Support      | ✔                      |
| Keyboard           | Chiclet-Keyboard       |
| Noise              | 33.3 dB                |

## Apple ##

|                    | Macbook  Pro                       |
|--------------------|------------------------------------|
| Model              | Retina 15"                         |
| Price              | 1999 Euro                          |
| Dimensions (B × D × H)| 358.9 × 247.1 × 18 mm              |
| Weight             | 2.02 kg                            |
| CPU                | [Intel Core i7 2760QM](http://ark.intel.com/products/53474) |
| Display Size       | 15.4"                              |
| Display Resolution | 2880×1800                          |
| Display more       |                                    |
| Matte display      | ✔                                  |
| RAM                | 8 GB 1600 MHz DDR3L                |
| Disk               | 256 SSD                            |
| Network            | no RJ45                            |
| Wireless           | 802.11a/b/g/n                      |
| WLAN-Chip          | ?                                  |
| Bluetooth          | 4.0                                |
| Akku               | up to 7h                           |
| USB                | 2× USB 3.0                         |
| SD Card Reader     | ✔                                  |
| Linux-Support      | ?                                  |
| Keyboard           | Chiclet-Keyboard                   |
| Noise              | 29.4 dB in normal mode, 47.4 dB max|

Although the hardware looks very nice, it is still comparable with
both of my favorites.

## Asus ##

### Asus Zenbooks ###

|                    | Asus Zenbook       | Asus Zenbook          | Asus Zenbook          |
|--------------------|--------------------|-----------------------|-----------------------|
| Model              | UX51VZ-CN035H      | UX51VZ-DB114H         | U500VZ                |
| Price              | 1390 Euro          | 1380 Euro             | 1350 Euro             |
| Dimensions (B × D × H)| 380 × 254 × 20  | 380 × 254 × 20        | 380 × 254 × 20 mm     |
| Weight             | 2.2 kg             | 2.2 kg                | 2.2 kg                |
| CPU                |Intel Core i7-3612QM| Intel Core i7 3632QM  | Intel Core i7-3612QM  |
| Display Size       | 15.6"              | 15.6"                 | 15.6"                 |
| Display Resolution |1920×1080           | 2880×1620             | 1920×1080             |
| Matte display      | ✔                  | ✘                     | ✔                     |
| RAM                | 8 GB DDR3, 1600 MHz| 8 GB DDR3, 1600 MHz   | 4 GB                  |
| Disk               | 256 SSD            | 256 SSD               | 512 GB SSD            |
| Network            | 10/100/1000, RJ45  | ?                     | ?                     |
| Wireless           | 802.11a/g/n, 2×2 WiDi | 802.11a/g/n, WiDi  | 802.11a/b/g/n, 2×2    |
| WLAN-Chip          | ?                  | ?                     | ?                     |
| Bluetooth          | 4.0                | 4.0                   | 4.0                   |
| Akku               | ?                  | 4750 mAh              | 4750 mAh              |
| USB                | 3× USB 3.0         | 3× USB 3.0            | 2× USB 3.0            |
| SD Card Reader     | ✔                  | ✔                     | ✔                     |
| Linux-Support      | ?                  | ?                     | ?                               |
| Keyboard           | ?                  | ?                     | Chiclet-Keyboard with Numblock  |
| Noise              | ?                  | ?                     | 34 dB in normal mode, 42 dB max |

### Asus PU500CA-XO002X and Asus N550JV-CN201H ###

|                    | Asus                  | Asus             |
|--------------------|-----------------------|------------------|
| Model              | PU500CA-XO002X        | N550JV-CN201H    |
| Price              | 998 Euro              | 1099             |
| Dimensions (B × D × H)| 383 × 257 × 22.5 mm| 383 × 255 × 27   |
| Weight             | 1.96 kg               | 2.7 kg           |
| CPU                | Intel Core i5-3317U   | Intel Core i7-4700HQ |
| Display Size       | 15.6"                 | 15.6"            |
| Display Resolution | 1366 × 768            | 1920 × 1080      |
| Matte display      | ✔                     | ✔                |
| RAM                | 4 GB                  | 8GB DDR3         |
| Disk               | 524 GB                | 1000 GB HDD      |
| Network            | ?                     | ?                |
| Wireless           | 802.11 a/b/g/n, WiDi  | 802.11 b/g/n     |
| WLAN-Chip          |                       | Atheros (AR9485) |
| Bluetooth          | 4.0                   | 4.0              |
| Akku               | 4000 mAh, up to 7h    | 4000 mAh         |
| USB                | 1× USB 3.0            | 2× USB 3.0       |
| SD Card Reader     | ✔                     | ✔                |
| Linux-Support      | ?                     | ?                |
| Keyboard           | Chiclet-Keyboard with Numblock      | Chiclet-Keyboard with Numblock      |
| Noise              | 30.7 dB in normal mode, 38.4 dB max | 32.9 dB in normal mode, 38 dB max   |

## Dell ##

|                    | [XPS 15](http://www.notebookcheck.com/Test-Dell-XPS-15-2015-Notebook.137681.0.html) |
|--------------------|----------------------|
| Model              | 9530-1906            |
| Price              | 1711  Euro           |
| Dimensions (B × D × H)| 372 × 254 × 18    |
| Weight             | 2.02 kg              |
| CPU                | Intel Core i7-4702HQ |
| Display Size       | 15.6"                |
| Display Resolution | 3200x1800            |
| Matte display      | ✘                    |
| RAM                | 8 GB DDR3L, 1600 MHz |
| Disk               | 512 GB SSD           |
| Network            | (no RJ45)            |
| Wireless           | 802.11 ac, 2x2       |
| WLAN-Chip          | Intel AC 7260        |
| Bluetooth          | 4.0                  |
| Akku               | ?                    |
| USB                | 3× USB 3.0           |
| SD Card Reader     | ✔                   |
| Linux-Support      | ?                    |
| Keyboard           | Chiclet-Keyboard     |
| Noise              | 29.8 dB, 42.1 dB max |

There seem to be other versions of the XPS 15:

* XPS 15 (L501X)
* XPS 15 (L502X)
* XPS 15z

However, I was not able to find any specification of those.

## Fujitsu ##

|                    | Fujitsu Lifebook   |
|--------------------|--------------------|
| Model              | E753               |
| Price              | 1759  Euro         |
| Dimensions (B × D × H)| 374 × 374 × 20  |
| Weight             | 1.99 kg            |
| CPU                | Intel Core i7-3632QM |
| Display Size       | 15.6"              |
| Display Resolution | 1920×1080          |
| Matte display      | ✔                  |
| RAM                | 8 GB DDR3          |
| Disk               | 256 GB SSD         |
| Network            | 10/100/1000MBit    |
| Wireless           | 802.11 a/b/g/n     |
| WLAN-Chip          | Centrino Advanced-N 6235 |
| Bluetooth          | 4.0                |
| Akku               | 6700 mAh           |
| USB                | 3× USB 3.0         |
| SD Card Reader     | ✔                  |
| Linux-Support      | ?                  |
| Keyboard           | Chiclet-Keyboard   |
| Noise              | 33.3 dB            |

## HP ##

|                    | HP Envy 15            |
|--------------------|-----------------------|
| Model              | J011SG                |
| Price              | 811 Euro              |
| Dimensions (B × D × H)| 380 × 251 × 28     |
| Weight             | 2.19 kg               |
| CPU                | Intel Core i5-4200M   |
| Display Size       | 15.6"                 |
| Display Resolution | 1920×1080             |
| Matte display      | ✘                     |
| RAM                | 12 GB DDR3L, 1600 MHz |
| Disk               | 1000 GB               |
| Network            | 10/100/1000 RJ-45     |
| Wireless           | 802.11b/g/n           |
| WLAN-Chip          | Intel AC 7260         |
| Bluetooth          | 4.0                   |
| Akku               | 2200 mAh              |
| USB                | 4× USB 3.0            |
| SD Card Reader     | ✔                     |
| Linux-Support      | ?                     |
| Keyboard           | with numblock         |
| Noise              | ?                     |



## Samsung ##

### Serie 9 ###
The next few lines show the difference of the `900X4C A0A` to...

* `NP900X4C-A01`: Intel Core i5-3317U, 128GB SSD, no Dualband
* `900X3C A03`: 3610 mAh, 1399 Euro
* `900X4B-A01`: Intel Core i7 2637M, 1999 Euro
* `900X4C-A04`: Intel Core i5 3317U, 1999 Euro
* `900X4C-A05`: Intel Core i5 3317U, 128GB SSD, no Dualband, ca 1200 Euro
* `900X4C A06`: 256 GB SSD, 15.6" Display, 1629 Euro
* `900X4C A09`: Costs 1999 Euro (any other difference?)
* `900X4D A03` has also 15" Display, but only 4GB RAM and a
   [Intel Core i5-3317U](http://ark.intel.com/products/65707) and a
   128 GB SSD. But it
   costs only 799 Euro.
* `900X4D K01`: Intel Core i5-3337U, 128 GB SSD, 8400 mAh, Dual Band, 997 Euro

### Samsung ATIV Book 9 2014 Edition ###

|                    | Samsung ATIV Book 9 2014 Edition   |
|--------------------|------------------------------------|
| Model              | NP930X5J-K01DE                     |
| Price              |  1599 Euro                         |
| Dimensions (B × D × H)|  ? × ? × 14.9 mm                |
| Weight             |  1.78 kg                           |
| CPU                | [Intel Core i7-4500U](http://ark.intel.com/products/75460) |
| Display Size       | 15.6"                              |
| Display Resolution | 1920×1080                          |
| Display more       | Touch-Display                      |
| Matte display      | ✘                                 |
| RAM                | 8 GB ? MHz                         |
| Disk               | 256GB SSD                          |
| Network            | RJ45 with adapter and 1.000 Mbit/s |
| Wireless           | 802.11 ac (2x2) ([source](http://de.samsung.com/webdownloads/pressedownloads/Presseinformation_Samsung_ATIV_Book_9_Edition_2014_1.pdf)) |
| WLAN-Chip          | Intel Wireless-AC 7260, 802.11 ac  |
| Bluetooth          | 4.0                                |
| Akku               | ?, 14h                             |
| USB                | 2× USB 3.0, 1 × USB 2.0            |
| SD Card Reader     | ✔                                 |
| Linux-Support      | ?                                  |
| Keyboard           | Chiclet-keyboard                   |
| Noise              | ?                                  |


* Good audio qualit: 24-bit, 192kHz audio, 2x 2W
* HDMI out, mini VGA, an SD card reader
* 720p webcam

Release date should be 28.03.2014 ([source](http://www.arlt.com/Notebook/Ultrabooks/Samsung/Samsung-ATIV-Book-9-NP930X5J-K01DE-2014-Edition.html)).

#### Sources ####

* [techradar.com](http://www.techradar.com/reviews/pc-mac/laptops-portable-pcs/laptops-and-netbooks/samsung-ativ-book-9-2014-edition-1212115/review)
* [notebookcheck.de](http://www.notebookcheck.com/Samsung-praesentiert-Notebook-Ativ-Book-9-2014-Edition.108498.0.html)


## Tuxedo ##

|                    | Tuxedo Book                        |
|--------------------|------------------------------------|
| Model              | BC1503                             |
| Price              |  763 Euro                          |
| Dimensions (B × D × H)|  374 × 252 × 31 mm              |
| Weight             |  2.4 kg                            |
| CPU                | [Intel Core i5 4200M](http://ark.intel.com/products/76348) |
| Display Size       | 15.6"                              |
| Display Resolution | 1920×1080                          |
| Display more       | IPS-Display                        |
| Matte display      | ✔                                 |
| RAM                | 1×8 GB 1600 MHz                    |
| Disk               | 120 SSD (Samsung EVO / SATA III)   |
| Network            | has RJ45 built-in, 10/100/1000     |
| Wireless           | 802.11 ac/a/b/g/n                  |
| WLAN-Chip          | Intel Dual AC7260                  |
| Bluetooth          | 4.0                                |
| Akku               | 62,16 Wh, 2.5h[^4]                 |
| USB                | 2× USB 3.0                         |
| SD Card Reader     | ✔                                 |
| Linux-Support      | shipped with Linux Mint ☺        |
| Keyboard           | ?                                  |
| Noise              | Laut[^4]                           |

See also: [tuxedocomputers.com](https://www.tuxedocomputers.com/Linux-Hardware/Linux-Notebooks/15-6-Zoll/TUXEDO-Book-BU1505-15-6-matt-Full-HD-IPS-bis-Intel-Core-i7-Energiespar-CPU-zwei-HDD-SSD-bis-16GB-RAM-bis-10h-Akku-bel-Tastatur-Slim-Book-LTE-opt.geek), [linux-onlineshop.de](http://www.linux-onlineshop.de/Linux-Hardware/Linux-Notebooks/15-6-Zoll/TUXEDO-Book-BU1505-15-6-matt-Full-HD-IPS-bis-Intel-Core-i7-Energiespar-CPU-zwei-HDD-SSD-bis-16GB-RAM-bis-10h-Akku-bel-Tastatur-Slim-Book-LTE-opt.geek)

* TUXEDO Book BU1505 (with Skylake, up to 16GB RAM, ca. 1240 Euro)


## Librem 15

|                    | [Librem 15](https://puri.sm/librem-15/) |
|--------------------|------------------------------------|
| Model              |                                    |
| Price              |  2185 Euro                         |
| Dimensions (B × D × H)|  375 × 244 × 22 mm              |
| Weight             |  2.0 kg                            |
| CPU                | [Intel i7-5557U](http://ark.intel.com/products/84993/Intel-Core-i7-5557U-Processor-4M-Cache-up-to-3_40-GHz) (Broadwell-U architecture) |
| Display Size       | 15.6"                              |
| Display Resolution | 3840×2160                          |
| Display more       | IPS-Display                        |
| Matte display      | ✔                                 |
| RAM                | 1×8 GB 1600 MHz                    |
| Disk               | 250 GB SSD                         |
| Network            | ✘, 10/100/1000                    |
| Wireless           | 802.11 n                           |
| WLAN-Chip          | ?                                  |
| Bluetooth          | ✔, ?                              |
| Akku               | 65W, 48 Wh, Up to 6 hours usage    |
| USB                | 1× USB 3.1, 2× USB 3.0             |
| SD Card Reader     | SDXC                               |
| Linux-Support      | ✔                                  |
| Keyboard           | ?                                  |
| Noise              | ?                                  |


#### Other ####
On a first glance, the Samsung ATIV Book 8 NP880Z5E-X01 looked quite
promising. But it doesn't have an SSD, it weights 2.54 kg, but has
no optical drive.

* Samsung ATIV 870Z5E-X03DE


* ATIV Book 8 870Z5E X04
* ATIV Book 8 880Z5E X01
* ATIV Book 9 900X4D K01 ([notebookinfo.de](http://www.notebookinfo.de/produkte/samsung-ativ-book-9-900x4d-k01/np900x4d-k01de/00016092/#Datenblatt))

## Notebooks that did not meet the criteria ##

Display is too small:

* Chromebook Pixel has only 12.85"
* XPS 13 has only 13.3"
* Asus Zenbook has only 13.3"
* Lenovo IdeaPad U300s have only 13.3"
* All Samsung Series 9 X3A seem to have 13.3" displays
* Samsung Series 9 900X3D-A02: 13.3"
* Samsung Series 9 900X3C-A01: 13.3"
* Samsung Series 9 900X3C A07: 13.3"

Too low resolution:

* Acer TravelMate 6594eG-464G50Mikk
* Asuspro PU500
* All Acer Aspire TimelineU M5

To heavy:

* Lenovo IdeaPad Y510p: 2.89 kg
* HP EliteBook 8570p-B6Q03EA-ABD: 2.91 kg
* Sony Vaio VPC-F21Z1E/BI: 3.17 kg

Availability: seems not to be available on Amazon

* Samsung Serie 9 NP900X4C-A02
* Sony Vaio SV-E1511V1EW
* Sony Vaio VGN-TX2
* HP Envy 6-1000sg

Other:

* Acer Aspire M3-581TG: Too loud, only 667MHz RAM

## Dear Notebook-Producers ##
After searching so much for notebooks, I have some hints for you
what you could do better:

* Add a single specification page for each notebook. This page should include at least:
  * Weight in kg and dimensions in mm
  * Battery life in mAh
  * Display (size, glare or matte display, supported resolutions)
  * Exact CPU name (not only Intel i5 - if it varies, list all possible CPUs)
  * Disk (size, SSD or not)
  * Wireless support (IEEE 802.11 supported standards? Dual band? Bluetooth? Bluetooth version?)
  * Keyboard: Does it have a numblock? Backlit?
  * Does it have a DVD-Player / Burner? Blue-Ray?
  * Webcam (resolution)
  * Microphone
  * Sensors (GPS)
  * Image of the notebook
* A good specification page would include:
  * Noise in dB
  * Information about Linux support (especially Debian)
* Explain your version names!
* Provide a possibility to compare your products like Intel does with [ark.intel.com](http://ark.intel.com/) for its processors
* Provide a possibility to filter your products by technical specification.
* Add an image of your product to Wikipedia Commons

## References ##

[^1] [Linux and the Samsung Series 9 NP900X3C](http://blog.jospoortvliet.com/2012/09/linux-and-samsung-series-9-np900x3c.html): A review for the NP900X3C and openSUSE on 24th or September, 2012.
[^2] [Samsung Series 9 - Ubuntu Community Page](https://help.ubuntu.com/community/SamsungSeries9)
[^3] [Linux auf Samsung Series 9 2012](http://www.sump.org/blog/213)
[^4] [Tuxedo Book DC1502 im Test](http://www.pcwelt.de/produkte/Tuxedo-Book_DC1502-Standard-Notebook-Test-8115776.html)
[^5] [No wireless with Intel Centrino Advanced-N 7260](http://askubuntu.com/questions/322511/no-wireless-with-intel-centrino-advanced-n-7260)
[^6] [AsusZenbook - Ubuntu Community Page](https://help.ubuntu.com/community/AsusZenbook)
