# Project Canvas: Podgląd plików

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-09-09
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-09-09

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | Piotr Buczkowski | Implementacja backendu, weryfikacja `GetAttachmentContent` |
| **Deweloper** | Przemysław Sołdacki | Implementacja frontendu (React) |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Występują dwa powiązane problemy z obsługą plików tekstowych. Po pierwsze, podgląd plików `.txt`, który kiedyś działał, przestał funkcjonować (regresja) i zachowuje się niespójnie w różnych częściach systemu. Po drugie, kluczowa funkcja silnika reguł, `GetAttachmentContent`, nie zwraca faktycznej treści plików tekstowych, a jedynie ich metadane, co uniemożliwia programowe przetwarzanie ich zawartości. Brakuje również wsparcia dla popularnych formatów jak JSON, XML czy Markdown.

### Cel biznesowy
Zapewnienie spójnego, bezpiecznego i funkcjonalnego mechanizmu podglądu dla szerokiej gamy plików tekstowych. Umożliwienie konsultantom i deweloperom niezawodnego dostępu do treści plików z poziomu reguł, co jest kluczowe dla automatyzacji i integracji.

### Cel techniczny
Naprawa regresji w podglądzie plików `.txt`. Rozszerzenie mechanizmu o wsparcie dla formatów `.json`, `.xml`, `.md`, `.html`, `.log`. Implementacja bezpiecznego renderowania (za pomocą `iframe sandbox`). Poprawa funkcji `GetAttachmentContent`, aby zwracała czystą treść tekstową. Wprowadzenie listy wykluczeń dla typów plików, które powodują problemy wydajnościowe (np. `.xlsm`).

### Metryka sukcesu
- Podgląd dla wszystkich zdefiniowanych typów plików tekstowych działa spójnie w całym systemie.
- Funkcja `GetAttachmentContent` poprawnie zwraca treść tekstową dla 100% plików tekstowych.
- Czas generowania podglądu dla problematycznych plików jest zerowy (po dodaniu ich do listy wykluczeń).

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-09-09]] | Naprawić regresję i przywrócić działanie podglądu dla plików `.txt`, ujednolicając jego zachowanie w całym systemie. | Jest to błąd, który obniża użyteczność systemu. Naprawa jest priorytetem. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-09-09]] | Rozszerzyć mechanizm podglądu o wsparcie dla formatów: `.json`, `.xml`, `.md`, `.html`, `.log`. | Są to powszechnie używane formaty, których brak wsparcia jest ograniczeniem dla użytkowników. | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-09-09]] | Wszystkie pliki tekstowe (w tym HTML) muszą być wyświetlane w `iframe` z atrybutem `sandbox` bez `allow-scripts`. | Jest to kluczowy wymóg bezpieczeństwa, który zapobiega wykonaniu potencjalnie złośliwych skryptów (XSS) zawartych w plikach HTML. | - |
| ADR-004 | ✅ Zatwierdzone | [[2025-09-09]] | Dodać konfigurowalną listę wykluczeń dla typów plików, dla których podgląd nie powinien być generowany. | Niektóre pliki (np. `.xlsm` z makrami) powodują ogromne problemy wydajnościowe podczas próby generowania podglądu. Możliwość ich wykluczenia jest niezbędna. | - |
| ADR-005 | 🔍 Do weryfikacji | [[2025-09-09]] | Funkcja `GetAttachmentContent` musi zostać poprawiona, aby zwracała czystą treść pliku tekstowego, a nie metadane. | Obecne zachowanie jest błędne i blokuje możliwość wykorzystania tej funkcji w regułach do przetwarzania treści plików. | - |
| ADR-006 | ⏸️ Odroczone | [[2025-09-09]] | Wdrożenie pełnego renderowania składni Markdown w podglądzie. | Jest to ulepszenie funkcjonalne, ale nie jest krytyczne dla MVP. W pierwszej wersji wystarczy wyświetlanie surowego tekstu. | - |

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-09]] | Utworzenie projektu. Zdiagnozowano problem z podglądem plików `.txt` i funkcją `GetAttachmentContent`. Zatwierdzono plan naprawy i rozszerzenia funkcjonalności. | [[2025-09-09 Rada architektów]] |
