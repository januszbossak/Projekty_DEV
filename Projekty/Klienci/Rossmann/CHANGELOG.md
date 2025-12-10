# CHANGELOG – Rossmann

Historia ustaleń i zmian dla klienta Rossmann.

---

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-03 Notatka projektowa - Historia biznesowa.md]
**Kategoria:** #Funkcjonalność #Design

**Kontekst:** Rossmann jako główny sponsor przeprojektowania mechanizmu historii biznesowej - wieloprocesowa historia korespondencji.

**Problem biznesowy:**
- Korespondencja wpływa przez e-Doręczenia (proces techniczny), potem jest przekierowywana do różnych procesów obiegu (X, Y, Z)
- Automatyzacja przekazywania → błędy w kierowaniu → kopiowanie spraw między procesami → **utrata historii**
- Użytkownik otwiera sprawę "dzisiaj", ale dokument jest z "3 dni temu" - brak informacji, co się działo wcześniej

**Rozwiązanie:**
- Mechanizm `connectedCase` do spinania historii z wielu procesów w jedną chronologiczną listę
- Rekurencyjne ładowanie historii z powiązanych spraw (e-Doręczenia → Obieg X → Obieg Y)
- Dedykowana tabela `CaseEventBusinessSubjects` zamiast JSON - szybkie indeksowanie i raportowanie

**Mockup UI:**
- Lista chronologiczna zdarzeń z nazwami procesów (heurystyka: nazwa procesu tylko przy zmianie kontekstu)
- Format wpisu: nazwa zdarzenia + data/godzina + użytkownik/system + opcjonalnie nazwa procesu
- Obsługa HTML w `message` (linki do dokumentów, z walidacją XSS)
- Do przekazania klientowi na feedback

**MVP 1 (sponsor: Rossmann):**
- Tabela powiązań `CaseEventBusinessSubjects`
- Mechanizm `connectedCase` w widoku historii
- Mockup UI - lista chronologiczna z nazwami procesów
- Typ powiązania `case` (connectedCase)

**Punkty otwarte:**
- Kolejność wyświetlania: najnowsze na górze czy na dole?
- Czy wyświetlać nagłówek procesu? (decyzja klienta)
- Limit głębokości rekurencji (propozycja: max 10 poziomów)

---
