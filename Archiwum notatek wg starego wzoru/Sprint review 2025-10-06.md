[[2025-10-06 Sprint review]] [[2025-10-06 poniedziałek]]

### Sprint review z dnia 6 października 2025

---

#### 1. Logi systemowe

- **Dlaczego to robimy**
    
    - Celem było odświeżenie strony logów systemowych i przeniesienie jej na nową technologię (React), jako ostatniego elementu systemu, który tego wymagał.
        
- **Opis funkcjonalności / rozwiązania:**
    
    - Strona logów systemowych została w pełni przebudowana, zyskując nowy, spójny z resztą systemu wygląd.
        
    - Zachowano dotychczasowy podział na zakładki: Logi systemowe, Aktywność administracyjna oraz Kolejka maili do wysłania.
        
    - Wprowadzono zmianę w działaniu filtrów i wyszukiwania – ze względów wydajnościowych aktywują się one dopiero po kliknięciu przycisku „Zastosuj”.
        
    - Zmieniono mechanizm eksportu logów. Zamiast globalnego eksportu całej widocznej strony, użytkownik może teraz zaznaczyć konkretne, interesujące go logi i tylko je wyeksportować.
        
    - W zakładce „Aktywność administracyjna” wyświetlane są teraz szczegóły zarejestrowanej zmiany.
        
    - W zakładce „Kolejka maili” dodano nową funkcjonalność pozwalającą na ręczne usuwanie wiadomości z kolejki, co jest przydatne np. podczas testów, aby uniknąć masowej wysyłki maili po ponownym uruchomieniu mechanizmu.
        
- **Dalsze kroki:**
    
    - Należy naprawić funkcję kopiowania pojedynczego logu, tak aby do schowka trafiały wszystkie jego szczegóły (m.in. URL, użytkownik), a nie tylko sama treść.
        
    - W widoku szczegółów logu należy dodać brakujące pole z adresem URL.
        
    - Konieczna jest weryfikacja mechanizmu rejestrowania zmian w „Aktywności administracyjnej”, ponieważ obecnie zapisywane są zdarzenia, w których nie doszło do żadnej faktycznej modyfikacji (tzw. zmiany "null na null").
        
    - W zakładce „Kolejka maili” należy dodać informację o planowanej dacie wysyłki dla każdego maila.
        
    - Należy zaimplementować mechanizm obsługi tzw. maili poufnych, których treść nie powinna być widoczna z poziomu logów.
        

---

#### 2. Komunikator

- **Dlaczego to robimy**
    
    - Celem było dokończenie prac nad komunikatorem, poprawa jego spójności wizualnej z resztą systemu oraz dodanie nowych funkcjonalności.
        
- **Opis funkcjonalności / rozwiązania:**
    
    - Prace nad komunikatorem zostały w dużej części ukończone.
        
    - Ujednolicono wygląd elementów wizualnych, takich jak awatary użytkowników, czcionki i ogólny układ okna konwersacji, aby były spójne z całym systemem i bardziej czytelne.
        
    - Zaimplementowano możliwość tworzenia konwersacji prywatnych (z jedną osobą) oraz grupowych (z wieloma osobami).
        
- **Dalsze kroki:**
    
    - Należy dodać w interfejsie tzw. ścieżkę (breadcrumbs) dla komunikatora.
        
    - Proces tworzenia konwersacji zostanie uproszczony – typ konwersacji (prywatna lub grupowa) będzie automatycznie definiowany na podstawie liczby wybranych uczestników.
        
    - Planowane jest dodanie funkcjonalności pozwalającej na tworzenie konwersacji na podstawie składu istniejących grup użytkowników w systemie.
        

---

#### 3. Edytor procesów (diagramy i formularze)

- **Dlaczego to robimy**
    
    - Wprowadzenie usprawnień w edytorze procesów, które zwiększą bezpieczeństwo modyfikacji oraz poprawią komfort pracy projektantów.
        
- **Opis funkcjonalności / rozwiązania:**
    
    - **Wyszukiwarka pól:** W edytorze formularza dodano wyszukiwarkę, która pozwala szybko odnaleźć pole po jego nazwie systemowej lub wyświetlanej.
        
    - **Bezpieczna edycja:** Wprowadzono dodatkowe zabezpieczenia przy krytycznych zmianach. Zarówno zmiana typu pola, jak i zmiana przypisanego do niego słownika, wymagają teraz zaznaczenia przez użytkownika checkboxa potwierdzającego świadomość potencjalnego ryzyka (np. utraty danych).
        
    - **Usprawnienia interfejsu:** W polach do definiowania tłumaczeń (np. nazw pól) wyświetlane są teraz dynamiczne podpowiedzi (placeholdery) z wartością z domyślnego języka, co ułatwia pracę.
        
    - **Edytor HTML:** Zmieniono sposób edycji pól statycznych. Edytor HTML otwiera się teraz w dedykowanym, większym oknie modalnym, co ułatwia pracę z obszernymi treściami.
        
    - **Diagram procesu:** Stworzono fundament pod nowy, graficzny edytor diagramów. Obecnie umożliwia on wizualizację etapów i tworzenie między nimi połączeń. Linie ciągłe oznaczają istniejące, działające przejścia, natomiast przerywane – przejścia dopiero planowane.
        
- **Dalsze kroki:**
    
    - Należy poprawić wizualne odstępy między ikonami a etykietami w górnym menu edytora.
        
    - Trzeba ujednolicić nazewnictwo wersji językowych (np. używać jednego "English" zamiast wariantów regionalnych).
        
    - Okno edytora HTML dla pól statycznych zostanie powiększone (zarówno na szerokość, jak i na wysokość), aby było bardziej funkcjonalne.
        
    - Należy zaimplementować w edytorze graficznym obsługę pól systemowych, których edycja (zmiana nazwy, typu) powinna być zablokowana.
        
    - Kwestia umiejscowienia reguł dla tabel wymaga dalszej analizy i podjęcia decyzji, czy powinny być dostępne wyłącznie w dedykowanej zakładce „Reguły”, czy także jako skrót w edytorze formularza.
        

---

#### 4. Podpisywanie raportów

- **Dlaczego to robimy**
    
    - Uzupełnienie nowych raportów o brakującą metodę podpisu elektronicznego (SimplySign) i optymalizacja tego procesu dla użytkownika końcowego.
        
- **Opis funkcjonalności / rozwiązania:**
    
    - W module nowych raportów dodano możliwość składania podpisu za pomocą SimplySign.
        
    - Wprowadzono mechanizm, który pozwala administratorom na skonfigurowanie, które metody podpisu mają być widoczne i dostępne dla użytkowników. Pozwoli to ukryć nieużywane w danej organizacji opcje.
        
- **Dalsze kroki:**
    
    - Należy usprawnić proces podpisywania przez SimplySign. System powinien automatycznie przekierowywać do logowania, jeśli użytkownik nie jest zalogowany, zamiast wyświetlać osobną opcję „Zaloguj”. Funkcjonalność zostanie przetestowana z użytkownikami.
        
    - Należy doprecyzować logikę działania tabel w raportach, a konkretnie momentu, w którym przy dużej liczbie kolumn powinien pojawiać się poziomy pasek przewijania.
        

---

#### 5. Aplikacja do podpisywania dokumentów na macOS

- **Dlaczego to robimy**
    
    - Stworzenie nowej, bardziej przyjaznej dla użytkownika wersji aplikacji do składania podpisów kwalifikowanych na komputerach z systemem macOS.
        
- **Opis funkcjonalności / rozwiązania:**
    
    - Nowa wersja aplikacji automatycznie wykrywa dostępne na komputerze certyfikaty i biblioteki do podpisu (obecnie wspierane są Szafir oraz SimplySign). Użytkownik nie musi już ręcznie wskazywać ścieżki do sterownika.
        
    - Zaimplementowano obsługę przypadków, w których na jednej karcie kryptograficznej znajduje się wiele kluczy prywatnych.
        
- **Dalsze kroki:**
    
    - Interfejs użytkownika zostanie gruntownie przebudowany, aby był bardziej czytelny i spójny wizualnie z wersją dla systemu Windows. Zamiast technicznych danych certyfikatu, będą wyświetlane kluczowe informacje, takie jak nazwa właściciela, wystawca i data ważności.
        
    - Zostaną przeprowadzone testy z certyfikatami od innych dostawców (np. PWPW), gdy tylko pojawi się taka techniczna możliwość.
        

---

#### 6. Logowanie do Trust Center

- **Dlaczego to robimy**
    
    - Usprawnienie procesu logowania do narzędzia Trust Center dla pracowników z uprawnieniami serwisowymi.
        
- **Opis funkcjonalności / rozwiązania:**
    
    - Dodano możliwość logowania do Trust Center za pomocą konta Microsoft (Azure AD), eliminując potrzebę ręcznego wpisywania loginu i hasła.
        
- **Dalsze kroki:**
    
    - Wygląd przycisku logowania zostanie zmieniony, aby był w pełni spójny z ekranem logowania głównej aplikacji systemu.
        

---

#### 7. Zmiana typów pól tekstowych w bazie danych

- **Dlaczego to robimy**
    
    - Rozwiązanie problemu ograniczenia długości znaków w polach krótkiego tekstu (domyślnie 255 znaków), co stanowiło problem np. przy zapisywaniu bardzo długich linków.
        
- **Opis funkcjonalności / rozwiązania:**
    
    - W narzędziu administracyjnym "Database Admin" stworzono funkcję, która generuje skrypt SQL.
        
    - Uruchomienie skryptu powoduje zmianę typu kolumn dla wszystkich pól tekstowych w bazie danych z `VARCHAR` na `MEDIUMTEXT` (dla MS SQL oraz MySQL), co radykalnie zwiększa ich pojemność i eliminuje problematyczne ograniczenie.
        
- **Dalsze kroki:**
    
    - Operacja zmiany typów pól jest czasochłonna (może trwać nawet ponad 30 minut) i wymaga pełnego wyłączenia aplikacji na czas jej trwania. Z tego powodu musi być wykonywana świadomie przez administratora, poza godzinami pracy i po uprzednim wykonaniu kopii zapasowej bazy danych. Została przygotowana odpowiednia instrukcja.