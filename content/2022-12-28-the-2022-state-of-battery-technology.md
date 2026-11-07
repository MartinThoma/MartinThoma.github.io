---
layout: post
title: The 2022 State of Battery Technology
slug: the-2022-state-of-battery-technology
lang: en
author: Martin Thoma
date: 2022-12-28 00:36
category: Cyberculture
tags: Energy, Technology
featured_image: logos/energy.png
summary: Price, cycles, energy density, charging speed, and resources of current battery types
medium_url: https://medium.com/@martinthoma/the-2022-state-of-battery-technology-43f8cb8ece03
---
Batteries are extremely important. They are built into millions of devices, especially smartphones, cars, and homes. You need to have different properties depending on which application you’re talking about. For example, smartphones need a very high energy density. In contrast, the batteries used to store energy from solar cells can be huge and heavy. For those, the cost per kWh stored is more important.

Let’s explore at which point we are in December 2022.

## The comparison categories

* **Price in EUR/kWh**: How much do you have to pay per kWh stored?
* **Lifespan in cycles**: How many charge/discharge cycles does the battery support until it gets below 80% of its original maximum capacity?
* **Gravimetric energy density in Wh/kg**: How heavy is the battery?
* **Volumetric energy density in Wh/L**: How big is the battery?
* **Resources**: What do you need to build the battery? Are there any resources which are primarily available in one country? Are there resources necessary that are typically mined from countries without good labour protection laws? Is mining / producing the battery causing environmental issues?
* **Efficiency**: How much charge is lost? The charge/discharge efficiency as well as the self-discharge rate are of interest.
* **Damage resistance**: What happens if the battery is punctured? What happens if there is heat?
* **Temperature resistance**: In which temperature range does the battery operate normally? Typically colder temperatures cause a loss of charge.

Let’s compare!

## The contenders

There are tons of different battery technologies in the wild. Even more in the research and development. In this article, I’ll focus on the most widespread ones as well as some that might become interesting in future.

The batteries differ in the type of material used for the anode and the cathode.

* [**Nickel-Manganese-Cobalt**](https://en.wikipedia.org/wiki/Lithium-ion_battery) **(Li-NMC333)**: It’s a type of Lithium Ion battery. LiNiMnCoO2 would be more accurate. It’s roughly 33% Nickel, 33% Manganese, and 33% Cobalt. This is the most used battery type worldwide.
* **Nickel-Manganese-Cobalt (Li-NMC811)**: It is one type of Li-NMC battery, but with 80% Nickel, 10% Manganese, 10% Cobalt.
* **Nickel-Manganese (Li-NMX)**: It’s 75% Nickel and 25% Manganese — and nothing extra! Expected in European markets in 2023. Removing the Cobalt makes it cheaper to produce.
* [**Sodium-Ion**](https://en.wikipedia.org/wiki/Sodium-ion_battery) **(Na+)**: CATL plans mass production in 2023 ([source](https://www.caixinglobal.com/2022-10-25/catl-aims-to-mass-produce-sodium-ion-batteries-in-2023-101955814.html)).
* [**Lithium Iron Phosphate**](https://en.wikipedia.org/wiki/Lithium_iron_phosphate_battery) **(LFP)**: More accurate is LiFePO4. Typically used for photovoltaics.
* [**Lithium Titanate**](https://en.wikipedia.org/wiki/Lithium-titanate_battery) **(LTO)**: More accurate is Li4Ti5O12. It’s used in the Samsung S-Pen, in certain Japanese-only versions of [Mitsubishi’s i-MiEV](https://en.wikipedia.org/wiki/Mitsubishi_i-MiEV), and mobile medical devices. They are fast to charge, but their energy density is low.
* **Nano Lithium Titanate (Nano LTO)**: Like LTO, but they worked on the structure of the electrode. This brings some crazy performance gains.

Honorable Mentions:

* [Li-S](https://en.wikipedia.org/wiki/Lithium%E2%80%93sulfur_battery): Very high energy density, but not commercially available.
* [Magnesium sulfur battery](https://en.wikipedia.org/wiki/Magnesium_sulfur_battery) (MgS): Extremely high theoretical energy density!
* [Lithium polymer battery](https://en.wikipedia.org/wiki/Lithium_polymer_battery) (LiPo): High energy density
* [Lead-Acid battery](https://en.wikipedia.org/wiki/Lead%E2%80%93acid_battery): Commonly found in cars. The self-discharge is high, the energy density low, the materials toxic, the number of cycles is low, the temperature range just -20°C to +60°C. And the price is higher than for Sodium-Ion. This sounds as if sodium ion could replace lead-acid batteries.
* [Nickel-metal hydride battery](https://en.wikipedia.org/wiki/Nickel%E2%80%93metal_hydride_battery): Typically used for those small cells (AA / AAA).
* [Nickel–cadmium battery](https://en.wikipedia.org/wiki/Nickel%E2%80%93cadmium_battery) (NiCd): Also commonly found in small battery cells. The self-discharge is at 10% per month according to Wikipedia.
* Lithium Manganese Oxide (LMO): Used for cell phones, laptops, and electric vehicles. An example is [SAMSUNG SDI-ESS](https://www.europe-solarstore.com/samsung-sdi-ess-lithium-ion-storage-3-6-kwh.html) with an operating temperature from -10°C to +40°C.

## Price

The prices change a lot. Especially currently in Germany. Check for your own. It might be helpful to know that 1 Watt = 1 Volt ⋅ Ampere.

* Na+: 65 EUR/kWh, expected to drop to 40 EUR/kWh ([source](https://www.nextbigfuture.com/2022/12/catl-will-mix-cheaper-sodium-ion-batteries-with-lithium-for-acceptable-range-evs.html))
* NMC333: 137 EUR/kWh ([source](https://www.engineering.com/story/the-promise-of-sodium-ion-batteries))
* NMC811: 90–100 EUR/kWh
* NMX: roughly 5% cheaper than NMC811
* LFP: 65 EUR/kWh — 75 EUR/kWh. I’ve only found one for 150 EUR/kWh. If you buy them for your photovoltaics system in Germany, they are WAY more expensive. Like 10x the price. It’s crazy at the moment.
* LTO: 300 EUR/kWh ([source](https://german.alibaba.com/product-detail/Yinlong-Class-A-2-3V-66160H-1600162850593.html))

## Cycles

* Na+: About 1000 cycles — that is quite a downside. It essentially means that the price either needs to be half the price of NMC batteries or the sodium battery needs to come with another huge advantage.
* NMC333: 2000–2500 cycles
* NMC811: 2000–2500 cycles
* NMX: 2500 cycles
* LFP: 3000 cycles
* LTO: **10,000- 20,000 cycles** ([source](https://files.gwl.eu/inc/_doc/attach/StoItem/7015/GWL_LTO1865_Rechargeable.pdf), [source](https://shop.gwl.eu/LTO-Tech/))🤯
* Nano LTO: **extremely high, potentially infinite** 🤯

## Gravimetric Energy Density

* Na+: 160 Wh/kg
* **NMC811**: **280 Wh/kg** and it’s expected to get over 300 Wh/kg
* NMX: 240–260 Wh/kg
* LFP: 200 Wh/kg
* LTO: 60–110 Wh/kg
* Nano LTO: I could not find anything

## Volumetric Energy Density

* Na+: 300 Wh/L
* **NMC811: 500 Wh/L**
* LFP: 350 Wh/L
* LTO: 177 Wh/L
* Nano LTO: I could not find anything

## Charging Speed

How fast can we get from 0% to 80% of the charge?

* Na+: 20 minutes
* NMC811: 15 minutes
* LFP: 15 minutes
* LTO: 6 minutes to charge
* **Nano LTO: 72s**. The charging station might not be able to do this.

## Temperature Resilience

Looking into data sheets of batteries you can see that there are two temperature ranges: (1) For charging (2) for capacity retention. In literature you can sometimes also see temperatures for thermal runaway — essentially when they catch fire.

* Li-NMC333 / LFP: 5°C to +45°C; thermal runaway at 210°C
* Na+: -20°C to +60°C ([source](https://faradion.co.uk/technology-benefits/strong-performance/)), thermal runaway is unknown ([source](https://faradion.co.uk/technology-benefits/superior-safety/))
* LTO: -15°C to +45°C ([source](https://files.gwl.eu/inc/_doc/attach/StoItem/7015/GWL_LTO1865_Rechargeable.pdf)), thermal runaway at 170°C ([source](https://www.mdpi.com/1996-1073/8/1/490/htm)). Another [source](https://shop.gwl.eu/LTO-Tech/) claims -30°C operating temperature.
* Nano LTO: Still good at -40°C!

## Robustness

What happens if the battery gets punctured? That is relevant e.g. in car accidents.

* Li-NMC333/Li-NMC811: They are known for the issue that they can catch fire.
* LTO: Almost nothing happens. Those are extremely safe.

## Efficiency

* **Li-NMC333**: The charge/discharge efficiency is around 80–90%. The self-discharge is around 0.35% to 2.5% per month.
* **Na+**: round-trip efficiency up to 92%, **negligible self-discharge**
* **LTO**: I saw claims for 98% recharge efficiency ([source](https://shop.gwl.eu/LTO-Tech/)).

## Resources

* [**Cobalt**](https://en.wikipedia.org/wiki/Cobalt) **(Co)**: Mainly mined in the Democratic Republic of the Congo (DRC). It’s a [conflict mineral](https://en.wikipedia.org/wiki/Conflict_minerals_law).
* [**Manganese**](https://en.wikipedia.org/wiki/Manganese) (Mn): Mined in South Africa, Australia, Gabon, China, Brazil, Ghana, India, Ukraine.
* [**Lithium**](https://en.wikipedia.org/wiki/Lithium) (Li): Mined in Australia, Chile, China, Argentina. The mining waste poses significant environmental and health hazards.
* [**Nickel**](https://en.wikipedia.org/wiki/Nickel) (Ni): Produced in Indonesia, the Philippines, Russia, New Caledonia, Australia, and Canada.
* [**Phosphate**](https://en.wikipedia.org/wiki/Phosphate) (PO4): Produced in China (45%), Morocco (13%), United States (12%), Russia (5%).
* [**Sodium**](https://en.wikipedia.org/wiki/Sodium) (Na): Can be produced in pretty much every country as salt is a [sodium chloride](https://en.wikipedia.org/wiki/Sodium_chloride) compound. If you have salt, you can get sodium.

## Resources for this article

* Andreas Schmitz: [NMX Akku: Bald in vielen E-Autos ?](https://www.youtube.com/watch?v=Ztj1VdJMJrI) on YouTube, 01.08.2021 (German, 12:31)
* Andreas Schmitz: [Natrium Ionen Akku — Unbekannte Details](https://www.youtube.com/watch?v=y8Ut9mMX0Kg) on YouTube, 08.08.2021 (German, 16:31)
* Andreas Schmitz: [Nano LTO Akku — 72s voll & unbegrenzte Zyklenfestigkeit](https://www.youtube.com/watch?v=LgucKC14xxM) on YouTube, 31.10.2021 (German, 12:06)
* [NMC-Akkumulator](https://de.wikipedia.org/wiki/NMC-Akkumulator) on Wikipedia (German)
* [Lithium-Nickel-Mangan-Cobalt-Oxide](https://de.wikipedia.org/wiki/Lithium-Nickel-Mangan-Cobalt-Oxide) on Wikipedia (German)
* [Lithium-titanate battery](https://en.wikipedia.org/wiki/Lithium-titanate_battery) on Wikipedia
* [Sodium-ion battery](https://en.wikipedia.org/wiki/Sodium-ion_battery) on Wikipedia
* Yuqing Chen, Yuqiong Kang, Yun Zhao et al: [A review of lithium-ion battery safety concerns: The issues, strategies, and testing standards](https://www.diva-portal.org/smash/get/diva2:1506359/FULLTEXT01.pdf) in Journal of Energy Chemistry, 2021.
* Man Chen, Qiujuan Sun, Yongqi Li et al: [A Thermal Runaway Simulation on a Lithium Titanate Battery and the Battery Module](https://www.mdpi.com/1996-1073/8/1/490/htm) in Energies, 2015.
