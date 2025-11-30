# Project Canvas: Ustawienia systemowe

**Status:** 🛠️ W realizacji
**Powód statusu / Bloker:** Trwa stopniowe przepisywanie kolejnych ekranów na React.
**Ostatnia aktualizacja:** 2025-08-26
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-08-07
**Budżet/Czas:** [do uzupełnienia]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead** | Przemek, Kamil | Architektura, Code Review |
| **Deweloper** | Kamil Dubaniowski, Przemek, Adrian | Implementacja |
| **Tester** | [do uzupełnienia] | |
| **Opiekun handlowy** | [do uzupełnienia] | |
| **Klient (Decydent)** | [do uzupełnienia] | Akceptacja MVP, ostateczne decyzje biznesowe |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Obecny moduł ustawień systemowych AMODIT jest przestarzały, nieintuicyjny i rozproszony. Administratorzy napotykają na trudności w konfiguracji systemu, zarządzaniu integracjami, zadaniami cyklicznymi (jobs) i parametrami. Interfejs wymaga kompleksowej przebudowy, aby był nowoczesny, spójny wizualnie i łatwy w użyciu.

### Cel biznesowy

Dostarczenie nowoczesnego, spójnego modułu ustawień systemowych z intuicyjnym interfejsem, który umożliwi administratorom szybką i bezbłędną konfigurację wszystkich aspektów systemu AMODIT bez potrzeby wsparcia technicznego.

### Cel techniczny

Migracja modułu ustawień systemowych na React, zachowując stabilność backendu (tabela `parameters`), przy jednoczesnym wprowadzeniu ulepszeń ergonomii, grupowania parametrów i mechanizmów bezpieczeństwa.

### Metryka sukcesu

- Administrator może skonfigurować nową integrację **w < 5 minut** bez dokumentacji technicznej
- Parametry systemowe są pogrupowane logicznie i **łatwo znajdowalne w < 30 sekund**
- **Zero błędów konfiguracyjnych** wynikających z literówek w nazwach klas lub bibliotek (listy wyboru zamiast ręcznego wpisywania)

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Backend bez zmian (tabela `parameters`)

Przebudowa front-endu panelu ustawień systemowych **nie może** wprowadzać zmian w schemacie bazy danych ani logice backendu. Tabela `parameters` pozostaje bez modyfikacji. Jednak powstaną nowe endpointy do komunikacji z Frontendem.

**Uzasadnienie:** Minimalizacja ryzyka i skupienie na UI. Zmiana backendu wymagałaby migracji danych i testów regresyjnych na setkach instalacji klientów.

### Zasada 2: Kompatybilność wsteczna

Wszystkie nowe mechanizmy muszą działać bez wpływu na istniejące instalacje, które nie korzystają z tych funkcji.

**Uzasadnienie:** Setki instalacji AMODIT nie mogą zostać zablokowane po aktualizacji systemu.

---

## Decyzje architektoniczne (ADR)

| ID      | Status         | Data           | Decyzja                                                                                                                            | Uzasadnienie                                                                                                                                                                                                                         | Powód odrzucenia |
| ------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| ADR-001 | ✅ Zatwierdzone | [[2025-08-07]] | Backend bez zmian (tabela `parameters`)                                                                                            | Skupienie na UI, minimalizacja ryzyka, uniknięcie migracji danych                                                                                                                                                                    | -                |
| ADR-002 | ✅ Zatwierdzone | [[2025-08-07]] | Rozróżnienie integracji i modułów: integracje = połączenia z zewnętrznymi systemami, moduły = funkcjonalności systemu (w licencji) | Jasne kryterium podziału, eliminacja pomieszania w interfejsie użytkownika                                                                                                                                                           | -                |
| ADR-003 | ✅ Zatwierdzone | [[2025-08-12]] | Nowy interfejs dla jobów wymagających pola `Owner` zamiast modyfikacji istniejącego interfejsu `IJob`                              | Bezpieczne rozwiązanie, nie łamie kompatybilności wstecznej. Istniejące joby nie wymagają modyfikacji, nowe joby wymagające `Owner` implementują nowy interfejs                                                                      | -                |
| ADR-004 | ❌ Odrzucone    | [[2025-08-12]] | Modyfikacja istniejącego interfejsu `IJob` o pole `Owner`                                                                          | Powoduje problemy z kompatybilnością wsteczną - błędy wykonania we wszystkich istniejących implementacjach jobów, które nie zostały zaktualizowane (zarówno joby w solucji AMODIT jak i poza solucją, np. wszystkie joby integracji) | -                |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji

Projekt jest w fazie stopniowego przepisywania kolejnych ekranów na technologię React. Kluczowe widoki zostały już zmigrowane, a kolejne są w przygotowaniu.

**Ukończono:**
- ✅ Przepisano kluczowe ekrany ustawień na React.
- ✅ Zapewniono pełną kompatybilność wsteczną z możliwością powrotu do starego interfejsu.

**Trwa praca nad:**
- Migracją kolejnych, mniej priorytetowych ekranów ustawień.

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Średnie]** Utrata kompatybilności z istniejącymi konfiguracjami klientów podczas reorganizacji interfejsu | Średnie | Wysoki | Zapewnienie kompatybilności wstecznej - wszystkie istniejące konfiguracje muszą pozostać widoczne | Tech Lead |
| **[Średnie]** Przedłużenie się prac nad MVP przez próbę realizacji wszystkich pomysłów jednocześnie | Średnie | Średni | Skupienie na MVP bez reorganizacji kategorii i funkcjonalności AI - odłożenie na później | PDM |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

Projekt składa się z podprojektów, każdy z własnym MVP. Szczegóły w sekcji "7. PODPROJEKTY".

---

## 5. HISTORIA ZMIAN

| Data           | Zmiana                                                                                                                                         | Źródło                                                 |                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------------- |
| [[2025-08-07]] | Utworzenie projektu - definicja MVP dla konfiguracji integracji, ustalenie struktury interfejsu, decyzje architektoniczne                      | [[Notatki/Rada architektów/2025-08-07 Rada architektów\|Rada Architektów 2025-08-07]] |
| [[2025-08-12]] | Decyzja o nowym interfejsie dla jobów wymagających pola `Owner` zamiast modyfikacji istniejącego `IJob` - zachowanie kompatybilności wstecznej | [[Notatki/Rada architektów/2025-08-12 Rada architektów\|Rada Architektów 2025-08-12]] |
| [[2025-08-25]] | Zaimplementowano prototyp interfejsu do zarządzania Jobami z intuicyjną konfiguracją harmonogramu i automatycznym skanowaniem klas. | [[2025-08-25 Sprint review]] |
| [[2025-08-26]] | Rozpoczęto przepisywanie frontendu ustawień systemowych na React, zachowując pełną kompatybilność wsteczną i możliwość powrotu do starej wersji. | [[2025-08-26 Notatka projektowa - AMODIT UI]] |
| [[2025-09-04]] | Zgłoszenie hotfixa dotyczącego problemu z automatyczną zmianą koloru interfejsu po aktualizacji, potencjalnie związanego z migracją ustawień do React. | [[2025-09-04 Rada architektów]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Dokumentacja zewnętrzna:** [do uzupełnienia]
- **Umowa z klientem:** [do uzupełnienia]
- **Inicjatywa w backlogu:** [do uzupełnienia]

---

## 7. PODPROJEKTY

| Podprojekt | Status | MVP | Opis |
|------------|--------|-----|------|
| [Integracje-rozszerzenia](./Integracje-rozszerzenia/) | 🟡 W analizie | MVP1 Q4 2025 | Konfiguracja integracji z zewnętrznymi systemami - intuicyjny interfejs pokazujący tylko skonfigurowane integracje |
| [Zadania-jobs](./Zadania-jobs/) | 🛠️ W realizacji | - | Zarządzanie zadaniami cyklicznymi (usługi asynchroniczne) - widok zadań, konfigurator harmonogramu cron |

**Uwaga:** Każdy podprojekt ma własny katalog i pełną dokumentację Project Canvas.

---

## X. ARCHITEKTURA TECHNICZNA

### Technologie
- Frontend: React
- Backend: [do uzupełnienia]
- Baza danych: Tabela `Parameters` (bez zmian w schemacie)

### Szczegóły techniczne

**Backend:**
- Tabela `Parameters` pozostaje bez modyfikacji
- Nowe endpointy do komunikacji z Frontendem

**Frontend:**
- Interfejs w Reactcie
- Kompatybilność wsteczna: istniejące konfiguracje klientów muszą pozostać widoczne

**Rozróżnienie integracji vs modułów:**
- Integracje: połączenia z zewnętrznymi systemami (np. KSeF, OpenAI, Biała Lista, VIES, kursy walut)
- Moduły: funkcjonalności systemu (np. "Raporty zaawansowane") - w licencji, nie w zakładce integracji
