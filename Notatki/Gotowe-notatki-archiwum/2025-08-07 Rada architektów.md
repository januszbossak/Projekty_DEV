# Rada Architektów – 2025-08-07

> 🛡️ Notatka zweryfikowana i zmapowana (Codex Review) w dniu 2025-12-03

**Powiązane projekty:**
- [[Moduly/Ustawienia-systemowe/README|Ustawienia-systemowe]] – tematy 1, 2, 3, 4, 5, 6

---

## 1. MVP dla integracji w ustawieniach systemowych

**Projekt:** `Moduly/Ustawienia-systemowe`

### Kontekst i Problem

Dyskusja dotyczyła finalizacji MVP dla modułu integracji w nowych ustawieniach systemowych. Obecna implementacja wymaga uproszczenia interfejsu, aby pokazywać tylko te integracje, które są faktycznie skonfigurowane i używane przez klienta. Kluczowe jest rozróżnienie między integracjami wbudowanymi (nie wymagającymi konfiguracji) a tymi wymagającymi konfiguracji oraz integracjami własnymi (customowymi).

### Zidentyfikowane Ryzyka

- Ryzyko utraty kompatybilności z istniejącymi konfiguracjami klientów podczas reorganizacji interfejsu
- Ryzyko przedłużenia się prac nad MVP przez próbę realizacji wszystkich pomysłów jednocześnie
- Ryzyko niejasności dla użytkownika końcowego co do lokalizacji konfiguracji różnych typów integracji

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Pokazywanie wszystkich potencjalnych integracji w drugiej kolumnie | Wyświetlanie pełnej listy dostępnych integracji od razu | ❌ Odrzucona – zbyt przeładowany interfejs, nie pokazuje faktycznego stanu konfiguracji |
| Pokazywanie tylko skonfigurowanych integracji | Integracje pojawiają się na liście tylko gdy mają skonfigurowane parametry (nawet częściowo) | ✅ Wybrana – czytelny interfejs pokazujący faktyczny stan |
| Integracje wbudowane jako osobna sekcja | VIES, kursy walut, Biała Lista jako stała pierwsza pozycja "Integracje wbudowane" | ✅ Wybrana – jasne rozróżnienie integracji nie wymagających konfiguracji |
| Pełna reorganizacja ustawień systemowych | Podział na kategorie (podpisy, przechowywanie dokumentów, uwierzytelnianie) | ⏸️ Odroczona – wymaga osobnego projektu, nie mieści się w MVP |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono strukturę MVP dla integracji w ustawieniach systemowych:

1. **Pierwsza pozycja:** "Integracje wbudowane" – stała sekcja zawierająca integracje nie wymagające konfiguracji (VIES, kursy walut, Biała Lista). Po kliknięciu wyświetla się ikonka i krótki opis działania.

2. **Druga kolumna:** Lista integracji skonfigurowanych:
   - Integracje wbudowane wymagające konfiguracji – pojawiają się tylko gdy są skonfigurowane (mają uzupełnione parametry, nawet częściowo)
   - Integracje własne (customowe) – dodawane przez przycisk "Skonfiguruj własną"

3. **Przycisk "Nowa" / "Dodaj integrację":**
   - Wybór między standardową integracją (z listy dostępnych)
   - Opcja "Skonfiguruj własną" – pojawia się formularz z parametrami (np. Custom CRM)

4. **Zasada wyświetlania:** Integracja pojawia się na liście tylko gdy ma skonfigurowane parametry (nawet nie w całości). Integracje "czyste" (bez konfiguracji) nie są widoczne na liście.

**Szczegóły techniczne:**
- Interfejs w Reactcie
- Dodanie możliwości konfiguracji parametrów z poziomu interfejsu (bez dostępu do bazy danych)
- Baza danych: nadal korzystamy z tabeli `Parameters` na ten moment
- Kompatybilność wsteczna: istniejące konfiguracje klientów muszą pozostać widoczne

### Zadania

- **Kamil Dubaniowski, Przemek:** Finalizacja MVP zgodnie z ustaleniami – uproszczenie interfejsu, dodanie sekcji "Integracje wbudowane", logika wyświetlania tylko skonfigurowanych integracji
- **Kamil Dubaniowski:** Rozszerzenie panelu o możliwość dodawania parametrów z poziomu interfejsu

### Punkty otwarte

- Kwestia obsługi integracji wymagających licencji/abonamentu – do rozważenia w przyszłości możliwość generowania prośby o licencję do działu handlowego
- Lokalizacja konfiguracji OAuth i tokenów – czy w integracjach czy osobna zakładka (patrz temat 3)

---

## 2. OAuth i tokeny – konfiguracja aplikacji

**Projekt:** `Moduly/Ustawienia-systemowe`

### Kontekst i Problem

Piotr przedstawił koncepcję konfiguracji OAuth dla integracji. Zamiast wpisywania 3-5 parametrów osobno dla każdej integracji, proponuje się definicję aplikacji OAuth z możliwością generowania wielu tokenów. Następnie w konfiguracji integracji wybiera się tylko odpowiedni token zamiast ręcznego wpisywania parametrów.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Konfiguracja OAuth w integracjach | Definicja aplikacji OAuth jako część modułu integracji | ⏸️ Odroczona – wymaga przemyślenia lokalizacji |
| Osobna zakładka do definiowania aplikacji OAuth | Analogicznie do obecnej zakładki "Baza danych" z Connection Stringami | 💡 Propozycja – bardziej spójne z obecną strukturą ustawień |

### Decyzja

**Status:** 🔍 Do weryfikacji

Koncepcja OAuth i tokenów została zaakceptowana jako właściwy kierunek, jednak lokalizacja tej funkcjonalności wymaga dalszego przemyślenia. Piotr przedstawił szczegóły techniczne, ale ostateczna decyzja czy to ma być w integracjach czy osobna zakładka została odroczona do dalszej analizy.

**Szczegóły techniczne:**
- Definicja aplikacji OAuth z 5 parametrami
- Możliwość generowania wielu tokenów dla jednej aplikacji
- W konfiguracji integracji wybór tokenu zamiast ręcznego wpisywania parametrów
- Przykłady: Microsoft, Google, poczta przychodząca

### Zadania

- **Piotr Buczkowski:** Dalsze przemyślenie lokalizacji konfiguracji OAuth i tokenów w strukturze ustawień systemowych

### Punkty otwarte

- Czy konfiguracja OAuth powinna być w integracjach czy osobnej zakładce (analogicznie do Connection Stringów)?
- Jak wpleść tę funkcjonalność w MVP bez opóźniania publikacji ustawień systemowych?

---

## 3. Reorganizacja ustawień systemowych – kategorie integracji

**Projekt:** `Moduly/Ustawienia-systemowe`

### Kontekst i Problem

Obecne ustawienia systemowe są nieuporządkowane – integracje dodawane są w kolejności implementacji bez logicznego podziału. Dyskutowano o potrzebie kategoryzacji integracji według zastosowań biznesowych (np. podpisy elektroniczne, przechowywanie dokumentów, uwierzytelnianie użytkowników).

### Zidentyfikowane Ryzyka

- Ryzyko przedłużenia się prac nad MVP przez próbę reorganizacji wszystkiego jednocześnie
- Ryzyko opóźnienia publikacji ustawień systemowych przez próbę realizacji wszystkich pomysłów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Kategoryzacja integracji w MVP | Podział na kategorie: podpisy (Autenti, DocuSign, Trust Center), przechowywanie (SharePoint, KSeF, Alfresco), uwierzytelnianie (Active Directory, baza danych) | ⏸️ Odroczona – zbyt złożone na MVP |
| MVP bez reorganizacji | Odwzorowanie obecnej struktury w Reactcie, tylko ładniej | ✅ Wybrana – pozwala na szybkie dowiezienie funkcjonalności |
| Osobny projekt reorganizacji | Pełna reorganizacja ustawień systemowych w przyszłym kwartale/roku | ⏸️ Odroczona – jako osobny projekt po MVP |

### Decyzja

**Status:** ⏸️ Odroczone

Ustalono, że kategoryzacja integracji i pełna reorganizacja ustawień systemowych jest potrzebna, ale nie mieści się w zakresie MVP. Obecne podejście MVP zakłada odwzorowanie istniejącej struktury w Reactcie z poprawą UX, bez głębokiej reorganizacji.

**Szczegóły techniczne:**
- Przykładowe kategorie: integracje z systemami do podpisywania, przechowywania dokumentów, uwierzytelniania użytkowników
- Integracje związane z użytkownikami (Active Directory, synchronizacja przez bazę danych) mogą trafić do osobnej zakładki "Uwierzytelnianie użytkowników"
- Connection Stringi do baz danych również mogą być traktowane jako element integracji (przez bazę danych zamiast API)

### Zadania

- **[Do ustalenia]:** Planowanie osobnego projektu reorganizacji ustawień systemowych na przyszły kwartał/rok

### Punkty otwarte

- Jak podzielić integracje na kategorie biznesowe?
- Czy Active Directory powinno być w integracjach czy osobnej zakładce "Uwierzytelnianie użytkowników"?
- Czy Connection Stringi powinny być traktowane jako integracje czy osobna zakładka?
- Lokalizacja konfiguracji poczty przychodzącej/wychodzącej – czy w integracjach czy osobnej zakładce?

---

## 4. Wykorzystanie AI do tworzenia integracji

**Projekt:** `Moduly/Ustawienia-systemowe`

### Kontekst i Problem

Dyskutowano o możliwości wykorzystania AI (np. AMODIT Copilot) do automatycznego generowania konfiguracji integracji na podstawie specyfikacji API (np. link do Swaggera). AI miałoby analizować dokumentację i proponować parametry oraz sposób logowania wymagane do integracji.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| AI do generowania konfiguracji integracji | Wrzucenie linku do Swaggera, AI analizuje i proponuje parametry | ⏸️ Odroczona – nie w zakresie MVP |
| Ręczna konfiguracja parametrów | Obecne podejście – konsultant/handlowiec wpisuje parametry ręcznie | ✅ Obecne – działa, ale czasochłonne |

### Decyzja

**Status:** ⏸️ Odroczone

Funkcjonalność wykorzystania AI do tworzenia integracji została uznana za wartościową, ale nie mieści się w zakresie MVP. Jest to element "MVP rozszerzonego" i części szerszej strategii wykorzystania AI do ułatwienia pracy integratorów i konsultantów.

**Szczegóły techniczne:**
- Wykorzystanie AMODIT Copilot (obecnie w core'ie)
- Analiza dokumentacji API (np. Swagger)
- Generowanie propozycji parametrów i sposobu logowania
- Parametry z zdefiniowanej listy (nie dowolne) – system obsługuje określony zestaw parametrów
- Przykład już wdrożony: wyszukiwanie i interpretacja parametrów w Copilocie

### Zadania

- **[Do ustalenia]:** Planowanie funkcjonalności AI do generowania konfiguracji integracji w przyszłości

### Punkty otwarte

- Kiedy i w jakim zakresie wdrożyć funkcjonalność AI do tworzenia integracji?
- Jakie parametry mogą być automatycznie wykrywane przez AI?

---

## 5. Eksport helpa do PDF

**Projekt:** `Moduly/Ustawienia-systemowe`

### Kontekst i Problem

Pytanie klienta o możliwość wyeksportowania całej listy helpa (dostępnej pod linkiem) do jednego pliku PDF lub pliku tekstowego z listą komend.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Eksport helpa do PDF | Implementacja funkcjonalności eksportu | ❌ Odrzucona – brak uzasadnienia biznesowego, help jest dostępny w AMODIT Copilocie i plikach YAML |
| Oferta płatna | Wycena na 15 000 zł za implementację | 💡 Propozycja – jako sposób na weryfikację rzeczywistej potrzeby |

### Decyzja

**Status:** ❌ Odrzucona

Funkcjonalność eksportu helpa do PDF została odrzucona jako nieuzasadniona biznesowo. Help jest dostępny w AMODIT Copilocie oraz w plikach YAML, które mogą być udostępnione klientowi. Dokumentacja zmienia się często, więc eksport do statycznego pliku nie ma sensu.

**Szczegóły techniczne:**
- Help dostępny w AMODIT Copilocie
- Pliki YAML z dokumentacją mogą być udostępnione klientowi
- Dokumentacja zmienia się często – statyczny eksport szybko się dezaktualizuje

### Zadania

- Brak zadań

### Punkty otwarte

- Brak

---

## 6. Integracje vs moduły – rozróżnienie

**Projekt:** `Moduly/Ustawienia-systemowe`

### Kontekst i Problem

Podczas dyskusji o integracjach pojawiła się kwestia rozróżnienia między integracjami (połączeniami z zewnętrznymi systemami) a modułami (funkcjonalnościami systemu, np. "Raporty zaawansowane"). Moduły powinny być w licencji, a nie w zakładce integracji.

### Zidentyfikowane Ryzyka

- Ryzyko pomieszania integracji z modułami w interfejsie użytkownika
- Ryzyko niejasności dla klienta co jest integracją a co modułem

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rozróżnienie integracji i modułów | Integracje = połączenia z zewnętrznymi systemami, moduły = funkcjonalności systemu (w licencji) | ✅ Wybrana – jasne kryterium podziału |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono jasne rozróżnienie: integracje to połączenia z zewnętrznymi systemami (np. KSeF, OpenAI, Biała Lista), natomiast moduły to funkcjonalności systemu (np. "Raporty zaawansowane") i powinny być w licencji, a nie w zakładce integracji.

**Szczegóły techniczne:**
- Przykłady integracji: KSeF, OpenAI, Biała Lista, VIES, kursy walut
- Przykłady modułów: Raporty zaawansowane (nie integracja, tylko moduł)
- Moduły mogą wymagać licencji/abonamentu, ale są to funkcjonalności systemu, nie integracje

### Zadania

- **Kamil Dubaniowski, Przemek:** Upewnienie się, że w interfejsie integracji nie ma modułów (tylko prawdziwe integracje)

### Punkty otwarte

- Brak

