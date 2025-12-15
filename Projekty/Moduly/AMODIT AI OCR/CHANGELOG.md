# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-12-04 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-04 Spotkanie projektowe - AMODIT AI.md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-04%20Spotkanie%20projektowe%20-%20AMODIT%20AI.md)
**Kategoria:** #Architektura
**Projekt:** [Klienci/Vasco/Integracja-Google-OCR](../../Klienci/Vasco/Integracja-Google-OCR/)

- **Alternatywny model OCR - Google Gemini:**
  - Integracja z Google Gemini jako alternatywa dla Azure Document Intelligence
  - Model: Gemini 1.5 / Flash (bardziej uniwersalny, tańszy niż Document AI)
  - Wysyłanie całego PDF-a do LLM (dostęp do struktury dokumentu i układu graficznego)
  - PoC dla klienta Vasco (pełne informacje w projekcie klienckim powyżej)
  - Jeśli się sprawdzi - możliwość globalnego przejścia z Azure na Google

---

## 2025-12-02 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-02 Spotkanie projektowe - AMODIT UI.md]
**Kategoria:** #Funkcjonalność #Integracja
**Projekt:** [Klienci/Vasco/Integracja-Google-OCR](../../Klienci/Vasco/Integracja-Google-OCR/)

- **Integracja z Google Gemini dla OCR (Vasco)** - alternatywny model OCR:
  - Klient Vasco wykonał PoC z Gemini i chce używać tego modelu zamiast Azure OCR
  - Podłączenie Google Gemini: 1-2 dni (Mateusz)
  - Rozważane podejścia:
    - Transformacja formatu Gemini → format Azure (aby heurystyki zadziałały)
    - Przepisanie heurystyk dla formatu Gemini (bardziej czasochłonne)
    - Użycie promptu klienta (LLM od początku, nie model OCR)
  - Wartość biznesowa: utrzymanie klienta Vasco (kilkadziesiąt tysięcy zł rocznie)
  - Dodatkowa korzyść: możliwość chwalenia się współpracą z różnymi modelami (Google, OpenAI, Azure)
  - Google Gemini może być tańszy niż dedykowany model OCR

---

## 2025-11-25 | Design OCR i Transkrypcje
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-25 Design OCR i Transkrypcje.md]
**Kategoria:** #Decyzja #Architektura

- **Potwierdzenie braku OCR On-Premise:** Obecne modele lokalne (np. Llama) są zbyt słabe i wymagają drogiego sprzętu, by dorównać chmurze.
- Decyzja o kontynuacji wykorzystania modeli chmurowych (GPT-4o mini + modele dokumentowe).
- Wdrożenie on-premise rozważane tylko przy skali milionów dokumentów.

---

## 2025-11-04 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-04 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Decyzja #Zadanie #Optymalizacja

- Zapobieganie wielokrotnemu wysyłaniu tych samych plików do AI OCR (koszty 20 000 zł).
- Wprowadzone zabezpieczenia: AMODIT (parametr `force`) i OCR (lista hashy).
- Zadania dla Piotra Buczkowskiego (implementacja mechanizmów).
- Zadanie dla Kamila Dubaniowskiego (weryfikacja `Skanuj`).

---
