# CHANGELOG

Historia ustaleń i zmian dla projektu.

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
