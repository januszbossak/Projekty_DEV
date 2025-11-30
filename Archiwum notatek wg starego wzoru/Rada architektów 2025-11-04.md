

## 1. Niezgodność statusów dokumentów w Trust Center

Kontekst i Problem:

Zidentyfikowano przypadki, w których status dokumentu w Trust Center nie odpowiada rzeczywistemu etapowi procesu podpisywania (np. dokument podpisany przez wszystkich, ale status nie zmienia się na "1", co blokuje dodanie do blockchaina). Problemy te korelują z awariami dostępu do bazy danych Azure i potencjalnym brakiem zapisu potwierdzenia transakcji w bazie mimo braku błędu po stronie serwera.

**Zidentyfikowane Ryzyka:**

- Blokada procesów biznesowych (dokumenty "wiszą" jako niepodpisane).
    
- Brak spójności danych między aplikacją a bazą danych.
    

**Proponowane Rozwiązania Techniczne:**

- **Manualne wymuszenie:** Wykorzystanie istniejących mechanizmów (`TrustCenter_CheckStatus` lub `TrustCenter_FinishSigning`) do aktywnego sprawdzenia i wymuszenia zmiany statusu przez administratora/użytkownika w przypadkach krytycznych.
    
- **Automatyzacja (Job):** Wdrożenie cyklicznego zadania (uruchamianego raz na dobę), które skanuje bazę w poszukiwaniu niespójnych statusów i automatycznie je koryguje.
    
- **Wiki/Szkolenia:** Edukacja wdrożeniowców na temat obsługi takich wyjątków (użycie endpointu `Finishing`).
    

Decyzja:

Zdecydowano o wdrożeniu rozwiązania dwutorowego: doraźne ręczne wywoływanie sprawdzenia statusu dla spraw pilnych oraz docelowe stworzenie automatycznego joba naprawczego. Dodatkowo należy zweryfikować zasady retencji dokumentów oczekujących na podpis (czy mogą oczekiwać w nieskończoność).

**Zadania:**

- **Marek Dziakowski:** Przygotować joba skanującego i naprawiającego statusy (uruchamianie raz na dobę).
    
- **Marek Dziakowski:** Opisać na Wiki procedurę ręcznego domykania procesów (`TrustCenter_FinishSigning`) dla wdrożeniowców.
    
- **Marek Dziakowski:** Przeanalizować możliwość automatycznego wygaszania dokumentów o nieokreślonym terminie podpisu (np. po 6 miesiącach) i przedstawić rekomendację na kolejnej Radzie.
    

---

## 2. Optymalizacja kosztów i deduplikacja zapytań do AI OCR

Kontekst i Problem:

Wykryto przypadki wielokrotnego wysyłania tych samych plików do usługi AI OCR, co generuje zbędne, wysokie koszty (przykład: 20 000 PLN za weekend przez pętlę w regule okresowej). Problemem są zarówno błędy w konfiguracji procesów (reguły okresowe), jak i błędy komunikacyjne przy zakładaniu spraw z maila/pliku (ponowne przetwarzanie mimo odczytu).

**Zidentyfikowane Ryzyka:**

- Wysokie, nieuzasadnione koszty usług Azure/AI.
    
- Zdublowane sprawy w systemie.
    

**Proponowane Rozwiązania Techniczne:**

- **Obsługa parametru `force`:**
    
    - Reguły automatyczne/okresowe w AMODIT nie mogą wysyłać parametru `force`. Parametr ten powinien być zarezerwowany dla akcji ręcznych.
        
    - Serwis OCR musi weryfikować hash pliku. Jeśli plik o tym samym hashu (i ID) został przetworzony, a nie ma flagi `force`, serwis zwraca błąd "duplikat".
        
- **Mechanizm zakładania spraw (Mail/Plik):**
    
    - Wprowadzenie tabeli pośredniej przechowującej identyfikatory przetworzonych wiadomości (`Message-ID`) lub plików (Hash + Data modyfikacji + Nazwa).
        
    - Przed założeniem sprawy system sprawdza w tabeli, czy dany obiekt był już procesowany.
        

Decyzja:

Należy zabezpieczyć system na dwóch poziomach: po stronie AMODIT (zarządzanie parametrem force) oraz po stronie mikroserwisu OCR (tabela hashy). Problem pętli przy zakładaniu spraw z maila/pliku ma zostać wydzielony jako zadanie o wysokim priorytecie.

**Zadania:**

- **Piotr Buczkowski:** Zaimplementować mechanizm deduplikacji po stronie serwisu OCR (weryfikacja hashy, obsługa braku flagi `force`).
    
- **Piotr Buczkowski:** Rozpisać zadanie dotyczące zabezpieczenia mechanizmu zakładania spraw z maila (wykorzystanie `Message-ID` i tabeli pośredniej).
    
- **Zespół (Piotr/Damian):** Zaktualizować dokumentację/OWU dla klientów korzystających z API bezpośrednio (wymóg samodzielnego zabezpieczenia przed duplikatami, jeśli nie używają AMODIT).
    

---

## 3. Konfiguracja kategorii powiadomień mailowych

Kontekst i Problem:

Klient (AmRest) zgłosił potrzebę rozdzielenia powiadomień o edycji dokumentu/komentarzach od powiadomień o przekazaniu sprawy. Obecnie są one traktowane łącznie jako powiadomienia główne, co uniemożliwia ich wybiórcze wyłączenie w profilu użytkownika.

**Zidentyfikowane Ryzyka:**

- Zmiana globalna może negatywnie wpłynąć na innych klientów przyzwyczajonych do obecnego działania.
    
- Konieczność głębszej analizy starego mechanizmu tabeli powiadomień.
    

**Proponowane Rozwiązania Techniczne:**

- Analiza istniejącej tabeli konfiguracyjnej powiadomień i dodanie nowej kategorii lub flagi dla zdarzeń typu "edycja/komentarz".
    

Decyzja:

Temat wymaga osobnego spotkania analitycznego. Nie wprowadzamy szybkich zmian "na prośbę" bez weryfikacji wpływu na cały system.

**Zadania:**

- **Damian Kaminski:** Przeanalizować logikę powiadomień na podstawie dostarczonego artykułu z Wiki i zorganizować spotkanie w celu wypracowania systemowego rozwiązania.
    

---

## 4. Błąd w module raportowym ("Zaznacz wszystko")

Kontekst i Problem:

Funkcja "Zaznacz wszystko" w module raportowym działa nieprawidłowo – nie uwzględnia wszystkich elementów widocznych na raporcie (np. zaznacza 2 z 3 rekordów).

**Zidentyfikowane Ryzyka:**

- Błędy w raportowaniu i przetwarzaniu danych przez użytkowników.
    

Decyzja:

Temat pozostaje otwarty do weryfikacji.

**Zadania:**

- **Anna Skupinska:** Zweryfikować przyczynę błędu i mechanizm generowania listy do zaznaczenia przed kolejną Radą.
    

---

## 5. Bezpieczne zatrzymywanie usług (Graceful Shutdown)

Kontekst i Problem:

Wprowadzono nowe joby (AI, e-Nadawca), które mogą nie obsługiwać poprawnie procedury zatrzymania usługi. Istnieje ryzyko, że przy restarcie serwera proces zostanie "zabity" w trakcie przetwarzania, co doprowadzi do niespójności danych. Starsze joby mają zaimplementowane mechanizmy sprawdzania stanu usługi.

**Zidentyfikowane Ryzyka:**

- Uszkodzenie danych przy restarcie serwisów.
    
- Błędy w przetwarzaniu masowym.
    

Decyzja:

Należy dokonać przeglądu wszystkich nowych jobów pod kątem obsługi przerwania działania (graceful shutdown).

**Zadania:**

- **Piotr Buczkowski:** Utworzyć zgłoszenie główne oraz podzadania (PBI) dla poszczególnych jobów wymagających weryfikacji mechanizmu zatrzymywania.