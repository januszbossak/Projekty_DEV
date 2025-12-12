# Spotkanie projektowe – 2025-12-03

**Data:** 2025-12-03  
**Typ:** Spotkanie projektowe  
**Temat główny:** Błędy w formularzach (Adecco hotfix), procedury aktualizacji, walidacja dat

---

## 1. Brak tłumaczeń przycisków na liście spraw (Wersje językowe)

**Komponent:** Cross-cutting / Interfejs sprawy

### Kontekst i cel

Zgłoszenie błędu dotyczącego braku tłumaczeń przycisków na liście spraw do wykonania. Klient używa starej wersji AMODIT (grudniowa z zeszłego roku). Błąd prawdopodobnie istnieje od zawsze, ale dopiero teraz został wykryty.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Mobilizacja klienta do aktualizacji wersji systemu (co najmniej do czerwcowej). To nie jest hotfix - błąd nie działał od zawsze, klient po prostu go wykrył dopiero teraz.

**Szczegóły techniczne:**
- Wersja klienta: grudniowa (zeszłoroczna)
- Wersja grudniowa jest oficjalnie zablokowana i nie otrzymuje już poprawek
- Zalecana wersja: czerwcowa (minimum)

### Punkty otwarte

- Łukasz Bott zgłosił szerszy temat wersji językowych do poruszenia na jutrzejszej Radzie Architektów
- Kolega Walter znalazł artykuł na Wiki opisujący różne aspekty obsługi wersji językowych - wymaga globalnego podejścia

---

## 2. PKF - Brak możliwości edycji klucza rejestru

**Komponent:** Moduły / Proces-rejestr

### Kontekst i cel

W środowisku testowym PKF (wersja marcowa przyszłoroczna) po kliknięciu przycisku "Edytuj klucz" w definicji rejestru pojawia się szary ekran z błędem JavaScript.

### Decyzja / Ustalenie

**Status:** 🔍 Do naprawienia

Mechanizm edycji klucza rejestru działa sprawnie na innych wersjach. Problem dotyczy tylko środowiska testowego PKF, które zainstalowało wersję marcową (develop) z powodu potrzeby konkretnej funkcjonalności zrealizowanej przez Piotrka Łuczkowskiego.

**Szczegóły techniczne:**
- Błąd: "Cannot read property" (JavaScript)
- Środowisko: PKF testowe
- Wersja: marcowa przyszłoroczna (develop)

### Zadania / Dalsze kroki

- **Do przypisania:** Naprawienie błędu - szybkie do zrealizowania (moim zdaniem - Łukasz Bott)

---

## 3. Walidacja pól typu data - funkcje już istnieją

**Komponent:** Moduły / Silnik-regul

### Kontekst i cel

Propozycja wprowadzenia automatycznej walidacji pól typu data na formularzu, aby uniknąć konieczności każdorazowego wyklikania komunikatu o niedozwolonej dacie. Zgłaszający zaproponował walidację na poziomie formularza lub za pomocą funkcji.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Nowa funkcjonalność walidacji | Stworzenie nowego mechanizmu walidacji dat | ❌ Odrzucona – funkcje już istnieją |
| Użycie istniejących funkcji | `SetDateFilters`, `ValidateDateField` | ✅ Wybrana – wystarczy używać |

### Decyzja / Ustalenie

**Status:** ✅ Rozwiązane – funkcje już istnieją

Funkcje do walidacji dat już istnieją w silniku reguł:
- **`SetDateFilters`** – blokuje wybór dat poza określonym zakresem w kalendarzyku
- **`ValidateDateField`** – walidacja wprowadzonych dat

Wystarczy wpisać "date" w wyszukiwarce reguł, aby zobaczyć listę dostępnych funkcji.

### Punkty otwarte

**Problem wiedzy o funkcjach:**
- Damian Kamiński (5+ lat doświadczenia) nie wiedział o istnieniu funkcji `SetDateFilters`
- **Potrzeba lepszego Copilota:** Copilot musi sensownie odpowiadać na tego typu problemy bez konieczności znajomości dokładnej nazwy funkcji
- **Brak artykułów Wiki:** Funkcje mają tylko techniczne opisy w specyfikacji, brakuje artykułów instruktażowych
- **Nakaz używania Copilota:** Absolutny nakaz dla zespołu
- **Nakaz uzupełniania artykułów:** Jeśli artykułu nie ma, musi się pojawić

**Propozycja Damiana:** Przygotowywanie zadań w ramach dobrych praktyk z użyciem specyficznych funkcji, aby podnosić świadomość zespołu.

---

## 4. Nieprawidłowa widoczność komentarzy dla użytkowników zewnętrznych (GTA)

**Komponent:** Cross-cutting / GTA - dostęp tymczasowy do sprawy

### Kontekst i cel

W Neuca (wersja czerwcowa najnowsza) sekcja komentarzy przeznaczona dla użytkowników wewnętrznych jest widoczna dla użytkowników zewnętrznych (grant temporary access). Użytkownicy zewnętrzni nigdy nie powinni mieć możliwości edytowania komentarzy.

### Decyzja / Ustalenie

**Status:** 🔍 Do weryfikacji

Kamil Dubaniowski weryfikuje:
1. Czy dotyczy użytkowników zewnętrznych (MSIT) czy tymczasowych (GTA)
2. Czy klient zdefiniował dozwolone wartości w `GrantTemporaryAccessToCase` (parametr `allowedButtons`)
3. Czy problem dotyczy tylko wyświetlania listy komentarzy, czy też możliwości ich edycji

**Szczegóły techniczne:**
- Funkcja: `GrantTemporaryAccessToCase`
- Parametr: `allowedButtons` (definiuje widoczne przyciski w sprawie)
- Domyślnie komentarze są ukryte dla użytkowników zewnętrznych
- Dla tymczasowych (GTA) - wymaga weryfikacji

### Ograniczenia / Poza zakresem

Kamil wspomina o funkcji `HideElement`, która również ukrywa elementy interfejsu - należy uwzględnić w weryfikacji.

### Zadania / Dalsze kroki

- **Kamil Dubaniowski:** Przetestować na wyższej wersji, poszukać wcześniejszego zgłoszenia, zweryfikować czy działa jak należy
- **Eryk:** Sprawdzić po swojej stronie (Neuca)

### Punkty otwarte

- Czy to jest bug (komentarze się pokazują mimo braku konfiguracji), czy klient świadomie je udostępnił?
- Jeśli zdefiniowali `allowedButtons` z komentarzami, ale nie da się ich kliknąć - to też bug

---

## 5. Wyświetlanie starego interfejsu wewnątrz nowego (Edytor formularza)

**Komponent:** Moduły / Edytor-procesow / Edytor-formularzy

### Kontekst i cel

W edytorze formularza na liście pól, po wejściu do tabeli (kliknięcie na pole typu tabela), doładowuje się całe menu jeszcze raz - w starym interfejsie. Domyślnie widok listy pól jest w nowym interfejsie (OK), ale po wejściu do tabeli pojawia się stary.

### Decyzja / Ustalenie

**Status:** ⏸️ Odroczone

Nie naprawiamy do wersji czerwcowej - zbyt duży koszt. Wymaga pracy Przemka Rogasia lub Filipa (frontend), a nie ma dostępnych zasobów.

**Alternatywa:** Wymuszenie jak najszybszego zamknięcia i wydania wersji grudniowej, w której ten problem już nie występuje (nowy interfejs listy pól od grudniowej).

### Punkty otwarte

- Piotr Górski robi zmiany na produkcji w PKF - wymaga wyjaśnienia procedur (nie powinien modyfikować procesów na produkcji, tylko na testowym i przenosić definicję)

---

## 6. **KRYTYCZNY HOTFIX: Adecco - Zmieniony wygląd tabeli wyświetlanej jako formularz**

**Komponent:** Cross-cutting / Interfejs-sprawy / Formularz-sprawy

### Kontekst i cel

Po aktualizacji Adecco do wersji czerwcowej (wczoraj wieczorem) tabela wyświetlana w trybie "jako formularz" całkowicie się rozjechała. Proces dotyczy zgód i oświadczeń wysyłanych do kandydatów (około 100 formularzy w obiegu z 3-dniowym terminem). Kandydaci nie mogą wypełnić formularzy.

**Wykryte problemy:**

1. **Checkboxy znikły** - pole typu "tak/nie" (checkbox) w trybie "jako formularz" nie wyświetla się wcale
2. **Opcja "ukryj etykietę pola" nie działa** - etykiety się wyświetlają mimo zaznaczenia opcji
3. **Nazwy pól static text się wyświetlają** - pola statyczne z założenia nie mają wyświetlanej etykiety, a teraz mają
4. **Tabela jednowierszowa wyświetla dodatkowy poziom** - w starszych wersjach (marcowa) jednowierszowa tabela nie wyświetlała dodatkowej pozycji do rozwinięcia, tylko plusik do dodania. Teraz wyświetla się poziom rozwinięcia
5. **Przycisk "usuń wiersz" widoczny w trybie tylko do odczytu (mobile)** - w trybie mobilnym można usunąć wiersz mimo trybu "tylko do odczytu"
6. **Duplikacja kolumn z etykietami** - kolumna z etykietami pól pojawia się zarówno po lewej, jak i po prawej stronie (powinna być tylko po lewej, zamrożona)

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Szybka naprawa CSS/JavaScript | Ukrycie lewej kolumny CSS-em, naprawa checkboxów JavaScriptem w ustawieniach procesu | ⏸️ Rozważana - ryzyko konsekwencji |
| Cofnięcie wersji produkcyjnej | Rollback Adecco prod do marcowej | ✅ Wybrana - natychmiastowe działanie |
| Naprawa systemowa + testy | Pełna naprawa błędów, testy na dev, potem aktualizacja prod | ✅ Wybrana - po cofnięciu wersji |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone - HOTFIX

**Natychmiastowe działania (Michał Zwierzchowski + Daniel Reszka):**
1. **Cofnięcie wersji produkcyjnej Adecco do marcowej** - natychmiast (100 formularzy czeka, terminy 3-dniowe)
2. **Zostawienie dev na czerwcowej** - do testów poprawek
3. **Komunikacja z klientem** - poinformowanie o cofnięciu wersji i przyczynie

**Dalsze kroki (Mariusz + Damian):**
1. Naprawienie wszystkich wykrytych błędów na dev
2. Testy przez klienta na dev (wszystkie ścieżki formularzy - około 4-5)
3. Po zatwierdzeniu przez klienta - aktualizacja produkcji

**Szczegóły techniczne:**
- Wersja problematyczna: czerwcowa (2025)
- Wersja rollback: marcowa (2025)
- Środowiska Adecco: dev, pity (nieistotne), prod
- Proces: Rekrutacja - zgody i oświadczenia
- Tryb wyświetlania: tabela jako formularz, jednowierszowa
- Opcje: "ukryj etykietę pola", "jednowierszowa"

### Ograniczenia / Poza zakresem

**Przypadek specyficzny dla Adecco:**
- Użycie tabeli jako obejścia limitu pól na formularzu głównym (powinny być pola formularza głównego, ale było ograniczenie)
- Mieszanka typów pól: checkbox, radio button, static text
- Instrukcje umieszczone w etykietach pól (brak dedykowanego mechanizmu)

### Feedback / Uwagi uczestników

**Janusz Bossak:**
- "Dopóty dopóki nie będzie testów end-to-end, to zginiemy"
- Potrzeba konkretnych przypadków testowych, nie tylko ogólnej funkcjonalności
- Przemek nie zgodził się na zatrudnienie kogoś do pisania testów e2e

**Łukasz Bott:**
- Przykład Deutsche Bank: checklist po aktualizacji testowej, potem produkcja, support hotline następnego dnia, rollback jeśli problemy
- Procedura dla Adecco: dev → testy → prod (jak on-premise, nie jak chmura)

**Kamil Dubaniowski:**
- Tabela była projektowana do zbierania danych (imię, nazwisko), nie do obejść limitu pól
- Jednowierszowa tabela powinna mieć ikonę pojedynczej kartki (zachowane), ale bez poziomów rozwinięcia

**Damian Kamiński:**
- Cofnięcie wersji źle o nas świadczy, ale skala problemu (100 formularzy, terminy) wymaga działania
- Potrzeba przemyślenia wszystkich elementów naprawy, nie tylko szybkich poprawek

### Zadania / Dalsze kroki

- **Michał Zwierzchowski:** Cofnięcie wersji prod Adecco do marcowej (natychmiast)
- **Daniel Reszka:** Komunikacja z klientem o cofnięciu wersji
- **Mariusz (+ Damian Kamiński):** Naprawienie błędów na dev:
  1. Opcja "ukryj etykietę" - ma ukrywać właściwe elementy (treść pola, nie etykietę)
  2. Nazwy pól static text - nie powinny się wyświetlać
  3. Tabela jednowierszowa - brak dodatkowego poziomu rozwinięcia
  4. Przycisk "usuń" w trybie odczytu (mobile) - ukrycie
  5. Duplikacja kolumn z etykietami - tylko jedna kolumna po lewej
- **Damian Kamiński:** Współpraca z Mariuszem - zna proces, wie jak powinno wyglądać

### Punkty otwarte

**Procedury aktualizacji (organizacyjne):**
- Adecco i inni duzi klienci z dev/test muszą mieć procedurę: dev → testy → prod (jak on-premise)
- MSIT jest jedynym klientem chmurowym z taką procedurą - trzeba rozszerzyć na wszystkich dużych
- Nie można podnosić dev i prod jednocześnie

**Testy end-to-end:**
- Playwright, Cypress - wymaga full-time job
- Kursy dostępne (część darmowa, część płatna z pomocą - kilkadziesiąt tysięcy złotych)
- Michał Zwierzchowski zaczął przeglądać materiały

**Rozwiązania długofalowe:**
- Opcja na poziomie tabeli: "ukryj etykiety w trybie formularza" (dla przypadków jak Adecco)
- Mechanizm instrukcji do pól (zamiast umieszczania w etykietach) - propozycja: ikona "i" z popupem (wzór: mBank, WordPress)
- Hover niekoniecznie pożądany (przeskakuje przy przewijaniu), lepiej kliknięcie lub ikona

---

## 7. Procedury aktualizacji dla klientów chmurowych

**Komponent:** Organizacja-DEV / Dokumentacja-organizacyjna

### Kontekst i cel

Brak procedur testowania przed aktualizacją produkcji dla klientów chmurowych. Adecco i prod zostały zaktualizowane jednocześnie, co doprowadziło do krytycznego błędu na produkcji.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

**Nowa procedura dla dużych klientów chmurowych z dev/test:**
1. Aktualizacja środowiska dev/test
2. Testy przez klienta (checklist krytycznych ścieżek)
3. Aktualizacja produkcji tylko po zatwierdzeniu testów
4. Support/hotline następnego dnia po aktualizacji produkcji
5. Rollback jeśli problemy - dopóki nie zostanie naprawione

**Klienci do objęcia procedurą:**
- **Adecco** - traktować jak on-premise (ma 3 oddzielne witryny: dev, pity, prod)
- **MSIT** - już ma taką procedurę (wzorcowy)
- Wszyscy duzi klienci z środowiskiem testowym

**Wzór:** Deutsche Bank (Łukasz Bott)

### Ograniczenia / Poza zakresem

Mniejsi klienci chmurowi bez środowiska testowego - pozostają w standardowym modelu chmurowym (aktualizacje zbiorowe).

---

## 8. Testy end-to-end - potrzeba automatyzacji

**Komponent:** Organizacja-DEV / Dokumentacja-organizacyjna / Narzędzia

### Kontekst i cel

Potrzeba automatycznych testów end-to-end, aby wykrywać regresje przed wdrożeniem na produkcję. Przypadek Adecco pokazał, że testy funkcjonalne (czy działa) nie wystarczą - potrzebne są testy na konkretnych przypadkach biznesowych.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Zatrudnienie osoby do testów e2e | Dedykowany tester automatyczny | ❌ Odrzucona - Przemek nie zgodził się |
| Playwright / Cypress | Narzędzia do testów e2e | 🔍 Do rozważenia - wymaga full-time job |
| Kursy z pomocą | Płatne kursy z asystą (kilkadziesiąt tys. zł) | 🔍 Do rozważenia |

### Decyzja / Ustalenie

**Status:** 🔍 Do dalszej analizy

Michał Zwierzchowski zaczął przeglądać kursy Playwright/Cypress. Janusz Bossak również próbował, ale utknął (full-time job, nawet z AI).

### Punkty otwarte

**Dwa rodzaje testów:**
1. **Testy funkcjonalne** - czy funkcjonalność działa w ogóle
2. **Testy przypadków biznesowych** - czy działa w konkretnych, pokręconych scenariuszach klientów (jak Adecco)

Problem: Trudno przewidzieć wszystkie przypadki biznesowe bez testów na żywych procesach klientów.

---

## Podsumowanie

**Najważniejsze ustalenia:**
1. ✅ **Adecco hotfix** - cofnięcie wersji prod, naprawa na dev, testy, potem aktualizacja
2. ✅ **Procedury aktualizacji** - dev → testy → prod dla dużych klientów
3. ✅ **Walidacja dat** - funkcje już istnieją, potrzeba lepszego Copilota i artykułów
4. 🔍 **Testy e2e** - do dalszej analizy (Playwright/Cypress)
5. 🔍 **Wersje językowe** - szerszy temat na jutrzejszą Radę Architektów

**Krytyczne zadania:**
- Michał: Cofnięcie Adecco prod (natychmiast)
- Mariusz + Damian: Naprawa formularzy na dev
- Kamil: Weryfikacja komentarzy GTA
- Łukasz: Temat wersji językowych na Radę
