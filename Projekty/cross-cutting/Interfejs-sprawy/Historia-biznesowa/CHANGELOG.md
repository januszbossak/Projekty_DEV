# CHANGELOG – Historia biznesowa

---

## 2025-11-19 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-19 Notatka projektowa - Przegląd wycen.md]
**Kategoria:** #Funkcjonalność #Design #Zadanie #Decyzja

- Klient oczekuje wyświetlania historii spraw powiązanych (Rossmann).
- Należy ustalić, czy klient potrzebuje pełnej historii technicznej, czy dedykowanej historii biznesowej.
- Spotkanie z klientem w celu ustalenia oczekiwań biznesowych.

---

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Spotkania projektowe/2025-12-03 Notatka projektowa - Historia biznesowa.md](../../../../Notatki/Spotkania%20projektowe/2025-12-03%20Notatka%20projektowa%20-%20Historia%20biznesowa.md)
**Kategoria:** 💡 Koncepcja

- **Dedykowana tabela powiązań biznesowych** – nowa tabela `CaseEventBusinessSubjects` z kolumnami `EventID`, `BusinessSubjectType`, `BusinessSubjectID`, `BusinessSubjectName`. Pozwala na indeksowanie i wielowymiarowe śledzenie zdarzeń.
- **Nowa składnia API `AddCaseEvent`** – funkcja przyjmuje listę obiektów `BusinessSubject` zamiast pojedynczego obiektu w JSON. Umożliwia przypisanie jednego zdarzenia do wielu bytów biznesowych (klient, polisa, teczka JRWA).
- **Mechanizm `connectedCase`** – rekurencyjne ładowanie historii z powiązanych spraw przez pole `connectedCaseID`. Pozwala na "spinanie" historii z wielu procesów w jedną chronologiczną listę.
- **Mockup UI historii wieloprocesowej** – lista chronologiczna z heurystyką (nazwa procesu tylko przy zmianie kontekstu). Do przekazania klientowi (Rossmann).
- **Obsługa błędnego przypisania** – mechanizm odpinania/przypinania z zachowaniem audit trail. Generowanie dwóch zdarzeń: "Odpięcie" + "Przypięcie" z powodem w `message`.
- **MVP w 3 pakietach:** MVP1 (tabela + connectedCase), MVP2 (JRWA + wielowymiarowość), MVP3 (UI enhancements + migracja).

---
