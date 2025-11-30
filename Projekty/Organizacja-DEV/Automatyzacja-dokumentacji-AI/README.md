# Automatyzacja dokumentacji AI

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | Janusz | |
| **Deweloper** | | |
| **Tester** | | |

**Typ:** Projekt organizacyjny (Organizacja Działu DEV)
**Status:** 🟢 W realizacji
**Data rozpoczęcia:** 2025-09-02
**Planowane zakończenie:** -

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

Obecny proces tworzenia dokumentacji jest nieefektywny i czasochłonny:
- Komunikacja werbalna dominuje, ale jej treść pozostaje nieustrukturyzowana
- Nagrania ze spotkań są rzadko przetwarzane na konkretne dokumenty
- Ręczne pisanie artykułów i dokumentacji projektowej jest powolne
- Opóźnia przejście od pomysłu do realizacji

### Cel projektu

Wdrożenie nowego procesu opartego na narzędziach AI w celu znacznego przyspieszenia tworzenia dokumentacji, w tym dokumentacji projektowej na podstawie spotkań.

### Powiązane dokumenty
- Inicjatywa w backlogu: [link]

---

## 2. Kontekst techniczno-architektoniczny

### Podejście architektoniczne

Proces oparty na nagrywaniu i przetwarzaniu AI:
1. **Nagrywanie** - rejestracja dyskusji/spotkań
2. **Transkrypcja** - automatyczna konwersja na tekst
3. **Przetwarzanie AI** - wykorzystanie Gemini z przygotowanymi promptami
4. **Generowanie dokumentacji** - strukturyzowany artykuł/dokument

### Technologie
- AI: Google Gemini
- Transkrypcja: [do ustalenia]
- Słownik terminologii: Google Sheets

### Kluczowe zasady
- Jeden artykuł = jeden wąsko zdefiniowany temat
- Terminologia ujednolicona poprzez centralny słownik (arkusz Google)
- AI odwołuje się do słownika przy generowaniu

### Kluczowe decyzje architektoniczne

| Data | Decyzja | Uzasadnienie |
|------|---------|--------------|
| 2025-09-02 | Akceptacja podejścia AI do dokumentacji | Przyspieszenie procesów wytwórczych |
| 2025-09-02 | Centralny słownik terminologii w Google Sheets | Spójność terminologii w całej dokumentacji |

---

## 3. Szablony promptów

Janusz opracował **6 szablonów promptów** dla różnych typów artykułów:

1. **Artykuły funkcjonalne** - opis funkcjonalności systemu
2. **Artykuły koncepcyjne** - wyjaśnienie koncepcji i architektury
3. **Poradniki "how-to"** - instrukcje krok po kroku
4. **Artykuły techniczne** - dokumentacja techniczna
5. [do uzupełnienia]
6. [do uzupełnienia]

---

## 4. Zadania

- [ ] **Janusz:** Udostępnić zespołowi opracowane prompty do generowania artykułów
- [x] **Janusz:** Przygotować dokumentację projektową dla matrycy uprawnień (jako test metody)

---

## 5. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-09-02 | Utworzenie projektu, akceptacja podejścia AI | Rada Architektów 2025-09-02 |
