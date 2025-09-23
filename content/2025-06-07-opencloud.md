---
layout: post
title: Self-Hosted Cloud Solutions
slug: self-hosted-cloud-solutions
author: Martin Thoma
date: 2025-06-07 20:00
category: My bits and bytes
tags: digital sovereignty, self-hosted, cloud, ownCloud, NextCloud, OpenCloud
featured_image: logos/earth.png
status: draft
---

## Features

* File Administration: Google Drive / Dropbox
    * Full text search
* Calendar
* Contacts
* Notes
* Office:
    * OnlyOffice / Collabora
    * Spellchecker
* Email:
    * IMAP client, e.g. for Mailbox / Posteo
* Backups

## ownCloud Infinite Scale

[ownCloud](https://en.wikipedia.org/wiki/OwnCloud) is a free and open-source
software platform for file synchronization and sharing. It allows users to store
files on a private server and access them from various devices, providing a
secure alternative to public cloud services.

* License: AGPL-3.0-or-later
* History:
    * Founded in 2010 by Frank Karlitschek
    * Developed by ownCloud GmbH and the open-source community
    * Major rewrite in 2020 to create ownCloud Infinite Scale
* Software Stack:
    * Backend: Go
    * Frontend: React
    * DB: PostgreSQL

## NextCloud

[Nextcloud](https://en.wikipedia.org/wiki/Nextcloud) is a free and open-source software suite for file hosting, similar to ownCloud. It is designed to provide a secure and private cloud storage solution, allowing users to store and share files, calendars, contacts, and more.

* License: AGPL-3.0-only
* History:
    * Forked from ownCloud in 2016
    * Developed by the Nextcloud GmbH and the Nextcloud community
* Software Stack:
    * Backend: PHP running on Apache or Nginx
    * Frontend: JavaScript with  Vue.js
    * DB: MySQL/MariaDB/PostgreSQL/SQLite
* Security:
    * TOTP (two-factor authentication)

## OpenCloud

[OpenCloud](https://github.com/opencloud-eu/opencloud/tree/main) is a free and open-source software platform
for cloud computing, designed to provide a secure and scalable infrastructure
for hosting applications and services. It aims to offer a flexible and
customizable cloud environment, allowing users to deploy and manage their own
cloud solutions.

* License: Apache-2.0
