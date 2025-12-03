# CHANGELOG - Edytor formularzy

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
