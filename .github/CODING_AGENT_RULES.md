# Coding Agent Rules - Blog Verbesserungen

Erstellt am: 30. September 2025
Für: Automatisierte Blog-Artikel Verbesserungen
Repository: MartinThoma.github.io

## Übersicht

Diese Datei enthält spezifische Regeln und Richtlinien für AI Coding Agents, die an der systematischen Verbesserung der Blog-Artikel arbeiten.

## 🌐 Metadaten-Standards

### Sprach-Tags
**Regel:** Jeder Artikel muss ein `lang` Tag mit ISO 639-1 Code haben
- **Deutsche Artikel:** `lang: de`
- **Englische Artikel:** `lang: en`
- **Position:** Im YAML Front Matter

**Beispiele:**
```yaml
---
layout: post
title: Beispiel Artikel
slug: beispiel-artikel
lang: de
category: German posts
tags: German, example
---
```

### Slug-Tags
**Regel:** Jeder Artikel muss ein `slug` Tag haben
- **Ableitung:** Aus Dateinamen ohne Datums-Präfix und .md-Suffix
- **Position:** Im YAML Front Matter nach `title`

**Beispiele:**
- `2025-09-23-pv-wirtschaftlichkeitsberechnung.md` → `slug: pv-wirtschaftlichkeitsberechnung`
- `2024-12-31-wood-joints.md` → `slug: wood-joints`
- `simple-filename.md` → `slug: simple-filename`

## 📊 Zahlenformatierung

### Dezimaltrennzeichen
**Regel:** Verwende immer den **Punkt (.)** als Dezimaltrennzeichen
- **Gilt für:** Alle Artikel (deutsche UND englische)
- **Grund:** Einheitlichkeit und internationale Kompatibilität

**Beispiele:**
```
✅ Richtig:  3.14159
✅ Richtig:  0.25
✅ Richtig:  1.5 Millionen
✅ Richtig:  2.7%

❌ Falsch:   3,14159 (auch nicht in deutschen Artikeln!)
❌ Falsch:   0,25 (auch nicht in deutschen Artikeln!)
❌ Falsch:   1,5 Millionen (auch nicht in deutschen Artikeln!)
```

### Tausendertrennzeichen
**Regel:** Keine Tausendertrennzeichen verwenden
- **Anwendung:** Zahlen ohne Trennzeichen schreiben

**Beispiele:**
```
✅ Richtig:  1000
✅ Richtig:  10000
✅ Richtig:  100000
✅ Richtig:  1000000
✅ Richtig:  5250.75
✅ Richtig:  350000 EUR

❌ Falsch:   1,000 (Komma als Tausendertrennzeichen)
❌ Falsch:   1 000 (Leerzeichen)
❌ Falsch:   1&thinsp;000 (schmales Leerzeichen)
❌ Falsch:   1.000 (Punkt als Tausendertrennzeichen)
```

### Währungsformatierung
**Regel:** Währungszeichen immer NACH der Zahl platzieren
- **Anwendung:** Für alle Währungen (€, $, £, etc.)
- **Gilt für:** Alle Artikel (deutsche UND englische)

**Beispiele:**
```
✅ Richtig:  72€
✅ Richtig:  500$
✅ Richtig:  1250£
✅ Richtig:  15.99€
✅ Richtig:  1000000€

❌ Falsch:   €72
❌ Falsch:   $500
❌ Falsch:   £1250
❌ Falsch:   €15.99
❌ Falsch:   €1000000
```

### Dimensionsangaben
**Regel:** Verwende × (Multiplikationszeichen) statt x für Dimensionen
- **Symbol:** × (Unicode U+00D7)
- **Anwendung:** Maße, Auflösungen, Größenangaben

**Beispiele:**
```
✅ Richtig:  1920×1080 (Bildschirmauflösung)
✅ Richtig:  200×150×100mm (Abmessungen)
✅ Richtig:  A4: 210×297mm
✅ Richtig:  5×3 Meter
✅ Richtig:  1200×800 Pixel

❌ Falsch:   1920x1080
❌ Falsch:   200x150x100mm
❌ Falsch:   A4: 210x297mm
❌ Falsch:   5x3 Meter
❌ Falsch:   1200x800 Pixel
```

## ✍️ Sprachspezifische Regeln

### Deutsche Artikel
- **Komma-Setzung:** Nach einleitenden Nebensätzen
- **Groß-/Kleinschreibung:** Substantive groß, adjektivische Verwendung klein
- **"das" vs "dass":** Konjunktion = "dass", Artikel/Pronomen = "das"
- **Anglizismen:** Nur wenn etabliert, sonst deutsche Begriffe bevorzugen
- **Höflichkeitsformen:** Konsistent "Sie" in technischen Anleitungen

### Englische Artikel
- **Oxford Comma:** Verwenden in Listen (A, B, and C)
- **Zeitformen:** Konsistenz innerhalb eines Artikels
- **Artikel:** "a/an/the" korrekte Verwendung
- **Passive Voice:** Sparsam verwenden, aktive Stimme bevorzugen
- **Amerikanisches vs. Britisches Englisch:** Konsistent amerikanisch

## 🔧 Technische Regeln

### Markdown-Formatierung
- **Überschriften:** Logische Hierarchie (H1 → H2 → H3)
- **Listen:** Konsistente Formatierung (- für ungeordnet, 1. für geordnet)
- **Code-Blöcke:** Immer mit Sprach-Tag (```python, ```bash, etc.)
- **Links:** Aussagekräftige Link-Texte, keine "hier klicken"

### LaTeX/Mathematik
- **Formeln:** Konsistente Notation innerhalb eines Artikels
- **Variablen:** Kursiv für Variablen, aufrecht für Funktionen
- **Einheiten:** Aufrecht und mit schmalen Leerzeichen

## 🎯 Prioritäten bei Korrekturen

### Hohe Priorität
1. **Rechtschreibfehler** - Immer korrigieren
2. **Grammatikfehler** - Immer korrigieren
3. **Zahlenformatierung** - Nach obigen Regeln
4. **Broken Links** - Reparieren oder entfernen

### Mittlere Priorität
1. **Stilistische Verbesserungen** - Nur bei deutlichen Problemen
2. **Markdown-Formatierung** - Standardisieren
3. **Fachterminologie** - Vereinheitlichen

### Niedrige Priorität
1. **Umformulierungen** - Nur bei Verständnisproblemen
2. **Strukturelle Änderungen** - Nur bei gravierenden Problemen

## 🚫 Was NICHT geändert werden soll

### Inhaltliche Aspekte
- **Meinungen und Bewertungen** - Autorensicht respektieren
- **Persönliche Erfahrungen** - Nicht neutralisieren
- **Fachliche Einschätzungen** - Nur bei offensichtlichen Fehlern korrigieren

### Stilistische Aspekte
- **Persönlicher Schreibstil** - Individuelle Note beibehalten
- **Humor und Ironie** - Nicht "professionalisieren"
- **Umgangssprachliche Elemente** - Bei bewusstem Einsatz belassen

## 🔍 Regex-Patterns für häufige Korrekturen

### Deutsche Dezimalzahlen korrigieren
```regex
# Suchen: \b\d+,\d+\b
# Ersetzen: [Komma durch Punkt ersetzen]
```

### Währungszeichen korrigieren
```regex
# Suchen: ([€$£])([0-9]+(?:\.[0-9]+)?)
# Ersetzen: $2$1
```

### Dimensionen mit × korrigieren
```regex
# Suchen: (\d+)x(\d+)
# Ersetzen: $1×$2
```

### Tausendertrennzeichen hinzufügen
```regex
# Suchen: \b(\d{1,3})(\d{3})\b
# Ersetzen: $1&thinsp;$2
```

### Doppelte Leerzeichen entfernen
```regex
# Suchen:   (zwei oder mehr Leerzeichen)
# Ersetzen:  (ein Leerzeichen)
```

## 📋 Checkliste pro Artikel

### Vor der Bearbeitung
- [ ] Artikel-Sprache identifiziert (DE/EN)
- [ ] Fachbereich erkannt (Mathematik, IT, Politik, etc.)
- [ ] Bestehende Formatierung analysiert

### Während der Bearbeitung
- [ ] Rechtschreibung geprüft
- [ ] Grammatik geprüft
- [ ] Zahlenformatierung nach Regeln angepasst
- [ ] Links auf Funktionalität geprüft
- [ ] Markdown-Syntax validiert

### Nach der Bearbeitung
- [ ] Änderungen dokumentiert
- [ ] Inhaltliche Korrektheit sichergestellt
- [ ] Keine strukturellen Brüche verursacht

## 📈 Erfolgsmetriken

### Quantitative Metriken
- Anzahl korrigierter Rechtschreibfehler
- Anzahl korrigierter Grammatikfehler
- Anzahl standardisierter Zahlenformate
- Anzahl reparierter Links

### Qualitative Metriken
- Verbesserte Lesbarkeit
- Konsistentere Formatierung
- Einheitlichere Terminologie

---

**Status:** Aktiv
**Letzte Aktualisierung:** 30. September 2025
**Gültig für:** Alle automatisierten Blog-Verbesserungen
**Version:** 1.0
