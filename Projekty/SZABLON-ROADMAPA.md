---
ostatnia_aktualizacja: YYYY-MM-DD
changelog_przeglad_do: YYYY-MM-DD
---

# Roadmapa: [Nazwa Projektu]

> **Ostatnia aktualizacja:** YYYY-MM-DD  
> **CHANGELOG przegląd do:** YYYY-MM-DD

---

## ✅ PRODUKCJA - MVP1 "[Nazwa]"

**Wydane:** YYYY-MM-DD / [DO UZUPEŁNIENIA]

**Dostarczone funkcjonalności:**

- ✅ [Funkcja 1 z CHANGELOG oznaczona jako ukończona] - [[YYYY-MM-DD Sprint review]]
- ✅ [Funkcja 2 z CHANGELOG oznaczona jako ukończona] - [[YYYY-MM-DD Rada architektów]]
- ✅ [Funkcja 3] - [[YYYY-MM-DD Notatka projektowa]]

*(Tylko funkcje z CHANGELOG wyraźnie oznaczone jako ukończone/wdrożone/wydane)*

**Znane ograniczenia:**

- ⚠️ [Bug/ograniczenie z CHANGELOG] - planowana naprawa: [sprint XX / data] - [[YYYY-MM-DD źródło]]
- ⚠️ [Ograniczenie 2] - [[YYYY-MM-DD źródło]]

*(Jeśli brak ograniczeń w CHANGELOG - usuń tę sekcję lub zostaw [DO UZUPEŁNIENIA])*

---

## 🛠️ W TRAKCIE - MVP2 "[Nazwa]"

**Planowane wydanie:** [Data/kwartał z CHANGELOG] / [DO UZUPEŁNIENIA]

**Cel:** [Cel MVP z CHANGELOG - 1-2 zdania, jaką wartość dostarczamy] / [DO UZUPEŁNIENIA]

**Status funkcjonalności:**

- ✅ [Funkcja A ukończona] - [[YYYY-MM-DD Sprint review]]
- 🔄 [Funkcja B w trakcie] - w trakcie (dev: [Imię z CHANGELOG], sprint XX)
- 🔄 [Funkcja C w analizie] - w analizie
- ⏳ [Funkcja D zaplanowana]

**Out of Scope (NIE robimy w tym MVP):**

- [Funkcja odroczona z CHANGELOG]
- [Funkcja odroczona 2]

*(Tylko jeśli w CHANGELOG jest wyraźna informacja "poza zakresem" / "odroczone" / "nie robimy")*

---

## 📋 PLANOWANE - MVP3 "[Nazwa]"

**Planowane:** [Data/kwartał z CHANGELOG] / [DO UZUPEŁNIENIA]

**Zakres (wstępny):**

- [ ] [Funkcja E z CHANGELOG]
- [ ] [Funkcja F z CHANGELOG]

**Otwarte pytania:**

- [ ] [Pytanie do rozstrzygnięcia z CHANGELOG]
- [ ] [Pytanie 2]

*(Jeśli brak informacji o MVP3 w CHANGELOG - usuń tę sekcję)*

---

## 🗄️ BACKLOG (przyszłe wersje)

**Funkcjonalności odroczone:**

- [Funkcja X] (priorytet: Wysoki / Średni / Niski) - [[YYYY-MM-DD źródło]]
- [Funkcja Y] (priorytet: Średni) - [[YYYY-MM-DD źródło]]

*(Tylko funkcje wyraźnie oznaczone w CHANGELOG jako "odroczone" / "backlog" / "przyszłość")*

---

## 📊 Historia wydań

| Data | Wersja | Co wydano | Źródło |
|------|--------|-----------|--------|
| [[YYYY-MM-DD]] | MVP1 | [Krótki opis z CHANGELOG] | [[YYYY-MM-DD Sprint review]] |
| [[YYYY-MM-DD]] | MVP1.1 | [Opis aktualizacji] | [[YYYY-MM-DD Sprint review]] |

*(Tylko wydania potwierdzone w CHANGELOG przez Sprint review lub podobne źródło)*

---

## 📦 Podprojekty *(tylko dla projektów zbiorczych)*

| Podprojekt | Status | Najbliższe MVP | Zespół |
|------------|--------|----------------|--------|
| [[Nazwa-podprojektu-1]] | 🛠️ W trakcie | MVP2: grudzień 2025 | Dev: [Imię] |
| [[Nazwa-podprojektu-2]] | 🟡 W analizie | MVP1: Q1 2026 | Dev: [DO UZUPEŁNIENIA] |
| [[Nazwa-podprojektu-3]] | ✅ Produkcja | Wydano: 2025-09-15 | Dev: [Imię] |

**Szczegóły:** Zobacz katalogi podprojektów i ich pliki ROADMAPA.md

*(Usuń tę sekcję jeśli projekt NIE ma podprojektów)*

---

## Uwagi dla agenta overview-sync

**KRYTYCZNE zasady kategoryzacji:**

Agent MUSI analizować **treść wpisu** z CHANGELOG, nie tylko tag!

**Wpisy należące do ROADMAPA.md:**
- Funkcjonalności użytkownika ("użytkownik może", "dodano przycisk", "nowy formularz")
- Features (drag & drop, wyszukiwarka, filtrowanie, eksport)
- Status implementacji (ukończone, w trakcie, zaplanowane, odroczone)
- MVP, sprint, wydanie, terminy
- Bugi i ich naprawy

**Przykłady:**
- ✅ `#Funkcjonalność` + "Dodano drag & drop sekcji" → ROADMAPA.md
- ✅ `#Bug` + "Naprawiono czyszczenie pola daty" → ROADMAPA.md (znane ograniczenia)
- ✅ `#Decyzja` + "MVP2 przesunięty na grudzień" → ROADMAPA.md (decyzja o planie)
- ✅ `#Sprint-review` + "Ukończono wyszukiwarkę" → ROADMAPA.md (produkcja)
- ❌ `#Decyzja` + "Używamy OAuth2" → NIE roadmapa (to ARCHITEKTURA.md)
- ❌ `#Decyzja` + "Zwiększamy budżet" → NIE roadmapa (to PROJEKT.md)

**Agregacja funkcjonalności:**
Zamiast listować wszystkie 50 wpisów, syntetyzuj:
- ❌ ZŁE: "Dodano przycisk A", "Dodano przycisk B", "Dodano przycisk C"...
- ✅ DOBRE: "Dodano funkcje UI (przyciski A, B, C; drag & drop; panel właściwości)"

**Statusy:**
- ✅ = ukończone, wdrożone, wydane
- 🔄 = w trakcie, w realizacji
- ⏳ = zaplanowane, w backlogu sprintu
- ⚠️ = znane ograniczenie, bug

**NIE ZMYŚLAJ:** Jeśli w CHANGELOG brak informacji o MVP/funkcjach → zostaw `[DO UZUPEŁNIENIA]`


