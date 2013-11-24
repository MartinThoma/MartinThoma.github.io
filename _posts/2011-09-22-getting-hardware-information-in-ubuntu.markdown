---
layout: post
status: publish
published: true
title: Getting Hardware Information in Ubuntu
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 1341
wordpress_url: http://martin-thoma.com/?p=1341
date: 2011-09-22 20:44:21.000000000 +02:00
categories:
- Code
tags:
- cheat sheet
- Linux
- Ubuntu
- Hardware
comments: []
---
I'm using Ubuntu now for many years, but I always have to look the commands for retrieving hardware information up. Now I will not Google any longer but search in my own little cheat sheet.

I guess most commands will work in every Linux distribution, but I tried it only in Ubuntu 10.04LTS.

Maybe you need to install some packages.

If you know more commands, please post a comment!

<h2>CPU</h2>
[bash]cat /proc/cpuinfo

processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Pentium(R) Dual-Core CPU       T4500  @ 2.30GHz
stepping	: 10
cpu MHz		: 1200.000
cache size	: 1024 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fdiv_bug	: no
hlt_bug		: no
f00f_bug	: no
coma_bug	: no
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe nx lm constant_tsc arch_perfmon pebs bts aperfmperf pni dtes64 monitor ds_cpl est tm2 ssse3 cx16 xtpr pdcm xsave lahf_lm
bogomips	: 4588.23
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Pentium(R) Dual-Core CPU       T4500  @ 2.30GHz
stepping	: 10
cpu MHz		: 1200.000
cache size	: 1024 KB
physical id	: 0
siblings	: 2
core id		: 1
cpu cores	: 2
apicid		: 1
initial apicid	: 1
fdiv_bug	: no
hlt_bug		: no
f00f_bug	: no
coma_bug	: no
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe nx lm constant_tsc arch_perfmon pebs bts aperfmperf pni dtes64 monitor ds_cpl est tm2 ssse3 cx16 xtpr pdcm xsave lahf_lm
bogomips	: 4588.44
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:
[/bash]

<h2>RAM</h2>
[bash]free

             total       used       free     shared    buffers     cached
Mem:       4047112    1712724    2334388          0      94328     744808
-/+ buffers/cache:     873588    3173524
Swap:      8864760          0    8864760
[/bash]

<h2>Graphic card</h2>
[bash]lspci | grep VGA

00:02.0 VGA compatible controller: Intel Corporation Mobile 4 Series Chipset Integrated Graphics Controller (rev 07)[/bash]

And some more details:
[bash]lspci -s 00:02.0 -v
00:02.0 VGA compatible controller: Intel Corporation Mobile 4 Series Chipset Integrated Graphics Controller (rev 07)
	Subsystem: Acer Incorporated [ALI] Device 048a
	Flags: bus master, fast devsel, latency 0, IRQ 29
	Memory at d0000000 (64-bit, non-prefetchable) [size=4M]
	Memory at c0000000 (64-bit, prefetchable) [size=256M]
	I/O ports at 4110 [size=8]
	Capabilities: <access denied>
	Kernel driver in use: i915
	Kernel modules: i915[/bash]

<h2>Audio Chipset</h2>
[bash]lspci | grep Audio

00:1b.0 Audio device: Intel Corporation 82801I (ICH9 Family) HD Audio Controller (rev 03)[/bash]

And some more details:
[bash]lspci -s 00:1b.0 -v
00:1b.0 Audio device: Intel Corporation 82801I (ICH9 Family) HD Audio Controller (rev 03)
	Subsystem: Acer Incorporated [ALI] Device 048a
	Flags: bus master, fast devsel, latency 0, IRQ 22
	Memory at d6700000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: HDA Intel
	Kernel modules: snd-hda-intel[/bash]

<h2>Network Chipset</h2>
[bash]lspci | grep Network

04:00.0 Network controller: Atheros Communications Inc. AR9287 Wireless Network Adapter (rev 01)
[/bash]

Then get some more information:
[bash]lspci -s 04:00 -v
04:00.0 Network controller: Atheros Communications Inc. AR9287 Wireless Network Adapter (rev 01)
	Subsystem: Foxconn International, Inc. Device e034
	Flags: bus master, fast devsel, latency 0, IRQ 17
	Memory at d4600000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: ath9k
	Kernel modules: ath9k[/bash]

<h2>Monitor</h2>
The packages ddcprobe or xresprobe will help.

<h2>Hard disk</h2>
[bash]df -H

Dateisystem             Gr&ouml;&szlig;e   Benut  Verf Ben% Eingeh&auml;ngt auf
/dev/sda1              307G    28G   264G  10% /
none                   2,1G   320k   2,1G   1% /dev
none                   2,1G   934k   2,1G   1% /dev/shm
none                   2,1G   209k   2,1G   1% /var/run
none                   2,1G      0   2,1G   0% /var/lock
none                   2,1G      0   2,1G   0% /lib/init/rw[/bash]
