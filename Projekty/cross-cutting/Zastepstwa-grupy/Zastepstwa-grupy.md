# Project Canvas: Zastępstwa w grupach

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-08-12
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-08-12
**Budżet/Czas:** [do uzupełnienia]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead** | [do uzupełnienia] | Architektura, Code Review |
| **Deweloper** | Piotr Buczkowski | Implementacja |
| **Tester** | [do uzupełnienia] | |
| **Opiekun handlowy** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Wykryto niespójność między starym a nowym mechanizmem zastępstw dotyczącą obsługi zastępstw za grupy. W starym mechanizmie, jeśli użytkownik jest zastępcą osoby należącej do grupy, widzi również sprawy przypisane do tej grupy. W nowym mechanizmie tego nie ma – zastępca widzi tylko sprawy przypisane bezpośrednio do osoby, którą zastępuje, ale nie sprawy przypisane do grup, do których ta osoba należy. Niespójność prowadzi do błędów logicznych i problemów wydajnościowych.

### Cel biznesowy

Ujednolicenie działania mechanizmów zastępstw dla grup użytkowników oraz wprowadzenie elastycznej konfiguracji, która umożliwi administratorom kontrolę nad tym mechanizmem. Docelowo oba mechanizmy powinny działać tak samo.

### Cel techniczny

Dodanie obsługi zastępstw za grupy jednoosobowe domyślnie w nowym mechanizmie oraz wprowadzenie parametru "Uwzględnij zastępstwa dla tej grupy" dla grup wieloosobowych, umożliwiającego jawne włączenie mechanizmu zastępstw dla dowolnej grupy.

### Metryka sukcesu

- Zastępca widzi sprawy przypisane do grup osoby zastępowanej (dla grup jednoosobowych domyślnie, dla wieloosobowych przez parametr)
- Oba mechanizmy zastępstw działają tak samo
- Administrator może skonfigurować zastępstwa dla grupy w < 1 minucie

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Kompatybilność wsteczna

Wszystkie zmiany muszą działać bez wpływu na istniejące mechanizmy zastępstw i konfiguracje klientów.

**Uzasadnienie:** Istniejące instalacje AMODIT nie mogą zostać zablokowane po wprowadzeniu zmian.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-08-12 | Obsługa zastępstw za grupy jednoosobowe domyślnie w obu mechanizmach (gdzie grupa = rola) | Najbardziej sensowny przypadek użycia - grupy jednoosobowe definiujące role (np. Dyrektor Finansowy, RODO) wymagają zastępstw | - |
| ADR-002 | ✅ Zatwierdzone | 2025-08-12 | Parametr "Uwzględnij zastępstwa dla tej grupy" dla grup wieloosobowych | Elastyczne rozwiązanie dla grup wieloosobowych - pozwala na jawne włączenie mechanizmu zastępstw dla dowolnej grupy (np. HR z 20 osobami - nie potrzebuje zastępstw, bo zawsze ktoś z grupy się zajmie) | - |
| ADR-003 | ⏸️ Odroczona | 2025-08-12 | Obsługa zastępstw za grupy w nowym mechanizmie (jak w starym) - pełna implementacja | Wymaga kilku godzin pracy, wymaga przemyślenia | - |
| ADR-004 | ❌ Odrzucone | 2025-08-12 | Brak obsługi zastępstw za grupy w obu mechanizmach | Grupy jednoosobowe (role) wymagają zastępstw | - |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta
- ⏸️ **Odroczona** - decyzja odroczona na później

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji

Projekt jest w fazie aktywnego rozwoju. Trwa implementacja obsługi zastępstw za grupy jednoosobowe oraz parametru dla grup wieloosobowych.

**Ukończono:**
- ✅ Ustalenie architektury i podejścia technicznego

**Trwa praca nad:**
- Dodanie obsługi zastępstw za grupy jednoosobowe domyślnie w nowym mechanizmie
- Dodanie parametru "Uwzględnij zastępstwa dla tej grupy" dla grup wieloosobowych

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Średnie]** Niespójność funkcjonalna między starym a nowym mechanizmem | Średnie | Średni | Ujednolicenie logiki - docelowo oba mechanizmy powinny działać tak samo (wymaga kilku godzin pracy) | Tech Lead |
| **[Średnie]** Problemy dla użytkowników korzystających ze starego mechanizmu przy przejściu na nowy | Średnie | Średni | Zapewnienie kompatybilności wstecznej - oba mechanizmy działają równolegle | Tech Lead |
| **[Niskie]** Problemy wydajnościowe przy obsłudze zastępstw za grupy w nowym mechanizmie | Niskie | Niski | Nowy mechanizm wykorzystuje 2 zapytania (`CASE...` dla spraw przypisanych do użytkownika lub jego grup `UNION` z działaniami kategorii, gdzie dozwolone zastępstwo) | Tech Lead |

---

### Punkty wymagające decyzji (w fazie analizy)

**Implementacja:**
- [ ] Czy dodać nową kolumnę do tabeli grup, czy można to obsłużyć bezpośrednio w SQL (np. przez sprawdzenie liczby członków grupy)?
- [ ] Jak będzie wyglądał interfejs do ustawiania parametru "Uwzględnij zastępstwa dla tej grupy"?

**Architektura:**
- [ ] Czy docelowo przejść całkowicie na nowy mechanizm zastępstw?

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Grupy jednoosobowe + konfiguracja (Plan: [do uzupełnienia])

**Cel:** Ujednolicić działanie zastępstw i dać administratorom kontrolę nad tym mechanizmem. Zastępca widzi sprawy przypisane do grup osoby zastępowanej dla grup jednoosobowych domyślnie oraz dla grup wieloosobowych przez parametr.

**Definicja ukończenia (DoD):**
- Zastępca widzi sprawy przypisane do grup jednoosobowych osoby zastępowanej (gdzie grupa = rola)
- Administrator może włączyć zastępstwa dla grupy wieloosobowej przez parametr "Uwzględnij zastępstwa dla tej grupy"
- Oba mechanizmy zastępstw działają tak samo w zakresie obsługi grup

**Funkcjonalności:**

#### Obsługa grup jednoosobowych
- [ ] Automatyczna obsługa zastępstw dla grup jednoosobowych domyślnie w nowym mechanizmie
- [ ] Grupy jednoosobowe (gdzie grupa = rola, np. Dyrektor Finansowy, RODO) domyślnie uwzględniają zastępstwa w obu mechanizmach

#### Konfiguracja dla grup wieloosobowych
- [ ] Parametr "Uwzględnij zastępstwa dla tej grupy" dla grup wieloosobowych
- [ ] Interfejs do ustawiania parametru (wymaga interfejsu i kolumny w bazie lub logiki SQL)
- [ ] Możliwość jawnego włączenia mechanizmu zastępstw dla dowolnej grupy niezależnie od liczby członków

#### Ujednolicenie mechanizmów
- [ ] Ujednolicenie logiki starego i nowego mechanizmu (docelowo oba mechanizmy powinny działać tak samo - wymaga kilku godzin pracy)

**Poza zakresem MVP (Out of Scope):**
- Pełna implementacja obsługi zastępstw za grupy w nowym mechanizmie (jak w starym) - odroczona, wymaga kilku godzin pracy i przemyślenia

**Planowana data:** [do uzupełnienia]

**Zadania:**
- **Piotr Buczkowski:** Dodanie obsługi zastępstw za grupy jednoosobowe domyślnie w nowym mechanizmie
- **Piotr Buczkowski:** Dodanie parametru "Uwzględnij zastępstwa dla tej grupy" dla grup wieloosobowych (wymaga interfejsu i kolumny w bazie lub logiki SQL)

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Pełna implementacja obsługi zastępstw za grupy w nowym mechanizmie (jak w starym) - wymaga kilku godzin pracy (Priorytet: Średni)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-12 | Utworzenie projektu - ustalenie rozwiązania dwuetapowego: obsługa zastępstw za grupy jednoosobowe domyślnie oraz parametr dla grup wieloosobowych | [[Notatki/Rada architektów/2025-08-12 Rada architektów|Rada Architektów 2025-08-12]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Dokumentacja zewnętrzna:** [do uzupełnienia]
- **Umowa z klientem:** [do uzupełnienia]
- **Inicjatywa w backlogu:** [do uzupełnienia]

