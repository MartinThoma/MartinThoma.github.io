---
layout: post
lang: en
title: Homeserver
slug: homeserver
author: Martin Thoma
date: 2025-06-10 20:00
category: My bits and bytes
tags: digital sovereignty, self-hosted, cloud
featured_image: logos/earth.png
status: draft
---
## Hardware

I have a Mini PC:

* CPU: ...
* RAM: 16 GB
* Storage: ...
* Network: Gigabit Ethernet
    * Wake on LAN (WoL) support
    * Wi-Fi 6 or better

Probably any ThinClient or mini PC would do.

Raspberry Pi was too slow for me

## OS

I run mine on Ubuntu Mate

## Software

What I run on my homeserver:

* SSH / vim: Remote access
* [Pi-hole](https://pi-hole.net/): Network-wide ad blocking
* [Home Assistant](https://www.home-assistant.io/) on Docker: Home Automation
* DuckDNS.org: Dynamic DNS service so that I can access my homeserver from outside my home network

Ideas:

* Unraid
* [immich](https://immich.app/): Image and Video Management
* [Kiwix](https://kiwix.org/en/applications/): Offline Wikipedia
* [vaultwarden](https://vaultwarden.com/): Password Management
* OpenSense: Firewall and Router
* Baikal: Calendar and Contacts
* Storage / File Server: ownCloud / NextCloud / Seafile
    * https://www.seafile.com/en/home/
    * with SAMBA?
* Media Server: Jellyfin / Emby / Plex
* VPN: WireGuard / OpenVPN
* DNS Server: Unbound
* Reverse Proxy: Nginx / Traefik
* Monitoring: Prometheus / Grafana
* Backup: Borg / Restic
* Containerization: Docker / Podman
* Virtualization: Proxmox / KVM

## Configuration

### Automatic Updates

Install and configure `unattended-upgrades`:

```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```


### SSH Hardening

```
# Allow SSH access via public key authentication:
ssh-copy-id username@your-server-ip

# Disallow password authentication:
sudo vim /etc/ssh/sshd_config
# Set:
#    PasswordAuthentication no
#    PubkeyAuthentication yes
sudo systemctl reload sshd
```
