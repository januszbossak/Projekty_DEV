> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-08
# Spotkanie projektowe – 2025-11-19 – Problem odświeżania raportu

**Data:** 2025-11-19
**Uczestnicy:** Kamil Dubaniowski, Damian Kamiński, Łukasz Bott, Janusz Bossak

**Powiązane projekty:**
- `Moduly/Modul-raportowy` – funkcjonalność odświeżania raportów po akcjach na sprawie
- `cross-cutting/Interfejs-sprawy`

---

## 1. Problem odświeżania raportów po wykonaniu akcji na sprawie

**Projekt:** `moduly/Modul-raportowy`
**Komponent:** Raporty tabelaryczne, dashboardy

### Cel i problem

Użytkownicy zgłaszają problem z odświeżaniem raportów po wykonaniu akcji na sprawie. Po wejściu na sprawę z raportu, wykonaniu akcji (np. anulowanie, zmiana etapu, wypełnienie pola) i powrocie do raportu, dane nie aktualizują się automatycznie – sprawa pozostaje w raporcie mimo że nie powinna się tam już znajdować, lub wyświetlane wartości nie są aktualne.

**Pierwotny zgłoszony problem (Kamil Dubaniowski):**
- Wchodzę na wycenę, anuluję ją, wracam do raportu
- Sprawa nadal siedzi w raporcie, mimo że według filtrów już być nie powinna
- Muszę ręcznie odświeżyć całą stronę
- Wcześniej działało automatyczne odświeżenie po powrocie

**Problem priorytetowy:**
Przycisk "Odśwież" w dashboardzie nie odświeża stanu raportów.

### Rozważane alternatywy

#### Test 1: Dashboard vs raport standalone

**Hipoteza:** Problem dotyczy tylko dashboardów

**Test:**
- Dashboard: Przycisk "Odśwież" NIE działa
- Raport standalone (poza dashboardem): Przycisk "Odśwież" DZIAŁA

**Wnioski:**
- W raportach standalone przycisk "Odśwież" skutecznie odświeża dane
- Problem jest specyficzny dla dashboardów

**Istniejące zgłoszenie:**
Znaleziono zgłoszenie D123 (wersja 122): "Kliknięcie przycisku Odśwież w dashboardzie powoduje odświeżenie wartości raportów"
- Status: Done
- Ale faktycznie nadal nie działa

#### Test 2: Tryb otwierania sprawy (pop-up vs zakładka)

**Konfiguracje:**
1. Sprawa otwiera się w nowej zakładce
2. Sprawa otwiera się w pop-upie

**Wyniki:**
- W obu przypadkach przycisk "Odśwież" działa (w raporcie standalone)
- W obu przypadkach po zamknięciu sprawy dane się nie odświeżają automatycznie

#### Test 3: Interesujące zachowanie – kliknięcie w filtry

**Obserwacja:**
- Samo kliknięcie w kafelek filtrów (bez wybierania wartości) powoduje odświeżenie całego ekranu
- Po odświeżeniu dane są już aktualne
- To niezamierzone zachowanie, ale skuteczne

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

**Przypadki użycia do rozważenia:**

#### **Przypadek 1: Zmiana danych w sprawie bez zmiany kwalifikacji do filtru**

**Scenariusz:**
- Raport wyświetla sprawy
- Wchodzę na sprawę na pozycji 5
- Zmieniam wartość pola (np. wypełniam nazwisko)
- Po tym polu NIE jest sortowanie, NIE ma filtra
- Wraca do raportu

**Oczekiwane zachowanie:**
- Pozostaję na pozycji 5
- Dane w tym rekordzie się odświeżają (widzę wypełnione nazwisko)
- Raport NIE jest przebudowywany (NIE stosuje sortowania, NIE stosuje filtrów)
- Jestem w tym samym miejscu co byłem (ta sama strona paginacji)

**Uzasadnienie:**
Użytkownik może przetwarzać po kolei wiele spraw (np. wypełniać puste pola). Chce być w tym samym miejscu raportu, aby przejść do następnej sprawy bez gubienia się.

#### **Przypadek 2: Zmiana danych powodująca wykluczenie z filtru**

**Scenariusz:**
- Raport wyświetla sprawy z filtrem "nazwisko jest puste"
- Wchodzę na sprawę
- Wypełniam nazwisko
- Sprawa już nie spełnia warunku filtru

**Opcja A (proponowana przez Janusza):**
- Dane w rekordzie się odświeżają (widzę wypełnione nazwisko)
- Rekord NIE znika z raportu
- Rekord zniknie dopiero po RĘCZNYM kliknięciu "Odśwież"

**Uzasadnienie:**
Użytkownik może przetwarzać po kolei 10 spraw. Chce widzieć które już przetworzył (wypełnione pola), ale nie chce żeby mu "znikały spod ręki". Po przetworzeniu kilku spraw klika "Odśwież" i przetworzone sprawy znikają.

**Opcja B:**
- Rekord znika natychmiast po zamknięciu sprawy (automatyczne odświeżenie z zastosowaniem filtrów)

**Argument za B:** Użytkownik ma filtr "nazwisko puste", więc chce widzieć TYLKO puste

#### **Przypadek 3: Zmiana danych w kolumnie z aktywnym sortowaniem**

**Scenariusz:**
- Raport posortowany po nazwisku rosnąco
- Wchodzę na sprawę na pozycji 5 (nazwisko puste)
- Wypełniam nazwisko "Nowak"
- Teoretycznie sprawa powinna przeskoczyć w inne miejsce (sortowanie alfabetyczne)

**Propozycja (Janusz):**
- Dane w rekordzie się odświeżają
- Sortowanie NIE jest stosowane
- Rekord pozostaje na pozycji 5
- Sortowanie zostanie zastosowane dopiero po ręcznym kliknięciu "Odśwież"

**Uzasadnienie:** Jak w przypadku 2 – użytkownik chce przetwarzać po kolei sprawy i widzieć progres

#### **Przypadek 4: Wykonanie akcji z przyciskiem ustawionym "Wróć do listy spraw"**

**Scenariusz:**
- Raport
- Wchodzę na sprawę
- Klikam akcję (np. "Indeksuję")
- Akcja ma ustawienie "Po wykonaniu: Wróć do listy spraw"
- Sprawa się zamyka automatycznie

**Pytanie:** Czy w tym przypadku zachowanie powinno być inne niż przy zwykłym zamknięciu?

**Status:** 🔍 Nierozstrzygnięte

#### **Przypadek 5: Zamknięcie pop-upu vs strzałka wstecz**

**Pytanie:** Czy zamknięcie pop-upu przez "X" powinno się zachowywać inaczej niż strzałka wstecz z zakładki?

**Status:** 🔍 Nierozstrzygnięte

### Ograniczenia / Poza zakresem

**Różne typy raportów mogą wymagać różnych zachowań:**
- Tabelaryczne: opisane powyżej
- Kanban: zmiana statusu → natychmiastowe przesunięcie karty?
- Gantt: zmiana dat → natychmiastowa aktualizacja wykresu?
- Kalendarz: analogicznie

**Uwaga:** Niekonsekwentne zachowanie między typami raportów może być mylące dla użytkowników.

### Punkty otwarte

1. **Czy przycisk "Odśwież" w dashboardzie faktycznie działa w wersji 122?**
   - Zgłoszenie D123 oznaczone jako Done
   - Faktycznie nie działa
   - Wymaga weryfikacji z Michałem

2. **Jaki powinien być domyślny tryb odświeżania?**
   - Automatyczne odświeżenie po zamknięciu sprawy?
   - Ręczne odświeżenie przyciskiem "Odśwież"?
   - Automatyczne odświeżenie tylko rekordu (bez przebudowy raportu)?

3. **Jak powinny się zachowywać różne typy raportów?**
   - Czy tabelaryczne, Kanban, Gantt powinny się zachowywać jednakowo?
   - Czy użytkownik końcowy zrozumie różnice?

4. **Jak implementować to technicznie?**
   - SignalR do odświeżania pojedynczego rekordu?
   - Odświeżenie z pamięci vs ponowne zapytanie do backendu?
   - Jak zachować stan paginacji?
   - Jak obsłużyć sortowanie i filtry?

5. **Czy warto wdrażać częściowo (tylko przycisk "Odśwież")?**
   - Argument za: szybkie naprawienie krytycznego błędu
   - Argument przeciw: lepiej zrobić całościowo, aby uniknąć przyszłych zmian zachowania

### Ustalenia

1. **Priorytet hotfix:** Naprawa przycisku "Odśwież" w dashboardzie
   - To jest minimum – przycisk "Odśwież" ZAWSZE powinien odświeżać

2. **Odrębne zgłoszenia:**
   - Przycisk "Odśwież" (priorytet 1)
   - Automatyczne odświeżanie po zamknięciu sprawy (do projektowania)

3. **Konsultacja z Przemkiem:**
   - Przekazać wszystkie przypadki użycia
   - Poprosić o propozycję implementacji
   - Sprawdzić złożoność techniczną

4. **Podejście ewolucyjne:**
   - Lepiej zaimplementować konsekwentnie docelowe rozwiązanie
   - Niż wprowadzać szybkie zmiany, które będą zmieniane za miesiąc
   - Użytkownicy przyzwyczajają się do trybu pracy

5. **Spisanie przypadków użycia:**
   - Janusz spisze wszystkie rozważane przypadki
   - Każdy przypadek jako osobny user story
   - Opis oczekiwanego zachowania dla każdego

---

## Notatki techniczne

**Zgłoszenie D123 (wersja 122):**
- Tytuł: "Odświeżenie raportu tabelarycznego w dashboardzie nie wyświetla zmienionej wartości pola"
- Kryterium akceptacji: "Kliknięcie przycisku Odśwież w dashboardzie powoduje również odświeżenie zawartości raportu w aktywnej zakładce"
- Status: Done
- Problem: Faktycznie nadal nie działa w dashboardach

**Obserwacje techniczne:**
- Przełączanie stron paginacji coś odświeża (pobiera z pamięci?)
- Kliknięcie w filtry również wywołuje odświeżenie
- W raporcie standalone "Odśwież" działa poprawnie
- Problem jest specyficzny dla dashboardów

**Złożoność implementacji:**
- Odświeżenie pojedynczego rekordu wymaga:
  - Pobrania danych ze sprawy
  - Aktualizacji pamięci cache raportu
  - NIE stosowania filtrów
  - NIE stosowania sortowania
  - Zachowania stanu paginacji
- To nie jest trywialne rozwiązanie

---

## Kontekst produktowy

Problem odświeżania raportów jest krytyczny dla użyteczności systemu. Użytkownicy często pracują w trybie:
1. Przeglądaj raport
2. Wejdź na sprawę
3. Wykonaj akcję
4. Wróć do raportu
5. Przejdź do następnej sprawy

Obecne zachowanie psuje ten przepływ pracy – użytkownik:
- Nie widzi aktualnych danych
- Musi ręcznie odświeżać stronę
- Gubi się w raporcie po odświeżeniu
- Nie wie czy akcja się wykonała

To prowadzi do frustracji i błędów w pracy.