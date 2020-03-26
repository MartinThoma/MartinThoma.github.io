---
layout: post
title: Raspberry Pi
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Cyberculture
tags:
- Raspberry Pi
featured_image: logos/raspberry-pi.png
---

This mini-article describes what you need to get a Raspberry Pi to run.


## Get the Hardware

Get all the hardware you need. That might include:

* Power supply: I use the Rydges 5V 2000 mAh unit for 12.99 Euro
* microSD memory card (>= 8GB): The Raspberry does not ship with a hard drive.
  I use the SanDisk SDSDQUN-032G-FFP-A Class 10 card with 32GB for 14.99 Euro.
* WiFi dongle: I use the EDIMAX EW-7811UN Wireless USB Adapter, 150 Mbit/s, IEEE802.11b/g/n for 7.99 Euro
* HDMI to VGA adapter: 15.85 Euro
* Ethernet cable - it does NOT have built-in WiFi!
* USB mouse
* USB keyboard


## Get the OS

Now install the operating system. You need another computer with a card reader
for this step.

First, you should [Download Raspbian](https://www.raspberrypi.org/downloads/).
Then you can check if the image got downloaded correctly. To do so,
enter the following command

```bash
$ sha1sum 2015-05-05-raspbian-wheezy.zip
cb799af077930ff7cbcfaa251b4c6e25b11483de  2015-05-05-raspbian-wheezy.zip
```

Now go to the download page and search for
`cb799af077930ff7cbcfaa251b4c6e25b11483de`. If this step worked, you can follow
the [image installation guide](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) and copy the image on your micro-SD card.

After it booted, I had to set my keyboard layout from an English layout to
German:

```bash
$ setxkbmap de
```

This will only last for one session. To make the change permanently, you
can execute

```bash
$ sudo dpkg-reconfigure keyboard-configuration
```


## Clone the SD card

```bash
# from sd-card to your computer (make sure /dev/sdb is your sd card)
$ sudo dd if=/dev/sdb of=~/raspi.img

# and back (make sure /dev/sdb is your sd card)
sudo dd if=~/raspi.img of=/dev/sdb
```


## See also

* [raspberrypi.stackexchange.com](http://raspberrypi.stackexchange.com/)
