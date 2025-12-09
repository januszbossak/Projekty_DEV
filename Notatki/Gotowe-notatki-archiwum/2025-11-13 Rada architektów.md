> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-08
# Rada Architektów – 2025-11-13

**Powiązane projekty:**
- `Klienci/LOT` – tematy 1, 2
- `cross-cutting/Interfejs-sprawy/Podglad-szablonow` – temat 3
- `Moduly/Modul-raportowy` – temat 4

---

## 1. Podpis standardowy dla LOT-u

**Projekt:** `Klienci/LOT`

### Kontekst i Problem

LOT potrzebuje funkcjonalności podpisu odręcznego. Sprawdzono pole typu "podpis standardowy" i okazało się, że realizuje to, czego chce LOT, czyli podpis odręczny. Kwestia tylko odpowiedniej konfiguracji.

### Zidentyfikowane Ryzyka

Nie zidentyfikowano.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ✅ Zatwierdzone

Pole typu "podpis standardowy" działa dla potrzeb LOT-u. Wymaga tylko odpowiedniej konfiguracji.

**Szczegóły techniczne:**
- Pole typu "podpis standardowy" już istnieje w systemie
- Konfiguracja wymagana do pełnej funkcjonalności

### Zadania

- **[Lukasz Bott]:** Sprawdzenie i konfiguracja pola "podpis standardowy" dla LOT-u

### Punkty otwarte

- [DO USTALENIA]

---

## 2. Użycie employeeId z systemów kadrowych w regułach

**Projekt:** `Klienci/LOT`

### Kontekst i Problem

Z zewnętrznego systemu kadrowego przychodzi identyfikator pracownika (`employeeId`), który nie jest jego loginem w AD ani e-mailem. Ten atrybut jest synchronizowany do profilu użytkownika w AMODIT. W regule chcielibyśmy przypisać do pola typu "Użytkownik" osobę na podstawie tego właśnie numeru pracowniczego, który ktoś wprowadził na formularzu. Obecnie, gdy przychodzi numer pracownika, musimy robić dodatkowe mapowanie.

### Zidentyfikowane Ryzyka

- Brak obsługi warunków brzegowych (co się stanie, jak użytkownika nie znajdzie) może powodować błędy

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Funkcja `FindUserInAD` | Znalezienie użytkownika AMODIT na podstawie zewnętrznego ID przez wyszukanie w atrybucie AD | ✅ Wybrana – funkcja już istnieje, wystarczy wiedzieć w którym atrybucie AD jest employeeId |
| Cykliczna synchronizacja z AD do lokalnego źródła danych | Raz dziennie pobieranie potrzebnych atrybutów z AD i odczyt z lokalnego źródła (rozwiązanie użyte w WIM) | ❌ Odrzucona – niepotrzebne dla tego przypadku, `FindUserInAD` wystarczy |

### Decyzja

**Status:** ✅ Zatwierdzone

Użycie funkcji `FindUserInAD` do znalezienia użytkownika AMODIT na podstawie zewnętrznego ID (`employeeId`). Funkcja zwraca login użytkownika, jeśli atrybut jest unikalny. Numer pracowniczy do loginu jest jeden do jednego (lepsze niż adres e-mail, bo ktoś może mieć kilka kont).

**Szczegóły techniczne:**
- Funkcja: `FindUserInAD`
- Atrybut AD: `employeeId` (lub odpowiedni atrybut zawierający numer pracowniczy)
- Zwracana wartość: login użytkownika
- Wymagane: obsługa warunków brzegowych (co się stanie, jak użytkownika nie znajdzie)

### Zadania

- **[Lukasz Bott]:** Napisanie fragmentu skryptu (jedna-dwie linijki) z użyciem `FindUserInAD` i obsługą warunków brzegowych

### Punkty otwarte

- [DO USTALENIA]

---

## 3. Podgląd szablonów PDF/DOCX na sprawie

**Projekt:** `cross-cutting/Interfejs-sprawy/Podglad-szablonow`

### Kontekst i Problem

Biznesowy cel: użytkownik ma 15 szablonów o nazwach "Umowa 1", "Umowa 2" itd. Musi podejrzeć, który szablon jest właściwy, zanim go wygeneruje. Chce zobaczyć szablon źródłowy (DOCX, PDF, Excel), tak samo jak da się je podejrzeć jako załączniki. Przykład użycia: regulamin, który pracownik ma oświadczyć, że się z nim zapoznał. Nie chcemy dodawać tego samego pliku jako załącznika do 1000 spraw. Zamiast tego załączamy go raz jako szablon, a pracownik może go podejrzeć, klikając na podgląd. Wtedy w całym systemie jest jeden plik.

### Zidentyfikowane Ryzyka

- Generowanie podglądu z DOCX trwa 3-4 sekundy (dla 10-stronicowego pliku to kilka sekund)
- Przy dużych plikach musi być robione przyrostowo
- Istniejące szablony nie będą miały wygenerowanego podglądu

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Podgląd surowego szablonu (bez zmapowanych wartości) | Wyświetlenie szablonu źródłowego, bez kontekstu sprawy | ✅ Wybrana – zgodnie z wymaganiami biznesowymi |
| Podgląd wypełnionego szablonu | Wyświetlenie szablonu z zmapowanymi wartościami z formularza | ❌ Odrzucona – nie jest to cel funkcjonalności |
| Zapisywanie podglądu w bazie danych | Podgląd generowany raz przy uploadzie, zapisany w bazie | ✅ Wybrana – szablonów jest ograniczona ilość (maksymalnie 100-200 nawet w dużych instalacjach), szablony są w bazie |
| Zapisywanie podglądu na dysku | Podgląd zapisany na dysku, w tabeli tylko znacznik ile stron ma podgląd | ❌ Odrzucona – szablony są w bazie, więc podgląd też w bazie |
| Generowanie podglądu dynamicznie przy każdym wywołaniu | Podgląd generowany za każdym razem | ❌ Odrzucona – trwa 3-4 sekundy, bez sensu robić to za każdym razem |
| Podgląd w pamięci podręcznej (MVP) | Podgląd generowany przy użyciu, jeśli go nie ma, zapisywany w cache | ⏸️ Odroczona – jako MVP, później rozwinięte o zapisywanie |
| Ikona podglądu obok nazwy | Dodanie ikony podglądu obok nazwy szablonu | ❌ Odrzucona – zgodność z interfejsem załączników (pod trzema kropkami) |
| Ikona podglądu pod trzema kropkami | Dodanie opcji "Podgląd" w menu pod trzema kropkami | ✅ Wybrana – zgodność z interfejsem załączników, spójny interfejs |
| Checkbox "Kliknięcie w nazwę powoduje tylko podgląd" | W ustawieniach szablonu checkbox zmieniający zachowanie kliknięcia w nazwę | ⏸️ Odroczona – do rozwinięcia później (regulaminy) |

### Decyzja

**Status:** ✅ Zatwierdzone

Dodanie funkcjonalności podglądu szablonów PDF/DOCX na sprawie. Podgląd wyświetla szablon źródłowy (surowy, bez zmapowanych wartości z formularza), bez kontekstu sprawy. Podgląd jest generowany raz, w momencie uploadu szablonu (lub przy pierwszym użyciu, jeśli nie został wygenerowany), a potem na każdej sprawie wyświetlamy ten sam, statyczny podgląd.

**Szczegóły techniczne:**
- Obsługiwane formaty: PDF, DOCX, Excel (MVP: PDF i DOCX jako najważniejsze)
- XSLT: nie interpretujemy (brak podglądu)
- Pliki tekstowe (TXT): można rozszerzyć obsługę (podgląd HTML już istnieje, można rozszerzyć na TXT)
- Lokalizacja podglądu: w menu pod trzema kropkami (zgodnie z interfejsem załączników)
- Zapisywanie: w bazie danych (szablony są w bazie, więc podgląd też)
- Generowanie: przy uploadzie szablonu (lub przy pierwszym użyciu, jeśli nie został wygenerowany)
- Istniejące szablony: podgląd generuje się przy użyciu, jeśli go nie ma
- Interfejs: przepisanie interfejsu do załączania szablonów na React (nie rozbudowywanie starego), wtedy też dołożymy podgląd

### Zadania

- **[Anna Skupinska]:** Implementacja podglądu szablonów PDF/DOCX na sprawie (MVP: PDF i DOCX jako najważniejsze)
- **[Anna Skupinska]:** Użycie tego samego mechanizmu co dla załączników (spójność)
- **[Anna Skupinska]:** Dodanie opcji "Podgląd" w menu pod trzema kropkami
- **[Zespół]:** Przepisanie interfejsu do załączania szablonów na React (później)

### Punkty otwarte

- Rozwinięcie o checkbox "Kliknięcie w nazwę powoduje tylko podgląd" dla regulaminów (później)
- Obsługa plików tekstowych (TXT) w podglądzie (rozszerzenie istniejącego podglądu HTML)
- Obsługa innych formatów plików (Excel, itp.) – promil użycia, ale można rozważyć później

---

## 4. Obsługa Oracle w nowych raportach (LIMIT)

**Projekt:** `Moduly/Modul-raportowy`

### Kontekst i Problem

W starych raportach jest specjalna obsługa generowania zapytań dla Oracle (dla `LIMIT` jest specjalna konstrukcja). W nowych raportach być może jej brakuje. Trzeba sprawdzić, jak w starym raporcie jest przekazywany `LIMIT` - jako parametr czy wklejany liczbowo w SQL. Trzeba przejrzeć cały kod do generowania zapytań dla zewnętrznych źródeł ODBC i dostosować do Oracle dla nowych raportów.

### Zidentyfikowane Ryzyka

- Brak obsługi Oracle w nowych raportach może powodować problemy z klientami używającymi Oracle (np. Rossmann)

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Trzeba sprawdzić, czy w nowych raportach jest obsługa Oracle dla `LIMIT`. Jeśli nie, trzeba przejrzeć cały kod do generowania zapytań dla zewnętrznych źródeł ODBC i dostosować do Oracle dla nowych raportów (podobnie jak było zrobione dla starych raportów).

**Szczegóły techniczne:**
- W starych raportach jest funkcja transpilująca zapytanie pod Oracle
- Dla `LIMIT` jest specjalna konstrukcja
- Trzeba sprawdzić, jak w starym raporcie jest przekazywany `LIMIT` - jako parametr czy wklejany liczbowo w SQL
- Trzeba przejrzeć cały kod do generowania zapytań dla zewnętrznych źródeł ODBC

### Zadania

- **[DO USTALENIA]:** Sprawdzenie obsługi Oracle w nowych raportach
- **[DO USTALENIA]:** Przejrzenie kodu do generowania zapytań dla zewnętrznych źródeł ODBC i dostosowanie do Oracle dla nowych raportów (wymagana współpraca z konsultantami Rossmanna, dostęp do środowiska testowego)

### Punkty otwarte

- Czy w nowych raportach jest obsługa Oracle dla `LIMIT`?
- Jak w starym raporcie jest przekazywany `LIMIT` - jako parametr czy wklejany liczbowo w SQL?
- Kto będzie mógł pracować z konsultantami Rossmanna i mieć dostęp do ich serwera?