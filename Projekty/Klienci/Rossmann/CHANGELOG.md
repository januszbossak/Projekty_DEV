# CHANGELOG – Rossmann

Historia ustaleń i zmian dla klienta Rossmann.

---

## 2025-12-22 | Projekt: Historia Biznesowa - Uszczegółowienie designu
**Źródło:** [Notatki/Gotowe-notatki/2025-12-22 Historia biznesowa dla Rossmann](../../../Notatki/Gotowe-notatki/2025-12-22%20Historia%20biznesowa%20dla%20Rossmann)
**Kategoria:** #Design #Funkcjonalność #Moduł

- Definicja interaktywnego timeline'u z kolorowym kodowaniem procesów.
- Projekt "Kafelków zdarzeń" z możliwością rozwijania szczegółów.
- Wprowadzenie wyszukiwarki pełnotekstowej oraz zaawansowanych filtrów w panelu bocznym.
- Określenie modelu konfiguracji opartego na *Amodit Script* i relacjach `connectedCase`.
- Link do projektu: [Historia-biznesowa/README.md](Historia-biznesowa/README.md)

---

## 2025-12-19 | Compliance AI Act

**Źródło:** [Notatki/Gotowe-notatki/2025-12-19 Odpowiedz-do-Rossman-w-sprawie-AI-Act](2025-12-22%20Odpowiedz-do-Rossman-w-sprawie-AI-Act.md)

**Kategoria:** #Bezpieczeństwo #Legislacja #AI

- Przygotowanie kompleksowej odpowiedzi na 12 pytań AI Compliance Officera Rossmann.
- Potwierdzenie statusu Astrafox jako **dostawcy (provider)** oraz Rossmann jako **wdrażającego (deployer)** w rozumieniu AI Act.
- Deklaracja braku wykorzystania danych klienta do trenowania modeli bazowych (Azure OpenAI).
- Potwierdzenie przetwarzania danych wewnątrz UE (regiony Microsoft Azure).
- Zaklasyfikowanie systemu AMODIT w standardowym użyciu jako system niewchodzący w kategorię wysokiego ryzyka (High-Risk).

---

## 2025-12-09 | Spotkanie projektowe - Design


**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-09 Design - Edytor formularzy.md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-09%20Design%20-%20Edytor%20formularzy.md)

**Kategoria:** #Problem #Integracje

- Problem z synchronizacją kartoteki - eskalacja od Rossmann
- Kartoteka istnieje w systemie, ale odpowiedź AMODIT wskazuje "nie można utworzyć sprawy"
- Powinna być informacja "nie można zaktualizować"
- Przyczyna pośrednio nieznana - kartoteka istnieje, duplikat nie istnieje, ale system odpowiada błędnie
- Wymaga analizy przez Adriana po powrocie ze szkolenia
- Status: 🔍 Do weryfikacji

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
