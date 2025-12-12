# Spotkanie projektowe – 2025-12-02

**Data:** 2025-12-02  
**Typ:** Spotkanie projektowe  
**Temat główny:** AMODIT UI - Edytor procesów, Strategia AI (generowanie dokumentacji, MCP), Integracje OCR

**Źródło:** [Transkrypcja](../Transkrypcje/oczyszczone-archiwum/2025-12-02 Spotkanie projektowe - AMODIT UI - transkrypcja - część 1.md)

---

## 1. Edytor procesów - Prawy panel ustawień pól

**Komponent:** Edytor Formularzy

### Kontekst i cel

Przeprojektowanie prawego panelu ustawień pól w edytorze formularzy. Celem jest uporządkowanie akcji dostępnych dla pól formularza, zapewnienie spójności z innymi częściami aplikacji oraz przygotowanie do rozbudowy o zarządzanie regułami powiązanymi z polami. Obecnie dedykowana zakładka do zarządzania polem pozwala na zmianę typu pola i usunięcie pola - te akcje muszą być przeniesione do nowej struktury.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (design w trakcie)

**Nowa struktura prawego panelu:**

- **Górna belka** - wszystkie akcje dodatkowe (spójne z resztą aplikacji):
  - Usuń pole
  - Historia pola
  - Zarządzanie widocznością i uprawnieniami
  
- **Przy typie pola** - zmiana typu pola (intuicyjne umiejscowienie obok aktualnego typu)

- **Ikona błyskawicy (⚡)** - dla każdego pola:
  - Otwiera popup z listą reguł powiązanych z tym polem
  - Dla tabel: główna akcja to przejście do edycji reguł tabeli
  - Pokazuje również reguły powiązane z polem tabeli
  - Kliknięcie w konkretną regułę otwiera edytor reguły na cały ekran

**Szczegóły techniczne:**
- Reguły tabeli mogą być rozbite tematycznie (nie musi być jedna zbiorcza reguła)
- Lista reguł w prawym panelu, edytor reguły na cały ekran po kliknięciu

### Punkty otwarte

- Finalizacja designu popupu z listą reguł
- Decyzja czy lista reguł ma być w prawym panelu czy w osobnym oknie

---

## 2. Planowanie sprintów - Metodyka i roadmapa

**Komponent:** Organizacja pracy DEV

### Kontekst i cel

Dyskusja o metodyce planowania sprintów i roadmapy. Przemysław Sołdacki postuluje planowanie 2 sprintów do przodu (bieżący + kolejny) aby zapewnić zgodność z roczną roadmapą i umożliwić weryfikację postępów. Janusz wskazuje na trudności z szczegółowym planowaniem z wyprzedzeniem ze względu na nieprzewidywalne zlecenia klientów.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Planowanie 2 sprintów do przodu | Bieżący sprint + kolejny sprint szczegółowo zaplanowane | 💡 Propozycja - do wdrożenia |
| Planowanie tylko bieżącego sprintu | Skupienie na aktualnym sprincie, kolejny kierunkowo | ⏸️ Obecny stan - do zmiany |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (do wdrożenia)

**Metodyka:**
- Planowanie na 2 sprinty do przodu (bieżący + kolejny)
- Szczegółowe cele sprintu z kryteriami sukcesu
- Cele mogą być zmieniane jeśli sytuacja się zmieni (np. po Sprint Review)
- Roadmapa roczna z szczegółowym pierwszym kwartałem
- Planowanie kolejnego sprintu na początku tygodnia (poniedziałek-wtorek)

**Uzasadnienie biznesowe:**
- Weryfikacja zgodności z roadmapą
- Lepsza komunikacja priorytetów do zespołu
- Programiści wiedzą co jest najważniejsze (nie muszą zgadywać)
- Możliwość wcześniejszego wykrycia rozbieżności z planem

### Zadania / Dalsze kroki

- **Janusz, Kamil, Damian:** Wdrożyć planowanie 2 sprintów do przodu
- **Janusz:** Przekazywać cele sprintów w ustandaryzowanej formie (jak w obecnym dokumencie)

---

## 3. Bieżący sprint - Cele i projekty klienckie

**Komponent:** Organizacja pracy DEV

### Kontekst i cel

Przegląd celów bieżącego sprintu i projektów klienckich w realizacji. Główne cele: MVP edytora procesów oraz repozytorium dla WIM. Równolegle realizowane są zlecenia klientów (LOT, Lewiatan) które nie są ujęte jako osobne cele sprintu.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (w realizacji)

**Cele bieżącego sprintu:**
1. **Edytor procesów** - kompletne MVP
2. **Repozytorium WIM** - gotowe do użycia przez konsultantów i klienta

**Projekty klienckie (poza celami sprintu):**
- **LOT:**
  - JRWA - uproszczona koncepcja, realizacja przez Marka (1-2 dni)
  - Paczka do archiwum państwowego (ADE) - pierwsza wersja do weryfikacji
  - Integracja UPS - stabilizacja
  - Integracja Global Express - stabilizacja
  
- **Lewiatan:**
  - Comarch Hub (integracja KSeF) - wartość potwierdzona przez klienta: 18 000 zł

- **Vasco:**
  - Integracja z Google Gemini dla OCR (temat powrócił 2025-12-02)

**Inne zadania:**
- Poprawki błędów
- Drobne zadania rozwojowe (nie ujęte w cele)
- Proof of concept generowania dokumentacji (Mateusz)

### Ograniczenia / Poza zakresem

- Nie rozpoczynać nowych rzeczy rozwojowych poza celami sprintu (chyba że zlecenie klienta)
- Część mocy zespołu zarezerwowana na nieprzewidywalne zlecenia klientów

### Punkty otwarte

- Czy konsultanci LOT są gotowi na przygotowywanie paczek do archiwum w grudniu? (wątpliwości Janusza - mogą nie mieć jeszcze wdrożonego procesu obiegu korespondencji)
- Możliwe przesunięcie paczki do archiwum na kolejny kwartał jeśli konsultanci nie są gotowi

---

## 4. Generowanie dokumentacji procesów przez AI

**Komponent:** AMODIT Copilot / AI

### Kontekst i cel

Automatyczne generowanie dokumentacji procesów przez AI. Mateusz wykonał proof of concept - funkcjonalność działa. Celem jest oszczędność czasu konsultantów (obecnie ~1 dzień pracy na dokumentację procesu) oraz dodatkowa wartość dla licencji AI (możliwość sprzedaży klientom którzy sami tworzą procesy).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| MVP - tylko opis procesu | Podstawowa wersja generująca opis procesu | ✅ PoC gotowy (Mateusz) |
| Rozbudowana wersja | Checkboxy z wyborem typów dokumentacji (proces, ustawienia systemowe, raporty, etc.) + endpoint do generowania | 💡 Propozycja - do zaprojektowania |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (priorytet - do realizacji)

**Wartość biznesowa:**

1. **Oszczędności wewnętrzne:**
   - ~1 dzień pracy na dokumentację procesu
   - Przy każdej zmianie procesu trzeba aktualizować dokumentację (kolejny dzień)
   - Szacunkowo: 60 dni rocznie oszczędności = 2-3 osobo-miesiące
   - LOT: ~6 dni oszczędności (kilka procesów)
   
2. **Przychody z licencji AI:**
   - Funkcjonalność w ramach licencji AI (standard lub advanced)
   - Klienci którzy sami tworzą procesy mogą kupić licencję aby generować dokumentację
   - Przykład: Res Invest - zainteresowanie eksportem XML + dokumentacji

**Szczegóły techniczne:**
- Przycisk "Generuj dokumentację" w edytorze procesów
- Popup z checkboxami - wybór typów dokumentacji:
  - Opis procesu (instrukcja użytkownika)
  - Ustawienia systemowe
  - Raporty
  - Inne elementy konfiguracji
- Opcja "Wygeneruj wszystko"
- Endpoint do wywołania generowania

**Licencjonowanie:**
- Generowanie dokumentacji jako element licencji AI (wersja standard lub advanced - do ustalenia)
- Konsultanci mogą używać AI u klientów bez licencji (osobny mechanizm autoryzacji)

### Zadania / Dalsze kroki

- **Przemysław:** Opisać przypadki użycia dla generowania dokumentacji (checkboxy, typy dokumentów)
- **Mateusz:** Rozbudować PoC o UI (checkboxy, endpoint) - szacunkowo kilkanaście godzin
- **Zespół:** Określić czy funkcjonalność w wersji standard czy advanced licencji AI

### Punkty otwarte

- Finalna decyzja o poziomie licencji AI (standard vs advanced)
- Szczegółowy zakres typów dokumentacji do wygenerowania

---

## 5. MCP (Model Context Protocol) - AMODIT Copilot

**Komponent:** AMODIT Copilot / AI

### Kontekst i cel

Integracja AMODIT Copilot z Model Context Protocol (MCP) - umożliwienie zewnętrznym agentom AI (np. Claude, ChatGPT) dostępu do funkcji AMODIT Copilot. Mateusz wykonał proof of concept w weekend. Celem jest zwiększenie ARR z licencji AI oraz umożliwienie klientom integracji własnych narzędzi AI z AMODIT.

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (priorytet - do realizacji w tym roku)

**Architektura:**
- MCP wystawia te same endpointy, z których korzysta AMODIT Copilot
- **NIE** jest to pełne API AMODIT - tylko wybrane funkcje Copilot
- Działanie w kontekście użytkownika (nie globalny dostęp)
- Logowanie zapytań AI (audyt, śledzenie co AI robiło)

**Wartość biznesowa:**
- **Rossmann** - zamówił, gotowy płacić (proof of concept na 3 miesiące):
  - Wersja standard przez 3 miesiące (~4000 zł/miesiąc)
  - Chce wersję advanced po PoC
  - Szacunkowo: 50 000 zł rocznie (2 serwery)
  
- **Inne klienci zainteresowani:** Polpharma, AmRest
- Możliwość sprzedaży kilku dużym klientom = ~200 000 zł rocznego przychodu

**Szczegóły techniczne:**
- Podłączenie do AMODIT Copilot (nie bezpośrednio do AMODIT API)
- Wystawione endpointy kontrolowane przez AMODIT
- Kontekst użytkownika (uprawnienia użytkownika który wywołuje)
- Audyt i logowanie zapytań AI

### Zidentyfikowane ryzyka

- **Wydajność** - AI może pytać nieoptymalne zapytania, obciążenie systemu
- **Bezpieczeństwo** - wymaga dokładnej weryfikacji uprawnień i audytu
- **Długa droga do produkcji** - PoC to nie wersja produkcyjna (stabilność, testy, security)

### Zadania / Dalsze kroki

- **Mateusz:** Kontynuować rozwój MCP (cel: wersja testowa w tym roku)
- **Janusz:** Weryfikacja wydajności i bezpieczeństwa przed wersją produkcyjną
- **Przemysław:** Przygotować wersję testową dla Rossmann, Polpharma, AmRest (środowisko testowe)

### Punkty otwarte

- Testy wydajnościowe - jak MCP wpłynie na obciążenie systemu
- Testy bezpieczeństwa - audyt uprawnień, logowanie
- Finalna decyzja o poziomie licencji AI (advanced dla MCP?)

---

## 6. AI dla konsultantów (bez licencji klienta)

**Komponent:** AMODIT Copilot / AI

### Kontekst i cel

Mechanizm umożliwiający konsultantom AMODIT używanie funkcji AI (np. generowanie dokumentacji, generowanie procesów) u klientów którzy nie posiadają licencji AI. Celem jest przyspieszenie pracy konsultantów oraz demonstracja wartości AI klientom (zachęta do zakupu licencji).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Detekcja adresu email (@amodit.pl, @astrafox.pl) | Funkcje AI działają dla użytkowników z domeną firmową | 💡 Propozycja - ryzyko oszustwa |
| OAuth + domena firmowa | Tylko logowanie przez OAuth (konto firmowe) aktywuje AI | ✅ Preferowane - bezpieczniejsze |
| Token czasowy | Konsultant generuje token czasowy do użycia AI | 💡 Propozycja - najbezpieczniejsze |
| Wewnętrzne hasło | Dodatkowe hasło do aktywacji AI dla konsultantów | 💡 Propozycja - dodatkowe zabezpieczenie |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (do ustalenia szczegółów)

**Preferowane rozwiązanie (wstępne):**
- Logowanie przez OAuth (konto firmowe) + domena @amodit.pl lub @astrafox.pl
- Klient może włączyć/wyłączyć możliwość używania AI przez konsultantów
- Ewentualnie dodatkowe zabezpieczenie (token czasowy lub wewnętrzne hasło)

**Uzasadnienie biznesowe:**
- Konsultanci pracują szybciej (generowanie dokumentacji, procesów)
- Demonstracja wartości AI klientom (zachęta do zakupu licencji)
- Przyszły rok: skracanie wdrożeń i zwiększanie przychodów przez narzędzia AI

### Zidentyfikowane ryzyka

- **Oszustwo klienta** - klient może zmienić adres email i używać AI bez licencji (niskie ryzyko)
- **Ryzyko biznesowe** - klient może żądać darmowego generowania dokumentacji w ramach umowy serwisowej

### Zadania / Dalsze kroki

- **Janusz:** Zaprojektować mechanizm autoryzacji (OAuth + domena lub token czasowy)
- **Zespół:** Ustalić czy klient może wyłączyć AI dla konsultantów

### Punkty otwarte

- Finalna decyzja o mechanizmie autoryzacji (OAuth vs token czasowy)
- Czy klient może wyłączyć AI dla konsultantów?
- Jak obsłużyć sytuację gdy klient żąda darmowego generowania dokumentacji?

---

## 7. Integracja z Google Gemini dla OCR (Vasco)

**Komponent:** AMODIT AI OCR

### Kontekst i cel

Podłączenie Google Gemini jako alternatywnego modelu OCR dla klienta Vasco. Klient wykonał proof of concept z Gemini i chce używać tego modelu zamiast Azure OCR. Celem jest utrzymanie klienta oraz możliwość chwalenia się współpracą z różnymi modelami AI (Google, OpenAI, Azure).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Transformacja formatu Gemini → Azure | Gemini zwraca dane w innym formacie, transformacja do formatu Azure, reszta heurystyk bez zmian | 💡 Propozycja - prostsze rozwiązanie |
| Przepisanie heurystyk dla Gemini | Odwzorowanie wszystkich heurystyk (kontrola tabel, sumy, VAT) dla formatu Gemini | ⏸️ Odroczona - bardziej czasochłonne |
| Użycie promptu klienta | Użycie promptu który klient przekazał (LLM od początku, nie model OCR) | 💡 Propozycja - do przetestowania |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (do realizacji - priorytet klient)

**Podejście:**
1. Podłączyć Google Gemini (1-2 dni - Mateusz)
2. Przetestować z promptem klienta lub własnym promptem
3. Zmodyfikować prompt aby zwracał dane w formacie który AMODIT oczekuje
4. Jeśli potrzeba: transformacja formatu Gemini → format Azure (aby heurystyki zadziałały)

**Uzasadnienie biznesowe:**
- Utrzymanie klienta Vasco (kilkadziesiąt tysięcy zł rocznie)
- Możliwość chwalenia się współpracą z różnymi modelami (Google, OpenAI, Azure)
- Google Gemini może być tańszy niż dedykowany model OCR

**Szczegóły techniczne:**
- Obecny proces: model visionowy + model do paragonów → LLM 4.1 (uzupełnianie) → heurystyki (tabele, sumy, VAT)
- Nowy proces (Gemini): LLM od początku (nie model OCR) → transformacja formatu → heurystyki

### Zadania / Dalsze kroki

- **Mateusz:** Podłączyć Google Gemini (1-2 dni)
- **Zespół:** Przetestować z promptem klienta lub własnym
- **Zespół:** Zdecydować czy transformacja formatu czy przepisanie heurystyk

### Punkty otwarte

- Czy transformacja formatu wystarczy czy trzeba przepisać heurystyki?
- Czy Google Gemini będzie tańszy niż Azure OCR?

---

## 8. Zarządzanie projektami i automatyzacja przez AI

**Komponent:** Organizacja pracy DEV

### Kontekst i cel

Automatyzacja zarządzania projektami przez AI. Janusz pracuje nad mechanizmem który automatycznie generuje cele sprintów z transkrypcji spotkań, klasyfikuje zgłoszenia na backlogu (inicjatywa, PBI, epic) oraz przeformułowuje opisy zadań. Celem jest oszczędność czasu menedżerów oraz standaryzacja procesów.

### Decyzja / Ustalenie

**Status:** ✅ W realizacji (Janusz)

**Funkcjonalności:**

1. **Automatyczne generowanie celów sprintów:**
   - Z transkrypcji spotkań planowania
   - AI zna kontekst (poprzednie MVP, roadmapa, projekty)
   - Wymaga rewizji przez Janusza/Damiana przed zatwierdzeniem

2. **Klasyfikacja zgłoszeń na backlogu:**
   - Agent ocenia czy zgłoszenie to inicjatywa, PBI czy epic
   - Przeformułowuje opisy zadań (tryb dokonany, lepsze nazewnictwo)
   - Przekazane Kamilowi i Damianowi do użycia

3. **Pilnowanie roadmapy:**
   - Weryfikacja czy cele sprintów są zgodne z roadmapą
   - Alerty gdy coś odbiega od planu

**Uzasadnienie biznesowe:**
- Oszczędność czasu menedżerów (automatyzacja planowania)
- Standaryzacja procesów (niezależnie kto planuje, proces jest ten sam)
- Lepsza komunikacja priorytetów do zespołu
- Możliwość mierzenia efektów (OKR, KPI)

**Cele do mierzenia (KPI):**
- Mniejsza liczba błędów w nowych wersjach (cel: zero błędów przy przekazaniu do klienta)
- Mniej powracania do tych samych tematów
- Szybsze dowożenie projektów

### Zadania / Dalsze kroki

- **Janusz:** Dokończyć mechanizm automatycznego generowania celów sprintów
- **Janusz:** Wdrożyć mechanizm klasyfikacji backlogu (już przekazane Kamilowi i Damianowi)
- **Przemysław:** Dodać uzasadnienie biznesowe do celów sprintów (co to da finansowo)

### Punkty otwarte

- Jak mierzyć efekty (OKR, KPI) - np. liczba błędów, czas dowożenia projektów
- Jak powiązać cele sprintów z celami strategicznymi (przeliczenie na pieniądze)

---

## 9. Filozofia planowania i projektowania

**Komponent:** Organizacja pracy DEV

### Kontekst i cel

Dyskusja o filozofii pracy zespołu - więcej czasu na planowanie i projektowanie, mniej na poprawianie błędów. Janusz wskazuje że im więcej czasu poświęcą menedżerowie (Kamil, Damian, Janusz) na planowanie, tym szybciej idzie implementacja.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (filozofia pracy)

**Zasady:**
- "5 godzin rozmowy oszczędza 5 dni pracy programisty" (odwrotnie: "10 minut rozmowy oszczędza 5 dni pracy programisty")
- Więcej czasu na planowanie, projektowanie, uzgodnienia = szybsza implementacja
- Prototypowanie po 2 godzinach pracy programisty (szybka weryfikacja) zamiast tygodnia implementacji
- Filtrowanie błędów w projektowaniu zanim trafią do wytworzenia
- Przykład: JRWA - uproszczona koncepcja, Marek zrobi w 1-2 dni

**Uzasadnienie:**
- Mniej błędów w produkcji
- Szybsze dowożenie projektów
- Mniej powracania do tych samych tematów
- Programiści nie muszą zgadywać co jest ważniejsze

### Zadania / Dalsze kroki

- **Kamil, Damian, Janusz:** Kontynuować filozofię "więcej planowania, mniej poprawek"
- **Zespół:** Mierzyć efekty (liczba błędów, czas dowożenia)

---

## 10. Standaryzacja procesów przez AI

**Komponent:** Organizacja pracy (ogólnie)

### Kontekst i cel

Dyskusja o standaryzacji procesów w firmie przez AI. Przykład: ocena zgłoszeń od klientów (budżet, koszt, priorytet) przez LLM - niezależnie kto ocenia, proces jest ten sam. Marketing już używa tego podejścia (ocena leadów przez LLM w Google Drive).

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (do wdrożenia w różnych obszarach)

**Przykłady standaryzacji:**

1. **Ocena zgłoszeń od klientów:**
   - LLM zadaje serię pytań: budżet, koszt, priorytet
   - Klasyfikacja: robimy / zastanówmy się / nie robimy (brak budżetu)
   - Może być zintegrowane z procesem w AMODIT

2. **Ocena leadów (marketing):**
   - LLM ocenia czy lead pasuje do segmentu
   - Generuje odpowiedź do klienta (obsługujemy / nie obsługujemy)
   - Już wdrożone w marketingu

3. **Wyceny dla klientów:**
   - Problem: klient wysyła wiele wersji wymagań, różne kanały komunikacji
   - Rozwiązanie: klient ma dostęp do procesu wyceny w AMODIT, wpisuje komentarze bezpośrednio
   - LLM ocenia kompletność wymagań, pyta o brakujące informacje

**Korzyści:**
- Niezależnie kto ocenia, proces jest ten sam (standaryzacja)
- Nie trzeba szkolić nowych pracowników (LLM już wie jak oceniać)
- Pracownicy uczą się z odpowiedzi LLM (jak oceniać w przyszłości)
- LLM może wykrywać badanie konkurencji (czy to realne zapytanie?)

### Zadania / Dalsze kroki

- **Janusz:** Rozważyć standaryzację procesu wyceny (dostęp klienta do AMODIT, LLM ocenia kompletność)
- **Zespół:** Zidentyfikować inne procesy do standaryzacji przez AI

---

## Podsumowanie organizacyjne

**Sprzęt:**
- Janusz rozważa MacBook Pro (32 GB RAM, 1 TB dysk) vs MacBook Air
- Główny cel: więcej pamięci (obecnie 16 GB, swap ciągle używany) i większy dysk (obecnie 256 GB prywatny)
- Wątpliwości: Pro jest mocniejszy (GPU dla lokalnych modeli AI) ale głośniejszy i cięższy
- Decyzja: Janusz sprawdzi w iSpot jak Pro hałasuje, potem finalna decyzja
- Przemysław: spoko, to inwestycja na lata

**AI tools:**
- Janusz: Claude (brak tokenów, rozważa Max Plan), QwQ (inżynierski styl, konkretny)
- Przemysław: GPT-4, Gemini (dobra analiza, ale teksty "drewniane", wymyśla pojęcia po angielsku)
- Gemini: trzeba uczyć aby nie upiększał tekstów i nie wymyślał pojęć
