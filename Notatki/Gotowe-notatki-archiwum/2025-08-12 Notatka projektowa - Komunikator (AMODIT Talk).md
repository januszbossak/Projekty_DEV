# Notatka projektowa – 2025-08-12 – Komunikator (AMODIT Talk)

> 🛡️ Notatka zweryfikowana i zmapowana (Codex Review) w dniu 2025-12-03

**Data:** 2025-08-12
**Temat główny:** Architektura, uwierzytelnianie i model danych modułu Komunikator (AMODIT Talk)

**Powiązane projekty:**
- [[Klienci/WIM/Komunikator/README|Komunikator (AMODIT Talk)]] – funkcjonalności 1, 2, 3, 4, 5, 6, 7, 8

---

## 1. Architektura komunikatora – osobna aplikacja vs część AMODIT

**Projekt:** `Klienci/WIM/Komunikator`
**Komponent:** Architektura systemu

### Cel i problem

Komunikator został zaimplementowany jako osobna aplikacja wykorzystująca SignalR, jednak pojawiły się pytania o sensowność takiego podejścia oraz kompatybilność z wymogami środowiska chmurowego (SaaS). Obecna implementacja działa dobrze dla instalacji on-premises, ale wymaga dopracowania dla środowiska chmurowego z wieloma organizacjami (multi-tenant).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Osobna aplikacja SignalR | Komunikator jako osobna aplikacja, nie obciąża głównej instancji AMODIT | ✅ Wybrana – izolacja od głównego systemu, lepsza wydajność przy wielu połączeniach |
| Część AMODIT | Komunikator jako moduł wbudowany w AMODIT | ❌ Odrzucona – SignalR obciążałby główną instancję, problemy z wydajnością |
| Tylko dla firmy (on-premises) | Ograniczenie komunikatora tylko do instalacji lokalnych | ⏸️ Odroczona – docelowo musi działać i w chmurze i on-premises |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Ustalono kontynuację projektu jako osobnej aplikacji SignalR. Komunikator pozostaje odrębną aplikacją, ale musi być zaprojektowany tak, aby działał zarówno w środowisku on-premises jak i chmurowym (SaaS) bez konieczności utrzymywania dwóch wersji kodu.

**Szczegóły techniczne:**
- SignalR jako osobna aplikacja – nie obciąża głównej instancji AMODIT
- Automatyczne wykrywanie trybu pracy (lokalny vs chmurowy) przez system
- W wersji chmurowej connection string i konfiguracja pobierane dynamicznie z serwisu centralnego na podstawie identyfikatora organizacji
- Adresy w chmurze mają postać `*.amodit.com`, gdzie gwiazdka to identyfikator organizacji (np. Astrafox Test, Velux)

### Ograniczenia / Poza zakresem

- Komunikator nie będzie promowany jako osobny produkt – jest funkcjonalnością AMODIT, nie konkurencją dla Teams czy Slacka
- Nie będzie używany jako samodzielna aplikacja bez AMODIT-a – zawsze wymaga integracji z systemem

### Punkty otwarte

- Jak dokładnie będzie działać mechanizm automatycznego wykrywania trybu pracy (on-premises vs chmura)?
- Jak będzie wyglądać konfiguracja w środowisku chmurowym z wieloma organizacjami?

---

## 2. Konfiguracja – Connection String i mechanizm pobierania organizacji

**Projekt:** `Klienci/WIM/Komunikator`
**Komponent:** Konfiguracja systemu

### Cel i problem

Obecna konfiguracja komunikatora wymaga sztywnego wpisania Connection Stringa do bazy danych w pliku konfiguracyjnym. W środowisku chmurowym z wieloma organizacjami (multi-tenant) potrzebny jest mechanizm dynamicznego pobierania konfiguracji na podstawie identyfikatora organizacji.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Sztywny Connection String w config | Connection String wpisany bezpośrednio w pliku konfiguracyjnym | ✅ Obecne (on-premises) – działa dla instalacji lokalnych |
| Dynamiczne pobieranie z bazy centralnej | Connection String pobierany z serwisu centralnego na podstawie identyfikatora organizacji | ✅ Docelowe (chmura) – wymagane dla środowiska multi-tenant |
| Connection String do bazy AMODIT | Wykorzystanie istniejącej bazy AMODIT zamiast osobnej bazy | 💡 Propozycja – do rozważenia |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

Ustalono, że:
- W środowisku on-premises: Connection String może być w pliku konfiguracyjnym (`appsettings`)
- W środowisku chmurowym: Connection String będzie pobierany z bazy centralnej (tabela określająca listy organizacji chmurowych)
- System automatycznie wykrywa tryb pracy i odpowiednio pobiera konfigurację

**Szczegóły techniczne:**
- Mechanizm pobierania listy organizacji z bazy centralnej
- Tworzenie tabel w odpowiednich bazach na podstawie organizacji
- W chmurze: parametr określający adresy w formacie `*.amodit.com` (gwiazdka = identyfikator organizacji)
- Connection String może wskazywać na bazę AMODIT (wspólna baza) lub osobną bazę komunikatora

### Punkty otwarte

- Czy Connection String powinien wskazywać na bazę AMODIT czy osobną bazę komunikatora?
- Jak dokładnie będzie działać mechanizm pobierania konfiguracji z bazy centralnej?

---

## 3. Model danych – tabele i nazewnictwo

**Projekt:** `Klienci/WIM/Komunikator`
**Komponent:** Model danych

### Cel i problem

Komunikator wykorzystuje osobne tabele w bazie danych. Pojawiły się pytania o zgodność nazewnictwa kolumn z konwencją AMODIT oraz o potrzebę niektórych tabel (np. Users).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Konwencja AMODIT | Nazwy kolumn zgodne z konwencją AMODIT | ⏸️ Odroczona – zmiana nazw kolumn wymagałaby migracji |
| Konwencja Entity Framework | Nazwy kolumn jak wygenerował Entity Framework | ✅ Obecne – już zaimplementowane |
| Osobne tabele w osobnej bazie | Tabele komunikatora w osobnej bazie danych | ✅ Wybrana – niezależność od rdzenia AMODIT |
| Tabele w bazie AMODIT | Tabele komunikatora w głównej bazie AMODIT | ❌ Odrzucona – lepsza separacja jako osobna aplikacja |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Ustalono, że komunikator będzie korzystał z osobnych tabel w osobnej bazie danych (lub w bazie AMODIT, ale jako osobne tabele). Nazwy kolumn pozostają zgodne z konwencją Entity Framework, ponieważ zmiana wymagałaby migracji i jest już zaimplementowane.

**Szczegóły techniczne:**
- Tabele: `ChatMessages`, `Chat`, `ChatUsers`
- Tabela `LogUsers` (historia migracji Entity Framework) – `__EFMigrationsHistory`
- Tabela `Users` – do rozważenia usunięcia (może nie być potrzebna, jeśli użytkownicy są pobierani z AMODIT)
- Migracje Entity Framework do zarządzania schematem bazy danych

### Ograniczenia / Poza zakresem

- Zmiana nazewnictwa kolumn na konwencję AMODIT – wymagałaby migracji i przepisania kodu

### Punkty otwarte

- Czy tabela `Users` jest potrzebna, czy można ją usunąć i korzystać tylko z danych z AMODIT?
- Czy w przyszłości warto będzie zmienić nazewnictwo kolumn na konwencję AMODIT?

---

## 4. Szyfrowanie wiadomości – klucze szyfrowania

**Projekt:** `Klienci/WIM/Komunikator`
**Komponent:** Bezpieczeństwo

### Cel i problem

Wszystkie wiadomości w komunikatorze są szyfrowane. W środowisku chmurowym z wieloma organizacjami pojawia się pytanie o sposób przechowywania kluczy szyfrowania – czy jeden klucz dla wszystkich, czy osobny klucz per organizacja (tenant).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Jeden klucz dla wszystkich | Wszystkie organizacje używają tego samego klucza szyfrowania | ❌ Odrzucona – brak izolacji bezpieczeństwa między organizacjami |
| Klucz per organizacja (tenant) | Każda organizacja ma swój własny klucz szyfrowania | ✅ Docelowe (chmura) – wymagane dla izolacji bezpieczeństwa |
| Klucz w pliku konfiguracyjnym | Klucz przechowywany w pliku konfiguracyjnym | ✅ Obecne (on-premises) – działa dla instalacji lokalnych |
| Klucz w bazie danych | Klucz przechowywany w bazie danych (kolumna per tenant) | 💡 Propozycja – do rozważenia dla chmury |
| Klucz w Azure Key Vault | Klucz przechowywany w Azure Key Vault (jak w e-Doręczeniach) | 💡 Propozycja – do rozważenia dla chmury |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

Ustalono, że:
- W środowisku on-premises: klucz szyfrowania w pliku konfiguracyjnym
- W środowisku chmurowym: klucz per organizacja (tenant) – wymagana izolacja bezpieczeństwa
- W chmurze klucz może być przechowywany w bazie danych (kolumna per tenant) lub w Azure Key Vault (analogicznie do e-Doręczeń)

**Szczegóły techniczne:**
- Wszystkie wiadomości są szyfrowane przed zapisem do bazy danych
- Klucz w pliku konfiguracyjnym dla on-premises
- W chmurze: osobny klucz dla każdej organizacji (izolacja bezpieczeństwa)

### Punkty otwarte

- Gdzie dokładnie przechowywać klucze szyfrowania w środowisku chmurowym – w bazie danych czy Azure Key Vault?
- Jak będzie wyglądać mechanizm przypisywania kluczy do organizacji?

---

## 5. Uwierzytelnianie – JWT i jednorazowe kody (OTP)

**Projekt:** `Klienci/WIM/Komunikator`
**Komponent:** Bezpieczeństwo / Integracja

### Cel i problem

Komunikator działa jako osobna aplikacja (inna domena/port), co utrudnia współdzielenie ciasteczek sesyjnych oraz obsługę zintegrowanego logowania Windows. Przekazywanie tokena bezpośrednio w URL jest niebezpieczne. Potrzebny jest bezpieczny mechanizm uwierzytelniania użytkowników z systemu AMODIT.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Token JWT w URL | Przekazywanie tokena JWT bezpośrednio w adresie URL | ❌ Odrzucona – niebezpieczne, token dostępny przez 15 minut |
| Ciasteczka sesyjne | Wykorzystanie ciasteczek do współdzielenia sesji | ❌ Odrzucona – problemy z różnymi domenami, trudne do testowania lokalnie |
| JWT przez jednorazowy kod (OTP) | Przekierowanie na AMODIT, generowanie jednorazowego kodu, wymiana na token JWT | ✅ Wybrana – bezpieczne, kod jednorazowy nie jest długotrwały |
| REST API zewnętrzne | Wykorzystanie istniejącego REST API do uwierzytelniania | ⏸️ Odroczona – brak opcji pobrania listy użytkowników w REST API |
| Windows Auth (Integrated) | Wykorzystanie zintegrowanego uwierzytelniania Windows | ✅ Wspierane (on-premises) – działa w odpowiednich miejscach |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Ustalono mechanizm uwierzytelniania przez jednorazowy kod (OTP) wymieniany na token JWT:

1. Użytkownik klika przycisk "Otwórz komunikator" w AMODIT
2. Przekierowanie na AMODIT z endpointem `/JWT Login`
3. AMODIT generuje jednorazowy kod
4. Przekierowanie z powrotem do komunikatora z kodem w Query Stringu
5. Komunikator pobiera kod i wymienia go na token JWT przez endpoint w AMODIT
6. Token JWT jest używany do dalszych żądań

**Szczegóły techniczne:**
- Endpoint AMODIT: `/JWT Login` – generuje jednorazowy kod
- Endpoint AMODIT: `Generate` – wymienia kod na token JWT
- Token JWT zawiera informacje o użytkowniku
- Kod jednorazowy jest aktywny tylko raz (po użyciu staje się nieaktywny)
- Token JWT nie jest przekazywany w URL (tylko kod jednorazowy)
- Obsługa Windows Auth (Integrated) w odpowiednich miejscach (handlery, `Global.asax`)
- Dostęp anonimowy włączony dla endpointów uwierzytelniania

### Ograniczenia / Poza zakresem

- Token JWT nie jest przekazywany bezpośrednio w URL (tylko kod jednorazowy)

### Punkty otwarte

- Jak będzie działać mechanizm w środowisku z Load Balancingiem (farma serwerów) – kody jednorazowe muszą być dostępne dla wszystkich serwerów (patrz temat 6)

---

## 6. Problem z farmą serwerów – przechowywanie kodów jednorazowych

**Projekt:** `Klienci/WIM/Komunikator`
**Komponent:** Architektura / Bezpieczeństwo

### Cel i problem

Obecna implementacja przechowuje jednorazowe kody (OTP) w pamięci RAM. W środowisku z farmą serwerów (Load Balancing) kod wygenerowany na jednym serwerze może być używany na innym serwerze, co spowoduje błąd, jeśli kod jest przechowywany tylko w pamięci lokalnej.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Kody w pamięci RAM | Przechowywanie kodów jednorazowych w pamięci lokalnej serwera | ❌ Odrzucona – nie działa w farmie serwerów |
| Kody w bazie danych | Przechowywanie kodów w bazie danych (wspólnej dla wszystkich serwerów) | ✅ Wybrana – wymagane dla środowisk z Load Balancingiem |
| Kody w wspólnym cache | Przechowywanie kodów w wspólnym cache (Redis, itp.) | 💡 Alternatywa – możliwe rozwiązanie |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Ustalono, że jednorazowe kody (OTP) muszą być przechowywane w bazie danych zamiast w pamięci RAM, aby działać poprawnie w środowisku z farmą serwerów (Load Balancing).

**Szczegóły techniczne:**
- Kody jednorazowe zapisywane w bazie danych (wspólnej dla wszystkich serwerów)
- Możliwe wykorzystanie istniejącej tabeli do przechowywania zaproszeń/powiadomień (z GUID)
- Filtrowanie kodów przez czas (np. tylko z ostatnich 3 godzin) dla wydajności
- Obecna implementacja w pamięci RAM jest tymczasowa i wymaga zmiany

### Punkty otwarte

- Która tabela w bazie AMODIT będzie używana do przechowywania kodów jednorazowych?
- Jak będzie wyglądać mechanizm czyszczenia starych kodów?

---

## 7. Integracja z AMODIT – pobieranie listy użytkowników

**Projekt:** `Klienci/WIM/Komunikator`
**Komponent:** Integracja

### Cel i problem

Komunikator potrzebuje pobierać listę użytkowników z AMODIT. Obecna implementacja korzysta z wewnętrznego kontrolera AMODIT (`UsersController`) przez JWT, ale pojawiły się pytania o wykorzystanie istniejącego REST API zewnętrznego.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Wewnętrzny kontroler przez JWT | Pobieranie użytkowników przez `UsersController` z uwierzytelnianiem JWT | ✅ Obecne – działa, ale wymaga logowania przez JWT |
| REST API zewnętrzne | Wykorzystanie istniejącego REST API do pobierania użytkowników | ⏸️ Odroczona – brak opcji pobrania listy użytkowników w REST API |
| Dodanie endpointu do REST API | Rozszerzenie REST API o możliwość pobrania listy użytkowników | 💡 Propozycja – do rozważenia w przyszłości |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

Obecnie komunikator pobiera listę użytkowników przez wewnętrzny kontroler AMODIT (`UsersController`) z uwierzytelnianiem przez token JWT. W przyszłości warto rozważyć dodanie endpointu do REST API zewnętrznego dla pobierania listy użytkowników.

**Szczegóły techniczne:**
- Endpoint: `UsersController` w AMODIT
- Uwierzytelnianie: token JWT (nie ciasteczka)
- Komunikator korzysta z tego samego kontrolera co AMODIT

### Punkty otwarte

- Czy warto dodać endpoint do REST API zewnętrznego dla pobierania listy użytkowników?
- Jak będzie wyglądać integracja w środowisku chmurowym z wieloma organizacjami?

---

## 8. Proces projektowy – potrzeba akceptacji architektonicznej

**Projekt:** `Klienci/WIM/Komunikator`
**Komponent:** Proces projektowy

### Cel i problem

Komunikator został zaimplementowany bez wcześniejszej akceptacji architektonicznej i dyskusji na Radzie Architektów. Pojawiły się problemy z kompatybilnością z filozofią AMODIT (on-premises vs chmura) oraz z wyborem technologii, które mogły być uniknięte przez wcześniejszą dyskusję.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Kontynuacja bez zmian | Kontynuacja obecnej implementacji bez większych zmian | ⏸️ Odroczona – wymaga dopracowania dla chmury |
| Cofnięcie i przeprojektowanie | Cofnięcie tygodnia pracy i przeprojektowanie zgodnie z filozofią AMODIT | 💡 Rozważane – ostatecznie odrzucone ze względu na postęp prac |
| Kontynuacja z dopracowaniem | Kontynuacja obecnej implementacji z dopracowaniem dla chmury | ✅ Wybrana – wykorzystanie doświadczeń, dopracowanie zgodności |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Ustalono kontynuację projektu z dopracowaniem zgodności z filozofią AMODIT. Projekt powinien był przejść przez akceptację architektoniczną przed rozpoczęciem implementacji, ale ze względu na postęp prac (tydzień implementacji) zdecydowano o kontynuacji z wykorzystaniem doświadczeń i dopracowaniem zgodności.

**Szczegóły techniczne:**
- Projekt powinien przechodzić przez akceptację architektoniczną przed rozpoczęciem implementacji
- Wszystkie projekty powinny być zgodne z filozofią AMODIT (on-premises i chmura)
- Wykorzystanie doświadczeń z tygodnia pracy do dopracowania zgodności

### Ograniczenia / Poza zakresem

- Cofnięcie całej pracy i przeprojektowanie od zera – zbyt kosztowne przy tygodniu pracy

### Punkty otwarte

- Jak zapewnić, że przyszłe projekty będą przechodzić przez akceptację architektoniczną przed rozpoczęciem implementacji?

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: Stabilizacja On-Premises i bezpieczeństwo

**Cel:** Uruchomienie działającej, bezpiecznej wersji komunikatora w środowisku lokalnym klienta, eliminując błędy architektury uwierzytelniania.

**Zakres funkcjonalny:**
- Osobna aplikacja SignalR
- Konwersacje prywatne i grupowe
- Wzmiankowanie użytkowników (@)
- Infinite scroll, wskaźnik pisania

**Zakres bezpieczeństwa:**
- Implementacja wymiany kodu jednorazowego na token JWT (eliminacja tokena z URL)
- Przeniesienie zapisu kodów OTP z pamięci RAM do bazy danych (wymagane dla farmy serwerów)
- Integracja z kontrolerem użytkowników AMODIT
- Szyfrowanie wiadomości z kluczem z konfiguracji

**Planowany termin:** [do ustalenia]

### MVP 2: Wsparcie środowiska chmurowego (SaaS)

**Cel:** Dostosowanie komunikatora do działania w środowisku chmurowym z wieloma organizacjami (multi-tenant).

**Zakres:**
- Dynamiczne pobieranie konfiguracji z bazy centralnej na podstawie identyfikatora organizacji
- Klucze szyfrowania per organizacja (tenant)
- Mechanizm automatycznego wykrywania trybu pracy (on-premises vs chmura)
- Obsługa adresów w formacie `*.amodit.com`

**Planowany termin:** [do ustalenia]

---

## Punkty do dalszej dyskusji (globalne)

- Dokładny mechanizm automatycznego wykrywania trybu pracy (on-premises vs chmura)
- Lokalizacja przechowywania kluczy szyfrowania w środowisku chmurowym (baza danych vs Azure Key Vault)
- Rozszerzenie REST API zewnętrznego o możliwość pobrania listy użytkowników
- Proces akceptacji architektonicznej dla przyszłych projektów – jak zapewnić, że projekty przechodzą przez Radę Architektów przed rozpoczęciem implementacji

