---
ostatnia_aktualizacja: 2025-12-09
changelog_przeglad_do: 2025-12-01
---

# Roadmapa: Repozytorium plików (DMS)

> **Ostatnia aktualizacja:** 2025-12-09
> **CHANGELOG przegląd do:** 2025-12-01

---

## ✅ Produkcja (MVP 1)

**Cel:** Podstawowa funkcjonalność umożliwiająca odbiór wdrożenia w WIM.
**Termin:** Grudzień 2025

### Zrealizowane / Wdrażane:

- **Struktura:**
  - ✅ Przestrzenie (Root) - tworzenie, edycja nazwy, usuwanie (ikona kosza).
  - ✅ Foldery - zagnieżdżanie do 20 poziomów.
  - ✅ Pliki - przechowywanie na zasobach sieciowych.
  
- **Uprawnienia:**
  - ✅ Definiowanie na poziomie Przestrzeni (Administrator, Edycja, Odczyt).
  - ✅ Dziedziczenie w dół (bez możliwości przerwania w MVP1).
  
- **Interfejs Użytkownika:**
  - ✅ Drzewo folderów z Lazy Loading (max 100 węzłów).
  - ✅ Widok kafelkowy plików.
  - ✅ Upload plików (Drag & Drop).
  - ✅ Podgląd plików (komponent z raportów).
  
- **Backend:**
  - ✅ Oddzielna baza danych.
  - ✅ Endpointy do zarządzania strukturą.
  - ✅ Integracja z Lucene (wyszukiwanie pełnotekstowe).

**Źródła:** [[2025-12-01 Planowanie sprintu]], [[2025-11-27 Planowanie Sprintu]], [[2025-11-14 Spotkanie projektowe - Repozytorium]]

---

## 🛠️ W trakcie / Planowane (MVP 2 - Rozwojowe)

**Cel:** Rozszerzenie funkcjonalności o zaawansowane zarządzanie i metadane.

### Funkcjonalności:

- **Zaawansowane Uprawnienia:**
  - ⏳ Przerwanie dziedziczenia na poziomie folderu/pliku.
  - ⏳ Uprawnienia do poszczególnych plików.
  
- **Metadane Użytkownika:**
  - ⏳ Opis pliku (do wyszukiwania).
  - ⏳ Tagi/Etykiety.
  - ⏳ Daty obowiązywania (wygaszanie).

- **Operacje na plikach:**
  - ⏳ Przenoszenie plików między folderami (Drag & Drop).
  - ⏳ Wersjonowanie plików.
  - ⏳ Historia zmian (kto dodał, kto usunął).
  - ⏳ Kosz (soft delete z retencją np. 30 dni).

- **Inne:**
  - ⏳ Publiczne linki do plików.
  - ⏳ Powiadomienia o zmianach.

**Źródła:** [[2025-10-28 Spotkanie projektowe - Design]]

---

## 🗄️ Backlog / Odroczone

- **Metadane:** Zestawy metadanych definiowane per katalog.
- **Eksport/Import:** Eksport struktury folderów.
- **Przechowywanie:** Przechowywanie plików w bazie danych (Blob) - odrzucone dla dużych wolumenów.
- **Widoki:** Widok listy ze szczegółami (właściciel, rozmiar) - odroczone, w MVP tylko kafelki/prosta lista.

---

## Historia Wydań

| Data | Wersja | Opis | Źródło |
|------|--------|------|--------|
| Planowane | MVP 1.0 | Pierwsze wdrożenie produkcyjne u klienta WIM. | [[2025-12-01 Planowanie sprintu]] |