---
layout: post
title: Computer Temperature
slug: computer-temperature
author: Martin Thoma
date: 2019-06-05 20:00
category: My bits and bytes
tags: Hardware
featured_image: logos/star.png
---
I just realized that my Thinkpad T460p gets really loud. I suspect that there
is just quite some dust in the machine so that the fan gets louder. But I'm not
sure how to check that and I hesitate to open the machine. So let's see which
information I can get form the software.


## My System

* Hardware: Lenovo Thinkpad T460p
* Software: Ubuntu 18.04
* Running: Chrome (no videos playing; no Flash), Sublime Text - nothing fancy


## CPU Temperture

My room temperature is 24°C, my CPU temperature is roughly 50°C:

```
sensors
coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +54.0°C  (high = +100.0°C, crit = +100.0°C)
Core 0:        +51.0°C  (high = +100.0°C, crit = +100.0°C)
Core 1:        +50.0°C  (high = +100.0°C, crit = +100.0°C)
Core 2:        +54.0°C  (high = +100.0°C, crit = +100.0°C)
Core 3:        +49.0°C  (high = +100.0°C, crit = +100.0°C)

thinkpad-isa-0000
Adapter: ISA adapter
fan1:        2506 RPM

acpitz-virtual-0
Adapter: Virtual device
temp1:        +50.0°C  (crit = +128.0°C)

iwlwifi-virtual-0
Adapter: Virtual device
temp1:        +34.0°C

pch_skylake-virtual-0
Adapter: Virtual device
temp1:        +47.0°C
```


## HDD Temperature

My HDD (a Samsung SSD) is roughly 40°C.

```
sudo hddtemp /dev/sda
/dev/sda: SAMSUNG MZ7LN512HCHP-0001L              �: 39°C
```


## Make it Silent

I installed `thermald` and soon after that it got more silent. Could be
coincidence, though.

### Intel vs Nvidia

Changing from Nvidia to Intel dropped the CPU temperature from roughly 50°C to
roughly 40°C and the SSD to 38°C.

```
sensors
coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +42.0°C  (high = +100.0°C, crit = +100.0°C)
Core 0:        +41.0°C  (high = +100.0°C, crit = +100.0°C)
Core 1:        +41.0°C  (high = +100.0°C, crit = +100.0°C)
Core 2:        +40.0°C  (high = +100.0°C, crit = +100.0°C)
Core 3:        +40.0°C  (high = +100.0°C, crit = +100.0°C)

thinkpad-isa-0000
Adapter: ISA adapter
fan1:        2409 RPM

acpitz-virtual-0
Adapter: Virtual device
temp1:        +42.0°C  (crit = +128.0°C)

iwlwifi-virtual-0
Adapter: Virtual device
temp1:        +33.0°C

pch_skylake-virtual-0
Adapter: Virtual device
temp1:        +44.0°C
```