# CHANGELOG - Integracja Google OCR (Vasco)

Historia ustaleń i zmian dla projektu.

---

## 2025-12-05 | Roadmapa Update

**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-05 Roadmapa.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-05%20Roadmapa.md)

**Kategoria:** #Wydanie #Roadmap

- Integracja Google LLM potwierdzona jako ukończona w Q4 2025
- Zrealizowane wczoraj (4 grudnia), można wyrzucić z roadmapy
- Rozszerzenie integracji z modelami LLM o rozwiązania Google
- Projekt zrealizowany dla klienta Vasco, rozwija produkt

---

## 2025-12-09 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-09 Postęp roadmapy.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-09%20Postęp%20roadmapy.md)
**Kategoria:** #Funkcjonalność #Wydanie

- **Dostęp do AI OCR:** Vasco ma dostęp do AI OCR na obu środowiskach, Google OCR podpięty przez Mateusza, mikroserwis podpisany na weekendzie, na razie tylko OCR (nie ASK), jest o krok od włączenia ASK

---

## 2025-12-04 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-04 Spotkanie projektowe - AMODIT AI.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-04%20Spotkanie%20projektowe%20-%20AMODIT%20AI.md)
**Kategoria:** #Funkcjonalność #Architektura #Decyzja

- **OCR dla Vasco - integracja z Google Gemini** - najwyższy priorytet (ryzyko utraty klienta):
  - **Kontekst biznesowy:** Vasco generuje ~80k zł rocznie, rozważa odejście do konkurencji z powodu słabego OCR (Azure Document Intelligence)
  - **Spotkanie z klientem:** 25.10.2025 - ustalono możliwość pozostania jeśli zostanie wdrożone Google OCR
  - **Status:** Minął ponad miesiąc od spotkania - klient może stracić cierpliwość
  - **Testy klienta:** faktury których Azure nie rozczytał żadnej poprawnie, Gemini rozczytał 90% poprawnie
  - **Klient dostarczył:** gotowy prompt do testów, Google gotowe do wsparcia technicznego (spotkanie z przedstawicielami)

**Decyzja - zatwierdzone (priorytet najwyższy):**

**Minimalna integracja (PoC):**
- Osobna integracja w mikroserwisie OCR (wybór modelu: OCR google'owy)
- Wysyłanie całego PDF-a do Gemini (zamiast tylko wyników z Document Intelligence)
- Użycie prompta dostarczonego przez klienta Vasco
- Zwracanie surowych wyników w postaci tekstu (bez mapowania na pola AMODIT)

**Cel etapu 1:**
- Pokazać klientowi: "działa na Google Gemini z waszym promptem"
- Porównać faktury które źle się odczytują: Azure vs Google
- Sprawdzić czy Google rzeczywiście odczytuje lepiej

**Dalsze prace (jeśli test się uda):**
- Mapowanie wyników na pola AMODIT (schemat jak obecnie)
- Wdrożenie heurystyk (jak obecnie w Azure)
- Przerobienie prompta na format AMODIT (ręcznie lub przez AI)

**Szczegóły techniczne:**
- Model: Google Gemini 1.5 lub Flash (bardziej uniwersalny i tańszy niż Document AI)
- Prompt: dostarczony przez Vasco (Mateusz Kisiel ma)
- Integracja: przez proxy w mikroserwisie (jak obecnie Azure)
- Konto Google: trial (Mateusz utworzy nowe konto)
- Koszt: klient bierze na siebie (stwierdził że nie będą wyższe niż Azure)
- Gemini ma dostęp do pełnej struktury dokumentu i układu graficznego

**Priorytetyzacja zadań AI:**
1. **Vasco OCR (Google Gemini)** - najwyższy priorytet
2. Generowanie dokumentacji - dalsze dopracowanie
3. MCP - później

**Ograniczenia (poza zakresem PoC):**
- Brak mapowania na pola AMODIT (surowe dane)
- Brak heurystyk
- Brak produkcyjnej integracji (najpierw test)

**Zadania:**
- **Mateusz Kisiel:** Zająć się integracją z Google Gemini dzisiaj (4.12) - priorytet najwyższy
- **Mateusz Kisiel:** Utworzyć konto Google (trial) do testów
- **Przemysław Sołdacki:** W razie potrzeby zadzwonić do Google (opiekun) i założyć konto firmowe
- **Przemysław Sołdacki:** Po sukcesie podpisać umowę partnerską z Google
- **Janusz Bossak:** W razie niejasności pisać do osoby z Vasco odpowiedzialnej za rozwój

**Punkty otwarte:**
- Czy Gemini rzeczywiście działa lepiej? (według klienta tak, trzeba zweryfikować na produkcyjnych fakturach)
- Jaki będzie finalny koszt dla klientów?
- Czy przejdziemy na Google z Azure globalnie, jeśli się okaże że jest dużo lepszy?

**Ryzyka:**
- Utrata klienta Vasco (~80k zł ARR) jeśli nie wdrożymy
- Opóźnienie wdrożenia (minął już miesiąc)
- Wyższe koszty Google (wysyłanie całego PDF-a może być droższe)
- Niedziałające rozwiązanie ("nie umiecie tego robić" → odejście klienta)

---

## 2025-12-02 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-02 Spotkanie projektowe - AMODIT UI.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-02%20Spotkanie%20projektowe%20-%20AMODIT%20UI.md)
**Kategoria:** #Funkcjonalność #Integracja

- **Integracja z Google Gemini dla OCR** - główny projekt dla klienta Vasco:
  - Klient Vasco wykonał PoC z Gemini i chce używać tego modelu zamiast Azure OCR
  - Podłączenie Google Gemini: 1-2 dni (Mateusz)
  - Rozważane podejścia:
    - **Transformacja formatu Gemini → format Azure** (prostsze - aby heurystyki zadziałały)
    - Przepisanie heurystyk dla formatu Gemini (bardziej czasochłonne - odroczone)
    - Użycie promptu klienta (LLM od początku, nie model OCR - do przetestowania)
  - Obecny proces AMODIT: model visionowy + model do paragonów → LLM 4.1 (uzupełnianie) → heurystyki (tabele, sumy, VAT)
  - Nowy proces (Gemini): LLM od początku (nie model OCR) → transformacja formatu → heurystyki
  - Wartość biznesowa: utrzymanie klienta Vasco (kilkadziesiąt tysięcy zł rocznie)
  - Dodatkowa korzyść: możliwość chwalenia się współpracą z różnymi modelami (Google, OpenAI, Azure)
  - Google Gemini może być tańszy niż dedykowany model OCR

**Zadania:**
- **Mateusz:** Podłączyć Google Gemini (1-2 dni)
- **Zespół:** Przetestować z promptem klienta lub własnym
- **Zespół:** Zdecydować czy transformacja formatu wystarczy czy trzeba przepisać heurystyki

**Punkty otwarte:**
- Czy transformacja formatu wystarczy czy trzeba przepisać heurystyki?
- Czy Google Gemini będzie tańszy niż Azure OCR?

---
