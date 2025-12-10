---
ostatnia_aktualizacja: 2025-12-09
changelog_przeglad_do: 2025-12-01
---

# Architektura: Podpis kwalifikowany SignApp (macOS)

> **Ostatnia aktualizacja:** 2025-12-09
> **CHANGELOG przegląd do:** 2025-12-01

---

## Aktualna koncepcja

### Stack techniczny

- **Framework:** MAUI.NET (następca Xamarin)
- **Platforma:** macOS
- **Biblioteki:** Obsługa Szafir (KIR)
- **Dystrybucja:** Poza App Store (Apple Enterprise)

### Główne komponenty

- **UI:** Wyświetlanie aktywnych certyfikatów, opcja "Pokaż wszystkie" (tryb dev), komunikaty błędów wzorowane na module raportowym.
- **Logika:** Automatyczne wykrywanie bibliotek do podpisywania.

### Integracja z AMODIT

- Integracja z Trust Center (implied from context, details missing in recent changelog).

---

## Kluczowe decyzje architektoniczne

| Data | Decyzja | Dlaczego | Status | Źródło |
|------|---------|----------|--------|--------|
| [[2025-12-01]] | Dystrybucja poza App Store (Apple Enterprise) | Wymagania projektowe/biznesowe | ✅ Wdrożone | [[2025-12-01 Planowanie sprintu]] |
| [[2025-11-19]] | Domyślnie widoczne tylko aktywne certyfikaty | Poprawa UX | ✅ Wdrożone | [[2025-11-19 Notatka projektowa]] |
| [[2025-11-03]] | Budowa w MAUI.NET | Nowsza technologia, następca Xamarin | ✅ Wdrożone | [[2025-11-03 Sprint review]] |

---

## Historia koncepcji (odrzucone/zmienione)

| Data | Co było | Dlaczego odrzucono | Źródło |
|------|---------|-------------------|--------|
| [[2025-11-07]] | Użycie SimpleSign (alternatywa) | Klient odrzucił (wymóg Szafira na Mac) | [[2025-11-07 Planowanie Sprintu]] |

---

## Uwagi dla agenta overview-sync

**KRYTYCZNE zasady kategoryzacji:**

Agent MUSI analizować **treść wpisu** z CHANGELOG, nie tylko tag!

**Wpisy należące do ARCHITEKTURA.md:**
- Decyzje o technologiach (OAuth2, React, .NET, MSSQL, Docker, SignalR)
- Decyzje o strukturze (architektura, endpoint, API, integracja)
- Odrzucone koncepcje techniczne
- Stack techniczny, wybór bibliotek
