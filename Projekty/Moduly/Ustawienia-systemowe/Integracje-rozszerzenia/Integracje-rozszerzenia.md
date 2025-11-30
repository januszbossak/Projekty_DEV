# Project Canvas: Integracje-rozszerzenia

**Projekt nadrzędny:** [[Ustawienia-systemowe]]
**Status:** 🟡 W analizie
**Powód statusu / Bloker:** Finalizacja MVP - wymaga uproszczenia interfejsu
**Ostatnia aktualizacja:** 2025-08-07
**Klient:** AMODIT (roadmapa)

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | Przemek, Kamil | Architektura tego podprojektu |
| **Deweloper** | Kamil Dubaniowski, Przemek | Implementacja |
| **Tester** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Obecny interfejs konfiguracji integracji pokazuje wszystkie możliwe integracje (nawet nieużywane), co utrudnia administratorom identyfikację faktycznie skonfigurowanych integracji. Brak jasnego rozróżnienia między integracjami wbudowanymi (nie wymagającymi konfiguracji) a tymi wymagającymi konfiguracji oraz integracjami własnymi (customowymi).

### Cel biznesowy

Dostarczenie intuicyjnego interfejsu konfiguracji integracji, który pokazuje tylko faktycznie skonfigurowane integracje i umożliwia administratorom szybką konfigurację bez potrzeby wsparcia technicznego.

### Cel techniczny

Przebudowa interfejsu konfiguracji integracji w Reactcie, zachowując kompatybilność wsteczną z istniejącymi konfiguracjami klientów. Backend pozostaje bez zmian (tabela `Parameters`), jednak powstaną nowe endpointy do komunikacji z frontendem.

### Metryka sukcesu

- Administrator może zidentyfikować skonfigurowane integracje **w < 30 sekund** (czytelna lista tylko aktywnych)
- Administrator może skonfigurować nową integrację **w < 5 minut** bez dokumentacji technicznej
- Wszystkie istniejące konfiguracje klientów pozostają widoczne po migracji (kompatybilność wsteczna)

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Backend bez zmian (tabela `parameters`)

Przebudowa front-endu panelu konfiguracji integracji **nie może** wprowadzać zmian w schemacie bazy danych ani logice backendu. Tabela `parameters` pozostaje bez modyfikacji. Jednak powstaną nowe endpointy do komunikacji z Frontendem.

**Uzasadnienie:** Minimalizacja ryzyka i skupienie na UI. Zmiana backendu wymagałaby migracji danych i testów regresyjnych na setkach instalacji klientów.

### Zasada 2: Kompatybilność wsteczna

Wszystkie istniejące konfiguracje klientów muszą pozostać widoczne po reorganizacji interfejsu.

**Uzasadnienie:** Setki instalacji AMODIT nie mogą zostać zablokowane po aktualizacji systemu.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-08-07 | Struktura MVP integracji: integracje wbudowane jako pierwsza pozycja, lista tylko skonfigurowanych integracji, przycisk "Nowa" z opcją "Skonfiguruj własną" | Czytelny interfejs pokazujący faktyczny stan konfiguracji, jasne rozróżnienie typów integracji | - |
| ADR-002 | ✅ Zatwierdzone | 2025-08-07 | Backend bez zmian (tabela `parameters`) | Skupienie na UI, minimalizacja ryzyka, uniknięcie migracji danych | - |
| ADR-003 | ✅ Zatwierdzone | 2025-08-07 | Rozróżnienie integracji i modułów: integracje = połączenia z zewnętrznymi systemami, moduły = funkcjonalności systemu (w licencji) | Jasne kryterium podziału, eliminacja pomieszania w interfejsie użytkownika | - |
| ADR-004 | 🔍 Do weryfikacji | 2025-08-07 | Koncepcja OAuth i tokenów: definicja aplikacji OAuth z możliwością generowania wielu tokenów, wybór tokenu w konfiguracji integracji | Właściwy kierunek, ale lokalizacja wymaga dalszego przemyślenia (integracje vs osobna zakładka) | - |
| ADR-005 | ⏸️ Odroczone | 2025-08-07 | Kategoryzacja integracji według zastosowań biznesowych (podpisy, przechowywanie dokumentów, uwierzytelnianie) | Zbyt złożone na MVP, wymaga osobnego projektu | - |
| ADR-006 | ⏸️ Odroczone | 2025-08-07 | Wykorzystanie AI (AMODIT Copilot) do automatycznego generowania konfiguracji integracji na podstawie specyfikacji API (np. Swagger) | Nie mieści się w zakresie MVP, element "MVP rozszerzonego" | - |
| ADR-007 | ❌ Odrzucone | 2025-08-07 | Eksport helpa do PDF | Brak uzasadnienia biznesowego, help jest dostępny w AMODIT Copilocie i plikach YAML, dokumentacja zmienia się często | - |
| ADR-008 | ✅ Zatwierdzone | [[2025-09-08]] | Wprowadzenie walidacji i predefiniowanych wartości dla parametrów integracji. | Eliminuje błędy (literówki) i przyspiesza konfigurację poprzez podpowiadanie poprawnych wartości i typów (np. "password" -> typ hasło). | - |
| ADR-009 | 💡 Propozycja | [[2025-09-08]] | Rozdzielenie listy "Integracje systemowe" i "Rozszerzenia" w interfejsie. | Upraszcza UI i ułatwia orientację. Użytkownik od razu wie, czy konfiguruje wbudowaną integrację, czy dodaje własną. | - |
| ADR-010 | 💡 Propozycja | [[2025-09-08]] | Dodać opisy dla integracji systemowych i panel do ukrywania nieużywanych integracji. | Zwiększa czytelność i pozwala użytkownikowi dostosować listę do swoich potrzeb, ukrywając zbędne opcje. | - |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza

Projekt jest w fazie analizy i finalizacji MVP dla modułu integracji w ustawieniach systemowych. Trwa definiowanie struktury interfejsu i zasad wyświetlania integracji.

**Ukończono:**
- ✅ Definicja struktury MVP integracji
- ✅ Ustalenie zasad wyświetlania (tylko skonfigurowane integracje)

**Trwa praca nad:**
- Finalizacja szczegółów interfejsu zgodnie z ustaleniami MVP
- Przemyślenie lokalizacji konfiguracji OAuth i tokenów

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Średnie]** Utrata kompatybilności z istniejącymi konfiguracjami klientów podczas reorganizacji interfejsu | Średnie | Wysoki | Zapewnienie kompatybilności wstecznej - wszystkie istniejące konfiguracje muszą pozostać widoczne | Tech Lead |
| **[Średnie]** Przedłużenie się prac nad MVP przez próbę realizacji wszystkich pomysłów jednocześnie | Średnie | Średni | Skupienie na MVP bez reorganizacji kategorii i funkcjonalności AI - odłożenie na później | PDM |
| **[Niskie]** Niejasność dla użytkownika końcowego co do lokalizacji konfiguracji różnych typów integracji | Niskie | Niski | Jasne rozróżnienie integracji wbudowanych (pierwsza pozycja) i skonfigurowanych (druga kolumna) | Tech Lead |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: "Konfiguracja integracji" (Plan: Q4 2025)

**Cel:** Dostarczenie intuicyjnego interfejsu konfiguracji integracji, który pokazuje tylko faktycznie skonfigurowane integracje i umożliwia administratorom szybką konfigurację bez potrzeby wsparcia technicznego. Interfejs eliminuje przeładowanie listą wszystkich możliwych integracji i jasno rozróżnia typy integracji.

**Definicja ukończenia (DoD):**
- Administrator widzi tylko skonfigurowane integracje (z parametrami, nawet częściowo)
- Integracje wbudowane nie wymagające konfiguracji są widoczne w osobnej sekcji
- Administrator może dodać nową integrację standardową lub własną przez przycisk "Nowa"
- Wszystkie istniejące konfiguracje klientów pozostają widoczne (kompatybilność wsteczna)
- Interfejs w Reactcie z możliwością konfiguracji parametrów z poziomu UI

**Funkcjonalności:**

#### Struktura interfejsu
- [ ] Pierwsza pozycja: "Integracje wbudowane" – stała sekcja zawierająca integracje nie wymagające konfiguracji (VIES, kursy walut, Biała Lista)
- [ ] Po kliknięciu integracji wbudowanej wyświetla się ikonka i krótki opis działania
- [ ] Druga kolumna: Lista integracji skonfigurowanych (tylko te z parametrami, nawet częściowo)
- [ ] Integracje wbudowane wymagające konfiguracji pojawiają się na liście tylko gdy są skonfigurowane
- [ ] Integracje własne (customowe) dodawane przez przycisk "Skonfiguruj własną"

#### Przycisk "Nowa" / "Dodaj integrację"
- [ ] Wybór między standardową integracją (z listy dostępnych)
- [ ] Opcja "Skonfiguruj własną" – pojawia się formularz z parametrami (np. Custom CRM)

#### Logika wyświetlania
- [ ] Integracja pojawia się na liście tylko gdy ma skonfigurowane parametry (nawet nie w całości)
- [ ] Integracje "czyste" (bez konfiguracji) nie są widoczne na liście

#### Konfiguracja parametrów
- [ ] Możliwość dodawania parametrów z poziomu interfejsu (bez dostępu do bazy danych)
- [ ] Weryfikacja, że w interfejsie integracji nie ma modułów (tylko prawdziwe integracje)

**Poza zakresem MVP (Out of Scope):**
- Kategoryzacja integracji według zastosowań biznesowych (podpisy, przechowywanie dokumentów, uwierzytelnianie) – odłożone na osobny projekt
- Konfiguracja OAuth i tokenów – do weryfikacji lokalizacji
- Wykorzystanie AI do automatycznego generowania konfiguracji integracji – odłożone na przyszłość
- Eksport helpa do PDF – odrzucone

**Planowana data:** Q4 2025

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- **Konfiguracja OAuth i tokenów** (Priorytet: Średni)
  - Definicja aplikacji OAuth z 5 parametrami
  - Możliwość generowania wielu tokenów dla jednej aplikacji
  - W konfiguracji integracji wybór tokenu zamiast ręcznego wpisywania parametrów
  - Wymaga decyzji: lokalizacja w integracjach vs osobna zakładka
- **Reorganizacja ustawień systemowych – kategoryzacja integracji** (Priorytet: Średni)
  - Podział na kategorie: podpisy (Autenti, DocuSign, Trust Center), przechowywanie (SharePoint, KSeF, Alfresco), uwierzytelnianie (Active Directory, baza danych)
  - Osobny projekt na przyszły kwartał/rok
- **Wykorzystanie AI do tworzenia integracji** (Priorytet: Niski)
  - Wykorzystanie AMODIT Copilot do analizy dokumentacji API (np. Swagger)
  - Generowanie propozycji parametrów i sposobu logowania
  - Element "MVP rozszerzonego" i części szerszej strategii wykorzystania AI
- **Obsługa integracji wymagających licencji/abonamentu** (Priorytet: Niski)
  - Możliwość generowania prośby o licencję do działu handlowego

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-07 | Utworzenie podprojektu - definicja MVP dla konfiguracji integracji, ustalenie struktury interfejsu, decyzje architektoniczne | Rada Architektów 2025-08-07 |
| [[2025-09-08]] | Demo walidacji parametrów integracji. Zebrano feedback: potrzeba rozdzielenia integracji systemowych od rozszerzeń, dodania opisów, poprawy UX (przycisk "nowa") i zwiększenia limitu znaków dla nazw. | [[2025-09-08 Sprint review]] |

---

## 6. PRZYDATNE LINKI

- **Projekt nadrzędny:** [[Ustawienia-systemowe]]
- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Inicjatywa w backlogu:** [do uzupełnienia]

