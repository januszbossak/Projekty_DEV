# Propozycja aktualizacji artykułu Wiki - AMODIT Copilot

**Data:** 2025-12-20  
**Źródło:** https://wiki.amodit.com/pl/baza-wiedzy/jak-przyspieszyc-tworzenie-procesow-i-dostep-do-wiedzy-w-2025-amodit-wprowadza-asystenta-ai-copilot/  
**Typ:** Propozycja aktualizacji treści

---

## 1. Kontekst

Artykuł na Wiki AMODIT opisuje funkcjonalności AMODIT Copilot w wersji MVP1 (wydanej we wrześniu 2025). Od tego czasu nastąpił znaczący rozwój projektu, a wiele nowych funkcjonalności jest w trakcie realizacji lub planowania. Niniejszy dokument zawiera propozycje aktualizacji artykułu w oparciu o aktualną bazę wiedzy projektowej.

---

## 2. Główne obszary wymagające aktualizacji

### 2.1 Nowe funkcjonalności dostarczone po MVP1

#### A. Generowanie dokumentacji procesów (MVP2 - w trakcie)

**Propozycja dodania sekcji:**

> **Automatyczne generowanie dokumentacji powdrożeniowej**
> 
> AMODIT Copilot potrafi teraz automatycznie wygenerować kompletną dokumentację techniczną procesu, oszczędzając konsultantom wdrożeniowym dziesiątki godzin pracy. Funkcjonalność obejmuje:
> - Automatyczny opis procesu na podstawie jego konfiguracji
> - Wizualizację diagramu etapów z poprawnymi proporcjami
> - Szczegółowe zestawienie pól formularza
> - Dokumentację reguł biznesowych z numeracją globalną
> - Opis restrykcji pól na poszczególnych etapach
> 
> **Wartość biznesowa:** Szacujemy, że funkcjonalność ta pozwala zaoszczędzić około 60 dni pracy działu wdrożeń rocznie (2-3 osobo-miesiące).
> 
> Dokumentacja może być generowana w formacie Word i jest dostępna dla administratorów systemowych oraz procesowych bezpośrednio z ustawień procesu.

**Uzasadnienie:** Funkcjonalność jest w fazie MVP (PoC gotowy, wydanie w grudniowej wersji - styczeń 2026). To znacząca wartość dodana, która powinna być komunikowana klientom.

---

#### B. Przesyłanie dokumentów do konwersacji

**Propozycja rozszerzenia sekcji "Dla Użytkowników Końcowych":**

> **Analiza dokumentów w czasie rzeczywistym**
> 
> Podczas rozmowy z Copilotem możesz przesłać dokument (PDF, Word, Excel) bezpośrednio do konwersacji. Copilot przeanalizuje jego treść i odpowie na pytania dotyczące dokumentu, np.:
> - "Jakie są kluczowe terminy w tej umowie?"
> - "Czy w tym regulaminie jest informacja o okresie wypowiedzenia?"
> - "Podsumuj najważniejsze punkty z tego raportu"

**Uzasadnienie:** Funkcjonalność dostarczona w październiku 2025 (Sprint review 2025-10-20).

---

#### C. Eksport wyników konwersacji

**Propozycja dodania:**

> **Eksport wyników do dokumentów**
> 
> Odpowiedzi uzyskane od Copilota można eksportować do formatów Word lub Markdown, co ułatwia dalsze wykorzystanie informacji w dokumentacji czy raportach. Funkcjonalność respektuje uprawnienia użytkownika do danych.

**Uzasadnienie:** POC dostępny (Sprint review 2025-11-03), funkcjonalność w MVP2.

---

### 2.2 Nowe kierunki strategiczne - MCP (Model Context Protocol)

**Propozycja dodania nowej sekcji:**

> ### Integracja z ekosystemem AI - Model Context Protocol (MCP)
> 
> AMODIT Copilot rozwija się w kierunku pełnej integracji z ekosystemem sztucznej inteligencji poprzez wsparcie dla **Model Context Protocol (MCP)** - uniwersalnego standardu komunikacji między systemami AI.
> 
> **Co to oznacza w praktyce?**
> 
> **1. AMODIT jako serwer MCP:**
> - Zewnętrzne narzędzia AI (np. Claude, ChatGPT, Cursor) mogą łączyć się z AMODIT i korzystać z jego funkcji
> - Możliwość zadawania pytań o procesy, dane czy raporty z poziomu ulubionych narzędzi AI
> - Bezpieczna autentykacja i kontrola uprawnień
> 
> **2. AMODIT jako klient MCP:**
> - Copilot może korzystać z zewnętrznych narzędzi i źródeł wiedzy
> - Integracja z wyszukiwarkami internetowymi, bazami wiedzy, narzędziami analitycznymi
> - Rozszerzenie możliwości Copilota o specjalistyczne funkcje (wykresy, diagramy, analizy SQL)
> 
> **Bezpieczeństwo:**
> - Mechanizm checkbox "Pozwól AI dostęp do tego procesu" na poziomie procesu
> - Pełne logowanie wszystkich działań AI (audyt)
> - Możliwość tworzenia kont systemowych z określonymi uprawnieniami dla agentów AI
> - Autentykacja OAuth i tokeny dostępu
> 
> **Status:** Prototyp gotowy, planowane wdrożenie produkcyjne w Q1 2026.
> 
> **Wartość biznesowa:** Klienci tacy jak Rossmann, Polpharma i AmRest wyrazili zainteresowanie tą funkcjonalnością. Szacowany dodatkowy przychód: ~200k zł rocznie.

**Uzasadnienie:** MCP to kluczowy element strategii rozwoju Copilota (Sprint review 2025-12-01, Notatka projektowa 2025-12-02, 2025-12-09). To innowacyjna funkcjonalność, która wyróżnia AMODIT na rynku.

---

### 2.3 Usprawnienia UX/UI

**Propozycja rozszerzenia sekcji o planowane usprawnienia:**

> **Planowane usprawnienia doświadczenia użytkownika:**
> - Lepsze wizualne wskaźniki "myślenia" modelu (spinner z informacją o aktualnej operacji)
> - Przeprojektowany interfejs bazy wiedzy zgodny z design systemem AMODIT
> - Sugestie pytań dla użytkowników ("Nie wiesz o co zapytać? Spróbuj...")
> - Możliwość zadawania pytań pojedynczo zamiast w bloku (bardziej naturalna konwersacja)

---

### 2.4 Aktualizacja sekcji "Bezpieczeństwo i Prywatność Danych"

**Propozycja rozszerzenia:**

> **Zgodność z AI Act i regulacjami UE:**
> 
> AMODIT Copilot został zaprojektowany z myślą o pełnej zgodności z europejskimi regulacjami dotyczącymi AI, w tym AI Act:
> - **Przejrzystość:** Pełna dokumentacja funkcji AI dostępna dla klientów
> - **Kontrola:** Klient decyduje, które funkcje AI są aktywne i jakie dane są przetwarzane
> - **Audyt:** Wszystkie operacje AI są logowane i dostępne do przeglądu
> - **Granularna kontrola:** Możliwość włączania/wyłączania dostępu AI do poszczególnych procesów i baz wiedzy
> - **On-premise:** Dla klientów z najwyższymi wymaganiami bezpieczeństwa możliwe jest wdrożenie modeli AI w infrastrukturze klienta
> 
> Więcej informacji o zgodności z AI Act: [link do amodit.pl/ai-act/]

**Uzasadnienie:** Temat zgodności z AI Act jest aktualny (konwersacja z Rossmann, grudzień 2025) i stanowi istotny argument sprzedażowy.

---

### 2.5 Aktualizacja FAQ

**Propozycja dodania nowych pytań:**

> **Pytanie 4: Czy mogę używać Copilota z poziomu innych narzędzi AI?**
> 
> Tak, w ramach integracji MCP (Model Context Protocol) planujemy umożliwić dostęp do funkcji AMODIT z poziomu narzędzi takich jak Claude, ChatGPT czy Cursor. Funkcjonalność będzie dostępna w Q1 2026 z pełnym zachowaniem bezpieczeństwa i uprawnień użytkownika.

> **Pytanie 5: Czy Copilot może generować dokumentację moich procesów?**
> 
> Tak, AMODIT Copilot potrafi automatycznie wygenerować kompletną dokumentację techniczną procesu, oszczędzając dziesiątki godzin pracy. Funkcjonalność jest dostępna dla administratorów systemowych i procesowych od wersji grudniowej (styczeń 2026).

> **Pytanie 6: Czy mogę przesłać dokument do analizy podczas rozmowy z Copilotem?**
> 
> Tak, możesz przesyłać dokumenty (PDF, Word, Excel) bezpośrednio do konwersacji z Copilotem. AI przeanalizuje treść dokumentu i odpowie na pytania dotyczące jego zawartości.

---

### 2.6 Aktualizacja sekcji "Dostępność i Dalsze Kroki"

**Propozycja rozszerzenia:**

> ### Roadmapa rozwoju
> 
> AMODIT Copilot jest aktywnie rozwijany. W najbliższych miesiącach planujemy:
> 
> **Q1 2026 (MVP2):**
> - Generowanie dokumentacji powdrożeniowej procesów
> - Serwer MCP - integracja z zewnętrznymi systemami AI
> - Przeprojektowany interfejs bazy wiedzy
> - Eksport wyników konwersacji do Word/Markdown
> - Usprawnienia bezpieczeństwa i zgodności z RODO
> 
> **Q2-Q3 2026 (MVP3):**
> - Dostęp do danych transakcyjnych (opcjonalny, włączalny per organizacja)
> - AI do automatycznego tłumaczenia formularzy
> - Usprawnienia bazy wiedzy (administratorzy, wersjonowanie treści, data ważności)
> - Analiza zbiorcza zależności między regułami
> - Automatyczne dodawanie tooltipów do pól
> 
> **Wizja długoterminowa - AI-driven workflow:**
> 
> Naszym celem jest ewolucja AMODIT w kierunku systemu "AI-driven workflow", gdzie złożone, deterministyczne reguły biznesowe będą mogły być zastępowane elastycznymi agentami AI. Zamiast kodować skomplikowane reguły if-else, będzie można zdefiniować "agenta AI", który na podstawie parametrów sprawy podejmie inteligentną decyzję (np. akceptacja, odrzucenie, eskalacja) wraz z uzasadnieniem.
> 
> To oznacza:
> - Szybsze wdrożenia (mniej kodowania, więcej konfiguracji)
> - Łatwiejsze utrzymanie (zmiany w modelu zamiast w kodzie)
> - Adaptacyjność (model może się uczyć i dostosowywać)

**Uzasadnienie:** Roadmapa jest dobrze udokumentowana (ROADMAPA.md), a wizja AI-driven workflow to kluczowy element strategii (projekt koncepcyjny AI-driven-workflow).

---

## 3. Sugestie dotyczące tonu i stylu

### 3.1 Większy nacisk na wartość biznesową

Obecny artykuł dobrze opisuje funkcjonalności, ale można mocniej podkreślić konkretne korzyści biznesowe:

- **Oszczędność czasu:** "~60 dni rocznie oszczędności działu wdrożeń" (generowanie dokumentacji)
- **Skrócenie wdrożeń:** "Skrócenie czasu od pomysłu do działającego prototypu o 70%"
- **ROI:** Konkretne przykłady oszczędności (np. LOT: ~6 dni dokumentacji)

### 3.2 Przykłady użycia z życia wzięte

Warto dodać konkretne case studies lub scenariusze:

> **Przykład z praktyki: Dział HR w firmie produkcyjnej**
> 
> Firma zatrudniająca 500 osób wgrała do bazy wiedzy Copilota wszystkie regulaminy wewnętrzne, polityki HR i procedury. Efekt? Pracownicy zamiast dzwonić do HR z pytaniami typu "Ile dni urlopu mi przysługuje?" czy "Jak zgłosić delegację?" - pytają Copilota. HR odnotował 40% spadek rutynowych zapytań, co pozwoliło skupić się na bardziej strategicznych zadaniach.

---

## 4. Propozycja nowej struktury artykułu

### Obecna struktura:
1. Wprowadzenie
2. Kluczowe możliwości (pigułka)
3. Problem
4. Rozwiązanie (funkcjonalności)
5. Bezpieczeństwo
6. FAQ
7. Dostępność

### Proponowana struktura:
1. **Wprowadzenie** (bez zmian)
2. **Kluczowe możliwości** (rozszerzone o nowe funkcje)
3. **Problem** (bez zmian)
4. **Rozwiązanie:**
   - Dla Twórców Procesów (rozszerzone)
   - Dla Użytkowników Końcowych (rozszerzone)
   - **NOWOŚĆ:** Dla Konsultantów Wdrożeniowych (generowanie dokumentacji)
   - **NOWOŚĆ:** Integracja z ekosystemem AI (MCP)
5. **Wartość biznesowa** (nowa sekcja - konkretne liczby, ROI, case studies)
6. **Bezpieczeństwo i zgodność** (rozszerzone o AI Act)
7. **FAQ** (rozszerzone)
8. **Roadmapa i wizja rozwoju** (nowa sekcja)
9. **Dostępność i kontakt** (bez zmian)

---

## 5. Kluczowe przesłania do przekazania

1. **AMODIT Copilot to nie tylko chatbot** - to kompleksowy asystent AI wspierający cały cykl życia procesu biznesowego
2. **Konkretne oszczędności** - ~60 dni rocznie dla działu wdrożeń, 70% skrócenie czasu prototypowania
3. **Innowacyjność** - MCP to technologia przyszłości, AMODIT jest w awangardzie
4. **Bezpieczeństwo i zgodność** - pełna zgodność z AI Act i regulacjami UE
5. **Ciągły rozwój** - jasna roadmapa, wizja AI-driven workflow

---

## 6. Rekomendacje dotyczące aktualizacji

### Priorytet 1 (krytyczne):
- Dodanie sekcji o generowaniu dokumentacji (MVP2, styczeń 2026)
- Aktualizacja FAQ o nowe pytania
- Dodanie informacji o przesyłaniu dokumentów do konwersacji

### Priorytet 2 (ważne):
- Dodanie sekcji o MCP
- Rozszerzenie sekcji o bezpieczeństwo (AI Act)
- Dodanie roadmapy rozwoju

### Priorytet 3 (nice to have):
- Dodanie case studies / przykładów z praktyki
- Reorganizacja struktury artykułu
- Dodanie sekcji o wartości biznesowej z konkretnymi liczbami

---

## 7. Uwagi końcowe

Artykuł na Wiki jest dobrym fundamentem, ale wymaga aktualizacji o nowe funkcjonalności i kierunki rozwoju. Kluczowe jest:

1. **Aktualność** - artykuł powinien odzwierciedlać stan na grudzień 2025 / styczeń 2026
2. **Konkretność** - więcej liczb, mniej ogólników
3. **Wizja** - pokazanie dokąd zmierza Copilot (MCP, AI-driven workflow)
4. **Compliance** - podkreślenie zgodności z regulacjami (AI Act)

**Sugerowany termin aktualizacji:** Styczeń 2026 (po wydaniu wersji grudniowej z generowaniem dokumentacji)

---

## Źródła

- Projekty/Moduly/AMODIT Copilot/PROJEKT.md
- Projekty/Moduly/AMODIT Copilot/ROADMAPA.md
- Projekty/Moduly/AMODIT Copilot/CHANGELOG.md
- Projekty/koncepcje/AI-driven-workflow/AI-driven-workflow.md
- Projekty/Roadmapa-AMODIT/AI które "myśli" – co to oznacza dla AMODIT w 2026.md
- Notatki projektowe z okresu wrzesień-grudzień 2025
