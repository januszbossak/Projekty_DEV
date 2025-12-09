> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-09

# Planowanie Sprintu – 2025-11-27

**Sprint:** [Sprint po 2025-11-24]
**Okres:** 2 tygodnie (koniec grudnia 2025)

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Status | Uwagi |
|-------|--------|-------|
| Edytor graficzny formularza | 🔄 W trakcie | Jeszcze są niuanse do poprawienia, planowane zamknięcie w następnym sprincie |
| Matryca uprawnień | ✅ Prawie zamknięte | Brakuje tłumaczeń etapów, wyszukiwarki pól, obsługi pustych pól |
| Lista pól | 🔄 W trakcie | Kontynuacja rozwoju |
| Widok sprawy | 🔄 Poprawki | Problemy z porozjeżdżanym wyglądem, scroll vs. przycisk "plus" |
| Komunikator | ✅ Skonfigurowany | Brak uwag od klienta |

---

## 2. Plany na sprint

### JRWA (Jednolity Rzeczowy Wykaz Akt)

**Kontekst i cel:**
Obsługa JRWA dla klienta LOT. Klient dopiero zaczyna pracować z JRWA (od 2025 roku zobligowani), użytkownicy kompletnie nie znają struktury katalogów. Konieczne jest wsparcie dla wyszukiwania i podpowiadania. Prezentacja dla klienta zaplanowana jutro (28.11.2025).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Obsługa typu źródła JRWA w polu Odnośnik do źródła zewnętrznego | **Marek** | Full sprint | - |
| Dodanie pliku instrukcji/schematu JRWA | **Marek** | Część sprintu | - |

**Szczegóły techniczne:**
- Pole: `Odnośnik do źródła zewnętrznego`
- Mechanizm wyszukiwania: Analogiczny do GUS TERYT
- Wyświetlanie: Pełna ścieżka w drzewie od wybranej pozycji (np. `016` → pozycja `016` + podkategorie `0160`, `0161`, `0162`, `0163`)
- Przypisywanie tylko do ostatecznych gałązek (kategorii archiwalnych)

**Decyzje podjęte przy planowaniu:**
- Klient (LOT) nie widzi potrzeby nadawania uprawnień do katalogów JRWA – wszyscy widzą wszystkie katalogi
- 💭 Pomysł: Podpowiadanie ostatnio używanych katalogów JRWA (analogicznie do "Ostatnio użyte procesy" w nawigacji) – **nie MVP**, do rozważenia w przyszłości
- 💭 Pomysł: Rozszerzenie mechanizmu "ostatnio używane" na wszystkie pola typu Odnośnik, słowniki, listy wyboru (np. najczęściej wybierani użytkownicy do akceptacji)

**Ryzyka:**
- Klient nie zna struktury JRWA – może nie wiedzieć, co wpisać w wyszukiwarkę bez widoku pełnego drzewa

---

### Widok sprawy - wygląd i UX

**Kontekst i cel:**
Poprawienie porozjeżdżanych elementów widoku sprawy zgłoszonych przez użytkowników.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawienie UX tabeli na sprawie (scroll vs. przycisk "plus") | **Mariusz** | Część sprintu | - |
| Przegląd i wyrównanie wyglądu całego formularza sprawy | **Mariusz** | Część sprintu | - |
| Spójność kolorów, selektów, podświetleń | **Mariusz** | Część sprintu | - |
| Podświetlenie scrollbara przy hover (jak w Teams) | **Mariusz** | Część sprintu | - |

**Szczegóły techniczne:**
- Problem: Scroll i przycisk "plus" (dodawanie wiersza) są bardzo blisko siebie – użytkownicy klikali "plus" zamiast scroll
- Zmiana: Dodawanie wiersza teraz jednoetapowe (wcześniej dwuetapowe)
- Niespójności: Różne kolory czarnego, różne podświetlenia pól (część na niebiesko cała wartość, część tylko fragment)

**Decyzje podjęte przy planowaniu:**
- Cel: Zamknięcie tematu wyglądu sprawy w tym sprincie

---

### Edytor graficzny formularza i matryca uprawnień

**Kontekst i cel:**
Dokończenie prac nad edytorem graficznym i matrycą uprawnień.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Dokończenie edytora graficznego formularza | **Przemek Rogaś, Filip** | Część sprintu | - |
| Dokończenie matrycy uprawnień | **Przemek Rogaś, Filip** | Część sprintu | - |
| Dodanie tłumaczeń etapów w matrycy | **Przemek Rogaś, Filip** | - | - |
| Wyszukiwarka pól w matrycy uprawnień | **Przemek Rogaś, Filip** | - | - |
| Opcja "zwiń/rozwiń wszystko" w matrycy | **Przemek Rogaś, Filip** | - | - |
| Edycja uprawnień sekcji w matrycy | **Przemek Rogaś, Filip** | - | - |
| Obsługa pustych pól (wszystkie 3 widoki) | **Przemek Rogaś, Filip** | - | - |

**Decyzje podjęte przy planowaniu:**
- Cel: Zamknięcie tematu edytora graficznego w tym sprincie (stan: funkcjonalny, nie wymaga dalszego rozwoju, tylko ewentualne usprawnienia)

---

### Repozytorium plików

**Kontekst i cel:**
Uruchomienie modułu repozytorium plików do końca sprintu (instalacja u klienta Piotra Murawskiego w piątek ostatniego dnia sprintu).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Zarządzanie drzewem katalogów (przestrzenie, foldery) | **Filip, Ania** | ✅ Już zrobione (backend) | - |
| Frontend zarządzania drzewem | **Filip** | ✅ Już zrobione | - |
| Dodawanie/edycja/usuwanie folderów | **Filip** | ✅ Już zrobione | - |
| Poprawienie UX edycji nazwy (inline, bez ikony ołówka) | **Filip** | - | - |
| Dodanie ikony kosza do usuwania przestrzeni | **Filip** | - | - |
| Wyszukiwanie w strukturze (analogiczne do komunikatora) | **Filip** | 🔄 Częściowo | Wyszukuje tylko po widocznych elementach, wymaga rozbudowy |
| Wyświetlanie plików (widok kafelkowy) | **Filip, Ania** | - | - |
| Dodawanie plików (drag & drop + przycisk "Dodaj plik") | **Ania** | - | Backend do zarządzania dokumentami |
| Podgląd plików | **Ania, Filip** | - | - |
| Uprawnienia do przestrzeni | **Ania, Filip** | Cel na ten sprint | - |
| Historia zmian | **Ania, Filip** | ⏸️ Przełożone | Ostatni element MVP |

**Szczegóły techniczne:**
- Lokalizacja w menu: Moduł w obszarze "Wszystkie procesy" (analogicznie do Nadawcy, Przelewów bankowych)
- Struktura: Przestrzenie (najwyższy poziom) → Foldery → Pliki
- Widok: Dwukolumnowy (lewy panel: struktura drzewa, prawy panel: lista plików w formie kafelków)
- Kafelki plików: Analogiczne do widoku dokumentów na sprawie (ikona typu dokumentu, nazwa, data, 3 kropki z opcjami)
- Foldery: Ikona folderu + nazwa (również jako kafelki)
- Edycja inline: Kliknięcie w nazwę → edycja inline (bez ikony ołówka, spójnie z listą pól)
- Usuwanie: 3 kropki przy przestrzeni → opcja "Usuń" (tylko jeśli pusta)
- Drag & drop: Upuszczanie plików na całą przestrzeń roboczą (fioletowe podświetlenie przy hover)
- Dodawanie wielu plików: Analogicznie do sprawy – wybór wielu plików, kolejkowanie uploadu

**Decyzje podjęte przy planowaniu:**
- Nazwa "przestrzeń" zachowana (alternatywa: "repozytorium", zdecydowano zostawić "przestrzeń")
- Widok domyślny: Kafelkowy (widok lista ukryty w MVP)
- Sortowanie przestrzeni: W kolejności dodania (alfabetyczne opcjonalne w przyszłości)
- Wyszukiwarka: Przeniesiona z górnego paska (jak w komunikatorze) do paska narzędzi (jak w edytorze graficznym)
- Wielkość czcionki: 14px (spójnie z komunikatorem, nie 16px)
- 3 kropki: Przy nazwie przestrzeni (nie w drzewku nawigacyjnym) – zawiera: Uprawnienia, Usuń, (w przyszłości: Dodaj folder)
- Uprawnienia: Na poziomie przestrzeni (w MVP), dziedziczenie folderów w przyszłości
- Tryb zarządzania: Brak osobnego trybu edycji (uprawnienia dostępne bezpośrednio przez 3 kropki)

**Ryzyka:**
- Bardzo ambitny plan – konieczna pełna dedykacja zespołu (Ania, Filip, testerki) przez cały sprint
- Testowanie: Wymagane codzienne przekazywanie zmian do testów (nie czekanie do końca sprintu)
- Instalacja u klienta: Koniec sprintu (piątek) – konieczne wcześniejsze testy regresyjne

---

### Raporty - stabilizacja i indeksowanie

**Kontekst i cel:**
Poprawienie błędów w raportach tabelarycznych i filtrach, wdrożenie mechanizmu indeksowania pól tekstowych dla poprawy wydajności.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Indeksowanie pól tekstowych – konfiguracja po stronie procesu | **Mateusz** | Część sprintu | - |
| Usprawnienia filtrów – domyślny operator "zawiera" dla pól tekstowych | **Przemek Rogaś** | - | - |
| Usprawnienia filtrów dat – domyślne wartości (bieżący miesiąc, bieżący rok) | **Przemek Rogaś** | ✅ Częściowo zrobione | - |
| Poprawienie błędów: przeładowanie raportu przy zmianie nazwy | **Przemek Rogaś** | - | Backend + Frontend |
| Poprawienie błędów: filtry po podpisaniu dokumentów | **Przemek Rogaś** | - | - |
| Poprawienie błędów: sortowanie, zaokrąglenia liczb, eksporty | **Przemek Rogaś** | - | - |
| Poprawienie błędów: drzewko po lewej stronie (filtrowanie, podsumowania) | **Przemek Rogaś** | - | - |

**Szczegóły techniczne:**
- Indeksowanie: Tworzenie dodatkowej tabeli indeksowanej dla pól tekstowych (nie bezpośrednie indeksy na kolumnach `CaseDefinition`)
- Konfiguracja indeksowania:
  - Lokalizacja: Ustawienia procesu (React)
  - Widok: Dwa kontenery (lewy: pola dostępne do indeksowania, prawy: zaindeksowane pola – drag & drop)
  - Limit: Max 10 pól indeksowanych na proces
  - Filtrowanie: Tylko pola tekstowe, listy wyboru
- Filtry – operator domyślny:
  - Pola tekstowe: Zmiana z "równa się" na "zawiera" (już możliwe przez "Ustaw wartość domyślną")
  - 💭 Pomysł: Dodanie operatora "zaczyna się od" (wyszukiwanie od początku, bardziej optymalne niż "zawiera")
- Filtry dat – kolejność wartości:
  - Najczęściej wybierane na początku: Bieżący miesiąc, Bieżący rok, Bieżący dzień
  - Rzadziej: Poprzedni miesiąc, Poprzedni rok, Zakres dat

**Decyzje podjęte przy planowaniu:**
- Indeksowanie: MVP – konfiguracja na poziomie ustawień procesu (analogicznie do ustawień systemowych React)
- Indeksowanie automatyczne (na podstawie typu pola) – odrzucone, zbyt mało kontroli
- Mateusz: Przesunięcie priorytetów z serwerów MCP na indeksowanie (serwery MCP zaplanowane na Q1 2026)
- Lokalizacja ustawień indeksowania: Ustawienia procesu → zakładka "Indeksowanie" lub "Wydajność"
- 💭 Pomysł: Źródło widoku indeksowania – analogicznie do raportów (drag & drop między kontenerami)

**Ryzyka:**
- Praca ciągła nad raportami – dużo zgłoszeń od użytkowników
- Wymagana współpraca backend + frontend przy większości błędów

---

### Teczki JRWA - przypisywanie spraw

**Kontekst i cel:**
Umożliwienie przypisywania spraw do teczek JRWA oraz zarządzania teczkami.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Pole Odnośnik do procesu "Teczki JRWA" | **[Do przypisania]** | - | - |
| Filtr zaawansowany w polu Odnośnik (wybór teczki) | **[Do przypisania]** | - | - |
| Dodawanie nowej teczki z poziomu filtru | **[Do przypisania]** | - | - |

**Szczegóły techniczne:**
- Pole typu: Odnośnik do procesu "Teczki JRWA"
- Wyszukiwanie: Po nazwie teczki, symbolu teczki (cztero-/pięcioznakowy), roku
- Wyświetlanie w filtrze: Nazwa + symbol teczki
- Dostępne akcje z filtru: Wybór istniejącej teczki, Dodanie nowej teczki, Uruchomienie nowej sprawy w ramach teczki

**Decyzje podjęte przy planowaniu:**
- Konsultanci otrzymali wytyczne do dostosowania mockupów (przycisk "Dodaj nową sprawę" z poziomu wyszukiwania zaawansowanego)

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| Mechanizm "ostatnio używane" dla wszystkich pól typu Odnośnik/słowniki | Usprawnienie UX – podpowiadanie ostatnio wybranych wartości (analogicznie do "Ostatnio użyte procesy") | 💡 Propozycja | Zmniejszenie klikania, szybsze wypełnianie formularzy. Wymaga zapisywania historii wyborów użytkownika (lokalnie lub w bazie). |
| Spójny system designu dla komponentów React | Ujednolicenie wyglądu tabelek, kafelków, edycji inline, 3 kropek (pionowe vs. poziome), czcionek (wielkość, grubość), paddingów | ✅ Zatwierdzone | Konieczne spotkanie frontendowców (Przemek Rogaś, Filip) + Damian/Kamil – spisanie zasad, utworzenie Storybook z komponentami. Uniknięcie niespójności między widokami. |
| Przerobienie ustawień procesu na React | Umożliwienie dodania konfiguracji indeksowania | ✅ Zatwierdzone | Pierwszy krok: Przerobienie zakładki głównej ustawień procesu 1:1 na React (wymaga pracy backend – wystawienie API). |
| Prawy przycisk myszy w repozytorium | Wykorzystanie kontekstu prawego przycisku myszy (jak w "Zarządzanie organizacją") | 💡 Propozycja odrzucona | Decyzja: Zostawienie 3 kropek przy nazwach (spójność z resztą systemu). Prawy przycisk myszy używany rzadko w systemie. |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Kontekst | Wpływ | Mitygacja | Właściciel |
|---------------|----------|-------|-----------|------------|
| Brak pełnej dedykacji zespołu repozytorium | Jeśli Filip czeka na Anię lub odwrotnie, może być przestój | Wysoki | Filip: Priorytet = repozytorium, w razie przestoju kontakt z Kamilem o dodatkowe zadania z edytora/matrycy. Ania: Priorytet = repozytorium, wyjątek tylko hotfixy. | Damian |
| Opóźnione testowanie repozytorium | Jeśli testy zaczną się pod koniec sprintu, nie będzie czasu na poprawki | Wysoki | Codzienne przekazywanie zmian do testów (nie czekanie do końca sprintu). Testerki (Oktawia, Patrycja) dedykowane do testowania repozytorium. | Damian |
| Instalacja repozytorium u klienta pod koniec sprintu | Jeśli pojawią się błędy na produkcji, brak czasu na poprawki | Średni | Instalacja na środowisku testowym w środku sprintu, testy regresyjne przed instalacją u klienta. | Damian |
| Brak środowiska testowego dla JRWA | Klient LOT dopiero zaczyna pracować z JRWA, może brakować danych testowych | Średni | Współpraca z konsultantami wdrożeniowymi (Kamil, Łukasz Bott) – przygotowanie próbnych danych. | Kamil |
| Brak spójnego system designu | Różne style komponentów (tabelki, edycja inline, 3 kropki, czcionki) | Średni | Spotkanie frontendowców + spisanie zasad, utworzenie Storybook. | Przemek Rogaś, Filip |

---

## 5. Organizacja pracy

- **Urlopy:** Brak informacji
- **Spotkania:**
  - Prezentacja JRWA dla klienta LOT (jutro, 28.11.2025)
  - Planowana instalacja repozytorium u Piotra Murawskiego (piątek, koniec sprintu)
- **Przesunięcia:**
  - Mateusz: Serwery MCP → Indeksowanie pól
  - Ania: Podglądy szablonów → Repozytorium plików
  - Przemek Rogaś, Filip: Pełna dedykacja na edytor graficzny, matrycę, raporty (w razie przestoju)

---

## 6. Pomysły do rozważenia (nie MVP)

- 💭 **Ostatnio używane wartości dla pól Odnośnik/słowniki** (analogia: "Ostatnio użyte procesy")
- 💭 **Operator "zaczyna się od" dla filtrów tekstowych** (bardziej optymalny niż "zawiera")
- 💭 **Drag & drop sortowania przestrzeni w repozytorium** (jak w lewym menu)
- 💭 **Tryby wyświetlania plików** (małe ikony, duże ikony, lista, kafelki – jak w Windows)
- 💭 **Konfiguracja metadanych wyświetlanych pod kafelkiem pliku** (data, autor, rozmiar)
- 💭 **Historia zmian w repozytorium** (kto co dodał/usunął)
- 💭 **Automatyczne rozpoznawanie AI treści sprawy → sugerowanie kategorii JRWA**

---

## Powiązane projekty

- Klienci/WIM/Repozytorium-plikow-DMS
- Klienci/LOT/JRWA
- Moduly/Modul-raportowy
- Moduly/Edytor-procesow/Edytor-formularzy
- Moduly/Edytor-procesow/Matryca-uprawnien
- Moduly/Edytor-procesow/Edytor-formularzy
- cross-cutting/Interfejs-sprawy/Formularz-sprawy
- Klienci/LOT/JRWA
- Klienci/WIM/Komunikator
- cross-cutting/Design-System
