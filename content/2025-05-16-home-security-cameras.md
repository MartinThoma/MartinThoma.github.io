---
layout: post
title: Home Security Cameras 2025
slug: home-security-cameras-2025
author: Martin Thoma
date: 2025-05-11 20:00
category: My bits and bytes
tags: cameras, review, Smart Home, Home Assistant
featured_image: logos/money.png
---
When I'm not at home, I still want to know if anything is happening. Especially
when a person is in an unexpected place, but also e.g. when somebody is at the
door.

In this article, I will compare different home security cameras systems.

## General Notes

I am in Germany so the prices and availability are for Germany.

What I want:

* At least one option for an **indoor camera** (cable-powered) and one for an
  **outdoor camera** (battery-powered, with solar panel and IP65-rating or
  better, the power should be USB-C that can also be used for charging the
  battery directly)
* I hate subscription models. I just want to buy the stuff and own it.
* It should have a decent **Home Assistant integration** as well as a reasonable app
* The camera should have a **local storage** option (microSD card or similar)
* A **smart hub** that works without internet and syncs with the cameras is a plus

I excluded those vendors:

* [Blink](https://en.wikipedia.org/wiki/Blink_Home) (Amazon, basic option) [needs a
  subscription for motion
  detection](https://support.blinkforhome.com/en_GB/subscriptions-faq/subscription-faq),
  so that's a no-go for me.
* For [Ring](https://en.wikipedia.org/wiki/Ring_(company)) (Amazon, premium otipn), it was
  rather hard to find what you can/cannot do without a subscription. There seems
  to be "Ring Edge" to allow you to store the recordings locally.
* [Google Nest](https://de.wikipedia.org/wiki/Google_Nest) offers just a few cameras. They seem to be
  [overpriced](https://www.amazon.de/Google-Indoor-Kabel-%C3%9Cberwachungskamera-Hause/dp/B09TN65LQF/)
  (74€ for one indoor camera) and it's unclear how much you can do [without a
  subscription](https://www.reddit.com/r/Nest/comments/ry8t7i/are_nest_cameras_worthless_without_nest_aware/).


### Offline Access

In the following table, "local" means your phone is connected to the same WiFi
network as the camera. "Remote" means your phone is connected to the Internet
but not to the same WiFi network as the camera.

Accessing the camera means to see its setting.

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Feature</th>
      <th>Camera has no WiFi</th>
      <th>Camera has WiFi, but no Internet</th>
      <th>Camera has WiFi with Internet</th>
      <th>Note</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Local Access via app</td>
      <td>❌</td>
      <td>✅</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Local Live-view</td>
      <td>❌</td>
      <td>✅</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Local Playback</td>
      <td>❌</td>
      <td>✅</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Remote Access via app</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Remote Live-view</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅</td>
      <td>&nbsp;</td>
    <tr>
      <td>Remote Playback</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
    </tr>
    <tr>
      <td>Record to SD card</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Audio Alarm</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Push Notification</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅</td>
      <td></td>
    </tr>
    <tr>
      <td>Email Alert</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Auto Upgrade</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>

## IP-Ratings

IP ratings are a measure of how well a device is protected against dust and water.
The first digit indicates the level of protection against solid objects, while the
second digit indicates the level of protection against liquids.

The letter "X" can be used in place of a digit to indicate that the device has
not been tested for that specific type of protection.

<table>
    <thead>
    <tr>
        <th>Digit</th>
        <th>Protection against solid objects</th>
        <th>Protection against liquids</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>0</td>
        <td>No protection</td>
        <td>No protection</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Protected against solid objects larger than 50 mm (e.g., hands)</td>
        <td>Protected against vertically falling water drops</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Protected against solid objects larger than 12.5 mm (e.g., fingers)</td>
        <td>Protected against vertically falling water drops with enclosur tilted up to 15°</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Protected against solid objects larger than 2.5 mm (e.g., screwdriver)</td>
        <td>Protected against water spray at an angle of up to 60°</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Protected against solid objects larger than 1 mm (e.g., wires)</td>
        <td>Protected against water splashes from any direction</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Dust-protected (limited ingress of dust) for 2-8 hours</td>
        <td>Protected against water jets from any direction</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Dust-tight (no ingress of dust) for 2-8 hours</td>
        <td>Protected against powerful water jets</td>
    </tr>
    <tr>
        <td>7</td>
        <td>&nbsp;</td>
        <td>Protected against immersion in water up to 1 meter for 30 minutes</td>
    </tr>
    <tr>
        <td>8</td>
        <td>&nbsp;</td>
        <td>Protected against immersion in water beyond 1 meter (depth and duration specified by the manufacturer)</td>
    </tr>
    </tbody></table>


## Tapo Link

* Android App: [TP-Link Tapo](https://play.google.com/store/apps/details?id=com.tplink.iot&hl=en) (4.6 stars, 362K reviews)
* iOS App: [TP-Link Tapo](https://apps.apple.com/us/app/tp-link-tapo/id1472718009) (4.8 stars, 9.4K reviews)
* [Home Assistant Integration](https://www.home-assistant.io/integrations/tplink/) ([YouTube](https://www.youtube.com/watch?v=Op-5fnLLaM4))
* Local storage: ✅ (microSD card)
* Cloud storage: ✅ (free for 30 days, then $2.99/month)
* Local access: ✅
* Remote access: ✅

Models:

* All of them have a MicroSD slot for up to 512 GB
* All of them have two-way audio with noise suppression
* All of them have 	Google Assistant / Amazon Alexa integrations
* Model Names:
    * The 2XX-series are indoor cameras
    * The 3XX-series are outdoor cameras
    * The 4XX-series are battery-powered outdoor cameras
    * [Tapo D235](https://de.store.tapo.com/products/tapo-d235-2k-5mp-akku-festverdrahtet): A doorbell for [100€](https://www.amazon.de/Tapo-D235-Video-T%C3%BCrklingel-Festverdrahtet-ultrabreiten/dp/B0DDL95M8Z/)

<table>
    <thead>
    <tr>
        <th>Model</th>
        <th>Video</th>
        <th>IP-Specs</th>
        <th>Battery</th>
        <th>FOV (diagonal/horizontal/vertical)</th>
        <th>Movable (horizontal / vertical)</th>
        <th>Spotlight / Siren</th>
        <th>Price</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><a href="https://de.store.tapo.com/products/tapo-c200-1080p-360">Tapo C200</a></td>
        <td>2 MP (1920x1080)</td>
        <td>-</td>
        <td>❌</td>
        <td>88° / 75° / 41°</td>
        <td>360° / 114°</td>
        <td>❌ / ❌</td>
        <td><a href="https://www.amazon.de/Tapo-C200-%C3%9Cberwachungskamera-Linsenschwenkung-1080p-Aufl%C3%B6sung/dp/B07XLML2YS/">26€</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/products/tapo-c210-2k-3mp">Tapo C210</a></td>
        <td>3 MP (2304x1296)</td>
        <td>-</td>
        <td>❌</td>
        <td>88° / 75° / 41°</td>
        <td>360° / 114°</td>
        <td>❌ / ❌</td>
        <td><a href="https://www.amazon.de/TP-Link-Tapo-%C3%9Cberwachungskamera-Linsenschwenkung-3MP-Aufl%C3%B6sung/dp/B095CLQ1PT/">26€</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c220?srsltid=AfmBOoqUPxbVgnWVWkPtDshYVJsCgv0w4MTBcTOVVpDaW4JmxGS3sipQ">Tapo C220</a></td>
        <td>3 MP (2304x1296) / 30fps</td>
        <td>-</td>
        <td>❌</td>
        <td>88° / 75° / 41°</td>
        <td>360° / 114°</td>
        <td>❌ / 99dB</td>
        <td><a href="https://www.amazon.de/TP-Link-Tapo-%C3%9Cberwachungskamera-Linsenschwenkung-3MP-Aufl%C3%B6sung/dp/B095CLQ1PT/">26€</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c225?srsltid=AfmBOoqvWAP6oM94UhL60asZXo334hgsX5I2DCxi21VMdonIuP4uejXK">Tapo C225</a></td>
        <td>4 MP (2688×1520) / 30fps</td>
        <td>-</td>
        <td>❌</td>
        <td>100° / 83° / 43° </td>
        <td>360° / 149°</td>
        <td>✅ / 98dB</td>
        <td><a href="https://www.amazon.de/Tapo-360%C2%B0-WLAN-%C3%9Cberwachungskamera-Privatsph%C3%A4renmodus-Starlight-Sensor-Benachrichtigung/dp/B0BN4BQ1DM/">50€</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c310?srsltid=AfmBOoocD2vN10v62EHWVytHAsaRx723GQdN8kpFnfjBWpoMmTUCpFgQ">Tapo C310</a></td>
        <td>3 MP (2304×1296) / 15fps</td>
        <td>IP66</td>
        <td>❌</td>
        <td>100° / 84° / 46°</td>
        <td>❌</td>
        <td>✅ / 91dB</td>
        <td><a href="https://www.amazon.de/Tapo-C310-%C3%9Cberwachungskamera-Hochaufl%C3%B6sung-Bewegungserkennung/dp/B08JLR2751/">34€</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c310?srsltid=AfmBOopHJinMOcVO8TiJ9NBdoNFzKjAIuO9HIcel2gRGzPEVRdlOYfIC">Tapo C310</a></td>
        <td>3 MP (2304x1296)</td>
        <td>IP66</td>
        <td>❌</td>
        <td>100° / 84° / 46°</td>
        <td>❌</td>
        <td>✅ / 91 dB</td>
        <td><a href="https://www.amazon.de/Tapo-C310-%C3%9Cberwachungskamera-Hochaufl%C3%B6sung-Bewegungserkennung/dp/B08JLR2751/">34€</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c320ws?srsltid=AfmBOopw8fpjz_6LoE2smAEMPjPALNfrmzM3ltvf_7qOObRdbAJ3sRDU">Tapo C320WS</a></td>
        <td>3.7 MP (2560×1440) / 15fps</td>
        <td>IP66</td>
        <td>❌</td>
        <td>113° / 97° / 54°</td>
        <td>❌</td>
        <td>✅ / 91 dB</td>
        <td><a href="https://www.amazon.de/TP-Link-Tapo-%C3%9Cberwachungskamera-Vollfarb-Nachtsicht-Bewegungserkennung/dp/B098TVZ6TS/">37€</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c325wb">Tapo C325WB</a></td>
        <td>4 MP (2688 × 1520)</td>
        <td>IP66</td>
        <td>❌</td>
        <td>131° / 106° / 56°</td>
        <td>❌</td>
        <td>✅ / 97 dB</td>
        <td><a href="https://www.amazon.de/Tapo-C325WB-%C3%9Cberwachungskamera-Hochaufl%C3%B6sung-Bewegungserkennung/dp/B0C8NYMBRR/">67€</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c410">Tapo C410</a></td>
        <td>3 MP (2304 × 1296) / 15fps</td>
        <td>IP65</td>
        <td>6400 mAh (integrated)</td>
        <td>125° / 111° / 56°</td>
        <td>❌</td>
        <td>2 LEDs / 94 dB</td>
        <td><a href="https://www.amazon.de/Tapo-C410-%C3%9Cberwachungskamera-MicroSD-Speicher-Personenerkennung/dp/B0D544WSFP/ref=sr_1_6?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1CM6NGUAF0E0B&dib=eyJ2IjoiMSJ9.92RDIcKzGqC8ARx51PwPxRkfmfdYkBqap-YjjaeKCZaqGIjkPc4r1v7OLXUnARS0EzVbQREOuOOkObLVW2ulKUPp54Sqez9mcQBnE-tS-IkTWT68-dDXaXJxxixLWLZSxAPptGHzpxbhegFZyMhvxIk47TkdJa2xk6wA6aRyJqmLR_ywhvwZfgDCynd7aWNpUxc9r7TQTlGCOzdOx-RF_mA22mAaU5Zr0HARafv3WKZIlDKpq7B6mMJhFbJ7vZM3e1jVk6jgaZ5xVDMzrBf27PNQ-IEjLOjy90L3czJMWZ0.apSRDGfHk7wdwB0u_2oIkzemETc7tNGaNyvOgwunuRo&dib_tag=se&keywords=Tapo%2BC410&qid=1747386373&sprefix=tapo%2Bc410%2Caps%2C272&sr=8-6&th=1">65€</a> (Solar Kit)</td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c420s2?srsltid=AfmBOoq3QCHJHks5KZGZkMFYKmCwN48rqmJ0-aegi1LQwgM4Li_ZcId4">Tapo C420</a></td>
        <td>4 MP (2560 &times; 1440)</td>
        <td>IP65</td>
        <td>6700 mAh (removable)</td>
        <td>113° / 97° / 54°</td>
        <td>❌</td>
        <td>2 LEDs / 92 dB</td>
        <td><a href="https://www.amazon.de/TP-Link-Tapo-%C3%9Cberwachungskamera-Aussen-Ersatzakku/dp/B0CSML4GBR/">105€</a> with battery and hub</td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c425">Tapo C425</a></td>
        <td>4 MP (2560 &times; 1440) / 30fps</td>
        <td>IP66</td>
        <td>10000 mAh (300 days, integrated)</td>
        <td>150° / 134° / 77°</td>
        <td>❌</td>
        <td>4 LEDs / 94 dB</td>
        <td><a href="https://www.amazon.de/Tapo-C425-%C3%9Cberwachungskamera-MicroSD-Speicher-Super-Weitwinkel/dp/B0D546B4LL/">90 &euro;</a></td>
    </tr>
    <tr>
        <td><a href="https://de.store.tapo.com/blogs/haufig-gestellte-fragen/spezifikationen-von-tapo-c520ws">Tapo C520WS</a></td>
        <td>4 MP (2560 × 1440) / 30fps</td>
        <td>IP66</td>
        <td>❌</td>
        <td>112° / 95° / 53°</td>
        <td>340° / 60°</td>
        <td>2 LEDs / 93 dB</td>
        <td><a href="https://www.amazon.de/TP-Link-Tapo-C520WS-%C3%9Cberwachungskamera-leistungsstarke/dp/B0CCW8GHT8/">54 &euro;</a></td>
    </tr>
</table>

## Reolink

* [Android App](https://play.google.com/store/apps/details?id=com.mcu.reolink&hl=en) has only 3.4 stars with 35.2K reviews
* [Home Assistant Integration](https://www.home-assistant.io/integrations/reolink/)
* Google Assistant
* Aparently its possible to load the videos via FTP on a NAS.


Of course, all of the security camera models have 2-way audio:

<table>
    <thead>
    <tr>
        <th>Model</th>
        <th>Video</th>
        <th>IP-Specs</th>
        <th>Battery</th>
        <th>FOV (diagonal/horizontal/vertical)</th>
        <th>Movable (horizontal / vertical)</th>
        <th>Spotlight / Siren</th>
        <th>Price</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><a href="https://reolink.com/product/argus-4-pro/">Reolink Argus 4 Pro</a></td>
        <td>8 MP (5120x1440) @ 15fps</td>
        <td>IP66</td>
        <td>5000mAh ()</td>
        <td>? / 180° / 50°</td>
        <td>❌</td>
        <td>yes / yes</td>
        <td><a href="https://www.amazon.de/Reolink-Argus-Solar-%C3%9Cberwachungskamera-ColorX-Nachtsicht/dp/B0D1BNPRR6/">160€</a> incl. 6W Solar Panel</td>
    </tr>
    <tr>
        <td><a href="https://reolink.com/product/altas-pt-ultra/#specifications">Reolink Atlast PT Ultra</a></td>
        <td>8 MP (3840x2160) @ 15fps</td>
        <td>IP65</td>
        <td>20.000mAh ()</td>
        <td>110° / 90° / 50°</td>
        <td>Pan: 355°, Tilt: 90°</td>
        <td>yes / yes</td>
        <td><a href="https://www.amazon.de/Reolink-Altas-Ultra-Solar-%C3%9Cberwachungskamera/dp/B0D948YBFH/">200€</a> incl. 6W Solar Panel</td>
    </tr>
    <tr>
        <td><a href="https://reolink.com/product/argus-pt-lite/">Reolink Atlast PT Light</a></td>
        <td>3 MP (2304 x 1296) @ 15fps</td>
        <td>IP64</td>
        <td>17.2Wh ()</td>
        <td>110° / 90° / 47°</td>
        <td>Pan: 355°, Tilt: 140°</td>
        <td>yes / yes</td>
        <td><a href="https://www.amazon.de/Reolink-%C3%9Cberwachungskamera-Neigefunktion-Bewegungsmelder-2-Wege-Audio/dp/B07WTVYWGF/">80€</a> incl. 6W Solar Panel</td>
    </tr>
</tbody>
</table>


## Eufy (by Anker)

[Eufy](https://en.wikipedia.org/wiki/Anker_Innovations) is a brand of Anker
Innovations, which is a Chinese company.

All Eufy cams seem to have:

* two-way audio
* Integrations into: Apple HomeKit, Google Assistant und Amazon Alexa
* SD-card up to 128GB

Eufy has the [HomeBase S380](https://www.eufy.com/eu-en/products/t80303d1?variant=42451449413784)
(180€, up to 16 devices with up to 34 sensors) for battery-powered cameras.

Here are the Eufy models I found:

<table>
    <thead>
    <tr>
        <th>Model</th>
        <th>Video</th>
        <th>IP-Specs</th>
        <th>Battery</th>
        <th>FOV (diagonal/horizontal/vertical)</th>
        <th>Movable (horizontal / vertical)</th>
        <th>Spotlight / Siren</th>
        <th>Price</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><a href="https://www.eufy.com/products/t84001w1?variant=37765865832634">eufy Cam C120</a></td>
        <td>2 MP (2048 x 1080)</td>
        <td>IP54</td>
        <td>❌</td>
        <td>? / 125° / 57°</td>
        <td>❌</td>
        <td>❌ / ❌</td>
        <td><a href="https://www.amazon.de/eufy-%C3%9Cberwachungskamera-Personenerkennung-Sprachassistent-Bewegungssensor/dp/B086LBWH4M/">40€</a></td>
    </tr>
    <tr>
        <td><a href="https://www.eufy.com/eu-de/products/t8410?variant=32243192332390">eufy Indoor Cam E220</a></td>
        <td>2 MP (2048 x 1080)</td>
        <td>-</td>
        <td>❌</td>
        <td>? / 125° / ?</td>
        <td>360° / 96°</td>
        <td>❌ / ❌</td>
        <td><a href="https://www.amazon.de/dp/B086LBCQJL">32€</a></td>
    </tr>
    <tr>
    <td><a href="https://www.eufy.com/products/t8441z21?variant=39787379753146">eufy Outdoor Cam E220</a></td>
        <td>2 MP (2048 x 1080)</td>
        <td>IP67</td>
        <td>❌</td>
        <td>? / 108° / 57°</td>
        <td>❌</td>
        <td>❌ / ❌</td>
        <td><a href="https://www.amazon.de/eufy-eigenst%C3%A4ndige-%C3%9Cberwachungskamera-Au%C3%9Fenbereiche-Geb%C3%BChrenfreie/dp/B08ZSCBBLV/">60€</a>
    </td>
    </tr>
    <tr>
    <td>eufyCam 2c</td>
        <td>2 MP (1920 x 1080)</td>
        <td>IP67</td>
        <td>? (for 180 days)</td>
        <td>? / 120° / 60°</td>
        <td>❌</td>
        <td>✅ / ❌</td>
        <td><a href="https://www.amazon.de/eufy-kabelloses-%C3%9Cberwachungskamera-zus%C3%A4tzliche-Akkulaufzeit/dp/B07XCC3GDX/">70€</a></td>
    </tr>
    <tr>
        <td><a href="https://www.eufy.com/eu-de/products/t8134321?variant=40143356592230">eufy Outdoor S220 SoloCam</a></td>
        <td>2 MP (2048 x 1080)</td>
        <td>IP67</td>
        <td>6500mAh</td>
        <td>? / ?° / ?</td>
        <td>❌</td>
        <td>? / 75dB</td>
        <td><a href="https://www.amazon.de/eufy-Security-%C3%BCberwachungskamera-monatliche-General%C3%BCberholt/dp/B0CD747V33">90€</a></td>
    </tr>
    </tbody>
</table>

I couldn't find any specs for the different Eufy cameras. Additionally, the model
names are a mess. No thanks.

## Wyze

I found exactly two cameras on Amazon: The Wyze Cam v4
and the Wyze Cam Pan v3. No camera that can rotate. No battery-powered
camera (and none with a solar panel).

<table>
    <thead>
    <tr>
        <th>Model</th>
        <th>Video</th>
        <th>IP-Specs</th>
        <th>Battery</th>
        <th>FOV (diagonal/horizontal/vertical)</th>
        <th>Movable (horizontal / vertical)</th>
        <th>Spotlight / Siren</th>
        <th>Price</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><a href="https://support.wyze.com/hc/en-us/articles/23746258989851-Wyze-Cam-v4-Tech-Specs">Wyze Cam v4</a></td>
        <td>2560 x 1440</td>
        <td>IP65</td>
        <td>❌</td>
        <td>116° / 99° / 53°</td>
        <td>❌</td>
        <td>❌ / ❌</td>
        <td><a href="https://www.amazon.de/KMOUANTS-Wyze-Cam-Kamera-%C3%9Cberwachungshalterung-Schutzgeh%C3%A4use/dp/B0D54B9NN7/">22€</a></td>
    </tr>
</tbody>
</table>

## Arlo (by Netgear)

There are several Arlo SmartHubs and Arlo Base Stations. They have a microSD
slot for local storage, some have an integrated siren, some have USB Type-A for
extendable storage. No integrated battery in case of power failure. No
specification on how many devices can be connected.


The Arlo security cams also have 2-way Audio.

Models:

<table>
    <thead>
    <tr>
        <th>Model</th>
        <th>Video</th>
        <th>IP-Specs</th>
        <th>Battery</th>
        <th>FOV (diagonal/horizontal/vertical)</th>
        <th>Movable (horizontal / vertical)</th>
        <th>Spotlight / Siren</th>
        <th>Price</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><a href="https://www.arlo.com/en-au/cameras/pro/arlo-pro-5.html">Arlo Pro 5</a></td>
        <td>2K+ HDR</td>
        <td>?</td>
        <td> 8 months (? mAh)</td>
        <td>?° / 160° / ?°</td>
        <td>❌</td>
        <td>yes / yes</td>
        <td><a href="https://www.amazon.de/Arlo-%C3%9Cberwachungskamera-Verbesserte-Farbnachtsicht-Testzeitraum/dp/B0D6GTBMV9/">140€</a></td>
    </tr>
    <tr>
        <td><a href="https://www.arlo.com/en-us/cameras/ultra/arlo-ultra-2.html">Arlo Ultra 2</a></td>
        <td>4K HDR</td>
        <td>IP65</td>
        <td>6 months (? mAh, removable)</td>
        <td>?° / 180° / ?°</td>
        <td>❌</td>
        <td>yes / yes</td>
        <td><a href="https://www.amazon.de/Arlo-%C3%9Cberwachungskamera-Bewegungsmelder-2-Wege-Audio-180%C2%B0-Blickwinkel/dp/B08WX76RWH/">190€</a></td>
    </tr>
</tbody>
</table>

## Others

* SimpliSafe and Vivint seem not to be on Amazon
