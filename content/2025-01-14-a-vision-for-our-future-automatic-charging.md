---
layout: post
title: A Vision for our Future: Automatic Charging
slug: a-vision-for-our-future-automatic-charging
lang: en
author: Martin Thoma
date: 2025-01-14 18:42
category: Cyberculture
tags: Energy, Traffic
featured_image: logos/energy.png
summary: The future is battery electric 🔋 🚙
medium_url: https://medium.com/@martinthoma/a-vision-for-our-future-automatic-charging-949f673a23f9
---
Imagine you’re driving to a supermarket. While you’re shopping, your car is automatically re-charging for an acceptable price. You don’t have to plug it in. You don’t have to compare prices. You don’t have to think about it. Welcome to the future.

## The Hardware

If we want this to work, there has to be some infrastructure. Cars and charging stations have to use compatible tech.

The charging cable has to be able to move on its own a little bit.

The charging port has to be able to open / indicate where it is to help the charging station to plug it in.

There are prototypes for this:

<iframe width="560" height="315" src="https://www.youtube.com/embed/uMM0lRfX6YI" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

Or a private project:

<iframe width="560" height="315" src="https://www.youtube.com/embed/octvXMaTG44" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

The key part here is how to find the charge port. That needs to be standardized. It would help to make it a law.

My suggestion would be this:

1. Add 3 LEDs around the charging port
1. Make the charging port itself have a very distinct color, e.g. the color of a green-screen.

## Software

Chargers need to “announce” which price they will use, ensure automatic payment works, how fast they can charge, how much they will charge. A protocol has to be defined.

## The Flow

1. **Parking**: You park in a parking spot that has an automatic charger with a car that supports this workflow.
1. **Car ↔ Charging station negotiations**: The car and the charging station negotiate the maximum charge, the price per kWh charged, the charging method. The car validates that it is one of the charging stations it may use — here we use cryptographic methods to verify the identity.
1. The charging station ensures that it can “see” the charging port.
1. The car is opening the charging port and flashing the charging port LEDs
1. The charger is confirming it has seen the LED flashes and approaching.
1. Once plugged in, car and charger confirm that they want to start. The car makes a 1-cent payment and the charger shows that there is electricity.
1. For every 0.5 kWh charged, both the car and the charger communicate. They continuously ensure that the car receives the charge. If it doesn’t, the charge stops. This prevents a man-in-the-middle attack.

## Security

* You don’t want anybody to be able to open your charging port. For this reason, the payment flow before is important.

## Alternatives

I initially thought it would be nice if this was hidden, e.g. that the charging works below the car. But then you would need to ensure that the car is parked correctly and you couldn’t see what is happening. Older cars could not use the same infrastructure.

A complete battery pack exchange would also be nice. If the battery pack and the opening mechanism was standardized, one could do this super fast. But many car manufacturers, battery manufacturers, and charging point operators would need to align. And it would be incompatible with existing cars. I don’t see that happening.

## See also

* Tesla API: [Official Fleet API](https://developer.tesla.com/docs/fleet-api) and the unofficial documentations [teslaapi.io](https://www.teslaapi.io/vehicles/commands) and [tesla-api.timdorr.com](https://tesla-api.timdorr.com/vehicle/commands/charging)
