---
layout: post
title: Homeserver
slug: homeserver
lang: en
author: Martin Thoma
date: 2025-06-10 20:00
category: My bits and bytes
tags: digital sovereignty, self-hosted, cloud
featured_image: logos/earth.png
status: draft
---
## Hardware

I use a Mini PC with the following specifications:

* **CPU**: [Specific model to be added]
* **RAM**: 16 GB
* **Storage**: [Capacity and type to be added]
* **Network**:
    * Gigabit Ethernet
    * Wake on LAN (WoL) support
    * Wi-Fi 6 or better

Most thin clients or mini PCs would work well for this purpose.

**Note**: A Raspberry Pi was too slow for my needs.

## Operating System

I run Ubuntu MATE on my homeserver.

## Software

### Currently Running

Services I currently run on my homeserver:

* **SSH / vim**: Remote access and administration
* **[Pi-hole](https://pi-hole.net/)**: Network-wide ad blocking
* **[Home Assistant](https://www.home-assistant.io/)** (Docker): Home automation platform
* **DuckDNS.org**: Dynamic DNS service for external access to my homeserver

### Ideas for Future Implementation

* **Operating System**: Unraid
* **Media Management**: [immich](https://immich.app/) - Image and video management
* **Knowledge Base**: [Kiwix](https://kiwix.org/en/applications/) - Offline Wikipedia
* **Password Management**: [vaultwarden](https://vaultwarden.com/) - Bitwarden-compatible server
* **Network**: OpnSense - Firewall and router
* **Calendar/Contacts**: Baikal server
* **File Storage**: ownCloud / NextCloud / [Seafile](https://www.seafile.com/en/home/) with SAMBA
* **Media Server**: Jellyfin / Emby / Plex
* **VPN**: WireGuard / OpenVPN
* **DNS Server**: Unbound
* **Reverse Proxy**: Nginx / Traefik
* **Monitoring**: Prometheus / Grafana
* **Backup**: Borg / Restic
* **Containerization**: Docker / Podman
* **Virtualization**: Proxmox / KVM

## Configuration

### Automatic Updates

Install and configure `unattended-upgrades`:

```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```


### SSH Hardening

```bash
# Allow SSH access via public key authentication:
ssh-copy-id username@your-server-ip

# Disable password authentication for improved security:
sudo vim /etc/ssh/sshd_config
# Set the following options:
#    PasswordAuthentication no
#    PubkeyAuthentication yes
sudo systemctl reload sshd
```
