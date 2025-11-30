---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) ma charakter **techniczny i jednorazowy**. Jej celem jest realizacja wymogu **`WK58`** z Załącznika EZD: _"Import... danych historycznych... import teczek spraw... ze starego systemu..."_.

Obejmuje ona proces analizy, transformacji i załadowania (ETL) istniejącego zasobu kancelaryjno-archiwalnego LOT do nowo wdrożonego systemu AMODIT. Celem jest zapewnienie **ciągłości zasobu** dla Archiwisty i użytkowników merytorycznych, aby mogli oni wyszukiwać i zarządzać sprawami zakończonymi _przed_ uruchomieniem AMODIT.

Migracja ta dotyczy **wyłącznie teczek i spraw już zamkniętych (historycznych)** i nie obejmuje spraw "w toku".

### **UC-MIG-001 – Analiza i Mapowanie Danych Źródłowych**

**Rola:** Zespół Wdrożeniowy AMODIT / Archiwista LOT

**Cel:** Zrozumienie struktury danych w starym systemie (`WK58`) i przygotowanie mapowania na nową strukturę AMODIT (Grupy 1, 2 i 3).

**Opis:**

1. Zespół AMODIT otrzymuje dostęp (np. zrzut bazy danych, eksporty CSV) do starego systemu.
    
2. Wspólnie z Archiwistą LOT dokonywana jest analiza:
    
    - Jak w starym systemie reprezentowana jest `Teczka_sprawy`?
        
    - Jak reprezentowana jest pojedyncza "sprawa" (dokument)?
        
    - Jak powiązane są metadane (Nadawca, Adresat, Daty)?
        
    - Jak (i czy) stary system mapował klasy do **JRWA 1997**?
        
3. Wynikiem jest **dokument mapowania** (np. "Stare pole `X` -> Nowe pole `Y`", "Stara klasa `12/A` -> Nowa klasa `010`").
    

### **UC-MIG-002 – Przygotowanie Skryptów Transformacyjnych (ETL)**

**Rola:** Zespół Wdrożeniowy AMODIT

**Cel:** Stworzenie narzędzi do automatycznej konwersji danych historycznych na format importowalny przez AMODIT.

**Opis:**

1. Na podstawie dokumentu mapowania (`UC-MIG-001`), deweloperzy AMODIT przygotowują skrypty (SQL, Python, C#).
    
2. Skrypty te muszą:
    
    - Odczytać dane źródłowe.
        
    - Wyczyścić "brudne" dane (np. zunifikować format dat, poprawić kodowanie znaków).
        
    - Przekształcić starą strukturę na nową (np. stworzyć obiekty `Teczka_sprawy` i powiązać z nimi sprawy).
        
    - Wygenerować pliki wsadowe (np. CSV/XML) gotowe do importu przez AMODIT.
        

### **UC-MIG-003 – Import (Załadowanie) Teczek i Spraw Historycznych**

**Rola:** Zespół Wdrożeniowy AMODIT

**Cel:** Fizyczne utworzenie w systemie AMODIT historycznych teczek i spraw.

**Opis:**

1. Uruchomienie skryptów importujących na środowisku testowym.
    
2. Skrypty automatycznie tworzą w AMODIT:
    
    - **Historyczne `Teczka_sprawy`** (zgodnie z `UC-JRWA-SPR-001/001a/002`), nadając im status "Archiwalna (Import)" oraz wypełniając pole `ID_ZE_STAREGO_SYSTEMU`.
        
    - **Historyczne "Sprawy AMODIT"** (np. jako instancje procesu `P_PismoArchiwalne`), nadając im status "Zamknięta (Import)" i automatycznie wpinając je (`UC-JRWA-LNK-001`) do odpowiednich teczek historycznych.
        
3. Wszystkie oryginalne metadane (daty, opisy, nadawcy) są importowane do odpowiednich pól w AMODIT.
    

### **UC-MIG-004 – Import Powiązanych Skanów / Załączników**

**Rola:** Zespół Wdrożeniowy AMODIT

**Cel:** Powiązanie zaimportowanych metadanych (`UC-MIG-003`) z ich cyfrowymi obrazami (skanami).

**Opis:**

1. Skrypty migracyjne muszą odczytać skany/załączniki ze starego systemu (np. z serwera plików).
    
2. Podczas importu sprawy (`UC-MIG-003`), system musi automatycznie dołączyć do niej odpowiedni plik (np. `faktura_123.pdf`) na podstawie identyfikatora (`ID_ZE_STAREGO_SYSTEMU`).
    
3. Wszystkie załączniki są ładowane do repozytorium AMODIT.
    

### **UC-MIG-005 – Walidacja i Korekta Danych Po Imporcie**

**Rola:** Zespół Wdrożeniowy AMODIT / Archiwista LOT

**Cel:** Potwierdzenie poprawności i kompletności migracji przed uruchomieniem produkcyjnym.

**Opis:**

1. Po zakończeniu importu na środowisku testowym, Archiwista LOT dokonuje walidacji wyrywkowej.
    
2. Sprawdza np. 10 losowych teczek: "Czy teczka `BA.010.1.2023` w AMODIT zawiera te same 5 pism, które miała w starym systemie?".
    
3. Zgłasza ewentualne błędy (np. złe mapowanie klasy, brakujące załączniki).
    
4. Zespół AMODIT poprawia skrypty (`UC-MIG-002`) i powtarza proces (`UC-MIG-003`, `004`) aż do uzyskania pełnej zgodności.
    
5. Ostatnim krokiem jest uruchomienie finalnych skryptów na środowisku produkcyjnym (podczas "okna serwisowego" tuż przed Go-Live).
    

## **Najważniejsze do zapamiętania**

> Ta grupa jest kluczowa dla **ciągłości historycznej** Archiwum Zakładowego i realizuje wymóg **`WK58`**.
> 
> 1. **Jednorazowość:** Proces jest wykonywany tylko raz, przed startem produkcyjnym.
>     
> 2. **Statusy:** Wszystkie importowane obiekty muszą mieć statusy historyczne (np. "Zamknięta (Import)", "Archiwalna (Import)"), aby nie mieszały się z bieżącymi sprawami operacyjnymi (z Grup 4, 5, 6).
>     
> 3. **Kluczowe powiązanie:** Najważniejsze jest zachowanie relacji `Teczka_sprawy` -> `Sprawa AMODIT` -> `Załącznik (skan)` oraz poprawne zmapowanie starej klasyfikacji na nowy **JRWA 1997**.
>