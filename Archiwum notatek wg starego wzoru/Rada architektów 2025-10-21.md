

### Spotkanie rady architektów z dnia 21 października 2025

---

#### 1. Obsługa błędów przy wczytywaniu procesu XML
[[Projekty/Moduly/Eksport-import-definicji-procesow/README|Eksport-import-definicji-procesow]]

- **Ryzyko:**
    
    - Obecny system raportowania błędów (procesor XML) wyświetla błędy w formie technicznej tabeli, co jest mało czytelne dla użytkownika.
        
    - Występują konflikty przy imporcie, np. nadpisywanie pól o tych samych ID.
        
    - Zdarzają się przypadki dodania pola o tej samej nazwie niezależnie na środowisku produkcyjnym i testowym, co powoduje konflikty.
        
- **Proponowane rozwiązanie:**
    
    - Zmiana formy prezentacji błędów na opis tekstowy, sugerujący użytkownikowi akcję naprawczą.
        
    - Umożliwienie wpisywania GUID na danym środowisku (teście), aby rozwiązać konflikt duplikatów z produkcji.
        
    - Całkowite przeprojektowanie importu procesu w przyszłości.
        
- **Decyzja:**
    
    - Na ten moment pozostawiono obecne rozwiązanie (ostrzeżenie/tabelę), uznając je za wystarczające ulepszenie względem braku informacji.
        
    - Temat redesignu importu procesu zostaje odłożony na później, obecne ostrzeżenie ma wymusić na użytkownikach zastanowienie się przed działaniem.
        
- **Zadania:**
    
    - Brak przypisanych zadań w tym wątku.
        

---

#### 2. Zmiany w parserze i języku reguł poprzez DLL
[[Projekty/Moduly/Silnik-regul/README|Silnik-regul]]

- **Ryzyko:**
    
    - Wprowadzanie zmian w definicji języka lub parserze (silniku reguł) poprzez DLL (biblioteki dynamiczne) jest ryzykowne i uznane za "drogę do nikąd".
        
    - Może to prowadzić do problemów z utrzymaniem i stabilnością systemu (tzw. "pułapka").
        
- **Proponowane rozwiązanie:**
    
    - Klienci wymagający nowych funkcji standardowych powinni podnieść wersję systemu, zamiast otrzymywać je jako hotfix/DLL.
        
    - Ewentualna obsługa takich zmian przez DLL wymagałaby kompletnej zmiany filozofii systemu AMODIT.
        
- **Decyzja:**
    
    - Rada nie wyraża zgody na wprowadzanie zmian w parserze/języku jako DLL.
        
    - Funkcje standardowe są dostępne tylko poprzez aktualizację wersji.
        
- **Zadania:**
    
    - Brak przypisanych zadań.
        

---

#### 3. Błąd funkcji `deleteAttachment` w silniku reguł AMODIT
[[Projekty/Moduly/Silnik-regul/README|Silnik-regul]]

- **Ryzyko:**
    
    - Funkcja `deleteAttachment` w silniku reguł nie działa, mimo że funkcja `getAttachment` funkcjonuje poprawnie.
        
- **Proponowane rozwiązanie:**
    
    - Należy naprawić działanie funkcji `deleteAttachment`, aby była spójna z innymi funkcjami obsługi załączników w silniku reguł.
        
- **Decyzja:**
    
    - Błąd ma zostać zgłoszony i naprawiony.
        
- **Zadania:**
    
    - **Damian Kamiński:** Utworzenie zgłoszenia błędu i przypisanie go do odpowiedniej osoby (Mariusza).
        

---

#### 4. Błąd pobierania danych w nowych raportach (uprawnienia kolumn)
[[Projekty/Moduly/Modul-raportowy/README|Modul-raportowy]]

- **Ryzyko:**
    
    - Występuje błąd pobierania danych w module nowych raportów, gdy kolumny są widoczne tylko dla konkretnych osób lub ukryte.
        
- **Proponowane rozwiązanie:**
    
    - System powinien zwracać pustą wartość (lub odpowiedni znak pusty), jeśli użytkownik nie ma uprawnień do danej kolumny, zamiast wyrzucać błąd.
        
- **Decyzja:**
    
    - Należy obsłużyć ten przypadek w nowych raportach.
        
- **Zadania:**
    
    - **Damian Kamiński:** Opisanie problemu i przypisanie zadania naprawczego.
        

---

#### 5. Wyświetlanie tabeli jako formularza
[[Projekty/cross-cutting/UI-formularza-sprawy/README|UI-formularza-sprawy]]

- **Ryzyko:**
    
    - Obecna implementacja wyświetlania tabeli jako formularza jest obejściem problemu i jakość kodu jest niezadowalająca.
        
    - Napisanie tego rozwiązania poprawnie od nowa zajęłoby około 10-15 dni roboczych.
        
- **Proponowane rozwiązanie:**
    
    - Opcja 1: Szybkie przywrócenie starego wyglądu.
        
    - Opcja 2: Przepisanie modułu od nowa (kosztowne czasowo).
        
    - Mariusz sugeruje oparcie rozwiązania o tabelę, a nie drzewa, dla zgodności z UX/UI.
        
- **Decyzja:**
    
    - Decyzja wstrzymana. Piotr musi przeanalizować obecną reprezentację kodu przed podjęciem decyzji.
        
- **Zadania:**
    
    - **Piotr Buczkowski:** Weryfikacja sposobu implementacji wyświetlania tabeli.