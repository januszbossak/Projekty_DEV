

# Spotkanie Rady Architektów – 2025-10-30

## 1. Konfiguracja środowiska szkoleniowego (Partnerzy Comarch)

Kontekst i Problem:

Podczas przygotowań do darmowego szkolenia dla partnerów Comarch, uczestnikom przypisano tymczasowe adresy w domenie astrafox.pl, aby ukryć ich rzeczywiste dane. Testy wykazały, że adresy te nie są funkcjonalne (brak skrzynek/aliasów), co uniemożliwia komunikację i poprawne działanie scenariuszy szkoleniowych.

**Zidentyfikowane Ryzyka:**

- Brak możliwości realizacji scenariuszy szkoleniowych wymagających obsługi mailowej.
    
- Problemy wizerunkowe przed partnerami.
    

**Proponowane Rozwiązania Techniczne:**

- Utworzenie fizycznych skrzynek pocztowych lub aliasów dla przypisanych adresów.
    

Decyzja:

Należy niezwłocznie uruchomić obsługę przypisanych adresów e-mail.

**Zadania (Action Items):**

- **Janusz/Przemek:** Skonfigurować skrzynki pocztowe lub aliasy w domenie astrafox.pl dla uczestników szkolenia.
    

---

## 2. Diagnostyka problemów z Lucene (Administrator vs Twórca)

Kontekst i Problem:

Zgłoszono błąd wyszukiwania spraw po Case ID. Problem występuje specyficznie, gdy użytkownik jest jednocześnie twórcą sprawy i administratorem systemu. W przypadku standardowych użytkowników wyszukiwanie działa poprawnie. Dokumentacja błędu (Repro Steps) jest nieczytelna, ale problem leży w warstwie indeksowania lub konstrukcji zapytania.

**Zidentyfikowane Ryzyka:**

- Utrudniona obsługa systemu przez administratorów.
    
- Potencjalne błędy w budowie zapytań do indeksu.
    

**Proponowane Rozwiązania Techniczne:**

- Weryfikacja indeksu za pomocą narzędzia zewnętrznego (Luke) w celu ustalenia, czy problem leży po stronie zapisu w indeksie, czy konstrukcji zapytania (query).
    
- Modyfikacja zapytania w przypadku braku zwracania wyników, mimo istnienia danych w indeksie.
    

Decyzja:

Diagnostyka ma zostać przeprowadzona bezpośrednio na indeksach przy użyciu narzędzi deweloperskich, zamiast pełnej odbudowy indeksów.

**Zadania (Action Items):**

- **Tomasz/Damian:** Przeprowadzić diagnostykę indeksu narzędziem Luke (według instrukcji na Wiki) i zweryfikować zwracane wyniki dla problematycznego scenariusza.
    

---

## 3. System powiadomień o awariach krytycznych (Self-healing)

Kontekst i Problem:

System napotyka błędy krytyczne, takie jak wyczerpanie limitu OCR lub brak miejsca na dysku (uniemożliwiający zapis załączników), o czym administratorzy dowiadują się z opóźnieniem od biznesu. Brakuje proaktywnego mechanizmu informowania o stanie zdrowia systemu, co wydłuża czas reakcji (RTO).

**Zidentyfikowane Ryzyka:**

- Zatrzymanie procesów biznesowych (np. brak wczytywania faktur).
    
- Brak możliwości odróżnienia awarii dysku od braku dostępu do zasobu sieciowego (w obu przypadkach brak zapisu).
    
- Nieskuteczność powiadomień mailowych w przypadku awarii serwera pocztowego.
    

**Proponowane Rozwiązania Techniczne:**

- **MVP:** Wysłanie natychmiastowego maila do administratorów w momencie wystąpienia w logach błędu krytycznego (limit OCR, błąd I/O dysku).
    
- **Docelowo:** Wyświetlanie czerwonego paska/powiadomienia w interfejsie GUI aplikacji (widoczne dla admina po zalogowaniu).
    

Decyzja:

Wdrożyć mechanizm powiadomień mailowych dla zdefiniowanych zdarzeń krytycznych (OCR, Dysk). Docelowo rozbudować o powiadomienia w UI (sekcja "Uwagi dla administratora").

**Zadania (Action Items):**

- **Damian:** Przygotować PBI (Product Backlog Item) opisujący przypadki użycia.
    
- **Mateusz:** Zaimplementować logowanie i wysyłkę maila przy wyczerpaniu limitu OCR (MVP).
    

---

## 4. UX/UI Importu danych (Źródła Statyczne)

Kontekst i Problem:

Podczas aktualizacji źródła statycznego (re-import pliku), jeśli użytkownik pominie krok "Mapuj" i od razu zapisze zmiany, system gubi wcześniejsze definicje kolumn, zmieniając ich typ na domyślny LongText. Obecny proces jest nieintuicyjny i generuje błędy w strukturze danych.

**Zidentyfikowane Ryzyka:**

- Przypadkowe uszkodzenie struktury danych w źródłach słownikowych.
    

**Proponowane Rozwiązania Techniczne:**

- Zmiana przepływu (flow) użytkownika: Po wybraniu pliku okno mapowania powinno otwierać się automatycznie, bez możliwości jego pominięcia.
    

Decyzja:

Uprościć interfejs. Wybór pliku automatycznie przenosi do widoku mapowania. Zastąpić przyciski "Zapisz/Zamknij" parą "Wczytaj" (zatwierdza i importuje) oraz "Anuluj" (czyści wybór pliku).

**Zadania (Action Items):**

- **Zespół Deweloperski:** Przebudować modal importu pliku zgodnie z nowym flow (automatyczne otwarcie mapowania, zmiana nazw przycisków).
    

---

## 5. Mechanizm wydruku spraw

Kontekst i Problem:

Obecny moduł generowania widoku do druku jest przestarzały (niezmieniany od 10 lat). Padła sugestia jego aktualizacji.

Decyzja:

Temat o niskim priorytecie. Funkcja drukowania spraw jest marginalna biznesowo. Pozostawić bez zmian, dodać jedynie minimalną dokumentację dla obecnego stanu. Rozwój możliwy tylko na wyraźne, sponsorowane życzenie klienta.

**Zadania (Action Items):**

- **Brak** (poza ewentualnym uzupełnieniem dokumentacji).
    

---

## 6. Błędy w nowym module raportowym (Klient: Niden)

Kontekst i Problem:

Klient zgłaszał błędy SQL generowane przez nowy moduł raportowy. Poprawki (hotfixy) były wdrażane w ostatnich miesiącach.

Decyzja:

Należy ostatecznie potwierdzić rozwiązanie problemu po zakończeniu bieżących prac nad hotfixami. Jeśli błędy nie występują, zamknąć zgłoszenie.

**Zadania (Action Items):**

- **Anna:** Po zakończeniu bieżących hotfixów zweryfikować brak błędów SQL w raportach i zamknąć temat (Priorytet 1).
    

---

## 7. Filtrowanie w raportach (Checkbox List)

Kontekst i Problem:

W filtrach raportów opcja "Zaznacz wszystko" oraz lista dostępnych wartości działają myląco. Lista checkboxów jest budowana prawdopodobnie na podstawie ograniczonej próbki danych (np. pierwsze 100 rekordów lub distinct z ograniczeniem), przez co nie wszystkie wartości są widoczne i możliwe do wybrania.

**Zidentyfikowane Ryzyka:**

- Użytkownik jest wprowadzany w błąd – widzi na wykresie dane, których nie może wybrać w filtrze.
    
- Brak możliwości wyfiltrowania rzadszych danych.
    

Decyzja:

Temat wymaga analizy technicznej sposobu budowania listy wartości w filtrach przed podjęciem decyzji o zmianach. Decyzja odroczona do Sprintu 45.

**Zadania (Action Items):**

- **Anna:** Przeanalizować i przedstawić na kolejnej Radzie mechanizm budowania listy checkboxów (dlaczego pomija wartości widoczne na wykresie).
    

---

## 8. Walidacja reguł w zamkniętych sprawach (AMODIT to AMODIT)

Kontekst i Problem:

Wywołanie funkcji (reguły) na sprawie o statusie "Zamknięta" kończy się błędem walidacji. Funkcje systemowe nie powinny być blokowane przez status sprawy, w przeciwieństwie do edycji manualnej.

Decyzja:

Wyłączyć walidację statusu sprawy dla wywołań typu funkcja/reguła.

**Zadania (Action Items):**

- **Piotr/Zespół:** Dodać wyjątek w walidatorze dla funkcji.
    

---

## 9. Separacja dokumentów kodami kreskowymi (RegEx)

Kontekst i Problem:

System ma problem z dzieleniem dokumentów, gdy nie wykryje kodu kreskowego zgodnego ze wzorcem. Pojawiły się wątpliwości, czy w takim przypadku powinien tworzyć jedną sprawę zbiorczą, czy nie robić nic. Dodatkowo zidentyfikowano problem z nazwami plików zawierającymi średniki (format EML), co psuje parsowanie.

**Proponowane Rozwiązania Techniczne:**

- Logika: Jeśli dokument ma być dzielony po _konkretnym_ kodzie, a kod ten nie występuje – dokument nie jest dzielony (traktowany jako całość).
    
- Poprawka dla nazw plików: Obsługa nazw plików zawierających znaki specjalne (średniki) generowane przez niektóre serwery pocztowe.
    

Decyzja:

Naprawa błędu parsowania nazw plików oraz weryfikacja logiki dzielenia (brak podziału przy braku zdefiniowanego kodu).

**Zadania (Action Items):**

- **Piotr:** Poprawić obsługę nazw plików (ticket #22431) i logikę separatora.
    
- **Kamil:** Przygotować/zaktualizować przypadki testowe.