# Logowanie operacji delete case

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | Łukasz (design) | |
| **Tester** | | |

**Typ:** Funkcjonalność cross-cutting
**Status:** W analizie
**Data rozpoczęcia:** 2025-08-28
**Planowane zakończenie:** -

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

Klienci zgłaszają brak trwałego rejestru operacji usuwania spraw. Obecne logi systemowe są okresowo czyszczone, przez co znika historia tych działań. Jest to problem audytowy i compliance.

### Cel projektu

Zapewnienie trwałego rejestru operacji trwałego usuwania spraw (delete case) w systemie.

### Problem

- Brak trwałego rejestru operacji usuwania spraw
- Obecne logi systemowe są okresowo czyszczone
- Znika historia działań usuwania
- Problem zgłaszany przez klientów

---

## 2. Kontekst techniczno-architektoniczny

### Podejście architektoniczne

Wykorzystanie istniejącego mechanizmu "Aktywności użytkownika", który:
- Jest dostępny dla administratorów
- Nie jest powiązany z cyklem życia sprawy (permanentny)

### Rozwiązanie techniczne

**Rejestrowane operacje:**
- Trwałe usunięcie sprawy z poziomu reguły `delete case`
- Trwałe usunięcie sprawy z kosza

**Zawartość wpisu w logu:**
- Data operacji
- Identyfikator użytkownika wykonującego akcję
- Numer usuniętej sprawy
- Nazwa procesu, z którego pochodziła sprawa

### Kluczowe decyzje architektoniczne

| Data | Decyzja | Uzasadnienie |
|------|---------|--------------|
| 2025-08-28 | Wykorzystanie "Aktywności użytkownika" | Istniejący mechanizm, permanentny, dostępny dla administratorów |

---

## 3. Plan wydań MVP

### MVP1: Logowanie delete case

**Cel:** Zapewnić trwały rejestr operacji usuwania spraw

**Funkcjonalności:**
- [ ] Rejestrowanie usunięcia z reguły `delete case`
- [ ] Rejestrowanie usunięcia z kosza
- [ ] Zapis w logu "Aktywność użytkownika"
- [ ] Zawartość: data, użytkownik, numer sprawy, nazwa procesu

**Zespół:** Łukasz

**Planowana data:** -

---

## 4. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-28 | Utworzenie projektu, definicja wymagań | Rada Architektów 2025-08-28 |
