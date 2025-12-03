# CHANGELOG - Logowanie delete case

## 2025-08-28 - Rada architektów

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-28 Rada architektów|2025-08-28 Rada architektów]]

**Kategoria:** #Funkcjonalność #Audyt

**Kontekst:**
Klienci wymagają permanentnego rejestrowania informacji o tym, kto i kiedy usunął sprawę za pomocą funkcji DeleteCase. Obecnie operacja ta jest logowana tylko w logach systemowych, które są okresowo czyszczone, przez co nie ma trwałego śladu audytowego.

### Problem

Problem pojawia się gdy sprawa zostaje usunięta (np. z powodu wymogu usunięcia danych osobowych), a później ktoś inny próbuje do niej dotrzeć – nie ma informacji kto, kiedy i dlaczego sprawa została usunięta.

### Zidentyfikowane Ryzyka

- Brak śladu audytowego dla operacji usuwania spraw
- Niemożność wyjaśnienia klientom, kto i kiedy usunął sprawę
- Brak możliwości weryfikacji przyczyny usunięcia sprawy

### Rozważane alternatywy (odrzucone)

- **UserActivity w zakładce "Aktywność administracyjna"** - aktywność administracyjna dotyczy zarządzania kontami i uprawnieniami, nie operacji na sprawach
- **CaseEvent (historia biznesowa sprawy)** - sprawa jest usuwana razem z historią, więc wpis również zniknie
- **CaseActivity** - CaseActivity jest czyszczone przy usuwaniu sprawy

### Decyzja

**Status:** ✅ Zatwierdzone

Utworzenie nowej zakładki w UserActivity o nazwie **"Usunięte Sprawy"** (ewentualnie "Usuwanie Spraw") do rejestrowania operacji DeleteCase. Zakładka będzie również wykorzystywana do innych podobnych operacji w przyszłości, jeśli zajdzie taka potrzeba.

### Szczegóły techniczne

- Logowanie w UserActivity Log (widoczne w logach systemowych)
- Rejestrowane informacje:
  - CaseID (numer sprawy)
  - Nazwa procesu (z którego pochodziła sprawa)
  - Data i czas operacji
  - Użytkownik, który wykonał operację
  - Ewentualnie komentarz/uzasadnienie (opcjonalnie)
- Operacja DeleteCase wywoływana z reguły funkcji również będzie logowana w ten sam sposób
- Usunięcie sprawy z poziomu kosza (przez administratora) również będzie logowane w ten sam sposób

**Uwaga:** Rozważano wyświetlanie modala z komentarzem przy usuwaniu, ale uznano to za zbyt utrudniające proces. Na razie rejestrowane będzie minimum: kto, kiedy, CaseID i nazwa procesu.

### Zadania

- **Piotr Buczkowski:** Implementacja logowania DeleteCase w UserActivity Log
- **Piotr Buczkowski:** Utworzenie nowej zakładki "Usunięte Sprawy" w UserActivity
- **Łukasz Bott:** Przygotowanie propozycji projektu na designie (termin: 2025-08-29)

### Punkty otwarte

- Czy w przyszłości będą inne operacje wymagające logowania w tej zakładce?
- Czy komentarz/uzasadnienie powinno być obowiązkowe czy opcjonalne?

