# CHANGELOG - Integracja Google OCR (Vasco)

Historia ustaleń i zmian dla projektu.

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
