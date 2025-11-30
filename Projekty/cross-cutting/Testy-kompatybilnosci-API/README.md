# Testy kompatybilności API

**Klient:** AMODIT (roadmapa)
**Status:** 💡 Propozycja
**PDM:** [do uzupełnienia]
**Deweloper:** Adrian Kotowski
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Testy-kompatybilnosci-API]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR) - test snapshotowy
- Roadmapa MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Częste problemy z kompatybilnością wsteczną wynikają z braku automatycznej kontroli nad zmianami w publicznych interfejsach i metodach kluczowych bibliotek. Przypadkowe modyfikacje publicznego API mogą łamać kompatybilność wsteczną.

### Rozwiązanie

Test snapshotowy zapisujący snapshot wszystkich publicznych metod z kluczowych bibliotek do pliku i porównujący z aktualnym stanem przy każdym uruchomieniu, wykrywając zmiany w publicznych metodach przed wdrożeniem.

### Obecna faza

📋 **Propozycja** - wymaga decyzji o zakresie bibliotek i częstotliwości aktualizacji snapshota

**Ukończono:**
- ✅ Zaproponowanie rozwiązania testu snapshotowego

**W trakcie:**
- Decyzja o zakresie bibliotek objętych testem
- Decyzja o częstotliwości aktualizacji snapshota

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Test snapshotowy** | Proste rozwiązanie, łatwe do zrealizowania, wykrywa zmiany przed wdrożeniem |

---

## MVP1: Test snapshotowy dla publicznych metod

**Cel:** Wykrywanie przypadkowych zmian w publicznym API przed wdrożeniem

**Zakres:**
- [ ] Test zapisujący snapshot wszystkich publicznych metod
- [ ] Porównanie z aktualnym stanem przy każdym uruchomieniu
- [ ] Wykrywanie zmian (modyfikacje, usunięcia)
- [ ] Mechanizm aktualizacji snapshota

**Planowana data:** [do uzupełnienia]

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]

