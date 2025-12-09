# Notatka projektowa – 2025-11-27 – Edytor Procesów: Ustawienia pól i nawigacja

**Data:** 2025-11-27
**Temat główny:** Edytor Procesów: Ustawienia pól, nawigacja w tabelach i podformularzach
> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-09

**Powiązane projekty:**
- `Moduly/Edytor-procesow`
- `Moduly/Edytor-procesow/Edytor-formularzy`
- `cross-cutting/Design-System`

---

## 1. Optymalizacja i poprawki panelu prawego ustawień pól

**Komponent:** Edytor Formularza

### Cel i problem

Poprawa użyteczności i czytelności panelu ustawień pól, który jest kluczowym elementem konfiguracyjnym zarówno w edytorze graficznym, jak i edytorze listy. Istniejące problemy to nieoptymalna kolejność ustawień, niejasne wizualizacje oraz brak spójności w wyglądzie.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| **Obecny układ** | Pozostawienie istniejącej kolejności i wizualizacji | ❌ Odrzucona – nieoptymalna kolejność, niskie użycie istotnych ustawień |
| **Przemeblowanie układu** | Zmiana kolejności i grupowania ustawień, poprawa wizualizacji | ✅ Wybrana – planowane na przyszły sprint |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (częściowo zrealizowane, częściowo planowane)

- **Zmiana nagłówka panelu:** Przemek wprowadził już zmiany w nagłówku.
- **Kolejność i układ ustawień:** Na przyszły sprint planowane jest spisywanie zmian w prawym panelu ustawień pola, aby poprawić układ i kolejność (np. istotne ustawienia na górze). Jest to wspólny komponent dla edytora graficznego i edytora listy.
- **Wyrównanie marginesów:** Zauważono dyskomfort z powodu nierównych marginesów w prawym panelu i liście pól. Kamil zgodził się na poprawę.
- **Wizualizacja "Dodaj sekcję" / "Dodaj wiersz":**
    - Wskazano na potrzebę lepszego rozróżnienia kolorystycznego przycisków "Dodaj sekcję" i "Dodaj wiersz" pojawiających się na hover.
    - **Status:** 💡 Propozycja (do przemyślenia), aby uniezależnić kolorystykę od systemowej i zastosować spójny kolor (np. zielony) dla akcji dodawania.
- **Zaokrąglenia rogów:** Zastosowano zaokrąglenia rogów sekcji (takie jak na formularzu, styl `piątka`). W zgłoszono zadanie, aby ujednolicić to również w innych miejscach (`ósemki` na `piątki`).
- **Ikony w nagłówkach sekcji:** W nagłówku sekcji pojawia się ikona nawiązująca do typu pola, zamiast samej nazwy typu, co poprawia intuicyjność.
- **Wygląd panelu:** Prawy panel jest teraz spójnym boksem (tak jak na liście), co rozwiązuje problem przesuwania nawigacji i przycisków po jego otwarciu.

**Szczegóły techniczne:**
- Wspólny komponent dla edytora graficznego i listy.
- Nowy wzorzec zaokrągleń: "piątka".

### Punkty otwarte

- Ustalenie finalnej kolorystyki dla przycisków "Dodaj sekcję" / "Dodaj wiersz".
- Dokładne zmiany w układzie i kolejności ustawień w prawym panelu (do sprecyzowania w przyszłym sprincie).

---

## 2. Wyszukiwanie pól po atrybutach technicznych

**Komponent:** Edytor Formularza

### Cel i problem

Umożliwienie efektywniejszego wyszukiwania pól przez serwisantów lub analityków poprzez techniczne atrybuty, takie jak ID pola, nazwa kolumny w bazie danych i GUID.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (zrealizowane)

- **Rozszerzenie wyszukiwania:** Dodano możliwość wyszukiwania pól również po GUID. Wyszukiwanie było już dostępne po ID pola i nazwie kolumny w bazie danych.
- **Funkcjonalność:** Po włączeniu opcji, wpisanie fragmentu GUID (np. "5-4-E") podpowiada pasujące pole. Wybranie pola automatycznie otwiera jego ustawienia.

**Szczegóły techniczne:**
- Opcja włączana "na życzenie" (do celów serwisowych).
- Wyszukiwanie po ID, nazwie kolumny, GUID.

---

## 3. Nawigacja w tabelach i podformularzach (decyzja o powrocie do starej koncepcji)

**Komponent:** Edytor Formularza

### Cel i problem

Uproszczenie i ujednolicenie nawigacji w edytorze procesów, szczególnie w kontekście zagnieżdżonych tabel i podformularzy. Obecna koncepcja "drążenia" w głąb tabel na widoku listy prowadzi do zamieszania, problemów z kontekstem i niejasności.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| **Obecne zagnieżdżanie** | Drążenie w głąb tabel bezpośrednio z widoku listy pól | ❌ Odrzucona – problemy z kontekstem, nieczytelność przy głębokich zagnieżdżeniach |
| **Powrót do starej koncepcji** | Tabela jako pole, nawigacja do jej pól przez dedykowany przycisk/strzałkę | ✅ Wybrana – uproszczenie nawigacji, utrzymanie kontekstu |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (planowane na przyszły sprint)

- **Zmiana nawigacji dla tabel:** Tabela nie będzie już rozwijana bezpośrednio na widoku listy pól. Zamiast tego będzie traktowana jako pole. Aby wejść do pól w tabeli, używana będzie strzałka w prawo (tak jak w starym edytorze).
- **Zasada "wizualizacja vs. nawigacja":** Środkowa część ekranu (gdzie wizualizowany jest formularz) powinna służyć **wyłącznie prezentacji** wyglądu formularza, a nie nawigacji. Kliknięcie pola w tej części powinno otwierać prawy panel z jego ustawieniami, a nie wchodzić w głąb. Nawigacja do zagnieżdżonych elementów powinna odbywać się poprzez dedykowane przyciski (np. "Edytuj pola formularza") lub menu.
- **Uwierzytelnianie:** Niezależne od standardowego REST API Amodit.
- **Zamykanie panelu prawego:** Po zmianie kontekstu (np. wejściu do tabeli), prawy panel ustawień powinien być zamykany, aby uniknąć wyświetlania ustawień z poprzedniego kontekstu.
- **Wyświetlanie dodatkowych kolumn:** Dostępna jest opcja wyświetlania dodatkowych kolumn, domyślnie wyłączona.
- **Struktura drzewka:** Zmieniono nawigację lewego panelu na strukturę drzewa, pokazującą relacje rodzic-dziecko między elementami formularza. Zapewnia to lepszą czytelność niż pełna ścieżka.
    - **Status:** ✅ Zatwierdzone
    - Problem: Brak breadcrumbów na poziomie tabel.
        - **Status:** 🔍 Do weryfikacji (potrzebne przemyślenie rozwiązania breadcrumbs dla nawigacji w zagnieżdżeniach)

**Szczegóły techniczne:**
- Koncepcja "wizualizacja kontra nawigacja" ma być podstawą dalszego projektowania interfejsu.
- Rozważana implementacja: kliknięcie pola w głównym widoku zawsze otwiera prawy panel ustawień tego pola.

### Punkty otwarte

- Ostateczne rozwiązanie kwestii breadcrumbów dla zagnieżdżeń (tabel i podformularzy) w lewym panelu nawigacji.
- Finalne dopracowanie zachowania prawego panelu po zmianie kontekstu.
- Potrzebne jest zaprojektowanie spójnego rozwiązania w Figmie (Kamil).

---

## Punkty do dalszej dyskusji (globalne)

- Omówienie i zaprojektowanie spójnego modelu nawigacji dla zagnieżdżonych struktur w edytorze formularzy. Konieczność rozgraniczenia wizualizacji od nawigacji.
