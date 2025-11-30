[[2025-08-19 wtorek]] [[Rada architektów 2025-10-14]]

Jasne, oto scalona, szczegółowa wersja podsumowania, stworzona na podstawie analizy obu dostarczonych wariantów.

### Spotkanie rady architektów z dnia 19 sierpnia 2025

---

#### 1. Weryfikacja dostępu do dokumentów i przejście serwisowe do Trust Center

- **Ryzyko:**
    
    - Brak jednoznacznego i bezpiecznego mechanizmu weryfikacji uprawnień użytkownika przy przejściu do zewnętrznego systemu (Trust Center) poza standardową grupą.
        
    - Automatyzacja procesu logowania może zablokować dostęp klientom korzystającym ze starszych wersji oprogramowania, które nie są w stanie przekazać adresu e-mail w parametrze wywołania.
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzenie dodatkowej weryfikacji uprawnień w oparciu o logowania `out` (lub mechanizm typu OAuth), aby sprawdzić, czy użytkownik posiada wymagany dostęp.
        
    - Zmiana nazwy przycisku na "Zarządzaj dokumentem w Trust Center", aby jego funkcja była bardziej intuicyjna dla użytkownika.
        
    - Zautomatyzowanie procesu: po kliknięciu przycisku system zweryfikuje, czy użytkownik jest wysyłającym dokument lub administratorem organizacji. Jeśli walidacja będzie pozytywna, system automatycznie wyśle e-mail z kodem dostępowym.
        
- **Decyzja:**
    
    - Nazwa przycisku zostanie zmieniona zgodnie z propozycją.
        
    - Rozwiązanie zostanie wdrożone z zachowaniem pełnej kompatybilności wstecznej. System najpierw sprawdzi, czy adres e-mail jest przekazywany w parametrze (w nowszych wersjach klienta). Jeśli tak, kod dostępowy zostanie wysłany automatycznie. Jeśli parametr będzie pusty (starsze wersje), użytkownikowi zostanie wyświetlone pole do ręcznego wprowadzenia swojego adresu e-mail.
        
- **Zadania:**
    
    - [Brak przypisanych zadań]
        

---

#### 2. Funkcjonalność tablicy ogłoszeń (News feed)

- **Ryzyko:**
    
    - Stworzenie nowej funkcjonalności, która będzie powielała możliwości istniejących już w systemie narzędzi, takich jak AMODIT Talk czy dedykowane procesy obiegu informacji.
        
    - Obecny prototyp nie uwzględnia kluczowych wymagań biznesowych, takich jak planowanie daty publikacji, data wygaśnięcia ogłoszenia czy elastyczny dobór odbiorców (np. po grupach użytkowników, a nie tylko po działach).
        
    - Istniejący, stary mechanizm newsów jest przestarzały technologicznie i nie jest używany przez kluczowych klientów.
        
- **Proponowane rozwiązanie:**
    
    - Damian zaprezentował prototyp modułu "Ogłoszenia", umieszczonego jako nowa zakładka w menu powiadomień.
        
    - W toku dyskusji zaproponowano rozbudowę funkcjonalności o kluczowe elementy:
        
        - Mechanizm wyboru odbiorców rozszerzony o grupy użytkowników i konkretne osoby (na wzór selektorów z modułu raportów).
            
        - Opcja planowania publikacji (data i godzina startu).
            
        - Możliwość ustawienia terminu ważności ogłoszenia, po którym byłoby ono automatycznie archiwizowane lub ukrywane.
            
        - Rozważenie wykorzystania dedykowanego procesu AMODIT lub modułu AMODIT Talk jako alternatywnego rozwiązania, które dostarcza gotowe mechanizmy (np. załączniki, komentarze, historia zmian).
            
- **Decyzja:**
    
    - Prace deweloperskie nad nową funkcjonalnością zostają wstrzymane do czasu precyzyjnego zdefiniowania wymagań biznesowych.
        
    - Należy wyjaśnić z Piotrem Murawskim różnice między jego wizją "news feedu", "tablicy ogłoszeń" a systemem anonsów (typu "sprzedam/oddam"), aby uniknąć tworzenia redundantnych narzędzi i dopasować rozwiązanie do realnych potrzeb.
        
- **Zadania:**
    
    - **Damian:** Skontaktowanie się z Piotrem Murawskim w celu doprecyzowania wymagań biznesowych dla nowej funkcjonalności.
        
    - **Mateusz:** Przygotowanie prezentacji możliwości AMODIT Talk jako potencjalnej alternatywy do przedstawienia w dalszych rozmowach.
        

---

#### 3. Logowanie powiadomień systemowych w celu zapewnienia śladu audytowego

- **Ryzyko:**
    
    - Brak centralnego rejestru (śladu audytowego) dla wysyłanych z systemu wiadomości e-mail, co uniemożliwia weryfikację, czy, kiedy i o jakiej treści powiadomienie zostało wysłane do odbiorcy.
        
- **Proponowane rozwiązanie:**
    
    - Rozszerzenie istniejącego mechanizmu logowania zdarzeń (używanego m.in. do rejestrowania pobrań dokumentów) o nową kategorię zdarzeń dla wszystkich powiadomień e-mail wysyłanych z procesów (workflow).
        
    - Logowanie powinno być opcjonalne i włączane na poziomie definicji konkretnego procesu.
        
- **Decyzja:**
    
    - Zostanie wdrożony mechanizm trwałego logowania powiadomień e-mail.
        
    - W ustawieniach definicji procesu zostanie dodany checkbox "Loguj z treścią maila", aby umożliwić administratorom kontrolę nad zakresem logowania.
        
    - Log będzie zawierał kluczowe informacje: datę, odbiorcę, tytuł, treść, typ zdarzenia oraz ID sprawy, której dotyczyło powiadomienie. Zapisy będą permanentne.
        
- **Zadania:**
    
    - **Piotr:** Zweryfikowanie szczegółów technicznych implementacji, określenie struktury danych do zapisu w bazie i przygotowanie zadania deweloperskiego.
        

---

#### 4. Widoczność globalnej zakładki "Do wykonania"

- **Ryzyko:**
    
    - Użytkownicy, którzy wyłączają w interfejsie widok obszaru "Wszystkie procesy" (np. z powodu dużej liczby raportów), niezamierzenie tracą również dostęp do globalnej zakładki "Do wykonania", co jest błędem i obniża użyteczność aplikacji.
        
- **Proponowane rozwiązanie:**
    
    - Oddzielenie logiki widoczności globalnej zakładki "Do wykonania" od ustawień widoczności obszaru "Wszystkie procesy".
        
- **Decyzja:**
    
    - Globalna zakładka "Do wykonania" musi być zawsze widoczna w głównym menu interfejsu, niezależnie od konfiguracji widoczności poszczególnych obszarów przez użytkownika.
        
    - Zakładka ta musi zawsze wyświetlać zadania ze wszystkich procesów, działając spójnie ze swoim odpowiednikiem w obszarze "Wszystkie procesy".
        
- **Zadania:**
    
    - [Brak przypisanych zadań]
        

---

#### 5. Dostęp do sprawy dla byłego współpracownika

- **Ryzyko:**
    
    - Osoba, która wykonywała akcje w sprawie jako współpracownik, po odebraniu tej roli całkowicie traci do niej dostęp (nawet w trybie do odczytu), co może utrudniać audyt, zachowanie ciągłości kontekstu lub wgląd w historyczne działania.
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzenie konfigurowalnej na poziomie procesu opcji, która pozwoliłaby byłym współpracownikom na zachowanie stałego dostępu do odczytu spraw, w których byli aktywni.
        
- **Decyzja:**
    
    - Funkcjonalność zostanie zaimplementowana.
        
    - Możliwość zachowania dostępu będzie konfigurowalna na poziomie definicji procesu za pomocą dedykowanej opcji, działającej analogicznie do istniejącego mechanizmu dla zastępstw.
        
- **Zadania:**
    
    - **Piotr:** Zaktualizowanie zgłoszenia (21722) o podjętą decyzję i szczegóły implementacyjne.