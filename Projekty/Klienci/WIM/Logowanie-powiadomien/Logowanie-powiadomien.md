# Project Canvas: Logowanie powiadomień

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-09-08
**Klient:** WIM
**Data rozpoczęcia:** 2025-08-19

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | Przemek | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Klient (WIM) potrzebuje pełnego audytu komunikacji wychodzącej z systemu, w szczególności powiadomień e-mail. Brak szczegółowego logowania utrudnia weryfikację, czy i jakie informacje zostały wysłane do użytkowników, co jest kluczowe w procesach wymagających ścisłego śledzenia komunikacji.

### Cel biznesowy
Zapewnienie klientowi WIM pełnej transparentności i możliwości audytu wszystkich powiadomień systemowych wysyłanych w ramach spraw.

### Cel techniczny
Rozbudowa mechanizmu `UserActivity` o możliwość logowania powiadomień (w tym maili z treścią i załącznikami). Implementacja musi być elastyczna i konfigurowalna, aby umożliwić włączanie/wyłączanie poszczególnych opcji logowania w zależności od potrzeb wydajnościowych i wymagań klienta.

### Metryka sukcesu
- Administrator jest w stanie odtworzyć pełną historię komunikacji mailowej dla dowolnej sprawy.
- Mechanizm logowania jest w pełni konfigurowalny i domyślnie włączony dla nowych instalacji.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-08-19]] | Wymagane jest logowanie powiadomień o wszystkich zmianach statusu, dodaniu załącznika, komentarza itp. | Zapewnia to pełny ślad audytowy komunikacji systemowej, co jest kluczowym wymaganiem klienta. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-08-21]] | Logowanie powiadomień będzie domyślnie włączone (`ON`) dla nowych instalacji. | Upraszcza to konfigurację dla nowych klientów i zapewnia, że kluczowa funkcjonalność audytowa jest aktywna od samego początku. | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-09-08]] | Mechanizm logowania zostanie rozszerzony o 3 opcje: logowanie maili (włącz/wyłącz), logowanie treści maili (włącz/wyłącz), logowanie załączników (włącz/wyłącz). | Daje to administratorom elastyczną kontrolę nad poziomem szczegółowości logów i wpływem na wydajność oraz rozmiar bazy danych. | - |
| ADR-004 | ✅ Zatwierdzone | [[2025-09-08]] | W logu zdarzenia będzie zapisywana informacja o uprawnieniach użytkownika, który wykonał akcję. | Umożliwia to pełniejszą analizę audytową, wyjaśniając, dlaczego dany użytkownik mógł wykonać określoną operację. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🟢 W realizacji

**Ukończono:**
- ✅ Zaimplementowano podstawowy mechanizm logowania powiadomień.
- ✅ Dodano elastyczne opcje konfiguracji (logowanie treści, załączników).
- ✅ Dodano logowanie informacji o uprawnieniach.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-08-19]] | Utworzenie projektu w odpowiedzi na wymaganie klienta WIM dotyczące potrzeby audytu powiadomień systemowych. | [[2025-08-19 Rada architektów]] |
| [[2025-08-21]] | Podjęto decyzję, że logowanie powiadomień będzie domyślnie włączone dla nowych instalacji. | [[2025-08-21 Rada architektów]] |
| [[2025-09-08]] | Rozbudowano mechanizm o szczegółowe, konfigurowalne logowanie wysyłanych maili (treść, załączniki) oraz informacji o uprawnieniach użytkownika. | [[2025-09-08 Sprint review]] |
