# CHANGELOG - Tłumaczenia i aliasy

## 2025-09-09 - Rada architektów

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-09-09 Rada architektów|2025-09-09 Rada architektów]]

**Kategoria:** #Funkcjonalność #Problem

**Kontekst:**
W raportach występuje problem z tłumaczeniami etykiet kolumn i agregacji. Kolumny pochodzące ze źródeł zewnętrznych (np. "Report created by", "Report tip", "Report category") mają etykiety po angielsku, mimo że interfejs jest po polsku. Dodatkowo agregacje typu "count", "sum", "min", "max" są wyświetlane po angielsku zamiast po polsku.

### Problem

- Kolumny ze źródeł zewnętrznych są po angielsku (mieszanka języków w raportach)
- Agregacje są po angielsku (count, sum, min, max)
- Brak możliwości dostosowania etykiet do kontekstu biznesowego raportu (np. zamiast "sum Report id" → "Ilość raportów")
- Niespójność między procesami (mają tłumaczenia) a raportami (nie mają)

### Zidentyfikowane Ryzyka

- Nieczytelność raportów dla użytkowników polskojęzycznych (mieszanka języków)
- Brak możliwości dostosowania etykiet do kontekstu biznesowego raportu
- Problemy z wielojęzycznością – każdy raport wymagałby osobnego tłumaczenia wszystkich etykiet

### Decyzja

**Status:** 🔍 Do weryfikacji / ⏸️ Częściowo odroczone

**MVP (Minimum Viable Product):**

1. **Wyświetlanie istniejących tłumaczeń:**
   - Naprawa wyświetlania tłumaczeń agregacji (count → suma, sum → suma, min → min, max → max) w trybie odczytu
   - Tłumaczenia są już zdefiniowane, tylko nie są wyświetlane prawidłowo

2. **Tłumaczenia kolumn na poziomie źródła danych:**
   - Dodanie mechanizmu tłumaczeń dla kolumn na poziomie źródła danych (podobnie jak w procesach)
   - Tłumaczenia będą dostępne we wszystkich językach, w których system jest dostępny
   - Raz zdefiniowane tłumaczenie będzie działać dla wszystkich raportów używających tego źródła danych
   - Mechanizm będzie analogiczny do tłumaczeń w procesach

3. **Tłumaczenia agregacji systemowo:**
   - Tłumaczenie podstawowych agregacji (count, sum, min, max, average) na poziomie systemowym
   - Agregacje będą automatycznie przetłumaczone w zależności od języka interfejsu

**Rozwój (kolejne kroki):**

4. **Własne etykiety dla agregacji per raport:**
   - Możliwość nadania własnej etykiety dla agregacji w kontekście konkretnego raportu
   - Przykład: zamiast "sum Report id" wyświetlić "Ilość rekordów" lub "Ilość raportów"
   - Etykiety będą definiowane per raport (np. w konfiguracji osi X/Y wykresu)
   - Dotyczy zarówno raportów systemowych, jak i biznesowych

### Szczegóły techniczne

- W procesach już istnieje mechanizm tłumaczeń – należy go rozszerzyć na źródła danych
- Tłumaczenia kolumn będą definiowane na poziomie źródła danych (podobnie jak tłumaczenia pól w procesach)
- Tłumaczenia agregacji będą systemowe (automatyczne w zależności od języka interfejsu)
- Własne etykiety dla agregacji będą definiowane w konfiguracji raportu (np. w ustawieniach osi wykresu)
- Problem dotyczy różnych typów raportów: wykresy słupkowe, kolumnowe, pivot, Gantt

**Uwaga:** Rozważano również możliwość definiowania tłumaczeń per raport, ale uznano to za niepraktyczne – każdy raport wymagałby osobnego tłumaczenia wszystkich etykiet, co prowadziłoby do duplikacji pracy.

### Zadania

- **Łukasz Bott:** Przygotowanie PA (Product Analysis) dla tłumaczeń w raportach
- **Marek Dziakowski / Anna Skupińska:** Naprawa wyświetlania istniejących tłumaczeń agregacji w trybie odczytu
- **Marek Dziakowski / Anna Skupińska:** Implementacja tłumaczeń agregacji na poziomie systemowym (count, sum, min, max, average)
- **Backend:** Dodanie mechanizmu tłumaczeń dla kolumn na poziomie źródła danych (analogicznie do procesów)
- **Frontend:** Wyświetlanie przetłumaczonych kolumn w raportach
- **Marek Dziakowski / Anna Skupińska:** Implementacja możliwości nadawania własnych etykiet dla agregacji per raport

### Punkty otwarte

- Czy wszystkie agregacje powinny być tłumaczone systemowo, czy tylko podstawowe?
- Jak obsłużyć przypadek, gdy użytkownik chce mieć różne etykiety dla tej samej agregacji w różnych miejscach raportu?
- Czy własne etykiety dla agregacji powinny być dostępne tylko dla raportów biznesowych, czy również dla systemowych?
- Jak rozwiązać problem z wielojęzycznością – czy własne etykiety powinny być definiowane per język?

