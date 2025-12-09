---
ostatnia_aktualizacja: 2025-12-08
changelog_przeglad_do: 2025-11-17
---

# Roadmapa: AMODIT Copilot

> **Ostatnia aktualizacja:** 2025-12-08  
> **CHANGELOG przegląd do:** 2025-11-17

---

## ✅ PRODUKCJA - MVP1 "AI Driven Workflow"

**Wydane:** 2025-09-08

**Dostarczone funkcjonalności:**

- ✅ **Generowanie procesu przez Copilota (tryb konsultacyjny)** - AI zadaje ~20 kluczowych pytań analitycznych, użytkownik może odpowiadać lub wrzucić dokument wymagań, podsumowanie przed generowaniem JSON, mechanizm polling dla długich operacji - [[2025-09-08 Sprint review]]
- ✅ **Baza wiedzy organizacji** - Prywatna per instancja, izolacja między klientami, świadome dodawanie dokumentów (bez auto-dodawania), integracja przez funkcje silnika reguł, uprawnienia zarządzane przez administratorów - [[2025-09-18 Planowanie sprintu]]
- ✅ **Ask AI** - Funkcja AI na poziomie pojedynczej sprawy, analiza dokumentów ze sprawy (zapytania ofertowe, umowy, CV kandydatów), integracja z OCR post-processing, dostępne wszystkie modele Azure (GPT-4o, GPT-3.5, mini, nano) - [[2025-08-26 Notatka projektowa - AMODIT UI]]
- ✅ **Pomoc w tworzeniu i edytowaniu reguł** - Generowanie reguł w języku skryptowym AMODIT na podstawie tematu biznesowego, opisywanie istniejących reguł ("co robi ta reguła") - [[2025-08-26 Notatka projektowa - AMODIT UI]]
- ✅ **Wsparcie dla użytkowników** - Copilot zna procesy i raporty w systemie, pomaga znaleźć odpowiedni proces/raport i może uruchomić sprawę - [[2025-08-26 Notatka projektowa - AMODIT UI]]
- ✅ **Wiedza o AMODIT** - Pełna dokumentacja z Wiki AMODIT, wiedza o wszystkich funkcjach z kodu źródłowego, odpowiedzi na ogólne pytania o system - [[2025-08-26 Notatka projektowa - AMODIT UI]]

**Znane ograniczenia MVP1:**

- ⚠️ **Brak dostępu do danych transakcyjnych** - Użytkownik nie może zapytać np. "Ile zostało mi urlopu?". Częściowo możliwe przez funkcję `AddToKnowledgeBase` na poziomie reguł. Planowane: dostęp włączalny per organizacja - [[2025-08-26 Notatka projektowa - AMODIT UI]]
- ⚠️ **Analiza reguł tylko pojedynczo** - Copilot analizuje pojedynczą regułę, nie analizuje zbiorczych zależności między regułami - [[2025-08-26 Notatka projektowa - AMODIT UI]]

---

## 🛠️ W TRAKCIE - MVP2 "Usprawnienia i bezpieczeństwo"

**Planowane wydanie:** Q1 2026 / [DO UZUPEŁNIENIA]

**Cel:** Rozbudowa funkcjonalności dla zaawansowanych użytkowników, usprawnienie UI/UX, zabezpieczenie danych zgodnie z RODO.

**Status funkcjonalności:**

- 🔄 **Generowanie dokumentacji powdrożeniowej** - Przycisk "Generuj dokumentację" w ustawieniach procesu, wymaga przygotowania schematu dokumentacji i promptu - [[2025-11-17 Planowanie sprintu]]
- 🔄 **Przepisanie frontendu bazy wiedzy** - Zgodność z design systemem (szablon jak obszary/słowniki/źródła danych/klucze szyfrujące) - [[2025-11-03 Sprint review-codex]]
- 🔄 **Eksport wyników** - POC eksportu do Word/Markdown, dostęp do spraw przez zapytania, docelowo respektowanie uprawnień via raporty tymczasowe - [[2025-11-03 Sprint review-codex]]
- 🔄 **Przesyłanie dokumentów do konwersacji** - Analiza treści dokumentu przesłanego przez użytkownika podczas konwersacji z Copilotem - [[2025-10-20 Sprint review]]
- 🔄 **Poprawa wyświetlania function calling** - Przycisk z ogólnym opisem zamiast kodu - [[2025-10-20 Sprint review]]
- 🔄 **Analiza bezpieczeństwa danych (RODO)** - Dedykowane spotkanie w sprawie szyfrowania, retencji i ewentualnego przechowywania danych u klienta (on-prem). Moduł AI dorobiony przez Mateusza, konkluzje do spisania - [[2025-11-04 Rada architektów]], [[2025-11-03 Sprint review-codex]]
- 🔄 **Podgląd logów OCR w bilingu** - Bez wchodzenia do bazy, sygnały o konieczności przepięcia klientów na nowy OCR - [[2025-11-03 Sprint review-codex]]

---

## 📋 PLANOWANE - MVP3 "Rozszerzenie możliwości"

**Planowane:** Q2-Q3 2026 / [DO UZUPEŁNIENIA]

**Zakres (wstępny):**

- [ ] **Usprawnienia bazy wiedzy** - Administratorzy baz wiedzy, możliwość wrzucania plików (PDF, Word) jako treści, zarządzanie datą ważności (od-do), wersjonowanie treści (zachowanie starych wersji, filtrowanie bieżących/wygasłych) - [[2025-09-25 Rada architektów]]
- [ ] **AI do tłumaczenia formularzy** - Automatyczne tłumaczenie formularzy na różne języki, automatyczne dodawanie tooltipów do pól - [[2025-09-25 Rada architektów]]
- [ ] **Analiza zbiorcza zależności między regułami** - Copilot analizuje wzajemne zależności między regułami, nie tylko pojedyncze reguły - [[2025-08-26 Notatka projektowa - AMODIT UI]]
- [ ] **Dostęp do danych transakcyjnych** - Włączalny per organizacja, zgodnie z uprawnieniami użytkownika (np. "Ile zostało mi urlopu?") - [[2025-08-26 Notatka projektowa - AMODIT UI]]
- [ ] **Usprawnienia UX** - Lepszy spinner oczekiwania ("Model myśli..."), zadawanie pytań pojedynczo zamiast w bloku (bardziej naturalna konwersacja) - [[2025-09-08 Sprint review]]

**Otwarte pytania:**

- [ ] Model cenowy Copilota - podnieść ceny aby zarabiać na funkcjonalności - [[2025-09-02 Rada architektów]]

---

## 🗄️ BACKLOG (przyszłe wersje)

**Funkcjonalności odroczone:**

- **Trwałość przesłanych dokumentów** - Obecnie dokumenty przesyłane do konwersacji są dostępne tylko na czas konwersacji - [[2025-10-20 Sprint review]]
- **Wyświetlanie nazwy procesu przy uruchamianiu sprawy** - Zgłoszona potrzeba wyświetlania nazwy procesu gdy AI uruchamia sprawę - [[2025-10-20 Sprint review]]

**Problemy do rozwiązania:**

- **Problem z analizą procesów PKF** - Jeden z procesów powoduje błąd "ups, coś poszło nie tak", przekazane Mateuszowi do analizy - [[2025-09-02 Rada architektów]]
- **Optymalizacja zużycia tokenów w bazie wiedzy** - Ryzyko długiego czasu zapisu, brak dokumentacji - [[2025-09-18 Planowanie sprintu]]
- **Brak IntelliSense dla funkcji silnika reguł** - Funkcje `Knowledge Base Document Insert`, `Knowledge Base Search`, `Ask AI`, `Get To Do` - brak autouzupełniania - [[2025-09-18 Planowanie sprintu]]

---

## 📊 Historia wydań

| Data | Wersja | Co wydano | Źródło |
|------|--------|-----------|--------|
| [[2025-09-08]] | MVP1 "AI Driven Workflow" | Tryb konsultacyjny generowania procesów, baza wiedzy organizacji, Ask AI, pomoc z regułami, wsparcie użytkowników, wiedza o AMODIT | [[2025-09-08 Sprint review]] |
| [[2025-08-26]] | Projekt utworzony | Rozdzielenie Copilota i AI OCR na dwa osobne projekty | [[2025-08-26 Notatka projektowa - AMODIT UI]] |

---

