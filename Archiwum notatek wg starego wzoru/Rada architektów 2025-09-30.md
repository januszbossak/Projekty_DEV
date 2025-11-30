[[2025-09-30 wtorek]] [[Rada architektów 2025-10-14]]

### Spotkanie rady architektów z dnia 30 września 2025

---

#### 1. Ujednolicenie logiki historii wysłanych maili i kolejki mailowej

- **Ryzyko:**
    
    - Nowa funkcja historii wysłanych maili rejestruje wiadomość jako "wysłaną" w momencie jej dodania do kolejki, a nie faktycznego wysłania przez serwer.
        
    - Prowadzi to do niespójności danych: administrator może widzieć w historii, że mail został wysłany, podczas gdy w rzeczywistości utknął on w kolejce (np. z powodu awarii usługi) lub został z niej ręcznie usunięty i nigdy nie dotarł do adresata.
        
- **Proponowane rozwiązanie:**
    
    - Zmiana logiki tak, aby zapis w historii wysłanych maili następował dopiero po pomyślnym przetworzeniu wiadomości przez usługę mailową i jej zdjęciu z kolejki.
        
- **Decyzja:**
    
    - Problem jest złożony technicznie, m.in. z powodu istnienia maili zbiorczych (dotyczących wielu spraw) oraz maili wysyłanych natychmiast (które trafiają do kolejki tylko w przypadku błędu).
        
    - Temat wymaga głębszej analizy i zaprojektowania rozwiązania. Zostanie zorganizowane osobne spotkanie techniczne w tej sprawie.
        
- **Zadania:**
    
    - Brak.
        

---

#### 2. Możliwość łączenia (join) raportów po polach typu "Odnośnik"

- **Ryzyko:**
    
    - Brak możliwości wykorzystania pól typu "Odnośnik" (lookup) jako kluczy do łączenia źródeł danych w nowym module raportowym.
        
- **Proponowane rozwiązanie:**
    
    - Dodanie takiej funkcjonalności.
        
- **Decyzja:**
    
    - Istnieje podejrzenie, że ta funkcja została już zaimplementowana w nowej wersji raportów, jednak podczas próby demonstracji na poprzednim spotkaniu nie zadziałała poprawnie.
        
    - Temat zostaje zdjęty z agendy rady w celu weryfikacji. Jeśli funkcjonalność istnieje, ale jest wadliwa, zostanie zgłoszony błąd.
        
- **Zadania:**
    
    - **Łukasz:** Sprawdzi działanie tej funkcjonalności na najnowszej wersji systemu.
        

---

#### 3. Rozszerzenie funkcji filtrujących o kontrolę domyślnego zaznaczania

- **Ryzyko:**
    
    - Funkcje filtrujące (np. `SetDictionaryFilter`, `SetUsersFilter`) automatycznie zaznaczają wartość w polu, jeśli w wyniku filtrowania pozostaje tylko jedna dostępna opcja. Takie zachowanie nie zawsze jest pożądane.
        
- **Proponowane rozwiązanie:**
    
    - Dodanie do wszystkich funkcji filtrujących opcjonalnego parametru (np. `setDefault`), który pozwoliłby deweloperowi zdecydować, czy pojedynczy wynik ma być automatycznie wybrany. Rozwiązanie to jest już zaimplementowane w funkcji `SetSqlReference` i powinno zostać ujednolicone.
        
    - Należy również zweryfikować zachowanie funkcji `SetList` w podobnym scenariuszu.
        
- **Decyzja:**
    
    - Propozycja zostaje zaakceptowana. Funkcjonalność zostanie ujednolicona we wszystkich odpowiednich funkcjach.
        
- **Zadania:**
    
    - **Łukasz:** Zweryfikuje, które funkcje wymagają modyfikacji, i zaimplementuje brakujący parametr w celu zapewnienia spójnego działania.