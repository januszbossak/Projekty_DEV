> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

# Rada Architektów – 2025-09-23

**Powiązane projekty:**
- `cross-cutting/GTA - dostęp tymczasowy do sparwy` – temat 1
- `Moduly/Modul-raportowy` – temat 2
- `Moduly/Modul-raportowy/Tlumaczenia-i-aliasy` – temat 2, 3
- `koncepcje/CallFunctionEx` – temat 4
- `koncepcje/RunAsUser` – temat 5
- `Moduly/Ustawienia-systemowe` – tematy 6, 7

---

## 1. GTA – automatyczne forward case dla użytkowników wewnętrznych

**Projekt:** `cross-cutting/GTA`

### Kontekst i Problem

Klient (prawdopodobnie LPP) zgłosił sugestię, że jeśli użytkownik jest użytkownikiem wewnętrznym i dodatkowo jest aktywny, to zamiast Grant Temporary Access (GTA) system powinien automatycznie wykonać forward case. Problem wynika z kontekstu biznesowego – w firmach takich jak LPP pracownicy często są pracownikami czasowymi, którzy pracują 3 miesiące, potem nie pracują, a następnie znowu się zatrudniają. Wdrożeniowcy ustawili GTA bez sprawdzania kontekstu biznesowego, co powoduje problemy.

### Zidentyfikowane Ryzyka

- Brak automatycznego rozpoznawania użytkowników wewnętrznych przy GTA
- Konieczność ręcznego sprawdzania i ustawiania forward case zamiast GTA
- Problemy z kontekstem biznesowym – pracownicy czasowi często wracają do pracy

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Automatyczne forward case dla użytkowników wewnętrznych | System automatycznie wykonuje forward case zamiast GTA dla użytkowników wewnętrznych | ❌ Odrzucona – nie jest bezpieczne, klient nie ma kasy na rozwiązanie systemowe |
| Funkcja pomocnicza do sprawdzania | Funkcja sprawdzająca czy użytkownik jest wewnętrzny, wykonywana przed regułą GTA | ✅ Wybrana – rozwiązanie dla klienta (6 miejsc), można skopiować i użyć |
| Zmiana nazwy użytkownika systemowego | Zmiana nazwy użytkownika systemowego (np. "system Józef" → "centrum transakcyjne") | ✅ Alternatywne rozwiązanie – wystarczyło w przypadku Orlenu |

### Decyzja

**Status:** ❌ Odrzucona (rozwiązanie dla klienta)

Klient nie ma kasy na rozwiązanie systemowe. Zostało zaproponowane rozwiązanie dla klienta – funkcja pomocnicza, która sprawdzi czy użytkownik jest wewnętrzny i wypisze odpowiednią akcję (GTA lub forward case). Klient ma to w 6 miejscach, więc może skopiować funkcję i użyć w każdym miejscu.

**Szczegóły:**
- Problem dotyczy konkretnego klienta (prawdopodobnie LPP)
- Kontekst biznesowy: pracownicy czasowi często wracają do pracy
- Rozwiązanie: funkcja pomocnicza wykonywana przed regułą GTA, która sprawdza czy użytkownik jest wewnętrzny
- Alternatywne rozwiązanie: zmiana nazwy użytkownika systemowego (wystarczyło w przypadku Orlenu)
- GTA działa długo u wielu klientów i nikt do tej pory takiej potrzeby nie zgłaszał
- Nie jest to bloker globalny, tylko dotyczy konkretnego klienta

**Uwaga:** Rozważano automatyczne forward case dla użytkowników wewnętrznych, ale uznano to za niebezpieczne i niepraktyczne. Klient nie ma kasy na rozwiązanie systemowe, więc otrzymał rozwiązanie do samodzielnej implementacji.

### Zadania

- **[Damian Kamiński]:** Przekazanie rozwiązania klientowi (funkcja pomocnicza) → termin: [wykonane]

### Punkty otwarte

- Czy w przyszłości pojawi się potrzeba systemowego rozwiązania dla automatycznego forward case dla użytkowników wewnętrznych?
- Czy inne klienci będą zgłaszać podobne potrzeby?

---

## 2. Aliasy w Module Raportowym – źródła zewnętrzne

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

Potrzeba dodania możliwości nadawania aliasów dla kolumn pochodzących ze źródeł zewnętrznych w raportach (podobnie jak w procesach). Temat był już dyskutowany na wcześniejszych Radach architektów.

### Zidentyfikowane Ryzyka

- Brak możliwości nadawania własnych nazw kolumnom ze źródeł zewnętrznych
- Niespójność między procesami (gdzie są aliasy) a raportami (gdzie ich nie ma)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dodanie aliasów do źródeł zewnętrznych | Możliwość nadawania aliasów dla kolumn ze źródeł zewnętrznych (podobnie jak w procesach) | ✅ Wybrana – rozwiązanie systemowe, spójne z procesami |

### Decyzja

**Status:** ✅ Zatwierdzone (już zgłoszone)

Dodanie możliwości nadawania aliasów dla kolumn pochodzących ze źródeł zewnętrznych w raportach. Temat został już zgłoszony i jest w realizacji.

**Szczegóły:**
- Mechanizm analogiczny do aliasów w procesach
- Możliwość nadawania własnych nazw kolumnom ze źródeł zewnętrznych
- Temat był już dyskutowany na wcześniejszych Radach architektów
- Zgłoszenie już istnieje i jest w realizacji

### Zadania

- **[Łukasz Bott]:** Rozbicie tematu na drobniejsze zadania → termin: [do ustalenia]

### Punkty otwarte

- Brak – temat jest już w realizacji

---

## 3. Tłumaczenia agregacji w raportach

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

Tłumaczenia agregacji (count → liczba, suma → suma) w raportach zostały już zaimplementowane. Łukasz sprawdzi czy działa na developie.

### Zidentyfikowane Ryzyka

- Brak – funkcjonalność już zaimplementowana

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ✅ Zatwierdzone (już zaimplementowane)

Tłumaczenia agregacji w raportach zostały już zaimplementowane. Po stronie backendu raportu agregacje były już przetłumaczone (suma, liczba), ale nie wyświetlały się prawidłowo przy opisach. Poprawka została wykonana.

**Szczegóły:**
- Agregacje są już przetłumaczone (count → liczba, suma → suma)
- Wyświetlanie zostało poprawione (na osi poziomej już jest "liczba" zamiast "count")
- Łukasz sprawdzi czy działa na developie

### Zadania

- **[Łukasz Bott]:** Weryfikacja działania tłumaczeń agregacji na developie → termin: [do ustalenia]

### Punkty otwarte

- Brak – funkcjonalność już zaimplementowana

---

## 4. CallFunctionEx – odroczenie

**Projekt:** `koncepcje/CallFunctionEx`

### Kontekst i Problem

Funkcja CallFunctionEx została zaproponowana w kontekście wprowadzenia czwartego typu procesów (biblioteka). Temat nie jest krytyczny i nikt o to nie pędzi.

### Zidentyfikowane Ryzyka

- Brak – temat nie jest krytyczny

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Realizacja w obecnym sprincie | Wdrożenie funkcji CallFunctionEx | ❌ Odrzucona – nie jest krytyczne, są ważniejsze tematy |
| Odroczenie | Przeniesienie tematu na później | ✅ Wybrana – temat nie jest krytyczny, są ważniejsze tematy |

### Decyzja

**Status:** ⏸️ Odroczone

Funkcja CallFunctionEx została odroczona. Temat nie jest krytyczny i nikt o to nie pędzi. Są ważniejsze tematy do realizacji (np. integracja z nowym systemem).

**Szczegóły:**
- Funkcja została zaproponowana w kontekście wprowadzenia czwartego typu procesów (biblioteka)
- Temat nie jest krytyczny
- Nikt o to nie pędzi
- Są ważniejsze tematy do realizacji
- Temat został odroczony do przyszłych Rad architektów

### Zadania

- **[Product Owner]:** Rozważenie tematu CallFunctionEx na przyszłych Radach architektów → termin: [do ustalenia]

### Punkty otwarte

- Czy funkcja CallFunctionEx jest potrzebna w kontekście procesów typu biblioteka?
- Kiedy temat powinien być rozważony ponownie?

---

## 5. Run As User – pomysł do przemyślenia

**Projekt:** `koncepcje/RunAsUser`

### Kontekst i Problem

Pojawił się pomysł dodania funkcji "Run As User" zamiast "Run As System". Kontekst biznesowy: klienci chcą z reguły czasowej przekazywać sprawę jako konkretny użytkownik (np. "pokój pocztowy") zamiast jako system (np. "system Józef"). Obecnie trzeba zmieniać nazwę użytkownika systemowego, co jest niepraktyczne.

### Zidentyfikowane Ryzyka

- Brak możliwości przekazywania sprawy jako konkretny użytkownik z reguły czasowej
- Konieczność zmiany nazwy użytkownika systemowego zamiast użycia konkretnego użytkownika

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dodanie funkcji Run As User | Nowa funkcja "Run As User" zamiast "Run As System" | 🔍 Do przemyślenia – podobny pomysł jak poprzedni, wymaga analizy |
| Zmiana nazwy użytkownika systemowego | Zmiana nazwy użytkownika systemowego (np. "system Józef" → "centrum transakcyjne") | ✅ Alternatywne rozwiązanie – wystarczyło w przypadku Orlenu i innych klientów |

### Decyzja

**Status:** 🔍 Do przemyślenia

Pomysł dodania funkcji "Run As User" wymaga przemyślenia. Podobny pomysł jak poprzedni (GTA) – niekoniecznie musi być przyjęty przez wszystkich. Alternatywne rozwiązanie (zmiana nazwy użytkownika systemowego) wystarczyło w przypadku Orlenu i innych klientów.

**Szczegóły:**
- Kontekst biznesowy: przekazywanie sprawy jako konkretny użytkownik (np. "pokój pocztowy") zamiast jako system (np. "system Józef")
- Alternatywne rozwiązanie: zmiana nazwy użytkownika systemowego (wystarczyło w przypadku Orlenu – "centrum transakcyjne", Łukasz używa "przedstawiciel systemu AMODIT")
- Pomysł podobny do poprzedniego (GTA) – niekoniecznie musi być przyjęty przez wszystkich
- Temat został odroczony do przyszłych Rad architektów

**Uwaga:** Rozważano czy funkcja "Run As User" jest potrzebna dla zwykłych użytkowników, czy powinna pozostać "Run As System" z możliwością podania loginu użytkownika systemowego. Uznano, że lepiej dodać oddzielną funkcję "Run As User" jeśli zajdzie taka potrzeba.

### Zadania

- **[Product Owner]:** Rozważenie tematu Run As User na przyszłych Radach architektów → termin: [do ustalenia]

### Punkty otwarte

- Czy funkcja "Run As User" jest potrzebna, czy wystarczy zmiana nazwy użytkownika systemowego?
- Czy inne klienci będą zgłaszać podobne potrzeby?
- Jak różni się "Run As User" od "Run As System" z loginem użytkownika systemowego?

---

## 6. Parametry systemowe – par_modified_by_id

**Projekt:** `cross-cutting/Ustawienia-systemowe`

### Kontekst i Problem

Łukasz zauważył, że kolumna `par_modified_by_id` w tabeli `parameters` nie jest wypełniana dla większości parametrów. Kolumna jest wypełniana tylko w sytuacji, gdy wykorzystywany jest mechanizm czterech oczu. Łukasz chciałby, żeby kolumna była zawsze wypełniana, aby można było szybko zobaczyć kto ostatnio edytował parametr (szybki audyt).

### Zidentyfikowane Ryzyka

- Brak możliwości szybkiego audytu zmian parametrów (kto ostatnio edytował)
- Konieczność sprawdzania historii w UserActivity zamiast bezpośredniego odczytu z tabeli parameters

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zawsze wypełniać par_modified_by_id | Wypełnianie kolumny par_modified_by_id zawsze przy dodawaniu/modyfikacji parametru | ❌ Odrzucona – nie mieszamy z mechanizmem czterech oczu, historia jest w UserActivity |
| Sprawdzanie historii w UserActivity | Używanie historii aktywności użytkowników do sprawdzania zmian parametrów | ✅ Wybrana – istniejący mechanizm, nie mieszamy z mechanizmem czterech oczu |

### Decyzja

**Status:** ❌ Odrzucona

Nie mieszamy kolumny `par_modified_by_id` z mechanizmem czterech oczu. Historia zmian parametrów jest dostępna w UserActivity (aktywność administracyjna), więc nie ma potrzeby duplikowania tej informacji w tabeli `parameters`.

**Szczegóły:**
- Kolumna `par_modified_by_id` jest częścią mechanizmu czterech oczu
- Nie należy mieszać tej kolumny z innymi celami (szybki audyt)
- Historia zmian parametrów jest dostępna w UserActivity (aktywność administracyjna)
- Kolumna `par_accepted_by_id` również jest częścią mechanizmu czterech oczu
- Kolumna `par_new_value` również istnieje i może być wyświetlana

**Uwaga:** Rozważano dodanie nowej kolumny dla szybkiego audytu, ale uznano, że nie ma potrzeby duplikowania informacji, która już jest dostępna w UserActivity.

### Zadania

- Brak – temat odrzucony

### Punkty otwarte

- Brak – temat odrzucony

---

## 7. Rejestracja zmian parametrów kolorów w aktywności administracyjnej

**Projekt:** `cross-cutting/Ustawienia-systemowe`

### Kontekst i Problem

Łukasz zauważył, że zmiany 2 parametrów odpowiadających za zmiany kolorów w raportach nie są rejestrowane w aktywności administracyjnej. Parametry te powinny być rejestrowane podobnie jak inne zmiany parametrów systemowych.

### Zidentyfikowane Ryzyka

- Brak śladu audytowego dla zmian parametrów kolorów
- Niespójność w rejestrowaniu zmian parametrów systemowych

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rejestracja zmian parametrów kolorów | Dodanie rejestracji zmian parametrów kolorów w aktywności administracyjnej | ✅ Wybrana – poprawa spójności rejestrowania zmian |

### Decyzja

**Status:** ✅ Zatwierdzone (zgłoszenie)

Dodanie rejestracji zmian parametrów kolorów w aktywności administracyjnej. Łukasz zgłosi temat jako osobne zgłoszenie.

**Szczegóły:**
- 2 parametry odpowiadające za zmiany kolorów w raportach nie są rejestrowane w aktywności administracyjnej
- Wymagana weryfikacja wszystkich okienek, gdzie coś się zmienia, aby sprawdzić czy mechanizm rejestracji działa prawidłowo
- Możliwe, że przy wprowadzaniu mechanizmu rejestracji nie sprawdzono wszystkich miejsc, gdzie parametry są zmieniane

### Zadania

- **[Łukasz Bott]:** Zgłoszenie tematu rejestracji zmian parametrów kolorów w aktywności administracyjnej → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Weryfikacja mechanizmu rejestracji zmian parametrów we wszystkich okienkach → termin: [do ustalenia]

### Punkty otwarte

- Czy są inne parametry, które nie są rejestrowane w aktywności administracyjnej?
- Czy mechanizm rejestracji działa prawidłowo we wszystkich miejscach, gdzie parametry są zmieniane?

