# Notatka projektowa – 2025-11-18 – Ulepszanie filtrów użytkownika w raportach

**Data:** 2025-11-18
**Temat główny:** Ulepszanie filtrów użytkownika w raportach.

---

> 🛡️ Zweryfikowano przez Note Reviewer: poniedziałek, 8 grudnia 2025

## Powiązane projekty
- Moduly/Modul-raportowy/Filtry-uzytkownika
- Moduly/Modul-raportowy/Wydajnosc

---

## 1. Filtry pól tekstowych (np. "Nazwisko", "Kod")



### Cel i problem
Poprawa wydajności i użyteczności filtrów tekstowych, które obecnie wykonują nieindeksowane wyszukiwanie "LIKE %...%" na dużych zbiorach danych, co jest nieoptymalne. Filtry podpowiadają wartości tylko z pierwszych 20 rekordów, zamiast ze wszystkich dostępnych danych.

### Zidentyfikowane Ryzyka
- Problemy wydajnościowe przy wyszukiwaniu na dużych bazach danych.
- Niska użyteczność filtra (brak podpowiadania faktycznie istniejących wartości).

### Rozważane alternatywy
| Opcja | Opis | Status |
|-------|------|--------|
| `SELECT DISTINCT` (tymczasowo) | Zastosowanie `SELECT DISTINCT` na całym zbiorze danych dla filtra, a nie tylko na pierwszych 20 rekordach, w celu poprawy wyświetlania wartości. | ✅ Wybrana – doraźna poprawka, rozwiązuje problem wyświetlania, ale nie wydajności. |
| Mechanizm indeksowania | Wdrożenie dedykowanego mechanizmu indeksowania pól (np. Lucene, JSON w tabeli Case) dla pól, po których ma być możliwe wyszukiwanie. | 💡 Propozycja – rozwiązanie długoterminowe, adresujące wydajność. |

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone (doraźnie) / 💡 Propozycja (docelowo)

- **Doraźnie:** Mateusz ma poprawić mechanizm pobierania wartości do filtrów, aby używał `SELECT DISTINCT` na całym zbiorze danych (po stronie backendu), a nie tylko na pierwszych 20 rekordach.
- **Docelowo:** Należy zaimplementować mechanizm indeksowania pól, który umożliwi wyszukiwanie na dużych zbiorach danych bez obciążania systemu. Opcja "Zaindeksuj" dla pól będzie dostępna dla twórcy raportu w ustawieniach filtra. Indeks powinien wspierać wyszukiwanie od początku frazy, ewentualnie w środku (do ustalenia).

### Zadania
- **Mateusz Kisiel:** Stworzyć buga i zaimplementować doraźną poprawkę dla filtrów (zwiększenie limitu >20 lub usunięcie limitu i `DISTINCT` po stronie backendu). Podpiąć pod epic "Ulepszanie filtrów użytkownika" (ID 20153).
- **Mateusz Kisiel / Przemysław Rogaś:** Wysłuchać nagrania z Rady Developerów (część o filtrach i wydajności), aby zrozumieć kontekst problemu i docelowe rozwiązania.

---

## 2. Filtry pól słownikowych (małe vs duże słowniki)


### Cel i problem
Dostosowanie logiki wyświetlania wartości w filtrach pól słownikowych w zależności od ich rozmiaru. Dwie sprzeczne sytuacje:
- Małe słowniki (np. A, B, C): powinny wyświetlać wszystkie opcje, nawet jeśli nie ma ich w raporcie.
- Duże słowniki (np. 10 000 klientów): powinny wyświetlać tylko wartości występujące w raporcie, aby uniknąć przeładowania listy.
Obecnie filtry traktują oba przypadki tak samo, często pokazując tylko wartości z pierwszych 20 rekordów.

### Rozważane alternatywy
Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji
**Status:** 💡 Propozycja

Należy wypracować mechanizm rozróżniający wyświetlanie wartości w filtrach słownikowych, uwzględniający liczbę dostępnych pozycji w słowniku i w raporcie, aby zapewnić optymalne UX i wydajność.

### Punkty otwarte
- Zdefiniowanie progów dla "małych" i "dużych" słowników.
- Określenie, czy mechanizm ma działać automatycznie, czy być konfigurowalny.

---

## 3. Funkcjonalność "Zaznacz wszystko" w filtrach


### Cel i problem
Przycisk "Zaznacz wszystko" w filtrach obecnie zaznacza tylko pierwsze 20 widocznych elementów, wprowadzając użytkownika w błąd, że zaznaczył wszystkie dane.

### Rozważane alternatywy
Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- Zmiana nazwy przycisku z "Zaznacz wszystko" na **"Zaznacz widoczne"**.
- W przyszłości rozważenie opcji "Zaznacz wszystko" z uwzględnieniem paginacji/doładowywania danych.

### Zadania
- **Przemysław Rogaś:** Zaimplementować zmianę nazwy przycisku na "Zaznacz widoczne".

---

## 4. Uporządkowanie filtra pola "Data"


### Cel i problem
Operatorzy filtra daty są nieuporządkowani. Najczęściej używane opcje biznesowe (np. "bieżący miesiąc", "poprzedni miesiąc") powinny być na górze listy, a zaawansowane opcje (np. "nie wcześniej niż", "zakres od-do") niżej.

### Rozważane alternatywy
Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- Uporządkowanie kolejności operatorów daty w filtrze, priorytetyzując opcje biznesowe.
- Nadanie odpowiednich, czytelnych nazw operatorom.

### Zadania
- **Przemysław Rogaś:** Uporządkować kolejność operatorów daty i ich nazewnictwo w filtrach.

---

## 5. Komunikaty o wymaganych filtrach ("Empty State Screen")


### Cel i problem
Raporty z pustymi danymi lub wymagające podania filtrów (np. obszaru, projektu) wyświetlają mało informatywny "brak danych" na środku pustego ekranu, co jest nieużyteczne dla użytkownika.

### Rozważane alternatywy
| Opcja | Opis | Status |
|-------|------|--------|
| Ilustracje Kristiny | Wykorzystanie istniejących ilustracji Kristiny. | 💡 Propozycja |
| Mockupowe elementy | Wizualne wskazówki (np. pusty wykres, kolumny tabeli z komunikatem "brak danych"). | 💡 Propozycja |

### Decyzja / Sposób realizacji
**Status:** 💡 Propozycja

Należy wypracować angażujące i informatywne "empty state screens" dla wszystkich typów raportów, które jasno komunikują przyczynę braku danych i zachęcają do podjęcia akcji (np. "Wprowadź pierwszą umowę", "Wprowadź filtry, aby zobaczyć dane").

### Zadania
- **Przemysław Rogaś:** Zaproponować wizualne rozwiązania dla "empty state screens" dla raportów.

---

## Punkty do dalszej dyskusji (globalne)

- Kontynuacja zbierania use case'ów i dopisywanie ich do epicu "Ulepszanie filtrów użytkownika" (ID 20153).
- Janusz udostępni dokument z use case'ami Mateuszowi i Przemkowi.
- Weryfikacja podejścia do "zaznacz wszystko" dla dużych zbiorów danych (z uwzględnieniem paginacji).
