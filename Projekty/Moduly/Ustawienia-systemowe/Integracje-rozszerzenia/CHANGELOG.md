# CHANGELOG - Integracje i rozszerzenia

---

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Funkcjonalność #Design

**Walidacja parametrów integracji - Demo implementacji** ✅
- **Cel:** Eliminacja błędów konfiguracji (literówki w nazwach parametrów)
- **Zaimplementowano:**
  - Predefiniowane nazwy i typy parametrów
  - Walidacja nazw (blokada duplikatów systemowych)
  - Grupowanie parametrów (zakładki)
- **Feedback/Zmiany:**
  - Rozdzielić parametry dla POST i GET różnymi grupami
  - Ukryć "ExternalREST" w nazwach (zbyt techniczne)
  - Rozdzielić Integracje AMODIT i Rozszerzenia AMODIT (docelowo)
  - Zwiększyć limit długości nazwy (obecnie 50 znaków)
