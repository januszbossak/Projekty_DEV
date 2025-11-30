---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje pełen cykl życia obiektu `Teczka_sprawy` w systemie AMODIT. Obiekt ten jest **elektroniczną reprezentacją** teczki aktowej (w modelu hybrydowym LOT) lub teczki zbiorczej.

Celem jest odwzorowanie wszystkich formalnych czynności kancelaryjnych i archiwalnych, jakie są wykonywane na teczce – od jej założenia (zgodnie z JRWA 1997), przez prowadzenie i przypisywanie do niej spraw (z Grupy 3), aż po jej zamknięcie, przekazanie do Archiwum Zakładowego (AZ), udostępnianie, ewentualne wznowienie, finalne brakowanie (dla kat. B) lub przekazanie do Archiwum Państwowego (dla kat. A).

Te przypadki są realizowane przez **użytkowników merytorycznych, koordynatorów i archiwistów**.

### **UC-JRWA-SPR-001 – Utworzenie `Teczka_sprawy` (teczki macierzystej) ze znakiem 4-członowym**

**Rola:** Użytkownik merytoryczny / Koordynator kancelaryjny

**Cel:** Założenie nowej, rocznej teczki rzeczowej JRWA, w której będą gromadzone akta spraw (przypinane sprawy AMODIT) powiązane z daną klasą JRWA.

**Opis:** Użytkownik tworzy nową instancję procesu `Teczka_sprawy`. Wskazuje **symbol JRWA** (z obowiązującego słownika JRWA 1997, np. `032` - Umowy), **rok** (np. 2025) i **komórkę organizacyjną**.

System automatycznie nadaje **znak sprawy 4-członowy** (zgodny z § 21 ust. 3 Instrukcji Kancelaryjnej LOT), np. `BA.032.1.2025`, gdzie "1" to kolejny numer teczki z tej klasy w danym roku. System pobiera też **kategorię archiwalną** (np. BE10) i **tytuł** (np. "Zbiory umów krajowych...") ze słownika JRWA (Grupa 1).

Teczka może być utworzona bezpośrednio lub „w locie” z formularza sprawy AMODIT (np. „Utwórz nową teczkę JRWA”).

Od tego momentu teczka staje się formalnym kontenerem dla spraw i jest gotowa do przekazania do AZ po jej zamknięciu. W modelu hybrydowym LOT, ta teczka w AMODIT jest elektroniczną reprezentacją teczki papierowej.

### **UC-JRWA-SPR-001a – Utworzenie Podteczki (wydzielonej grupy spraw) ze znakiem 5-członowym**

**Rola:** Użytkownik merytoryczny / Koordynator kancelaryjny

**Cel:** Założenie nowej teczki przedmiotowej (podteczki) dla konkretnego obiektu (np. pracownika, komisji, nieruchomości), zgodnie z wymogiem w kolumnie "Uwagi" JRWA 1997.

**Opis:** Jeśli reguła biznesowa (zdefiniowana w Grupie 1, UC-005) dla danej klasy JRWA (np. `120` - Akta osobowe) nakazuje tworzenie podteczek, proces jej tworzenia jest inny:

1. Użytkownik najpierw tworzy lub wskazuje "Sprawę-matkę" (teczkę 4-członową, np. `BK.120.1.2025` o tytule "Akta osobowe").
    
2. Następnie, w ramach tej sprawy-matki, zakłada nową `Teczka_sprawy` (podteczkę), podając jej unikalny tytuł (np. "Jan Kowalski").
    
3. System automatycznie nadaje **znak sprawy 5-członowy** (zgodny z § 21 ust. 5 Instrukcji Kancelaryjnej LOT), np. `BK.120.1.15.2025` (gdzie "15" to 15-ta podteczka w ramach sprawy-matki nr 1).
    

Podteczka dziedziczy kategorię archiwalną po klasie JRWA. Wszystkie sprawy AMODIT (np. wnioski urlopowe, umowy) dla Jana Kowalskiego będą wpinane do tej podteczki.

### **UC-JRWA-SPR-002 – Utworzenie Teczki zbiorczej dla dokumentacji nietworzącej akt sprawy**

**Rola:** Użytkownik merytoryczny / Koordynator kancelaryjny

**Cel:** Założenie rocznej teczki zbiorczej (segregatora) do grupowania dokumentacji, która zgodnie z Instrukcją Kancelaryjną LOT (§ 22) **nie tworzy akt sprawy** (np. faktury, listy obecności).

**Opis:** Jest to proces zgodny z logiką AMODIT, w której "wszystko jest sprawą".

1. Użytkownik tworzy instancję `Teczka_sprawy` jako teczkę zbiorczą (segregator).
    
2. Wskazuje właściwą klasę JRWA (np. `340` - Dowody księgowe).
    
3. System **nie nadaje numeru sprawy** ze spisu spraw (zgodnie z § 22 ust. 1 Instrukcji LOT).
    
4. Teczka otrzymuje tylko oznaczenie klasy (np. `BF.340.2025`) i pobiera kategorię archiwalną (np. B5).
    

Do tak utworzonej teczki zbiorczej wpinane są **sprawy AMODIT** (np. 100 instancji procesu `P_Faktura`). Te "sprawy-faktury" są traktowane jako pojedyncze dokumenty ewidencyjne; mają swoje metadane (opis), ale **nie otrzymują własnego znaku sprawy** w rozumieniu kancelaryjnym. Teczka ta, wraz z przypiętymi sprawami, podlega normalnemu cyklowi życia (zamknięcie, archiwizacja, brakowanie).

### **UC-JRWA-SPR-003 – Rejestracja i podgląd listy aktywnych teczek JRWA**

**Rola:** Użytkownik merytoryczny / Archiwista / Koordynator kancelaryjny   **Cel:** Wyszukanie i przegląd teczek JRWA (macierzystych, podteczek i zbiorczych) w celu uzyskania informacji o ich statusie i zawartości.

**Opis:** System udostępnia widok rejestru `Teczka_sprawy` z filtrami po symbolu JRWA, znaku sprawy, roku, komórce, kategorii archiwalnej i statusie.

Użytkownik może otworzyć formularz teczki w trybie podglądu, zobaczyć metadane (znak sprawy, tytuł, rok, status, kategoria) oraz **listę spraw AMODIT przypiętych do tej teczki** (w przypadku UC-001 i UC-001a) lub listę spraw/dokumentów (w przypadku UC-002).

Archiwista i koordynator mają pełny wgląd we wszystkie teczki; użytkownicy merytoryczni – tylko w zakresie swojej komórki lub uprawnień operacyjnych (zgodnie z Kompendium, Rozdział 10).

### **UC-JRWA-SPR-004 – Edycja i aktualizacja metadanych Teczka_sprawy**

**Rola:** Koordynator kancelaryjny / Archiwista / Administrator JRWA

**Cel:** Korekta lub aktualizacja danych opisowych teczki w celu utrzymania zgodności z JRWA i rzeczywistym stanem spraw.

**Opis:** Uprawnione osoby mogą edytować pola opisowe teczki (tytuł, komórka prowadząca, rok, osoba prowadząca).

Zmiany dotyczące symbolu JRWA i kategorii archiwalnej (np. po ekspertyzie archiwalnej) mogą być dokonywane tylko przez Administratora JRWA lub Archiwistę.

System prowadzi pełną historię zmian („kto, kiedy, co zmienił”), umożliwiając audyt i porównanie z pierwotnym stanem.

### **UC-JRWA-SPR-005 – Zamknięcie Teczka_sprawy**

**Rola:** Koordynator kancelaryjny / Użytkownik merytoryczny

**Cel:** Zakończenie prowadzenia teczki (z końcem roku kalendarzowego lub po zakończeniu sprawy) i przygotowanie jej do przekazania do archiwum.

**Opis:** Po zakończeniu wszystkich spraw przypiętych do teczki (lub z końcem roku dla teczek zbiorczych), użytkownik zmienia jej status na „Zamknięta”.

System weryfikuje, czy wszystkie powiązane sprawy AMODIT są również zamknięte i czy nie pozostają w obiegu aktywne dokumenty.

Status "Zamknięta" jest warunkiem wstępnym do rozpoczęcia biegu **2-letniego okresu oczekiwania** na przekazanie do AZ (zgodnie z § 37 ust. 1 Instrukcji Kancelaryjnej LOT).

### **UC-JRWA-SPR-006 – Przekazanie Teczka_sprawy do Archiwum Zakładowego (AZ)**

**Rola:** Koordynator kancelaryjny / Archiwista

**Cel:** Formalne przekazanie zamkniętej teczki do Archiwum Zakładowego po upływie wymaganego 2-letniego okresu.

**Opis:** Po upływie 2 lat od zamknięcia, system oznacza teczkę jako gotową do przekazania. Koordynator generuje z AMODIT **Spis zdawczo-odbiorczy** (zgodny z § 39 Instrukcji Kancelaryjnej LOT), grupujący teczki.

Archiwista weryfikuje spis i fizyczne teczki (w modelu hybrydowym). Jeśli wszystko się zgadza, zatwierdza przyjęcie w systemie. Jeśli nie (np. błędy, braki, niezgodność opisu), **odmawia przejęcia** (§ 37 ust. 4 Instrukcji Kancelaryjnej LOT) i zwraca proces do koordynatora z komentarzem.

Po zatwierdzeniu, system nadaje teczce status „Archiwalna”, a Archiwista uzupełnia pole **Sygnatura Archiwalna** (zgodnie z § 15 ust. 2 pkt 5 Instrukcji Archiwalnej LOT). Teczka staje się nieedytowalna.

### **UC-JRWA-SPR-007 – Wznowienie Teczka_sprawy (Wycofanie z AZ)**

   **Rola:** Archiwista / Koordynator kancelaryjny    **Cel:** Ponowne otwarcie zarchiwizowanej teczki (lub formalne wycofanie jej z ewidencji AZ) w celu kontynuacji akt sprawy.

**Opis:** W uzasadnionych przypadkach (np. wznowienie postępowania), Kierownik Komórki wnioskuje do Archiwisty o wznowienie teczki.

Archiwista (zgodnie z § 30-31 Instrukcji Archiwalnej LOT) zmienia status teczki na „Wznowiona” lub "Wycofana" i przekazuje ją z powrotem do komórki merytorycznej.

System umożliwia ponowne dodawanie spraw AMODIT do teczki. Historia wznowień jest widoczna dla audytu. Po ponownym zamknięciu teczki, 2-letni cykl przekazania do AZ rozpoczyna się od nowa.

### **UC-JRWA-SPR-008 – Wnioskowanie o udostępnienie teczki z AZ (Papier / Elektronika)**

**Rola:** Użytkownik merytoryczny / Archiwista / Kierownik Komórki / Prezes Zarządu

**Cel:** Umożliwienie pracownikom LOT lub podmiotom zewnętrznym bezpiecznego i ewidencjonowanego dostępu do zarchiwizowanych akt, zgodnie z § 26-29 Instrukcji Archiwalnej LOT.

**Opis:** To kluczowy proces obsługi zasobu AZ, oparty na ustaleniach ze spotkania (Kompendium § 13.3):

1. Użytkownik (lub pracownik kancelarii w imieniu podmiotu zewnętrznego) inicjuje **jeden proces "Wniosek o udostępnienie"**.
    
2. We wniosku wskazuje teczkę (po sygnaturze lub znaku sprawy) oraz **żądaną formę**: **Papierowa** (oryginał) lub **Elektroniczna** (skan).
    
3. System automatycznie kieruje wniosek do akceptacji:
    
    - **Wniosek wewnętrzny:** Akceptuje **Kierownik Komórki**, która wytworzyła akta.
        
    - **Wniosek zewnętrzny:** Akceptuje **Prezes / Członek Zarządu**.
        
4. Po akceptacji, Archiwista realizuje wniosek:
    
    - **Dla formy elektronicznej:** Nadaje wnioskodawcy (lub grupie osób) czasowy (np. 30 dni) dostęp do wglądu w akta w AMODIT. System **automatycznie cofa dostęp** po terminie.
        
    - **Dla formy papierowej:** Fizycznie wydaje teczkę, odnotowując ten fakt w AMODIT. Po zwrocie oryginału oryginału, Archiwista **ręcznie potwierdza zwrot** w systemie.
        
5. Każda czynność (wniosek, akceptacja, wydanie, zwrot) jest logowana w ewidencji udostępnień.
    

### **UC-JRWA-SPR-009 – Brakowanie teczki niearchiwalnej (Kat. B)**

**Rola:** Archiwista / Kierownik Komórki

**Cel:** Formalne zniszczenie dokumentacji niearchiwalnej (Kat. B) po upływie wymaganego okresu przechowywania (np. B5, B10, BE10).

**Opis:** Proces ten jest zgodny z Rozdziałem 10 Instrukcji Archiwalnej LOT:

1. **Typowanie:** AMODIT automatycznie generuje raport "Teczki do brakowania w roku X", bazując na kategorii archiwalnej i dacie zamknięcia teczki.
    
2. **Inicjowanie:** Archiwista, na podstawie raportu, tworzy **Spis dokumentacji do wybrakowania** (§ 32 ust. 2).
    
3. **Opinia:** System wysyła spis do **Kierowników Komórek**, którzy mogą zaopiniować spis lub zawnioskować o wydłużenie okresu przechowywania (§ 32 ust. 3-4).
    
4. **Akceptacja Zewnętrzna:** Po uzyskaniu opinii, Archiwista wysyła spis do akceptacji **Archiwum Państwowego**.
    
5. **Zniszczenie:** Po otrzymaniu zgody, Archiwista odnotowuje w AMODIT datę zniszczenia i numer zgody (§ 35 ust. 1). Teczka zmienia status na "Zbrakowana" i znika z aktywnych rejestrów, pozostając w logach systemowych.
    

### **UC-JRWA-SPR-010 – Przekazanie teczki kat. A do Archiwum Państwowego (AP)**

**Rola:** Archiwista

**Cel:** Formalne przygotowanie i przekazanie materiałów archiwalnych (teczek Kat. A), którym minął okres przechowywania w Archiwum Zakładowym, do właściwego Archiwum Państwowego (zgodnie z `WK50` i `WK68`).

**Opis:** Jest to końcowy etap cyklu życia materiałów archiwalnych (Kat. A), zgodny z Rozdziałem 11 Instrukcji Archiwalnej LOT oraz wymaganiami `WK50` i `WK68`:

1. **Typowanie:** AMODIT automatycznie generuje raport "Materiały archiwalne (Kat. A) do przekazania do AP".
    
2. **Generowanie Spisu:** Archiwista inicjuje proces i generuje w systemie **Spis zdawczo-odbiorczy** w formacie elektronicznym wymaganym przez Archiwum Państwowe (zgodnie z `WK68b`).
    
3. **Eksport Paczki Archiwalnej:** System musi umożliwiać **eksport teczek (dokumentów i metadanych)** w uzgodnionym formacie (paczka archiwalna, zgodnie z `WK68c`), aby przekazać je do AP.
    
4. **Oznaczenie w systemie:** Po formalnym przejęciu materiałów przez AP, Archiwista zmienia status teczek w AMODIT na **"Przekazana do AP"**. Spowoduje to "zamrożenie" teczek, uniemożliwiając ich edycję, brakowanie czy wznowienie, ale zachowując je w systemie do celów ewidencyjnych (zgodnie z `WK68d`).
    

## **Najważniejsze do zapamiętania**

> **`Teczka_sprawy`** w AMODIT odwzorowuje formalny byt JRWA (zgodny z Instrukcją LOT) i obejmuje trzy typy:
> 
> 1. **Teczkę macierzystą** (4-członowy znak, tworząca akta sprawy),
>     
> 2. **Podteczkę** (5-członowy znak, wydzielona grupa spraw, tworząca akta sprawy),
>     
> 3. **Teczkę zbiorczą** (oznaczenie klasą, nietworząca akt sprawy, ale gromadząca "sprawy" AMODIT, np. faktury).
>     
> 
> Każda teczka ma pełny cykl życia: utworzenie → prowadzenie → zamknięcie → (oczekiwanie 2 lata) → przekazanie do AZ → (udostępnianie / wznowienie) → **brakowanie (dla Kat. B)** lub **przekazanie do AP (dla Kat. A)**.
> 
> Dla konsultantów wdrożeniowych: proces `Teczka_sprawy` to rdzeń odwzorowania JRWA – łączy logikę kancelaryjną, archiwalną i workflow w jeden spójny mechanizm systemowy.