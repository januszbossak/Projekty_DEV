---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje proces biznesowy związany z tworzeniem, opiniowaniem, publikowaniem i archiwizowaniem formalnych **aktów normatywnych** (wewnętrznych) LOT S.A., zgodnie z zakresem zamówienia ("Repozytorium aktów wewnętrznych").

Obejmuje to m.in. Zarządzenia, Decyzje, Instrukcje, Regulaminy czy Okólniki. Proces ten jest kluczowym przykładem dokumentacji **tworzącej akta sprawy** o najwyższej **kategorii archiwalnej A** (materiały wieczyste).

Celem jest zapewnienie jednego, audytowalnego źródła prawdy o wewnętrznych regulacjach, od wersji roboczej po oficjalną publikację i wersjonowanie (zmiany, uchylenia). Każdy akt (sprawa AMODIT) jest automatycznie wpinany do odpowiedniej, rocznej **Teczki macierzystej** (np. `BZ.020.1.2025`) z **JRWA 1997** (np. klasa `020` - Zbiór aktów normatywnych Prezesa Zarządu).

### **UC-RAW-001 – Inicjowanie projektu aktu wewnętrznego**

**Rola:** Użytkownik merytoryczny (Inicjator z dowolnej komórki) / Dział Prawny

**Cel:** Rozpoczęcie pracy nad nowym aktem wewnętrznym (np. regulaminem, zarządzeniem).

**Opis:**

1. Inicjator uruchamia proces `P_AktWewnetrzny`.
    
2. Wybiera typ aktu (Zarządzenie, Instrukcja, itp.) oraz wskazuje, kto będzie organem wydającym (np. Prezes Zarządu, Członek Zarządu ds. Finansów).
    
3. Wypełnia formularz (Tytuł, Uzasadnienie, komórka wiodąca).
    
4. Załącza draft dokumentu (najczęściej w formacie *.docx), który będzie podlegał wersjonowaniu (`UC-RAW-002`).
    

### **UC-RAW-002 – Równoległy obieg opinii i wersjonowanie (Uzgodnienia)**

**Rola:** Opiniujący (Prawnik, Finanse, Merytoryczni) / Inicjator

**Cel:** Współpraca nad treścią aktu, zebranie formalnych opinii i śledzenie historii zmian (podobnie jak w `UC-UMOWY-003`).

**Opis:**

1. Inicjator kieruje projekt na ścieżkę uzgodnień (np. do Działu Prawnego, Finansów, IT).
    
2. Uczestnicy obiegu otrzymują zadania w AMODIT. Mogą:
    
    - Akceptować treść bez uwag.
        
    - Zgłaszać uwagi w komentarzach (odrzucając do poprawy).
        
    - Wgrać **nową wersję** dokumentu (*.docx) z naniesionymi zmianami (tryb śledzenia zmian).
        
3. System przechowuje pełną historię wersji pliku oraz wszystkie komentarze z etapu uzgodnień, co stanowi integralną część akt sprawy.
    

### **UC-RAW-003 – Automatyczne utworzenie/powiązanie `Teczka_sprawy` (Kat. A)**

**Rola:** System / Inicjator

**Cel:** Zapewnienie najwyższego standardu archiwizacji (Kat. A) dla wszystkich aktów normatywnych, zgodnie z JRWA 1997.

**Opis:** Jest to realizacja `UC-JRWA-LNK-005` (Automatyczne przypisanie):

1. System jest skonfigurowany tak, że każda instancja `P_AktWewnetrzny` jest automatycznie klasyfikowana.
    
2. Na podstawie wybranego w `UC-RAW-001` "organu wydającego", system automatycznie wybiera właściwą klasę JRWA:
    
    - Organ = Prezes Zarządu -> Klasa `020` (Zbiór aktów... Prezesa) -> Kategoria **A**.
        
    - Organ = Wiceprezes -> Klasa `021` (Zbiór aktów... wiceprezesów) -> Kategoria **A**.
        
    - Organ = Dyrektor Pionu -> Klasa `022` (Zbiór aktów... dyrektorów) -> Kategoria **A**.
        
3. System automatycznie wyszukuje lub tworzy "w locie" (`LNK-002`) roczną **Teczkę macierzystą** (`SPR-001`), np. `BZ.020.1.2025`.
    
4. Sprawa (akt) jest wpinana do tej teczki jako kolejna pozycja w spisie spraw.
    

### **UC-RAW-004 – Formalne podpisanie i "Publikacja" aktu**

**Rola:** Osoba upoważniona (Organ wydający, np. Prezes Zarządu)

**Cel:** Ostateczne zatwierdzenie aktu, nadanie mu mocy obowiązującej oraz numeru.

**Opis:**

1. Po zebraniu wszystkich akceptacji (`UC-RAW-002`), finalny projekt trafia do podpisu Osoby Upoważnionej.
    
2. Podpis następuje w modelu hybrydowym (zgodnie z `UC-KANC-WYCH-005`):
    
    - **Preferowany:** Podpis elektroniczny (kwalifikowany) złożony na dokumencie w AMODIT.
        
    - **Papierowy:** Druk, podpis odręczny, a następnie **skan oryginału** jest wgrywany z powrotem do sprawy AMODIT jako wersja ostateczna ("ad acta").
        
3. Po podpisaniu, system (lub Pracownik Biura Zarządu) nadaje aktowi **finalny numer** (np. Zarządzenie nr 3/2025) oraz **datę wejścia w życie**.
    
4. Status sprawy zmienia się na "Opublikowany" / "Obowiązujący".
    

### **UC-RAW-005 – Dystrybucja i centralne repozytorium (Wyszukiwarka Aktów)**

**Rola:** System / Każdy pracownik

**Cel:** Poinformowanie pracowników o nowym akcie oraz zapewnienie wszystkim dostępu do _aktualnej_ bazy obowiązujących regulacji.

**Opis:**

1. Po publikacji (`UC-RAW-004`), system automatycznie dystrybuuje informację o nowym akcie (np. e-mail z linkiem) do wszystkich pracowników lub do wskazanych grup (zgodnie z `UC-KANC-WEW-004`).
    
2. Co ważniejsze, system udostępnia specjalny widok/moduł **"Repozytorium Aktów Wewnętrznych"**.
    
3. To repozytorium (realizacja `UC-REP-005` i `REP-006`) jest publicznie dostępne dla pracowników i pokazuje **wyłącznie finalne, podpisane wersje aktów** ze statusem "Obowiązujący".
    
4. Umożliwia wyszukiwanie pełnotekstowe (OCR/text) oraz filtrowanie po typie aktu, dacie, numerze, komórce wydającej.
    

### **UC-RAW-006 – Zarządzanie wersjami (Zmiana lub Uchylenie aktu)**

**Rola:** Użytkownik merytoryczny / Dział Prawny

**Cel:** Zarządzanie cyklem życia aktu, który jest zmieniany lub uchylany przez nowy akt.

**Opis:**

1. Gdy pracownik inicjuje nowy akt (`UC-RAW-001`), który ma _zmienić_ lub _uchylić_ istniejący, musi wskazać w formularzu ten akt (relacja do sprawy).
    
2. Gdy nowy akt (zmieniający/uchylający) zostanie opublikowany (`UC-RAW-004`):
    
3. System automatycznie:
    
    - Oznacza stary akt w repozytorium jako "Uchylony" lub "Zmieniony".
        
    - Tworzy dwukierunkowe powiązanie (link) między starym a nowym aktem.
        
4. Dzięki temu pracownik w repozytorium (`UC-RAW-005`) zawsze widzi historię zmian i aktualną wersję.
    
5. Oba akty (stary i nowy) pozostają nienaruszone w swoich teczkach JRWA (Kat. A) do celów archiwalnych.
    

## **Najważniejsze do zapamiętania**

> Ta grupa definiuje formalny proces legislacyjny w LOT.
> 
> 1. **Archiwizacja (Kat. A):** Jest to proces o najwyższym priorytecie. `UC-RAW-003` zapewnia, że każdy akt trafia automatycznie do właściwej teczki `Kat. A` w JRWA 1997 (klasy `020`, `021`, `022`).
>     
> 2. **Repozytorium vs Proces:** System musi wyraźnie oddzielić proces _tworzenia_ aktu (z workflow, draftami, opiniami) od procesu _konsumowania_ (Repozytorium w `UC-RAW-005`, które pokazuje tylko finalne, obowiązujące wersje).
>     
> 3. **Wersjonowanie:** Kluczowa jest obsługa zmian i uchyleń (`UC-RAW-006`), aby zapewnić, że pracownicy zawsze mają dostęp do aktualnego prawa wewnętrznego.
>