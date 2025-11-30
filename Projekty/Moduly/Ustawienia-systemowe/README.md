# Ustawienia systemowe

**Klient:** AMODIT (roadmapa)
**Status:** 🟡 W analizie
**PDM:** [do uzupełnienia]
**Tech Lead:** Przemek, Kamil, Adrian
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Ustawienia-systemowe]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- Podprojekty z własnymi MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Obecny moduł ustawień systemowych AMODIT jest przestarzały, nieintuicyjny i rozproszony. Administratorzy napotykają na trudności w konfiguracji systemu, zarządzaniu integracjami, zadaniami cyklicznymi (jobs) i parametrami.

### Rozwiązanie

Nowoczesny, spójny moduł ustawień systemowych w React, podzielony na podprojekty:
- **Integracje-rozszerzenia** - konfiguracja integracji z zewnętrznymi systemami
- **Zadania-jobs** - zarządzanie zadaniami cyklicznymi (usługi asynchroniczne)

### Obecna faza

📋 **W analizie** - finalizacja MVP dla konfiguracji integracji

**Ukończono:**
- ✅ Definicja struktury MVP integracji
- ✅ Ustalenie zasad wyświetlania (tylko skonfigurowane integracje)

**W trakcie:**
- Finalizacja szczegółów interfejsu zgodnie z ustaleniami MVP
- Przemyślenie lokalizacji konfiguracji OAuth i tokenów

---

## Podprojekty

| Podprojekt | Status | MVP | Opis |
|------------|--------|-----|------|
| [[Integracje-rozszerzenia]] | 🟡 W analizie | MVP1 Q4 2025 | Konfiguracja integracji z zewnętrznymi systemami |
| [[Zadania-jobs]] | 🟡 W analizie | - | Zarządzanie zadaniami cyklicznymi (usługi asynchroniczne) |

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Backend bez zmian** (tabela `parameters`) | Minimalizacja ryzyka, skupienie na UI, uniknięcie migracji danych |
| **Rozróżnienie integracji i modułów** | Integracje = połączenia z zewnętrznymi systemami, moduły = funkcjonalności systemu (w licencji) |

---

## Główne ryzyka

| Ryzyko | Mitygacja |
|--------|-----------|
| Utrata kompatybilności z istniejącymi konfiguracjami klientów | Zapewnienie kompatybilności wstecznej - wszystkie istniejące konfiguracje muszą pozostać widoczne |
| Przedłużenie się prac nad MVP przez próbę realizacji wszystkich pomysłów jednocześnie | Skupienie na MVP bez reorganizacji kategorii i funkcjonalności AI - odłożenie na później |

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Backlog: [do uzupełnienia]
