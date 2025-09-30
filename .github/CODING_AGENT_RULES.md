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
lang: de
category: German posts
tags: German, example
---
```

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
