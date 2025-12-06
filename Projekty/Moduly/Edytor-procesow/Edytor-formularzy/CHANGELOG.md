# CHANGELOG - Edytor formularzy

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
