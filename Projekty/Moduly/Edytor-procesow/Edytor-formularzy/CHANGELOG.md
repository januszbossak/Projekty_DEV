# CHANGELOG - Edytor formularzy


## 2025-12-02 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-02 Spotkanie projektowe - Design.md]
**Kategoria:** #Design

- Reorganizacja prawego panelu - przeniesienie akcji (Historia, Reguły, Usuń) do górnej belki
- Zmiana typu pola dostępna tylko z listy pół (zabezpieczenie przed destrukcyjną operacją)
- Konsolidacja widoczności - opcje przeniesione do zakładki "Właściwości"
- Zmiana nazwy zakładki z "Ustawienia" na "Właściwości pola"
- Przycisk "Edytuj pola tabeli" przeniesiony ponad sekcje (pełny przycisk z tekstem)
- Edycja GUID pola - ikona ołówka z oknem modalnym i ostrzeżeniem
- Plan pracy Design - przegląd nazewnictwa, kolejności i tooltipów właściwości pól

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Cele sprintu - Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Design #Zadanie

- Ulepszony prawy panel w edytorze graficznym i liście pól zgodnie z projektem.
- Ustalenie gotowego projektu prawego panelu.
- Realizacja zmian zgodnie z projektem.
- Uporządkowanie kolejności ustawień (najczęściej używane na górze).
- Zmiana sposobu edycji parametrów GUID w polu (okno zamiast osadzenia).
- Zlokalizowanie akcji związanych z regułami tabeli w prawym panelu.

## 2025-11-30 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-30 Spotkanie projektowe - Edytor procesow.md](../../../../../Notatki/Gotowe-notatki-archiwum/2025-11-30%20Spotkanie%20projektowe%20-%20Edytor%20procesow.md)
**Kategoria:** #Funkcjonalność #UI/UX #Problem

- Panel prawy: zmiana kolejności i układu ustawień (zadanie P. Rogaś).
- Walidacja: dodanie komunikatu o przekroczeniu limitu pól (zamiast cichego błędu).
- Słowniki: usprawniony interfejs edycji (bezpośrednia edycja, akceptacja ryzyka).
- Brak wyszukiwania w oknach wyboru słowników (zgłoszona potrzeba).
- Masowe działania na liście pól: potrzeba przenoszenia (drag & drop) w widoku listy.



## 2025-11-27 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-11-27 Planowanie sprintu.md]
**Kategoria:** #Rozwój #Funkcjonalność #Ukończenie

- Cel: Dokończenie prac nad graficznym edytorem formularza oraz kontynuacja rozwoju listy pól.
- Status: Zaawansowanie prac w edytorze i liście pól.
- Zakres prac: Finalizacja edytora graficznego formularza, planowane zamknięcie tematu w bieżącym sprincie.
- Decyzje: Cel - osiągnięcie stanu funkcjonalnego, nie wymagającego dalszego rozwoju, tylko ewentualnych usprawnień.

## 2025-11-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-27 Notatka projektowa - Edytor procesów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-27%20Notatka%20projektowa%20-%20Edytor%20procesów.md)
**Kategoria:** #Funkcjonalność #Design #UI/UX

- **Edytor Graficzny:** Dodawanie sekcji "pomiędzy" istniejącymi sekcjami (przycisk na hover).
- **Design:** Ujednolicenie zaokrągleń rogów sekcji (5px) i układu prawego panelu.
- **UI:** Przycisk powiększ/zmniejsz nie zmienia pozycji przy otwarciu prawego panelu.
- **Search:** Wyszukiwanie pól po atrybutach technicznych (ID, nazwa kolumny, GUID).
- **Lista Pól:** Zmiana sposobu wyboru liczby kolumn (spójność z graficznym).
- **Lista Pól:** Powrót do nawigacji "w głąb" tabeli (strzałka) zamiast zagnieżdżania.
- **Lista Pól:** Ramka na hover dla pól klikalnych.
- **Nawigacja:** Zmiana lewego panelu na strukturę drzewa (TreeSelect).
- **Dyskusja:** Problem rozgraniczenia prezentacji i nawigacji w środkowym panelu.

## 2025-11-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-27 Notatka projektowa - Edytor procesow.md]
**Kategoria:** #Funkcjonalność #Design #Decyzja

- Poprawa użyteczności i czytelności panelu ustawień pól w Edytorze Formularza.
- Planowane spisywanie zmian w prawym panelu ustawień pola (układ, kolejność).
- Poprawa wizualizacji "Dodaj sekcję" / "Dodaj wiersz" (kolorystyka).
- Ujednolicenie zaokrągleń rogów (`ósemki` na `piątki`).
- Wyszukiwanie pól po GUID, ID, nazwie kolumny w bazie danych.
- Zmiana nawigacji dla tabel w Edytorze Formularza (tabela jako pole, strzałka w prawo).
- Uproszczenie i ujednolicenie nawigacji w kontekście zagnieżdżonych tabel i podformularzy.
- Zamykanie prawego panelu po zmianie kontekstu (np. wejściu do tabeli).
- Zmieniono nawigację lewego panelu (struktura drzewa dla relacji rodzic-dziecko).
- Koncepcja "wizualizacja kontra nawigacja" jako podstawa projektowania interfejsu edytora.

---

## 2025-11-25 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-25 Notatka projektowa - Projekt listy pól.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-25%20Notatka%20projektowa%20-%20Projekt%20listy%20pól.md)
**Kategoria:** #Design #Funkcjonalność

- **Lista Pól:** Nowa ikona "Plus" (+) zawsze dodaje element kontekstowo (pod tabelą przy zwiniętej).
- **Tabele:** Ikona rozwijania (szewron) przeniesiona na prawą stronę nazwy pola, by odróżnić od ikony typu pola.
- **Akcje:** Ograniczenie ikon przy polu do dwóch: "Zębatka" (Prawy Panel) i "Menu" (Trzy kropki).
- **Menu pola:** Zawiera rzadsze akcje: Widoczność/Uprawnienia, Historię pola, Reguły.
- **Prawy Panel:** Nowy nagłówek z nazwą pola, usunięcie sekcji "Zarządzaj polem", przeniesienie kluczowych akcji do paska narzędzi.
- **Pole Systemowe:** Wymaga wyjaśnienia działania (tooltip) i ewentualnej zmiany nazwy (niejasne działanie).

---

## 2025-11-21 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-21 Planowanie sprintu.md]
**Kategoria:** #Design #Bug #Funkcjonalność #Zadanie #Problem #Architektura

- Porządkowanie błędów wizualnych i funkcjonalnych w edytorze formularzy i listy pól.
- Mariusz będzie pracował nad uporządkowaniem pola typu Tabela.
- Potrzeba widoku "Gdzie to pole jest używane?" (lista reguł) w prawym panelu dla edytora pól.
- Naprawa niedostępnych reguł tabeli z nowej listy pól.
- Problem z dodawaniem nowej sekcji z poziomu listy pól (ograniczenia tabeli Ant Design).
- Postulat zmiany backendu: sekcje powinny mieć swoją reprezentację w bazie danych (do analizy).

---

## 2025-11-20 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-20 Spotkanie projektowe - Edytor procesów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-20%20Spotkanie%20projektowe%20-%20Edytor%20procesów.md)
**Kategoria:** #UI/UX #Design #Decyzja

- **Prawy panel ustawień:** Decyzja o przeniesieniu jako osobny boks poniżej górnej belki (aby belka była statyczna i nie przesuwała się).
- **Toolbox:** Propozycja wizualnego wydzielenia lewego toolboxa i prawego panelu jako osobne kontenery z ramką, zaokrągleniami (5px) i ewentualnym tłem, aby odróżnić je od białego formularza.
- **MVP:** Edytor formularza bliski ukończenia (MVP), planowane zamknięcie prac w ciągu 1-2 sprintów.

---

## 2025-11-13 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-13 Notatka projektowa - Edytor procesów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-13%20Notatka%20projektowa%20-%20Edytor%20procesów.md)
**Kategoria:** #Funkcjonalność #Problem

- Przywrócenie parzystości funkcjonalnej ze starym widokiem listy pól (np. ustawienia kolumn w sekcji).
- Ustawienia pól (typ, wartości) dostępne w prawym panelu otwieranym kołem zębatym.
- Dodano przyciski "Zwiń/Rozwiń wszystko" oraz ustawienia ilości kolumn przy nagłówkach sekcji.
- Problem UX: Dodawanie nowej sekcji jest nieintuicyjne (wymaga zjechania na dół formularza).
- Dedykowane ustawienia typów pól przeniesione do prawego panelu.

---

## 2025-11-06 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-06 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Decyzja

- Rozszerzenie pola "Odnośnik do procesu" o obsługę pól słownikowych i listy wyboru
- Odroczona obsługa pól numerycznych, dat i użytkownika (zbyt skomplikowane - wymagają zakresów)
- Wymagana obsługa dwóch wariantów: z Lucene i bez Lucene dla słowników
- Realizacja zatwierdzona, termin: po pierwszym kwartale 2026 roku

---

## 2025-11-06 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-06 Notatka projektowa - Edytor procesów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-06%20Notatka%20projektowa%20-%20Edytor%20procesów.md)
**Kategoria:** #UX/UI

- Prace nad wizualną organizacją lewego panelu narzędzi (Toolbox): rozważane kolorowe ikony typów pól, zmiana tła panelu lub oddzielenie go ramką.
- Zaimplementowano dodawanie nowych pól do konkretnych sekcji (przycisk "Dodaj pole" przy sekcji).
- Zaplanowano dodanie opcji tworzenia nowych sekcji w bieżącym sprincie.
- Wdrażanie opcji dostępnych na hover na liście pól: otwieranie prawego panelu, usuwanie, edycja, historia zmian.
- Zidentyfikowano brak opcji "Zwiń/Rozwiń wszystko" dla sekcji (do dodania).
- Dodano sekcję "Informacje techniczne" w prawym panelu pola (Nazwa kolumny DB, ID, edytowalny GUID) na potrzeby serwisu.
- Zgłoszono błędy: nadmiarowy scroll w liście pól, brakujące ustawienia specyficzne dla typów pól (np. miejsca po przecinku), niejasne wyświetlanie nazwy typu pola w prawym panelu.
- Rozważana koncepcja edycji formularza w trybie tekstowym lub integracji z Copilotem AI dla przyspieszenia pracy.

---

## 2025-10-31 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-31 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Design #Zadanie #UX

- Główny cel sprintu to poprawa UX edytora formularza, aby konsultanci z niego korzystali.
- Wśród usprawnień UX: szukanie po typie, zapamiętywanie ostatniej zakładki, zmiana ścieżki dodawania nowego pola.
- Obsługa błędów przy edycji pól (np. zdublowanie nazwy) przeniesiona do wersji czerwcowej.
- Rozważane akcje masowe (usuwanie, przenoszenie) i uwagi do drag and drop.
- Uzupełnienie braków w liście pól (szybki odnośnik do słownika, ustawienia pola).

---

## 2025-11-03 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-03 Sprint review-codex.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-03%20Sprint%20review-codex.md)
**Kategoria:** #Funkcjonalność #UI

- Drag & drop sekcji w edytorze graficznym (zwijanie sekcji na czas przenoszenia, rozwijanie po upuszczeniu).
- Kontynuacja wyrównywania funkcji vs stary edytor: przenoszenie pól między sekcjami i szybki odnośnik do słownika zaplanowane; wyszukiwanie po typie do zrobienia.

## 2025-10-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-27 Spotkanie projektowe - Przegląd projektów.md]
**Kategoria:** #Bug #Funkcjonalność

- Problem z czyszczeniem pola daty/czasu w edytorze formularza (błąd przy zapisie).
- Decyzja: Minimum funkcjonalności - trzeba móc wyczyścić pole daty.

---

## 2025-10-23 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-23 Notatka projektowa - Edytor procesów.md]
**Kategoria:** #Funkcjonalność #Decyzja

- Finalizacja prac nad nowym edytorem formularza (React).
- Dodano funkcję przesuwania sekcji (zarządzanie kolejnością).
- Decyzja: Nie dodawanie już nowych funkcji, tylko stabilizacja obecnego rozwiązania na wersję grudniową.

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Funkcjonalność #Design

- Ujednolicenie ikon pól (rozmiar, kolor, styl outline) z formularzem sprawy
- Ograniczenie wizualne długości pola do 500px (jak na sprawie)
- Obsługa pól zablokowanych (ikona kłódki)
- Ulepszenia pola statyczny tekst (edycja, podgląd treści)
- Nowa lista pól z edycją tłumaczeń inline i wizualnym rozróżnieniem dziedziczenia
- Tabele rozklaszowane w widoku listy pól (pola z tabel widoczne na głównej liście)

---

## 2025-10-16 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-16 Notatka projektowa - Edytor procesów.md]
**Kategoria:** #Design #Bug #Funkcjonalność

- Odwzorowanie wyglądu formularza w edytorze ("What You See Is What You Get")
- Zaakceptowano obecny wygląd mimo mniejszych odstępów pionowych
- Zidentyfikowano błąd: brak wizualnego wskaźnika wstawiania dla Drag & Drop

---

## 2025-10-09 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-09 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Bezpieczeństwo #Decyzja

- Implementacja mechanizmu utrudniającego dodawanie pól bezpośrednio na środowisku produkcyjnym z poziomu edytora formularzy

---

## 2025-10-07 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-07 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Bug #Decyzja

- Decyzja o zachowaniu obecnego rozwiązania dla zmiany typu pola (wymaga potwierdzenia ryzyka)
- Problem z walidacją pola z maską (Telefon): błąd wyświetlania, mylące czerwone pole
- Decyzja: Wprowadzenie opcji "Wymuś zgodność z maską" dla pól tekstowych z maską, która zablokuje zapis

---

## 2025-10-06 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Sprint review.md]
**Kategoria:** #Funkcjonalność #Bug #Design

- Dodano wyszukiwarkę w edytorze formularza (po nazwach wyświetlanych i systemowych)
- Wprowadzono bezpieczną edycję słownika i zmianę typu pola z potwierdzeniem ryzyka
- Zaimplementowano dziedziczone placeholdery i labele dla pól bez Labeli
- Zidentyfikowano błędy: za małe okienko edytora, brak obsługi pól zablokowanych, zawsze wymagane potwierdzenie przy zmianie typu pola

---

## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🚀 Postęp

- **Edytor formularza graficznego:** realizacja korekt i usprawnień.
- **Wersja czerwcowa:** stabilizacja przed wydaniem (planowane wydanie w bieżącym tygodniu).

---

## 2025-09-18 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-18 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-18%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność #Design

- **Pole static jako Callout:** Pole static będzie mogło być wyświetlane w jednej kolumnie (opcja konfigurowalna). Docelowo również właściwość "display jako callout" (info, danger, warning) w ustawieniach pola static.

---

## 2025-09-16 | Rada architektów

**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-16 Rada architektów - Przegląd projektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-16%20Rada%20architektów%20-%20Przegląd%20projektów.md)
**Kategoria:** #Funkcjonalność #Decyzja

**Pola puste i placeholdery w edytorze**

- **Problem:** Backend nie zwraca pól pustych, problemy z uprawnieniami do placeholderów, znikające kolumny przy przejściu lista-edytor.
- **Decyzja:** ✅ Zatwierdzone (MVP) - pozostawienie obecnej logiki pól pustych bez zmian.
- **Uzasadnienie:** Zmiana logiki jest zbyt ryzykowna dla istniejących formularzy (setki wdrożeń). Nowa koncepcja (wiersze/grupy) wymaga głębszej analizy.
- **Zadania:** Poprawa zapamiętywania kolumn układu (3 kolumny -> 2 kolumny).

---

## 2025-09-11 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-11 Rada architektów - Multipart REST checkboxy edytor.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-11%20Rada%20architektów%20-%20Multipart%20REST%20checkboxy%20edytor.md)
**Kategoria:** #Design #Funkcjonalność #Decyzja

**Edytor formularzy – przełączanie między widokami** ✅

Przeniesienie wyboru formularza głównego na górny pasek (obok Edytor Graficzny/Lista). Odzyskanie przestrzeni roboczej i poprawa intuicyjności interfejsu.

**Szczegóły:**
- Przeniesienie wyboru formularza głównego na górny pasek (obok Edytor Graficzny/Lista)
- Nagłówek: "Edytujesz formularz główny [nazwa]"
- Przycisk: "Zobacz dla nazwy systemowe" (obok nagłówka)
- Usunięcie strzałki wstecz (niepotrzebna po przeniesieniu)
- Usunięcie dolnego paska z wyborem (odzyskanie przestrzeni)
- Długie nazwy: skracanie z kropkami
- Przełączanie Edytor Graficzny/Lista: zachowanie kontekstu (tabele)

**Kontekst:**
- Obecny wybór w środku ekranu zajmuje miejsce, nieintuicyjny
- Matryca Uprawnień w wersji wrześniowej (obecnie tylko Edytor Graficzny i Lista w czerwcowej)
- Przyszłościowo: sekcja "Reguły" po prawej stronie (dla pól i tabel)
- Full screen dla edytora graficznego (jak dashboard) - odroczone

**Zadania:**
- Przemysław Sołdacki - przeniesienie wyboru na górny pasek (wersja czerwcowa)
- Przemysław Sołdacki - nagłówek i przycisk "Zobacz dla nazwy systemowe" (wersja czerwcowa)
- Przemysław Sołdacki - usunięcie strzałki wstecz i dolnego paska (wersja czerwcowa)
- Przemysław Sołdacki - obsługa długich nazw (wersja czerwcowa)

**Punkty otwarte:**
- Przyszłościowo full screen dla edytora graficznego?
- Czy reguły tabeli w sekcji "Reguły" po prawej?
- Jak obsłużyć przełączanie podczas edycji tabeli (zachowanie kontekstu)?

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Design #Architektura

**Cel:**
Przebudowa całego obszaru definiowania procesu na "ramę Reactową", rozpoczęcie od Edytora Formularza jako pierwszego elementu w tej wersji.

### Zupełnie nowy projekt oparty na feedbacku klientów

**Układ:**
- Po lewej stronie lista typów pól (przenoszenie na formularz)
- Po kliknięciu na pole na formularzu, po prawej stronie w panelu pojawiają się szczegóły i ustawienia tego pola

### Kompatybilność

- Pełna kompatybilność – żadna funkcjonalność nie została zgubiona
- Użytkownik po wejściu trafi do nowego edytora
- Zostawiamy jednak przełącznik na "starą listę pól" dla bezpieczeństwa/wygody, jeśli ktoś czegoś nie znajdzie
- Docelowo (za ok. pół roku) stary edytor zostanie wyłączony

### Plany na przyszłość

- W kolejnych wydaniach: nowy edytor diagramu i reguł

### Szczegóły techniczne

- Przebudowa na React
- Przełącznik między nowym a starym edytorem

### Ograniczenia

- Stary edytor zostanie wyłączony za około pół roku
- Nowy edytor diagramu i reguł jeszcze nie zaimplementowany (planowany w kolejnych wydaniach)

---

## 2025-08-12 | Rada architektów

**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)

**Kategoria:** #Funkcjonalność

**Zarządzanie szerokością kolumn w tabeli na formularzu**

- **Problem:** Brak możliwości zarządzania szerokością kolumn per kolumna dla pól w trybie edycji
- **Decyzja:** ✅ Zatwierdzone - implementacja zarządzania szerokością kolumn
- **Szczegóły:** Możliwość ustawienia szerokości kolumn w tabeli na formularzu dla pól w trybie edycji (nie tylko w trybie podglądu)
