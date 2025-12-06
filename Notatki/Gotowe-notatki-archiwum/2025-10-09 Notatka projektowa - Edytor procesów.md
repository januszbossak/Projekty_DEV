> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

**Data:** 2025-10-09
**Temat główny:** Edytor procesów – diagram, reguły i roadmapa MVP

**Powiązane projekty:**
- `Moduly/Edytor-procesow/Edytor-diagramu`
- `Moduly/Edytor-procesow`

---

## 1. Wizualizacja reguł na diagramie

**Komponent:** Edytor Diagramu

### Cel i problem
Odróżnienie reguł ręcznych (przycisków) od reguł automatycznych na diagramie. Obecnie zbyt duża liczba kolorów i ikon wprowadza chaos informacyjny ("zbyt dużo bodźców dla mózgu").

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| **Osobne style** | Wyraźne rozróżnienie: przyciski jako "guziki" (ikona + napis), reguły automatyczne jako tekst z ikoną (np. fioletowe, spójne kolorystycznie). | 🔍 Do weryfikacji (Damian przygotuje propozycję) |
| **Minimalizm** | Usunięcie kolorów z reguł automatycznych, pozostawienie tylko ikony i tekstu. | 💡 Propozycja |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do dalszego projektowania

Damian Kaminski ma przygotować alternatywną propozycję wizualną, która uprości widok i zmniejszy "szum" kolorystyczny.
- **Cel:** Użytkownik ma od razu wiedzieć, co jest przyciskiem dla użytkownika, a co automatem w tle.
- **Kierunek:** Spójny kolor dla automatów (np. fioletowy) lub całkowita rezygnacja z kolorów dla nich.

---

## 2. Algorytmy rysowania diagramu (Layout)

**Komponent:** Edytor Diagramu

### Cel i problem
Automatyczne układanie elementów na diagramie. Różne procesy wyglądają lepiej w różnych algorytmach. Algorytm ELK (hierarchiczny) czasem nakłada na siebie elementy, ale ładnie prostuje linie. Dagre jest prostszy.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Wprowadzenie **przełącznika trybu rysowania** (wyboru algorytmu) dla użytkownika.
- Użytkownik będzie mógł wybrać między układem np. "Hierarchicznym" (ELK) a "Podstawowym" (Dagre) w zależności od tego, który lepiej prezentuje dany proces.
- Funkcjonalność ma trafić do najbliższego sprintu (MVP).

---

## 3. Zakres MVP (Wersja Grudniowa)

**Komponent:** Edytor Diagramu / Roadmapa

### Cel i problem
Ustalenie zakresu prac na wersję grudniową (rezygnacja z wersji wrześniowej). Kluczowe jest dowiezienie działającego edytora w nowej technologii (React).

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

1.  **Edycja właściwości (Prawy Panel):** ❌ Poza zakresem MVP.
    - Nie będzie prawego panelu do edycji etapów ani reguł na diagramie w tej wersji.
    - Użytkownicy będą musieli korzystać z zakładek "Etapy" i "Reguły" (stare podejście).
2.  **Edycja reguł:**
    - Na diagramie można zdefiniować przejście (strzałkę) i nadać nazwę.
    - Szczegółowa edycja (kod, warunki) odbywa się w osobnej zakładce "Reguły".
3.  **Zakładka "Etapy":** Pozostaje w MVP (nie rezygnujemy z niej jeszcze), ponieważ brakuje prawego panelu do edycji właściwości etapu na diagramie.

### Punkty otwarte
- **Edytor Reguł:** Docelowo ma powstać nowy edytor reguł. Dopiero po jego stworzeniu zostanie on zintegrowany z diagramem (edycja bezpośrednio z diagramu).

---

## 4. Inne funkcjonalności diagramu

**Komponent:** Edytor Diagramu

### Decyzja / Sposób realizacji

**Status:** 💡 Różne ustalenia

1.  **Dodawanie etapu:**
    - Zatwierdzanie dodania nowego etapu klawiszem `Enter` lub ikoną.
    - Ikona zatwierdzenia: zmiana z "plusa" na "haczyk" (tick), aby była bardziej intuicyjna.
2.  **Tory (Swimlanes) / Aktorzy:**
    - **Status:** ❌ Odrzucone / Odroczone.
    - Nie będziemy implementować grupowania etapów w tory (swimlanes) według aktorów w MVP. Jest to zbyt skomplikowane, a klienci rzadko rysują procesy w ten sposób w systemie (używają do tego Enterprise Architect).
3.  **Przycisk "Sprawdź reguły":**
    - Istniejąca funkcja walidacji reguł. Mało widoczna, ale przydatna. Pozostaje bez zmian.

---

## Punkty do dalszej dyskusji (globalne)

- **Roadmapa:** Przegląd roadmapy i ustalenie priorytetów na spotkaniu w przyszłym tygodniu.
- **Historia zmian:** Konsultacja z działem Serwisu odnośnie wymagań co do historii zmian na diagramie/regułach.
