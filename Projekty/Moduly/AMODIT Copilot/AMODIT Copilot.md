# Project Canvas: AMODIT Copilot

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-09-08
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-08-26

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | Janusz Bossak, Przemek | Wymagania, wizja produktu |
| **Tech Lead** | Piotr Buczkowski | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Tworzenie procesów biznesowych od zera jest czasochłonne i wymaga specjalistycznej wiedzy. Użytkownicy, nawet z pomysłem na proces, często napotykają trudności w przełożeniu go na konkretne kroki, formularze i reguły w AMODIT. Potrzebują inteligentnego wsparcia, które poprowadzi ich przez ten proces.

### Cel biznesowy
Radykalne uproszczenie i przyspieszenie procesu tworzenia i wdrażania nowych procesów biznesowych w AMODIT. Celem jest przekształcenie Copilota z narzędzia wykonującego polecenia w inteligentnego konsultanta, który aktywnie pomaga użytkownikowi w zdefiniowaniu i zbudowaniu kompletnego, działającego procesu.

### Cel techniczny
Rozbudowa Copilota o zaawansowane możliwości konwersacyjne (tryb konsultacyjny) oparte o dedykowane prompty. Implementacja mechanizmu asynchronicznego generowania procesu, aby obejść problemy z timeoutami. Zapewnienie, że promptami można zarządzać po stronie mikroserwisu, bez konieczności aktualizacji całej aplikacji AMODIT.

### Metryka sukcesu
- Skrócenie czasu od pomysłu do działającego prototypu procesu o 70%.
- Zwiększenie adopcji narzędzia do tworzenia procesów wśród mniej technicznych użytkowników o 50%.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-08-26]] | Rozdzielono funkcjonalności Copilota i AI OCR na dwa osobne projekty: `AMODIT Copilot` i `AMODIT AI OCR`. | Są to dwie odrębne, duże funkcjonalności. Rozdzielenie pozwala na lepsze zarządzanie i klarowniejszą komunikację. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-09-08]] | Wprowadzenie "trybu konsultacyjnego", w którym Copilot dopytuje użytkownika o szczegóły procesu, używając predefiniowanego zestawu pytań analitycznych. | Zmienia to paradygmat z "narzędzia" na "asystenta". Pomaga to użytkownikowi ustrukturyzować swoje wymagania i prowadzi do tworzenia bardziej kompletnych i przemyślanych procesów. | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-09-08]] | Generowanie procesu jest operacją asynchroniczną. Interfejs odpytuje serwer o status generowania. | Generowanie całego procesu przez AI jest operacją długotrwałą. Asynchroniczność rozwiązuje problem timeoutów na gatewayu w chmurze i poprawia UX. | - |
| ADR-004 | ✅ Zatwierdzone | [[2025-09-08]] | Prompt sterujący trybem konsultacyjnym jest przechowywany i zarządzany po stronie mikroserwisu. | Umożliwia to szybkie iteracje i zmiany w zachowaniu Copilota (np. dodawanie nowych pytań) bez konieczności wdrażania nowej wersji całej aplikacji AMODIT. | - |
| ADR-005 | 💡 Propozycja | [[2025-09-08]] | Należy uatrakcyjnić proces oczekiwania na wygenerowanie procesu (np. spinner z losowymi komunikatami o postępie). | Obecny, statyczny ekran oczekiwania jest mało angażujący. Dynamiczne komunikaty poprawią odczucia użytkownika (UX). | - |
| ADR-006 | 💡 Propozycja | [[2025-09-08]] | Rozważyć zmianę promptu, aby Copilot zadawał pytania pojedynczo, a nie w jednym bloku. | Taka forma konwersacji jest bardziej naturalna i przypomina interakcję z ludzkim konsultantem, co może być bardziej intuicyjne dla użytkowników. | - |

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-08-26]] | Utworzenie projektu po reorganizacji. Zdefiniowanie trzech filarów: tworzenie procesów, asystent reguł, baza wiedzy. | [[2025-08-26 Notatka projektowa - AMODIT UI]] |
| [[2025-09-02]] | Odnotowano problemy z analizą procesów klienta PKF. Rozpoczęto dyskusję na temat modelu cenowego dla Copilota. | [[2025-09-02 Rada architektów]] |
| [[2025-09-08]] | Demo nowej, kluczowej funkcjonalności: trybu konsultacyjnego do generowania procesów. Zebrano feedback dotyczący UX (ekran oczekiwania, sposób zadawania pytań). | [[2025-09-08 Sprint review]] |
