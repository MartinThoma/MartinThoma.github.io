---
layout: post
title: How to get Hardware Information on Linux Systems
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Linux
- Hardware
featured_image: logos/linux.png
---

Linux support for hardware is still not optimal. Before I buy any new device,
I check if Linux supports it.

[h-node.org](https://www.h-node.org/) is a new site where you can check if
devices are supported - and how well they are supported - by Linux.

So I hope that everybody who has a computer gives information to this project.

## How to test if your hardware is supported by Linux

1. [Get a Live CD system](https://www.debian.org/CD/live/)
2. Burn the downloaded iso image on a CD
3. Boot that CD and check the hardware support

### Speakers

Just search some `.wav` or `.ogg` files. `/etc/share/sounds/` might be a place
where you have some.

```bash
$ play /usr/share/sounds/alsa/Front_Left.wav
```

or

```bash
$ aplay /usr/share/sounds/alsa/Front_Left.wav
```

or

```bash
$ mplayer /usr/share/sounds/alsa/Front_Left.wav
```

other options are:

* `vlc` / `cvlc`
* `mpg123`

### Webcam

```bash
$ mplayer -vo png -frames 1 tv://
```

### Microphone

```bash
$ arecord -vv -fdat stackoverflow.wav
```

## How to get Software Information

It is essential that you know with which software you test your hardware.

Here is a command that gives you the distribution name and version:

```bash
$ cat /etc/issue
Linux Mint 16 Petra \n \l
```

And - more important - the used Linux kernel:

```bash
$ uname -a
Linux pc08 3.11.0-12-generic #19-Ubuntu SMP Wed Oct 9 16:20:46 UTC 2013 x86_64 x86_64 x86_64 GNU/Linux
```

## How to get hardware information

Many Linux systems offer many different ways to check hardware support.
I will show different ways for many different parts of the hardware. Some
require you to install additional software.

General console tools are:

* `lsusb`
* `lspci`
* `lshw`
* `dmidecode`

### Audio chipset

```bash
$ lspci | grep -i "audio"
00:1b.0 Audio device: Intel Corporation 5 Series/3400 Series Chipset High Definition Audio (rev 05)
```

or

```bash
$ sudo lshw -class multimedia
  *-multimedia
       description: Audio device
       product: 5 Series/3400 Series Chipset High Definition Audio
       vendor: Intel Corporation
       physical id: 1b
       bus info: pci@0000:00:1b.0
       version: 05
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress bus_master cap_list
       configuration: driver=snd_hda_intel latency=0
       resources: irq:43 memory:d0600000-d0603fff
```

### CPU

```bash
$ cat /proc/cpuinfo
processor   : 0
vendor_id   : GenuineIntel
cpu family  : 6
model       : 37
model name  : Intel(R) Pentium(R) CPU        P6200  @ 2.13GHz
stepping    : 5
microcode   : 0x2
cpu MHz     : 933.000
cache size  : 3072 KB
physical id : 0
siblings    : 2
core id     : 0
cpu cores   : 2
apicid      : 0
initial apicid  : 0
fpu     : yes
fpu_exception   : yes
cpuid level : 11
wp      : yes
flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni dtes64 monitor ds_cpl est tm2 ssse3 cx16 xtpr pdcm pcid popcnt lahf_lm arat dtherm
bogomips    : 4266.48
clflush size    : 64
cache_alignment : 64
address sizes   : 36 bits physical, 48 bits virtual
power management:

processor   : 1
vendor_id   : GenuineIntel
cpu family  : 6
model       : 37
model name  : Intel(R) Pentium(R) CPU        P6200  @ 2.13GHz
stepping    : 5
microcode   : 0x2
cpu MHz     : 2133.000
cache size  : 3072 KB
physical id : 0
siblings    : 2
core id     : 2
cpu cores   : 2
apicid      : 4
initial apicid  : 4
fpu     : yes
fpu_exception   : yes
cpuid level : 11
wp      : yes
flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni dtes64 monitor ds_cpl est tm2 ssse3 cx16 xtpr pdcm pcid popcnt lahf_lm arat dtherm
bogomips    : 4266.48
clflush size    : 64
cache_alignment : 64
address sizes   : 36 bits physical, 48 bits virtual
power management:
```

or

```bash
$ sudo lshw -class cpu
  *-cpu
       description: CPU
       product: Intel(R) Pentium(R) CPU        P6200  @ 2.13GHz
       vendor: Intel Corp.
       physical id: 20
       bus info: cpu@0
       version: Intel(R) Pentium(R) CPU        P6200  @ 2.13GHz
       slot: U3E1
       size: 1199MHz
       capacity: 4GHz
       width: 64 bits
       capabilities: x86-64 fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni dtes64 monitor ds_cpl est tm2 ssse3 cx16 xtpr pdcm pcid popcnt lahf_lm arat dtherm cpufreq
       configuration: cores=2 enabledcores=2 threads=2
```

### Graphic cards

```bash
$ sudo update-pciids
Downloaded daily snapshot dated 2014-09-16 03:15:02

$ lspci | grep -Ei --color 'vga|3d|2d'
00:02.0 VGA compatible controller: Intel Corporation Core Processor Integrated Graphics Controller (rev 02)

$ sudo lspci -v -s 00:02.0
00:02.0 VGA compatible controller: Intel Corporation Core Processor Integrated Graphics Controller (rev 02) (prog-i\f 00 [VGA controller])
    Subsystem: Acer Incorporated [ALI] Device 0612
    Flags: bus master, fast devsel, latency 0, IRQ 40
    Memory at d0000000 (64-bit, non-prefetchable) [size=4M]
    Memory at c0000000 (64-bit, prefetchable) [size=256M]
    I/O ports at 2050 [size=8]
    Expansion ROM at <unassigned> [disabled]
    Capabilities: [90] MSI: Enable+ Count=1/1 Maskable- 64bit-
    Capabilities: [d0] Power Management version 2
    Capabilities: [a4] PCI Advanced Features
    Kernel driver in use: i915
```

Or

```bash
sudo lshw -class display
  *-display
       description: VGA compatible controller
       product: Core Processor Integrated Graphics Controller
       vendor: Intel Corporation
       physical id: 2
       bus info: pci@0000:00:02.0
       version: 02
       width: 64 bits
       clock: 33MHz
       capabilities: msi pm vga_controller bus_master cap_list rom
       configuration: driver=i915 latency=0
       resources: irq:40 memory:d0000000-d03fffff memory:c0000000-cfffffff ioport:2050(size=8)
```

Or, for nvidia:

```bash
$ nvidia-smi
```

#### 3D acceleration

```bash
$ /usr/lib/nux/unity_support_test -p
OpenGL vendor string:   Intel Open Source Technology Center
OpenGL renderer string: Mesa DRI Intel(R) Ironlake Mobile
OpenGL version string:  2.1 Mesa 9.2.1

Not software rendered:    yes
Not blacklisted:          yes
GLX fbconfig:             yes
GLX texture from pixmap:  yes
GL npot or rect textures: yes
GL vertex program:        yes
GL fragment program:      yes
GL vertex buffer object:  yes
GL framebuffer object:    yes
GL version is 1.4+:       yes

Unity 3D supported:       yes
```

or

```bash
$ glxinfo | grep direct
direct rendering: Yes
```

### LAN

```bash
$ lspci | grep -i "ethernet"
03:00.0 Ethernet controller: Broadcom Corporation NetLink BCM57780 Gigabit Ethernet PCIe (rev 01)
```

or

```bash
$ sudo dmidecode | grep -i -B 2 -A 5 "ethernet"
Handle 0x000D, DMI type 10, 6 bytes
On Board Device Information
    Type: Ethernet
    Status: Enabled
    Description: Realtek Lan Controller

Handle 0x000E, DMI type 11, 5 bytes
OEM Strings
--
Onboard Device
    Reference Designation: Hanksville Gbe Lan Connection
    Type: Ethernet
    Status: Enabled
    Type Instance: 1
    Bus Address: 0000:00:00.1

Handle 0x0013, DMI type 136, 6 bytes

```

### Microphone

### Webcam

### WLAN

```bash
$ lspci | grep -i "wireless"
02:00.0 Network controller: Qualcomm Atheros AR9485 Wireless Network Adapter (rev 01)

$ sudo lspci -v -s 02:00.0
02:00.0 Network controller: Qualcomm Atheros AR9485 Wireless Network Adapter (rev 01)
    Subsystem: Lite-On Communications Inc Device 6617
    Flags: bus master, fast devsel, latency 0, IRQ 17
    Memory at d0500000 (64-bit, non-prefetchable) [size=512K]
    Expansion ROM at d0c00000 [disabled] [size=64K]
    Capabilities: [40] Power Management version 2
    Capabilities: [50] MSI: Enable- Count=1/4 Maskable+ 64bit+
    Capabilities: [70] Express Endpoint, MSI 00
    Capabilities: [100] Advanced Error Reporting
    Capabilities: [140] Virtual Channel
    Capabilities: [160] Device Serial Number 00-00-00-00-00-00-00-00
    Kernel driver in use: ath9k
```

or

```bash
$ sudo lshw -class network
  *-network
       description: Wireless interface
       product: AR9485 Wireless Network Adapter
       vendor: Qualcomm Atheros
       physical id: 0
       bus info: pci@0000:02:00.0
       logical name: wlan0
       version: 01
       serial: ------------
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress bus_master cap_list rom ethernet physical wireless
       configuration: broadcast=yes driver=ath9k driverversion=3.11.0-12-generic firmware=N/A ip=192.168.178.64 latency=0 link=yes multicast=yes wireless=IEEE 802.11bgn
       resources: irq:17 memory:d0500000-d057ffff memory:d0c00000-d0c0ffff
  *-network
       description: Ethernet interface
       product: NetLink BCM57780 Gigabit Ethernet PCIe
       vendor: Broadcom Corporation
       physical id: 0
       bus info: pci@0000:03:00.0
       logical name: eth0
       version: 01
       serial: ------
       size: 10Mbit/s
       capacity: 100Mbit/s
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress bus_master cap_list ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd autonegotiation
       configuration: autonegotiation=on broadcast=yes driver=tg3 driverversion=3.132 duplex=half firmware=sb latency=0 link=no multicast=yes port=MII speed=10Mbit/s
       resources: irq:44 memory:d0400000-d040ffff
```


## Troubleshoot

### WLAN



Sources:
* [My WiFi adapter is not working at all, how to troubleshoot?](http://askubuntu.com/questions/235279/my-wifi-adapter-is-not-working-at-all-how-to-troubleshoot)

## GUI-Tools

* `hardinfo`

## Other Linux Hardware Compatibility Lists

* [www.linux-drivers.org](http://www.linux-drivers.org/)
* [Debian GNU/Linux device driver check page](http://kmuto.jp/debian/hcl/)
* [InstallingDebianOn](https://wiki.debian.org/InstallingDebianOn/)
* [Hardwaredatenbank](http://wiki.ubuntuusers.de/Archiv/Hardwaredatenbank)
* [Hardware Compatibility List](http://www.linuxquestions.org/hcl/)

## See also

* [Linux Find Out Graphics Card Installed In My System](http://www.cyberciti.biz/faq/linux-tell-which-graphics-vga-card-installed/)
* Linux Wireless
  * [b43 and b43legacy](http://wireless.kernel.org/en/users/Drivers/b43)
  * [Supported Broadcom wireless devices](http://wireless.kernel.org/en/users/Drivers/b43/devices)
