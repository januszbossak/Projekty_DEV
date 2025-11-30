---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje **podstawowy proces biznesowy** systemu kancelaryjnego: cykl życia korespondencji wpływającej do LOT. Obejmuje wszystkie kroki od fizycznego odbioru przesyłki w Kancelarii, poprzez jej digitalizację (skanowanie), rejestrację i dekretację w AMODIT, aż po merytoryczne opracowanie przez pracownika docelowego.

Jest to główny proces, który **generuje "sprawy AMODIT"** (instancje procesu) zasilające system. Przypadki użycia z tej grupy bezpośrednio **wykorzystują (konsumują)** mechanizmy zdefiniowane w **Grupie 3** (wpinanie do teczek) i **Grupie 2** (tworzenie teczek). Logika ta jest oparta na mapie procesu "TO BE" oraz Instrukcji Kancelaryjnej LOT (model hybrydowy).

### **UC-KANC-PRZYCH-001 – Odbiór i Weryfikacja Przesyłki Papierowej w Kancelarii**

**Rola:** Pracownik Kancelarii (Recepcja / Administracja)

**Cel:** Fizyczny odbiór przesyłki, wstępna weryfikacja i przygotowanie do rejestracji w systemie.

**Opis:**

1. Pracownik Kancelarii odbiera przesyłkę (list, paczkę).
    
2. Weryfikuje, czy nie jest uszkodzona (zgodnie z § 9 Instrukcji Kancelaryjnej LOT) oraz czy nie jest to przesyłka wyłączona z otwierania (np. "Poufne", "Dane osobowe", "Do rąk własnych" – zgodnie z § 10 ust. 3 Instrukcji).
    
3. Otwiera przesyłki nie podlegające wyłączeniu.
    
4. W przypadku korespondencji, która jest dostarczana bezpośrednio do komórek merytorycznych (a nie przez Kancelarię), pracownik tej komórki, który odbiera ją fizycznie, **potwierdza odbiór na tablecie** (wymaganie z transkrypcji spotkania), co jest logowane w AMODIT.
    

### **UC-KANC-PRZYCH-002 – Rejestracja Przesyłki (Skanowanie i Metadane)**

**Rola:** Pracownik Kancelarii

**Cel:** Utworzenie nowej "sprawy AMODIT" (instancji procesu Korespondencja Przychodząca) w systemie, na podstawie zeskanowanego dokumentu.

**Opis:**

1. Pracownik skanuje dokument papierowy (zgodnie z mapą "TO BE"). System zapisuje odwzorowanie cyfrowe.
    
2. Oryginał papierowy jest odkładany do składnicy (model hybrydowy).
    
3. Pracownik Kancelarii uzupełnia w AMODIT **minimalny zestaw metadanych** (zgodny z Rejestrem Przesyłek Wpływających, § 8 Instrukcji Kancelaryjnej):
    
    - Data wpływu (zazwyczaj automatycznie).
        
    - Nadawca (wybór z bazy lub wpisanie nowego).
        
    - Data pisma (z dokumentu).
        
    - Znak pisma (sygnatura nadawcy).
        
    - Tytuł / krótki opis (np. "Wniosek o...", "Faktura nr...").
        
    - Liczba załączników.
        
4. Pole `Teczka_sprawy` na tym etapie pozostaje **puste** (zgodnie z mapą "TO BE").
    
5. System nadaje sprawie unikalny numer (np. Ldz. Kancelarii) i status "Zarejestrowana".
    

### **UC-KANC-PRZYCH-003 – Dekretacja Przesyłki**

**Rola:** Pracownik Kancelarii / Przełożony dekretujący

**Cel:** Elektroniczne skierowanie zarejestrowanej przesyłki do właściwej komórki organizacyjnej lub osoby merytorycznej.

**Opis:**

1. Pracownik Kancelarii (lub wyznaczona osoba, np. Asystent Zarządu) dokonuje dekretacji w AMODIT (zgodnie z § 17-19 Instrukcji Kancelaryjnej i mapą "TO BE").
    
2. Wybiera z systemu komórkę organizacyjną, grupę lub konkretnego pracownika.
    
3. Może dodać komentarz (dyspozycje) co do sposobu załatwienia sprawy.
    
4. System przenosi sprawę do "skrzynki zadań" osoby dekretowanej i zmienia status na "Zadekretowana".
    

### **UC-KANC-PRZYCH-004 – Merytoryczna Klasyfikacja i Przypięcie do Teczki JRWA**

**Rola:** Użytkownik merytoryczny (Pracownik / Kierownik)

**Cel:** Merytoryczne opracowanie sprawy i jej formalne przypisanie do właściwej `Teczka_sprawy` JRWA.

**Opis:** Jest to kluczowy krok z mapy "TO BE" ("Ocena powiązania korespondencji..."):

1. Pracownik merytoryczny otrzymuje zadanie w AMODIT (zadekretowaną sprawę).
    
2. Analizuje treść skanu i podejmuje decyzję o klasyfikacji:
    
    - **Jeśli sprawa dotyczy istniejącej teczki:** Wykonuje akcję `UC-JRWA-LNK-001` (Wybierz istniejącą `Teczka_sprawy`).
        
    - **Jeśli sprawa rozpoczyna nową teczkę:** Wykonuje akcję `UC-JRWA-LNK-002` (Utwórz nową `Teczka_sprawy` "w locie").
        
3. System w tym momencie **wymusza** klasyfikację (realizując `UC-JRWA-LNK-004`), ponieważ jest to etap "Weryfikacji merytorycznej" (zgodnie z `UC-JRWA-LNK-003`).
    
4. Po przypięciu, sprawa AMODIT dziedziczy metadane z teczki (znak sprawy, kategoria).
    

### **UC-KANC-PRZYCH-005 – Obsługa Przesyłki Błędnie Zadekretowanej**

**Rola:** Użytkownik merytoryczny / Pracownik Kancelarii

**Cel:** Obsługa sytuacji, w której pracownik merytoryczny stwierdza, że nie jest właściwy do załatwienia sprawy (zgodnie z § 18 ust. 4 Instrukcji Kancelaryjnej).

**Opis:**

1. Użytkownik merytoryczny, który otrzymał błędną dekretację, wybiera akcję "Przekaż / Zwróć do Kancelarii".
    
2. Podaje uzasadnienie lub wskazuje sugerowaną poprawną komórkę.
    
3. Sprawa wraca do Pracownika Kancelarii (lub osoby dekretującej) ze statusem "Do ponownej dekretacji".
    
4. Pracownik Kancelarii wykonuje ponownie `UC-KANC-PRZYCH-003`, kierując sprawę we właściwe miejsce.
    

### **UC-KANC-PRZYCH-006 – Zamknięcie Obiegu Pisma Przychodzącego**

**Rola:** Użytkownik merytoryczny

**Cel:** Zakończenie pracy nad sprawą AMODIT (pismem przychodzącym).

**Opis:** Po merytorycznym załatwieniu sprawy (np. udzieleniu odpowiedzi w ramach Grupy 5, lub podjęciu działań wewnętrznych), pracownik kończy obieg.

1. Wybiera akcję "Zakończ sprawę".
    
2. System sprawdza, czy spełniono warunek `UC-JRWA-LNK-004` (czy sprawa jest wpięta do teczki JRWA).
    
3. Jeśli tak, sprawa AMODIT otrzymuje status "Zamknięta" / "Załatwiona".
    
4. Zamknięcie tej _sprawy_ (pisma) **nie zamyka** automatycznie nadrzędnej `Teczka_sprawy` (z Grupy 2), która nadal może przyjmować kolejne pisma w danym roku.
    

## **Najważniejsze do zapamiętania**

> Ta grupa definiuje **główną "linię produkcyjną"** kancelarii.
> 
> 1. **Kancelaria (UC-001, 002, 003):** Skanuje, rejestruje podstawowe metadane i dekretuje. **Nie klasyfikuje** do JRWA.
>     
> 2. **Pracownik Merytoryczny (UC-004, 006):** Otrzymuje zadanie, **dokonuje klasyfikacji** (wykonując UCs z Grupy 3) i zamyka obieg pisma.
>     
> 
> Ten podział ról jest kluczowy dla wdrożenia w LOT.