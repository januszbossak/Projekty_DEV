[[Rada architektów 2025-10-14]] [[2025-09-18 czwartek]]
#### 1. Ujednolicenie i uproszczenie komunikatów w formularzach

- **Ryzyko:**
    - Obecny sposób tworzenia stylizowanych komunikatów dla użytkowników w polach statycznych wymaga ręcznego pisania kodu HTML, co jest nieefektywne, czasochłonne i podatne na błędy.

- **Proponowane rozwiązanie:**
    - Stworzenie nowej funkcji w mechanizmie reguł, np. `CreateCallout(tekst, styl)`, która będzie generować odpowiednio ostylowany komunikat.
    - Funkcja przyjmowałaby dwa parametry: treść komunikatu oraz predefiniowany styl (np. 'info', 'warning', 'danger').
    - Wynik działania funkcji byłby przypisywany do pola typu `static text` w formularzu.
    - W przyszłości rozważone zostaną dodatkowe usprawnienia:
        - Możliwość umieszczania pól statycznych w pojedynczej kolumnie (obecnie zajmują całą szerokość formularza).
        - Opcja wyboru predefiniowanego stylu bezpośrednio w ustawieniach pola statycznego, co eliminowałoby konieczność tworzenia reguły dla stałych komunikatów (np. instrukcji).

- **Decyzja:**
    - W najbliższym sprincie zostanie zaimplementowana funkcja `CreateCallout` jako rozwiązanie MVP (Minimum Viable Product).
    - Komunikat będzie wyświetlany na pełnej szerokości pola statycznego, w którym się znajduje.
    - Pozostałe proponowane usprawnienia (szerokość kolumny, ustawienia w polu) zostają odłożone na przyszłość.

- **Zadania:**
    - **Ania:** Implementacja nowej funkcji `CreateCallout` w mechanizmie reguł.
    - **Łukasz:** Zaktualizowanie opisu zadania o szczegółowe ustalenia techniczne i przyjęty format działania funkcji.

---

#### 2. Problem z działaniem wykresu Gantta

- **Ryzyko:**
    - Zgłoszono bliżej nieokreślony problem dotyczący funkcjonalności wykresu Gantta.

- **Proponowane rozwiązanie:**
    - Nie przedstawiono konkretnych propozycji rozwiązania. Zauważono, że ekspertem w tym obszarze jest Marek.

- **Decyzja:**
    - Zadanie nie jest traktowane jako krytyczne (hotfix) i zostaje odroczone. Nie będzie realizowane w najbliższym czasie.

- **Zadania:**

---

#### 3. Kontrola dostępu do reguł uruchamianych z poziomu raportów

- **Ryzyko:**
    - Użytkownicy w interfejsie raportów mogą widzieć opcję uruchomienia reguły, do której wykonania nie posiadają uprawnień, co może być mylące. Nie stanowi to jednak luki bezpieczeństwa, ponieważ system i tak blokuje wykonanie takiej akcji na poziomie serwera.

- **Proponowane rozwiązanie:**
    - Dodanie w konfiguracji reguły opcji (checkbox) "Dostępna w raportach". Domyślnie byłaby ona odznaczona dla nowych reguł, a zaznaczona dla wszystkich istniejących, aby zapewnić kompatybilność wsteczną.

- **Decyzja:**
    - Obecne zabezpieczenia są wystarczające. Wprowadzenie proponowanego usprawnienia zostaje odroczone i będzie zrealizowane w ramach przyszłej, kompleksowej przebudowy interfejsu zarządzania regułami.

- **Zadania:**

---

#### 4. Konieczność wdrożenia nowego mechanizmu uwierzytelniania dla SharePoint

- **Ryzyko:**
    - Microsoft wycofuje wsparcie dla mechanizmu uwierzytelniania ACS z dniem 2 kwietnia 2026 roku. Po tej dacie obecna integracja z SharePoint przestanie działać.

- **Proponowane rozwiązanie:**
    - Należy zaprojektować i zaimplementować nowy, docelowy mechanizm oparty o OAuth.
    - Konieczne jest stworzenie generycznego interfejsu w ustawieniach systemowych do zarządzania wieloma konfiguracjami połączeń (podobnego do istniejących dla poczty przychodzącej), co ułatwi obsługę różnych aplikacji i środowisk.

- **Decyzja:**
    - Zadanie jest krytyczne i musi zostać zrealizowane w sposób kompleksowy i przemyślany, bez stosowania tymczasowych rozwiązań.
    - Prace muszą rozpocząć się w najbliższych sprintach, aby zakończyć wdrożenie najpóźniej w czwartym kwartale bieżącego roku.

- **Zadania:**
    - **Piotr:** Zaprojektowanie nowego rozwiązania i przygotowanie zadania do implementacji w najbliższym sprincie.

---

#### 5. Uruchomienie narzędzia "AI child item generator"

- **Ryzyko:**
    - Wbudowane w system do zarządzania zadaniami narzędzie AI, służące do dekompozycji zadań, jest nieskonfigurowane lub nie działa poprawnie – jego uruchomienie kończy się błędem.

- **Proponowane rozwiązanie:**
    - Należy zdiagnozować problem (prawdopodobnie konfiguracyjny) i uruchomić narzędzie. Ma ono potencjał, aby usprawnić proces tworzenia i opisywania zadań poprzez automatyczne dzielenie większych elementów (Feature) na mniejsze (PBI).

- **Decyzja:**
    - Temat zostanie przeanalizowany w przyszłości, gdy znajdzie się na to czas. Obecnie nie ma przypisanych zasobów do rozwiązania tego problemu.

- **Zadania:**

---

#### 6. Wykorzystanie AI do tworzenia podsumowań spotkań

- **Ryzyko:**
    - Standardowe podsumowania generowane przez Microsoft Copilot są zbyt ogólnikowe i mało użyteczne.

- **Proponowane rozwiązanie:**
    - Kontynuacja wykorzystywania dedykowanego asystenta AI z precyzyjnie zdefiniowanym szablonem (Ryzyko, Rozwiązanie, Decyzja, Zadania).
    - Aby poprawić jakość generowanych podsumowań, uczestnicy spotkania powinni starać się na głos wyraźnie nazywać omawiane w danym momencie zagadnienie.

- **Decyzja:**
    - Przyjęto nowy standard tworzenia notatek ze spotkań rady architektów przy użyciu specjalistycznego asystenta AI.

- **Zadania:**
    - **Janusz:** Generowanie i udostępnianie ustrukturyzowanych podsumowań po każdym spotkaniu rady.