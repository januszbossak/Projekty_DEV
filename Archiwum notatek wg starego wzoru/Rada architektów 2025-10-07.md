[[2025-10-07 wtorek]] [[Rada architektów 2025-10-14]]

### Spotkanie rady architektów z dnia 7 października 2025

---

#### 1. Ograniczenie widoczności użytkowników w systemach wielospółkowych

- **Ryzyko:**
    
    - W środowiskach, gdzie na jednej instancji AMODIT pracują różne, odseparowane od siebie spółki (np. w projekcie LOT), istnieje ryzyko, że pracownik jednej firmy będzie mógł przypadkowo lub celowo udostępnić sprawę osobie z innej spółki. 
        
    - Problem dotyczy nie tylko panelu współwłaścicieli, ale wszystkich miejsc w systemie, gdzie wybierany jest użytkownik (pola typu `Użytkownik`, akcja `Przekaż do`, widoczność w panelu administracyjnym i raportach). 
        
- **Proponowane rozwiązanie:**
    
    - Początkowa propozycja zakładała dodanie na poziomie procesu możliwości ograniczenia listy dostępnych współwłaścicieli/obserwatorów do wybranej grupy. 3
        
    - Dyskusja wykazała, że potrzebne jest kompleksowe, architektoniczne rozwiązanie problemu "wielospółkowości", które zapewni separację danych w całej aplikacji. 4444
        
    - Jednym z pomysłów jest wprowadzenie w strukturze organizacyjnej możliwości oznaczenia, który jej poziom definiuje "spółkę", a następnie automatyczne filtrowanie list użytkowników na podstawie przynależności do tej samej jednostki. 
        
- **Decyzja:**
    
    - Temat jest zbyt szeroki, aby go rozwiązać doraźnie. Wymaga on głębszej analizy i zaprojektowania spójnego mechanizmu "wielospółkowości" w systemie.
        
    - Zgłoszenie zostaje przeniesione do backlogu i będzie ponownie analizowane, gdy pojawią się konkretne i szczegółowe wymagania od klienta (LOT). 
        
- **Zadania:**
    
    - Brak.
        

---

#### 2. Usprawnienie filtru "w miesiącu" w raportach

- **Ryzyko:**
    
    - Filtr "w miesiącu" dla pól daty jest mylący dla użytkownika, ponieważ wyświetla kontrolkę kalendarza z możliwością wyboru roku, mimo że operator ten ignoruje rok i filtruje dane ze wszystkich lat dla wybranego miesiąca. 7
        
- **Proponowane rozwiązanie:**
    
    - Ukrycie nagłówka z rokiem oraz strzałek nawigacyjnych w kontrolce kalendarza, gdy używany jest operator "w miesiącu". 8Alternatywą było zastąpienie kalendarza listą rozwijaną z 12 miesiącami, ale zrezygnowano z tego na rzecz prostszego rozwiązania. 
        
- **Decyzja:**
    
    - Przyjęto rozwiązanie polegające na ukryciu części kontrolki odpowiedzialnej за wybór roku za pomocą CSS. Jest to szybka poprawka, która eliminuje niejednoznaczność interfejsu. 
        
- **Zadania:**
    
    - **Ania:** Zaimplementuje poprawkę ukrywającą wybór roku w filtrze "w miesiącu". 11
        

---

#### 3. Weryfikacja grupowania parametrów integracji

- **Ryzyko:**
    
    - Nowa funkcjonalność grupowania parametrów integracji w ustawieniach systemowych mogłaby niepoprawnie działać dla starszych integracji, które nie stosowały się do zalecanej konwencji nazewniczej. 
        
- **Proponowane rozwiązanie:**
    
    - Przetestowanie nowej funkcjonalności na rzeczywistych, zróżnicowanych konfiguracjach zaimportowanych od klientów. 
        
- **Decyzja:**
    
    - Mechanizm migracji starych konfiguracji (gdzie nazwa grupy jest tworzona na podstawie nazwy integracji) został zaimplementowany i wydaje się poprawny. 14141414 Konieczne jest jednak przeprowadzenie testów na środowisku z realnymi danymi.
        
- **Zadania:**
    
    - **Adrian:** Wdroży zmiany na środowisko testowe. 
        
    - **Damian i Kamil:** Przetestują działanie grupowania na zaimportowanych, niestandardowych konfiguracjach integracji. 
        

---

#### 4. Logika zapisu historii wysłanych maili

- **Ryzyko:**
    
    - Zapisywanie w historii faktu wysłania maila w momencie dodania go do kolejki jest nieprecyzyjne. Mail może ostatecznie nie zostać wysłany (np. z powodu zatrzymania usługi), co tworzy fałszywy wpis w historii. 
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzenie dwuetapowego logowania: najpierw zapis z informacją "zaplanowano do wysłania", a następnie aktualizacja tego wpisu (lub dodanie nowego zdarzenia) ze statusem "wysłano" po faktycznym pomyślnym wysłaniu wiadomości. 
        
- **Decyzja:**
    
    - Dwuetapowy mechanizm zapisu statusu jest właściwym kierunkiem. Ustalono również, że konieczne jest utrzymanie osobnej tabeli dla historii wysyłek, a nie modyfikowanie istniejącej tabeli kolejki (`notification`), ze względu na różnice w strukturze danych (np. obsługa maili zbiorczych). 
        
- **Zadania:**
    
    - **Piotr:** Zaprojektuje szczegółowe rozwiązanie oparte na ustalonym podejściu. 
        

---

#### 5. Usprawnienie walidacji pól z maską (np. Telefon)

- **Ryzyko:**
    
    - Pole z maską "Telefon" pozwala na wpisanie nieprawidłowych znaków, a następnie jedynie podświetla pole na czerwono, nie blokując dalszych akcji. 22Użytkownicy interpretują czerwony kolor jako błąd krytyczny i są zdezorientowani, że formularz można zapisać. 
        
- **Proponowane rozwiązanie:**
    
    - Docelowo należy połączyć funkcjonalność pól tekstowych z maską i pól walidowanych. 
        
    - W ustawieniach pola tekstowego z wybraną maską należy dodać nową opcję (checkbox) o nazwie "Wymuś zgodność z maską". 
        
    - Jeśli opcja jest zaznaczona, niezgodność z maską będzie traktowana jako twardy błąd walidacji, blokujący zapis. 
        
    - Jeśli opcja nie jest zaznaczona, system będzie działał jak dotychczas – wyświetli jedynie ostrzeżenie na czerwono, ale pozwoli na zapis. 
        
- **Decyzja:**
    
    - Propozycja jest słuszna, ponieważ zwiększa elastyczność i pozwala wdrożeniowcom decydować o poziomie rygorystyczności walidacji w zależności od potrzeb biznesowych. 
        
    - Temat jest zbyt duży na szybką implementację i wymaga zaprojektowania. Zostaje przeniesiony do backlogu. 
        
- **Zadania:**
    
    - **Kamil:** Podejmie się zaprojektowania nowej funkcjonalności. 
        

---