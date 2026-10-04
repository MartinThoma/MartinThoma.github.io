"""Charts for content/2026-09-15-energiewende.md.

Run from the repository root: python scripts/energiewende_charts.py
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

OUT_DIR = "images/2026/09"

NAVY = "#1f2937"
ORANGE = "#d4541d"
GREEN = "#1a7f4b"
GREY = "#6b7280"
GRID = "#e5e7eb"

# Total emissions without LULUCF in Mt CO2-eq.
# 1990-2024: UBA, Nationale Trendtabellen 1990-2024 (2026_EM_Entwicklung_in_D_Trendtabelle_THG.xlsx)
# 2025: UBA, Emissionsdaten 2025 & Projektionsdaten 2026, Hintergrundpapier (14.03.2026)
EMISSIONS = {
    1990: 1253.1, 1991: 1206.4, 1992: 1158.0, 1993: 1148.5, 1994: 1130.8,
    1995: 1123.4, 1996: 1140.2, 1997: 1104.8, 1998: 1080.0, 1999: 1045.5,
    2000: 1043.0, 2001: 1057.1, 2002: 1036.7, 2003: 1030.5, 2004: 1010.7,
    2005: 988.9, 2006: 1002.0, 2007: 963.5, 2008: 964.9, 2009: 901.3,
    2010: 933.2, 2011: 907.6, 2012: 916.9, 2013: 936.6, 2014: 895.2,
    2015: 898.6, 2016: 899.0, 2017: 886.3, 2018: 850.1, 2019: 798.0,
    2020: 731.0, 2021: 762.8, 2022: 749.3, 2023: 669.6, 2024: 649.8,
    2025: 648.9,
}
BASE = EMISSIONS[1990]
# UBA Projektionsdaten 2026 (measures decided until November 2025)
PROJECTION = {2025: 648.9, 2030: BASE * (1 - 0.626), 2040: BASE * (1 - 0.80), 2045: 212.5}
# § 3 KSG: -65 % by 2030, -88 % by 2040, net zero by 2045
TARGETS = {2025: 648.9, 2030: BASE * 0.35, 2040: BASE * 0.12, 2045: 0.0}


# Share of renewables in gross electricity consumption in %.
# UBA/AGEE-Stat: Zeitreihen zur Entwicklung der erneuerbaren Energien in Deutschland, Tabelle 2 (Stand: Februar 2026)
RENEWABLE_SHARE = {
    2015: 31.6, 2016: 31.8, 2017: 36.2, 2018: 37.9, 2019: 42.2, 2020: 45.4,
    2021: 41.7, 2022: 46.3, 2023: 52.9, 2024: 54.4, 2025: 55.1,
}
RENEWABLE_TARGET_2030 = 80.0  # § 1 EEG


def de(x: float, decimals: int = 0) -> str:
    s = f"{x:,.{decimals}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def emissions_chart() -> None:
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    years = list(EMISSIONS)
    ax.plot(years, list(EMISSIONS.values()), color=NAVY, lw=3, label="Messwerte (Inventar)")
    ax.plot(
        list(PROJECTION), list(PROJECTION.values()), color=ORANGE, lw=3, ls=(0, (5, 3)),
        marker="o", ms=8, mfc="white", mew=2, label="Projektion (UBA 2026, bisherige Maßnahmen)",
    )
    ax.plot(
        list(TARGETS), list(TARGETS.values()), color=GREEN, lw=2, ls=":",
        label="Deutsche Klimaziele (§ 3 Klimaschutzgesetz)",
    )
    ax.plot(list(TARGETS)[1:], list(TARGETS.values())[1:], "D", color=GREEN, ms=10)

    ax.axvline(2025.5, color="#9ca3af", lw=1)
    ax.axvline(2045, color="#a7d7bd", lw=1)
    ax.text(2025.0, 1215, "← Messwerte", ha="right", va="center", color=GREY)
    ax.text(2026.0, 1215, "Projektion und Ziele →", ha="left", va="center", color=GREY)
    ax.text(2045, 1215, "Netto-Null", ha="center", va="center", color=GREEN)

    ax.annotate(f"1990: {de(BASE)} Mio. t (Basisjahr)", (1990, BASE), (1990.5, 1300), color=NAVY)
    ax.annotate(
        f"2025: {de(EMISSIONS[2025])} Mio. t", (2025, EMISSIONS[2025]), (2014.3, 1000),
        color=NAVY, arrowprops=dict(arrowstyle="-", color=NAVY, lw=1),
    )
    p = PROJECTION
    ax.annotate(
        f"Projektion 2030: −62,6 % ({de(p[2030])} Mio. t)\nLücke zum Ziel: ≈ {de(p[2030] - TARGETS[2030])} Mio. t",
        (2030, p[2030]), (2031.5, 660), color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1),
    )
    ax.annotate(
        f"Projektion 2040: ≈ −80 %\n(≈ {de(p[2040])} Mio. t)", (2040, p[2040]), (2040.3, 470),
        color=ORANGE, ha="center", arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1),
    )
    ax.annotate(
        "Projektion 2045: 212,5 Mio. t\nbrutto (−83 %), d.h. ohne\nSenken", (2045, p[2045]), (2046.2, 260),
        color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1),
    )
    t = TARGETS
    ax.annotate(
        f"Ziel 2030: −65 %\n({de(t[2030])} Mio. t)", (2030, t[2030]), (2026.3, 210), color=GREEN,
        fontweight="bold", ha="center", arrowprops=dict(arrowstyle="-", color=GREEN, lw=1),
    )
    ax.annotate(
        f"Ziel 2040: −88 %\n({de(t[2040])} Mio. t)", (2040, t[2040]), (2036.5, 10), color=GREEN,
        fontweight="bold", ha="center", arrowprops=dict(arrowstyle="-", color=GREEN, lw=1),
    )
    ax.annotate(
        "Ziel 2045:\nNetto-Null", (2045, 0), (2046.2, -95), color=GREEN, fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=GREEN, lw=1),
    )
    ax.text(
        2030.5, 1050,
        "Zum Vergleich: Die EU-weiten Ziele\nsind −55 % bis 2030 und −90 % bis 2040.\n"
        "Deutschland hat sich für 2030 mehr\nvorgenommen (−65 %).",
        color=GREY, va="top", linespacing=1.5,
        bbox=dict(boxstyle="round,pad=0.5", fc="white", ec=GRID),
    )

    ax.set_xlim(1988, 2053)
    ax.set_ylim(-140, 1340)
    ax.set_xticks(list(range(1990, 2050, 5)))
    ax.set_yticks(list(range(0, 1201, 200)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: de(v)))
    ax.set_ylabel("Treibhausgas-Emissionen (Mio. t CO$_2$-Äquivalente pro Jahr)")
    ax.grid(axis="y", color=GRID)
    ax.axhline(0, color="#9ca3af", lw=1)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#9ca3af")
    ax.legend(loc="lower left", frameon=False)
    fig.text(
        0.012, 0.015,
        "Quellen: Umweltbundesamt (Emissionen 1990–2025, Projektionsdaten 2026), "
        "§ 3 Klimaschutzgesetz (deutsche Ziele), EU-Klimagesetz (EU-Ziele).\n"
        "Grafik: Martin Thoma, mit Claude AI in Python/matplotlib erstellt.",
        color=GREY, fontsize=8,
    )
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(f"{OUT_DIR}/co2-emissionen-deutschland.png")


def renewable_share_chart() -> None:
    years = list(RENEWABLE_SHARE)
    shares = list(RENEWABLE_SHARE.values())
    first, last = years[0], years[-1]
    past_rate = (shares[-1] - shares[0]) / (last - first)
    needed_rate = (RENEWABLE_TARGET_2030 - shares[-1]) / (2030 - last)
    trend_2030 = shares[-1] + past_rate * (2030 - last)

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    bars = ax.bar(years, shares, color=NAVY, width=0.7, label="Anteil erneuerbarer Energien (AGEE-Stat)")
    for bar, share in zip(bars, shares):
        ax.text(bar.get_x() + bar.get_width() / 2, share + 1, de(share, 1), ha="center", color=NAVY, fontsize=9)

    ax.plot([last, 2030], [shares[-1], RENEWABLE_TARGET_2030], color=GREEN, lw=2, ls=":",
            label=f"Nötiges Tempo: +{de(needed_rate, 1)} Prozentpunkte pro Jahr")
    ax.plot(2030, RENEWABLE_TARGET_2030, "D", color=GREEN, ms=10)
    ax.annotate("Ziel 2030: 80 %", (2030, RENEWABLE_TARGET_2030), (2030, RENEWABLE_TARGET_2030 + 4),
                color=GREEN, fontweight="bold", ha="center")
    ax.plot([last, 2030], [shares[-1], trend_2030], color=ORANGE, lw=2, ls=(0, (5, 3)),
            label=f"Bisheriges Tempo {first}–{last}: +{de(past_rate, 1)} Prozentpunkte pro Jahr")
    ax.plot(2030, trend_2030, "o", color=ORANGE, ms=8, mfc="white", mew=2)
    ax.annotate(f"≈ {de(trend_2030)} %", (2030, trend_2030), (2030.4, trend_2030 - 1.5), color=ORANGE)

    ax.set_xlim(first - 0.8, 2031.5)
    ax.set_ylim(0, 92)
    ax.set_xticks(list(range(first, 2031)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f} %"))
    ax.set_ylabel("Anteil am Bruttostromverbrauch")
    ax.grid(axis="y", color=GRID)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#9ca3af")
    ax.legend(loc="upper left", frameon=False)
    fig.text(
        0.012, 0.015,
        "Quellen: Umweltbundesamt/AGEE-Stat (Zeitreihen, Stand Februar 2026), § 1 EEG (Ziel 2030). "
        "Die Linien bis 2030 sind lineare Fortschreibungen, keine Prognose.\n"
        "Grafik: Martin Thoma, mit Claude AI in Python/matplotlib erstellt.",
        color=GREY, fontsize=8,
    )
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(f"{OUT_DIR}/erneuerbare-anteil-strom.png")


if __name__ == "__main__":
    emissions_chart()
    renewable_share_chart()
