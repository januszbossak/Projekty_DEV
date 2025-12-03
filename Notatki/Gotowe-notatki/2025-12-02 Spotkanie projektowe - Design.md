# Notatka projektowa – 2025-12-02 – Edytor formularzy (prawy panel)

**Data:** 2025-12-02
**Temat główny:** Edytor formularzy - reorganizacja prawego panelu edycji pola
**Uczestnicy:** Janusz Bossak, Kamil Dubaniowski, Łukasz Bott

**Powiązane projekty:**
- `Moduly/Edytor-procesow/Edytor-formularzy`
- `Klienci/PKF/Rejestracja-czasu-pracy` (edge case: edycja wierszy z raportów)
- `Moduly/Modul-raportowy` (problem przekrojowy dotyczący edycji danych w raportach)

---

## 1. Reorganizacja prawego panelu edycji pola – konsolidacja akcji i sekcji

**Komponent:** Edytor formularzy

### Cel i problem

Prawy panel edycji pola w edytorze formularzy ma zbyt wiele sekcji (5-6 w skrajnych przypadkach), co wymusza przewijanie i utrudnia dostęp do najważniejszych funkcji. Celem jest uproszczenie struktury przez przeniesienie akcji do górnej belki i konsolidację sekcji właściwości, aby zredukować liczbę sekcji do 3 maksymalnie.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Pozostawienie sekcji "Zarządzanie polem" | Osobna zakładka z akcjami: usuń pole, zmień typ pola | ❌ Odrzucona – niepotrzebne wydzielanie osobnej sekcji dla dwóch akcji |
| Przeniesienie akcji do nagłówka prawego panelu | Akcje "Historia pola", "Reguły pola", "Usuń pole" w górnej belce (trzy kropki) | ✅ Wybrana – spójnie z innymi widokami (tabele, raporty) |
| Zmiana typu pola przy typie w danych podstawowych | Ołówek (edycja) obok typu pola w sekcji "Dane podstawowe" | ⏸️ Odroczona – obawa o zbyt łatwy dostęp do destrukcyjnej akcji |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Przeniesienie akcji do nagłówka prawego panelu:**
- **Historia pola** – ikona w górnej belce (trzy kropki)
- **Reguły pola** – ikona w górnej belce (dla pól typu tabela)
- **Usuń pole** – ikona kosza w górnej belce (trzy kropki), na czerwono

**Zmiana typu pola:**
- Dodać informację o typie pola w sekcji "Dane podstawowe" (tylko do odczytu)
- **NIE dodawać** ołówka (edycja) obok typu – obawa o zbyt łatwy dostęp do destrukcyjnej operacji
- Zmiana typu pozostaje dostępna tylko z listy pól (zaznaczenie → akcja "Zmień typ pola" u góry)
- Kamil zgłosi Filipowi: jeśli będzie w prawym panelu, usunąć z listy

**Uzasadnienie:** Zmiana typu pola jest destrukcyjna operacja (zmiany w bazie, obciążenie serwera), więc nie powinna być łatwo dostępna (nie zachęcać do kliknięcia). Dostęp z listy pól wymaga kilku kroków, co chroni przed przypadkową zmianą.

**Szczegóły techniczne:**
- Akcje w górnej belce – spójnie z innymi widokami (tabele, raporty)
- Ikona kosza (usuń) na czerwono – wizualne wyróżnienie destrukcyjnej akcji
- Typ pola w "Dane podstawowe" – tylko do odczytu, bez edycji inline

### Ograniczenia / Poza zakresem

- Nie wprowadzamy trybu "nieopublikowane/opublikowane" dla definicji procesu (buffer zmian) – to odrębny temat do przemyślenia w przyszłości
- Nie implementujemy restrykcji dla środowiska produkcyjnego vs testowego – wymaga rozróżnienia środowisk

### Punkty otwarte

- Kamil zgłosi Filipowi: jeśli zmiana typu będzie w prawym panelu, to usunąć z listy pól
- Do przemyślenia: tryb "nieopublikowane/opublikowane" dla definicji procesu (aby zmiany nie wchodziły od razu na produkcję)

---

## 2. Zarządzanie widocznością i uprawnieniami – konsolidacja sekcji

**Komponent:** Edytor formularzy

### Cel i problem

Obecna struktura ma osobną zakładkę "Widoczność" z opcjami właściwości pola (widoczne na listach, dostępne w raportach, pole systemowe) oraz osobną akcję "Zarządzaj widocznością i uprawnieniami" (oczko). To duplikuje funkcje i zajmuje miejsce w prawym panelu. Celem jest konsolidacja tych funkcji.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Pozostawienie zakładki "Widoczność" | Osobna zakładka z opcjami właściwości | ❌ Odrzucona – niepotrzebne wydzielanie zakładki dla właściwości |
| Przeniesienie opcji widoczności do zakładki "Właściwości" | Opcje: widoczne na listach, dostępne w raportach, pole systemowe | ✅ Wybrana – to są właściwości pola, nie osobna kategoria |
| Akcja "Zarządzaj widocznością i uprawnieniami" w górnej belce | Ikona oczka w nagłówku prawego panelu | ✅ Wybrana – spójnie z innymi akcjami |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Przeniesienie opcji widoczności do zakładki "Właściwości":**
- Opcje: "Widoczne na listach", "Dostępne w raportach", "Pole systemowe"
- To są właściwości pola, więc logicznie pasują do zakładki "Właściwości pola"

**Akcja "Zarządzaj widocznością i uprawnieniami":**
- Ikona oczka w górnej belce prawego panelu (trzy kropki)
- Tooltip: "Zarządzaj widocznością i uprawnieniami"
- Otwiera okno z ustawieniami: widoczność dla ról, edycja tylko dla, wymagane/niewymagane

**Nazewnictwo:**
- Pozostaje historyczna nazwa "Widoczność i uprawnienia" (choć nie do końca precyzyjna)
- Uzasadnienie: 15 lat tak funkcjonowało, użytkownicy to znają
- "Uprawnienia" w tym kontekście: widoczność dla ról, edycja tylko dla (nie klasyczne uprawnienia)

**Szczegóły techniczne:**
- Akcja w górnej belce – ikona oczka
- Tooltip: "Zarządzaj widocznością i uprawnieniami"
- Opcje właściwości pola przeniesione do zakładki "Właściwości"

### Punkty otwarte

- Trzeba opisać sensownie wszystkie opcje właściwości (np. "Widoczne na listach" – nie jest jasne, o jakich listach chodzi)
- Weryfikacja co dokładnie robi opcja "Pole systemowe" (prawdopodobnie: ignorowane w integracjach, nie indeksowane w wyszukiwaniu)

---

## 3. Zmiana nazwy zakładki "Ustawienia" na "Właściwości"

**Komponent:** Edytor formularzy

### Cel i problem

Zakładka "Ustawienia" w prawym panelu zawiera właściwości specyficzne dla typu pola (maska dla pól tekstowych, liczba wierszy dla długiego tekstu, etc.). Nazwa "Ustawienia" jest myląca, bo cały prawy panel to już "ustawienia pola". Lepszą nazwą jest "Właściwości pola".

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Pozostawienie nazwy "Ustawienia" | Nazwa historyczna | ❌ Odrzucona – myląca w kontekście całego panelu |
| Zmiana na "Właściwości pola" | Precyzyjniejsza nazwa | ✅ Wybrana – klarownie opisuje zawartość zakładki |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Zmiana nazwy zakładki:**
- Z: "Ustawienia"
- Na: "Właściwości pola"

**Uzasadnienie:** Zakładka zawiera właściwości specyficzne dla typu pola, nie ogólne ustawienia. Nazwa "Właściwości pola" jest bardziej precyzyjna i klarowna.

**Szczegóły techniczne:**
- Zmiana nazwy zakładki w prawym panelu edycji pola

---

## 4. Wartość domyślna i Podpowiedź – lokalizacja w prawym panelu

**Komponent:** Edytor formularzy

### Cel i problem

Damian zasugerował, że "Wartość domyślna" jest rzadko używana i zajmuje miejsce w sekcji "Dane podstawowe". Kamil rozważał przeniesienie do zakładki "Właściwości", ale to by "schowało" tę opcję. "Podpowiedź" powinna pozostać w "Dane podstawowe", bo jest podstawową daną do wypełniania (pomaga użytkownikom zrozumieć pole).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Przeniesienie "Wartość domyślna" do zakładki "Właściwości" | Schowanie rzadko używanej opcji | 💡 Propozycja – można rozważyć, ale brak miejsca w "Właściwości" |
| Pozostawienie w "Dane podstawowe" | Obecna lokalizacja | ✅ Wybrana – brak lepszego miejsca |
| Usunięcie edycji "Wartość domyślna" z listy pól | Propozycja Piotra – edycja tylko z prawego panelu | ❌ Odrzucona – było tak, niech tak zostanie |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**"Wartość domyślna" i "Podpowiedź" pozostają w "Dane podstawowe":**
- Brak lepszego miejsca do przeniesienia
- "Podpowiedź" jest podstawową daną (pomaga użytkownikom)
- "Wartość domyślna" jest rzadko używana, ale jeśli przenieść do "Właściwości", to "zapadnie się" poniżej częściej używanych opcji

**Edycja "Wartość domyślna" z listy pól:**
- Pozostaje możliwość edycji z listy pół (kliknięcie w komórkę)
- Filip musi uspójnić edycję: inne wartości można pisać "z palca" i wyjść, "Wartość domyślna" wymaga zatwierdzenia
- Dla pól bez obsługi wartości domyślnej (np. static text): kursor zmienia się na "zakazany", tooltip wyjaśnia, że dla tego typu pola nie da się ustawić

**Uwaga techniczna:**
- Pole "static text" używa "Podpowiedź" jako wartości treści (to jest błąd w nazewnictwie – powinno być "Wartość domyślna", bo to właśnie wartość pola)

**Szczegóły techniczne:**
- "Wartość domyślna" i "Podpowiedź" w sekcji "Dane podstawowe"
- Edycja z listy pól – uspójnienie z innymi wartościami (Filip)

### Punkty otwarte

- Filip: uspójnić edycję "Wartość domyślna" z listy pól (inne wartości można pisać "z palca", ta wymaga zatwierdzenia)
- Filip: dla pól bez obsługi wartości domyślnej – kursor "zakazany" + tooltip

---

## 5. Edycja pól tabeli – intuicyjność wejścia do edycji

**Komponent:** Edytor formularzy

### Cel i problem

Użytkownicy (w tym dziewczyny z testów) nie wiedzieli, jak dodać nowe pole do tabeli. Próbowali kliknąć "+" w ogólnym widoku, co dodawało pole do głównego formularza, nie do tabeli. Dopiero później odkryli akcję "Edytuj pola tabeli". Celem jest zwiększenie intuicyjności wejścia do edycji pól tabeli.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Akcja "+" w ogólnym widoku dodaje do tabeli i przenosi do edycji | Propozycja dziewczyn z testów | 💡 Propozycja – bardziej intuicyjne, ale zmienia zachowanie "+" |
| Automatyczne przeniesienie do edycji tabeli po dodaniu pola typu "tabela" | Po dodaniu tabeli od razu wejście do edycji jej pól | 💡 Propozycja – intuicyjne, ale traci się moment nadania nazwy |
| Akcja na liście (hover) do wejścia do tabeli | Najeżdżanie na tabelę wyświetla akcję "Wejdź do edycji pól" | 💡 Propozycja – może być bardziej intuicyjne, ale drag&drop nadal problematyczny |
| Przeniesienie przycisku "Edytuj pola tabeli" ponad sekcje | Przycisk pełny z tekstem ponad wszystkimi sekcjami prawego panelu | ✅ Wybrana – wyróżnienie akcji, zachowanie jako przycisk z tekstem |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Akcja "Edytuj pola tabeli":**
- Pozostaje jako pełny przycisk z tekstem (NIE tylko ikona)
- Przeniesiony ponad wszystkie sekcje prawego panelu (na samej górze, ale w obrębie panelu, nie w belce tytułowej)
- Uzasadnienie: wejście do tabeli jest specyficzną i częstą akcją, więc przycisk z tekstem jest bardziej intuicyjny niż ikona

**Inne propozycje odroczone:**
- Automatyczne przeniesienie do edycji tabeli po dodaniu pola typu "tabela" – odroczone, bo traci się moment nadania nazwy (Przemek czeka na backend, aby zapytać o nazwę systemową)
- Akcja na liście (hover) – odroczone, drag&drop nadal problematyczny

**Szczegóły techniczne:**
- Przycisk "Edytuj pola tabeli" ponad wszystkie sekcje prawego panelu
- Pełny przycisk z tekstem (nie ikona)

### Punkty otwarte

- Przemek czeka na backend: okienko pytające o nazwę systemową pola po dodaniu
- Do przemyślenia: automatyczne przeniesienie do edycji tabeli po dodaniu pola typu "tabela" (gdy będzie okienko z nazwą)
- Do przemyślenia: intuicyjność dodawania pola do tabeli (akcja "+" w ogólnym widoku vs wejście do tabeli)

---

## 6. Edycja GUID pola – zabezpieczenie destrukcyjnej akcji

**Komponent:** Edytor formularzy

### Cel i problem

Piotrek wymusił możliwość edycji GUID pola (obecnie tylko kopiowanie). To jest bardzo rzadka i specyficzna akcja (kopiowanie GUID-ów z testowego na produkcyjne środowisko). Musi być dostępna, ale nie łatwo dostępna (zabezpieczenie przed przypadkową zmianą).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Inline edycja GUID (jak obecnie dla innych pól) | Kliknięcie w GUID pozwala edytować | ❌ Odrzucona – zbyt łatwy dostęp do destrukcyjnej akcji |
| Przycisk "Edytuj" z oknem modalnym i ostrzeżeniem | Ikona ołówka obok GUID, okno z ostrzeżeniem i potwierdzeniem | ✅ Wybrana – zabezpieczenie przed przypadkową zmianą |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Edycja GUID pola:**
- GUID w sekcji "Informacje techniczne" – tylko do odczytu
- Ikona kopiowania obok GUID (zachowana, jak dla Field Name)
- **Ikona ołówka (edycja) obok GUID** – otwiera okno modalne z ostrzeżeniem
- Okno modalne: wyświetla starą wartość GUID, pole do wpisania nowej, ostrzeżenie, potwierdzenie

**Zabezpieczenia:**
- Edycja uzależniona od ustawienia systemowego (domyślnie wyłączone)
- Ikona ołówka pojawia się tylko gdy ustawienie włączone
- Okno modalne z ostrzeżeniem i potwierdzeniem

**Szczegóły techniczne:**
- Ikona kopiowania (jak dla Field Name) – po lewej
- Ikona ołówka (edycja) – po prawej (jeśli ustawienie systemowe włączone)
- Okno modalne: stara wartość GUID, pole nowej wartości, ostrzeżenie, potwierdzenie

---

## 7. Kolejne kroki projektowe – właściwości pól

**Komponent:** Edytor formularzy

### Cel i problem

Następne spotkania Design mają skupić się na szczegółach właściwości dla poszczególnych typów pól. Kamil planuje przegląd pod kątem: (1) nazewnictwa właściwości – czy są jasne i intuicyjne, (2) kolejności właściwości – najważniejsze na górze, rzadko używane na dole, (3) instrukcji/tooltipów – wyjaśnienie co robi każda właściwość.

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja – plan pracy na kolejne spotkania Design

**Plan pracy:**
1. **Wyróżnienie prawego panelu** – praca nad layoutem, aby prawy panel był bardziej wyróżniony (nie przez kolory, tylko układ)
2. **Nazewnictwo właściwości** – przegląd wszystkich właściwości pól, weryfikacja czy nazwy są jasne i intuicyjne
3. **Kolejność właściwości** – analiza które właściwości są najczęściej używane (na górę), które rzadko (na dół)
4. **Instrukcje i tooltipy** – dodanie opisów do właściwości, aby admin rozumiał co robi każda opcja

**Przykłady do poprawy:**
- "Widoczne na listach" – nie jest jasne, o jakich listach chodzi
- "Pole systemowe" – brak opisu co to robi

**Szczegóły techniczne:**
- Przegląd pole po polu
- Ocena "na oko" i na podstawie doświadczenia zespołu

---

## 8. Edge case: edycja wierszy tabel w raportach (PKF)

**Komponent:** Moduł raportowy

### Cel i problem

PKF zgłosił potrzebę edycji wierszy tabel z poziomu raportu osadzonego na sprawie. Przykład: raport wyświetla wiersze z tabel z różnych spraw (rejestracja czasu pracy z kilku dni), użytkownik chce zbiorczo edytować te wiersze (korekta godzin, zmiana projektów). Obecny system nie obsługuje edycji danych w raportach – tylko wyświetlanie.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Uproszczone okienka modalne do edycji wiersza tabeli | Wyświetlanie formularza wiersza tabeli w oknie modalnym z raportu | 💡 Propozycja – teoretycznie możliwe (formularz wiersza istnieje), ale szeroki temat |
| Edycja w trybie Excelowym (inline editing) | Edycja wierszy bezpośrednio w raporcie (jak w Excelu) | 💡 Propozycja – trudne dla reguł i zależności między polami |
| Edycja przez Excel (Get Excel Data / Set Excel Data) | Eksport do Excela, edycja, import z powrotem | ❌ Odrzucona – nie ma funkcji Set Excel Data, gimnastyka dla użytkownika |

### Decyzja / Sposób realizacji

**Status:** ⏸️ Odroczone – temat do dyskusji na Radzie Architektów, nie do realizacji w ciągu kilku dni

**Uzasadnienie odłożenia:**
- Temat jest bardzo szeroki, wymaga przemyślenia wielu aspektów
- Edycja danych w raportach to złożony problem (reguły, walidacje, zależności między polami)
- Nie ma obecnie sensownego pomysłu na implementację
- Dla PKF znaleziono obejścia (gimnastyka, ale działa)

**Pomysły do rozważenia w przyszłości:**
- Uproszczone okienka modalne do edycji wiersza tabeli (formularz wiersza istnieje, teoretycznie da się wyświetlić)
- Problem: reguły, zależności, walidacje – jak to obsłużyć w kontekście edycji z raportu?

**Szczegóły techniczne:**
- Funkcja Get Excel Data istnieje, Set Excel Data NIE istnieje
- Formularz wiersza tabeli istnieje (czasami wyświetla się przy błędach)

### Punkty otwarte

- Temat do dyskusji na Radzie Architektów lub osobnym spotkaniu Design
- Nie do realizacji w ciągu kilku dni – wymaga głębszej analizy i koncepcji

---

## Punkty do dalszej dyskusji (globalne)

- **Tryb "nieopublikowane/opublikowane" dla definicji procesu** – buffer zmian, aby edycje nie wchodziły od razu na produkcję (dotyczy zmian typu pola i innych destrukcyjnych operacji)
- **Edycja danych w raportach** (PKF) – szerszy temat do Rady Architektów
- **Zmiana klucza w procesie typu rejestr** – Łukasz zgłosił, że w nowym interfejsie nie ma możliwości zmiany klucza (możliwy błąd, do weryfikacji)
