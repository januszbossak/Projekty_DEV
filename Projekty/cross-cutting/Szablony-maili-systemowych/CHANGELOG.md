# CHANGELOG - Szablony maili systemowych

## 2025-09-09 - Rada architektów

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-09-09 Rada architektów|2025-09-09 Rada architektów]]

**Kategoria:** #Problem #Funkcjonalność

**Kontekst:**
Szablony maili systemowych są nadpisywane przy aktualizacji bazy danych, co powoduje problemy u klientów (szczególnie dużych, np. Orlen, LPP), którzy dostosowali szablony do swoich potrzeb. Klienci tracą swoje zmiany przy każdej aktualizacji systemu.

Dodatkowo szablony maili mają przestarzały wygląd (jak z poprzedniej epoki) i wymagają odświeżenia, ale to jest duże wyzwanie wymagające szerokiego podejścia.

### Problem

- Utrata zmian wprowadzonych przez klientów przy każdej aktualizacji systemu
- Problemy z klientami, którzy dostosowali szablony do swoich potrzeb
- Przestarzały wygląd szablonów maili (szarość, brak spójności z nowym interfejsem)
- Wszyscy duzi klienci mają ten problem (Orlen, LPP, inni)

### Zidentyfikowane Ryzyka

- Ryzyko kwalifikowania maili jako spam przy zmianach treści (wymagane testy na stronach sprawdzających współczynnik spamu)
- Duża liczba szablonów do przetworzenia (szacunkowo 20+ PBI dla różnych szablonów)

### Decyzja

**Status:** ✅ Zatwierdzone (rozwiązanie krótkoterminowe) / ⏸️ Odroczone (rozwiązania długoterminowe)

**Rozwiązanie krótkoterminowe (MVP):**
- Dodanie kolumny flagującej, które szablony mają być pomijane przy aktualizacji bazy danych
- Jeśli szablon jest oznaczony jako "pomijany", nie jest aktualizowany przy podnoszeniu wersji
- Rozwiązanie ad-hoc, które rozwiąże obecny problem (szacunkowo **1 godzina pracy**)
- Klienci mogą zmieniać szablony na własną odpowiedzialność, uwzględniając ryzyko kwalifikowania jako spam

**Rozwiązania długoterminowe (odroczone):**

1. **Customowy szablon + znacznik:**
   - Dodanie kolumny z customowym szablonem i kolumny decydującej, który szablon używać (domyślny vs customowy)
   - Jeśli kolumna customowego szablonu jest wypełniona, używa się customowego, jeśli pusta – domyślnego
   - W przyszłości może być rozbudowane o interfejs z przełącznikiem
   - Szacunkowo **5-20 godzin + testy**

2. **Pełny interfejs do zarządzania szablonami:**
   - Utworzenie interfejsu w ustawieniach systemowych do zarządzania szablonami maili
   - Możliwość tworzenia, edycji i zarządzania customowymi szablonami
   - Ochrona przed nadpisaniem przy aktualizacji
   - Szacunkowo **2 sprinty, 2 osoby**

3. **Globalna zmiana wszystkich szablonów:**
   - Odświeżenie wyglądu wszystkich szablonów maili (nowy design, spójność z interfejsem)
   - Proste ramki, białe tło (podobnie jak w głównym ekranie)
   - Wymaga mapy projektu i finansowania
   - Szacunkowo **20+ PBI** dla różnych szablonów

### Szczegóły techniczne

- Rozwiązanie krótkoterminowe: jedna kolumna flagująca (np. `SkipUpdate` lub `IsCustom`), która decyduje, czy szablon ma być pomijany przy aktualizacji
- Rozwiązanie długoterminowe: dwie kolumny – jedna z customowym szablonem, druga decydująca, który używać
- Szablony maili są przechowywane w bazie danych
- Przy aktualizacji bazy danych domyślne szablony są aktualizowane, chyba że są oznaczone jako pomijane

**Uwaga:** Temat był już wielokrotnie omawiany w przeszłości, ale nie został zrealizowany. Obecne rozwiązanie krótkoterminowe ma na celu szybkie rozwiązanie problemu, a długoterminowe rozwiązania wymagają mapy projektu i finansowania.

### Zadania

- **Piotr Buczkowski:** Implementacja pomijania wskazanych szablonów maili przy aktualizacji bazy danych (kolumna flagująca)
- **Piotr Buczkowski:** Przebadanie mechanizmu pomijania szablonów
- **Product Owner / Janusz Bossak:** Przygotowanie mapy projektu dla długoterminowych rozwiązań (customowy szablon, interfejs, globalna zmiana)

### Punkty otwarte

- Czy rozwiązanie krótkoterminowe (pomijanie przy aktualizacji) będzie wystarczające do czasu wdrożenia długoterminowych rozwiązań?
- Jak obsłużyć przypadek, gdy klient chce mieć różne szablony dla różnych języków?
- Czy customowe szablony powinny być dostępne tylko dla dużych klientów, czy dla wszystkich?
- Jak zapewnić, że customowe szablony nie będą kwalifikowane jako spam?
- Czy w przyszłości rozważyć przeniesienie szablonów poza bazę danych (np. do plików konfiguracyjnych)?

