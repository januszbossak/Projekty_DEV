# CHANGELOG – Źródła danych

---

## 2025-07-07 | Dokumentacja techniczna
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-07-07 Odczyt i zapis do Źródła danych typu static.md](../../../Notatki/Gotowe-notatki-archiwum/2025-07-07%20Odczyt%20i%20zapis%20do%20Źródła%20danych%20typu%20static.md)
**Kategoria:** #Dokumentacja #Architektura
**Projekt:** [Klienci/WIM/Zmienne-globalne](../../Klienci/WIM/Zmienne-globalne/)

- **CRUD dla Źródeł danych Static - pełna specyfikacja techniczna**
  - Funkcje: `SourceGet`, `SourceSet`, `SourceAddRow`, `SourceFind`
  - Zabezpieczenia: Optimistic Locking, ACL, audyt, walidacja
  - Flaga `IsRuleManaged` blokująca import z Excel
- **Szczegóły:** Zobacz pełną dokumentację w [Klienci/WIM/Zmienne-globalne](../../Klienci/WIM/Zmienne-globalne/CHANGELOG.md)

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność
**Projekt:** [Klienci/WIM/Zmienne-globalne](../../Klienci/WIM/Zmienne-globalne/)

- **Źródła danych "Static" - rozbudowa dla WIM/Zmienne-globalne**
  - Implementacja funkcji `SetEx`/`SetExternal` oraz `Add` dla źródeł typu Static/Local
  - Źródło inicjowane z Excela lub puste (tworzy tabelę w DB)
  - Zablokowanie możliwości usunięcia takiego źródła (ochrona integralności)
  - `SetEx`: Jeśli klucz istnieje → `Update`, jeśli nie istnieje → `Insert`
- **Status:** ✅ Zatwierdzone
- **Szczegóły:** Zobacz [Klienci/WIM/Zmienne-globalne](../../Klienci/WIM/Zmienne-globalne/CHANGELOG.md)

---

