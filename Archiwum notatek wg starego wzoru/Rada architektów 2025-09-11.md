[[2025-09-11 czwartek]] [[Rada architektów 2025-10-14]]


### Spotkanie Rady Architektów z dnia 11 września 2025

---

#### 1. Rozszerzenie funkcji `callRest` o obsługę `multipart/form-data`

- **Ryzyko:**
    
    - Obecna implementacja funkcji `callRest` nie pozwala na wysyłanie wielu plików w jednym żądaniu, co jest konkretnym wymaganiem klienta (Marba) i staje się coraz częstszą potrzebą w kontekście integracji (np. z KSeF).
        
    - Ręczne budowanie złożonych żądań `multipart/form-data` w regułach biznesowych (np. przez konkatenację stringów) jest niewydajne, zasobożerne i podatne na błędy.
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzić natywne wsparcie dla wysyłania danych w formacie `multipart/form-data` w ramach funkcji `callRest`.
        
    - Implementacja powinna opierać się na mechanizmie szablonów, podobnym do tego, który jest już używany do dynamicznego definiowania nagłówków (`headers`). Umożliwi to zdefiniowanie listy plików i innych danych do wysłania w ramach jednego parametru, bez potrzeby skomplikowanego kodowania w regułach.
        
- **Decyzja:**
    
    - Funkcjonalność musi zostać zrealizowana do końca września ze względu na zobowiązania wobec klienta. Zastosowane zostanie podejście oparte na szablonach.
        
    - Rozwiązanie to jest dedykowane dla formatu `multipart/form-data`; kwestia obsługi wysyłania wielu plików w formacie JSON zostaje odłożona do czasu pojawienia się konkretnego zapotrzebowania biznesowego.
        
- **Zadania:**
    
    - **Piotr:** Przeanalizuje szczegółowo propozycję techniczną Adriana dotyczącą implementacji.
        
    - **Damian:** Przygotuje osobne zgłoszenie opisujące przyszłą potrzebę obsługi wysyłania wielu plików w formacie JSON, aby zaplanować tę pracę w przyszłości.
        

---

#### 2. Problemy z działaniem e-Doręczeń dla klientów chmurowych

- **Ryzyko:**
    
    - Krytyczna funkcjonalność e-Doręczeń nie działa poprawnie, co powoduje narastającą frustrację kluczowych klientów chmurowych i stwarza ryzyko utraty wizerunku firmy.
        
    - Diagnostyka problemu jest blokowana przez brak efektywnego wsparcia technicznego ze strony Poczty Polskiej.
        
    - Brak transparentnej komunikacji na temat statusu prac i istniejących problemów sprawia, że klienci czują się ignorowani.
        
- **Proponowane rozwiązanie:**
    
    - Kontynuacja prac analitycznych i naprawczych po stronie kodu aplikacji z najwyższym priorytetem.
        
    - Należy poinformować klientów, aby sami eskalowali problem u swoich opiekunów handlowych w Poczcie Polskiej, co może przyspieszyć reakcję dostawcy usługi.
        
    - Konieczne jest natychmiastowe zaktualizowanie statusu prac w wewnętrznych kanałach komunikacyjnych, aby zapewnić, że wszystkie zaangażowane strony są świadome sytuacji.
        
- **Decyzja:**
    
    - Adrian kontynuuje prace nad rozwiązaniem problemu. Jednocześnie kluczowe jest usprawnienie komunikacji wewnętrznej i zewnętrznej, aby prawidłowo zarządzać oczekiwaniami klientów.
        
- **Zadania:**
    
    - **Adrian:** Przekaże Danielowi Reszce szczegółowe informacje na temat statusu prac i istniejących blokad, aby mógł on odpowiednio komunikować się z klientami.
        

---

#### 3. Poprawa czytelności historii zmian w sprawie

- **Ryzyko:**
    
    - W historii sprawy zmiany w polach formularza są zapisywane z użyciem ich nazw technicznych (np. `field_123`), które są często niezrozumiałe dla użytkowników biznesowych.
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzić natychmiastową, prostą poprawkę. W widoku historii, zamiast nazwy technicznej pola, będzie wyświetlana jego aktualna nazwa wyświetlana, z uwzględnieniem wersji językowej zalogowanego użytkownika.
        
    - Aby zachować jednoznaczność, jeśli nazwa techniczna różni się od wyświetlanej, zostanie ona pokazana w `tooltipie` (dymku) po najechaniu kursorem na nazwę pola.
        
- **Decyzja:**
    
    - Poprawka zostanie wdrożona natychmiast, ponieważ jest to szybkie i skuteczne rozwiązanie, które znacząco poprawia czytelność historii dla użytkowników końcowych.
        
- **Zadania:**
    
    - **Piotr:** Wdroży opisaną zmianę zaraz po spotkaniu i uzupełni kryteria akceptacji dla zadania.
        

---

#### 4. Mechanizm statycznych komunikatów systemowych dla użytkowników

- **Ryzyko:**
    
    - Brak jest skutecznego, wbudowanego narzędzia do informowania wszystkich użytkowników o ważnych wydarzeniach, takich jak planowane przerwy techniczne, co prowadzi do nieporozumień.
        
- **Proponowane rozwiązanie:**
    
    - Należy dokończyć i dostosować istniejący, częściowo zaimplementowany mechanizm, który pozwalał na wyświetlanie globalnych komunikatów.
        
    - Funkcjonalność powinna zostać zintegrowana z nowym interfejsem (React) i wyświetlać komunikat w formie zamykanego paska na górze ekranu po zalogowaniu.
        
    - Zarządzanie komunikatami powinno być scentralizowane dla środowisk chmurowych, a dla instalacji on-premise – dostępne z poziomu interfejsu dla lokalnego administratora.
        
- **Decyzja:**
    
    - Temat jest ważny i należy go zrealizować. W pierwszej kolejności konieczne jest zbadanie obecnego stanu implementacji i przygotowanie założeń do dalszych prac.
        
- **Zadania:**
    
    - **Ania:** Przeprowadzi research istniejącego rozwiązania, spisze jego aktualne możliwości oraz ograniczenia i przygotuje rekomendacje, co będzie podstawą do dalszych prac projektowych.
        

---

#### 5. Zapis stanu checkboxów w raporcie osadzonym

- **Ryzyko:**
    
    - Istnieje potrzeba biznesowa (klient WIN), aby w raporcie osadzonym na sprawie umożliwić interakcję z danymi (zaznaczanie checkboxów) i trwałe zapisywanie tego stanu. Obecne raporty osadzone nie posiadają takiej możliwości.
        
- **Proponowane rozwiązanie:**
    
    - Rozbudować funkcjonalność raportów osadzonych o możliwość dodania edytowalnej kolumny (np. z kontrolką typu checkbox), której stan będzie zapisywany w kontekście sprawy.
        
- **Decyzja:**
    
    - Koncepcja została zaakceptowana. Należy przeprowadzić dalszą analizę techniczną i przygotować Proof of Concept (PoC), aby zweryfikować wykonalność.
        
- **Zadania:**
    
    - **Piotr:** Przeanalizuje techniczną wykonalność i złożoność implementacji.
        
    - **Damian:** Szczegółowo opisze wymagania i przygotuje PoC rozwiązania.
        

---

#### 6. Usprawnienia interfejsu edytora formularzy

- **Ryzyko:**
    
    - Obecny układ przełączników widoków ("Edytor graficzny", "Lista") oraz selektora formularzy w edytorze jest nieintuicyjny i zajmuje cenną przestrzeń roboczą na ekranie.
        
- **Proponowane rozwiązanie:**
    
    - Przełączanie głównych widoków ("Edytor graficzny", "Lista", docelowo "Matryca uprawnień") zostanie zrealizowane za pomocą zakładek (tabów).
        
    - Selektor wyboru formularza (główny/tabela) pozostanie jako rozwijana lista umieszczona bezpośrednio nad obszarem roboczym.
        
    - Wprowadzona zostanie funkcja trybu "pełnoekranowego" dla edytora, która ukryje zbędne elementy interfejsu i zmaksymalizuje przestrzeń do pracy.
        
- **Decyzja:**
    
    - Zmiany w układzie zostaną wdrożone. Tryb pełnoekranowy jest kluczowym elementem, który ma zostać dostarczony w wersji wrześniowej.
        
- **Zadania:**
    
    - **Kamil:** Przekaże Przemkowi decyzję o pozostawieniu selektora formularza nad obszarem roboczym oraz zleci implementację trybu pełnoekranowego.