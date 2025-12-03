# Rada Architektów – 2025-09-30

**Powiązane projekty:**
- `cross-cutting/Logowanie-powiadomien` – temat 1
- `moduly/Modul-raportowy` – temat 2
- `moduly/Silnik-regul` – tematy 3, 4

---

## 1. Rejestrowanie wysłanych maili – moment rejestracji

**Projekt:** `cross-cutting/Logowanie-powiadomien`

### Kontekst i Problem

Kamil zgłosił problem z rejestrowaniem wysłanych maili w historii. Obecnie maile są rejestrowane w momencie, gdy trafiają do kolejki maili, a nie w momencie faktycznego wysłania. To może prowadzić do nieprawidłowych danych – mail może trafić do kolejki, ale nigdy się nie wysłać (np. usługa stoi, kolejka nie schodzi), a w tabeli będzie zapisane, że został wysłany.

Problem dotyczy również maili zbiorczych, które składają się z wielu spraw – nie może być na takim mailu zapisane jedno `ItemID` sprawy, tylko powinno być zapisane do poszczególnych spraw, że "wysłano mail".

### Zidentyfikowane Ryzyka

- Nieprawidłowe dane w tabeli wysłanych maili – maile mogą być oznaczone jako wysłane, choć faktycznie nie zostały wysłane
- Administratorzy mogą mieć błędne raporty maili wysłanych
- Użytkownicy mogą zgłaszać, że maile nie doszły, podczas gdy w systemie są oznaczone jako wysłane
- Maile zbiorcze nie mogą mieć jednego `ItemID` sprawy – muszą być zapisane per sprawa

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rejestrowanie w momencie faktycznego wysłania | Rejestrowanie maila jako wysłanego dopiero w momencie, gdy faktycznie zejdzie z kolejki i się wyśle | ✅ Wybrana – zapewnia prawidłowe dane |
| Rejestrowanie w momencie trafienia do kolejki | Obecne rozwiązanie | ❌ Odrzucona – prowadzi do nieprawidłowych danych |
| Rejestrowanie per sprawa dla maili zbiorczych | W momencie kompilacji maila zbiorczego zapisywanie do poszczególnych spraw, że "wysłano mail" | ✅ Wybrana – zapewnia prawidłowe przypisanie do spraw |

### Decyzja

**Status:** 🔍 Do weryfikacji

Trzeba przemyśleć, jak zaimplementować rejestrowanie maili jako wysłanych dopiero w momencie faktycznego wysłania (gdy mail zejdzie z kolejki), a nie w momencie trafienia do kolejki. Problem dotyczy również maili zbiorczych, które muszą być rejestrowane per sprawa.

**Szczegóły techniczne:**
- Obecnie rejestrowanie następuje w momencie trafienia do kolejki
- Maile mogą być wysyłane od razu (nie trafiają do kolejki) lub trafiają do kolejki, jeśli nie ma połączenia do serwera
- Maile zbiorcze składane przez Job (Notification Job) dotyczą kilku spraw i muszą być rejestrowane per sprawa
- Rejestrowanie jest opcjonalne (można włączyć/wyłączyć)
- Na razie funkcjonalność jest używana tylko testowo (poza Biamem)

### Zadania

- **Piotr Buczkowski:** Przeanalizowanie i zaprojektowanie rozwiązania rejestrowania maili jako wysłanych w momencie faktycznego wysłania → termin: do ustalenia
- **Kamil Dubaniowski / Piotr Buczkowski:** Dedykowane spotkanie projektowe do przegadania tematu → termin: do ustalenia

### Punkty otwarte

- Jak zarejestrować informację o sprawie dla maili, które trafiają do kolejki (gdy nie ma jeszcze informacji o sprawie)?
- Jak obsłużyć maile zbiorcze, które dotyczą wielu spraw?
- Czy rejestrowanie powinno być w momencie wykonania usługi wysyłającej mail, czy w momencie faktycznego wysłania?

---

## 2. Raport z zawężeniem do pola typu Odnośnik

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

Temat wyszedł w piątek na spotkanie z konsultantami. Chodzi o możliwość zbudowania raportu z zawężeniem do pola typu Odnośnik. Według komentarza zanotowanego wygląda na to, że funkcjonalność jest w nowych wersjach raportów, ale może nie działać poprawnie.

### Zidentyfikowane Ryzyka

- Brak możliwości zawężenia raportu do pola typu Odnośnik może utrudniać analizę danych
- Jeśli funkcjonalność istnieje, ale nie działa, może prowadzić do frustracji użytkowników

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Łukasz Bott sprawdzi, czy funkcjonalność faktycznie istnieje w nowych raportach i czy działa poprawnie. Jeśli nie działa, trzeba będzie poprawić.

**Szczegóły techniczne:**
- Funkcjonalność powinna być w nowych wersjach raportów
- Damian próbował to pokazać, ale coś nie działało
- Trzeba dobrze przetestować

### Zadania

- **Łukasz Bott:** Weryfikacja czy funkcjonalność zawężenia raportu do pola typu Odnośnik istnieje i działa poprawnie → termin: do ustalenia

### Punkty otwarte

- Czy funkcjonalność faktycznie istnieje w nowych raportach?
- Jeśli istnieje, dlaczego nie działała podczas demo Damiana?
- Jakie są dokładne wymagania dotyczące zawężenia raportu do pola typu Odnośnik?

---

## 3. Rozszerzenie funkcji SetListFilter o opcję SetDefault

**Projekt:** `moduly/Silnik-regul`

### Kontekst i Problem

Obecnie w funkcji `SetListFilter` (i podobnych funkcjach) jest zasada, że jeśli filtr zwróci jedną wartość, to ona zostaje automatycznie wybrana jako wartość pola. Do funkcji `SendReference` została dodana opcja `SetDefault`, którą można to wyłączyć. Przydałoby się dodać podobną opcję do pozostałych funkcji (`SetListFilter` i innych).

### Zidentyfikowane Ryzyka

- Brak spójności między funkcjami może prowadzić do zamieszania użytkowników
- Brak możliwości wyłączenia automatycznego wyboru wartości może być problematyczne w niektórych scenariuszach

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dodanie opcji SetDefault do pozostałych funkcji | Dodanie opcji `SetDefault` do funkcji `SetListFilter` i innych podobnych funkcji, podobnie jak w `SendReference` | ✅ Wybrana – zapewnia spójność między funkcjami |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostanie dodana opcja `SetDefault` do funkcji `SetListFilter` i innych podobnych funkcji, podobnie jak w `SendReference`. Opcja pozwoli wyłączyć automatyczne wybieranie wartości, gdy filtr zwróci jedną wartość.

**Szczegóły techniczne:**
- Funkcja `SendReference` ma już opcję `SetDefault`
- Funkcje do rozszerzenia: `SetListFilter` i inne podobne funkcje
- Opcja pozwala wyłączyć automatyczne wybieranie wartości, gdy filtr zwróci jedną wartość

### Zadania

- **Łukasz Bott:** Weryfikacja funkcji `SetListFilter` i dodanie opcji `SetDefault` w podobny sposób jak w `SendReference` → termin: do ustalenia

### Punkty otwarte

- Które jeszcze funkcje powinny mieć opcję `SetDefault`?
- Czy opcja powinna działać tak samo we wszystkich funkcjach?

---

## 4. SetList – zachowanie przy jednej pozycji

**Projekt:** `moduly/Silnik-regul`

### Kontekst i Problem

Kamil zauważył, że funkcja `SetList` działa nieco inaczej niż `SetListFilter`. W funkcji `SetList`, jeśli podamy tylko jedną pozycję jako listę, nie jest automatycznie wybrana (w przeciwieństwie do `SetListFilter`). Trzeba to zweryfikować i ewentualnie ujednolicić zachowanie.

### Zidentyfikowane Ryzyka

- Brak spójności między funkcjami może prowadzić do zamieszania użytkowników
- Różne zachowanie może być nieintuicyjne

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Trzeba zweryfikować zachowanie funkcji `SetList` przy jednej pozycji i sprawdzić, czy powinno być ujednolicone z `SetListFilter`. Pole typu Lista zachowuje się inaczej niż inne pola – może wpisać wartość inną niż to, co się proponuje z listy, i też zostanie zapamiętana.

**Szczegóły techniczne:**
- Funkcja `SetList` działa inaczej niż `SetListFilter`
- Pole typu Lista zachowuje się jak pole tekstowe – może przyjąć wartość inną niż z listy
- Trzeba zweryfikować, czy zachowanie jest zamierzone czy błąd

### Zadania

- **Łukasz Bott:** Weryfikacja zachowania funkcji `SetList` przy jednej pozycji podczas weryfikacji tematu 3 → termin: do ustalenia

### Punkty otwarte

- Czy różnica w zachowaniu między `SetList` a `SetListFilter` jest zamierzona?
- Czy pole typu Lista powinno automatycznie wybierać wartość, gdy jest tylko jedna pozycja?

---

## 5. ReferenceQueryEx – weryfikacja funkcjonalności

**Projekt:** `moduly/Silnik-regul`

### Kontekst i Problem

Kamil zapytał, czy w funkcji `ReferenceQueryEx` jest już dodana funkcjonalność `ThrowError`, która była zgłoszona wcześniej. Piotr potwierdził, że funkcjonalność jest już dodana.

### Zidentyfikowane Ryzyka

Nie zidentyfikowano.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ✅ Zatwierdzone

Funkcjonalność `ThrowError` jest już dodana do funkcji `ReferenceQueryEx`. Temat nie wymaga dalszych działań.

**Szczegóły techniczne:**
- Funkcja `ReferenceQueryEx` ma już wszystkie opcje, w tym `ThrowError`
- Temat został zamknięty

### Zadania

Brak – funkcjonalność już istnieje.

### Punkty otwarte

Brak.

