[[2025-09-16 wtorek]] [[Rada architektów 2025-10-14]]

### Spotkanie Rady Architektów z dnia 16 września 2025

---

#### 1. Edytor Formularzy - Problem z obsługą "pól pustych"

- **Ryzyko:**
    
    - W nowym edytorze formularzy użytkownicy nie mogą edytować ani zarządzać uprawnieniami dla "pól pustych", które są celowo dodawane jako placeholdery w celu zachowania sztywnego układu formularza.
        
    - Obecna logika edytora, która automatycznie przesuwa pola z niższych wierszy w górę, aby wypełnić puste miejsce, zaburza strukturę wizualną. Użytkownicy obchodzą ten problem, dodając właśnie "pola puste" jako separatory, co obecnie jest niemożliwe.
        
    - Backend nie zwraca informacji o "polach pustych", co uniemożliwia ich obsługę na froncie. Gwałtowna zmiana tej logiki mogłaby negatywnie wpłynąć na setki istniejących wdrożeń.
        
- **Proponowane rozwiązanie:**
    
    - **Krótkoterminowe (MVP):** Przywrócenie starej logiki działania. Należałoby dodać "Pole puste" jako typ pola do wyboru z listy i wyświetlać je na formularzu w sposób umożliwiający zarządzanie (edycję uprawnień, usuwanie), tak jak każdym innym polem.
        
    - **Długoterminowe (Nowa logika):** Całkowita przebudowa mechanizmu, tak aby operacje (np. ukrywanie) odbywały się w obrębie wiersza, a nie całego formularza. Koncepcje obejmują "grupowanie pól" lub "blokowanie wierszy", co zapobiegłoby "wskakiwaniu" pól z niższych wierszy w puste miejsca.
        
- **Decyzja:**
    
    - Ze względu na złożoność, problem obsługi "pól pustych" nie zostanie rozwiązany w najbliższym, "czerwcowym" wydaniu.
        
    - Wdrożenie nowej, długoterminowej logiki opartej na wierszach zostaje odroczone i wymaga osobnych spotkań projektowych.
        
    - Do czasu wdrożenia docelowego rozwiązania, użytkownicy powinni zarządzać skomplikowanymi formularzami w starym, listowym edytorze.
        
- **Zadania:**
    
    - **Kamil:** Poinformować Mateusza Kołakowskiego o decyzji wstrzymania prac nad tym zagadnieniem i o konieczności korzystania z widoku listy.
        
    - **Janusz:** Zlecić Przemkowi naprawę błędu polegającego na tym, że edytor nie zapamiętuje ustawionego układu kolumn po przejściu do widoku listy i z powrotem.
        

---

#### 2. Bezpieczeństwo - Dane poufne w nazwach plików wysyłanych przez Trust Center

- **Ryzyko:**
    
    - Nazwy plików wysyłane w treści wiadomości SMS przez Trust Center mogą zawierać dane poufne (np. imię i nazwisko), co stwarza ryzyko ich wycieku, jeśli odbiorca nie jest uprawniony.
        
- **Proponowane rozwiązanie:**
    
    - Ujednolicić działanie wysyłki SMS i e-mail. W obu kanałach komunikacji powinna być wykorzystywana "przyjazna nazwa pliku", jeśli została zdefiniowana w procesie.
        
    - Odpowiedzialność za zapewnienie, że "przyjazna nazwa" nie zawiera danych poufnych, spoczywa na osobie konfigurującej proces.
        
- **Decyzja:**
    
    - Należy zweryfikować, czy mechanizm wysyłki SMS w Trust Center już teraz wykorzystuje "przyjazną nazwę pliku".
        
    - Należy opracować i zakomunikować konsultantom dobre praktyki dotyczące konfigurowania "przyjaznych nazw", aby unikać umieszczania w nich danych wrażliwych.
        
- **Zadania:**
    
    - **Łukasz:** Sprawdzić u Marka, czy "przyjazna nazwa pliku" jest już obecnie używana w SMS-ach, jeśli została zdefiniowana.
        
    - **Łukasz:** Przygotować i przekazać konsultantom wytyczne dotyczące bezpiecznego stosowania "przyjaznych nazw plików".
        

---

#### 3. Błąd (Hotfix) - Nieprawidłowe działanie automatycznego wylogowania

- **Ryzyko:**
    
    - Gdy użytkownik jest zalogowany w dwóch zakładkach przeglądarki i wyloguje się w jednej, druga zakładka nie odświeża swojego stanu. Pozostaje widoczny interfejs aplikacji, ale sesja jest nieaktywna, a każda kolejna akcja powoduje błąd.
        
    - Jest to krytyczny problem z perspektywy bezpieczeństwa, który był już wcześniej zgłaszany w ramach pentestów.
        
- **Proponowane rozwiązanie:**
    
    - Należy natychmiast naprawić błąd, tak aby wylogowanie w jednej zakładce skutkowało pełnym wylogowaniem (np. przekierowaniem do strony logowania) we wszystkich pozostałych aktywnych zakładkach aplikacji.
        
- **Decyzja:**
    
    - Błąd ma najwyższy priorytet i musi zostać naprawiony jako hotfix w bieżącym sprincie, przed opublikowaniem nowej wersji.
        
- **Zadania:**
    
    - **Janusz:** Pilnie przypisać zadanie naprawy błędu (na podstawie zgłoszenia 21974) do Przemka.
        

---

#### 4. Funkcjonalność - Globalne komunikaty systemowe dla użytkowników

- **Ryzyko:**
    
    - Brak jest scentralizowanego mechanizmu do informowania wszystkich użytkowników o ważnych wydarzeniach systemowych, takich jak planowane prace konserwacyjne, zwłaszcza w instalacjach on-premise.
        
- **Proponowane rozwiązanie:**
    
    - **Dla chmury:** Wykorzystać istniejący, ale nieużywany w nowym interfejsie mechanizm i przywrócić jego działanie na froncie.
        
    - **Dla on-premise:** Stworzyć nową funkcjonalność, np. poprzez dodanie pola w ustawieniach systemowych lub rozbudowanie modułu powiadomień o specjalny typ "powiadomienia systemowego", które byłoby wyświetlane jako pasek na górze strony.
        
    - **Biznesowe:** Przygotować wycenę funkcjonalności i przedstawić ją kluczowym klientom (np. LPP, Rossmann) w celu pozyskania finansowania na jej rozwój.
        
- **Decyzja:**
    
    - Funkcjonalność jest potrzebna i zostanie zrealizowana po uzyskaniu finansowania od zainteresowanych klientów.
        
- **Zadania:**
    
    - **Łukasz:** Przejąć temat, przygotować wycenę i skontaktować się z klientami w sprawie potencjalnego sfinansowania prac.
        

---

#### 5. Błąd - Problem z usuwaniem sprawy nadrzędnej

- **Ryzyko:**
    
    - System blokuje możliwość usunięcia sprawy nadrzędnej, jeśli jest z nią powiązana sprawa podrzędna, która została wcześniej usunięta (i ma status `is_hidden=true`). Logika usuwania nie uwzględnia spraw ukrytych, co prowadzi do błędu spójności referencyjnej w bazie danych.
        
- **Proponowane rozwiązanie:**
    
    - Zmodyfikować proces usuwania tak, aby przed skasowaniem sprawy nadrzędnej poprawnie obsługiwał (odpinał) również relacje ze sprawami podrzędnymi o statusie `is_hidden`.
        
- **Decyzja:**
    
    - Problem jest jasno zdefiniowany i wiadomo, jak go naprawić. Zadanie zostanie przypisane do realizacji w kolejnym sprincie.
        
- **Zadania:**
    
    - **Łukasz:** Przypisać zadanie do Piotra na następny sprint w celu szczegółowej analizy i przygotowania opisu rozwiązania.
        

---

#### 6. Analiza wydajności bazy danych dla klienta

- **Ryzyko:**
    
    - Klient zgłasza poważne problemy z wydajnością systemu, w tym długo wykonujące się reguły i nadmierne obciążenie bazy danych, co negatywnie wpływa na jego pracę.
        
- **Proponowane rozwiązanie:**
    
    - Przeprowadzić płatną, dwudniową analizę środowiska klienta w celu zdiagnozowania źródła problemów.
        
    - W analizę, oprócz Piotra, zaangażować drugą osobę (propozycja: Łukasz Grodzki) w celu transferu wiedzy w zespole.
        
- **Decyzja:**
    
    - Analiza zostanie przeprowadzona zgodnie z zaakceptowaną przez klienta ofertą. Celem jest zdiagnozowanie problemu i przygotowanie raportu z rekomendacjami.
        
- **Zadania:**
    
    - **Damian:** Skontaktować Piotra z Danielem (opiekunem klienta) w celu ustalenia harmonogramu i szczegółów analizy.
        

---

#### 7. Ustalenia organizacyjne - Proces zgłaszania błędów

- **Ryzyko:**
    
    - Zgłoszenia błędów i sugestii dla nowych modułów są obecnie rozproszone, co utrudnia ich śledzenie, prowadzi do duplikacji i tworzy wąskie gardła.
        
- **Proponowane rozwiązanie:**
    
    - Ustanowić dedykowane kanały na Microsoft Teams dla poszczególnych modułów i projektów (np. "Edytor procesów", "Moduł raportowy").
        
    - Każdy zgłoszony na kanale temat powinien być walidowany przez wyznaczonego opiekuna (Product Ownera) lub zespół projektowy.
        
- **Decyzja:**
    
    - Oficjalną ścieżką zgłaszania błędów i sugestii stają się dedykowane kanały na Teams.
        
- **Zadania:**
    
    - **Wszyscy:** Nowe błędy i uwagi należy zgłaszać na odpowiednich, dedykowanych kanałach projektowych na MS Teams.