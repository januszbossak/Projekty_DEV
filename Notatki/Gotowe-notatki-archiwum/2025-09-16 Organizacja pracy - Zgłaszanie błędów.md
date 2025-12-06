# Organizacja pracy – 2025-09-16

> 🛡️ Utworzono podczas Review w dniu 2025-12-04
> Źródło transkrypcji: [2025-09-16 Rada developerów.md](../../Transkrypcje/oczyszczone-archiwum/2025-09-16%20Rada%20developerów.md)

---

## 1. Zgłaszanie błędów – kanały komunikacji i opiekun tematu

**Obszar:** `Organizacja-DEV`

### Kontekst i Problem

Piotr Buczkowski zgłosił pytanie o właściwy kanał zgłaszania błędów i niedogodności (np. problem z podmianą literki w nazwie pola). Obecnie brakuje jasnych wytycznych:
- Gdzie zgłaszać błędy: Teams vs Backlog?
- Kto jest odpowiedzialny za walidację zgłoszeń?
- Jak unikać duplikacji zgłoszeń (np. 3 te same tematy w ciągu 2 tygodni)?

Problem: bez dedykowanego opiekuna tematu trudno jest śledzić, co już było zgłoszone, co jest w trakcie obsługi, a co jest świadomym błędem w MVP.

### Zidentyfikowane Ryzyka

- Brak centralnego miejsca zgłaszania powoduje rozproszenie informacji
- Duplikacja zgłoszeń prowadzi do marnowania czasu zespołu
- Brak walidacji powoduje, że zgłoszenia mogą być nieprawidłowo priorytetyzowane

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zgłaszanie na Backlog z opiekunem tematu | Zgłoszenia na Backlog, ale zawsze przypisane do opiekuna tematu (np. Kamil dla edytora procesów) | ⏸️ Odroczona – wymaga konfiguracji i może być niewygodne dla wielu osób |
| Zgłaszanie na kanał Teams projektu | Zgłaszanie błędów na dedykowany kanał Teams dla danego projektu (np. "Edytor procesów", "Moduł raportowy") | ✅ Wybrana – prostsze rozwiązanie, łatwiejsze w użyciu |
| Work Item Generator w Azure DevOps | Wykorzystanie funkcji Microsoft do wykrywania podobnych zgłoszeń podczas tworzenia | ⏸️ Odroczona – wymaga konfiguracji, do sprawdzenia |

### Decyzja

**Status:** ✅ Zatwierdzone

Zgłoszenia błędów należy kierować na odpowiedni kanał Teams dla danego projektu. Kanały Teams powinny być przeglądane przez 3 osoby:
- Delivery Manager (Damian, Kamil lub Łukasz)
- Deweloper odpowiedzialny za projekt
- Tester odpowiedzialny za projekt

Te osoby są odpowiedzialne za:
- Odpowiedź na pytanie "czy to już jest zgłoszone?"
- Walidację czy zgłoszenie nadaje się na bug
- Informowanie czy nad tym już pracujemy lub jest rozwiązane w nowszej wersji
- Ewentualne przekierowanie do zgłoszenia na Backlog, jeśli wymagane

**Szczegóły techniczne:**
- Istniejące kanały: Pentesty, Moduł raportowy, Forma, Nowy X sprawy
- Możliwość dodania nowych kanałów w razie potrzeby

### Zadania

- **Wszyscy:** Zgłaszać błędy na odpowiedni kanał Teams projektu (np. "Edytor procesów" dla błędów edytora)
- **Delivery Managerzy:** Przeglądać kanały Teams i odpowiadać na zgłoszenia

### Punkty otwarte

- Czy Work Item Generator w Azure DevOps może pomóc w wykrywaniu duplikacji zgłoszeń?
- Jak zapewnić, że zgłoszenia nie będą zalegać, gdy opiekun jest nieobecny?
