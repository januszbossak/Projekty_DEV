# Historia zmian - Moduł raportowy

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Cele sprintu - Planowanie sprintu.md]
**Kategoria:** #Bug

- Naprawa bugów w raportach (ogólne ustawienia i raport tabelaryczny).
- Naprawa bugów dotyczących ogólnych ustawień raportów.
- Naprawa bugów z raportu tabelarycznego.
- Naprawa bugów z filtrów (ogólnych).

---

## 2025-11-28 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-28 Notatka projektowa - Połączenie z Marek Dziakowski.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-28%20Notatka%20projektowa%20-%20Połączenie%20z%20Marek%20Dziakowski.md)
**Kategoria:** #Funkcjonalność #Decyzja

- Umożliwienie generowania raportów, które mogą "drążyć" w głąb pól typu `Odnośnik`.
- Użytkownik powinien mieć możliwość wyboru pola typu `Odnośnik` w raporcie, a następnie wyboru pól z procesu, na który ten `Odnośnik` wskazuje.
- Funkcjonalność zostanie wdrożona w ramach prac nad projektem JRWA.

---

## 2025-11-27 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-11-27 Planowanie sprintu.md]
**Kategoria:** #Stabilizacja #Wydajność #UX #PoprawaBłędów

- Cel: Stabilizacja i indeksowanie raportów tabelarycznych oraz poprawa filtrów.
- Zakres prac: Wdrożenie mechanizmu indeksowania pól tekstowych dla poprawy wydajności, poprawienie błędów w raportach tabelarycznych i filtrach.
- Indeksowanie: Tworzenie dodatkowej tabeli indeksowanej, konfiguracja na poziomie ustawień procesu (React), limit 10 pól tekstowych/list wyboru na proces.
- Usprawnienia filtrów: Domyślny operator "zawiera" dla pól tekstowych, domyślne wartości dat (bieżący miesiąc, bieżący rok, bieżący dzień).
- Błędy do poprawy: Niespodziewane przeładowania raportu przy zmianie nazwy, problemy z filtrami po podpisaniu dokumentów, sortowaniem, zaokrągleniami liczb, eksportami i filtrowaniem w drzewku.
- Ryzyka: Duża liczba zgłoszeń od użytkowników, konieczność ścisłej współpracy backend-frontend.

---

## 2025-11-21 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-21 Planowanie sprintu.md]
**Kategoria:** #Wydajność #Funkcjonalność #Zadanie #Design

- Poprawa działania i wydajności filtrów użytkownika w module raportowym.
- Mateusz Kisiel pracuje nad indeksami w celu poprawy wydajności filtrów.
- Szymek/Przemek porządkują operatory daty w filtrach, uspójniając logikę.

---

## 2025-11-25 | Notatka projektowa - Roadmapa 2026 i Strategia Wdrożeniowa
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-11-25 Notatka projektowa - Roadmapa 2026 i Strategia Wdrożeniowa.md]
**Kategoria:** #Funkcjonalność #Architektura

- **Roadmapa Q4 2025:** Podstawowa funkcjonalność tabeli raportów (masowa obsługa spraw) musi działać stabilnie.
- **Roadmapa Q1 2026:** Głęboki refactoring architektury, wykresów, dashboardów i filtrów.

---

## 2025-11-20 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-20 Spotkanie projektowe - Edytor procesów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-20%20Spotkanie%20projektowe%20-%20Edytor%20procesów.md)
**Kategoria:** #Strategia #Decyzja

- Dyskusja priorytetów: Janusz naciska na naprawę Modułu raportowego dla użytkowników końcowych. Przemek sugeruje odłożenie prac do czasu zamknięcia MVP Edytora procesów (argumentując, że raporty i tak nie działają od początku).

---

## 2025-12-02 | ⚠️ Problem | Spotkanie projektowe - Design
**Źródło:** [Notatki/Spotkania projektowe/2025-12-02 Spotkanie projektowe - Design.md]

**Edge case: edycja wierszy tabel w raportach (zgłoszenie PKF)**

PKF zgłosił potrzebę edycji wierszy tabel z poziomu raportu osadzonego na sprawie. Obecny system nie obsługuje edycji danych w raportach – tylko wyświetlanie.

**Problem:**
- Raport wyświetla wiersze z tabel z różnych spraw (np. rejestracja czasu pracy z kilku dni)
- Użytkownik chce zbiorczo edytować te wiersze (korekta godzin, zmiana projektów)
- Brak możliwości edycji danych bezpośrednio z raportu

**Rozważane rozwiązania:**
1. Uproszczone okienka modalne do edycji wiersza tabeli
   - Formularz wiersza istnieje (czasami wyświetla się przy błędach)
   - Teoretycznie możliwe, ale szeroki temat
   - Problem: reguły, zależności, walidacje – jak to obsłużyć w kontekście edycji z raportu?

2. Edycja w trybie Excelowym (inline editing)
   - Edycja wierszy bezpośrednio w raporcie (jak w Excelu)
   - Trudne dla reguł i zależności między polami

3. Edycja przez Excel (Get Excel Data / Set Excel Data)
   - Eksport do Excela, edycja, import z powrotem
   - Problem: nie ma funkcji Set Excel Data
   - Gimnastyka dla użytkownika

**Status:** ⏸️ Odroczone – temat do dyskusji na Radzie Architektów

**Uzasadnienie:**
- Temat bardzo szeroki, wymaga przemyślenia wielu aspektów
- Nie ma obecnie sensownego pomysłu na implementację
- Dla PKF znaleziono obejścia (gimnastyka, ale działa)

**Szczegóły techniczne:**
- Funkcja Get Excel Data istnieje, Set Excel Data NIE istnieje
- Formularz wiersza tabeli istnieje (można go teoretycznie wykorzystać)

**Punkty otwarte:**
- Temat do dyskusji na Radzie Architektów lub osobnym spotkaniu Design
- Nie do realizacji w ciągu kilku dni – wymaga głębszej analizy i koncepcji
- Jak obsłużyć reguły, walidacje i zależności między polami w kontekście edycji z raportu?

**Powiązane projekty:**
- [Klienci/PKF/Rejestracja-czasu-pracy](../../Klienci/PKF/Rejestracja-czasu-pracy/CHANGELOG.md) - konkretny use case PKF

---

## 2025-11-19 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-19 Spotkanie projektowe - Problem odświeżania raportu.md]
**Kategoria:** #Bug #Problem #Decyzja #Funkcjonalność

- Problem z odświeżaniem raportów po akcjach na sprawie, szczególnie w dashboardach.
- Przycisk "Odśwież" w dashboardzie nie działa; w raportach standalone działa.
- Ustalono priorytet (hotfix): naprawa przycisku "Odśwież" w dashboardzie.
- Potrzeba spisania przypadków użycia dla automatycznego odświeżania raportów.
- Istniejące zgłoszenie D123 (v122) dotyczące odświeżania raportu w dashboardzie, oznaczone jako "Done", faktycznie nie działa.

---

## 2025-11-19 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-19 Notatka projektowa - Przegląd wycen.md]
**Kategoria:** #Bug #Funkcjonalność #Design #Decyzja

- Doraźnie należy naprawić działanie przycisku "Odśwież" na dashboardzie.
- Docelowo należy przeanalizować i opisać przypadki użycia dla automatycznego odświeżania raportu.
- Rekord nadal spełniający kryteria: czy ma zostać w tym samym miejscu, a dane odświeżone?
- Rekord przestający spełniać kryteria: czy ma zniknąć natychmiast, czy po ręcznym odświeżeniu?
- Decyzja: Nie wdrażać pochopnych zmian w automatyzacji bez spójnych zasad UX.

---

## 2025-11-17 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-17 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-17%20Planowanie%20sprintu.md)
**Kategoria:** #Bug #Problem #Decyzja

- Wstrzymanie zadań rozwojowych na rzecz stabilizacji i naprawy błędów.
- Decyzja o przeprowadzeniu refaktoryzacji (planowane spotkanie zespołu).
- Agregacja i priorytetyzacja błędów z backlogu.

---

## 2025-11-13 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-13 Rada architektów.md]
**Kategoria:** #Architektura #Zadanie

- Sprawdzenie, czy w nowych raportach jest obsługa Oracle dla `LIMIT`.
- Przejrzenie kodu do generowania zapytań dla zewnętrznych źródeł ODBC.
- Wymagana współpraca z konsultantami Rossmanna i dostęp do środowiska testowego.

---

## 2025-11-12 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-12 Spotkanie projektowe - Przegląd wycen.md]
**Kategoria:** #Bug #Zadanie

- Problem z źródłami Oracle w nowych raportach: `INVALID_CHARACTER` i `LIMIT ?` w zapytaniu.
- Stare raporty działają, problem specyficzny dla nowych.
- Do weryfikacji przez deweloperów, z włączeniem logowania zapytań SQL.
- `LIMIT ?` to składnia MySQL-owa, oczekiwana konkretna liczba.

---

## 2025-11-03 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-03 Sprint review-codex.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-03%20Sprint%20review-codex.md)
**Kategoria:** #Funkcjonalność #UI

- Podgląd raportu na sprawie ujednolicony z podglądem dokumentów: paginacja, widok pełnoekranowy, te same akcje co na sprawie, ładowanie kolejnych stron.
- Do rozważenia: przełączanie między raportami w kontekście wyszukiwania zaawansowanego (odtworzenie funkcji ze starego komponentu).

---

## 2025-10-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-30 Rada architektów.md]
**Kategoria:** #Bug #Diagnostyka

- Problem z otwieraniem raportu w nowym module raportowym u klienta Niden.
- Anna Skupińska ma zająć się tym po zakończeniu hotfixów. Potwierdzić, że logowanie błędów SQL jest zrobione we wszystkich miejscach.

---

## 2025-10-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-27 Spotkanie projektowe - Przegląd projektów.md]
**Kategoria:** #Organizacja #Decyzja

- Z raportami coś się zadeklarowaliśmy w umowie, ale jak zrobimy dwa, to przymkną na to oko.
- Janusz się tym raportom przyjrzy szczegółowo. Przemek jest od Reacta.
- Alternatywa: Damian zrobi raporty systemowe na ich środowisku.

---

## 2025-10-23 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-23 Rada architektow.md]
**Kategoria:** #Funkcjonalność #Decyzja #Problem

- **Eksport danych do szablonów XSLT:** W nowym interfejsie React rozszerzenie pliku ma być przypisane do definicji szablonu XSLT i ustawiane automatycznie. W starym UI zachowana wsteczna kompatybilność. Status: Do doprecyzowania.

- **Logowanie SQL w nowych raportach:** W nowych raportach React logowanie SQL nie działa poprawnie. Należy zweryfikować użycie AmodDBCommand i funkcji DatabaseError. Status: Do weryfikacji.

---

## 2025-10-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-21 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność

- Błąd pobierania danych w nowych raportach dla użytkowników nie będących administratorem (komunikat "Inna liczba kolumn").
- Decyzja: Zwracać pustą wartość dla kolumn niedostępnych dla użytkownika (zgodnie ze starymi raportami).

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Funkcjonalność

- Obsługa wyświetlania pola typu Podpis w nowym module raportowym

---

## 2025-10-06 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Sprint review.md]
**Kategoria:** #Funkcjonalność #Design

- Umożliwiono dostosowanie szerokości kolumn w tabeli raportów (zapamiętywanie lokalne, domyślne szerokości)
- Kwestie do dopracowania: przejście do suwaka poziomego i obsługa pól długiego tekstu

---

## 2025-10-06 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Planowanie sprintu.md]
**Kategoria:** #Design

- Dyskusja na temat ujednolicenia sposobu wyświetlania opisów raportów na kafelkach dashboardów

---

## 2025-10-02 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-02 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-10-02%20Rada%20architektów.md)
**Kategoria:** #Architektura #Design

- Ustalenie zasady wizualizacji: Tree Map tylko dla małej liczby wartości (3-4), w przeciwnym razie wykres słupkowy
- Wytyczne dotyczące źródeł danych w raportach: rozdzielenie logiki dla spraw zamkniętych (CaseDefinition) i w toku (CaseHistory)
- Wymagana poprawa kontrastu w wizualizacjach raportowych i ujednolicenie tooltipów

---

## 2025-09-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-30 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-30%20Rada%20architektów.md)
**Kategoria:** #Problem #Funkcjonalność

- Weryfikacja funkcjonalności zawężenia raportu do pola typu Odnośnik
- Zgłoszenie problemów z działaniem tej funkcji w nowych raportach (mimo że teoretycznie istnieje)
- Zadanie weryfikacyjne dla Łukasza Botta

---

## 2025-09-23 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-23 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-23%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **Aliasy w źródłach zewnętrznych:** Dodanie możliwości nadawania aliasów kolumnom ze źródeł zewnętrznych w raportach (analogicznie do procesów).
- **Cel:** Spójność mechanizmów i możliwość używania przyjaznych nazw w raportach opartych o SQL/API.

---
## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🚀 Postęp

- **Stabilizacja:** czyszczenie wykrytych błędów w raportach.
- **Testy:** kontynuacja intensywnych testów (szczególnie Łukasz).

---
## 2025-09-18 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-18 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-18%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **Dostęp do reguł:** Zatwierdzono, że obecna kontrola dostępu do reguł wywoływanych z raportów jest wystarczająca (weryfikacja na poziomie wywołania). Usprawnienia wizualne (checkboxy) odroczone.

---

## 2025-09-11 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-11 Rada architektów - Multipart REST checkboxy edytor.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-11%20Rada%20architektów%20-%20Multipart%20REST%20checkboxy%20edytor.md)
**Kategoria:** #Architektura #Funkcjonalność
**Projekt:** [Klienci/WIM/Raporty-osadzone-checkboxy](../../Klienci/WIM/Raporty-osadzone-checkboxy/)

**WIM – raport osadzony z checkboxami do zapisania stanu** 🔍

Rozbudowa mechanizmu raportów osadzonych o możliwość edycji checkboxów w źródłach zewnętrznych i zapisania stanu jako części sprawy. Wymaga Proof of Concept przed pełną implementacją.

**Szczegóły:**
- **Główna implementacja dla klienta WIM** - zobacz [Klienci/WIM/Raporty-osadzone-checkboxy](../../Klienci/WIM/Raporty-osadzone-checkboxy/)
- Raport osadzony ze źródła zewnętrznego (pozycje zamówienia na podstawie numeru)
- Możliwość zaznaczania checkboxów przez użytkowników (które pozycje zgodne z fakturą)
- Zapisanie stanu checkboxów jako część sprawy (nie w CaseDefinition, w źródle dynamicznym)

**Zadania:**
- Damian Kamiński - Proof of Concept dla edytowalnych checkboxów
- Damian Kamiński - rozpisanie wymagań i akceptacja rozwiązania

**Punkty otwarte:**
- Jak zapisać stan checkboxów w źródle dynamicznym?
- Czy rozszerzyć na inne typy raportów?
- Czy przyszłościowo edycja źródeł dynamicznych z formularza?
- Jak obsłużyć zmiany danych w źródle zewnętrznym (nowe pozycje)?

---

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Funkcjonalność #Administracja

**Kopiowanie i zapisywanie raportów systemowych jako własne** ✅
- **Problem:** Administratorzy musieli prosić o zmiany w raportach systemowych
- **Rozwiązanie:**
  - Możliwość skopiowania raportu systemowego ("zapisz jako") i edycji jako własny
  - Wymaga stworzenia specjalnej grupy użytkowników
  - Możliwość definiowania filtrów wymaganych (bez wartości domyślnej)
- **Ograniczenia:** Źródła systemowe pozostają w trybie "tylko do odczytu" (nie można zmieniać zapytań SQL)

---

## 2025-08-28 - Rada architektów

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-28 Rada architektów|2025-08-28 Rada architektów]]

**Kategoria:** #Funkcjonalność #Problem

### Tabelki edytowalne – pivot/Excel w raportach

**Kontekst:**
Pojawiły się wymagania dotyczące tabel z możliwością edycji w raportach. Problem dotyczy zarówno PKF (Timesheet - rejestracja czasu pracy) jak i WIM (pozycje zamówienia z checkboxami).

**Zidentyfikowane Ryzyka:**
- Wydajność przy dużych tabelkach (300+ wierszy)
- Obciążenie formularza sprawy przy dużych tabelkach
- Ryzyko utraty kontekstu przy stronicowaniu
- Różne podejścia do podobnych problemów mogą prowadzić do niespójności

**Rozważane alternatywy:**
- **Tabelka AMODITowa na sprawie** - obciąża CaseDefinition, problemy wydajnościowe (odrzucona)
- **Raport tabelaryczny osadzony** - wymaga rozbudowy mechanizmu edycji (odroczona dla PKF)
- **Raport tabelaryczny z checkboxami (WIM)** - wymaga rozbudowy o edycję checkboxów (wybrana)
- **GetExcelData + Excel zewnętrzny** - rozwiązanie jednostkowe, nie systemowe (odroczona)
- **Dashboard z raportem + podglądem sprawy** - propozycja do rozważenia

**Decyzja:** 🔍 Do weryfikacji / ⏸️ Odroczone

**Dla WIM:**
- Użycie raportu tabelarycznego osadzonego ze źródła zewnętrznego
- Rozbudowa mechanizmu raportów o możliwość edycji checkboxów w źródłach zewnętrznych
- Zwiększenie limitu wierszy dla źródeł zewnętrznych (obecnie 100, może być potrzeba 300+)

**Dla PKF:**
- Temat wymaga wyceny i dalszej analizy
- Można powołać się na wcześniejszą analizę, gdzie przedstawiono obecne rozwiązanie (rejestracja przez sprawy)

**Szczegóły techniczne:**
- Raporty osadzone ze źródła zewnętrznego obecnie nie obsługują edycji checkboxów – wymaga rozbudowy
- Stronicowanie w raportach może powodować problemy z kontekstem
- Duże tabelki na formularzu sprawy obciążają zarówno przeglądarkę, jak i serwer

**Zadania:**
- **Damian Kaminski:** PA dla rozbudowy raportów o edycję checkboxów
- **Kamil Dubaniowski:** Weryfikacja wydajności ładowania 300 pozycji z procedury składowanej

**Punkty otwarte:**
- Czy zwiększyć limit wierszy w raportach ze źródeł zewnętrznych powyżej 100?
- Czy dashboard powinien mieć mechanizm podglądu sprawy obok raportu?

**Powiązane projekty:**
- [[../../Klienci/PKF/Rejestracja-czasu-pracy/CHANGELOG|PKF/Rejestracja-czasu-pracy]] - PKF Timesheet
- [[../../Klienci/WIM/Faktury-edytowalne-tabele/CHANGELOG|WIM/Faktury-edytowalne-tabele]] - WIM pozycje zamówienia

---

### Paleta kolorów w raportach

**Kontekst:**
Obecnie system ma 20 kolorów w pierwszej serii palety kolorów dla raportów. Damian zaproponował zmianę kolejności kolorów, aby pierwsze 10 było bardziej różniących się od siebie (podobnie jak w Tableau). Problem polega na tym, że niektóre kolory są zbyt podobne do siebie (np. cyjan, niebieski, indygo, morski), co utrudnia rozróżnienie na wykresach.

**Zidentyfikowane Ryzyka:**
- Nieczytelność wykresów przy podobnych kolorach
- Problemy z dostępnością dla osób z zaburzeniami widzenia kolorów
- Brak możliwości automatycznego przypisania unikalnych kolorów dla więcej niż 20 serii
- Ryzyko tworzenia nieczytelnych wykresów przez konsultantów (pokazywanie zbyt wielu serii)

**Rozważane alternatywy:**
- **Ograniczenie do 10 kolorów (jak Tableau)** - wymaga konsultacji z Michałem Maliszewskim (odroczona)
- **20 kolorów z lepszą kolejnością** - zmiana kolejności, aby pierwsze 10 było bardziej różniących się (propozycja)
- **20+ kolorów z automatycznym przypisaniem** - propozycja Damiana (do rozważenia)
- **Funkcjonalność "pozostałe"** - agregacja mało istotnych serii (poniżej progu, np. 5%) do jednej pozycji "pozostałe" (propozycja Janusza)
- **Sortowanie po wartościach w legendzie** - częściowo wdrożone (wymaga weryfikacji)

**Decyzja:** 🔍 Do weryfikacji

Damian porozmawia z Michałem Maliszewskim o dobrych praktykach dotyczących palet kolorów w raportach (wzorce z Tableau, Adobe, dostępność dla osób z zaburzeniami widzenia kolorów). Decyzja o ostatecznej palecie zostanie podjęta po konsultacji.

**Szczegóły techniczne:**
- Obecnie: 20 kolorów w pierwszej serii, możliwość ręcznego definiowania dodatkowych
- Propozycja Damiana: zmiana kolejności (czerwony, zielony, niebieski jako pierwsze 3), potem turkusowe
- Tableau: domyślnie 10 kolorów w pierwszej serii
- Uwaga: palety kolorów są naukowo dobierane pod kątem kontrastu i dostępności dla osób z zaburzeniami widzenia kolorów

**Zadania:**
- **Damian Kaminski:** Konsultacja z Michałem Maliszewskim dotycząca dobrych praktyk palet kolorów
- **Anna Skupinska:** Wstrzymanie prac nad kolorami do czasu podjęcia decyzji

**Punkty otwarte:**
- Czy ograniczyć paletę do 10 kolorów czy pozostawić 20?
- Jak obsłużyć przypadek, gdy użytkownik świadomie chce wyświetlić więcej niż 10-20 serii?
- Czy wprowadzić funkcjonalność agregacji mało istotnych serii do "pozostałe"?
- Jak zapewnić dostępność dla osób z zaburzeniami widzenia kolorów?
- Czy sortowanie w legendzie powinno być domyślnie po wartościach zamiast alfabetycznie?

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Funkcjonalność

**Kontekst:**
Seria usprawnień w module raportowym przepisanym na nową technologię, w tym gradienty kolorów, filtry wymagane i domyślne, oraz usprawnienia podpisywania z poziomu raportów.

### Moduł raportowy w nowej technologii – nowinki

**1. Gradienty kolorów:**
- W raportach typu pivot można ustawić kolory dla wartości (np. najwyższe zielone, najniższe czerwone)

**2. Filtry wymagane:**
- Użytkownik nie zobaczy raportu, dopóki nie wybierze wartości w filtrze (np. konkretnego procesu)
- Zapobiega to szumowi informacyjnemu (wyświetlaniu danych ze wszystkich procesów naraz)

**3. Filtry z wartością domyślną:**
- Twórca ustawia np. bieżący rok, ale użytkownik może to zmienić

**4. Filtr zakresu dat:**
- Możliwość ustawienia przedziału "od-do" w ramach jednego filtru (wcześniej trzeba było robić dwa osobne)

**5. Przycisk "Wyczyść filtr użytkownika":**
- Resetuje ustawienia filtrów

**6. Przycisk "Zastosuj":**
- Wprowadzony we wszystkich typach filtrów (bardziej intuicyjne dla użytkowników)

### Usprawnienie podpisywania z poziomu raportów

- Jeśli na formularzu jest kilka pól z dokumentami, a na raporcie wyświetlamy je w kolumnach, teraz możemy wskazać, która konkretnie kolumna ma podlegać podpisywaniu (żeby nie podpisywać wszystkich załączników ze sprawy naraz)

### Szczegóły techniczne

- Moduł raportowy przepisany na nową technologię
- Filtry wymagane i domyślne
- Filtr zakresu dat (od-do w jednym filtrze)

---

## 2025-08-25 - Sprint review

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-25 Sprint review|2025-08-25 Sprint review]]

**Kategoria:** #Funkcjonalność

**Edycja gradientów w raportach**

Implementacja edycji gradientów kolorów w raportach Treemap i Pivot. Użytkownicy mogą definiować własne skale kolorystyczne, resetować do domyślnej palety oraz dostosowywać kolory dla wartości dodatnich, ujemnych i środkowych.

**Kontekst:** Główna implementacja dla klienta WIM - zobacz szczegóły: [[../../Klienci/WIM/Raporty-edycja-gradientow/CHANGELOG|WIM/Raporty-edycja-gradientow]]

---

## 2025-08-12 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Kolory w raportach tabelarycznych z agregacją** ✅
- **Problem:** Mechanizm kolorowania patrzy tylko na wartości z danej strony, nie wszystkie wartości (nieprawidłowy gradient)
- ❌ Odrzucone: Kolorowanie tylko wartości z aktualnej strony - nieprawidłowe działanie gradientu
- ✅ **Zatwierdzone:**
  1. **Pobieranie wszystkich wartości** - mechanizm pobiera wszystkie wartości z raportu przed kolorowaniem
  2. **Gradient min/max** - kolorowanie oparte na maksymalnej/minimalnej wartości + wartość zero
  3. **Zakres:** Tylko raporty tabelaryczne bez agregacji (głównie pod WIM/Piotr)
  4. **Typy raportów:** Pivot, mapa (na razie)
- ⏸️ Przyszłościowo: Dzielenie zakresów na więcej elementów z różnymi kolorami (nie tylko gradient)
- **Punkty otwarte:** Mechanizm dzielenia zakresów? Rozszerzenie na inne typy raportów?
- **Zadania:** Anna Skupińska - finalizacja (oddane do testowania na AMODIT Local), Janusz Bossak - testowanie

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **Rozbudowa Pivota:** Dodanie edycji kolorów w gradientach (użytkownik wybiera kolor dla min/max w kolorowaniu warunkowym)
- **Heatmapa:** Dodanie nowego typu wykresu (bazując na bibliotece AmCharts)
- **Status:** ✅ Zatwierdzone - realizacja obu tematów

---