"""
Jahreskosten wärme berechnung

https://www.waermepumpe.de/normen-technik/klimakarte/
"""


def get_leistungsbedarf_in_watt(
    volume: float,
    areas: dict[str, float],
    u_values: dict[str, float],
    outside_temp: float,
    desired_temp: float,
) -> float:
    transmission_energy = get_transimssion_energy(
        areas, u_values, outside_temp, desired_temp
    )
    ventilation_energy = get_ventilation_heat_energy(volume, outside_temp, desired_temp)
    return transmission_energy + ventilation_energy


def get_transimssion_energy(
    areas: dict[str, float],
    u_values: dict[str, float],
    outside_temp: float,
    desired_temp: float,
) -> float:
    """

    Returns:
        Required heating power to compensate heat transmission in Watt
    """
    energy = 0
    delta_t = desired_temp - outside_temp
    if delta_hours < 0:
        return 0
    for type, area in areas.items():
        u_value = u_values[type]
        energy += area * u_value * delta_t
    return energy


def get_ventilation_heat_energy(
    volume: float, outside_temp: float, desired_temp: float
) -> float:
    """

    Args:
        volume: in m³
        outside_temp: in °C
        desired_temp: in °C

    Returns:
        Required power in Watt
    """
    delta_t = desired_temp - outside_temp
    if delta_t < 0:
        return 0
    per_kelvin_and_cube_meter = 0.34  # W * h / (m³ * K)
    # The division by 2 is due to the fact that we should exchange half the
    # volume per hour
    return per_kelvin_and_cube_meter * delta_t * volume / 2


def get_energy_shower(
    people: int,
    minutes_per_person_per_day: float,
    desired_water_temp: float = 40,
    water_per_minute: float = 15.0,
    base_water_temperature: float = 15.0,
) -> float:
    if desired_temp > 50:
        raise ValueError("If you shower above 50°C, you will burn yourself.")
    water = minutes_per_person_per_day * water_per_minute
    delta_t = desired_water_temp - base_water_temperature
    if delta_t < 0:
        return 0
    energy_per_kelvin_per_liter = 1.16  # Wh/(L*K)
    return people * water * delta_t * energy_per_kelvin_per_liter


tmp2_hours = {  # temp in °C
    -16: 4.1,
    -14: 15.8,
    -12: 35.1,
    -10: 66.9,
    -8: 118,
    -6: 204.5,
    -4: 363,
    -2: 691.5,
    0: 1375.2,
    2: 2158.9,
    4: 2852.7,
    6: 3539.9,
    8: 4175.7,
    10: 4823.6,
    12: 5471.7,
    14: 6172.5,
    16: 6839.4,
}

total_energy = 0
u_value = 2.7  # W / (m² * K)
delta_t = 35.3
areas = {
    "window": 23.6,
    "wall": 286.881,
    "dach": 140.9,
    "rolladen": 2.4,
    "heizkoerper": 4.8,
}
u_values = {
    "window": 2.7,
    "wall": 0.6,
    "rolladen": 3.6,
    "heizkoerper": 1.2,
    "dach": 0.6,
}
desired_temp = 21  # °C

min_duschen_pro_tag_pro_person = 25
personen = 2
base_water_temperature = 15
showering_temp = 40
water_per_minute = 15
heating_oil_energy = 9.8  # kwh / Liter Heizöl
home_volume = 680.8  # in m³


hours_prev = 0
for temp, hours in sorted(tmp2_hours.items()):
    delta_hours = hours - hours_prev
    delta_t = desired_temp - temp
    total_energy += (
        get_leistungsbedarf_in_watt(
            home_volume, areas, u_values, outside_temp=temp, desired_temp=desired_temp
        )
        * delta_hours
    )
    hours_prev = hours
duschen = (
    get_energy_shower(
        people=personen,
        minutes_per_person_per_day=min_duschen_pro_tag_pro_person,
        desired_water_temp=showering_temp,
        base_water_temperature=base_water_temperature,
        water_per_minute=water_per_minute,
    )
    * 365.25
)
total_energy += duschen
duschen_kwh = duschen / 1000

total_energy_kwh = total_energy / 1000
print(f"Total {total_energy_kwh:,.0f} kWh")
print(f"- Heizöl: {total_energy_kwh / heating_oil_energy:,.0f} L")
print(f"Laut Energieausweis: {97 * 155:,} kh")

print("\n# Energie fürs Duschen")
print(f"Personen: {personen}")
print(f"Leitungswasser={base_water_temperature}°C, Duschtemperatur={showering_temp}°C")
print(f"Pro Person und Tag: {min_duschen_pro_tag_pro_person} min")
print(f"Wasser pro min: {water_per_minute}L")
print(
    f"⇒ {duschen_kwh:,.0f} kWh/Jahr oder {duschen_kwh / heating_oil_energy:,.0f} L Heizöl"
)

print("\n# Leistungsbedarf nach Außentemperatur")
for outside_tmp, hours in tmp2_hours.items():
    print(
        f"{outside_tmp:>4} ({hours:>6.0f} Stunden/Jahr): {get_leistungsbedarf_in_watt(home_volume, areas, u_values, outside_tmp, desired_temp)/1000:>4.1f}kW"
    )
