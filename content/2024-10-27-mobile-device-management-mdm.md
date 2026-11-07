---
layout: post
title: Mobile Device Management (MDM)
slug: mobile-device-management-mdm
lang: en
author: Martin Thoma
date: 2024-10-27 10:42
category: Security
tags: Security, Devices
featured_image: logos/cybersecurity.png
summary: Managing laptops, tablets, and smartphones of a company remotely
medium_url: https://medium.com/@martinthoma/mobile-device-management-mdm-85681b249f01
status: draft
---
<figure class="ai-generated">
    <a href="../images/2024/10/mobile-device-management-mdm-1.jpg"><img src="../images/2024/10/mobile-device-management-mdm-1.jpg" alt="An MDM system administrates mobile devices like phones and laptops." width="800" height="800"></a>
    <figcaption>An MDM system administrates mobile devices like phones and laptops.</figcaption>
</figure>

Mobile devices are laptops, tablets, and smartphones. The issue with mobile devices is that they get lost if you have enough employees/devices. You also cannot easily physically access them when you need to upgrade software.

Mobile Device Management (MDM) systems allow you to do that:

* Install/upgrade/delete Software and configuration remotely
* Block a device or delete data remotely in case the device gets lost

## What to look for

First and easiest to check: Does the MDM solution **support all device types/operating systems you want to manage**? Android and iOS phones and tablets should likely be covered. Maybe you still have a Windows phone? Do you have Linux laptops that should also be covered? Anything more exotic?

Core actions you want to do might differ, but I’d say:

* Onboard/offboard devices
* Install / upgrade / delete software
* Sync data
* Lock or even wipe the device
* Have a dashboard with when a device was last connected and which software (maybe even data) it had at this point.

**User Experience (UX)**: How does the onboarding/offboarding process for a new device work? How easily can you find the relevant information/actions in the dashboards?

An MDM has administrative access to your devices. If the MDM has a security issue, all your devices at once have the issue. Just remember [the SolarWinds hack](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach). For this reason, you want to make sure that you can trust the security of the provider. An **ISO 27001 certification** can be a good start, but also look for news regarding hacks and how the company communication regarding them was. Security incidents happen, but you have to be able to trust that the company doesn’t lie to you about the issue.

## Solutions

* [**Microsoft Intune**](https://en.wikipedia.org/wiki/Microsoft_Intune) ([demo](https://www.youtube.com/watch?v=Dl9F9N0GZic)): Supports Android, iOS, Linux, macOS, and Windows. Intune is under the [Microsoft ISO 27001 certification](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001).
* [**MobileIron**](https://en.wikipedia.org/wiki/MobileIron) by Ivanti ([demo](https://www.youtube.com/watch?v=DaSudBbLyFg)): Supports Active directory as identity provider. I could NOT find an ISO 27001 certification.
* [**NinjaOne**](https://www.ninjaone.com/) ([demo](https://www.youtube.com/watch?v=iVzDue5fzAk)): Is [ISO27001 certified](https://www.ninjaone.com/blog/ninjaone-is-iso27001-compliant/)

<!-- series: appsec -->
