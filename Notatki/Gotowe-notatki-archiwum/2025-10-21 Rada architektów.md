> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

# Rada Architektów – 2025-10-21

**Powiązane projekty:**
- `Moduly/Eksport-import-definicji-procesow` – temat 1
- `Moduly/Silnik-regul` – tematy 2, 3
- `Moduly/Modul-raportowy` – temat 4
- `Cross-cutting/Interfejs-sprawy/Formularz-sprawy` – temat 5

---

## 1. Wyświetlanie błędów konfliktów przy imporcie procesu XML

**Projekt:** `Moduly/Eksport-import-definicji-procesow`

### Kontekst i Problem

Podczas wczytywania procesu XML procesor XML rzuca błędy konfliktów, które są wyświetlane w formie tabelki. Piotr Buczkowski wykrył 2-3 nowe konflikty i chce zmienić sposób prezentacji tych informacji. Przykładowy konflikt: pole numer 2 w importowanym procesie nadpisuje pole numer 3 w obecnym, ponieważ mają ten sam GUID. Problem dotyczy sytuacji, gdy pole zostało dodane 2 razy niezależnie na produkcji i na teście – wtedy najlepiej byłoby przypisać GUID z produkcji na teście.

### Zidentyfikowane Ryzyka

- Niezgodność danych między środowiskami (produkcja vs test) przy duplikacji pól
- Brak jasnych instrukcji dla użytkownika jak rozwiązać konflikt
- Możliwość przypadkowego nadpisania danych przy nieuwadze użytkownika

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zmiana tabelki na tekstowe informacje | Przedstawienie konfliktów w formie tekstowej z instrukcjami jak poprawić | ⏸️ Odroczona – wymaga kompleksowego przeprojektowania całego importu procesu |
| Zostawienie obecnej tabelki | Obecna forma ostrzeżeń | ✅ Wybrana – działa, wymusza zastanowienie przed kliknięciem, przypadki są rzadkie (2 razy w tygodniu) |
| Możliwość wpisania GUID na środowisku | Dodanie funkcjonalności przypisania GUID z produkcji na teście | ⏸️ Odroczona – do realizacji w ramach większego przeprojektowania importu procesu przez Filipa |

### Decyzja

**Status:** ✅ Zatwierdzone

Obecna forma wyświetlania błędów konfliktów w tabelce zostaje bez zmian. Dodane zostały 2-3 nowe ostrzeżenia, które wymuszają zastanowienie przed kliknięciem i są wystarczające na obecny moment. Kompleksowe przeprojektowanie całego importu procesu zostaje odroczone i będzie realizowane w ramach większego projektu przez Filipa, gdzie zostanie zaopiekowana możliwość przypisania GUID na środowisku.

**Szczegóły techniczne:**
- Procesor XML: wykrywanie konfliktów GUID przy imporcie
- Forma prezentacji: tabelka z konfliktami

### Zadania

- **Piotr Buczkowski:** Zostawić obecną formę wyświetlania błędów konfliktów na razie

### Punkty otwarte

- Przeprojektowanie całego importu procesu (w ramach projektu Filipa)
- Dodanie możliwości przypisania GUID na środowisku dla przypadków duplikacji pól między środowiskami

---

## 2. Zmiany w języku reguł jako DLL

**Projekt:** `Moduly/Silnik-regul`

### Kontekst i Problem

Klient pyta czy zmiany w języku reguł mogą być dostarczone jako DLL. Mariusz Piotrzkowski przedstawił temat, który był wcześniej dyskutowany z Piotrem Buczkowskim. Zmiany dotyczą mechanizmu w języku reguł, który wymagałby przekopiowania definicji parsera.

### Zidentyfikowane Ryzyka

- Naruszenie filozofii AMODIT – klienci powinni podnosić wersje, aby korzystać z nowych funkcji
- Tworzenie precedensu dla innych zmian w core'owych komponentach systemu
- Problemy z wersjonowaniem i kompatybilnością DLL
- Ryzyko fragmentacji funkcjonalności między klientami

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dostarczenie zmian jako DLL | Wgranie zmian w języku reguł jako DLL dla klienta | ❌ Odrzucona – narusza filozofię AMODIT, silnik reguł jest integralną częścią systemu, nie da się tego przenieść jako DLL |
| Wymuszenie podniesienia wersji | Klient musi podnieść wersję AMODIT, aby korzystać z nowych funkcji | ✅ Wybrana – zgodna z filozofią produktu, standardowa funkcja wymaga standardowej wersji |
| Dostarczenie jako dedykowana funkcja za opłatą | Dodanie funkcji jako dedykowanej za 10 000 zł | 💡 Rozważana – możliwe dla nietypowych integracji, ale nie dla zmian w parserze silnika reguł |

### Decyzja

**Status:** ✅ Zatwierdzone

Zmiany w języku reguł nie mogą być dostarczone jako DLL. Jest to integralna część AMODIT i wymaga podniesienia wersji przez klienta. Wyjątkiem są dedykowane funkcje za opłatą (np. nietypowe integracje), ale nie dotyczy to zmian w parserze silnika reguł. Filozofia AMODIT zakłada, że standardowe funkcje są dostępne w standardowych wersjach produktu.

**Szczegóły techniczne:**
- Silnik reguł: integralna część AMODIT, nie może być wydzielony jako DLL
- Parser reguł: wymaga aktualizacji całego systemu

### Zadania

- **Mariusz Piotrzkowski:** Poinformować klienta, że wymagane jest podniesienie wersji

### Punkty otwarte

- Jakość AMODIT i obawy klientów przed wgrywaniem nowych wersji (temat poruszony w kontekście warsztatów)

---

## 3. Funkcja DeleteAttachment nie działa dla attachmentów

**Projekt:** `Moduly/Silnik-regul`

### Kontekst i Problem

Funkcja DeleteAttachment nie działa dla attachmentów. Mariusz Piotrzkowski zidentyfikował problem na podstawie przykładu od klienta. DeleteAttachment jest bardzo starą funkcją i nie została zastosowana w niej logika z funkcji GetAttachment, która sprawdza wszystkie możliwe formy przekazania załącznika (argument, brzeg, itp.).

### Zidentyfikowane Ryzyka

- Brak spójności w obsłudze załączników między różnymi funkcjami silnika reguł
- Nieprawidłowe działanie funkcji DeleteAttachment dla niektórych form przekazania załącznika

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zastosowanie logiki z GetAttachment | Przekopiowanie logiki sprawdzania wszystkich form przekazania załącznika z GetAttachment do DeleteAttachment | ✅ Wybrana – zapewni spójność i poprawne działanie dla wszystkich form załączników |

### Decyzja

**Status:** ✅ Zatwierdzone

Funkcja DeleteAttachment powinna działać dla attachmentów tak samo jak GetAttachment. Trzeba zastosować w DeleteAttachment tę samą logikę sprawdzania wszystkich możliwych form przekazania załącznika, która jest używana w GetAttachment.

**Szczegóły techniczne:**
- DeleteAttachment: stara funkcja wymagająca aktualizacji
- GetAttachment: funkcja z poprawną logiką sprawdzania form załącznika (argument, brzeg, itp.)

### Zadania

- **Mariusz Piotrzkowski:** Utworzyć PBI (pusty item) i przypisać do Damiana Kaminskiego, wywołać w komentarzu
- **Damian Kaminski:** Zaimplementować poprawkę DeleteAttachment z logiką z GetAttachment

### Punkty otwarte

- Brak

---

## 4. Błąd pobierania danych w raportach dla użytkowników nie będących panem

**Projekt:** `Moduly/Modul-raportowy`

### Kontekst i Problem

Występuje błąd pobierania danych w raportach: "Inna liczba kolumn". Problem dotyczy użytkowników, którzy nie są administratorem i dotyczy tylko nowych raportów. Błąd występuje gdy kolumna jest widoczna tylko dla konkretnej osoby – wtedy nie działa. Gdy kolumna jest ukryta, działa OK.

### Zidentyfikowane Ryzyka

- Nieprawidłowe działanie raportów dla użytkowników z ograniczonym dostępem do kolumn
- Brak obsługi pustych wartości dla kolumn niedostępnych użytkownikowi

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zwracanie pustej wartości dla niedostępnych kolumn | Generowanie pustego stringa ('') dla kolumn, do których użytkownik nie ma dostępu | ✅ Wybrana – zapewni poprawne działanie raportów, zgodne z logiką starych raportów |

### Decyzja

**Status:** ✅ Zatwierdzone

Trzeba obsłużyć sytuację, gdy kolumna jest widoczna tylko dla konkretnej osoby. W takim przypadku należy zwracać pustą wartość (pusty string) dla użytkowników, którzy nie mają dostępu do tej kolumny. Dotyczy to tylko nowych raportów – stare raporty mają to już obsłużone.

**Szczegóły techniczne:**
- Nowe raporty: wymagają obsługi pustych wartości dla niedostępnych kolumn
- Stare raporty: już mają poprawną obsługę

### Zadania

- **Damian Kaminski:** Opisać problem i przypisać zadanie (hotfix)

### Punkty otwarte

- Brak

---

## 5. Wyświetlanie tabeli jako formularz po zmianach

**Projekt:** `cross-cutting/Interfejs-sprawy/Formularz-sprawy`

### Kontekst i Problem

Po zmianach w sposobie wyświetlania tabeli jako formularz, działanie nie jest poprawne. Mariusz Piotrzkowski przedstawił temat, który był dyskutowany w zeszłym tygodniu. Są 2 możliwości: szybkie przywrócenie starego wyglądu (powrót do starego wyświetlania tabeli jako formularz) lub przepisanie całego mechanizmu od nowa (około 10-15 lub więcej godzin pracy). Obecne rozwiązanie jest obejściem problemu, które nie podoba się Mariuszowi.

### Zidentyfikowane Ryzyka

- Nieprawidłowe działanie wyświetlania tabeli jako formularz po zmianach
- Potrzeba podjęcia decyzji między szybką poprawką a kompleksowym przepisaniem

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Powrót do starego wyglądu | Przywrócenie poprzedniego sposobu wyświetlania tabeli jako formularz | ⏸️ Odroczona – wymaga weryfikacji przez Piotra Buczkowskiego |
| Przepisanie od nowa | Kompleksowe przepisanie mechanizmu wyświetlania tabeli jako formularz | ⏸️ Odroczona – wymaga weryfikacji przez Piotra Buczkowskiego, szacunek: 10-15+ godzin |
| Wyświetlanie na tabeli zamiast na drzewach | Zmiana sposobu wyświetlania na tabeli zgodnie z Bugą | 💡 Propozycja Mariusza – wymaga weryfikacji |

### Decyzja

**Status:** 🔍 Do weryfikacji

Decyzja odroczona do weryfikacji przez Piotra Buczkowskiego. Piotr musi zobaczyć jak zostało to zrobione obecnie, aby móc podjąć decyzję między szybkim powrotem do starego wyglądu a kompleksowym przepisaniem mechanizmu. Mariusz preferuje rozwiązanie na tabeli (zgodnie z Bugą) zamiast na drzewach.

**Szczegóły techniczne:**
- Wyświetlanie tabeli jako formularz: wymaga weryfikacji obecnej implementacji
- Szacunek przepisania: 10-15+ godzin

### Zadania

- **Piotr Buczkowski:** Sprawdzić obecną implementację wyświetlania tabeli jako formularz i podjąć decyzję o dalszym podejściu

### Punkty otwarte

- Wybór między szybkim powrotem do starego wyglądu a kompleksowym przepisaniem
- Decyzja o sposobie wyświetlania (tabela vs drzewa)

