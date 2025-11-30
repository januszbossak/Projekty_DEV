# Project Canvas: Zmienne globalne (Źródła danych Static)

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-09-04
**Klient:** WIM
**Data rozpoczęcia:** 2025-06-26

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead** | Damian Kamiński | Projektowanie interfejsu |
| **Deweloper** | Anna Skupińska | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Brak w AMODIT odpowiednika "zmiennych globalnych" (np. pula dni urlopowych, budżet, stany magazynowe), które można by dynamicznie i transakcyjnie modyfikować z poziomu wielu różnych procesów. Używanie do tego celu rejestrów (spraw) jest nieefektywne i "ciężkie", a statyczne źródła danych pozwalały tylko na odczyt.

### Cel biznesowy
Dostarczenie spójnego i wydajnego mechanizmu do zarządzania danymi współdzielonymi między procesami (np. budżety, limity, stany magazynowe, rezerwacje). Umożliwienie pełnej automatyzacji procesów, które opierają się na dynamicznie zmieniających się danych globalnych, z zapewnieniem kontroli dostępu i audytowalności.

### Cel techniczny
Rozbudowa istniejących źródeł danych typu "Static" o pełną obsługę operacji **CRU** (Create, Read, Update) bezpośrednio z poziomu silnika reguł. Implementacja mechanizmów zabezpieczających, takich jak kontrola współbieżności (optimistic locking), ACL i szczegółowy audyt zmian.

### Metryka sukcesu
- Użytkownik może zdefiniować i zarządzać strukturą źródła "Static" (dodawać kolumny) bez importu plików.
- Nowe funkcje reguł (`SourceGet`, `SourceSet`, `SourceAddRow`, `SourceFind`) pozwalają na pełną manipulację danymi.
- Mechanizm kontroli współbieżności zapobiega niespójności danych przy jednoczesnych zapisach.
- System obsługuje scenariusze biznesowe (np. wniosek urlopowy, wydanie z magazynu) w sposób transakcyjny i audytowalny.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-06-26 | Funkcjonalność zostanie zaimplementowana poprzez rozbudowę istniejącego typu źródeł danych "Static". | Wykorzystanie istniejącej, sprawdzonej infrastruktury minimalizuje ryzyko i zapewnia kompatybilność wsteczną. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-07-07]] | Wprowadzenie flagi `IsRuleManaged` blokującej import z Excela dla źródeł zarządzanych przez reguły. | Zapobiega to przypadkowemu nadpisaniu i utracie danych, które są dynamicznie modyfikowane przez aktywne procesy. | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-07-07]] | Wprowadzenie mechanizmu kontroli współbieżności (Optimistic Locking) z użyciem `rowversion` (SQL Server) lub licznika wersji. | Zapewnia integralność danych w scenariuszach, gdzie wiele procesów może próbować jednocześnie zmodyfikować ten sam rekord (np. ten sam budżet). | - |
| ADR-004 | ✅ Zatwierdzone | [[2025-07-07]] | Wprowadzenie czteropoziomowego systemu uprawnień (ACL): READ, WRITE, CREATE, ADMIN. | Umożliwia granularną kontrolę nad tym, które procesy lub użytkownicy mogą odczytywać, modyfikować, tworzyć dane lub zarządzać strukturą źródła. | - |
| ADR-005 | ✅ Zatwierdzone | [[2025-07-07]] | Wprowadzenie szczegółowego audytu i logowania wszystkich operacji CRUD. | Jest to kluczowe dla śledzenia zmian w krytycznych danych biznesowych, diagnostyki problemów i zapewnienia zgodności. | - |
| ADR-006 | ⏸️ Odroczone | [[2025-09-04]] | Prace nad interfejsem do definiowania źródeł typu `dynamic form` i ich kolumn zostają przeniesione na kolejny sprint. | Priorytetem są prace dla klienta WIM, a Ania Skupińska, która miała się tym zająć, wspiera obecnie Filipa Liwińskiego przy matrycy uprawnień. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji
Rozbudowa źródeł danych o typ Static jest w fazie implementacji.

### Główne ryzyka
| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Wysokie]** Niespójność danych przy konkurencyjnym zapisie z wielu procesów | Średnie | Wysoki | Implementacja mechanizmu Optimistic Locking, który wykryje konflikt i pozwoli na ponowienie operacji. | Tech Lead |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: "Źródła danych Static z pełnym CRUD i zabezpieczeniami" (Status: W realizacji)
**Cel:** Dostarczenie kompletnego i bezpiecznego mechanizmu do zarządzania zmiennymi globalnymi, który może być używany w krytycznych procesach biznesowych.

**Definicja ukończenia (DoD):**
- Użytkownik może zarządzać strukturą źródła "Static" (dodawać kolumny) z poziomu UI.
- Funkcje reguł `SourceGet`, `SourceSet`, `SourceAddRow`, `SourceFind` są w pełni zaimplementowane i udokumentowane.
- Źródła zarządzane przez reguły są chronione przed importem z pliku Excel.
- Mechanizm Optimistic Locking działa i zapobiega "zgubionym aktualizacjom".
- Uprawnienia ACL są weryfikowane przed każdą operacją.
- Wszystkie zmiany są logowane w audycie.

**Funkcjonalności:**

#### Zarządzanie strukturą
- [ ] UI do dodawania nowych kolumn (VARCHAR, DECIMAL, DATETIME, INT, BOOLEAN) do istniejących źródeł 'Static'.
- [ ] Flaga `IsRuleManaged` w ustawieniach źródła, blokująca import z Excela.

#### Funkcje w silniku reguł
- [x] `SourceGet(source, key, column)` - do odczytu całego wiersza lub pojedynczej komórki.
- [x] `SourceSet(source, key, column, value)` lub `SourceSet(source, key, {dict})` - do aktualizacji danych.
- [x] `SourceAddRow(source, {dict})` lub `SourceAddRow(source, key)` - do dodawania nowych wierszy.
- [x] `SourceFind(source, query, limit)` - do wyszukiwania danych.

#### Zabezpieczenia
- [ ] Implementacja Optimistic Locking (np. `rowversion`).
- [ ] Sprawdzanie uprawnień (READ, WRITE, CREATE, ADMIN) przed wykonaniem operacji.
- [ ] Logowanie wszystkich operacji CRUD do audytu ze szczegółami zmian.
- [ ] Walidacja typów danych przy zapisie.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-04]] | Decyzja o odroczeniu prac nad interfejsem dla `dynamic form` na kolejny sprint. | [[2025-09-04 Rada architektów]] |
| [[2025-07-07]] | Uszczegółowienie projektu. Dodano definicję funkcji CRUD w regułach (`SourceGet/Set/Add/Find`), mechanizmy zabezpieczeń (Optimistic Locking, ACL, Audyt, flaga `IsRuleManaged`) oraz możliwość zarządzania strukturą źródła z UI. | [[2025-07-07 Odczyt i zapis do Źródła danych typu static]] |
| 2025-06-26 | Utworzenie projektu - rozbudowa Zewnętrznych Źródeł Danych o typ "Static" / "Local". | [[Notatki/Rada architektów/2025-06-26 Rada architektów\|Rada Architektów 2025-06-26]] |
