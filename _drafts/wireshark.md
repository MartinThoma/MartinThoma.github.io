---
layout: post
title: Wireshark
author: Martin Thoma
date: 2013-02-05 03:17:04
categories: 
- The Web
tags: 
- Internet Security
- IT-Security
- Wireshark
featured_image: 2013/02/wireshark.png
---
Did you ever wonder if your wireless Internet access was secure? Do you want to check which packages your system sends without having to trust system internal tools? Then you should give <a href="http://en.wikipedia.org/wiki/Wireshark">Wireshark</a> a try. This tool allows you to capture and analyse all packages that your computer receives.

I've closed the browser and started Wireshark on my Ubuntu 10.04 (Linux) system. Then I've started my Windows 7 computer, logged in and did nothing for one hour on both computers. Wireshark 6759 packages in this hour. It looks like this:

[caption id="attachment_56401" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/02/wireshark-screenshot.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/wireshark-screenshot-300x157.png" alt="Screenshot of Wireshark" width="300" height="157" class="size-medium wp-image-56401" /></a> Screenshot of Wireshark[/caption]

<h2>How to filter packages</h2>
<ul>
  <li>192.168.0.139 is the IP address of my Windows 7 computer,</li>
  <li>192.168.0.169 is the IP address of my Linux computer,</li>
  <li>192.168.0.1 is the IP address of the router.</li>
</ul>

The WLAN MAC addresses (hardware address) might also be interesting:
<ul>
  <li>9c:b7:0d:f1:35:65 is the MAC address of my Windows 7 computer. You can get it with <code>ipconfig /all</code>. Look for "Wireless-LAN-Adapter" → "Physical Adress". (Does Windows have something like grep?)</li>
  <li>90:00:4e:25:ea:af is the MAC address of my Linux computer. You can get it with <code>ifconfig -a | grep HWaddr</code></li>
  <li>00:1b:11:8f:7c:90 is the MAC address of my router.</li>
</ul>

First of all, I would like to get to know how many packages were not sent by one of those three addresses. So I have to use the filter box, located at the top left:

[caption id="attachment_56411" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/02/wireshark-filter.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/wireshark-filter-300x104.png" alt="Filter packages with Wireshark" width="300" height="104" class="size-medium wp-image-56411" /></a> Filter packages with Wireshark[/caption]

Wireshark allows very simple, logical filtering. You can do comparisons with <code>==</code> or <code>!=</code> and you can connect expressions with <code>&&</code>.

Some interesting filtering options might be:
<ul>
  <li><code>ip.src</code> and <code>ip.dst</code>. Used like this: <code>ip.src==192.168.0.1</code></li>
  <li><code>bootp.option.type==53</code> to filter DHCP packages</li>
  <li><code>(ip.src==192.168.0.139 || ip.dst==192.168.0.139 || eth.src == 9c:b7:0d:f1:35:65 || eth.dst ==9c:b7:0d:f1:35:65)&& tcp</code> to get all TCP-packages that involved my windows computer.</li>
  <li><code>http.request</code>: All GET / POST requests</li>
  <li><code>tcp.analysis.retransmission</code>: Which packages were lost / had to be re-transmissioned?</li>
</ul>

<h2>Protocols</h2>
I've seen a lot of different protocols I have never heard of before:
<ul>
  <li><a href="http://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol">SSDP</a>: search for network printers</li>
  <li><a href="http://en.wikipedia.org/wiki/Address_Resolution_Protocol">ARP</a>: resolution of network layer addresses into link layer addresses</li>
  <li><a href="http://en.wikipedia.org/wiki/Link-local_Multicast_Name_Resolution">LLMNR</a>: name resolution for hosts on the same local link</li>
  <li><a href="http://wiki.wireshark.org/BrowserProtocol">browser</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Internet_Group_Management_Protocol">IGMP</a>: establish multicast group memberships</li>
  <li><a href="http://en.wikipedia.org/wiki/ICMPv6">ICMPv6</a>: error reporting, diagnostic functions, a framework for extensions to implement future changes</li>
  <li><a href="http://wiki.wireshark.org/NetBIOS/NBNS">NBNS</a>: like DNS,  translate human-readable names to IP addresses</li>
</ul>

<h2>Common Packages</h2>
<h3>TCP ACKed lost segment</h3>
<blockquote>The TCP ACKed lost segment means that Wireshark missed at least one packet in the other direction.</blockquote>
Source: <a href="http://ask.wireshark.org/questions/2425/tcp-acked-lost-segment/2426">ask.wireshark.org</a>