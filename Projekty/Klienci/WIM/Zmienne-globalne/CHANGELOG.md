# CHANGELOG – Zmienne-globalne

---

## 2025-07-07 | Dokumentacja techniczna
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-07-07 Odczyt i zapis do Źródła danych typu static.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-07-07%20Odczyt%20i%20zapis%20do%20Źródła%20danych%20typu%20static.md)
**Kategoria:** #Dokumentacja #Architektura

**CRUD dla Źródeł danych Static - pełna specyfikacja techniczna**

### Funkcje reguł:
- **`SourceGet`** - pobieranie danych (cały rekord lub konkretna kolumna)
- **`SourceSet`** - modyfikacja danych (jedna wartość lub wiele)
- **`SourceAddRow`** - dodawanie nowych rekordów
- **`SourceFind`** - wyszukiwanie z kryteriami, sortowaniem i limitem

### Use case'y:
- **Budżety**: urlopów, dni konsultacyjnych, szkoleń, finansowe, nadgodziny
- **Magazyny**: sprzęt biurowy, IT, materiały, próbki/leki
- **Zasoby**: sale konferencyjne, pojazdy służbowe, stanowiska pracy
- **Limity**: dostęp, certyfikaty, licencje oprogramowania
- **Systemy punktowe**: lojalnościowe, nagrody, rankingi
- **KPI i metryki**: departamentów, procesów, statystyki

### Zabezpieczenia:
- **Concurrency Control**: Optimistic Locking (rowversion/version counter)
- **ACL**: Poziomy READ/WRITE/CREATE/ADMIN
- **Audyt**: Pełny logging operacji CRUD
- **Walidacja**: Automatyczna (typy, długości) + niestandardowa (biznesowa)
- **Flaga `IsRuleManaged`**: Blokada importu z Excel dla zarządzanych źródeł

### Obsługiwane typy kolumn:
- VARCHAR(n), DECIMAL(p,s), DATETIME, INT, BOOLEAN

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **Zmienne globalne / Źródła danych "Static"** - rozbudowa zewnętrznych źródeł danych dla WIM
  - Problem: brak odpowiednika "zmiennych procesowych" (globalnych dla procesu), które można łatwo edytować z poziomu reguł
  - ❌ Odrzucono: użycie rejestrów (negatywne skojarzenia klienta, "ciężkie")
- **Implementacja funkcji `SetEx` / `SetExternal` oraz `Add`:**
  - Źródło inicjowane z Excela lub puste (tworzy tabelę w DB)
  - Zablokowanie możliwości usunięcia takiego źródła (ochrona integralności)
  - `SetEx`: Jeśli klucz istnieje → `Update`, jeśli nie istnieje → `Insert` (Add)
  - Umożliwi budowanie prostej logiki "zmiennych globalnych" (zdejmowanie ze stanu magazynowego, aktualizacja budżetu) bez tworzenia tysięcy spraw
- **Status:** ✅ Zatwierdzone

---

