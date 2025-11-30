---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje proces "wyjścia" dokumentu z organizacji, czyli **tworzenie, akceptację i wysyłkę korespondencji własnej**. Obejmuje zarówno pisma inicjowane jako odpowiedź na korespondencję przychodzącą (z Grupy 4), jak i pisma inicjowane "od zera" przez pracowników merytorycznych.

Celem jest zapewnienie, że **każde pismo wychodzące** jest tworzone na podstawie szablonu, przechodzi formalny obieg akceptacyjny (zgodnie z § 29 Instrukcji LOT), jest poprawnie powiązane z `Teczka_sprawy` (z Grupy 2), otrzymuje poprawny znak sprawy (zgodnie z § 21), zostaje podpisane (elektronicznie lub tradycyjnie) i zarejestrowane w Rejestrze Przesyłek Wychodzących (§ 32 Instrukcji LOT).

### **UC-KANC-WYCH-001 – Inicjowanie sprawy wychodzącej (jako odpowiedź lub nowa)**

**Rola:** Użytkownik merytoryczny

**Cel:** Rozpoczęcie pracy nad nowym pismem wychodzącym, zapewniając jego natychmiastowe i poprawne powiązanie z `Teczka_sprawy`.

**Opis:** Użytkownik może zainicjować sprawę na dwa sposoby:

1. **Jako ODPOWIEDŹ:** Będąc w kontekście sprawy przychodzącej (z Grupy 4), użytkownik wybiera akcję "Odpowiedz". System automatycznie tworzy nową sprawę wychodzącą (instancję procesu `P_KorespondencjaWychodząca`) i **automatycznie przypina ją** do tej samej `Teczka_sprawy` JRWA, do której wpięte jest pismo, na które odpowiada.
    
2. **Jako NOWA SPRAWA (własna):** Użytkownik inicjuje proces `P_KorespondencjaWychodząca` "od zera". System **wymusza** na nim wykonanie `UC-JRWA-LNK-001` (wybór istniejącej teczki) lub `UC-JRWA-LNK-002` (stworzenie nowej teczki "w locie").
    

W obu przypadkach, sprawa wychodząca od początku jest poprawnie sklasyfikowana w JRWA, co jest warunkiem koniecznym do nadania jej znaku sprawy.

### **UC-KANC-WYCH-002 – Generowanie znaku sprawy dla pisma wychodzącego**

**Rola:** System / Użytkownik merytoryczny

**Cel:** Nadanie pismu wychodzącemu unikalnego, pełnego znaku sprawy zgodnego z § 21 Instrukcji Kancelaryjnej LOT.

**Opis:** Gdy tylko sprawa wychodząca zostanie powiązana z `Teczka_sprawy` (co dzieje się w `UC-KANC-WYCH-001`):

1. System pobiera **bazowy znak teczki** (np. `BA.032.1.2025` dla teczki 4-członowej lub `BK.120.7.3.2025` dla 5-członowej podteczki).
    
2. System automatycznie nadaje **kolejny numer pisma w ramach tej sprawy** (zgodnie z § 21 ust. 8 pkt 1 Instrukcji LOT), np. `.1`, `.2`, `.3`.
    
3. Opcjonalnie, system dodaje na końcu symbol prowadzącego sprawę (np. `.AW`).
    
4. Pełny znak (np. `BA.032.1.2025.1.AW`) jest zapisywany w metadanych sprawy i automatycznie wstawiany do szablonu dokumentu.
    

### **UC-KANC-WYCH-003 – Edycja treści pisma (na podstawie szablonu)**

**Rola:** Użytkownik merytoryczny

**Cel:** Stworzenie kompletnej treści dokumentu wychodzącego (pisma, odpowiedzi) przy użyciu standardów firmowych.

**Opis:** System udostępnia szablony dokumentów (np. *.docx), które automatycznie pobierają dane z AMODIT:

- Znak sprawy (wygenerowany w `UC-KANC-WYCH-002`).
    
- Dane adresata (wybrane z bazy kontrahentów lub wprowadzone ręcznie).
    
- Datę pisma.
    
- Stopkę firmową, logo itp.
    

Użytkownik uzupełnia treść merytoryczną i dodaje ewentualne załączniki (które również stają się częścią sprawy AMODIT).

### **UC-KANC-WYCH-004 – Wewnętrzny obieg akceptacyjny (Akceptacja wielostopniowa)**

**Rola:** Użytkownik merytoryczny / Przełożeni (Akceptujący)

**Cel:** Uzyskanie formalnej zgody merytorycznej i formalnej na wysyłkę pisma, zgodnie z § 29 Instrukcji LOT.

**Opis:**

1. Po przygotowaniu treści, pracownik wysyła sprawę na ścieżkę akceptacyjną.
    
2. Ścieżka może być prosta (do jednego przełożonego) lub wielostopniowa (np. Merytoryczny -> Prawny -> Dyrektor), w zależności od typu pisma lub komórki.
    
3. Akceptujący (w AMODIT) mogą:
    
    - **Zaakceptować** (przesuwając sprawę dalej).
        
    - **Odrzucić** (wracając sprawę do autora z obowiązkowym komentarzem).
        
    - **Edytować** treść (jeśli mają uprawnienia), zachowując historię wersji.
        
4. Cały obieg akceptacji odbywa się na dokumencie elektronicznym w AMODIT (§ 29 ust. 3 pkt 2 Instrukcji LOT).
    

### **UC-KANC-WYCH-005 – Złożenie podpisu (Końcowa akceptacja)**

**Rola:** Osoba upoważniona (np. Dyrektor, Członek Zarządu)

**Cel:** Ostateczne zatwierdzenie treści i nadanie jej mocy prawnej.

**Opis:** Osoba upoważniona, jako ostatni krok obiegu akceptacyjnego, składa podpis. Proces musi wspierać model hybrydowy:

1. **Podpis Elektroniczny (Preferowany):** Osoba upoważniona składa w AMODIT podpis elektroniczny (np. kwalifikowany), zgodnie z § 30 ust. 1 Instrukcji LOT. Dokument staje się finalny i jest gotowy do wysyłki elektronicznej.
    
2. **Podpis Odręczny:** Jeśli pismo _musi_ wyjść w formie papierowej z podpisem odręcznym, system generuje finalną wersję do druku. Osoba upoważniona podpisuje ją odręcznie. W tym momencie _zeskanowana, podpisana wersja_ musi być wgrana z powrotem do AMODIT jako **egzemplarz "ad acta"**, aby zachować kompletność teczki elektronicznej (zgodnie z § 29 ust. 6).
    

### **UC-KANC-WYCH-006 – Rejestracja w Rejestrze Przesyłek Wychodzących i Wysyłka**

**Rola:** Pracownik Kancelarii / Pracownik merytoryczny

**Cel:** Formalne wysłanie pisma do adresata i zaewidencjonowanie tej operacji zgodnie z § 32 Instrukcji LOT.

**Opis:** Po uzyskaniu podpisu (UC-005), sprawa trafia do etapu "Do wysyłki":

1. **Wysyłka elektroniczna (e-Doręczenia, e-mail):** System (lub pracownik Kancelarii) wysyła pismo podpisane elektronicznie. AMODIT automatycznie zapisuje dowód nadania (UPP/UPD) i odnotowuje wysyłkę w Rejestrze Przesyłek Wychodzących.
    
2. **Wysyłka papierowa (Poczta, Kurier):** Pracownik Kancelarii fizycznie nadaje podpisany odręcznie dokument. Następnie w AMODIT uzupełnia metadane:
    
    - Sposób wysyłki (np. "Polecony priorytet").
        
    - Datę nadania.
        
    - Numer nadawczy (jeśli dotyczy). System automatycznie zapisuje te dane w Rejestrze Przesyłek Wychodzących.
        

### **UC-KANC-WYCH-007 – Automatyczne zamknięcie sprawy wychodzącej i archiwizacja "ad acta"**

**Rola:** System

**Cel:** Automatyczne zakończenie obiegu sprawy AMODIT i zapewnienie kompletności teczki JRWA.

**Opis:** Po wykonaniu wysyłki (UC-006) i zarejestrowaniu jej w Rejestrze Wychodzących, system automatycznie:

1. Zmienia status sprawy AMODIT na "Zamknięta" / "Wysłana".
    
2. Zapewnia, że finalna wersja pisma (wraz z załącznikami i dowodem nadania) jest trwale i nierozerwalnie **wpięta do właściwej `Teczka_sprawy` JRWA** (do której została przypisana w `UC-KANC-WYCH-001`).
    

W ten sposób realizowany jest wymóg § 31 ust. 4 ("włącza do akt sprawy podpisany egzemplarz... ad acta") bez dodatkowej pracy użytkownika.

## **Najważniejsze do zapamiętania**

> Ta grupa definiuje **proces "produkcji" dokumentu** w LOT.
> 
> 1. **Kluczowe powiązanie:** Sprawa wychodząca **musi** być powiązana z `Teczka_sprawy` (Grupa 2) **zanim** zostanie wysłana, ponieważ to z teczki pobierany jest znak sprawy (§ 21 Instrukcji LOT).
>     
> 2. **Model hybrydowy:** Proces musi obsługiwać zarówno wysyłkę pełnej elektroniki (e-mail, e-Doręczenia z podpisem kwalifikowanym), jak i wysyłkę papierową (druk, podpis odręczny, skan "ad acta" do AMODIT).
>     
> 3. **Kompletność:** System automatycznie zamyka pętlę, zapewniając, że finalna wersja pisma "ad acta" trafia do tej samej teczki, z której pobrano znak.
>