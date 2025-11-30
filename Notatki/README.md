# Notatki

## Przegląd

Ten katalog zawiera notatki ze spotkań zespołu R&D AMODIT. Notatki są **głównym źródłem informacji** o postępach projektów, decyzjach architektonicznych i ustaleniach technicznych.

---

## Rodzaje notatek

### Rada Architektów
**Częstotliwość:** 2-3 razy w tygodniu
**Zawartość:**
- Decyzje architektoniczne
- Nowe koncepcje i pomysły
- Problemy techniczne wymagające konsultacji
- Analiza złożonych zagadnień

**Format:** `Rada architektów YYYY-MM-DD.md`

---

### Sprint Review
**Częstotliwość:** Co 2 tygodnie (koniec sprintu)
**Zawartość:**
- Demo zrealizowanych funkcjonalności
- Podsumowanie wykonanej pracy
- Metryki sprintu
- Feedback od zespołu

**Format:** `Sprint review YYYY-MM-DD.md`

---

### Daily
**Częstotliwość:** Codziennie
**Zawartość:**
- Status update od uczestników (co robią, blokery)
- Omówienie nowych zgłoszeń do backlogu
- Tematy organizacyjne (urlopy, zastępstwa)

**Struktura:**
- **Część 1:** Status update (wszyscy uczestnicy)
- **Część 2:** Omówienie backlogu (węższe grono)
- **Część 3:** Tematy organizacyjne (opcjonalnie)

**Format:** `Daily YYYY-MM-DD.md`

---

### Spotkania projektowe
**Częstotliwość:** Ad-hoc
**Zawartość:**
- Szczegółowe omówienie konkretnych projektów
- Sesje projektowe UI/UX
- Warsztaty techniczne
- Specyfikacje funkcjonalne

**Format:** `[Typ spotkania] [Temat] YYYY-MM-DD.md`

---
## Transkrypcje
Tych notatek nie uwzględniasz w kolejce do przetwarzania. Stanowią archiwum transkrypcji.

---

## Rejestr przetworzonych notatek

Plik `_rejestr_przetworzonych.md` śledzi które notatki zostały już przetworzone i uwzględnione w dokumentacji projektów.

**Status notatki:**
- ✅ **Przetworzona** - wszystkie tematy z notatki zostały przeanalizowane i uwzględnione w odpowiednich projektach
- ⏳ **Oczekująca** - notatka czeka na przetworzenie

---

## Workflow przetwarzania

Notatki są regularnie analizowane i ich treść jest przenoszona do dokumentacji odpowiednich projektów w katalogu `projekty/`.

**Szczegółowy workflow:** Zobacz `PROMPT.md`

**Zasada:** Notatki przetwarzane są **chronologicznie** (według dat) aby zachować spójność historii projektów.

---

## Zasady tworzenia notatek
WAŻNE: Ty, jako AI nie tworzysz notatek. Notatki dostarcza użytkownik. Twoim zadaniem jest czytanie notatek a nie ich aktualizacja

1. **Data w nazwie pliku** - format YYYY-MM-DD
2. **Jasna struktura** - nagłówki dla poszczególnych tematów
3. **Kompletne informacje:**
   - Uczestnicy (opcjonalnie)
   - Decyzje i ich uzasadnienia
   - Zadania z przypisanymi osobami
   - Linki do powiązanych zasobów
4. **Kontekst** - wystarczająco szczegółowy opis aby zrozumieć temat bez dostępu do innych materiałów
