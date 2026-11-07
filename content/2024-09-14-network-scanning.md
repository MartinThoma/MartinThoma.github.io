---
layout: post
title: Network Scanning 😈
slug: network-scanning
lang: en
author: Martin Thoma
date: 2024-09-14 10:41
category: Security
tags: Security, AppSec
featured_image: logos/cybersecurity.png
summary: Assume you are an attacker and you are in the network you want to attack. What is your next step?
medium_url: https://medium.com/@martinthoma/network-scanning-9d9e83897490
status: draft
---
<figure class="ai-generated">
    <a href="../images/2024/09/network-scanning-1.jpg"><img src="../images/2024/09/network-scanning-1.jpg" alt="A router in the middle of a network with laptops, servers, phones and a cloud, sending out radio waves" width="800" height="800"></a>
    <figcaption>Scanning a network: which devices are there?</figcaption>
</figure>

## Host Discovery via Ping

First, you want to see who/what else is in the network. To do so, you want to execute a *ping* to every single address in the network. When you get a response, you know somebody is there:

```shell
# Find your network
$ ifconfig | grep "inet 192"
     inet 192.168.178.21  netmask 255.255.255.0  broadcast 192.168.178.255

# Execute a ping scan in your local network
$ nmap -sn 192.168.178.0/24
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-10 17:56 CEST
Nmap scan report for _gateway (192.168.178.1)
Host is up (0.0042s latency).
Nmap scan report for pc08 (192.168.178.21)
Host is up (0.00031s latency).
Nmap scan report for 192.168.178.26
Host is up (0.046s latency).
Nmap scan report for 192.168.178.34
Host is up (0.057s latency).
Nmap scan report for 192.168.178.39
Host is up (0.021s latency).
Nmap done: 256 IP addresses (5 hosts up) scanned in 2.88 seconds

# Using masscan
$ sudo masscan 192.168.178.0/24 --ping
Starting masscan 1.0.5 (http://bit.ly/14GZzcT)
    at 2024-09-14 07:30:27 GMT
 -- forced options: -sn -n --randomize-hosts -v --send-eth
Initiating ICMP Echo Scan
Scanning 256 hosts
Discovered open port 0/icmp on 192.168.178.1
Discovered open port 0/icmp on 192.168.178.26
Discovered open port 0/icmp on 192.168.178.34
Discovered open port 0/icmp on 192.168.178.38
Discovered open port 0/icmp on 192.168.178.39
```

If you want to know more about host discovery:

[**Host Discovery | Nmap Network Scanning** *One of the very first steps in any network reconnaissance mission is to reduce a (sometimes huge) set of IP ranges into…*](https://nmap.org/book/man-host-discovery.html)

## Service Discovery via Port Scanning

Once you have found a host such as 192.168.0.123 in your network, you want to find out what they are running. The nmap flags `-sV` give you the services with the versions after scanning the most common ports:

```shell
$ nmap -sV 192.168.0.123
Nmap scan report for 192.168.0.123
Host is up (0.00013s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux;
                               protocol 2.0)
25/tcp   open  smtp        Postfix smtpd
80/tcp   open  http        Apache httpd 2.4.41 ((Ubuntu))
631/tcp  open  ipp         CUPS 2.3
3306/tcp open  nagios-nsca Nagios NSCA
5432/tcp open  postgresql  PostgreSQL DB 9.6.0 or later
1 service unrecognized despite returning data.
If you know the service/version, please submit the following fingerprint
at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port5432-TCP:V=7.80%I=7%D=9/10%Time=66DFED59%P=x86_64-pc-linux-gnu%r(SM
SF:BProgNeg,8C,"E\0\0\0\x8bSFATAL\0VFATAL\0C0A000\0Munsupported\x20fronten
SF:d\x20protocol\x2065363\.19778:\x20server\x20supports\x202\.0\x20to\x203
SF:\.0\0Fpostmaster\.c\0L2120\0RProcessStartupPacket\0\0");
Service Info: Host:  pc08.fritz.box; OS: Linux;
CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at
https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.45 seconds
```

You can scan any port range you want.

You can also get information about the running operating system via the flag `nmap -O`:

```bash
$ sudo nmap -O 192.168.0.123
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-10 21:23 CEST
Nmap scan report for 192.168.0.123
Host is up (0.000075s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
25/tcp   open  smtp
80/tcp   open  http
631/tcp  open  ipp
3306/tcp open  mysql
5432/tcp open  postgresql
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops
```

## Vulnerability Scanning

The attacker now knows which OS is running and has some open ports with software and their versions running there. But how do they find vulnerabilities?

The [nmap script category vuln](https://nmap.org/nsedoc/categories/vuln.html) gives you some:

```shell
$ sudo nmap --script vuln localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-10 21:28 CEST
Pre-scan script results:
|_broadcast-avahi-dos: ERROR: Script execution failed (use -d to debug)
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000090s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
25/tcp   open  smtp
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
| smtp-vuln-cve2010-4344:
|_  The SMTP server is not Exim: NOT VULNERABLE
| ssl-dh-params:
|   VULNERABLE:
|   Anonymous Diffie-Hellman Key Exchange MitM Vulnerability
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use anonymous
|       Diffie-Hellman key exchange only provide protection against passive
|       eavesdropping, and are vulnerable to active man-in-the-middle attacks
|       which could completely compromise the confidentiality and integrity
|       of any data exchanged over the resulting session.
|     Check results:
|       ANONYMOUS DH GROUP 1
|             Cipher Suite: TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: Unknown/Custom-generated
|             Modulus Length: 2048
|             Generator Length: 8
|             Public Key Length: 2048
|     References:
|_      https://www.ietf.org/rfc/rfc2246.txt
|_sslv2-drown:
80/tcp   open  http
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum:
|   /phpmyadmin/: phpMyAdmin
|_  /server-status/: Potentially interesting folder
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
631/tcp  open  ipp
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
| http-slowloris-check:
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|
|     Disclosure date: 2009-09-17
|     References:
|       http://ha.ckers.org/slowloris/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_sslv2-drown:
3306/tcp open  mysql
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
5432/tcp open  postgresql
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
|_sslv2-drown:
```

Interesting. I didn’t even remember that I installed phpmyadmin 😄

## How can I defend?

Most importantly: **Uninstall software** you don’t need and **update software** you use.

**Client isolation** will prevent the clients from talking to each other. That also means they cannot detect each other. In home routers like FritzBox/Netgear/TP-Link this is easiest with a “Guest Network”.

You can certainly do more, but I’m not qualified to describe those:

* **Network Segmentation and Segregation**: The idea is similar to client isolation. Instead of letting everybody talk to all other hosts in the network or nobody as within guest networks, you make virtual networks (VLANs) where groups can talk to each other.
* **Intrusion Detection System (IDS)**: You can configure [iptables for routing and dnsmasq as a DHCP server/DNS proxy](https://blag.nullteilerfrei.de/2017/04/16/snort-on-raspberry-pi-behind-fritzbox/). Then you can use [snort](https://en.wikipedia.org/wiki/Snort_%28software%29) to detect and/or block network scanning.

<!-- series: appsec -->
