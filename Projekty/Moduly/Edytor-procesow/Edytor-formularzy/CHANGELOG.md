# Historia zmian - Edytor formularzy

## 2025-08-12 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Ustawianie szerokości kolumn w formularzu** ✅
- **Problem:** Częste zapytania klientów (Zbigniew Szymanowski, PKF) o szerokość kolumn w tabelach
- Obecnie kolumny mają domyślną szerokość - problematyczne dla krótkich wartości (KG, SZT, ilości ≤999)
- ❌ Odrzucone: Pełna kontrola CSS - ryzyko bezpieczeństwa (wstrzyknięcie JavaScript)
- ✅ **Zatwierdzone:**
  1. **Szerokość kolumny** - możliwość wpisania szerokości w pikselach (np. 50px)
  2. **Zawijanie tekstu** - opcja czy tekst ma się zawijać w kolumnie
  3. **Ograniczona kontrola CSS** - tylko wybrane właściwości (width, zawijanie)
  4. **Bezpieczeństwo** - backend interpretuje tylko oczekiwane właściwości, ignoruje resztę
- **Oddzielne ustawienia:** dla wyświetlania i wydruku (jak w starym systemie)
- **Tabelka w tabelce:** nie określa się szerokości (jest w nowej linii)
- **Punkty otwarte:** Czy rozszerzyć o więcej właściwości CSS? Jak wygląda interfejs?
- **Zadania:** Piotr Buczkowski - implementacja, Anna Skupińska - testy bezpieczeństwa

---

## 2025-12-02 | 🎯 Decyzja | Spotkanie projektowe - Design
**Źródło:** [Notatki/Spotkania projektowe/2025-12-02 Spotkanie projektowe - Design.md]

**Reorganizacja prawego panelu edycji pola:**
- Przeniesienie akcji do nagłówka: Historia pola, Reguły pola (tabele), Usuń pole (ikona kosza, czerwony)
- Zmiana typu pola: dostępna TYLKO z listy pól (ochrona przed destrukcyjną operacją), NIE z prawego panelu
- Typ pola w "Dane podstawowe": tylko do odczytu

**Konsolidacja sekcji właściwości:**
- Opcje widoczności ("Widoczne na listach", "Dostępne w raportach", "Pole systemowe") przeniesione do zakładki "Właściwości pola"
- Akcja "Zarządzaj widocznością i uprawnieniami": ikona oczka w nagłówku (okno z ustawieniami ról, edycji, wymagalności)
- Zmiana nazwy zakładki: "Ustawienia" → "Właściwości pola"

**Wartość domyślna i Podpowiedź:**
- Pozostają w sekcji "Dane podstawowe" (brak lepszego miejsca)
- Uspójnienie edycji "Wartość domyślna" z listy pól (Filip)
- Dla pól bez obsługi wartości domyślnej: kursor "zakazany" + tooltip

**Edycja pól tabeli:**
- Przycisk "Edytuj pola tabeli" przeniesiony na górę prawego panelu (ponad wszystkie sekcje)
- Pozostaje jako pełny przycisk z tekstem (nie ikona) - intuicyjność

**Edycja GUID pola:**
- Ikona ołówka obok GUID (obok ikony kopiowania)
- Okno modalne z ostrzeżeniem i potwierdzeniem
- Zabezpieczenie: uzależnione od ustawienia systemowego (domyślnie wyłączone)

**Kolejne kroki:**
- Wyróżnienie prawego panelu (layout)
- Przegląd nazewnictwa i kolejności właściwości dla każdego typu pola
- Dodanie instrukcji/tooltipów do właściwości

**Punkty otwarte:**
- Kamil zgłosi Filipowi: jeśli zmiana typu będzie w prawym panelu, usunąć z listy pól
- Filip: uspójnienie edycji "Wartość domyślna" z listy pól
- Filip: kursor "zakazany" + tooltip dla pól bez obsługi wartości domyślnej
- Przemek czeka na backend: okienko pytające o nazwę systemową pola po dodaniu
- Do przemyślenia: tryb "nieopublikowane/opublikowane" dla definicji procesu (buffer zmian)

---
