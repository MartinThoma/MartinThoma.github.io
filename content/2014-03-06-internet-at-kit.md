---
layout: post
title: Internet at KIT
author: Martin Thoma
date: 2014-03-06 11:35
category: Cyberculture
tags: Internet, WLAN, KIT, VPN, JNC
featured_image: 2011/10/KIT-Logo.png
---
This article is about how to get internet at KIT with Linux.
It was tested on Linux Mint 16 MATE which is based on Ubuntu which is based on
Debian.

## WLAN
At KIT are a lot of WLANs, but only two are important: `wkit-802.1x` and `eduroam`.

* Mode: Infrastructure
* Security: WPA & WPA2 Enterprise
* Authentificaiton: Protected EAP (PEAP)
* Anonymous identity: anonymous@kit.edu
* CA certificate: deutsche-telekom-root-ca-2.crt ([source](http://www.scc.kit.edu/downloads/ism/dtag-root-ca-2.cer))
* PEAP version: Automatic
* Inner authentification: MSCHAPv2
* Username:
  * for `wkit-802.1x`: uabcd (Your username. It begins with 'u' and has 5 letters)
  * for `eduroam`: uabcd@student.kit.edu
* Password: (Your password)
* IPv4 Settings: Automatic (DHCP)
* IPv6 Settings: Ignore

## VPN
I use Juniper VPN.

The following lines install some prerequesites, download Juniper from [this page](http://www.scc.kit.edu/dienste/7868.php), unpack it and execute the shell script.

```bash
sudo apt-get install libc6-i386 lib32z1 lib32nss-mdns
wget http://www.scc.kit.edu/scc/sw/juniper/7.4R8/linux_vpn_7.4R8.tar.gz
tar -xzvf linux_vpn_7.4R8.tar.gz
cd juniper_linux
./vpn-install.sh
```

After you have done this, you can use juniper with

```bash
jnc -n kit
```

The `-n` flag disables GUI. It will show this:

```bash
Server certificate verified and CN is vpn.kit.edu. Saving in /home/moose/.juniper_networks/network_connect/config/vpn.kit.edu.der.
Password:
Connecting to vpn.kit.edu : 443.
Waiting for ncsvc for 3 seconds... done
ncsvc is running, but tunnel is not established yet. Waiting for 3 seconds... done
ncsvc is running, but tunnel is not established yet. Waiting for 3 seconds... done.
ncsvc is running in background (PID: 11180):
tunnel interface tun0, addr: 141.3.192.60
```

You can stop it with `jnc stop`.

## Resources
* [Zertifizierung (KIT-CA)](http://www.scc.kit.edu/dienste/kit-ca.php)
* [Juniper VPN unter Linux](http://www.scc.kit.edu/dienste/7868.php)
