# Project Canvas: Komunikator (AMODIT Talk)

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-10-20
**Klient:** WIM
**Data rozpoczęcia:** 2025-08-12

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | [do uzupełnienia] | |
| **Deweloper** | [do uzupełnienia] | |
| **Tester** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

AMODIT nie posiada wbudowanego modułu komunikacji wewnętrznej. Użytkownicy muszą korzystać z zewnętrznych narzędzi do szybkiej wymiany informacji w kontekście spraw i procesów, co fragmentuje komunikację i utrudnia śledzenie historii ustaleń.

### Cel biznesowy

Dostarczenie zintegrowanego komunikatora wewnętrznego (AMODIT Talk), który umożliwi szybką, bezpieczną komunikację między użytkownikami systemu z pełną historią rozmów i integracją z kontekstem AMODIT.

### Cel techniczny

Stworzenie skalowalnej architektury komunikatora działającej zarówno w środowisku On-Premises jak i chmurowym (SaaS), z bezpiecznym uwierzytelnianiem opartym na tokenach JWT i szyfrowaniem wiadomości.

### Metryka sukcesu

- Użytkownicy mogą rozpocząć konwersację w **< 3 kliknięcia**
- Historia rozmów jest **trwale zapisana** i przeszukiwalna
- Komunikator działa **bez opóźnień** w środowisku z Load Balancingiem

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Osobna aplikacja SignalR

Komunikator działa jako **osobna aplikacja** wykorzystująca SignalR, aby nie obciążać głównej instancji AMODIT. To kluczowe dla wydajności przy dużej liczbie jednoczesnych połączeń.

**Uzasadnienie:** SignalR utrzymuje trwałe połączenia WebSocket, które generowałyby zbyt duże obciążenie w głównym procesie aplikacji.

### Zasada 2: Automatyczne wykrywanie trybu pracy

System musi **automatycznie wykrywać** czy działa w trybie lokalnym (On-Premises) czy chmurowym (SaaS) i odpowiednio dostosowywać konfigurację połączeń.

**Uzasadnienie:** Jeden codebase dla obu środowisk eliminuje koszty utrzymania dwóch wersji i redukuje ryzyko rozbieżności funkcjonalnych.

### Zasada 3: Dynamiczny connection string w chmurze

W wersji chmurowej connection string oraz konfiguracja są **pobierane dynamicznie** z serwisu centralnego na podstawie identyfikatora organizacji (tenant), zamiast być wpisane na sztywno.

**Uzasadnienie:** Architektura multi-tenant wymaga izolacji danych między organizacjami bez konieczności osobnych instancji aplikacji.

---

## Decyzje architektoniczne (ADR)

| ID | Data | Decyzja | Uzasadnienie |
|----|------|---------|--------------|
| ADR-001 | 2025-08-12 | Komunikator jako osobna aplikacja SignalR | Izolacja od głównej instancji AMODIT, brak obciążenia core systemu |
| ADR-002 | 2025-08-12 | Uwierzytelnianie przez OTP + JWT (nie token w URL) | Bezpieczeństwo - kod jednorazowy wymieniany na token przez API backendowe |
| ADR-003 | 2025-08-12 | Kody OTP w bazie danych (nie RAM) | Obsługa środowisk z Load Balancingiem - każdy serwer ma dostęp do tych samych kodów |
| ADR-004 | 2025-08-12 | Osobne tabele komunikatora + migracje EF | Niezależność od rdzenia AMODIT, wykorzystanie `__EFMigrationsHistory` |
| ADR-005 | 2025-08-12 | Klucze szyfrowania per-tenant w chmurze | Izolacja bezpieczeństwa między organizacjami, klucze w bazie lub Vault |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji (stabilizacja MVP1)

Komunikator jest w fazie aktywnego rozwoju. Główne funkcjonalności zostały zaimplementowane, trwa praca nad spójnością wizualną i finalnymi poprawkami przed wdrożeniem produkcyjnym.

**Ukończono:**
- ✅ Otwarcie jako nakładka lub osobna karta przeglądarki
- ✅ Infinite scroll - automatyczne doczytywanie starszych wiadomości
- ✅ Wskaźnik "rozmówca pisze"
- ✅ Zapis niedokończonych wiadomości w localStorage
- ✅ Wyszukiwanie użytkowników z paginacją
- ✅ Konwersacje prywatne i grupowe
- ✅ Wzmiankowanie użytkowników (@)
- ✅ Ujednolicony wygląd: awatary, czcionki, układ okna

**Trwa praca nad:**
- Breadcrumbs w interfejsie
- Automatyczne określanie typu konwersacji
- ✅ Tworzenie konwersacji na podstawie grup MOD - **zrealizowane** (2025-10-20)

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja |
|--------|-------------------|-------|-----------|
| **[Średnie]** Przechowywanie OTP w RAM w środowisku LB | Średnie | Wysoki | ADR-003: Przeniesienie do bazy danych - realizacja w MVP1 |
| **[Niskie]** Rozbieżność kodu On-Premises vs Cloud | Niskie | Średni | Jeden codebase z automatycznym wykrywaniem trybu |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Stabilizacja On-Premises i bezpieczeństwo (Status: W realizacji)

**Cel:** Uruchomienie działającej, bezpiecznej wersji komunikatora w środowisku lokalnym klienta, eliminując błędy architektury uwierzytelniania.

**Zakres funkcjonalny:**
- [x] Otwarcie jako nakładka lub osobna karta przeglądarki
- [x] Infinite scroll - automatyczne doczytywanie starszych wiadomości
- [x] Wskaźnik "rozmówca pisze"
- [x] Zapis niedokończonych wiadomości w localStorage
- [x] Wyszukiwanie użytkowników z paginacją
- [x] Konwersacje prywatne i grupowe
- [x] Wzmiankowanie użytkowników (@)
- [x] Ujednolicony wygląd (awatary, czcionki)
- [ ] Breadcrumbs w interfejsie
- [ ] Automatyczne określanie typu konwersacji
- [x] Tworzenie konwersacji na podstawie grup MOD ✅ *Sprint 2025-10-20*
  - Uprawnienia automatycznie synchronizowane ze składem grupy MOD
  - Dodawanie/usuwanie członków grupy = aktualizacja uprawnień konwersacji

**Zakres bezpieczeństwa:**
- [ ] Implementacja wymiany kodu jednorazowego na token JWT (eliminacja tokena z URL)
- [ ] Przeniesienie zapisu kodów OTP z pamięci RAM do bazy danych
- [ ] Integracja z kontrolerem użytkowników AMODIT
- [ ] Szyfrowanie wiadomości z kluczem z konfiguracji

**Zakres jakościowy:**
- [ ] Ujednolicenie nazewnictwa (Komunikator/Czat/Konwersacja/AMODIT Talk)
- [ ] Spójność wizualna z resztą systemu
- [ ] Weryfikacja zabezpieczeń XSS

**Planowana data:** Q4 2025

---

### 📦 MVP2: Dostosowanie do chmury SaaS (Status: Planowany)

**Cel:** Umożliwienie wdrażania komunikatora w środowisku wielodostępnym (multi-tenant).

**Zakres:**
- [ ] Automatyczne wykrywanie trybu pracy (lokalny vs chmurowy)
- [ ] Dynamiczne pobieranie connection string na podstawie identyfikatora organizacji
- [ ] Mechanizm zarządzania kluczami szyfrowania per-tenant
- [ ] Pełna separacja danych między organizacjami
- [ ] Przechowywanie kluczy w bezpiecznym magazynie (Vault)

**Planowana data:** 2026

---

### 📦 Backlog (przyszłe wersje)

**Punkty do dalszej dyskusji:**
1. **Przegląd kodu przez architekta** - Piotr musi przejrzeć kod i repozytorium aby zatwierdzić ostateczny kształt rozwiązań technicznych
2. **Miejsce zapisu kodów OTP** - Należy wskazać konkretną tabelę (sugerowane: `UserActivityLog` lub tabele powiadomień)
3. **Integracja z Copilotem** - Koncepcja: Copilot jako "użytkownik" w czacie, wymaga osobnego planowania

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-12 | Ustalenie architektury: osobna aplikacja SignalR, JWT/OTP, model bazy danych | Notatka projektowa 2025-08-12 |
| 2025-08-12 | Definicja MVP1 (On-Premises) i MVP2 (Cloud/SaaS) | Notatka projektowa 2025-08-12 |
| 2025-08-25 | Główne funkcjonalności zaimplementowane | Sprint review 2025-08-25 |
| 2025-09-22 | Kilkanaście poprawek zrealizowanych, prezentacja odłożona | Sprint review 2025-09-22 |
| 2025-10-06 | Ujednolicony wygląd, konwersacje prywatne/grupowe | Sprint review 2025-10-06 |
| 2025-10-20 | Konwersacje oparte o grupy MOD z automatyczną synchronizacją uprawnień | Sprint review 2025-10-20 |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Backlog:** [do uzupełnienia]

---

## Powiązane projekty

- **Copilot** - `moduly/Copilot-Baza-wiedzy-AI` - potencjalna integracja Copilota jako "użytkownika" czatu
