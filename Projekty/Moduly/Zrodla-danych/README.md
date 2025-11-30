# Źródła danych - usprawnienia
*Format: v2 (Project Canvas 2025-11)*

**Problem:** Zasilanie źródeł danych było ograniczone do SQL, a logika w `Call Function` nie była reużywalna między procesami.
**Rozwiązanie:** Wprowadzono dwa kluczowe usprawnienia:
1.  **Zasilanie źródeł danych przez REST API:** Systemy zewnętrzne mogą teraz bezpiecznie "wpychać" dane do AMODIT.
2.  **Globalna biblioteka `Call Function`:** Złożone skrypty można teraz pisać raz i używać ich w wielu różnych procesach, co promuje reużywalność kodu.
**Obecna faza:** ✅ Częściowo ukończone (API i biblioteka funkcji działają, biblioteka szablonów w planach).

**Link do pełnej dokumentacji:** [[Zrodla-danych]]
