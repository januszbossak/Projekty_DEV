# Notatka projektowa - 2025-11-27 - AMODIT AI: MCP i Automatyczna Dokumentacja

**Data:** 2025-11-27
**Temat główny:** Rozbudowa AMODIT Copilot o MCP oraz automatyczne generowanie dokumentacji procesów

---

## 1. MCP (Model Context Protocol) - Integracja z AMODIT Copilot

**Komponent:** AMODIT Copilot / AI

### Cel i problem

AMODIT Copilot ma ograniczone możliwości - obecnie generuje tylko tekst. MCP (Model Context Protocol) pozwala rozszerzyć funkcjonalność Copilota o dodatkowe narzędzia (tools) bez konieczności pisania kodu. Możliwe jest podłączenie zewnętrznych serwerów MCP (zarówno gotowych z internetu, jak i własnych), które dodają nowe możliwości jak generowanie wykresów, dostęp do zewnętrznych API, obsługa pogody, przeszukiwanie internetu itp.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Użycie gotowych MCP z internetu | Wykorzystanie istniejących serwerów MCP (webster, weather service, mermaid, chart generation) | ✅ Częściowo zaimplementowane - dodano stronę zarządzania MCP |
| Hosting MCP po stronie klienta | MCP uruchamiane lokalnie na serwerze klienta | ⏸️ Odroczone - wymaga większej autonomii klientów |
| Hosting MCP u nas (AMODIT) | Centralne serwery MCP dostępne dla wszystkich klientów | 💡 Propozycja Janusza - preferowane rozwiązanie |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (podstawowa implementacja)

Została zaimplementowana **strona zarządzania MCP** (`/ajax/MCP`), która pozwala:
- Definiować serwery MCP (typ: stdio lub remote)
- Dla stdio: podać ścieżkę do programu na dysku serwera
- Dla remote: podać adres hosta
- Synchronizować narzędzia (tools) z serwera MCP
- Zarządzać uprawnieniami do tools (wszyscy / administratorzy / custom)
- Ustawiać opisy i dodatkowe wiadomości dla tools

**Szczegóły techniczne:**
- Strona: `/ajax/MCP`
- Typy serwerów: stdio (lokalny program), remote (zewnętrzny host)
- Parametry konfiguracji: ścieżka/host, opis, uprawnienia
- Możliwość synchronizacji tools z serwera

**Przetestowane MCP:**
- **webster** - przeszukiwanie internetu (Bing News)
- **weather Service** - informacje o pogodzie (działa na "Mateusza mały")
- **Mermaid MCP** - generowanie diagramów Mermaid jako obrazki
- **Chart MCP** - generowanie wykresów wizualnych

**Decyzja dotycząca hostingu:**
- **Preferowane:** Hosting MCP u nas (AMODIT) na wspólnym serwerze - dostępne dla wszystkich klientów
- Możliwość pozwolenia klientom na dodawanie własnych lokalnych serwerów MCP (jeśli będą mieli kompetencje)

### Ograniczenia / Poza zakresem

- Niektóre MCP działają tylko lokalnie na komputerze developera (np. webster, joe na komputerze Mateusza)
- Wymaga publicznego serwera do hostingu MCP dla klientów
- Decyzja o lokalizacji hostingu (Azure, gdzie są serwisy modecom, inne)

### Punkty otwarte

- Gdzie hostować centralne serwery MCP? (Azure, modecom, inne)
- Jakie konkretne MCP mają sens biznesowy dla AMODIT?
- Czy pozwalać klientom na dodawanie własnych MCP?
- Przygotować listę rekomendowanych MCP do podłączenia (chart generation, Mermaid, SQL na plikach CSV, browser do czytania URL)

---

## 2. Docelowy Serwer AMODIT MCP - Built-in Tools

**Komponent:** AMODIT Copilot / AI

### Cel i problem

AMODIT powinien mieć własny, wbudowany serwer MCP, który będzie zawsze dostępny (niemożliwy do wyłączenia) i reprezentował natywne funkcje systemu. Użytkownicy powinni mieć możliwość zarządzania dostępem do poszczególnych tools na poziomie instancji lub użytkownika.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja

Docelowo będzie istniał **dedykowany serwer MCP dla AMODIT**, który:
- Będzie zawsze widoczny i niemożliwy do wyłączenia
- Będzie reprezentował natywne funkcje AMODIT (API, baza danych, procesy)
- Pozwoli zarządzać dostępnością tools dla użytkowników (włączanie/wyłączanie)
- Przykład: jeśli instancja nie chce mieć dostępu do sprawozdań, można wyłączyć odpowiedni tool

**Szczegóły techniczne:**
- Format: serwer MCP zawsze dostępny w interfejsie zarządzania
- Zarządzanie: włączanie/wyłączanie tools per instancja lub użytkownik
- Przykładowe tools: dostęp do procesów, raportów, spraw, ustawień systemowych

### Punkty otwarte

- Jakie dokładnie tools powinny być w wbudowanym serwerze AMODIT?
- Struktura uprawnień - per instancja czy per użytkownik?

---

## 3. MCP Serwer dla dostępu DO AMODIT (z zewnątrz)

**Komponent:** AMODIT API / Copilot

### Cel i problem

Oprócz możliwości wyjścia z AMODIT (dodawanie zewnętrznych MCP do Copilota), powinna istnieć możliwość **dostępu DO AMODIT z zewnątrz** poprzez MCP. Przykład: podłączenie się do AMODIT z poziomu zewnętrznego Copilota (np. Claude) i zapytanie "jakie mam wnioski urlopowe założone" lub inne dane z systemu.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji - wymaga analizy technicznej

AMODIT powinien udostępniać **własny serwer MCP**, który pozwoli zewnętrznym klientom (np. Copilot Claude) łączyć się z AMODIT i odpytywać o dane.

**Problem techniczny:**
- Biblioteka do tworzenia serwera MCP wymaga **.NET Core 8**
- AMODIT oparty jest na **.NET Framework** (starej wersji)
- Biblioteki są **niekompatybilne** - .NET Framework nie obsługuje .NET Core

**Szczegóły techniczne:**
- Wymagana biblioteka: .NET Core 8
- Obecny stack AMODIT: .NET Framework
- Przejście AMODIT na .NET Core: "bardzo długa i trudna migracja" (więcej niż 6 miesięcy, bardziej skomplikowane niż migracja frontendu na React)

**Alternatywy:**
- Poszukanie biblioteki MCP dla .NET Framework (jeśli istnieje)
- Rozważenie mikroservisu w .NET Core tylko dla MCP (Trust Center już jest w .NET Core)

### Ograniczenia / Poza zakresem

- Pełna migracja AMODIT na .NET Core jest bardzo długa i trudna (bardziej skomplikowana niż przejście frontendu na React)
- .NET Framework nie jest już rozwijany (tylko .NET Core)

### Punkty otwarte

- Czy istnieje biblioteka MCP dla .NET Framework?
- Czy możliwe jest stworzenie mikroservisu w .NET Core tylko dla obsługi MCP?
- Czy warto rozważyć długoterminową strategię migracji na .NET Core?

---

## 4. Automatyczne Generowanie Dokumentacji Procesu

**Komponent:** AMODIT Copilot / Edytor Procesów

### Cel i problem

Tworzenie dokumentacji procesów jest czasochłonne i żmudne. AMODIT Copilot powinien automatycznie generować dokumentację procesu na podstawie jego definicji (diagram, formularze, etapy, reguły). Dokumentacja ma być zgodna ze wzorcowym szablonem (dostarczonym przez Piotra Pawłowskiego z polu tomu).

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (wersja MVP)

Copilot generuje dokumentację procesu na podstawie:
- Prompta użytkownika (np. "Wygeneruj mi dokumentację dla procesu o CRV 3")
- Wzorcowego szablonu dokumentacji (plik Word dostarczony przez Janusza)

**Struktura dokumentacji (wstępna):**
- Cel procesu
- Opis procesu
- Sposób powstania sprawy (z zakładki procesy, z dedykowanego obszaru, automatyczne tworzenie)
- Diagram procesu (Mermaid - jako tekst, docelowo jako obrazek)
- Opis etapów procesu
- Lista pól formularza (nazwa systemowa, nazwa polska, typ, wymagalność, warunki)
- Wymagania biznesowe procesu
- Raporty powiązane z procesem

**Szczegóły techniczne:**
- Prompt: "Wygeneruj mi dokumentację dla procesu o [nazwa]"
- Szablon: wzorcowy dokument Word (dostarczony przez Piotra Pawłowskiego)
- Format danych diagram: Mermaid (tekstowo, docelowo obrazek poprzez MCP)
- Generowanie na podstawie: ProcessDefinition

**Przetestowano na procesie:** Podpisywanie w Trust Center (Link 14)

### Ograniczenia / Poza zakresem

**MVP 1 - obecna wersja:**
- Pola formularza: wyświetlane globalnie (bez podziału na etapy), tylko nazwa systemowa (brak polskiej nazwy), wymagalność i warunki niekoniecznie dokładne (zależne od etapu)
- Brak opisu pól (puste "Opis pola")
- Opis etapów: wstępny, brak szczegółów (jakie pola dostępne, jakie reguły, przyciski akcji)
- Raporty: wyświetlane wszystkie raporty korzystające z procesu (nie tylko osadzone)
- Brak szczegółowego opisu raportów
- Niektóre sekcje niekompletne (np. "Sposób powstania sprawy" - tylko nagłówek bez treści)

**Uzgodnienia na przyszłość (MVP 2+):**
- **Pola per etap:** Lista pól powinna być rozbudowana per etap (etap Rejestracja - jakie pola dostępne, wymagane, tylko odczyt, przyciski akcji)
- **Dwie kolumny nazw:** Nazwa systemowa + Nazwa polska
- **Reguły biznesowe:** Dodać reguły przejścia między etapami
- **Opis pól:** Możliwość generowania opisu pól przez AI (biznesowy opis pola)
- **Format nazw:** Wyświetlanie polskich nazw pól (jeśli dostępne), angielskie jako fallback

### Punkty otwarte

- Gdzie umieścić przycisk "Wygeneruj dokumentację" w interfejsie? (docelowo osobna zakładka "Dokumentacja procesu", MVP 1 - dowolne miejsce w definicji procesu)
- Czy generować opisy pól automatycznie przez AI?
- Czy zapisywać wygenerowane dokumentacje (versioning)?
- Kto może generować dokumentację? (tylko administrator + administrator procesu)

---

## 5. Zabezpieczenie Dostępu do Generowania Dokumentacji

**Komponent:** AMODIT Copilot

### Cel i problem

Generowanie dokumentacji zużywa kredyty AI i powinno być dostępne tylko dla administratorów lub administratorów procesu. Zwykły użytkownik nie powinien mieć możliwości wygenerowania dokumentacji.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Tylko administrator systemowy | Dostęp tylko dla administratorów systemu | ⏸️ Odroczona |
| Administrator systemowy + administrator procesu | Dostęp dla admin systemu i admin procesu | ✅ Zatwierdzone |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Tool do generowania dokumentacji procesu powinien:
- Sprawdzić czy użytkownik jest **administratorem systemowym** LUB **administratorem procesu**
- Jeśli NIE - odmówić wykonania (komunikat "Brak uprawnień")
- Jeśli TAK - wygenerować dokumentację

**Szczegóły techniczne:**
- Weryfikacja uprawnień: admin systemowy OR admin procesu
- Odmowa dostępu dla zwykłych użytkowników

---

## 6. Rozbudowa Generowania Dokumentacji - Dalsze Możliwości

**Komponent:** AMODIT Copilot

### Cel i problem

Dokumentacja procesu to tylko jeden z elementów dokumentacji wdrożenia. Podobnie można generować dokumentację raportów, ustawień systemowych, integracji, logów. Docelowo - pełna dokumentacja wdrożenia poprzez agenta, który wygeneruje wszystko automatycznie.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja (MVP 3-5)

**Roadmapa rozbudowy:**
- **MVP 1:** Dokumentacja procesu (obecna implementacja)
- **MVP 2:** Dopracowanie dokumentacji procesu (pola per etap, reguły, polskie nazwy)
- **MVP 3-4:** Dokumentacja ustawień systemowych, dokumentacja pojedynczego raportu
- **MVP 5+:** Agent generujący pełną dokumentację wdrożenia (wszystkie procesy + raporty + ustawienia + integracje)

**Szczegóły techniczne (koncepcja agenta):**
- Agent otrzymuje polecenie: "Zrób mi dokumentację tego wdrożenia"
- Agent automatycznie generuje dokumentację wszystkich procesów
- Agent generuje dokumentację ustawień systemowych
- Agent generuje dokumentację raportów
- Agent łączy wszystko w jeden wielki dokument Word

**Uwaga:** Dokumentacja raportów ma niższy priorytet (w praktyce wdrożeniowej to maksymalnie 2 zdania opisu raportu)

### Punkty otwarte

- Jaki format docelowy dokumentacji wdrożenia? (Word, PDF, Markdown)
- Czy zapisywać dokumentacje w systemie (versioning)?
- Struktura szablonu dla ustawień systemowych, raportów, integracji

---

## 7. Przycisk w Interfejsie - Generowanie Dokumentacji

**Komponent:** AMODIT UI / Edytor Procesów

### Cel i problem

Użytkownik powinien mieć możliwość wygenerowania dokumentacji procesu bezpośrednio z interfejsu edytora procesów. Docelowo powinna być osobna zakładka "Dokumentacja procesu", ale w MVP 1 może być dowolne miejsce.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Przycisk w dowolnym miejscu (Ustawienia) | MVP 1 - przycisk w dowolnym miejscu w definicji procesu | ✅ Zatwierdzone (MVP 1) |
| Osobna zakładka "Dokumentacja procesu" | Docelowe rozwiązanie - dedykowana zakładka | 💡 Propozycja (MVP 2+) |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (MVP 1)

**MVP 1:**
- Przycisk "Wygeneruj dokumentację" w dowolnym miejscu w definicji procesu (może być w Ustawieniach)
- Przycisk wywołuje wbudowany prompt do Copilota (użytkownik nie pisze własnego prompta)
- Prompt jest stały i zarządzany przez AMODIT (spójna dokumentacja)

**Docelowo (MVP 2+):**
- Osobna zakładka "Dokumentacja procesu" w edytorze procesów
- Możliwość zapisywania wygenerowanej dokumentacji
- Możliwość kasowania i regenerowania dokumentacji

**Szczegóły techniczne:**
- Przycisk: wywołanie Copilota z predefiniowanym promptem
- Prompt: stały szablon (nie edytowalny przez użytkownika w MVP 1)
- Cel: spójna struktura dokumentacji dla wszystkich procesów

---

## 8. Analiza Dostępnych MCP - Rekomendacja Biznesowa

**Komponent:** AMODIT Copilot / AI

### Cel i problem

Na GitHubie dostępna jest duża lista serwerów MCP. Należy wybrać te, które mają sens biznesowy dla AMODIT i są przydatne w kontekście systemu workflow/BPM.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja Janusza

Janusz zaproponował **ćwiczenie dla AI:**
- Podać AI stronę z listą serwerów MCP
- Kazać przeanalizować wszystkie dostępne serwery
- Wybrać te, które mają sens biznesowy dla systemu AMODIT

**Zidentyfikowane potencjalnie przydatne MCP:**
- **Chart Generation** - generowanie wykresów (połączenie z danymi AMODIT)
- **Mermaid MCP** - generowanie diagramów Mermaid jako obrazki
- **SQL na plikach CSV/Excel** - możliwość odpytywania plików jak bazę danych
- **Browser** - pobieranie treści z URL (streszczanie artykułów, dokumentacji)
- **Memory** - zapamiętywanie informacji (uwaga: wymaga oddzielnej instancji per klient!)

**Szczegóły techniczne:**
- Źródło: lista MCP na GitHubie
- Kryteria wyboru: sens biznesowy, zastosowanie w systemie workflow/BPM
- Uwaga: niektóre MCP (np. memory) muszą być dedykowane per klient (nie wspólne)

### Punkty otwarte

- Przesłać Januszowi adres strony z listą MCP
- Przeprowadzić analizę wszystkich dostępnych MCP
- Przygotować rekomendowaną listę MCP do podłączenia

---

## 9. Customizacja Prompta przy Generowaniu Dokumentacji

**Komponent:** AMODIT Copilot

### Cel i problem

Użytkownik może chcieć doprecyzować co ma być w dokumentacji (np. "opisz mi dokładniej raporty, które korzystają z tego procesu"). Pytanie czy prompt powinien być stały (pod przyciskiem) czy elastyczny (użytkownik może dopisać)?

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Stały prompt pod przyciskiem | AMODIT zarządza promptem, dokumentacja spójna | ✅ Zatwierdzone (MVP 1) |
| Elastyczny prompt (użytkownik może dopisać) | Użytkownik może customizować prompt w oknie Copilota | 💡 Propozycja (MVP 2+) |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (MVP 1)

**MVP 1:**
- Przycisk "Wygeneruj dokumentację" wywołuje **stały prompt**
- Prompt jest zarządzany przez AMODIT (użytkownik nie widzi/nie edytuje)
- Cel: spójna dokumentacja dla wszystkich procesów

**Docelowo (MVP 2+):**
- Użytkownik może w ramach Copilota doprecyzować prompt (np. "opisz mi dokładniej raporty")
- Copilot potrafi pobrać dodatkowe informacje (np. definicje raportów) i rozbudować dokumentację

**Szczegóły techniczne:**
- MVP 1: stały prompt, brak edycji przez użytkownika
- MVP 2+: możliwość customizacji prompta w oknie Copilota

---

## Punkty do dalszej dyskusji (globalne)

- Gdzie hostować centralne serwery MCP dla AMODIT? (Azure, modecom, inne)
- Jakie konkretne MCP wybrać do podłączenia? (potrzebna analiza listy z GitHuba)
- Jak rozwiązać problem .NET Framework vs .NET Core dla serwera MCP DO AMODIT?
- Gdzie umieścić przycisk "Wygeneruj dokumentację" w interfejsie? (MVP 1 vs MVP 2+)
- Czy zapisywać wygenerowane dokumentacje? (versioning, historia)
- Struktura szablonu dokumentacji dla raportów, ustawień systemowych, integracji
- Czy pozwalać klientom na dodawanie własnych MCP?
