# CHANGELOG – Ustawienia-systemowe

---

## 2025-08-12 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)
**Kategoria:** #Architektura #Problem

**Problem kompatybilności wstecznej interfejsu IJob** ✅
- **Problem:** Rozszerzenie `IJob` o pole `Owner` złamało wszystkie istniejące implementacje jobów
- Wystąpiło na Stage (Rossmann), na szczęście nie na produkcji
- ❌ Odrzucone: Modyfikacja istniejącego interfejsu - łamie kompatybilność wsteczną
- ✅ Zatwierdzone: Nowy osobny interfejs dla jobów wymagających `Owner`
- Istniejące joby nie wymagają modyfikacji, zachowana kompatybilność
- ⏸️ Punkty otwarte: "Czy można to zrobić lepiej?" - analiza po powrocie Marka z urlopu
- **Zadania:** Marek - weryfikacja rozwiązania po powrocie z urlopu

---

## 2025-08-07 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-07 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-07%20Rada%20architektów.md)

**Kategoria:** #Funkcjonalność

**1. MVP dla integracji w ustawieniach systemowych** ✅
- Struktura MVP:
  - **Integracje wbudowane** (VIES, kursy walut, Biała Lista) - stała pierwsza pozycja
  - **Druga kolumna:** Lista integracji skonfigurowanych (wyświetlane tylko gdy mają parametry)
  - **Przycisk "Dodaj integrację":** wybór standardowej lub "Skonfiguruj własną"
- Zasada: integracja pojawia się tylko gdy ma skonfigurowane parametry (nawet częściowo)
- Interfejs w Reactcie, kompatybilność wsteczna z istniejącymi konfiguracjami
- **Zadania:** Kamil Dubaniowski, Przemek - finalizacja MVP

**6. Integracje vs moduły – rozróżnienie** ✅
- **Integracje** = połączenia z zewnętrznymi systemami (KSeF, OpenAI, Biała Lista)
- **Moduły** = funkcjonalności systemu (Raporty zaawansowane) - powinny być w licencji, nie w integracji
- **Zadania:** Upewnienie się że w interfejsie integracji nie ma modułów

**Kategoria:** #Architektura

**2. OAuth i tokeny – konfiguracja aplikacji** 🔍
- Koncepcja: definicja aplikacji OAuth z możliwością generowania wielu tokenów
- W konfiguracji integracji wybór tokenu zamiast ręcznego wpisywania parametrów
- **Status:** Do weryfikacji - lokalizacja wymaga przemyślenia
- **Punkty otwarte:** Czy w integracjach czy osobna zakładka (analogicznie do Connection Stringów)?

**Kategoria:** #Roadmap

**3. Reorganizacja ustawień systemowych** ⏸️
- Potrzeba kategoryzacji integracji (podpisy, przechowywanie dokumentów, uwierzytelnianie)
- **Odroczone:** Zbyt złożone na MVP, osobny projekt w przyszłości
- MVP: odwzorowanie obecnej struktury w Reactcie z poprawą UX
- **Punkty otwarte:**
  - Czy Active Directory w integracjach czy osobnej zakładce "Uwierzytelnianie"?
  - Czy Connection Stringi jako integracje czy osobna zakładka?
  - Lokalizacja poczty przychodzącej/wychodzącej?

**4. Wykorzystanie AI do tworzenia integracji** ⏸️
- Koncepcja: AI (AMODIT Copilot) analizuje Swagger i generuje konfigurację integracji
- **Odroczone:** Nie w zakresie MVP, element strategii wykorzystania AI
- Przykład już wdrożony: wyszukiwanie i interpretacja parametrów w Copilocie

**Kategoria:** #Decyzja

**5. Eksport helpa do PDF** ❌
- Pytanie klienta o eksport helpa do PDF
- **Odrzucone:** Brak uzasadnienia biznesowego
  - Help dostępny w AMODIT Copilocie i plikach YAML
  - Dokumentacja zmienia się często - statyczny eksport szybko się dezaktualizuje
- Oferta płatna: 15 000 zł (jako weryfikacja rzeczywistej potrzeby)

---

