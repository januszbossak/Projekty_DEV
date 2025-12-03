# Rada Architektów – 2025-09-11

**Powiązane projekty:**
- `integracje/Integracje-REST-multipart` – temat 1
- `klienci/Marba` – temat 1
- `moduly/e-Doreczenia` – temat 2
- `cross-cutting/Interfejs-sprawy` – temat 3
- `klienci/WIM` – temat 4
- `moduly/Modul-raportowy` – temat 4
- `cross-cutting/Tablica-ogloszen` – temat 5
- `moduly/Edytor-procesow-formularzy` – temat 6

---

## 1. CallRest – obsługa multipart form data dla wielu plików

**Projekt:** `integracje/Integracje-REST-multipart`, `klienci/Marba`

### Kontekst i Problem

Klient Marba potrzebuje możliwości wysyłania wielu plików (dynamiczna ilość, do 100 plików) do zewnętrznego Web Service'u za pomocą funkcji CallRest w formacie multipart form data. Obecny mechanizm CallRest wymaga definiowania wielu parametrów systemowych (parametr 1, parametr 2, itd.), co jest niepraktyczne przy dużej liczbie plików. Problem dotyczy również szerszego kontekstu – w przyszłości podobna potrzeba może pojawić się przy integracji z KSeF (faktury z załącznikami) oraz innymi systemami, które wymagają wysyłania wielu plików.

### Zidentyfikowane Ryzyka

- Niepraktyczność obecnego rozwiązania przy dużej liczbie plików (do 100)
- Potrzeba definiowania wielu parametrów systemowych zamiast jednego dynamicznego
- Ryzyko pojawienia się podobnych potrzeb u innych klientów (KSeF, inne integracje)
- Różne formaty wymagane przez różne systemy (multipart form data vs JSON z Base64)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Budowanie JSON-a dynamicznie w regule | Tworzenie JSON-a ze stringów w regule funkcji | ❌ Odrzucona – operacje na dużych stringach są zasobochłonne i niewydajne |
| Multipart form data w jednym parametrze | Definiowanie listy plików w jednym parametrze z użyciem separatorów (podobnie jak w headers) | ✅ Wybrana – rozwiązanie spójne z istniejącym mechanizmem headers (10.2), użycie Handlebars do budowania |
| JSON z Base64 dla wielu plików | Konwersja plików do Base64 i wysyłanie w JSON-ie | ⏸️ Odroczona – może być rozważona w przyszłości, ale multipart form data jest bardziej optymalne dla plików binarnych |
| Wiele parametrów systemowych | Obecne rozwiązanie z parametrem 1, 2, 3... | ❌ Odrzucona – niepraktyczne przy dużej liczbie plików |

### Decyzja

**Status:** ✅ Zatwierdzone

Implementacja obsługi wysyłania wielu plików w formacie multipart form data za pomocą funkcji CallRest. Rozwiązanie będzie analogiczne do istniejącego mechanizmu headers (wersja 10.2), gdzie zamiast wielu parametrów używa się jednego parametru z listą wartości oddzielonych separatorami.

**Szczegóły techniczne:**
- Format: multipart form data (nie JSON) – bardziej optymalny dla plików binarnych
- Mechanizm: jeden parametr z listą plików, podobnie jak w headers (10.2)
- Separator: pojedynczy dwukropek (`:`) – zgodnie z istniejącym mechanizmem headers (nie podwójny dwukropek)
- Budowanie: użycie Handlebars (konstrukcje "each", "if") do dynamicznego budowania listy plików w regule
- Format parametru: `file:FieldByName:nazwa_pola:nazwa_pliku` (przykład dla pojedynczego pliku)
- Możliwość wskazania pliku na 3 sposoby: ID pliku, nazwa pola, nazwa załącznika
- Możliwość zmiany nazwy pliku przy wysyłaniu
- Nowa linia oznacza nową parę klucz-wartość w multipart form data
- Dokumentacja: przykład dostępny na Wiki Wewnętrzne (CallRest, sekcja 10.2 – Headers)

**Uwaga:** Rozważano użycie podwójnego dwukropka (`::`) jako separatora dla większej niezawodności, ale uznano, że należy zachować spójność z istniejącym mechanizmem headers, który używa pojedynczego dwukropka. Zmiana separatora wymagałaby aktualizacji istniejących integracji.

**Szerszy kontekst:**
- W przyszłości może pojawić się potrzeba wysyłania wielu plików w formacie JSON (np. dla innych systemów)
- W takim przypadku należy opisać potrzebę biznesową i rozważyć osobne rozwiązanie
- Temat został odroczony do przyszłych Rad architektów

### Zadania

- **[Adrian Kotowski]:** Implementacja obsługi multipart form data dla wielu plików w CallRest → termin: do końca września 2025 (zlecenie Marba)
- **[Piotr Buczkowski]:** Weryfikacja i uwagi do propozycji Adriana → termin: [do ustalenia]
- **[Damian Kamiński]:** Opisanie potrzeby biznesowej dla wysyłania wielu plików w formacie JSON (jeśli zajdzie taka potrzeba) → termin: [do ustalenia]

### Punkty otwarte

- Czy w przyszłości będzie potrzeba wysyłania wielu plików w formacie JSON (zamiast multipart form data)?
- Jak obsłużyć przypadek, gdy różne systemy wymagają różnych formatów (multipart vs JSON)?
- Czy separator (pojedynczy dwukropek) jest wystarczająco niezawodny, czy może powodować problemy przy specjalnych nazwach plików?

---

## 2. e-Doręczenia – problemy na chmurze

**Projekt:** `moduly/e-Doreczenia`

### Kontekst i Problem

Klienci korzystający z e-Doręczeń na chmurze zgłaszają problemy z działaniem funkcjonalności. Daniel Reszka (konsultant) zgłasza, że klienci się denerwują z powodu ciągłych problemów. Adrian pracuje nad rozwiązaniem, ale brakuje wsparcia ze strony Poczty Polskiej. Problem dotyczy tylko klientów na chmurze – klienci On-Premise nie zgłaszają problemów.

### Zidentyfikowane Ryzyka

- Niska satysfakcja klientów korzystających z e-Doręczeń na chmurze
- Problemy z komunikacją – klienci nie wiedzą, że trwają prace nad rozwiązaniem
- Brak wsparcia ze strony Poczty Polskiej (zewnętrzny partner)
- Ryzyko utraty zaufania klientów do systemu

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Klienci sami kontaktują się z Poczta Polską | Klienci (szczególnie więksi) kontaktują się bezpośrednio z opiekunem handlowym Poczty Polskiej | ✅ Częściowo wdrożona – Adrian prosi klientów o kontakt z Poczta Polską, ale jako integrator nie może tego zrobić bezpośrednio |
| Komunikacja z Danielem Reszką | Poinformowanie Daniela o postępach prac | ✅ Wybrana – poprawa komunikacji, aby klienci wiedzieli że trwają prace |

### Decyzja

**Status:** ✅ Zatwierdzone

Adrian kontynuuje pracę nad rozwiązaniem problemów z e-Doręczeniami na chmurze. Wymagana jest poprawa komunikacji z Danielem Reszką, aby klienci wiedzieli, że trwają prace nad rozwiązaniem.

**Szczegóły:**
- Adrian pracuje nad rozwiązaniem problemów z e-Doręczeniami na chmurze
- Problem dotyczy tylko klientów na chmurze (klienci On-Premise nie zgłaszają problemów)
- Brak wsparcia ze strony Poczty Polskiej – jako integrator nie można bezpośrednio kontaktować się z Poczta Polską
- Klienci (szczególnie więksi) mogą sami kontaktować się z opiekunem handlowym Poczty Polskiej
- Wymagana komunikacja z Danielem Reszką o postępach prac

### Zadania

- **[Adrian Kotowski]:** Kontynuacja prac nad rozwiązaniem problemów z e-Doręczeniami na chmurze → termin: [w trakcie]
- **[Adrian Kotowski]:** Komunikacja z Danielem Reszką w wątku zgłoszenia – poinformowanie o postępach prac i zapewnienie, że ktoś się tym zajmuje → termin: [do ustalenia]

### Punkty otwarte

- Jak zapewnić lepsze wsparcie ze strony Poczty Polskiej dla klientów na chmurze?
- Czy problem dotyczy wszystkich klientów na chmurze, czy tylko niektórych?
- Jak długo potrwa rozwiązanie problemów z e-Doręczeniami na chmurze?

---

## 3. Historia spraw – wyświetlanie nazw pól w języku użytkownika

**Projekt:** `cross-cutting/Interfejs-sprawy`

### Kontekst i Problem

W historii spraw zapisywane są nazwy techniczne pól zamiast nazw wyświetlanych, co utrudnia interpretację historii przez użytkowników. Nazwy techniczne nie odpowiadają wyświetlanym nazwom, co powoduje problemy z czytelnością historii. Problem dotyczy również wartości słowników – zostały już poprawione (wyświetlają się w języku użytkownika), ale nazwy pól nadal są wyświetlane jako techniczne.

### Zidentyfikowane Ryzyka

- Nieczytelność historii spraw dla użytkowników końcowych
- Trudności w interpretacji zmian wartości pól
- Niespójność – wartości słowników są już poprawione, ale nazwy pól nie
- Problem dotyczy również wielojęzyczności – nazwy pól powinny być wyświetlane w języku użytkownika

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zapisanie ID pola + wyświetlanie bieżącej nazwy | Zapisanie ID pola w historii i wyświetlanie bieżącej nazwy wyświetlanej | ⏸️ Odroczona – większe wyzwanie, wymaga zmian w strukturze danych |
| Zapisanie nazwy technicznej + nazwy wyświetlanej w nawiasie | Zapisanie obu nazw w historii (techniczna + wyświetlana) | ❌ Odrzucona – zwiększa rozmiar historii, utrudnia analizę, problem z wielojęzycznością (która nazwa wyświetlana była w momencie zmiany?) |
| Wyświetlanie bieżącej nazwy wyświetlanej + tooltip z nazwą techniczną | Wyświetlanie nazwy wyświetlanej w języku użytkownika, tooltip z nazwą techniczną (jeśli różna) | ✅ Wybrana – szybka poprawka (ok. 1 godzina), poprawia czytelność bez zmiany struktury danych |
| Wyświetlanie zawsze obu nazw | Zawsze wyświetlanie nazwy wyświetlanej i technicznej | ❌ Odrzucona – nieczytelne, zajmuje za dużo miejsca |

### Decyzja

**Status:** ✅ Zatwierdzone

Zmiana wyświetlania historii spraw – zamiast nazw technicznych wyświetlane będą nazwy wyświetlane w języku użytkownika. Jeśli nazwa wyświetlana różni się od technicznej, po najechaniu na nazwę pola wyświetli się tooltip z nazwą techniczną.

**Szczegóły techniczne:**
- Wyświetlanie: nazwa wyświetlana (DisplayValue) w języku użytkownika
- Mechanizm: pobieranie DisplayValue z pola (z wersją językową, jeśli zdefiniowana, lub domyślną nazwą wyświetlaną)
- Tooltip: jeśli nazwa wyświetlana różni się od technicznej, tooltip z nazwą techniczną (tylko wtedy, gdy są różne)
- Implementacja: zmiana w kontrolerze (zwracanie DisplayValue zamiast Value), tooltip obsługiwany przez Bootstrap (atrybut `title` w span)
- Wartości słowników: już poprawione wcześniej (wyświetlają się w języku użytkownika)
- Szacowany czas: ok. 1 godzina pracy

**Uwaga:** Rozważano zapisanie ID pola i wyświetlanie bieżącej nazwy wyświetlanej, ale uznano to za większe wyzwanie wymagające zmian w strukturze danych. Obecne rozwiązanie jest szybką poprawką, która poprawia czytelność bez zmiany struktury danych.

**Szerszy kontekst:**
- Historia spraw jest częścią większego tematu – kompleksowego podejścia do historii (historia sprawy, historia biznesowa, historia pól)
- Temat został odroczony do przyszłych Rad architektów (rozważenie widoku zakładkowego z 3 zakładkami)
- Obecna poprawka jest rozwiązaniem doraźnym dla konkretnego zgłoszenia

### Zadania

- **[Piotr Buczkowski]:** Implementacja wyświetlania nazw wyświetlanych w historii spraw z tooltipem z nazwą techniczną (jeśli różna) → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Uzupełnienie acceptance criteria dla zadania → termin: [do ustalenia]

### Punkty otwarte

- Czy w przyszłości należy przejść na zapisywanie ID pola zamiast nazwy technicznej?
- Jak obsłużyć przypadek, gdy pole zostało usunięte (deaktywowane) – czy nadal można wyświetlić jego nazwę?
- Czy kompleksowe podejście do historii (widok zakładkowy) powinno być zaplanowane jako osobny projekt?

---

## 4. WIM – raport osadzony z checkboxami do zapisania stanu

**Projekt:** `klienci/WIM`, `moduly/Modul-raportowy`

### Kontekst i Problem

Klient WIM potrzebuje raportu osadzonego na sprawie, który będzie wyświetlał pozycje zamówienia z zewnętrznego źródła danych (na podstawie numeru zamówienia). Użytkownicy mają zaznaczać checkboxami, które pozycje są zgodne z fakturą, a następnie zapisać ten stan jako część sprawy. Obecnie raporty osadzone ze źródeł zewnętrznych nie obsługują edycji checkboxów ani zapisywania stanu.

### Zidentyfikowane Ryzyka

- Brak możliwości zapisania stanu checkboxów jako części sprawy
- Potrzeba rozbudowy mechanizmu raportów osadzonych o edycję checkboxów
- Ryzyko pojawienia się podobnych potrzeb u innych klientów (źródła statyczne/dynamiczne)
- Potencjalne problemy wydajnościowe przy dużych tabelkach (300+ pozycji)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Raport osadzony z edytowalnymi checkboxami | Rozbudowa raportów osadzonych o możliwość edycji checkboxów i zapisania stanu | ✅ Wybrana – rozwiązanie systemowe, spójne z istniejącym mechanizmem raportów |
| Edycja danych w źródle dynamicznym z formularza | Możliwość bezpośredniej edycji danych w źródle dynamicznym z poziomu formularza (bez raportu) | ⏸️ Odroczona – może być rozważona jako kolejny MVP w przyszłości |
| Tabelka AMODITowa na sprawie | Standardowa tabelka z możliwością edycji checkboxów | ❌ Odrzucona – dane pochodzą z zewnętrznego źródła, nie z CaseDefinition |

### Decyzja

**Status:** 🔍 Do weryfikacji / ⏸️ Częściowo odroczone

Rozbudowa mechanizmu raportów osadzonych o możliwość edycji checkboxów w źródłach zewnętrznych i zapisania stanu jako części sprawy. Rozwiązanie będzie wymagało Proof of Concept przed pełną implementacją.

**Szczegóły techniczne:**
- Raport osadzony ze źródła zewnętrznego (na podstawie numeru zamówienia)
- Możliwość zaznaczania checkboxów przez użytkowników
- Zapisanie stanu checkboxów jako część sprawy (nie w CaseDefinition, ale w źródle dynamicznym)
- Mechanizm podobny do istniejącego dla źródeł statycznych/dynamicznych (możliwość zapisania stanu)
- Wymagany Proof of Concept przed pełną implementacją

**Szerszy kontekst:**
- W przyszłości może pojawić się potrzeba bezpośredniej edycji danych w źródłach dynamicznych z poziomu formularza (bez raportu)
- Może to być rozważone jako kolejny MVP w przyszłości
- Temat dotyczy również źródeł statycznych/dynamicznych, które mogą wymagać edycji

### Zadania

- **[Damian Kamiński]:** Przygotowanie Proof of Concept dla raportu osadzonego z edytowalnymi checkboxami → termin: [do ustalenia]
- **[Damian Kamiński]:** Rozpisanie wymagań i zaakceptowanie rozwiązania → termin: [do ustalenia]

### Punkty otwarte

- Jak zapisać stan checkboxów jako część sprawy (w źródle dynamicznym, nie w CaseDefinition)?
- Czy rozwiązanie powinno być dostępne tylko dla raportów osadzonych, czy również dla innych typów raportów?
- Czy w przyszłości należy rozważyć bezpośrednią edycję danych w źródłach dynamicznych z poziomu formularza (bez raportu)?
- Jak obsłużyć przypadek, gdy dane w źródle zewnętrznym się zmienią (np. dodanie nowych pozycji zamówienia)?

---

## 5. Komunikaty statyczne (info bar) – informowanie użytkowników

**Projekt:** `cross-cutting/Tablica-ogloszen`

### Kontekst i Problem

Istnieje potrzeba informowania użytkowników o ważnych wydarzeniach (np. planowane przerwy w działaniu systemu, aktualizacje) bez konieczności wysyłania maili. Obecnie istnieje mechanizm info bar (pasek informacyjny), który został zaimplementowany przez Annę Skupińską w starym widoku, ale nie został przeniesiony do Reacta. Mechanizm działa tylko On-Premise (per serwer), a potrzebne jest również rozwiązanie dla chmury (zbiorcze zarządzanie).

### Zidentyfikowane Ryzyka

- Brak możliwości informowania użytkowników o ważnych wydarzeniach w sposób systemowy
- Konieczność wysyłania maili zamiast wyświetlania komunikatu w systemie
- Brak spójności między widokiem starym a Reactowym
- Różne potrzeby dla On-Premise (per serwer) vs chmura (zbiorcze zarządzanie)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wyświetlanie na stronie głównej | Pasek informacyjny na górze ekranu głównego (możliwość zamknięcia) | ✅ Wybrana – rozwiązanie docelowe, dostępne dla wszystkich użytkowników |
| Wyświetlanie na stronie logowania | Pasek informacyjny na stronie logowania | ⏸️ Częściowo – tylko dla informacji o przerwach w działaniu bazy danych (gdy system nie działa) |
| Zarządzanie przez ustawienia systemowe (On-Premise) | Interfejs w ustawieniach systemowych do zarządzania komunikatami | ✅ Wybrana dla On-Premise – każdy administrator może zarządzać komunikatami |
| Zarządzanie zbiorcze (chmura) | Narzędzie do zbiorczego zarządzania komunikatami dla wszystkich klientów na chmurze | ✅ Wybrana dla chmury – Łukasz może publikować komunikaty dla wszystkich klientów |

### Decyzja

**Status:** 🔍 Do weryfikacji / ⏸️ Częściowo odroczone

Przywrócenie i rozbudowa mechanizmu info bar (pasek informacyjny) do informowania użytkowników o ważnych wydarzeniach. Mechanizm istnieje w starym widoku, ale wymaga przeniesienia do Reacta i rozbudowy o zarządzanie dla chmury.

**Szczegóły techniczne:**
- Wyświetlanie: pasek informacyjny na górze ekranu głównego (podobnie jak informacja o Raportach Premium)
- Możliwość zamknięcia: użytkownik może zamknąć komunikat po przeczytaniu
- Wyświetlanie raz: komunikat wyświetla się raz (po zamknięciu nie pojawia się ponownie)
- Zarządzanie On-Premise: interfejs w ustawieniach systemowych do zarządzania komunikatami (per serwer)
- Zarządzanie chmura: narzędzie do zbiorczego zarządzania komunikatami dla wszystkich klientów (Łukasz może publikować komunikaty)
- Format: tekst w języku polskim i angielskim, zakres dat (od-do)
- Obecny stan: mechanizm istnieje w starym widoku (strona logowania), wymaga przeniesienia do Reacta
- Endpoint: `/api/info-bar` (zwraca komunikat, jeśli aktywny)

**Uwaga:** Rozważano wyświetlanie komunikatu na stronie logowania, ale uznano, że powinien być na stronie głównej (gdy system działa). Strona logowania może być używana tylko dla informacji o przerwach w działaniu bazy danych (gdy system nie działa).

**Szerszy kontekst:**
- Mechanizm może być używany do różnych informacji (przerwy w działaniu, aktualizacje, ważne komunikaty)
- Możliwość publikowania komunikatów z wyprzedzeniem (np. "dzisiaj o 18:00 system będzie niedostępny przez 15 minut")
- Rozwiązanie ma na celu zmniejszenie liczby maili i poprawę komunikacji z użytkownikami

### Zadania

- **[Anna Skupińska]:** Research – spisanie obecnego stanu mechanizmu info bar (co zostało zrobione, jakie były założenia) → termin: [do ustalenia]
- **[Anna Skupińska]:** Przygotowanie opisu wymagań dla docelowego rozwiązania → termin: [do ustalenia]
- **[Product Owner]:** Przypisanie zadania do odpowiedniej osoby po zakończeniu researchu → termin: [do ustalenia]

### Punkty otwarte

- Czy komunikat powinien być wyświetlany również na stronie logowania (dla informacji o przerwach w działaniu bazy danych)?
- Jak obsłużyć przypadek, gdy komunikat jest bardzo długi (czy powinien być skracany, czy wyświetlany w pełni)?
- Czy komunikat powinien być wyświetlany dla wszystkich użytkowników, czy tylko dla wybranych grup?
- Jak zapewnić, że komunikat nie będzie przeszkadzał użytkownikom (możliwość zamknięcia, wyświetlanie raz)?

---

## 6. Edytor formularzy – przełączanie między widokami (Edytor Graficzny, Lista, Matryca Uprawnień)

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

W edytorze formularzy występuje problem z przełączaniem między różnymi widokami (Edytor Graficzny, Lista, Matryca Uprawnień). Obecnie wybór formularza głównego (Formularz Główny, tabele) jest w środku ekranu, co zajmuje miejsce i nie jest intuicyjne. Przemek zaproponował przeniesienie wyboru formularza głównego na górny pasek (obok przełączania między Edytorem Graficznym a Listą), co pozwoli odzyskać jeden wiersz przestrzeni roboczej.

### Zidentyfikowane Ryzyka

- Utrata przestrzeni roboczej przez wybór formularza głównego w środku ekranu
- Nieintuicyjność – nie jest jasne, że wybór formularza głównego dotyczy edycji pól
- Brak spójności – różne miejsca przełączania (formularz główny vs Edytor Graficzny/Lista)
- Potencjalne problemy z długimi nazwami tabel (okienko może być bardzo szerokie)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Przeniesienie wyboru formularza głównego na górny pasek | Wybór formularza głównego obok przełączania Edytor Graficzny/Lista | ✅ Wybrana – odzyskanie przestrzeni roboczej, bardziej intuicyjne |
| Zostawienie wyboru w środku ekranu | Obecne rozwiązanie | ❌ Odrzucona – zajmuje miejsce, nieintuicyjne |
| Full screen dla edytora graficznego | Możliwość rozszerzenia edytora graficznego na pełny ekran (jak dashboard) | ⏸️ Odroczona – może być rozważona jako kolejne rozszerzenie |
| Usunięcie strzałki wstecz | Usunięcie strzałki wstecz po przeniesieniu wyboru na górny pasek | ✅ Wybrana – strzałka w środku ekranu wyglądałaby dziwnie |

### Decyzja

**Status:** ✅ Zatwierdzone

Przeniesienie wyboru formularza głównego na górny pasek (obok przełączania między Edytorem Graficznym a Listą). Dodanie nagłówka "Edytujesz formularz główny [nazwa]" oraz przycisku "Zobacz dla nazwy systemowe" (analogicznie do istniejących rozwiązań w innych miejscach systemu).

**Szczegóły techniczne:**
- Przeniesienie wyboru formularza głównego na górny pasek (obok Edytor Graficzny/Lista)
- Dodanie nagłówka: "Edytujesz formularz główny [nazwa]" (np. "Edytujesz formularz główny Komórki organizacyjne")
- Dodanie przycisku: "Zobacz dla nazwy systemowe" (obok nagłówka)
- Usunięcie strzałki wstecz (po przeniesieniu wyboru na górny pasek strzałka w środku ekranu wyglądałaby dziwnie)
- Usunięcie dolnego paska z wyborem formularza głównego (odzyskanie przestrzeni roboczej)
- Długie nazwy: skracanie z kropkami (np. "Formularz główny Komórki organizacyjne..." → "Formularz główny Komórki...")
- Przełączanie między Edytorem Graficznym a Listą: zachowanie kontekstu (jeśli jesteś w tabeli i przełączysz się na Listę, lista pokazuje pola z tej tabeli)

**Uwaga:** Rozważano możliwość full screen dla edytora graficznego (jak w dashboardzie), ale uznano to za kolejne rozszerzenie, które nie jest priorytetem w obecnej wersji.

**Szerszy kontekst:**
- Matryca Uprawnień będzie dodana w wersji wrześniowej (obecnie tylko Edytor Graficzny i Lista w wersji czerwcowej)
- W przyszłości może być rozważone dodanie sekcji "Reguły" po prawej stronie (dla pól i tabel)
- Reguły tabeli mogą być wyświetlane w sekcji "Reguły" po prawej stronie (zamiast osobnego miejsca)

### Zadania

- **[Przemysław Sołdacki]:** Przeniesienie wyboru formularza głównego na górny pasek (obok Edytor Graficzny/Lista) → termin: wersja czerwcowa
- **[Przemysław Sołdacki]:** Dodanie nagłówka "Edytujesz formularz główny [nazwa]" oraz przycisku "Zobacz dla nazwy systemowe" → termin: wersja czerwcowa
- **[Przemysław Sołdacki]:** Usunięcie strzałki wstecz oraz dolnego paska z wyborem formularza głównego → termin: wersja czerwcowa
- **[Przemysław Sołdacki]:** Obsługa długich nazw tabel (skracanie z kropkami) → termin: wersja czerwcowa

### Punkty otwarte

- Czy w przyszłości należy rozważyć możliwość full screen dla edytora graficznego?
- Czy reguły tabeli powinny być wyświetlane w sekcji "Reguły" po prawej stronie (zamiast osobnego miejsca)?
- Jak obsłużyć przypadek, gdy użytkownik przełączy się między Edytorem Graficznym a Listą podczas edycji tabeli (czy kontekst powinien być zachowany)?

