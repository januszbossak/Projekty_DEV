# Podpis kwalifikowany macOS

**Klient:** WIM
**Status:** 🟡 W realizacji (MVP - wstrzymany)
**Tech Lead:** [do uzupełnienia]

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Podpis-kwalifikowany-macOS]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele
- Decyzje architektoniczne
- Roadmapa MVP
- Ryzyka i ich mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem
Użytkownicy macOS nie mogą składać podpisów kwalifikowanych w Trust Center.

### Rozwiązanie
Natywna aplikacja macOS (.NET MAUI) z automatyczną detekcją certyfikatów.

### Obecna faza
🟡 **MVP1: Podstawowe podpisywanie** - wstrzymany na rzecz e-Doręczeń

**Zrealizowane:**
- ✅ PoC ukończony i zwalidowany (Q3 2025)
- ✅ Automatyczna detekcja certyfikatów (Szafir, SimplySign)
- ✅ Obsługa wielu kluczy na jednej karcie

**W trakcie:**
- Testowanie wykrywania Szafir
- Przebudowa UI (spójność z wersją Windows)

**Blokery:**
- Brak podpisu SimpleSign do testów (Adrian)
- Brak centralnego dostępu do podpisów testowych i Mac dla zespołu

---

## Szybkie linki

- [Walidator EU DSS](https://ec.europa.eu/digital-building-blocks/DSS/webapp-demo/validation)
- Repozytorium: [link]
- Trust Center (staging): [link]
