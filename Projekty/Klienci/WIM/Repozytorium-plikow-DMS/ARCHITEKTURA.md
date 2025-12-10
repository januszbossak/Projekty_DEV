---
ostatnia_aktualizacja: 2025-12-09
changelog_przeglad_do: 2025-12-01
---

# Architektura: Repozytorium plików (DMS)

> **Ostatnia aktualizacja:** 2025-12-09
> **CHANGELOG przegląd do:** 2025-12-01

---

## Aktualna koncepcja

### Stack techniczny

- **Frontend:** React (widoki kafelkowe/listowe, drzewo z lazy loading).
- **Backend:** .NET (wpięty w AMODIT, wykorzystuje istniejącą infrastrukturę).
- **Baza danych:** Oddzielna baza danych SQL (decyzja 2025-12-01) dla metadanych.
- **Przechowywanie plików:** System plików (zasoby sieciowe), spójne z folderem Attachment (`Attachment/Repository Files/{ID_Przestrzeni}/{ID_Folderu}/...`).
- **Wyszukiwanie:** Lucene (pełnotekstowe) z filtrowaniem wyników po uprawnieniach.
- **Inne:** AI do wytwarzania kodu (generowanie na podstawie projektu wizualnego).

### Główne komponenty i parametry techniczne

- **Struktura logiczna:**
  - **Przestrzenie (Root):** Najwyższy poziom, brak możliwości przerwania dziedziczenia.
  - **Foldery:** Zagnieżdżona struktura. **Limit:** Maksymalnie 20 poziomów zagnieżdżenia.
  - **Pliki:** Przechowywane w folderach. **Limit:** Maksymalnie 2000 obiektów w jednym folderze.

- **System uprawnień (Model):**
  - **Dziedziczenie:** Top-down (Przestrzeń → Folder → Plik).
  - **MVP1:** Definiowanie uprawnień TYLKO na poziomie Przestrzeni (brak zrywania dziedziczenia w dół).
  - **Docelowo:** Możliwość przerwania dziedziczenia na poziomie folderu/pliku (checkbox "Przerwij dziedziczenie").
  - **Role:** Administrator (pełny), Edycja (swoje pliki + struktura), Odczyt.
  - **Uprawnienia wynikowe:** Widoczność folderu wynika z dostępu do plików wewnątrz (read-only na strukturę w górę).

- **Interfejs użytkownika:**
  - **Nawigacja:** Drzewo folderów po lewej stronie.
  - **Lazy Loading:** Pobieranie węzłów na żądanie (maksymalnie 100 pozycji na widok dla wydajności).
  - **Widoki:** Kafelkowy (MVP), opcjonalnie lista.
  - **URL:** Oparty na ID węzłów (`/repository/{ID_Przestrzeni}/{ID_Folderu}...`), a nie na nazwach (uniknięcie problemów ze znakami specjalnymi/długością).

---

## Kluczowe decyzje architektoniczne

| Data | Decyzja | Dlaczego | Status | Źródło |
|------|---------|----------|--------|--------|
| [[2025-12-01]] | **Oddzielna baza danych** | Decyzja o separacji od głównej bazy AMODIT, ale wpięcie w ten sam ekosystem aplikacyjny. | ✅ Wdrożone | [[2025-12-01 Planowanie sprintu]] |
| [[2025-11-27]] | **Nazwa "Przestrzeń" dla Root** | Uniknięcie konfliktu nazewniczego z "Obszarem" w AMODIT. | ✅ Wdrożone | [[2025-11-27 Planowanie Sprintu]] |
| [[2025-11-14]] | **Uprawnienia tylko na poziomie Przestrzeni (MVP1)** | Uproszczenie wdrożenia, eliminacja skomplikowanego zarządzania wyjątkami w pierwszej wersji. | ✅ Wdrożone | [[2025-11-14 Spotkanie projektowe - Repozytorium]] |
| [[2025-11-14]] | **Limity struktury (20 poziomów, 2000 obiektów)** | Ograniczenie złożoności technicznej i problemów wydajnościowych interfejsu/systemu plików. | ✅ Wdrożone | [[2025-11-14 Spotkanie projektowe - Repozytorium]] |
| [[2025-10-28]] | **Przechowywanie plików na dysku (nie DB)** | Uniknięcie problemów z rozmiarem bazy i backupem. Spójność z mechanizmem Attachment. | ✅ Wdrożone | [[2025-10-28 Spotkanie projektowe - Design]] |
| [[2025-10-28]] | **Struktura fizyczna oparta na ID** | Unikalność nazw, brak problemów z długością ścieżek Windows i znakami specjalnymi. | ✅ Wdrożone | [[2025-10-28 Spotkanie projektowe - Design]] |
| [[2025-10-28]] | **Wyszukiwanie Lucene z post-filtrowaniem** | Wymóg bezpieczeństwa: użytkownik widzi w wynikach tylko to, do czego ma prawo. | ✅ Wdrożone | [[2025-10-28 Spotkanie projektowe - Design]] |

---

## Historia koncepcji (odrzucone/zmienione)

| Data | Co było | Dlaczego odrzucono | Źródło |
|------|---------|-------------------|--------|
| [[2025-10-28]] | Pliki w tabeli CaseAttachment | Zmiana na oddzielną bazę danych (2025-12-01) dla lepszej separacji. | [[2025-12-01 Planowanie sprintu]] |
| [[2025-10-28]] | Przechowywanie w bazie danych (Blob) | Problemy z wydajnością i backupem przy dużych wolumenach. | [[2025-10-28 Spotkanie projektowe - Design]] |
| [[2025-07-30]] | Repozytorium jako widok na sprawy | Zmiana na odrębną aplikację/strukturę niezależną od spraw. | [[2025-11-30 Spotkanie projektowe]] |