# Notatka projektowa – 2025-11-25 – Roadmapa 2025 i Strategia Wdrożeniowa

**Data:** 2025-11-25
**Temat główny:** Ustalenia dotyczące Roadmapy na rok 2025, priorytetyzacja prac (Edytor, Raporty, Deploy) oraz strategia skrócenia czasu wdrożeń.

---

## 1. Roadmapa Q4 2024 (Domykanie)

**Komponent:** Roadmapa / Zarządzanie

### Cel i problem
Zamknięcie bieżących tematów przed końcem roku, aby w Q1 2025 móc skupić się na nowych, dużych inicjatywach.

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- **Raporty (Tabela):** Podstawowa funkcjonalność tabeli (masowa obsługa spraw) musi działać stabilnie.
- **Eksport do Archiwum Państwowego (LOT):** Realizacja poprzez generowanie paczek z walidacją (zamiast integracji z API). Bez grafiki z AMPL.
- **Komunikator:** Uznany za wdrożony (do weryfikacji).
- **MSP (Małe i Średnie Przedsiębiorstwa):** Mateusz realizuje w miarę możliwości.

---

## 2. Roadmapa Q1 2025 (Priorytety)

**Komponent:** Roadmapa / Rozwój Produktu

### Cel i problem
Skupienie zespołu na dwóch-trzech kluczowych obszarach, aby dostarczyć skończone, wysokiej jakości rozwiązania, które rozwiążą problemy sprzedażowe (przestarzały wygląd) i wdrożeniowe (trudne przenoszenie).

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

1.  **Dokończenie Nowego Edytora Procesów:**
    -   Priorytet ze względu na dział sprzedaży (prezentacja produktu).
    -   Zakres: Formularz (już jest), Diagram (reguły, wizualizacja), Lista etapów.
    -   Cel: Pokazanie relacji między elementami (np. które reguły wpływają na pole).

2.  **Przenoszenie Procesów (Deploy):**
    -   Rozwiązanie problemu migracji między środowiskami (DEV -> TEST -> PROD).
    -   Funkcjonalność: Wizard, historia zmian, porównywanie różnic (diff), wsparcie AI (analiza różnic).

3.  **Moduł Raportowy (Refactoring):**
    -   Głęboki refactoring architektury, wykresów, dashboardów i filtrów.

**Zasada pracy:** Skupienie całego zespołu na 2 tematach naraz (Focus), zamiast rozpraszania się na wiele drobnych zadań.

---

## 3. Strategia Wdrożeniowa i Szablony AI

**Komponent:** Wdrożenia / AI

### Cel i problem
AMODIT przegrywa przetargi u mniejszych klientów z powodu wysokich cen i długiego czasu wdrożenia (wycenianego jak dla dużych korporacji typu LPP). Brakuje oferty "szybkiego sukcesu" (wdrożenie w tydzień).

### Decyzja / Sposób realizacji
**Status:** 💡 Propozycja

- **Szablony procesów ("Pudełka"):** Powrót do koncepcji gotowych szablonów (np. Obieg Faktur, e-Teczka).
- **Wsparcie AI (Wizard Wdrożeniowy):** Zamiast tworzyć sztywne szablony z 15 opcjami, wykorzystać AI do "wywiadu" z konsultantem/klientem. AI na podstawie odpowiedzi dostosuje proces (np. usunie ścieżkę faktury korygującej).
- **Zmiana mentalności:** Dział wdrożeń musi nauczyć się wdrażać szybko i tanio, korzystając z gotowych narzędzi, a nie "rzeźbić" od zera.

---

## 4. Open Data

**Komponent:** Integracje / Open Data

### Cel i problem
Udostępnianie zbiorów danych publicznie w sposób wydajny i bezpieczny.

### Decyzja / Sposób realizacji
**Status:** ⏸️ Odroczone (na Q2)

- **Q1:** Prace koncepcyjne (architektura, wydajność, uprawnienia, przyrostowe pobieranie).
- **Q2:** Implementacja.

---

## Punkty do dalszej dyskusji (globalne)

- Szczegóły implementacji wizarda do przenoszenia procesów.
- Sposób zaangażowania Piotra Buczkowskiego w prace koncepcyjne (np. Open Data, Deploy).
- Weryfikacja dostępu do transkrypcji dla Janusza (nadanie uprawnień współorganizatora).
