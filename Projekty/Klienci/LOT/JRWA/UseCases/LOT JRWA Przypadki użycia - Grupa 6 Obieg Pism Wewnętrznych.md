---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje procesy związane z tworzeniem, obiegiem i klasyfikacją dokumentów służących do formalnej komunikacji **wewnętrznej** w LOT (np. notatki służbowe, wnioski wewnętrzne, polecenia, komunikaty).

Celem jest zapewnienie, że dokumenty te również są zarządzane w AMODIT, przechodzą odpowiedni (zazwyczaj uproszczony) obieg akceptacyjny, są dystrybuowane do adresatów i – co kluczowe – są poprawnie klasyfikowane w JRWA.

Większość spraw z tej grupy będzie zasilać **Teczki zbiorcze** (zgodnie z `UC-JRWA-SPR-002`, np. jako dokumentacja `Bc` lub `B5`), ale system musi też pozwalać na wpięcie pisma wewnętrznego (np. opinii prawnej) do merytorycznej `Teczka_sprawy` (np. teczki umowy).

### **UC-KANC-WEW-001 – Inicjowanie pisma wewnętrznego**

**Rola:** Użytkownik merytoryczny (każdy pracownik)

**Cel:** Stworzenie nowej sprawy AMODIT (np. notatki, wniosku, polecenia) przeznaczonej do obiegu wewnętrznego.

**Opis:**

1. Użytkownik inicjuje proces `P_PismoWewnetrzne`.
    
2. Wybiera adresatów (pracowników lub komórki organizacyjne LOT) oraz, opcjonalnie, osoby "Do wiadomości".
    
3. Tworzy treść dokumentu (korzystając z edytora lub prostego szablonu) i dodaje ewentualne załączniki.
    
4. Przed wysłaniem musi wykonać klasyfikację (zgodnie z `UC-KANC-WEW-002`).
    

### **UC-KANC-WEW-002 – Kontekstowa klasyfikacja (wpinanie) pisma wewnętrznego**

**Rola:** Użytkownik merytoryczny (Inicjator)

**Cel:** Poprawne zaklasyfikowanie pisma wewnętrznego w strukturze JRWA, zgodnie z jego charakterem (merytorycznym lub pomocniczym).

**Opis:** System wymusza (`UC-JRWA-LNK-004`), aby Inicjator przed wysłaniem pisma przypiął je do `Teczka_sprawy`:

1. **Scenariusz A (Standardowy - "Pomocniczy"):** Jeśli jest to typowa korespondencja wewnętrzna (notatka, wniosek urlopowy, polecenie), pracownik wpina ją do odpowiedniej **Teczki zbiorczej** (zgodnie z `UC-JRWA-SPR-002`), np. do klasy `0150` (Ewidencja obiegu) lub `151` (Absencje) z JRWA 1997. Pismo _nie otrzymuje_ własnego znaku sprawy, jest tylko częścią teczki zbiorczej.
    
2. **Scenariusz B (Merytoryczny - "Do akt sprawy"):** Jeśli pismo wewnętrzne jest istotną częścią większej sprawy (np. opinia prawna do umowy, notatka z negocjacji), pracownik wpina je do istniejącej `Teczka_sprawy` (macierzystej lub podteczki), np. do teczki `BA.032.1.2025` (Umowy). Pismo jest traktowane jako część akt tej sprawy.
    

Wybór scenariusza zależy od decyzji merytorycznej pracownika.

### **UC-KANC-WEW-003 – Uproszczony obieg akceptacyjny**

**Rola:** Użytkownik merytoryczny / Przełożony

**Cel:** Uzyskanie akceptacji przełożonego dla treści pisma wewnętrznego, jeśli jest to wymagane przez procedurę.

**Opis:**

1. Po przygotowaniu treści (`UC-001`) i klasyfikacji (`UC-002`), Inicjator może wysłać pismo do akceptacji swojego przełożonego (lub innej wskazanej osoby).
    
2. Przełożony otrzymuje zadanie w AMODIT, może zaakceptować treść lub ją odrzucić (zwrócić do poprawy z komentarzem).
    
3. Dla wielu pism wewnętrznych (np. prosta notatka "do wiadomości") ten krok może być pominięty, a pismo wysłane bezpośrednio do adresata.
    

### **UC-KANC-WEW-004 – Dystrybucja i potwierdzenie odbioru**

**Rola:** System / Adresat (Odbiorca)

**Cel:** Dostarczenie pisma wewnętrznego do adresatów i uzyskanie potwierdzenia zapoznania się z treścią (jeśli jest wymagane).

**Opis:**

1. Po akceptacji (lub od razu, jeśli `UC-003` jest pominięty), system wysyła zadanie AMODIT do wszystkich adresatów wskazanych w polu "Do" oraz "DW".
    
2. Proces może być skonfigurowany na dwa sposoby:
    
    - **Proste "Do wiadomości":** Adresat otrzymuje powiadomienie, otwiera sprawę i system automatycznie odnotowuje ten fakt.
        
    - **Wymagane potwierdzenie:** Adresat musi kliknąć przycisk "Potwierdzam zapoznanie się", aby zamknąć swój obieg.
        
3. Inicjator sprawy ma podgląd, kto już zapoznał się z pismem, a kto jeszcze nie.
    

### **UC-KANC-WEW-005 – Zamknięcie obiegu pisma wewnętrznego**

**Rola:** System / Inicjator

**Cel:** Automatyczne lub ręczne zakończenie cyklu życia sprawy wewnętrznej.

**Opis:**

1. System automatycznie zamyka sprawę (zmienia status na "Załatwiona" / "Zamknięta"), gdy ostatni adresat potwierdzi odbiór (w wariancie z potwierdzeniem).
    
2. W wariancie prostym "do wiadomości", system zamyka sprawę natychmiast po wysłaniu.
    
3. Inicjator może również ręcznie zamknąć sprawę w dowolnym momencie (np. gdy uzna, że cel informacyjny został osiągnięty).
    
4. Zamknięcie sprawy AMODIT zapewnia jej trwałe wpięcie do `Teczka_sprawy` wybranej w `UC-KANC-WEW-002`.
    

## **Najważniejsze do zapamiętania**

> Ta grupa domyka podstawowe procesy kancelaryjne (Przychodzące, Wychodzące, Wewnętrzne).
> 
> 1. **Elastyczność klasyfikacji:** Kluczowy jest `UC-KANC-WEW-002`, który pozwala pracownikowi zdecydować, czy pismo jest tylko pomocniczą notatką (i trafia do "teczki zbiorczej"), czy istotną częścią merytorycznej sprawy (i trafia do "teczki macierzystej").
>     
> 2. **Prostota:** Obieg ten powinien być znacznie lżejszy (mniej metadanych, prostsze akceptacje) niż korespondencja zewnętrzna.
>     
> 3. **Ewidencja:** Zapewnia, że _każda_ formalna komunikacja w firmie jest zarejestrowana i poprawnie zarchiwizowana.
>