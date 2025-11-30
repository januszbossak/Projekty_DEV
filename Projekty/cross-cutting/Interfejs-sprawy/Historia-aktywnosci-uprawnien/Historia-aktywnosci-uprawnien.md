# Project Canvas: Historia aktywności i uprawnień

**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-09-04
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-09-04

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem |
| **Tech Lead** | Piotr Buczkowski | Analiza techniczna i implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Mechanizmy śledzenia historii zmian i uprawnień w sprawach są niespójne i nie w pełni transparentne. Historia uprawnień nie zawsze uwzględnia wszystkie ustawienia procesu (np. "administrator nie ma praw"), a w historii aktywności (`CaseActivity`) logowane są zdarzenia, które nie są nigdzie wyświetlane. Prowadzi to do nieporozumień i utrudnia audytowanie dostępu do spraw.

### Cel biznesowy
Zapewnienie spójnego, dokładnego i w pełni transparentnego mechanizmu śledzenia historii uprawnień i aktywności w sprawach. Użytkownicy muszą mieć pewność, że informacje historyczne, które widzą w systemie, w 100% odzwierciedlają faktyczny stan i konfigurację.

### Cel techniczny
Ujednolicenie logiki odpowiedzialnej za generowanie i wyświetlanie historii uprawnień. Zweryfikowanie celu ukrytych zdarzeń w `CaseActivity` i podjęcie decyzji o ich wyświetlaniu lub usunięciu. Dodanie elastycznej konfiguracji logowania zdarzeń.

### Metryka sukcesu
- Historia uprawnień poprawnie odzwierciedla wszystkie konfiguracje, w tym ustawienie "administrator nie ma praw".
- Cel zdarzenia "edycja sprawy" w `CaseActivity` jest wyjaśniony, a jego logowanie lub wyświetlanie jest świadomą decyzją.
- Administratorzy mogą kontrolować poziom logowania aktywności (np. wysłane maile), aby zarządzać rozmiarem bazy danych.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | 🔍 Do weryfikacji | [[2025-09-04]] | Zdarzenie "edycja sprawy" w `CaseActivity` jest logowane, ale nie wyświetlane. Należy zweryfikować jego powiązanie z mechanizmem historii uprawnień. | Hipoteza: zdarzenie to tworzy migawkę stanu uprawnień w momencie edycji sprawy, co jest niezbędne do prawidłowego działania historii uprawnień. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-09-04]] | Mechanizm historii uprawnień musi uwzględniać ustawienie procesu "administrator nie ma praw do sprawy". | Zapewnia to spójność informacji o uprawnieniach w całym systemie i eliminuje mylące dane w historii. | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-09-04]] | Logowanie maili wysłanych ze sprawy w `CaseActivity` będzie opcjonalne (włączane/wyłączane w ustawieniach). | Daje to administratorom kontrolę nad ilością generowanych logów i rozmiarem bazy danych, co jest istotne w dużych instalacjach. | - |
| ADR-004 | ✅ Zatwierdzone | [[2025-09-08]] | Przy każdym logowanym zdarzeniu w historii sprawy powinna być zapisywana informacja o uprawnieniach użytkownika, który wykonał akcję. | Umożliwia to pełniejszą analizę audytową, wyjaśniając, dlaczego dany użytkownik mógł wykonać określoną operację. Jest to kluczowe dla pełnej transparentności historii. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza

**Trwa praca nad:**
- Weryfikacją powiązania zdarzenia "edycja sprawy" z historią uprawnień (Piotr Buczkowski).
- Implementacją uwzględnienia ustawienia "administrator nie ma praw" w historii (Piotr Buczkowski).

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-04]] | Utworzenie projektu w odpowiedzi na zidentyfikowane niespójności w historii aktywności i uprawnień. | [[2025-09-04 Rada architektów]] |
| [[2025-09-08]] | Rozszerzono wymagania o konieczność logowania informacji o uprawnieniach użytkownika przy każdym zdarzeniu w historii sprawy. | [[2025-09-08 Sprint review]] |
| [[2025-09-11]] | Zidentyfikowano powiązany problem w wyświetlaniu historii zmian pól na formularzu. Zobacz podprojekt [[Interfejs-sprawy/Historia-sprawy]]. | [[2025-09-11 Rada architektów]] |
