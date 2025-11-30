---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje formalny proces biznesowy związany z przygotowaniem, opiniowaniem i podejmowaniem decyzji dla **wniosków kierowanych na posiedzenia Zarządu LOT S.A.**, zgodnie z zakresem zamówienia ("wnioski na Zarząd").

Proces ten jest kluczowym przykładem dokumentacji **tworzącej akta sprawy** o najwyższym priorytecie archiwalnym.

Celem jest zapewnienie ustrukturyzowanego, audytowalnego i bezpiecznego obiegu wniosku – od jego inicjacji przez pracownika merytorycznego, przez weryfikację formalną (np. przez Biuro Zarządu), opiniowanie (prawne, finansowe), aż po formalne zarejestrowanie podjętej przez Zarząd decyzji (np. w formie Uchwały lub Postanowienia).

Każdy wniosek (jako sprawa AMODIT) jest **automatycznie** wpinany do rocznej, zbiorczej **Teczki macierzystej** (zgodnie z `UC-JRWA-SPR-001`), prowadzonej dla klasy **`004` ("Wnioski do Zarządu i postanowienia Zarządu")** z **JRWA 1997**, która posiada **kategorię archiwalną A** (materiały wieczyste).

### **UC-WNZ-001 – Inicjowanie Wniosku na Zarząd**

**Rola:** Użytkownik merytoryczny (Inicjator z dowolnej komórki)

**Cel:** Formalne zgłoszenie wniosku do rozpatrzenia przez Zarząd, wraz z kompletem wymaganych dokumentów.

**Opis:**

1. Inicjator uruchamia proces `P_WniosekNaZarzad`.
    
2. Wypełnia ustrukturyzowany formularz wniosku, zawierający m.in.:
    
    - Tytuł / Przedmiot wniosku.
        
    - Wnioskodawca / Komórka merytoryczna.
        
    - Uzasadnienie (biznesowe, prawne, finansowe).
        
    - Proponowany termin rozpatrzenia / data posiedzenia.
        
    - Oczekiwana decyzja (np. "Akceptacja", "Opinia").
        
3. Inicjator **musi załączyć** wymagane dokumenty, np. projekt Uchwały, prezentację, analizę finansową, projekt umowy (jeśli dotyczy).
    

### **UC-WNZ-002 – Automatyczne utworzenie/powiązanie `Teczka_sprawy` (Kat. A)**

**Rola:** System / Inicjator

**Cel:** Zapewnienie najwyższego standardu archiwizacji (Kat. A) i zgodności z JRWA 1997 od samego początku procesu.

**Opis:** Jest to realizacja `UC-JRWA-LNK-005` (Automatyczne przypisanie) połączona z `UC-JRWA-LNK-002` (Tworzenie "w locie"):

1. System jest skonfigurowany tak, że każda nowa instancja `P_WniosekNaZarzad`...
    
2. ...musi być powiązana z `Teczka_sprawy` z klasy `004` ("Wnioski do Zarządu...").
    
3. System **automatycznie** wyszukuje roczną **Teczkę macierzystą** (zgodną z `UC-JRWA-SPR-001`) dla tej klasy i roku, np. `BZ.004.1.2025` (gdzie BZ to np. Biuro Zarządu).
    
4. Jeśli teczka ta nie istnieje (bo to pierwszy wniosek w roku), system **automatycznie tworzy ją "w locie"**.
    
5. Każdy wniosek (sprawa AMODIT) jest wpinany do tej jednej, rocznej teczki `BZ.004.1.2025`, stając się kolejną pozycją w jej spisie spraw (realizując `UC-JRWA-LNK-006`).
    

### **UC-WNZ-003 – Weryfikacja formalna (Biuro Zarządu)**

**Rola:** Pracownik Biura Zarządu (Asystent Zarządu)

**Cel:** Kontrola kompletności wniosku i zgodności z wymogami formalnymi przed skierowaniem go do dalszego opiniowania lub na posiedzenie.

**Opis:**

1. Nowy wniosek trafia najpierw do Biura Zarządu (BZ).
    
2. Pracownik BZ sprawdza, czy:
    
    - Wniosek jest kompletny (wypełnione wszystkie pola).
        
    - Załączono wszystkie wymagane dokumenty (np. projekt uchwały).
        
    - Wniosek kwalifikuje się na agendę najbliższego posiedzenia.
        
3. Pracownik BZ może:
    
    - **Zaakceptować formalnie:** Przekazać wniosek na ścieżkę opiniowania (`UC-WNZ-004`).
        
    - **Zwrócić do poprawy:** Odesłać do Inicjatora (`UC-WNZ-001`) z komentarzem, co należy uzupełnić.
        

### **UC-WNZ-004 – Równoległy obieg opinii (Prawna, Finansowa, Merytoryczna)**

**Rola:** Prawnik / Dział Finansowy / Dyrektorzy merytoryczni

**Cel:** Zebranie wszystkich niezbędnych opinii i rekomendacji dla Zarządu przed podjęciem decyzji.

**Opis:**

1. Po weryfikacji formalnej (`UC-WNZ-003`), Biuro Zarządu kieruje wniosek na (zazwyczaj równoległą) ścieżkę opiniowania, np. do Pionu Prawnego, Finansowego i innych wskazanych Dyrektorów.
    
2. Opiniujący otrzymują zadania w AMODIT.
    
3. Każdy opiniujący może:
    
    - **Wydać opinię pozytywną.**
        
    - **Wydać opinię negatywną** (z obligatoryjnym uzasadnieniem).
        
    - **Wydać opinię z zastrzeżeniami** (wskazując, co należy zmienić).
        
4. Wszystkie opinie (jako komentarze w sprawie lub jako osobne dokumenty `P_PismoWewnetrzne` wpięte do teczki) są gromadzone w jednej sprawie AMODIT.
    

### **UC-WNZ-005 – Prezentacja i rejestracja decyzji Zarządu**

**Rola:** Pracownik Biura Zarządu

**Cel:** Formalne odnotowanie w systemie decyzji podjętej przez Zarząd na posiedzeniu.

**Opis:**

1. Po zebraniu opinii (`UC-WNZ-004`), sprawa w AMODIT trafia na etap "Na posiedzeniu Zarządu".
    
2. Po zakończeniu posiedzenia (lub w jego trakcie), Pracownik Biura Zarządu wchodzi w sprawę AMODIT i odnotowuje decyzję Zarządu, wybierając status:
    
    - **Zaakceptowano** (zgodnie z wnioskiem).
        
    - **Zaakceptowano ze zmianami** (wymagany komentarz).
        
    - **Odrzucono.**
        
    - **Skierowano do dalszych analiz / zdjęto z porządku obrad.**
        

### **UC-WNZ-006 – Załączenie finalnego dokumentu decyzyjnego (Uchwała/Postanowienie)**

**Rola:** Pracownik Biura Zarządu

**Cel:** Wprowadzenie do systemu ostatecznego, podpisanego dokumentu będącego wynikiem decyzji Zarządu.

**Opis:**

1. Po zarejestrowaniu decyzji (`UC-WNZ-005`), Pracownik Biura Zarządu (BZ) jest odpowiedzialny za dołączenie do sprawy AMODIT finalnego dokumentu.
    
2. BZ wgrywa do sprawy **podpisany skan (lub dokument podpisany elektronicznie) Uchwały lub Postanowienia Zarządu**.
    
3. W formularzu sprawy uzupełnia oficjalny numer dokumentu (np. `Uchwała nr 123/2025`).
    
4. Ten dokument staje się kluczowym elementem akt sprawy (Kat. A).
    

### **UC-WNZ-007 – Dystrybucja decyzji i zamknięcie sprawy wniosku**

**Rola:** Pracownik Biura Zarządu / System

**Cel:** Poinformowanie Inicjatora i zainteresowanych stron o podjętej decyzji oraz formalne zamknięcie obiegu wniosku.

**Opis:**

1. Po załączeniu uchwały (`UC-WNZ-006`), Pracownik BZ wybiera akcję "Zakończ i dystrybuuj".
    
2. System automatycznie wysyła powiadomienie (wraz z linkiem do sprawy i załączoną uchwałą) do Inicjatora (`UC-WNZ-001`) oraz do wszystkich opiniujących (`UC-WNZ-004`).
    
3. Sprawa AMODIT (`P_WniosekNaZarzad`) otrzymuje status "Zamknięta".
    
4. Sprawa pozostaje trwale wpięta w teczce `BZ.004.1.2025` (Kat. A), która po zakończeniu roku i 2 latach oczekiwania (`UC-JRWA-SPR-006`) trafi do AZ, a docelowo do Archiwum Państwowego (`UC-JRWA-SPR-010`).
    

## **Najważniejsze do zapamiętania**

> Ta grupa definiuje jeden z najważniejszych procesów decyzyjnych w LOT.
> 
> 1. **Archiwizacja (Kat. A):** Kluczowe jest automatyczne wpięcie (`UC-WNZ-002`) każdego wniosku do rocznej teczki macierzystej klasy **`004` (Kat. A)** z JRWA 1997.
>     
> 2. **Centralizacja:** Proces jest scentralizowany – Biuro Zarządu (`UC-WNZ-003`, `005`, `006`) pełni rolę "gatekeepera" i rejestratora decyzji.
>     
> 3. **Audytowalność:** System przechowuje pełną historię: wniosek, wszystkie opinie, finalną uchwałę i statusy akceptacji, co jest krytyczne dla materiałów wieczystych.
>