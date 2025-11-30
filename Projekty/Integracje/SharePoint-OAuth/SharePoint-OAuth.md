# SharePoint - OAuth

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | | |
| **Tester** | | |

**Typ:** Integracja techniczna
**Status:** KRYTYCZNY - W realizacji
**Data rozpoczęcia:** 2025-09-18
**Planowane zakończenie:** Q4 2025
**Deadline zewnętrzny:** 2 kwietnia 2026 (wycofanie ACS przez Microsoft)

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

**KRYTYCZNE:** Microsoft wycofuje wsparcie dla mechanizmu uwierzytelniania ACS z dniem **2 kwietnia 2026 roku**. Po tej dacie obecna integracja z SharePoint przestanie działać.

### Cel projektu

Zaprojektowanie i zaimplementowanie nowego mechanizmu uwierzytelniania opartego o OAuth, który zastąpi przestarzały ACS.

### Powiązane dokumenty
- Inicjatywa w backlogu: [link]

---

## 2. Kontekst techniczno-architektoniczny

### Podejście architektoniczne

Nowy mechanizm oparty o OAuth z generycznym interfejsem do zarządzania konfiguracjami połączeń.

### Rozwiązanie techniczne

- Implementacja nowego mechanizmu uwierzytelniania opartego o **OAuth**
- Stworzenie **generycznego interfejsu w ustawieniach systemowych** do zarządzania wieloma konfiguracjami połączeń
- Wzorzec podobny do istniejących konfiguracji dla poczty przychodzącej
- Obsługa różnych aplikacji i środowisk

### Kluczowe decyzje architektoniczne

| Data | Decyzja | Uzasadnienie |
|------|---------|--------------|
| 2025-09-18 | Realizacja kompleksowa, bez tymczasowych rozwiązań | Krytyczność zadania, potrzeba stabilnego rozwiązania |
| 2025-09-18 | Start prac w najbliższych sprintach, zakończenie Q4 2025 | Deadline zewnętrzny (ACS wygasa 02.04.2026) |

### Zadania

- [ ] **Piotr:** Zaprojektowanie nowego rozwiązania i przygotowanie zadania do implementacji w najbliższym sprincie

---

## 3. Plan wydań MVP

### MVP1: [Nazwa/Cel]
**Cel:** [Dlaczego akurat taki zakres? Co chcemy zweryfikować?]

**Funkcjonalności:**
- [ ] Funkcjonalność A
- [ ] Funkcjonalność B
- [ ] Funkcjonalność C

**Planowana data:**

---

### MVP2: [Nazwa/Cel]
**Cel:** [Co rozszerzamy? Dlaczego?]

**Funkcjonalności:**
- [ ] Funkcjonalność D
- [ ] Funkcjonalność E

**Planowana data:**

---

### Backlog (przyszłe MVP)
- Funkcjonalność F
- Funkcjonalność G

---

## 4. Powiązane koncepcje

### Centralne repozytorium "Aplikacji OAuth"

**Status:** Koncepcja odłożona na przyszłość (nie w bieżącym MVP)

**Problem:**
Obecne konfiguracje metod uwierzytelniania (np. dla poczty Microsoft 365) są często zaszyte w kodzie lub wymagają skomplikowanych wpisów w parametrach systemowych, co utrudnia zarządzanie i skalowanie.

**Proponowane rozwiązanie:**
- Stworzenie centralnego repozytorium do zarządzania "Aplikacjami OAuth" (podobnie do nazwanych połączeń do baz danych)
- Panel do definiowania aplikacji (np. "Microsoft Graph API") z kluczowymi parametrami:
  - Client ID
  - Secret
  - Tenant ID
- Generowanie wielu tokenów dostępowych dla różnych kont i celów
- W konfiguracjach integracji (np. poczta przychodząca) - wybór z listy zdefiniowanych tokenów zamiast ręcznego wpisywania danych

**Decyzja (2025-08-07):**
Koncepcja słuszna, ale wdrożenie nie jest częścią bieżącego zakresu. Zostanie uwzględniona w ramach przyszłej kompleksowej reorganizacji ustawień systemowych.

---

## 5. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-07 | Dodano koncepcję centralnego repozytorium OAuth | Rada Architektów 2025-08-07 |
| 2025-09-18 | KRYTYCZNE: ACS wygasa 02.04.2026, start prac OAuth, deadline Q4 2025 | Rada Architektów 2025-09-18 |
