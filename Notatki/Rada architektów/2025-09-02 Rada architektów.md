# Rada Architektów – 2025-09-02

**Powiązane projekty:**
- `cross-cutting/Automatyzacja-dokumentacji-AI` – temat 1
- `moduly/Edytor-procesow – tematy 2, 3

---

## 1. Dokumentacja projektowa z wykorzystaniem AI

**Projekt:** `cross-cutting/Automatyzacja-dokumentacji-AI`

### Kontekst i Problem

Janusz przedstawił metodę tworzenia dokumentacji projektowej z wykorzystaniem AI, która znacznie przyspiesza proces od pomysłu do realizacji. Problem polega na tym, że zespół dużo mówi podczas spotkań (szkolenia, Daily, retrospekcje), ale mało z tego wykorzystuje – transkrypcje są nagrywane, ale nie są przetwarzane na ustrukturyzowaną dokumentację. Metoda wykorzystuje narzędzia do transkrypcji (Super Whisper) i AI (Copilot, Gemini, v0) do przekształcania mówionego języka w eleganckie artykuły dokumentacyjne.

### Zidentyfikowane Ryzyka

- Brak standaryzacji słownictwa w dokumentacji
- Ryzyko utraty niuansów przy automatycznym przetwarzaniu
- Potrzeba weryfikacji i korekty wygenerowanych artykułów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Pisanie dokumentacji ręcznie | Tradycyjne pisanie artykułów | ❌ Odrzucona – zbyt czasochłonne (5x dłużej niż mówienie) |
| Mówienie + AI przetwarzanie | Nagranie transkrypcji + prompt do AI | ✅ Wybrana – skraca czas od pomysłu do realizacji dziesięciokrotnie lub więcej |
| Jeden artykuł na wiele tematów | Artykuł wprowadzający + szczegóły | ❌ Odrzucona – jeden artykuł = jeden temat |
| Artykuły powiązane | Osobne artykuły z linkami między sobą | ✅ Wybrana – lepsza organizacja i nawigacja |

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzenie metody tworzenia dokumentacji z wykorzystaniem AI jako standardowego narzędzia w zespole. Metoda składa się z kilku kroków:

1. **Nagranie transkrypcji:**
   - Użycie narzędzia Super Whisper do nagrywania i automatycznej transkrypcji
   - Mówienie naturalnym językiem (z zająknięciami, dygresjami – AI to wyczyści)

2. **Przetwarzanie przez AI:**
   - Użycie odpowiedniego promptu w zależności od typu dokumentu:
     - **Przegląd funkcjonalności** – opis funkcjonalności, jej przeznaczenia, problemów które rozwiązuje
     - **Poradnik how-to** – instrukcja krok po kroku dla użytkownika końcowego
     - **Poradnik how-to dla administratora** – bardziej techniczny, dla administratorów
     - **Artykuł koncepcyjny** – omówienie szerszej idei
     - **FAQ** – odpowiedzi na konkretne pytania (np. "Nie widzę Copilota, co mam zrobić?")
     - **Artykuł techniczny** – dogłębna wiedza techniczna

3. **Standaryzacja słownictwa:**
   - Utworzenie słownika w Google Sheets (lub podobnym narzędziu)
   - Słownik zawiera mapowanie: jak mówimy → jak powinno być w dokumentacji
   - Przykład: "procedura, proces, workflow, przepływ pracy" → "procesy"
   - Słownik jest dołączany do promptu, aby AI używało ustandaryzowanego słownictwa

4. **Zasady:**
   - Jeden artykuł = jeden temat (nie łączyć wielu funkcjonalności w jeden artykuł)
   - Artykuły powiązane są linkowane między sobą
   - Przykład: zamiast jednego artykułu "Nowy sidebar" z wszystkimi funkcjonalnościami, osobne artykuły: "Jak wyszukać w menu", "Jak zwinąć menu", "Jak przypiąć raport"

**Szczegóły techniczne:**
- Narzędzie: Super Whisper (nagrywanie + transkrypcja)
- AI: Copilot, Gemini, v0 (przetwarzanie transkrypcji)
- Format promptu: "Jesteś ekspertem od komunikacji produktowej. Przekształć surową transkrypcję w ustrukturyzowany artykuł..."
- Słownik: Google Sheets (lub podobne) z mapowaniem terminów
- Publikacja: Azure DevOps Wiki

### Zadania

- **[Janusz Bossak]:** Udostępnienie promptów dla różnych typów artykułów zespołowi → termin: [wykonane podczas spotkania]
- **[Wszyscy]:** Rozpoczęcie tworzenia dokumentacji metodą AI → termin: [natychmiast]
- **[Janusz Bossak]:** Utworzenie i udostępnienie słownika terminów w Google Sheets → termin: [w trakcie]

### Punkty otwarte

- Jak często aktualizować słownik terminów?
- Czy potrzebny jest proces review wygenerowanych artykułów przed publikacją?
- Jak obsłużyć przypadki, gdy AI zadaje pytania do eksperta (format "Pytanie do eksperta")?

---

## 2. Widok szablonów w procesach – migracja do React

**Projekt:** `moduly/Edytor-procesow

### Kontekst i Problem

Damian przedstawił projekt widoku szablonów w procesach stworzony z wykorzystaniem AI (v0) na podstawie System Design. Obecny widok szablonów jest w starszej technologii i wymaga modernizacji do React. Projekt obejmuje zarówno odtworzenie obecnej funkcjonalności, jak i propozycje nowych funkcji (podgląd, drag and drop, usuwanie zbiorcze).

### Zidentyfikowane Ryzyka

- Zbyt wiele nowości może wydłużyć czas projektowania, testowania i wydania
- Ryzyko odejścia od standardów UI/UX AMODIT (przyciski po lewej vs prawej stronie)
- Brak jasności co jest MVP, a co wersją max

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wersja MVP – tylko odtworzenie | Przeniesienie obecnej funkcjonalności do React bez zmian | ✅ Wybrana – szybkie dostarczenie, minimalne ryzyko |
| Wersja max – wszystkie nowości | Podgląd, drag and drop, usuwanie zbiorcze, widok kafelkowy, foldery | ⏸️ Odroczona – do rozważenia po MVP |
| Widok kafelkowy z mini podglądem | Kafelki z pierwszą stroną dokumentu jako podglądem | ⏸️ Odroczona – może być przydatne przy wielu szablonach |
| Foldery do organizacji szablonów | Grupowanie szablonów w foldery | ⏸️ Odroczona – przydatne przy dużej liczbie szablonów |
| Biblioteka szablonów wspólnych | Centralne miejsce dla szablonów używanych w wielu procesach | ⏸️ Odroczona – wymaga weryfikacji potrzeb klientów |

### Decyzja

**Status:** ✅ Zatwierdzone

**Wersja MVP:**
- Przeniesienie obecnej funkcjonalności do React
- Zachowanie obecnego układu i logiki działania
- Dodanie drag and drop do zmiany kolejności szablonów (zamiast przycisków góra/dół)
- Ewentualnie usuwanie zbiorcze (zaznaczenie wielu + usunięcie)
- Kolumna "Etapy" (zapomniana w pierwszej wersji projektu)
- Kolumna "Uprawnienia i etapy" w jednej kolumnie (są ze sobą powiązane)
- Przycisk "Dodaj" po lewej stronie (zgodnie ze standardem AMODIT)
- Wyszukiwanie i filtry po prawej stronie (nowy standard)
- Szczegóły z przyciskiem "Pobierz" (i w przyszłości "Edytuj")
- Podgląd dokumentu (użycie istniejącego okienka podglądu)

**Wersja max (do rozważenia później):**
- Widok kafelkowy z mini podglądem pierwszej strony
- Foldery do organizacji szablonów
- Biblioteka szablonów wspólnych dla wielu procesów
- Edycja szablonów z poziomu AMODIT (połączenie z Office 365)

**Szczegóły techniczne:**
- Technologia: React
- Biblioteka UI: Ant Design (z dostosowaniem do wyglądu AMODIT)
- Drag and drop: do zmiany kolejności szablonów
- Filtry: po ustawieniach, po plikach, po temacie
- Podgląd: użycie istniejącego okienka podglądu dokumentów
- Kolumny: Nazwa, Etapy (uprawnienia i etapy razem), Szczegóły, Podgląd

**Uwagi:**
- Projekt stworzony przez v0 na podstawie System Design
- v0 nie zawsze poprawnie używa komponentów Ant Design (robi po swojemu)
- Ikony nie są MDI (Material Design Icons) – wymagają dostosowania do ikon Zender
- Wymagane dostosowanie do standardów UI AMODIT

### Zadania

- **[Damian Kamiński]:** Dopracowanie szczegółów projektu zgodnie z uwagami → termin: na Design (12:30)
- **[Damian Kamiński]:** Dodanie kolumny "Etapy" do projektu
- **[Damian Kamiński]:** Połączenie kolumn "Uprawnienia" i "Etapy" w jedną
- **[Damian Kamiński]:** Przeniesienie przycisku "Dodaj" na lewą stronę
- **[Damian Kamiński]:** Przeniesienie wyszukiwania i filtrów na prawą stronę
- **[Filip Liwiński]:** Przełożenie obecnych uprawnień na nową tabelkę (pierwsze zadanie) → termin: [do ustalenia]

### Punkty otwarte

- Czy usuwanie zbiorcze powinno być w MVP?
- Jak obsłużyć przypadek, gdy szablon korzysta z wielu zmiennych (nie tylko pól)?
- Czy potrzebny jest widok kafelkowy w MVP?
- Jak zaimplementować edycję szablonów z poziomu AMODIT (połączenie z Office 365)?

---

## 3. Matryca uprawnień dla pól formularza

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

Kamil przedstawił projekt matrycy uprawnień dla pól formularza stworzony z wykorzystaniem AI (v0). Obecny interfejs zarządzania uprawnieniami jest nieintuicyjny i wymaga wielu kliknięć. Nowa matryca ma pokazywać wszystkie pola, sekcje i tabele wraz z uprawnieniami na wszystkich etapach procesu w jednym widoku, umożliwiając masowe zmiany uprawnień.

### Zidentyfikowane Ryzyka

- Przy dużej liczbie etapów (10+) matryca może być nieczytelna
- Różne kombinacje uprawnień między polami mogą utrudniać masowe zmiany
- Ryzyko błędów przy masowych zmianach uprawnień

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Obecny interfejs | Edycja uprawnień pojedynczo dla każdego pola | ❌ Odrzucona – zbyt dużo kliknięć, nieintuicyjne |
| Matryca z ikonami i tekstem | Przy małej liczbie etapów ikona + tekst | ✅ Wybrana – bardziej czytelne |
| Matryca tylko z ikonami | Przy dużej liczbie etapów tylko ikony | ✅ Wybrana – oszczędność miejsca |
| Masowa zmiana z wyzerowaniem | Wyzerowanie uprawnień przy różnicach między polami | ❌ Odrzucona – zbyt restrykcyjne |
| Masowa zmiana z zachowaniem różnic | Zachowanie obecnych uprawnień, nadpisanie tylko wybranych etapów | ✅ Wybrana – bardziej elastyczne |
| Filtry po sekcji i etapie | Możliwość zawężenia widoku matrycy | ✅ Wybrana – przydatne przy dużych procesach |
| Masowa zmiana sekcji | Możliwość zaznaczenia wielu sekcji | ❌ Odrzucona – rzadko używane, można zrobić pojedynczo |

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzenie nowej matrycy uprawnień dla pól formularza z następującymi funkcjonalnościami:

**Podstawowe funkcje:**
- Wyświetlanie wszystkich pól, sekcji i tabel w jednym widoku
- Kolumny dla każdego etapu procesu z uprawnieniami (edycja, odczyt, ukryte, wymagane)
- Dziedziczenie uprawnień z sekcji/tabeli oznaczane specjalnym znacznikiem
- Możliwość zerwania dziedziczenia i ustawienia indywidualnych uprawnień
- Wyjątki per użytkownik (edycja tylko dla X, ukryte dla Y)
- Przełącznik między użytkownikami zewnętrznymi i wewnętrznymi (jeśli włączone w ustawieniach systemowych)

**Wyświetlanie:**
- Przy małej liczbie etapów (1-3): ikona + tekst
- Przy dużej liczbie etapów (10+): tylko ikony, zamrożone pierwsze 2 kolumny (nazwa pola, typ)
- Sekcje oznaczone na szaro, możliwość zwijania
- Tabele z możliwością zwijania

**Masowe zmiany:**
- Zaznaczenie wielu pól → przycisk "Edytuj zaznaczone" na dole
- Okno masowej zmiany uprawnień:
  - Domyślnie: "Nie zmieniaj" (pozostaw obecne) dla każdego etapu
  - Możliwość wyboru uprawnienia dla wybranych etapów
  - Zmiana dotyczy tylko głównych uprawnień (edycja, odczyt, ukryte, wymagane)
  - Wyjątki per użytkownik pozostają bez zmian
- Opisowe prezentowanie uprawnień: "Ogólnie edycja, ale tak naprawdę ta edycja jest tylko dla użytkownika X, dla pozostałych pole jest ukryte"

**Filtry:**
- Filtr po sekcji (zawężenie widoku do wybranej sekcji)
- Filtr po etapie (wyświetlenie tylko wybranych etapów)
- Przydatne przy dużych procesach (15-20 etapów)

**Szczegóły techniczne:**
- Technologia: React
- Biblioteka UI: Ant Design (z dostosowaniem)
- Tabele z zaokrągleniami (zgodnie z Ant Design)
- Ikony: dostosowanie do ikon Zender (nie MDI)
- Zamrożone kolumny: pierwsze 2 kolumny przy przewijaniu w poziomie
- Zamrożony nagłówek: przy przewijaniu w pionie

**Uwagi:**
- Projekt stworzony przez v0, wymaga dostosowania do standardów AMODIT
- v0 nie zawsze poprawnie używa komponentów Ant Design
- Wymagane testowanie z różną liczbą etapów (1-2, 5, 10+)

### Zadania

- **[Kamil Dubaniowski]:** Dopracowanie szczegółów projektu zgodnie z uwagami → termin: [w trakcie]
- **[Kamil Dubaniowski]:** Zwężenie kolumn z uprawnieniami (tekst "Wymagane" jako najdłuższy) → termin: [w trakcie]
- **[Kamil Dubaniowski]:** Dodanie opcji "Nie zmieniaj" (pozostaw obecne) w oknie masowej zmiany → termin: [w trakcie]
- **[Kamil Dubaniowski]:** Przygotowanie wariantów z różną liczbą etapów (1-2, 5, 10) do testowania → termin: [w trakcie]
- **[Kamil Dubaniowski]:** Dodanie filtrów po sekcji i etapie → termin: [w trakcie]
- **[Filip Liwiński]:** Przełożenie obecnych uprawnień na nową tabelkę (pierwsze zadanie) → termin: [do ustalenia]
- **[Filip Liwiński]:** Implementacja funkcjonalności masowej zmiany uprawnień → termin: [po pierwszym zadaniu]

### Punkty otwarte

- Jak obsłużyć przypadek, gdy pole ma różne uprawnienia na różnych etapach i użytkownik chce zmienić tylko jeden etap?
- Czy potrzebny jest podgląd uprawnień przed zapisaniem zmian?
- Jak walidować zmiany uprawnień (np. czy wymagane pole może być ukryte)?

---

## 4. Uwagi organizacyjne

### Spotkanie Trust Center

Zaplanowane spotkanie o 12:00 dotyczące problemów w Trust Center (limity dokumentów) zidentyfikowanych przez Marka i Łukasza.

### Dotacja

Przemek zapowiedział, że za chwilę będą oferty do podpisania związane z dotacją. Dla współpracowników kontraktowych musi być konkurs na każdego.

### Copilot – problemy z analizą procesów

Łukasz zgłosił problem z Copilotem przy próbie analizy procesów z PKF – jeden z procesów powoduje błąd "ups, coś poszło nie tak" mimo że proces jest trywialny. Problem przekazany do analizy Mateuszowi.

### Ceny Copilota

Rozmowa o podniesieniu cen Copilota, aby zarabiać na tej funkcjonalności. AI jest tańsze niż pracownik (np. Krystyna kosztowała kilka tysięcy złotych miesięcznie, AI kosztowałoby ułamek tego).

