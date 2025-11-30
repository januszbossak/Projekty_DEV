[[2025-09-22 poniedziałek]]
[[2025-10-06 Sprint review]]

### Sprint review z dnia 22 września 2025

---

#### 1. Matryca uprawnień

- **Dlaczego to robimy**
    - Celem było rozwinięcie funkcjonalności matrycy uprawnień, znacząca poprawa jej wydajności oraz wprowadzenie nowych ułatwień dla administratorów, takich jak tryb kompaktowy i globalne uprawnienia domyślne dla pól.

- **Opis funkcjonalności / rozwiązania:**
    - Zmieniono sposób prezentacji uprawnień – wizualne kontrolki typu "select" zastąpiono lżejszymi ikonami, co drastycznie skróciło czas ładowania matrycy.
    - Wprowadzono nową, ujednoliconą nawigację (zakładki) do szybkiego przełączania się między edytorem graficznym, starą listą pól a nową matrycą uprawnień.
    - Dodano filtry, które pozwalają na ograniczenie widoku matrycy tylko do wybranych etapów procesu, co ułatwia pracę przy dużych procesach.
    - Wprowadzono "tryb kompaktowy", który zwęża kolumny, aby na ekranie mieściło się więcej informacji.
    - Dodano nową kolumnę "Domyślne", która pozwala zdefiniować uprawnienie dla pola na wszystkich etapach procesu jednym kliknięciem. Poszczególne etapy dziedziczą to ustawienie, chyba że zostanie dla nich zdefiniowany wyjątek.
    - Wyjątki od uprawnienia domyślnego są wizualnie oznaczane ikoną gwiazdki.
    - Dziedziczenie uprawnień z nadrzędnej sekcji lub tabeli jest oznaczane ikoną łańcucha.
    - Zaimplementowano możliwość masowej zmiany uprawnień dla wielu zaznaczonych pól jednocześnie.

- **Dalsze kroki:**
    - Zostanie przeprowadzona dyskusja i konsultacje z zespołem wdrożeniowym na temat wizualnego przedstawienia dziedziczenia i wyjątków, gdyż obecne rozwiązanie (wiele ikon) może być nieczytelne.
    - Rozważone zostanie dodanie wyszukiwarki/filtra po nazwach pól.
    - Zostanie dodana możliwość przełączania widoku nazw pól i etapów między wersją techniczną a wyświetlaną (np. polską). Sugeruje się, aby ten przełącznik był globalny dla wszystkich zakładek edytora procesu.
    - W oknie masowej edycji uprawnień, domyślna opcja w liście wyboru zostanie zmieniona z "Wybierz uprawnienie" na "Nie zmieniaj" lub "Pozostaw bez zmian", aby było jasne, że brak wyboru dla danego etapu nie spowoduje zresetowania istniejących uprawnień.

---

#### 2. Raporty systemowe i filtry

- **Dlaczego to robimy**
    - Przebudowa sposobu prezentacji i działania raportów systemowych w celu zwiększenia ich czytelności i wydajności.

- **Opis funkcjonalności / rozwiązania:**
    - Raporty systemowe będą prezentowane w formie dashboardów z zakładkami, grupującymi powiązane ze sobą analizy.
    - Część źródeł danych dla raportów systemowych będzie działać w trybie "lokalnym" – dane będą agregowane i przeliczane raz na dobę (w godzinach nocnych), co znacząco przyspieszy ich ładowanie.
    - Wprowadzono nową funkcjonalność, która pozwala zdefiniować dla raportu domyślny, obowiązkowy filtr (np. data z ostatnich 7 dni). Raport nie wyświetli żadnych danych, dopóki użytkownik nie ustawi wartości w wymaganym filtrze, co zapobiega przypadkowemu ładowaniu ogromnych, niefiltrowanych zbiorów danych.

- **Dalsze kroki:**
    - Planowane jest wprowadzenie mechanizmu tłumaczeń dla nazw kolumn w źródłach danych, aby cały interfejs raportu (łącznie z nagłówkami tabel) był spójny językowo.
    - Planowane jest dodanie możliwości definiowania aliasów dla kolumn, co pozwoli na bardziej opisowe nazwy, zwłaszcza w przypadku pól z agregacją (np. "Liczba spraw" zamiast "COUNT(ID)").

---

#### 3. Amodit Security Checklist

- **Dlaczego to robimy**
    - Stworzenie formalnego potwierdzenia, że w instalacji on-premise u klienta wdrożono zalecane standardy bezpieczeństwa. Ma to na celu uniknięcie powtarzających się zgłoszeń tych samych luk w kolejnych pen-testach.

- **Opis funkcjonalności / rozwiązania:**
    - Zostanie przygotowany dokument "checklista bezpieczeństwa", bazujący na wewnętrznych wytycznych.
    - Przed produkcyjnym uruchomieniem systemu, kierownicy projektu po stronie klienta i dostawcy będą musieli podpisać checklistę, potwierdzając, które zabezpieczenia zostały wdrożone, a które świadomie pominięte.

- **Dalsze kroki:**
    - Prace nad finalizacją checklisty i wdrożenie jej jako standardowego elementu procesu wdrożeniowego.

---

#### 4. Logowanie do Trust Center

- **Dlaczego to robimy**
    - Usprawnienie i uproszczenie dostępu serwisowego do dokumentów w Trust Center, tak aby pracownicy wsparcia technicznego nie musieli być dodawani jako administratorzy w każdej organizacji klienta z osobna.

- **Opis funkcjonalności / rozwiązania:**
    - Dodano możliwość logowania do panelu administracyjnego Trust Center za pomocą konta Microsoft (OAuth).
    - System weryfikuje, czy adres e-mail logującego się użytkownika znajduje się na centralnej, wewnętrznej liście kont serwisowych. Jeśli tak, użytkownik uzyskuje dostęp administracyjny do dokumentu, do którego posiada link, bez potrzeby bycia formalnie przypisanym do organizacji klienta.

- **Dalsze kroki:**
    - Należy utrzymywać i kontrolować listę osób uprawnionych do dostępu serwisowego, aby zapewnić, że jest ona ograniczona tylko do autoryzowanych pracowników.

---

#### 5. Strona wylogowania

- **Dlaczego to robimy**
    - Ułatwienie użytkownikowi powrotu do ekranu logowania po zakończeniu sesji w systemie.

- **Opis funkcjonalności / rozwiązania:**
    - Na stronie, która wyświetla się po poprawnym wylogowaniu, dodano wyraźny przycisk/link "Logowanie", który przekierowuje z powrotem do strony logowania.

- **Dalsze kroki:**
    - Funkcjonalność została zaimplementowana.

---

#### 6. Ujednolicenie logowania i wylogowania

- **Dlaczego to robimy**
    - Zapewnienie spójnego i przewidywalnego zachowania sesji użytkownika w całym systemie, zwłaszcza w kontekście współistnienia starego i nowego interfejsu (React).

- **Opis funkcjonalności / rozwiązania:**
    - Wylogowanie się w jednej zakładce przeglądarki automatycznie kończy sesję i wylogowuje użytkownika we wszystkich innych otwartych zakładkach z aplikacją.
    - Mechanizm poprawnie obsługuje scenariusze z automatycznym logowaniem (SSO), aby zapobiec sytuacji, w której użytkownik jest natychmiast ponownie logowany po akcji wylogowania.

- **Dalsze kroki:**
    - Funkcjonalność została zaimplementowana.

---

#### 7. Komunikator

- **Dlaczego to robimy**
    - Kontynuacja prac nad rozwojem i stabilizacją modułu komunikatora.

- **Opis funkcjonalności / rozwiązania:**
    - W trakcie sprintu zrealizowano kilkanaście zgłoszeń dotyczących poprawek w komunikatorze.

- **Dalsze kroki:**
    - Prezentacja finalnej wersji komunikatora zostanie odłożona do momentu ukończenia ostatnich kluczowych poprawek wizualnych.

---

#### 8. Ikonki grup w interfejsie sprawy

- **Dlaczego to robimy**
    - Poprawa czytelności interfejsu poprzez wizualne rozróżnienie między pojedynczymi użytkownikami a grupami użytkowników.

- **Opis funkcjonalności / rozwiązania:**
    - W różnych miejscach systemu (np. w oknie informacji o sprawie, na liście uprawnień) obok nazwy grupy wyświetlana jest teraz dedykowana ikona.
    - Kolor ikony grupy jest spójny z kolorystyką używaną w zakładce "Do wykonania".

- **Dalsze kroki:**
    - Należy zweryfikować i ewentualnie skorygować rozmiar ikony, aby był spójny z wysokością czcionki.
    - Wygląd ikon grup zostanie ujednolicony z ich reprezentacją w module Komunikatora.
    - 