### Spotkanie rady architektów z dnia 21 sierpnia 2025

---

#### 1. Funkcjonalność i obsługa raportów systemowych

- **Ryzyko:**
    - Brak możliwości dodawania raportów systemowych do dashboardów.
    - Kopiowanie raportu systemowego powoduje przeniesienie flagi "systemowy" na kopię, co uniemożliwia jej edycję i wprowadza niespójności w działaniu systemu.
    - Obecnie istnieje możliwość edycji raportów systemowych przez użytkowników nieposiadających odpowiednich uprawnień, co jest błędem, mimo że zmiany te są nadpisywane podczas aktualizacji systemu.

- **Proponowane rozwiązanie:**
    - Stworzenie hotfixa, który odblokuje raporty systemowe, umożliwiając ich dodawanie do dashboardów.
    - Zamiast tworzyć nową funkcję kopiowania, zdecydowano się wykorzystać istniejący mechanizm grupy uprawnień "System Report Managers". Administratorzy po stronie klienta, po dodaniu do tej grupy, będą mogli edytować i kopiować raporty systemowe.

- **Decyzja:**
    - Zostanie wdrożony hotfix odblokowujący możliwość dodawania raportów systemowych do dashboardów. Po skopiowaniu na dashboard, raport automatycznie utraci status "systemowy" i stanie się w pełni edytowalną kopią.
    - Klienci, którzy będą chcieli zarządzać (kopiować, modyfikować) raportami systemowymi, otrzymają instrukcję, jak wykorzystać do tego celu grupę uprawnień "System Report Managers".

- **Zadania:**
    - **Anna:** Przygotować i wdrożyć hotfix umożliwiający dodawanie raportów systemowych do dashboardów.
    - **Anna:** Usunąć błąd pozwalający na wejście w tryb edycji raportów systemowych przez nieuprawnionych użytkowników.
    - **Damian:** Przygotować artykuł instruktażowy dla klientów opisujący, jak zarządzać raportami systemowymi za pomocą dedykowanej grupy uprawnień.

---

#### 2. Prezentacja raportów systemowych na liście głównej

- **Ryzyko:**
    - Mieszanie raportów systemowych ze zwykłymi na jednej liście jest nieczytelne.
    - Używanie obecnego mechanizmu folderów do ich grupowania jest niewystarczające i podatne na błędy użytkowników.

- **Proponowane rozwiązanie:**
    - Dodanie na liście raportów nowej, stałej sekcji "Raporty systemowe", analogicznej do sekcji "Ulubione". Sekcja ta grupowałaby raporty na podstawie ich flagi w bazie danych.

- **Decyzja:**
    - Decyzja została odroczona. Propozycja musi zostać skonsultowana z Przemkiem, który miał kluczowe wymagania dotyczące tego widoku.

- **Zadania:**
    - **Damian/Kamil:** Przedstawić Przemkowi koncepcję nowej sekcji dla raportów systemowych i uzyskać jego akceptację.
    - **Łukasz:** Wstrzymać tworzenie zadania w backlogu do czasu podjęcia ostatecznej decyzji.

---

#### 3. Logowanie powiadomień e-mail

- **Ryzyko:**
    - Niejasność, jak rejestrować powiadomienia wysyłane do grup użytkowników. Rejestracja pojedynczego wpisu dla grupy jest nieprecyzyjna ze względu na zmienny skład grup w czasie.

- **Proponowane rozwiązanie:**
    - Rejestrowanie w logach każdego maila jako osobnego wpisu dla każdego indywidualnego odbiorcy, nawet jeśli wysyłka była skierowana do grupy.

- **Decyzja:**
    - W systemie będzie logowany każdy wysłany e-mail jako oddzielny rekord przypisany do konkretnego adresata. Mechanizm logowania będzie domyślnie wyłączony i klient będzie musiał go świadomie aktywować.

- **Zadania:**
    - **Piotr:** Zaimplementować mechanizm logowania powiadomień e-mail zgodnie z decyzją (jeden wpis per odbiorca).

---

#### 4. Zarządzanie tymczasowym dostępem do spraw (GTA)

- **Ryzyko:**
    - Brak centralnego panelu do zarządzania i przeglądania nadanych dostępów tymczasowych.
    - Brak globalnego widoku utrudnia monitorowanie aktywnych dostępów, co stwarza ryzyko związane z bezpieczeństwem i zgodnością z RODO.

- **Proponowane rozwiązanie:**
    - Stworzenie dedykowanego interfejsu do zarządzania dostępami tymczasowymi, np. w formie nowej zakładki w panelu zarządzania użytkownikami, która listowałaby wszystkie aktywne dostępy i pozwalała na ich odbieranie.

- **Decyzja:**
    - Problem został uznany za istotny, jednak jego rozwiązanie nie jest obecnie priorytetem, ponieważ nie ma presji ze strony klientów. Temat zostanie zaadresowany w przyszłości.

- **Zadania:**
    - [Brak przypisanych zadań]

---

#### 5. Poprawa funkcjonalności "Zapisz jako" dla raportów

- **Ryzyko:**
    - Funkcja "Zapisz jako" nieprawidłowo kopiuje flagę raportu systemowego, blokując możliwość edycji kopii.
    - Po wykonaniu operacji "Zapisz jako" interfejs użytkownika jest niespójny – adres URL się zmienia, ale widok (w tym nawigacja "breadcrumb") pozostaje w kontekście starego raportu.
    - Funkcja nie kopiuje przypisania do folderów, przez co kopia traci pierwotną kategoryzację.

- **Proponowane rozwiązanie:**
    - Należy kompleksowo naprawić działanie funkcji "Zapisz jako".

- **Decyzja:**
    - Funkcjonalność "Zapisz jako" musi zostać naprawiona w następujący sposób:
        - Podczas tworzenia kopii raportu systemowego flaga "systemowy" nie może być kopiowana.
        - Po zapisaniu kopii cały widok musi zostać w pełni przeładowany, aby odzwierciedlał kontekst nowego raportu.
        - Kategoryzacja (przypisanie do folderów) musi być poprawnie kopiowana do nowego raportu.

- **Zadania:**
    - **Anna:** Stworzyć zgłoszenie i zaimplementować poprawki dla funkcji "Zapisz jako" zgodnie z podjętymi decyzjami.