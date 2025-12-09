> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-09

# Rada Architektów – 2025-11-27

**Powiązane projekty:**
- Moduly/Edytor-procesow/Edytor-reguł
- cross-cutting/Interfejs-sprawy/Formularz-sprawy
- Klienci/LOT/JRWA

**Tematy:**
- Edytor reguł tabeli - integracja z Reactowym formularzem (lista pól)
- Formularze w trybie wizard (krokowe wypełnianie) - koncepcja dla mobilnych użytkowników
- JRWA (Jednolity Rzeczowy Wykaz Akt) - implementacja źródła zewnętrznego

---

## 1. Edytor reguł tabeli - obsługa zamykania z React

### Kontekst i Problem

Na nowej liście pól (Reactowej) dodano akcję "Reguły tabeli", która ma otwierać stary edytor reguł. Edytor ten był wcześniej dostępny tylko w starym formularzu Angular. Problem polega na tym, że edytor wywołuje funkcję `window.parent.close()` do zamknięcia okna, ale w kontekście React ta funkcja nie istnieje. Obecnie edytor otwiera się w nowej karcie zamiast w popup, a przyciski "Anuluj" i "Zapisz" nie zamykają okna.

Docelowo edytor reguł ma być całkowicie przerobiony na React, ale to większy temat na przyszłość. Na teraz potrzebne jest tymczasowe rozwiązanie.

### Zidentyfikowane Ryzyka

- Ryzyko "psucia" starego edytora podczas wprowadzania zmian
- Brak funkcji `close dialog` w React może powodować, że użytkownik nie może zamknąć edytora
- Otwieranie w nowej karcie zamiast popup pogarsza UX

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Modyfikacja starego edytora | Przerobienie logiki zamykania w starym edytorze Angular | ❌ Odrzucona - ryzyko psucia działającego kodu |
| Dodanie funkcji `closeDialog` w React | Stworzenie funkcji JavaScript w React, która zamknie zakładkę/popup | ✅ Wybrana - niskie ryzyko, rozwiązanie analogiczne do OAuth (Przemek robił wczoraj) |
| Natychmiastowe przerobienie edytora na React | Całkowity przepis edytora reguł na React | ⏸️ Odroczona - zbyt duży zakres, zaplanowane na przyszłość |

### Decyzja

**Status:** ✅ Zatwierdzone

Filip Liwiński doda w React funkcję JavaScript `closeDialog` (analogiczną do tej w starym Angular), która będzie obsługiwać zamykanie edytora reguł. Edytor będzie się otwierał w popup (iframe pełnoekranowy) w kontekście React. Przyciski "Anuluj" i "Zapisz" w edytorze będą wywoływać `window.parent.closeDialog()`, która zamknie popup.

Rozwiązanie wzorowane na implementacji Przemka dla OAuth, gdzie podobnie dodano funkcję JavaScript do React obsługującą komunikację ze starym kodem.

Docelowo edytor ma otwierać się w popup (nie w nowej karcie), aby zachować kontekst użytkownika na liście pól.

**Szczegóły techniczne:**
- Funkcja: `window.parent.closeDialog()`
- Kontekst wywołania: stary edytor Angular
- Miejsce implementacji: strona React (lista pól)
- Wzór implementacji: OAuth (implementacja Przemka)
- Typ okna: popup pełnoekranowy (iframe)

### Zadania

- **Filip Liwiński:** Dodać funkcję `closeDialog` w React, która zamyka popup z edytorem reguł → sprint bieżący (grudzień)
- **Filip Liwiński:** Skonsultować z Przemkiem implementację (wzór: OAuth) i w razie pytań dopytać Piotra Buczkowskiego

### Punkty otwarte

- Czy edytor będzie walidował dane przed zamknięciem, czy tylko zapisze stan?
- Czy popup ma być pełnoekranowy z minimalną ramką, czy standardowy popup?

---

## 2. Formularze w trybie wizard - krokowe wypełnianie (MVP)

### Kontekst i Problem

Klient LPP zgłosił potrzebę usprawnienia wypełniania długich formularzy (200-250 pól) na urządzeniach mobilnych. Obecnie kwestionariusz osobowy jest wypełniany przez pracowników tymczasowych/magazynowych na telefonach, a długi "wąż" pól jest mało czytelny i trudny w nawigacji na małym ekranie. Propozycja: wyświetlanie formularza w trybie "wizard" - sekcja po sekcji, z przyciskami "Następna/Poprzednia sekcja".

Problem dotyczy głównie wypełniania danych przez kandydatów (grant temporary access), ale może być stosowany szerzej (np. zmiana danych osobowych pracownika).

### Zidentyfikowane Ryzyka

- Komplikacja z grant temporary access - obecnie działa na jednym etapie, a rozwiązanie Łukasza (wiele etapów = wiele sekcji) powoduje "rozsypanie" diagramu procesu
- Walidacja reguł automatycznych - obecnie reguły są przypisane do etapu, nie do sekcji; konieczność walidacji po każdej sekcji komplikuje architekturę
- Ryzyko nadmiernej komplikacji MVP - jeśli od razu będziemy chcieli obsługiwać walidację merytoryczną per sekcja

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wiele etapów = wiele sekcji (rozwiązanie Łukasza) | Każda sekcja formularza = osobny etap w procesie | ❌ Odrzucona - diagram procesu staje się nieczytelny (10+ etapów dla jednego formularza), konflikt z grant temporary access |
| Osobny układ pól dla mobile | Dedykowany layout formularza dla widoku mobilnego | 🔍 Do weryfikacji - wymaga analizy, czy struktura sekcji byłaby inna |
| Tryb wizard per etap z przyciskami nawigacji | Jeden etap, ale wyświetlanie sekcji sekwencyjne z przyciskami "Następna/Poprzednia sekcja" | ✅ Wybrana - prosta w implementacji, uniwersalna, nie psuje diagramu |
| Grant temporary access na wielu etapach | Rozszerzenie GT, żeby działał na wielu etapach jednocześnie | ❌ Odrzucona - Piotr Buczkowski ostrzegł: "nie róbcie tego" (zbyt skomplikowane, każdy etap miałby inną sekcję) |

### Decyzja

**Status:** 💡 Propozycja (do wyceny dla klienta)

Wprowadzenie trybu "wizard" dla formularzy, działającego uniwersalnie (nie tylko mobile, ale także desktop). Tryb ten będzie opcjonalny i włączany per proces lub per etap.

**MVP (do zaproponowania klientowi):**
- Przyciski "Następna sekcja" i "Poprzednia sekcja" na dole formularza (lub na górze i dole - do ustalenia w mockup)
- Kliknięcie "Następna" zapisuje stan formularza i otwiera kolejną sekcję (na mobile: zamyka bieżącą, rozwija kolejną)
- Na mobile: wyświetlana tylko jedna sekcja naraz (accordion rozwinięty), przyciski nawigacji na dole
- Na desktop: opcjonalnie widoczne zakładki sekcji + przyciski nawigacji (Andrzej z LPP sugerował przyciski także na desktop)
- Walidacja odbywa się dopiero na końcu (nie per sekcja) - aby uniknąć komplikacji z regułami automatycznymi

**Rozszerzenie (MVP2):**
- Zdarzenie w regule automatycznej: "zmiana sekcji" - pozwala na walidację merytoryczną po wypełnieniu danej sekcji
- Jeśli reguła zwróci błąd, użytkownik zostaje zatrzymany na bieżącej sekcji (nie może przejść dalej)

**Szczegóły techniczne:**
- Przyciski: "Następna sekcja", "Poprzednia sekcja"
- Akcja: zapis stanu formularza + otwarcie kolejnej sekcji
- Widok mobile: accordion z tylko jedną rozwiniętą sekcją
- Widok desktop: zakładki + przyciski (opcjonalnie)
- Nawigacja: tylko między widocznymi sekcjami (niewidoczne sekcje pomijane automatycznie)

### Zadania

- **Damian Kamiński:** Przygotować mockup dla klienta LPP, pokazujący tryb wizard na mobile i desktop
- **Damian Kamiński:** Przygotować wycenę MVP (przyciski + zapis stanu) i MVP2 (walidacja per sekcja)
- **Zespół:** Po akceptacji klienta - zaprojektować szczegóły UX (gdzie przyciski, jak oznaczać bieżącą sekcję)

### Punkty otwarte

- Czy przyciski mają być na dole, czy na górze i dole?
- Czy ma być możliwość przeskakiwania sekcji (np. z pierwszej na ostatnią) poprzez zakładki, czy tylko sekwencyjnie?
- Czy walidacja wymagalności pól ma się odbywać od razu (per sekcja), czy dopiero na końcu?
- Jak oznaczyć wizualnie, w której sekcji użytkownik się znajduje? (progress bar, numeracja, inna wizualizacja?)

---

## 3. JRWA (Jednolity Rzeczowy Wykaz Akt) - implementacja źródła zewnętrznego

### Kontekst i Problem

Klient LOT potrzebuje w formularzu możliwości wyboru klasyfikacji JRWA. JRWA to słownik hierarchiczny (drzewko kategorii dokumentów) z uprawnieniami - nie wszyscy użytkownicy mogą wybierać wszystkie pozycje. Dodatkowo, można wybierać tylko "liście" drzewa (nie węzły nadrzędne).

Rozwiązanie ma być analogiczne do GUS TERYT - czyli pole typu "odnośnik do źródła zewnętrznego", gdzie użytkownik wpisuje tekst (np. "dokumenty rady nadzorczej") i dostaje listę pasujących pozycji JRWA. Po wybraniu, wartość (JSON z pełną informacją o pozycji) zapisuje się do pola.

Różnice względem GUS TERYT:
- Dane nie będą pobierane z zewnętrznego API, tylko z lokalnych tabel AMODIT
- Struktura hierarchiczna (katalogi nadrzędne i podrzędne)
- Uprawnienia - użytkownik widzi tylko te pozycje JRWA, do których ma dostęp
- Wybieralne tylko "liście" (pozycje najniższego poziomu), nie węzły nadrzędne

### Zidentyfikowane Ryzyka

- Komplikacja uprawnień - jeśli każdy użytkownik ma inny zestaw dostępnych pozycji JRWA, trzeba to obsłużyć w zapytaniach SQL
- Brak interfejsu do zarządzania danymi JRWA - na początku dane będą zasilane ręcznie na poziomie bazy danych

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Słowniki hierarchiczne | Wykorzystanie standardowych słowników AMODIT z hierarchią | ❌ Odrzucona - brak mechanizmu uprawnień per pozycja słownika |
| Rejestr | Stworzenie rejestru JRWA (analogicznie jak rejestr kontrahentów) | ❌ Odrzucona - JRWA to dane niezmienne/stałe (jak GUS TERYT), nie wymaga pracy użytkowników; rejestr byłby over-engineeringiem |
| Źródło zewnętrzne typu "klasa" | Implementacja źródła danych jako klasy C# (wzór: GUS TERYT) | ✅ Wybrana - elastyczne, umożliwia uprawnień i walidację, wzór już istnieje w kodzie |

### Decyzja

**Status:** ✅ Zatwierdzone

Implementacja JRWA jako źródła zewnętrznego typu "klasa" (analogicznie jak GUS TERYT). Marek Dziakowski stworzy klasę dziedziczącą po interfejsie źródeł danych, która:
- Wyszukuje pozycje JRWA w lokalnych tabelach AMODIT (nie webservice)
- Filtruje wyniki po uprawnieniach użytkownika
- Zwraca JSON z pełną informacją o wybranej pozycji (symbol, nazwa, poziom hierarchii)
- Umożliwia wybór tylko "liści" drzewa (nie węzłów nadrzędnych)

Dane JRWA będą przechowywane w 2-3 tabelach:
1. Lista pozycji JRWA (ID, symbol, nazwa, parent_id, poziom hierarchii, czy można wybrać)
2. Uprawnienia do pozycji JRWA (ID użytkownika/grupy, ID pozycji)
3. (Opcjonalnie) Przypisania pozycji do procesów/etapów

**Szczegóły techniczne:**
- Typ źródła: klasa (typ 5)
- Wzór implementacji: `GUS_TERYT` (kod w `~\core\bors`)
- Interfejs: implementacja analogiczna jak w GUS TERYT
- Wyszukiwanie: po symbolu i nazwie pozycji JRWA
- Zapis: JSON z property `symbol`, `nazwa`, `poziom`, `parent_id` (lub podobne)
- Tabele: 2-3 tabele (lista, uprawnienia, przypisania)

### Zadania

- **Marek Dziakowski:** Przeanalizować kod GUS TERYT (`~\core\bors\GUS_TERYT`) i zrozumieć mechanizm źródeł zewnętrznych typu "klasa"
- **Marek Dziakowski:** Zaprojektować strukturę tabel dla JRWA (lista pozycji, uprawnienia, przypisania)
- **Marek Dziakowski:** Zaimplementować klasę JRWA dziedziczącą po interfejsie źródeł danych
- **Kamil Dubaniowski:** Opisać szczegółowe wymagania funkcjonalne (np. które pozycje można wybierać, jak filtrować po uprawnieniach) i przekazać Markowi
- **Piotr Buczkowski:** Konsultacja z Markiem na początku implementacji (pierwsze dni sprintu Piotr nieobecny, potem dostępny)

### Punkty otwarte

- Czy JSON zwracany przez źródło ma zawierać pełną ścieżkę hierarchiczną (np. "Kategoria > Podkategoria > Pozycja"), czy tylko ID i nazwę?
- Jak będzie wyglądał interfejs do zarządzania danymi JRWA (dodawanie, edycja pozycji)? Na razie dane będą zasilane ręcznie na poziomie bazy.
- Czy uprawnienia mają być przypisywane per użytkownik, per grupa, czy per rola?
