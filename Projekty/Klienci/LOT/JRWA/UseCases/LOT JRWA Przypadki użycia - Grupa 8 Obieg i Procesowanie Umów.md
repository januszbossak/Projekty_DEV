---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje kompletny, merytoryczny proces biznesowy związany z cyklem życia umowy, zgodnie z zakresem zamówienia ("procesowanie umów"). Proces ten jest kluczowym przykładem dokumentacji **tworzącej akta sprawy**.

Celem jest zapewnienie, że każda umowa (oraz jej aneksy i załączniki) jest inicjowana, weryfikowana merytorycznie i prawnie, akceptowana, podpisywana i ewidencjonowana w ustrukturyzowany sposób.

Każdy proces umowy musi być nierozerwalnie związany z dedykowaną **`Teczka_sprawy`** (z Grupy 2), utworzoną we właściwej klasie **JRWA 1997** (np. `032` - Umowy krajowe, `033` - Umowy zagraniczne).

### **UC-UMOWY-001 – Wniosek o przygotowanie/rejestrację umowy**

**Rola:** Użytkownik merytoryczny (Inicjator z dowolnej komórki)

**Cel:** Formalne rozpoczęcie pracy nad nową umową i zebranie kluczowych metadanych.

**Opis:**

1. Inicjator uruchamia proces `P_Umowa`.
    
2. Wypełnia formularz, podając kluczowe dane:
    
    - Dane kontrahenta (wybierane z bazy lub wprowadzane ręcznie).
        
    - Przedmiot umowy (opis).
        
    - Strony umowy (kto reprezentuje LOT).
        
    - Wartość umowy (jeśli znana).
        
    - Okres obowiązywania.
        
3. Załącza pierwszy projekt umowy (draft) lub wskazuje, że umowa jest na wzorze kontrahenta.
    

### **UC-UMOWY-002 – Założenie (lub powiązanie) `Teczka_sprawy` dla umowy**

**Rola:** Inicjator / System

**Cel:** Zapewnienie, że proces umowy jest od samego początku poprawnie osadzony w strukturze JRWA.

**Opis:** Jest to **wymagany krok** na początku procesu (realizacja `UC-JRWA-LNK-004`):

1. Inicjator musi wskazać klasę JRWA (np. `032` dla umowy krajowej lub `033` dla zagranicznej).
2. Zgodnie z "Uwagami" w JRWA 1997 dla klasy `032` ("Każda umowa stanowi odrębną sprawę"), system wymusza logikę **jedna umowa = jedna `Teczka_sprawy`**.
3. Inicjator wykonuje akcję `UC-JRWA-LNK-002` (Utwórz nową teczkę "w locie").
4. System, wykrywając klasę `032`, automatycznie uruchamia scenariusz `C` (z `LNK-002`) i tworzy nową **Teczkę macierzystą** (zgodnie z `UC-JRWA-SPR-001`), nadając jej znak, np. `BH.032.1.2025`.
5. Wszystkie dalsze dokumenty (opinie, aneksy, korespondencja) dotyczące _tej_ umowy będą wpinane do _tej_ teczki.

### **UC-UMOWY-003 – Przygotowanie i wersjonowanie projektu umowy**

**Rola:** Inicjator / Prawnik / Uczestnicy obiegu

**Cel:** Współpraca nad treścią umowy i śledzenie historii zmian.

**Opis:**

1. Inicjator wgrywa draft umowy (plik *.docx).
    
2. Każdy uczestnik obiegu (np. Prawnik) może pobrać plik, nanieść zmiany (w trybie śledzenia zmian) i wgrać go jako **nową wersję**.
    
3. AMODIT przechowuje wszystkie historyczne wersje dokumentu, z informacją "kto" i "kiedy" dodał daną wersję, zapewniając pełną historię negocjacji.
    

### **UC-UMOWY-004 – Wielościeżkowy obieg akceptacyjny (Uzgodnienia)**

**Rola:** Akceptujący (Merytoryka, Finanse, Bezpieczeństwo IT, Prawnik)

**Cel:** Merytoryczna, finansowa i prawna weryfikacja projektu umowy.

**Opis:**

1. Po przygotowaniu draftu, Inicjator wysyła go na ścieżkę akceptacyjną.
2. Ścieżka może być dynamiczna (inicjator sam wskazuje akceptantów) lub statyczna (zdefiniowana na stałe, np. "każda umowa > 50 000 PLN musi iść do Akceptacji Finansowej").
3. Akceptujący (np. Prawnik, Dział Finansowy) otrzymują zadania w AMODIT. Mogą:
    
    - **Zaakceptować** (przesunąć dalej).
    - **Odrzucić** (wrócić do Inicjatora z komentarzem).
    - **Skomentować** (dodając uwagi).
        
    - **Dodać nową wersję** dokumentu (`UC-UMOWY-003`).
        

### **UC-UMOWY-005 – Powiązanie opinii prawnej (Integracja z Grupą 6)**

**Rola:** Prawnik

**Cel:** Formalne wydanie opinii prawnej do umowy i dołączenie jej do akt sprawy.

**Opis:** Podczas obiegu (`UC-UMOWY-004`), gdy sprawa trafia do Prawnika, ma on dwie możliwości:

1. Zaakceptować umowę (klikając "Akceptuj").
    
2. Wydać formalną opinię – w takim przypadku uruchamia proces `P_PismoWewnetrzne` (z Grupy 6), pisze w nim swoją opinię, a system (realizując `UC-KANC-WEW-002 Scenariusz B`) **automatycznie wpina tę opinię** do `Teczka_sprawy` (`BH.032.1.2025`) powiązanej z opiniowaną umową.
    

### **UC-UMOWY-006 – Akceptacja Zarządcza i Podpisanie Umowy**

**Rola:** Osoba upoważniona (Dyrektor, Członek Zarządu)

**Cel:** Ostateczne zatwierdzenie umowy i złożenie podpisu.

**Opis:** Jest to finałowy krok akceptacji, realizujący **model hybrydowy** (zgodnie z `UC-KANC-WYCH-005`):

1. **Podpis Elektroniczny:** Osoba upoważniona składa w AMODIT podpis kwalifikowany. Finalny, podpisany plik jest automatycznie zapisywany w sprawie.
    
2. **Podpis Odręczny:** System generuje finalny PDF do druku. Po zebraniu podpisów odręcznych, **skan podpisanej umowy** jest wgrywany z powrotem do sprawy AMODIT jako ostateczna wersja "ad acta".
    

### **UC-UMOWY-007 – Rejestracja podpisanej umowy i zamknięcie obiegu**

**Rola:** Inicjator / System

**Cel:** Zakończenie procesu i trwała archiwizacja umowy w jej teczce JRWA.

**Opis:**

1. Po wgraniu/złożeniu podpisanego dokumentu (`UC-UMOWY-006`), Inicjator uzupełnia ewentualne brakujące metadane (np. finalny numer umowy nadany przez kontrahenta).
    
2. Wybiera akcję "Zakończ".
    
3. System zmienia status sprawy `P_Umowa` na "Obowiązująca" / "Zamknięta".
    
4. Finalna, podpisana wersja umowy (wraz z historią obiegu i opiniami) jest trwale zapisana w `Teczka_sprawy` (`BH.032.1.2025`), która została utworzona w kroku `UC-UMOWY-002`.
    

### **UC-UMOWY-008 – Obsługa aneksów do umowy**

**Rola:** Użytkownik merytoryczny

**Cel:** Zarządzanie zmianami w umowie (aneksami) z zachowaniem pełnej ciągłości akt sprawy.

**Opis:**

1. Użytkownik odnajduje w systemie zakończoną sprawę `P_Umowa` (lub jej `Teczka_sprawy` `BH.032.1.2025`).
    
2. Wybiera akcję "Utwórz aneks".
    
3. System tworzy nową sprawę (proces `P_Aneks`), która jest **automatycznie powiązana** z tą samą `Teczka_sprawy` (`BH.032.1.2025`).
    
4. Proces `P_Aneks` przechodzi swój (zazwyczaj uproszczony) obieg akceptacji i podpisu (`UC-003` do `UC-007`).
    
5. Po zamknięciu, aneks jest dopinany do tej samej teczki, co umowa główna, realizując wymóg kompletności akt sprawy JRWA.
    

## **Najważniejsze do zapamiętania**

> Ta grupa definiuje kluczowy proces merytoryczny LOT-u.
> 
> 1. **Teczka per Umowa:** Proces ten realizuje logikę "jedna umowa = jedna `Teczka_sprawy`" (zgodnie z JRWA 1997, klasa `032`). Teczka ta jest tworzona na samym początku.
>     
> 2. **Integracja Procesów:** Proces umowy _konsumuje_ inne procesy (np. Pismo Wewnętrzne z Grupy 6 jako opinia prawna) i _mechanizmy_ (np. Wpinanie z Grupy 3, Podpis hybrydowy z Grupy 5).
>     
> 3. **Ciągłość Akt:** System musi zapewniać, że aneksy (`UC-UMOWY-008`) trafiają do **tej samej teczki**, co umowa macierzysta.
>