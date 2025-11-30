# Eksport/Import definicji procesów

**Typ:** Moduł systemu
**Status:** W realizacji
**Data rozpoczęcia:** 2025-10-20

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | [do uzupełnienia] | |
| **Deweloper** | [do uzupełnienia] | |

---

## Dokumentacja projektu

Pełna dokumentacja: [[Eksport-import-definicji-procesow]]

---

## Szybki przegląd

### Problem

Mechanizm eksportu i importu definicji procesów (XML) wymaga usprawnień w zakresie walidacji, obsługi konfliktów i prezentacji błędów użytkownikowi.

### Obecna faza

**W realizacji** - usprawnienia walidacji importu XML

**Zrealizowane:**
- Walidacja importu XML (4 nowe walidacje wykrywające konflikty GUID)

**Do realizacji:**
- Poprawa prezentacji błędów (opis tekstowy zamiast tabeli technicznej)
- Obsługa konfliktów duplikatów między środowiskami
- Docelowo: blokowanie importu przy konfliktach

---

## Powiązane projekty

- `moduly/Edytor-procesow-formularzy` - edycja definicji procesu
- `moduly/Ustawienia-systemowe` - parametr typu środowiska (prod/test)
