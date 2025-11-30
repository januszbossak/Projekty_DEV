# Integracje REST - multipart/form-data

**Klient:** AMODIT (roadmapa)
**Status:** 🟢 W realizacji
**PDM:** [do uzupełnienia]
**Deweloper:** Adrian Kotowski
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Integracje-REST-multipart]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR) - multipart/form-data, x-www-form-urlencoded, tablica documents
- Roadmapa MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Obecna metoda przesyłania plików przez funkcję `callRest` oparta na indywidualnych parach klucz-wartość w nagłówkach jest nieelastyczna, nieintuicyjna i generuje nadmiarową liczbę parametrów.

### Rozwiązanie

Usprawnienie mechanizmu przesyłania załączników w integracjach REST:
- Natywne wsparcie dla `multipart/form-data` i `x-www-form-urlencoded`
- Zmienna dla listy załączników (odwołanie do listy na sprawie)
- Tablica `documents` z obiektami `DocumentName` i `DocumentValue` (Base64)
- Mechanizm podobny do headers - pary klucz-wartość przez nową linię

### Obecna faza

🛠️ **W realizacji** - implementacja usprawnień

**Ukończono:**
- ✅ Ustalenie architektury i podejścia technicznego

**W trakcie:**
- Implementacja usprawnień mechanizmu przesyłania załączników

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Zmienna dla listy załączników** | Elastyczne, upraszcza konfigurację |
| **Tablica `documents`** | Ustrukturyzowane podejście dla wielu dokumentów |
| **Natywne wsparcie multipart/form-data i x-www-form-urlencoded** | Standardowe formaty wymagane przez klientów |

---

## MVP1: Natywne wsparcie multipart/form-data i x-www-form-urlencoded

**Cel:** Umożliwienie wysyłania wielu plików w jednym żądaniu w standardowych formatach

**Zakres:**
- [ ] Zmienna dla listy załączników
- [ ] Tablica `documents` z `DocumentName` i `DocumentValue` (Base64)
- [ ] Obsługa `multipart/form-data`
- [ ] Obsługa `x-www-form-urlencoded`

**Planowana data:** Q4 2025

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
