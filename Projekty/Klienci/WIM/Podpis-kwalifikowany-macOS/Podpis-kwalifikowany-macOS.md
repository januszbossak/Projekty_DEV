# Project Canvas: Podpis kwalifikowany macOS

**Status:** 🟡 W realizacji (Faza: MVP - wstrzymany)
**Ostatnia aktualizacja:** 2025-10-20
**Klient:** WIM
**Data rozpoczęcia:** 2025-08-25

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Tech Lead / Deweloper** | | |
| **Tester** | | |
| **Opiekun handlowy** | | |
| **Kontakt u klienta** | | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Użytkownicy pracujący na systemie macOS **nie mogą składać podpisów kwalifikowanych** w module Trust Center AMODIT. Obecna aplikacja do podpisywania działa wyłącznie na Windows, co zmusza użytkowników macOS do szukania obejść lub korzystania z innych komputerów.

### Cel biznesowy
Umożliwienie użytkownikom macOS pełnego korzystania z Trust Center bez konieczności posiadania dostępu do Windows. Zwiększenie dostępności AMODIT dla firm z ekosystemem Apple.

### Cel techniczny
Stworzenie **natywnej aplikacji macOS** wspierającej głównych polskich dostawców podpisów kwalifikowanych (Szafir, mSzafir, SimplySign, PWPW) z pełną integracją z Trust Center.

### Metryka sukcesu
Użytkownik macOS może podpisać dokument w Trust Center **w < 30 sekund** bez dodatkowej konfiguracji (auto-detekcja certyfikatów).

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Integracja z Trust Center
Aplikacja musi być **w pełni kompatybilna** z istniejącym przepływem Trust Center. Żadnych zmian w backend Trust Center dla obsługi macOS.

### Zasada 2: Bezpieczeństwo certyfikatów
Dostęp do kluczy prywatnych **wyłącznie przez standardowe API macOS** (Keychain, PKCS#11). Brak własnych mechanizmów zarządzania certyfikatami.

### Zasada 3: Dystrybucja
Aplikacja musi być **self-contained** - bez wymagania instalacji runtime .NET przez użytkownika końcowego.

### Zasada 4: Zgodność z walidatorami
Każdy podpis musi przejść **walidację przez oficjalny walidator Unii Europejskiej** (DSS).

---

## Decyzje architektoniczne (ADR)

| ID | Data | Decyzja | Uzasadnienie |
|----|------|---------|--------------|
| ADR-001 | 2025-08-25 | Framework: .NET MAUI | Udało się pokonać barierę dostępu do certyfikatów na macOS; wspólny kod z wersją Windows |
| ADR-002 | 2025-08-25 | Dystrybucja: Self-contained build | Eliminacja wymagań instalacyjnych dla użytkownika; lepsze UX |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠 MVP - Rozwój

**PoC zakończony (2025-08-25):**
- ✅ Udowodniono możliwość dostępu do certyfikatów macOS przez .NET MAUI
- ✅ Pozytywna walidacja podpisów przez walidator EU
- ✅ Testy z trzema głównymi dostawcami

**Trwa praca nad:**
- Prace **tymczasowo wstrzymane** na rzecz e-Doręczeń (priorytet)
- Testowanie wykrywania podpisów Szafir
- Przebudowa UI (spójność z wersją Windows)

**Blokery:**
- Adrian musi pozyskać podpis SimpleSign do kontynuacji testów
- Brak centralnego dostępu do zestawu podpisów testowych i komputera Mac dla zespołu

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja |
|--------|-------------------|-------|-----------|
| **[Wysokie]** PWPW nie udostępni środowiska testowego | Średnie | Wysoki | Przygotować fallback - opóźnione wsparcie PWPW do kolejnej wersji |
| **[Średnie]** Zmiany w bibliotekach dostawców (Szafir, SimplySign) | Niskie | Średni | Monitoring API dostawców; testy regresyjne przy każdym update |
| **[Niskie]** Apple zmieni politykę sandboxingu aplikacji | Bardzo niskie | Wysoki | Monitoring Apple Developer News; alternatywnie: notaryzacja zamiast pełnego sandboxu |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 PoC: "Proof of Concept" (Ukończony: Q3 2025)

**Cel:** Udowodnić techniczną wykonalność dostępu do certyfikatów macOS.

**Zrealizowane:**
- [x] Działający prototyp aplikacji
- [x] Dostęp do certyfikatów na macOS z .NET MAUI
- [x] Build jako self-contained
- [x] Testy z dostawcami:
  - [x] Szafir (podpis fizyczny na czytniku)
  - [x] mSzafir (podpis chmurowy)
  - [x] SimplySign
- [x] **Walidacja przez oficjalny walidator Unii Europejskiej - POZYTYWNA ✅**

---

### 📦 MVP1: "Podstawowe podpisywanie w Trust Center" (Plan: Q4 2025)

**Cel:** Umożliwić użytkownikom macOS podpisywanie dokumentów w Trust Center bez manualnej konfiguracji.

**Definicja ukończenia (DoD):**
- Użytkownik może podpisać dokument **bez ręcznego wskazywania ścieżek** do certyfikatów
- UI jest **wizualnie spójny** z wersją Windows
- Aplikacja **automatycznie wykrywa** zainstalowanych dostawców (Szafir, SimplySign)

**Funkcjonalności:**
- [x] Automatyczne wykrywanie certyfikatów i bibliotek (Szafir, SimplySign) ✅ *Sprint 2025-10-06*
- [x] Obsługa wielu kluczy prywatnych na jednej karcie kryptograficznej ✅ *Sprint 2025-10-06*
- [ ] Przebudowa UI - czytelniejszy, spójny z wersją Windows
- [ ] Wyświetlanie: **nazwa właściciela**, **wystawca**, **data ważności** (zamiast danych technicznych certyfikatu)
- [ ] Wsparcie dla wszystkich głównych dostawców podpisów w Polsce

**Cel do końca października 2025:** Obsługa 3 głównych podpisów (Szafir, SimplySign, PWPW)

**Dalsze kroki:**
- [ ] Adrian: pozyskać podpis SimpleSign do testów
- [ ] Rozwiązać problem centralnego dostępu do podpisów testowych i Mac dla zespołu
- [ ] Testy z certyfikatami PWPW (gdy będzie możliwość techniczna)

---

### 📦 Backlog (przyszłe wersje)

**MVP2: "Podpisywanie z raportów"** (Priorytet: Niski)
- Możliwość składania podpisów bezpośrednio z poziomu raportów AMODIT
- Wymaga integracji z modułem raportowym

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-25 | Prototyp gotowy, testy pozytywne z trzema dostawcami | Sprint review 2025-08-25 |
| 2025-10-06 | Automatyczne wykrywanie certyfikatów, obsługa wielu kluczy prywatnych | Sprint review 2025-10-06 |
| 2025-10-20 | Prace wstrzymane na rzecz e-Doręczeń. Trwa testowanie Szafir. Blokery: brak SimpleSign i centralnego dostępu do podpisów testowych | Sprint review 2025-10-20 |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [link do repo]
- **Trust Center (staging):** [link]
- **Walidator EU DSS:** https://ec.europa.eu/digital-building-blocks/DSS/webapp-demo/validation
- **Dokumentacja .NET MAUI macOS:** [link]
- **Kontakt techniczny - Szafir:** [email/portal]
- **Kontakt techniczny - SimplySign:** [email/portal]
