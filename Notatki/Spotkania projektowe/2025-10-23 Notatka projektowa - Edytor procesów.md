**Data:** 2025-10-23
**Temat główny:** Edytor procesów (formularz, diagram) i strategia roadmapy

---

## 1. Edytor Formularza

**Komponent:** Edytor Formularza

### Cel i problem

Finalizacja prac nad nowym edytorem formularza (React).

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (MVP 1)

- Moduł uznany za "w miarę gotowy".
- Dodano funkcję przesuwania sekcji (zarządzanie kolejnością), której brakowało w starym edytorze.
- **Decyzja:** Nie dodajemy już nowych funkcji, tylko stabilizujemy obecne rozwiązanie na wersję grudniową.

---

## 2. Edytor Diagramu

**Komponent:** Edytor Diagramu

### Cel i problem

Ustalenie zakresu prac dla wersji grudniowej (MVP 1) i kolejnych kroków (MVP 2). Diagram ma zostać wydany w wersji umożliwiającej budowanie procesu, ale bez pełnej integracji edycji właściwości na jednym ekranie.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| **Edycja na diagramie** | Pełna edycja reguł i etapów w prawym panelu na diagramie. | ⏸️ Odroczona (do MVP 2 / wersja marcowa) |
| **Odtworzenie zakładek** | Pozostawienie listy etapów jako osobnej zakładki (jak w starym systemie). | ✅ Wybrana (na MVP 2) |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

1.  **MVP 1 (Wersja Grudniowa):**
    - Odtworzenie podstawowej funkcjonalności budowania diagramu.
    - Nowy diagram **nie wszedł** do wersji czerwcowej, celujemy w wydanie grudniowe.
2.  **MVP 2 (Wersja Marcowa? / Kolejny etap):**
    - **Prawy panel:** Będzie służył do ustawień etapu (to co na liście etapów).
    - **Lista etapów:** Zostanie przywrócona jako zakładka (widok listy), ponieważ jest potrzebna do zarządzania kolejnością/indeksowaniem.
    - **Edycja reguł:** Integracja edycji reguł z diagramem odłożona na dalszy plan.

### Punkty otwarte

- **Prawy panel:** Wymaga zaprojektowania (Kamil Dubaniowski). Ma być bardziej złożony docelowo (obsługa wymagań, dokumentacji), ale w MVP 2 ma odtwarzać funkcjonalność listy etapów.
- **Dokumentacja procesu:** Pomysł (Przemysława Sołdackiego) wrzucania dokumentacji (Word/Excel) do ustawień procesu, ewentualnie z użyciem AI do rozpisania na punkty. Koncepcja niedopracowana, odłożona na przyszłość.

---

## 3. Edytor Reguł

**Komponent:** Edytor Reguł

### Status

**Status:** ⏸️ Odroczone

Projekt graficzny skończony (Damian), ale implementacja jeszcze nie ruszyła. Nie jest częścią obecnego sprintu wdrożeniowego na grudzień.

---

## 4. Strategia Roadmapy i Priorytety

**Komponent:** Organizacja / Roadmapa

### Cel i problem

Konieczność rewizji roadmapy na końcówkę roku i 2026. Konflikt zasobów między rozwojem (R&D) a domykaniem wdrożeń (przychody).

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (Decyzja Zarządu - Przemysław Sołdacki)

1.  **Priorytet absolutny:** **Domykanie wdrożeń (WIM, Lot).**
    - Cel: Wystawienie faktur i zamknięcie projektów w tym roku.
    - Jeśli trzeba, prace R&D (np. Edytor Diagramu) mogą poczekać, jeśli zasoby są potrzebne do wdrożeń.
2.  **Strategia rozwoju:**
    - Skupienie na 2 obszarach: **Wsparcie sprzedaży** (atrakcyjność systemu) i **Wsparcie wdrożeń/serwisu** (skrócenie czasu wdrożeń o 30%).
    - Wstrzymanie "wymyślania nowych rzeczy" w edytorach – dowiezienie tego, co zaczęte.
3.  **Termin:** Propozycja nowej roadmapy (uzgodnionej z Działem Wdrożeń i Serwisu) ma zostać przedstawiona Zarządowi do **3 listopada 2025**.

---

## Punkty do dalszej dyskusji (globalne)

- **Spotkanie R&D z Wdrożeniami/Serwisem:** Planowane na poniedziałek 12:30 (27.10.2025?). Cel: ustalenie wspólnych priorytetów.
- **Rewizja projektów:** Zidentyfikowano blisko 40 otwartych tematów w R&D. Konieczna ostra priorytetyzacja ("co robimy, a czego nie").
