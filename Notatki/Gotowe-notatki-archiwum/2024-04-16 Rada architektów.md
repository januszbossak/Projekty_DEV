> 🛡️ Zweryfikowano (Review) w dniu 2025-12-03

**Powiązane projekty:**
- [[Koncepcje/Okna-dialogowe/README|Okna-dialogowe]] – tematy 1, 2, 3

---

## 1. Koncepcja Uproszczonego Okna Dialogowego

**Projekt:** `Koncepcje/Okna-dialogowe`

### Kontekst i Problem

Dyskusja dotyczyła koncepcji uproszczonego okna dialogowego, które ma służyć jako rozszerzenie obecnej funkcjonalności systemu, odpowiadając na dwie główne potrzeby i zastosowania: proste zbieranie danych oraz bardziej złożone interakcje bazujące na formularzach lub procesach.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

Dyskusja dotyczyła trzech głównych koncepcji okien dialogowych, które są traktowane jako różne zastosowania lub etapy rozwoju:

| Opcja | Opis | Powód odrzucenia/wyboru |
|---|---|---|
| Proste okno dialogowe | Brak odrębnego procesu lub reguł. Rozwinięcie "okna potwierdzania reguły ręcznej" z opcjami wyświetlania prostych pól do wypełnienia (tekst, data, liczba, użytkownik, słownik). Pola definiowane w wywołaniu, nie na formularzu. Pozwala obsłużyć bardzo proste sytuacje, gdzie dane są natychmiast używane po zamknięciu okna. | ✅ Wybrana – jako najprostsze rozwiązanie dla podstawowych interakcji. |
| Okno dialogowe na podstawie formularza | Definicja procesu typu "proces - formularz" służącego do generowania formularza do wypełnienia przez użytkownika. Wywołanie z poziomu reguł procesu (np. `ShowDialog("nazwa formularza", ...)`). Wywołanie nie tworzy sprawy z `caseID`, okno ma być uproszczone (bez prawego panelu, załączników, historii). Wynik zwracany jako obiekt JSON, konsumowany przez formularz główny. | ✅ Wybrana – dla bardziej złożonych, ale tymczasowych interakcji z danymi. |
| Okno dialogowe na podstawie procesu | Pełnoprawny proces z formularzem, regułami i diagramem. Sprawy powstają i są zapisywane w bazie danych. Okno dialogowe również maksymalnie uproszczone, podobnie jak w przypadku opcji drugiej. | ⏸️ Odroczona – jako najbardziej złożone rozwiązanie, wymagające pełnej definicji procesu. |

### Decyzja

**Status:** 💡 Propozycja

Ustalono, że istnieją trzy główne kierunki rozwoju okien dialogowych, odpowiadające na różne poziomy złożoności interakcji. Dwa pierwsze (proste okno i okno na podstawie formularza) są traktowane jako odrębne, lecz powiązane koncepcje, do dalszej analizy i wdrożenia. Opcja trzecia (na podstawie procesu) jest odroczona jako najbardziej zaawansowana.

**Szczegóły techniczne**:
- Funkcja: `ShowDialog("nazwa formularza", .... inne parametry)`
- Format danych: obiekt JSON zwracany z okna dialogowego.
- Uproszczony UI: bez większości obecnych elementów formularza sprawy, prawego panelu, załączników, spraw powiązanych, historii itp.

### Zadania

- **[Do ustalenia]:** Dalsza analiza i sprecyzowanie wymagań dla "Prostego okna dialogowego" i "Okna dialogowego na podstawie formularza".
- **[Do ustalenia]:** Określenie, jak dane z okna dialogowego mają być konsumowane przez formularz główny.

### Punkty otwarte

- Brak konkretnych osób przypisanych do zadań.
- Brak szczegółowych definicji procesów dla okien dialogowych na podstawie formularza.
- Kwestia akcji, które użytkownik może wykonać w oknie dialogowym, poza prostymi przyciskami.
