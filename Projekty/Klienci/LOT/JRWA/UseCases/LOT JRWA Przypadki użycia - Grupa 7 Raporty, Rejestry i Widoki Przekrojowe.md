---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje funkcjonalności związane z **przeglądaniem, wyszukiwaniem i raportowaniem** danych zgromadzonych w systemie kancelaryjnym. Nie tworzy ona nowych spraw, lecz konsumuje dane wygenerowane w Grupach 2, 4, 5 i 6.

Celem jest dostarczenie trzem grupom interesariuszy odpowiednich narzędzi:

1. **Kancelarii:** Formalnych, audytowalnych rejestrów (Dzienników Podawczych).
    
2. **Archiwiście:** Centralnych ewidencji zasobu (Spisów teczek).
    
3. **Użytkownikom Merytorycznym i Kierownictwu:** Raportów operacyjnych (Statusowych) oraz biznesowych "Widoków Przekrojowych".
    

### **UC-REP-001 – Przeglądanie Rejestru Przesyłek Wpływających**

**Rola:** Pracownik Kancelarii / Koordynator kancelaryjny / Archiwista

**Cel:** Zapewnienie centralnego, audytowalnego wglądu we wszystkie przesyłki, które wpłynęły do organizacji (elektroniczny odpowiednik Dziennika Podawczego).

**Opis:** System udostępnia raport/rejestr wszystkich spraw z procesu `P_KorespondencjaPrzychodzaca` (utworzonych w `UC-KANC-PRZYCH-002`).

Rejestr ten musi być zgodny z wymogami **§ 8 Instrukcji Kancelaryjnej LOT** i zawierać m.in.:

- Liczbę porządkową (numer sprawy AMODIT / Ldz.).
    
- Datę wpływu.
    
- Dane nadawcy.
    
- Datę i znak pisma nadawcy.
    
- Tytuł (krótki opis).
    
- Komu zadekretowano (komórka/osoba).
    

Rejestr musi być przeszukiwalny i filtrowalny po wszystkich tych kryteriach oraz po statusie (np. "Zarejestrowana", "W dekretacji", "Załatwiona").

### **UC-REP-002 – Przeglądanie Rejestru Przesyłek Wychodzących**

**Rola:** Pracownik Kancelarii / Koordynator kancelaryjny / Archiwista

**Cel:** Zapewnienie centralnego, audytowalnego wglądu we wszystkie przesyłki formalnie wysłane z organizacji.

**Opis:** System udostępnia raport/rejestr wszystkich spraw z procesu `P_KorespondencjaWychodzaca` (zgodnie z `UC-KANC-WYCH-006`).

Rejestr ten musi być zgodny z wymogami **§ 32 Instrukcji Kancelaryjnej LOT** i zawierać m.in.:

- Liczbę porządkową.
    
- Datę przekazania do wysyłki.
    
- Nazwę adresata.
    
- **Znak sprawy** (kluczowy identyfikator powiązany z teczką JRWA).
    
- **Sposób przekazania** (np. "Poczta polecona", "e-Doręczenia", "Kurier").
    

Rejestr musi być przeszukiwalny i filtrowalny.

### **UC-REP-003 – Generowanie "Książki Nadawczej"**

**Rola:** Pracownik Kancelarii

**Cel:** Wygenerowanie formalnego dokumentu (artefaktu) wymaganego przez operatora pocztowego dla przesyłek papierowych (zgodnie z wymogiem `WK24` z Załącznika EZD).

**Opis:**

1. Pracownik Kancelarii wchodzi do Rejestru Przesyłek Wychodzących (`UC-REP-002`).
    
2. Filtruje przesyłki, które mają być fizycznie nadane w danym dniu (np. status "Do wysyłki - Poczta").
    
3. Zaznacza wybrane przesyłki.
    
4. Wybiera akcję **"Drukuj Książkę Nadawczą"**.
    
5. System generuje plik PDF w formacie akceptowanym przez Pocztę Polską, zawierający listę zaznaczonych przesyłek (Adresat, Adres, typ przesyłki, numer nadawczy - jeśli już pobrany z e-Nadawcy).
    

### **UC-REP-004 – Centralna Ewidencja Teczek JRWA**

**Rola:** Archiwista / Koordynator kancelaryjny / Kierownik Komórki

**Cel:** Nadzór nad całym zasobem archiwalnym i kancelaryjnym – przegląd wszystkich założonych `Teczka_sprawy` (obiektów z Grupy 2).

**Opis:** System udostępnia centralny rejestr _wszystkich_ teczek (macierzystych, podteczek i zbiorczych). Rejestr ten umożliwia Archiwiście i Koordynatorom zarządzanie cyklem życia teczek.

Widok musi być filtrowalny co najmniej po:

- Komórce organizacyjnej (kto wytworzył).
    
- Roku założenia.
    
- Klasie JRWA (np. pokaż wszystko z `032`).
    
- Kategorii archiwalnej (np. pokaż wszystkie `A` lub wszystkie `B5`).
    
- **Statusie teczki** (np. "Aktywna", "Zamknięta", "Gotowa do przekazania do AZ", "Archiwalna", "Zbrakowana").
    

Jest to główne narzędzie pracy Archiwisty do realizacji procesów z Grupy 2 (np. typowania do brakowania `UC-JRWA-SPR-009`).

### **UC-REP-005 – Implementacja "Widoku Przekrojowego" (Biznesowego)**

**Rola:** Użytkownik merytoryczny / Kierownik

**Cel:** Umożliwienie wglądu w sprawy powiązane z danym obiektem biznesowym (np. kontrahentem, projektem, nieruchomością), **niezależnie od ich klasyfikacji JRWA**, zgodnie z koncepcją z Kompendium (Rozdział 5).

**Opis:** To jest pulpit (dashboard) lub specjalny typ raportu, który **nie jest** formalną teczką archiwalną.

1. Użytkownik wchodzi do np. "Widoku Kontrahenta" i wybiera "Firma X".
    
2. System AMODIT przeszukuje _wszystkie_ sprawy (z Grup 4, 5, 6) oraz teczki (z Grupy 2) i wyświetla listę wszystkich obiektów, które w metadanych mają powiązanie z "Firmą X".
    
3. Wynikiem jest logiczny zbiór, np.:
    
    - `Teczka_sprawy`: `BA.032.1.2025` (Tytuł: "Umowa ramowa z Firma X")
        
    - `P_KorespondencjaPrzychodzaca`: `KANC/123/2025` (Tytuł: "Zapytanie ofertowe od Firma X")
        
    - `P_Faktura`: `FAK/555/2025` (Tytuł: "Faktura od Firma X", wpięta do teczki zbiorczej `BF.340.2025`)
        
    - `P_KorespondencjaWychodzaca`: `BA.032.1.2025.3` (Tytuł: "Re: Aneks nr 2 do umowy...")
        

Widok ten pozwala na szybką nawigację biznesową, nie naruszając jednocześnie formalnej struktury klasyfikacji JRWA (faktura pozostaje w teczce `340`, a umowa w `032`).

### **UC-REP-006 – Raporty Operacyjne (Zarządcze i Statusowe)**

**Rola:** Użytkownik merytoryczny / Kierownik Komórki

**Cel:** Monitorowanie bieżącej pracy, terminowości i obciążenia zadaniami w systemie kancelaryjnym.

**Opis:** System udostępnia predefiniowane dashboardy i raporty, takie jak:

1. **"Moje Zadania":** Lista wszystkich zadań AMODIT przypisanych do zalogowanego użytkownika (np. "Do dekretacji", "Do akceptacji", "Do załatwienia", "Do potwierdzenia").
    
2. **"Zadania w Mojej Komórce":** Widok dla Kierownika, pokazujący wszystkie aktywne zadania w jego zespole, z możliwością filtrowania po pracowniku.
    
3. **"Raport Terminowości":** Lista spraw (np. przychodzących) z widoczną datą wpływu i datą załatwienia, pozwalająca monitorować opóźnienia.
    
4. **"Sprawy Oczekujące":** Raport pokazujący, na kogo "czeka" dana sprawa (kto jest "wąskim gardłem" w procesie akceptacji).
    

## **Najważniejsze do zapamiętania**

> Ta grupa realizuje kluczową funkcję systemu – **umożliwia znalezienie informacji**.
> 
> 1. `REP-001`, `002`, `003`, `004` to **rejestry formalne**, wymagane przez Instrukcję LOT, Archiwistę i Kancelarię. Są one dowodem na to, co się wydarzyło.
>     
> 2. `REP-005` (Widok Przekrojowy) to **funkcja biznesowa**, która ułatwia pracę merytoryczną, grupując dane wg logiki innej niż JRWA.
>     
> 3. `REP-006` to **narzędzia zarządcze** (workflow) do monitorowania pracy bieżącej.
>