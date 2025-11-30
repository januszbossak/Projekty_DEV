# Call Snippet

**Klient:** WIM
**Status:** 🟢 W realizacji
**PDM:** [do uzupełnienia]
**Tech Lead:** [do uzupełnienia]
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Call-Snippet]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- Roadmapa MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Funkcja `CallFunction` w rzeczywistości wstawia kod (snippet) w miejsce wywołania, a nie działa jak klasyczna funkcja programistyczna. Nazwa jest myląca.

### Rozwiązanie

Zmiana nazwy z `Call Function` na `Call Snippet` z zachowaniem kompatybilności wstecznej (alias). Rezygnacja z dodawania jawnych parametrów na tym etapie - używanie zmiennych wewnątrz snippetu.

### Obecna faza

🛠️ **W realizacji** - implementacja zmiany nazwy

**Ukończono:**
- ✅ Decyzja o zmianie nazwy
- ✅ Decyzja o rezygnacji z jawnych parametrów

**W trakcie:**
- Implementacja zmiany nazwy w kodzie
- Utworzenie aliasu dla kompatybilności wstecznej
- Aktualizacja dokumentacji i interfejsu

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Zmiana nazwy na Call Snippet** | Dokładniej odzwierciedla rzeczywiste zachowanie - wstawianie kodu |
| **Kompatybilność wsteczna (alias)** | Istniejące wywołania nie mogą zostać zablokowane |
| **Rezygnacja z jawnych parametrów** | Uproszczenie implementacji, obecny model działa poprawnie |

---

## MVP1: Zmiana nazwy Call Function → Call Snippet

**Cel:** Wprowadzenie poprawnej nazwy z zachowaniem kompatybilności wstecznej

**Zakres:**
- [ ] Zmiana nazwy w kodzie
- [ ] Utworzenie aliasu
- [ ] Aktualizacja interfejsu i dokumentacji

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Backlog: [do uzupełnienia]

