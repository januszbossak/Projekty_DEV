[[2025-09-04 czwartek]] [[Rada architektów 2025-10-14]]

Oczywiście, oto scalone i uszczegółowione podsumowanie spotkania z 4 września 2025, przygotowane na podstawie obu dostarczonych wersji.

### Spotkanie rady architektów z dnia 4 września 2025

---

#### 1. Konfiguracja wyświetlania zadań dla współpracowników

- **Ryzyko:**
    
    - Globalne ustawienie powoduje, że zadania, w których użytkownik jest tylko współpracownikiem (a nie głównym wykonawcą), są wyświetlane na jego głównej liście "do wykonania", co prowadzi do jej nieczytelności i utrudnia pracę.
        
    - Wprowadzenie zmiany na dużej liczbie procesów u klienta poprzez modyfikację zapytań SQL może negatywnie wpłynąć na ogólną wydajność systemu.
        
- **Proponowane rozwiązanie:**
    
    - Przeniesienie możliwości konfiguracji (włącz/wyłącz pokazywanie zadań dla współpracowników na liście "do wykonania") z poziomu globalnego na poziom definicji pojedynczego procesu lub obszaru.
        
    - Technicznie, rozwiązanie polegałoby na dodaniu do zapytania SQL warunku filtrującego po identyfikatorach procesów, dla których zachowanie ma być inne (`AND CASE_PROCESS_ID IN (...)`).
        
- **Decyzja:**
    
    - Przed przygotowaniem wyceny i podjęciem ostatecznej decyzji, konieczne jest precyzyjne ustalenie, ilu procesów dotyczy potrzeba zmiany. Pozwoli to wybrać optymalne podejście techniczne (np. włączanie funkcji dla wybranych procesów zamiast jej wyłączania dla wyjątków).
        
- **Zadania:**
    
    - **Damian:** Skonsultuje się z Mateuszem w celu określenia dokładnej skali problemu i liczby procesów wymagających niestandardowych ustawień.
        

---

#### 2. Usprawnienie funkcjonalności wzmiankowania w komentarzach

- **Ryzyko:**
    
    - **Brak powiadomienia:** Użytkownik wspomniany w komentarzu po raz pierwszy nie otrzymuje dedykowanego powiadomienia mailowego o tym fakcie. Otrzymuje jedynie ogólną informację o zostaniu "obserwatorem", co jest niejasne i nieintuicyjne.
        
    - **Nadmiar powiadomień:** Automatyczne przypisanie roli "obserwatora" skutkuje subskrypcją wszystkich kolejnych powiadomień ze sprawy, co jest często niepożądane w przypadku jednorazowego zaangażowania.
        
    - **Bezpieczeństwo:** Użytkownicy mogą nieświadomie nadawać dostęp do spraw poufnych, wzmiankując osoby, które nie powinny mieć do nich wglądu, i nie otrzymując przy tym żadnego ostrzeżenia.
        
- **Proponowane rozwiązanie:**
    
    - **Zmiana roli:** Osoba wzmiankowana powinna domyślnie otrzymywać rolę "czytelnik" (`reader`), która zapewnia dostęp do odczytu sprawy, ale nie subskrybuje dalszych powiadomień mailowych.
        
    - **Dedykowany email:** Należy wprowadzić wysyłkę jasnego powiadomienia mailowego informującego bezpośrednio o wzmiance w komentarzu. Mail powinien być wysłany tylko przy pierwszej wzmiance.
        
    - **Inteligentne nadawanie roli:** Uprawnienia `reader` powinny być nadawane tylko wtedy, gdy użytkownik nie posiada jeszcze żadnego dostępu do danej sprawy.
        
    - **Ostrzeżenie w interfejsie:** Dodać komunikat ostrzegawczy informujący użytkownika, że wzmiankowanie osoby spoza grona uprawnionych nada jej dostęp do sprawy.
        
- **Decyzja:**
    
    - Funkcjonalność zostanie przebudowana zgodnie z proponowanymi rozwiązaniami, aby była bardziej intuicyjna, bezpieczna i konfigurowalna. Wdrożone zostanie wysyłanie powiadomienia o samej wzmiance, bez automatycznego dodawania użytkownika do obserwatorów.
        
- **Zadania:**
    
    - **Damian:** Przygotuje szczegółowy opis wymagań dla nowej, przebudowanej logiki wzmiankowania.
        

---

#### 3. Weryfikacja i poprawa mechanizmu historii aktywności i uprawnień

- **Ryzyko:**
    
    - **Logowanie "Edycji sprawy":** System stale rejestruje zdarzenie "edycja sprawy", które jest ukrywane w interfejsie. Generuje to nadmiarowe dane i niejasność co do celu tego mechanizmu.
        
    - **Niespójność uprawnień administratora:** W widoku historii uprawnień system błędnie informuje, że administrator posiada dostęp, nawet jeśli na poziomie procesu został on jawnie zablokowany. Stwarza to mylne wrażenie, choć faktyczny dostęp jest poprawnie ograniczony.
        
- **Proponowane rozwiązanie:**
    
    - Należy zweryfikować hipotezę, że logowanie "edycji sprawy" służy jako znacznik czasu do zapisu stanu uprawnień, co umożliwia działanie funkcji "sprawdź, kto miał uprawnienia na dany moment".
        
    - Zmodyfikować logikę wyświetlania historii uprawnień tak, aby poprawnie uwzględniała regułę blokady dostępu dla administratora zdefiniowaną na procesie.
        
- **Decyzja:**
    
    - Należy zbadać powiązanie logowania edycji z historią uprawnień. Jeśli hipoteza się potwierdzi, mechanizm zostanie zachowany.
        
    - Zidentyfikowany błąd w prezentacji uprawnień administratora musi zostać naprawiony, aby zapewnić spójność informacji.
        
- **Zadania:**
    
    - **Piotr:** Zbada kod i potwierdzi, czy zapis zdarzenia "edycja sprawy" jest niezbędny do działania historii uprawnień, oraz zgłosi i naprawi błąd w wyświetlaniu dostępu administratora.
        

---

#### 4. Rozwój funkcji operacji na źródłach danych (Source get/set)

- **Ryzyko:**
    
    - Funkcjonalność jest niekompletna i w fazie projektowej, co blokuje jej wykorzystanie przez klientów, którzy już o nią aktywnie pytają.
        
- **Proponowane rozwiązanie:**
    
    - Kompleksowe dokończenie implementacji poprzez przebudowę istniejących źródeł danych na nowy, elastyczny typ `dynamic field`.
        
    - Wprowadzenie nowego typu źródła `dynamic`, który pozwoli użytkownikom na ręczne dodawanie i edytowanie wierszy oraz kolumn bezpośrednio z poziomu interfejsu, bez konieczności importowania pliku (np. CSV, XLSX).
        
- **Decyzja:**
    
    - Zadanie zostaje przyjęte do realizacji. Projekt interfejsu i logiki zostanie przygotowany na następny sprint, a implementacja rozpocznie się, gdy tylko zwolnią się zasoby deweloperskie.
        
- **Zadania:**
    
    - **Damian:** Zaprojektuje kompletny interfejs oraz logikę działania dla nowego typu źródła danych `dynamic`.
        
    - **Anna:** Podejmie się implementacji funkcjonalności po zakończeniu bieżących zadań i finalizacji projektu.
        

---

#### 5. Spontaniczna zmiana koloru interfejsu

- **Ryzyko:**
    
    - U części zespołu domyślny kolor interfejsu aplikacji został samoczynnie nadpisany na czerwony, co wprowadza zamieszanie i może świadczyć o głębszym błędzie w systemie ustawień.
        
- **Proponowane rozwiązanie:**
    
    - Zdiagnozowano, że problem może wynikać z błędu wprowadzonego podczas migracji ustawień systemowych do nowej technologii (React), który mógł trwale zapisać nieprawidłową wartość koloru w konfiguracji.
        
- **Decyzja:**
    
    - Należy sprawdzić logi systemowe w poszukiwaniu przyczyny. Jeśli problem nie leży po stronie lokalnej konfiguracji, błąd musi zostać zgłoszony do pilnej naprawy (hotfix).
        
- **Zadania:**
    
    - **Łukasz:** Zweryfikuje logi aktywności administracyjnej i, jeśli nie znajdzie tam przyczyny, zgłosi błąd jako hotfix.