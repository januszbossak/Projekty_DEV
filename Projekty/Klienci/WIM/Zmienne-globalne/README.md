# Zmienne globalne (Źródła danych Static)

**Klient:** WIM
**Status:** 🟢 W realizacji
**PDM:** [do uzupełnienia]
**Tech Lead:** [do uzupełnienia]
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Zmienne-globalne]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- Roadmapa MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Brak w AMODIT odpowiednika "zmiennych procesowych" (globalnych dla procesu, np. pula dni urlopowych, budżet, lista sprzętu), które można łatwo edytować z poziomu reguł, a które nie są sprawami (rejestrami).

### Rozwiązanie

Rozbudowa Zewnętrznych Źródeł Danych o typ "Static" / "Local":
- Możliwość inicjalizacji z Excela lub jako puste źródło (tworzy tabelę w DB)
- Funkcje `SetEx` / `SetExternal` i `Add` z logiką Update/Insert
- Zabezpieczenie źródeł statycznych przed usunięciem

### Obecna faza

🛠️ **W realizacji** - implementacja typu Static i funkcji SetEx/Add

**Ukończono:**
- ✅ Decyzja o rozbudowie źródeł danych
- ✅ Decyzja o implementacji funkcji SetEx i Add
- ✅ Decyzja o zabezpieczeniu przed usunięciem

**W trakcie:**
- Implementacja typu źródła danych Static
- Implementacja funkcji SetEx i Add
- Zabezpieczenie przed usunięciem

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Typ źródła Static / Local** | Umożliwienie przechowywania zmiennych globalnych bez tworzenia spraw |
| **Funkcje SetEx i Add** | Elastyczność w zarządzaniu danymi - Update/Insert w zależności od istnienia klucza |
| **Zabezpieczenie przed usunięciem** | Ochrona integralności danych procesowych |
| **Odrzucenie rejestrów** | Negatywne skojarzenia klienta, "ciężkość" rozwiązania |

---

## MVP1: Źródła danych Static z funkcjami SetEx i Add

**Cel:** Umożliwienie przechowywania i zarządzania zmiennymi globalnymi z poziomu reguł

**Zakres:**
- [ ] Typ źródła Static / Local
- [ ] Inicjalizacja z Excela lub puste
- [ ] Funkcje SetEx i Add (Update/Insert)
- [ ] Zabezpieczenie przed usunięciem

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Backlog: [do uzupełnienia]

