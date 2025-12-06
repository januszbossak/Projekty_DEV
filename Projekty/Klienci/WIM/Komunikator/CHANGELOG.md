# CHANGELOG – Komunikator

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Funkcjonalność

- Opcja tworzenia konwersacji opartej o grupę modów (model)
- Automatyczna synchronizacja uprawnień w komunikatorze na podstawie zmian w grupie
- Planowane dodanie nazwy grupy w interfejsie

---

## 2025-10-06 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Sprint review.md]
**Kategoria:** #Funkcjonalność #Design

- Poprawki wizualne komunikatora (upodobnienie do konwersacji tekstowej, awatary)
- Uproszczenie formy tworzenia konwersacji (prywatne/grupowe), brak ścieżki dla komunikatora

---

## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🚀 Postęp

- **Poprawki wizualne:** realizacja kilkunastu zgłoszeń (stabilizacja MVP).
- **Status:** wersja bliska ostatecznej/stabilnej, pozostało kilka kluczowych elementów wizualnych i 3-4 otwarte zgłoszenia.
- **Plan:** prezentacja wersji stabilnej przewidziana jeszcze w tym tygodniu.

---

## 2025-08-25 - Sprint review

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-08-25 Sprint review|2025-08-25 Sprint review]]

**Kategoria:** #Design #Feedback

**Prezentacja:** Anna Kicior

**Status wdrożenia:**
Komunikator (AMODIT Talk) działa, jest gotowy do odbioru przez WIM. To MVP (wersja minimalna) pozwalająca zaliczyć wymaganie klienta.

**Feedback z demo - do dopracowania:**
- **Ujednolicenie nazewnictwa:** przejrzenie wszystkich ekranów i ujednolicenie nazw (jedna nazwa wszędzie: "komunikator" lub "AMODIT Talk")
- **Dodanie awatarów:** implementacja awatarów użytkowników
- **Limit znaków:** dodanie limitu znaków na pojedynczą wiadomość
- **Ujednolicenie komponentów:** użycie standardowych komponentów AMODIT (np. search)
- **Pełna zgodność WCAG:** dopracowanie zgodności z WCAG dla niewidomych użytkowników
- **Integracja logów:** rozważenie przeniesienia logów do standardowych logów AMODIT lub dodanie linku/przełącznika między logami

**Decyzje:**
- Nazwij to "AMODIT Talk" dla konsystencji marketingowej (będzie używane w chwaleniu się nowym produktem)
- MVP może iść do odbioru, dalsze upiększanie i ulepszanie po akceptacji

**Kontekst biznesowy:**
Realizowane dla WIM - minimalna wersja wystarczająca do zaliczenia wymagania klienta. Pan Piotr Murawski zaakceptował MVP.

---

## 2025-08-12 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Notatka projektowa - Komunikator (AMODIT Talk).md](../../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Notatka%20projektowa%20-%20Komunikator%20(AMODIT%20Talk).md)

**Kategoria:** #Architektura

**1. Architektura komunikatora – osobna aplikacja vs część AMODIT** ✅
- **Wybrana:** Osobna aplikacja SignalR (izolacja od głównego systemu, lepsza wydajność)
- ❌ Odrzucona: Moduł wbudowany w AMODIT (obciążałby główną instancję)
- Musi działać w on-premises i chmurze (SaaS) bez dwóch wersji kodu
- Automatyczne wykrywanie trybu pracy (lokalny vs chmurowy)
- W chmurze: adresy `*.amodit.com` (gwiazdka = ID organizacji)
- **Ograniczenie:** Nie promowany jako osobny produkt, nie konkurencja dla Teams/Slack

**3. Model danych – tabele i nazewnictwo** ✅
- Osobne tabele w osobnej bazie danych (lub w bazie AMODIT jako osobne)
- Tabele: `ChatMessages`, `Chat`, `ChatUsers`, `__EFMigrationsHistory`
- Nazwy kolumn: konwencja Entity Framework (zmiana wymagałaby migracji)
- ⏸️ Do rozważenia: Czy tabela `Users` jest potrzebna (może tylko dane z AMODIT)?

**6. Problem z farmą serwerów – przechowywanie kodów jednorazowych** ✅
- ❌ Kody w pamięci RAM - nie działa w farmie serwerów
- ✅ Kody w bazie danych - wspólne dla wszystkich serwerów (Load Balancing)
- Możliwe wykorzystanie istniejącej tabeli do zaproszeń/powiadomień (GUID)
- Filtrowanie kodów przez czas (np. ostatnie 3h) dla wydajności

**8. Proces projektowy – potrzeba akceptacji architektonicznej** ✅
- Projekt zaimplementowany bez wcześniejszej akceptacji na Radzie Architektów
- ✅ Kontynuacja z dopracowaniem zgodności z filozofią AMODIT
- ❌ Odrzucone: Cofnięcie i przeprojektowanie (zbyt kosztowne przy tygodniu pracy)
- **Wniosek:** Przyszłe projekty powinny przejść przez akceptację architektoniczną przed implementacją

**Kategoria:** #Bezpieczeństwo

**4. Szyfrowanie wiadomości – klucze szyfrowania** 🔍
- Wszystkie wiadomości szyfrowane przed zapisem do bazy
- **On-premises:** Klucz w pliku konfiguracyjnym ✅
- **Chmura:** Klucz per organizacja (tenant) - izolacja bezpieczeństwa
- 💡 Do weryfikacji: Gdzie przechowywać klucze w chmurze (baza danych vs Azure Key Vault)?

**5. Uwierzytelnianie – JWT i jednorazowe kody (OTP)** ✅
- ❌ Odrzucone: Token JWT w URL (niebezpieczne)
- ❌ Odrzucone: Ciasteczka sesyjne (problemy z różnymi domenami)
- ✅ Wybrana: JWT przez jednorazowy kod (OTP)
- **Flow:**
  1. Użytkownik klika "Otwórz komunikator" → przekierowanie do `/JWT Login`
  2. AMODIT generuje jednorazowy kod
  3. Przekierowanie do komunikatora z kodem w Query String
  4. Komunikator wymienia kod na token JWT (endpoint `Generate`)
  5. Token JWT używany do dalszych żądań
- Kod jednorazowy aktywny tylko raz
- Obsługa Windows Auth (Integrated) w on-premises

**Kategoria:** #Funkcjonalność

**2. Konfiguracja – Connection String i mechanizm pobierania organizacji** 🔍
- **On-premises:** Connection String w `appsettings` ✅
- **Chmura:** Dynamiczne pobieranie z bazy centralnej (lista organizacji)
- System automatycznie wykrywa tryb pracy
- 💡 Do weryfikacji: Connection String do bazy AMODIT czy osobnej bazy komunikatora?

**7. Integracja z AMODIT – pobieranie listy użytkowników** 🔍
- **Obecne:** Wewnętrzny `UsersController` przez JWT ✅
- ⏸️ Odroczone: REST API zewnętrzne (brak opcji pobrania listy użytkowników)
- 💡 Propozycja: Rozszerzenie REST API o endpoint dla listy użytkowników

**Kategoria:** #Roadmap

**MVP 1: Stabilizacja On-Premises i bezpieczeństwo**
- Osobna aplikacja SignalR
- Konwersacje prywatne/grupowe, wzmiankowanie (@), infinite scroll
- Wymiana OTP na JWT (eliminacja tokenu z URL)
- Przeniesienie OTP z RAM do bazy danych (farma serwerów)
- Szyfrowanie z kluczem z konfiguracji

**MVP 2: Wsparcie środowiska chmurowego (SaaS)**
- Dynamiczne pobieranie konfiguracji z bazy centralnej (ID organizacji)
- Klucze szyfrowania per organizacja (tenant)
- Automatyczne wykrywanie trybu (on-premises vs chmura)
- Obsługa adresów `*.amodit.com`

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)

**Kategoria:** #Problem

- **Ryzyka zidentyfikowane:**
  - Wydajność: ciągły polling (odpytywanie serwera) przez wiele otwartych kart może zabić serwery
  - Licencje: biblioteki Open Source (np. Matrix) często GPL v3, wymuszałoby udostępnienie kodu AMODIT

**Kategoria:** #Architektura

- **Rozważane alternatywy:**
  - Własna implementacja w AMODIT (rozbudowa komentarzy o real-time) - ⏸️ Odroczona (ryzyko wydajnościowe, duży nakład)
  - Integracja z gotowym rozwiązaniem Open Source (Matrix + iframe/API) - 💡 Propozycja wiodąca (pod warunkiem licencji MIT)
- **Decyzja:** ⏸️ Odroczone - temat "zaparkowany" do czasu zebrania wymagań i znalezienia odpowiedniej technologii (bezpiecznej licencyjnie i wydajnościowo)

---

