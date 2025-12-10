---
ostatnia_aktualizacja: YYYY-MM-DD
changelog_przeglad_do: YYYY-MM-DD
---

# Architektura: [Nazwa Projektu]

> **Ostatnia aktualizacja:** YYYY-MM-DD  
> **CHANGELOG przegląd do:** YYYY-MM-DD

---

## Aktualna koncepcja

### Stack techniczny

- **Frontend:** [React / Angular / Vue / brak] / [DO UZUPEŁNIENIA]
- **Backend:** [.NET 8 / .NET Framework / Node.js / ...] / [DO UZUPEŁNIENIA]
- **Baza danych:** [MSSQL / MySQL / PostgreSQL / brak] / [DO UZUPEŁNIENIA]
- **UI Library:** [Material-UI / Ant Design / ...] / [DO UZUPEŁNIENIA]
- **Inne technologie:** [DO UZUPEŁNIENIA]

### Główne komponenty

[Opis głównych komponentów systemu - 2-3 zdania lub [DO UZUPEŁNIENIA]]

**Przykład:**
- **Toolbox** (lewa strona): Lista typów pól, drag & drop
- **Canvas** (środek): Podgląd formularza (WYSIWYG)
- **Properties Panel** (prawa strona): Ustawienia wybranego pola

### Integracja z AMODIT

- [Punkt integracji 1 - np. "Endpoint: `/api/forms/{processId}`"] / [DO UZUPEŁNIENIA]
- [Punkt integracji 2 - np. "Autoryzacja: Bearer token"] / [DO UZUPEŁNIENIA]
- [Punkt integracji 3 - np. "Współdzielone tabele: `amod_fields`"] / [DO UZUPEŁNIENIA]

---

## Kluczowe decyzje architektoniczne

| Data | Decyzja | Dlaczego | Status | Źródło |
|------|---------|----------|--------|--------|
| [[YYYY-MM-DD]] | [Konkretna decyzja techniczna z CHANGELOG] | [Uzasadnienie biznesowe/techniczne z CHANGELOG] | ✅ Wdrożone | [[YYYY-MM-DD Rada]] |
| [[YYYY-MM-DD]] | [Konkretna decyzja 2] | [Uzasadnienie] | 💡 Propozycja | [[YYYY-MM-DD Sprint review]] |

**Statusy:**
- ✅ **Wdrożone** - decyzja wdrożona na produkcji
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona

**Pełna historia decyzji:** Zobacz [[CHANGELOG#Decyzje]]

---

## Historia koncepcji (odrzucone/zmienione)

| Data | Co było | Dlaczego odrzucono | Źródło |
|------|---------|-------------------|--------|
| [[YYYY-MM-DD]] | [Odrzucona koncepcja techniczna z CHANGELOG] | [Powód odrzucenia z CHANGELOG] | [[YYYY-MM-DD Rada]] |

*(Jeśli brak odrzuconych koncepcji w CHANGELOG - pozostaw tę sekcję pustą)*

---

## Dla developera

### Lokalne uruchomienie

```bash
# Instrukcje z CHANGELOG lub [DO UZUPEŁNIENIA]
cd projekt/
npm install
npm run dev
```

[DO UZUPEŁNIENIA]

### Struktura kodu

- **Główny moduł:** `/src/modules/[nazwa]` / [DO UZUPEŁNIENIA]
- **Komponenty:** `/src/modules/[nazwa]/components/` / [DO UZUPEŁNIENIA]
- **API client:** `/src/services/[Nazwa]Service.ts` / [DO UZUPEŁNIENIA]

### Testy

```bash
# Jak uruchomić testy lub [DO UZUPEŁNIENIA]
npm test
```

### Linki

- **Repozytorium:** [link] / [DO UZUPEŁNIENIA]
- **Środowisko DEV:** [link] / [DO UZUPEŁNIENIA]
- **Środowisko TEST:** [link] / [DO UZUPEŁNIENIA]
- **Dokumentacja techniczna:** [link] / [DO UZUPEŁNIENIA]

---

## Uwagi dla agenta overview-sync

**KRYTYCZNE zasady kategoryzacji:**

Agent MUSI analizować **treść wpisu** z CHANGELOG, nie tylko tag!

**Wpisy należące do ARCHITEKTURA.md:**
- Decyzje o technologiach (OAuth2, React, .NET, MSSQL, Docker, SignalR)
- Decyzje o strukturze (architektura, endpoint, API, integracja)
- Odrzucone koncepcje techniczne
- Stack techniczny, wybór bibliotek

**Przykłady:**
- ✅ `#Decyzja` + "Używamy OAuth2 zamiast custom tokenów" → ARCHITEKTURA.md
- ✅ `#Architektura` + "Wydzielenie microservice w Dockerze" → ARCHITEKTURA.md
- ❌ `#Decyzja` + "Zmieniamy termin MVP2 na grudzień" → NIE architektura (to ROADMAPA.md)
- ❌ `#Decyzja` + "Zwiększamy budżet" → NIE architektura (to PROJEKT.md)

**NIE ZMYŚLAJ:** Jeśli w CHANGELOG brak decyzji technicznych → zostaw tabele puste lub z `[DO UZUPEŁNIENIA]`


