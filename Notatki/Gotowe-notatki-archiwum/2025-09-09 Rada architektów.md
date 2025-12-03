# Rada Architektów – 2025-09-09

**Powiązane projekty:**
- `cross-cutting/Podglad-plikow` – tematy 1, 2
- `moduly/Modul-raportowy` – tematy 3, 4
- `cross-cutting/Szablony-maili-systemowych` – temat 5

---

## 1. Podgląd plików tekstowych – naprawa i rozszerzenie

**Projekt:** `cross-cutting/Podglad-plikow`

### Kontekst i Problem

Występuje problem z wyświetlaniem plików tekstowych (.txt) w systemie AMODIT. Pliki .txt nie wyświetlają się w podglądzie, tylko są pobierane, mimo że wcześniej działały poprawnie. Dodatkowo występuje niespójność w zachowaniu między podglądem na sprawie a podglądem w raporcie: na sprawie plik .txt jest od razu pobierany, a w raporcie pojawia się panel podglądu, który próbuje wyświetlić plik, ale ostatecznie nie pokazuje treści.

Pojawiła się również potrzeba rozszerzenia podglądu o inne formaty tekstowe: JSON, XML, Markdown (.md), HTML oraz pliki logów. Szczególnie istotne jest wsparcie dla Markdown, który jest coraz częściej używany.

### Zidentyfikowane Ryzyka

- Brak spójności w zachowaniu podglądu między różnymi miejscami w systemie (sprawa vs raport)
- Utrata funkcjonalności, która wcześniej działała (regresja)
- Brak wsparcia dla popularnych formatów tekstowych (JSON, XML, Markdown)
- Ryzyko bezpieczeństwa przy wyświetlaniu HTML bez odpowiednich zabezpieczeń
- Problemy wydajnościowe przy niektórych typach plików (np. pliki .xlsm z makrami generują podgląd przez 5 minut i zamulają system)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Naprawa tylko .txt | Przywrócenie wyświetlania plików .txt | ✅ Wybrana – priorytet, naprawa błędu |
| Rozszerzenie o JSON, XML, Markdown, HTML, logi | Dodanie wsparcia dla dodatkowych formatów tekstowych | ✅ Wybrana – potrzeba biznesowa |
| Wyświetlanie Markdown jako tekst (z hashami) | Najprostsza metoda – wyświetlanie surowego tekstu | ✅ Wybrana dla MVP – najprostsze rozwiązanie |
| Renderowanie Markdown (z nagłówkami, obrazkami) | Interpretacja Markdown i wyświetlanie sformatowanej treści | ⏸️ Odroczona – osobny temat, wymaga dodatkowych komponentów |
| Wyświetlanie w DIV | Standardowe wyświetlanie tekstu w elemencie DIV | ❌ Odrzucona – ryzyko bezpieczeństwa dla HTML |
| Wyświetlanie w iframe sandbox | Wyświetlanie w iframe z parametrem sandbox (bez allow-script) | ✅ Wybrana – bezpieczne rozwiązanie dla plików tekstowych i HTML |
| Lista wykluczeń dla podglądu | Możliwość wyłączenia generowania podglądu dla niektórych typów plików (np. .xlsm) | ✅ Wybrana – rozwiązanie problemu wydajnościowego |

### Decyzja

**Status:** ✅ Zatwierdzone

**Naprawa błędu z plikami .txt:**
- Przywrócenie wyświetlania plików .txt w podglądzie (naprawa regresji)
- Ujednolicenie zachowania między podglądem na sprawie a podglądem w raporcie
- Przemek zajmie się podglądami w raportach w Reactcie i zweryfikuje problem

**Rozszerzenie o dodatkowe formaty:**
- Dodanie wsparcia dla plików tekstowych: JSON, XML, Markdown (.md), HTML, pliki logów
- Wszystkie formaty tekstowe powinny być wyświetlane w podglądzie
- Dla Markdown w pierwszej wersji (MVP) wyświetlanie jako surowy tekst (z hashami i znacznikami)
- W przyszłości można rozważyć renderowanie Markdown z formatowaniem

**Szczegóły techniczne:**
- Pliki tekstowe należy wyświetlać w `iframe` z parametrem `sandbox` (bez `allow-script` i innych `allow-*`)
- Parametr sandbox zapewnia bezpieczeństwo przy wyświetlaniu HTML (ogranicza możliwość wykonywania skryptów i ataków)
- Lista rozszerzeń plików, które mają być wyświetlane jako tekst: .txt, .json, .xml, .md, .html, .log
- Możliwość wyłączenia generowania podglądu dla niektórych typów plików (np. .xlsm z makrami) – funkcjonalność do dodania
- Pliki MSG i EML nie będą obsługiwane (wymagają Outlooka lub innego klienta pocztowego)

**Uwaga:** Rozważano również możliwość zastąpienia edytora Quill edytorem Markdown, ale to jest osobny temat wymagający dalszej analizy.

### Zadania

- **[Przemysław Sołdacki]:** Weryfikacja i naprawa podglądu plików .txt w raportach (React) → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Weryfikacja backendu podglądu plików tekstowych → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Implementacja wyświetlania plików tekstowych w iframe sandbox → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Dodanie listy rozszerzeń plików tekstowych do wyświetlania (.txt, .json, .xml, .md, .html, .log) → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Implementacja możliwości wyłączenia generowania podglądu dla niektórych typów plików → termin: [do ustalenia]

### Punkty otwarte

- Czy w przyszłości renderować Markdown z formatowaniem zamiast surowego tekstu?
- Czy rozważyć zastąpienie edytora Quill edytorem Markdown?
- Jakie dokładnie parametry sandbox powinny być ustawione dla iframe (oprócz braku allow-script)?

---

## 2. GetAttachmentContent – brak treści tekstowej

**Projekt:** `cross-cutting/Podglad-plikow`

### Kontekst i Problem

Funkcja `GetAttachmentContent` nie zwraca treści tekstowej plików tekstowych. Zamiast tego zwraca metadane (nazwa pliku, email twórcy pliku), co jest problematyczne przy próbie użycia tej funkcji do przetwarzania treści plików tekstowych (np. w kontekście AI).

### Zidentyfikowane Ryzyka

- Niemożność programowego dostępu do treści plików tekstowych przez funkcję `GetAttachmentContent`
- Brak spójności – funkcja powinna zwracać treść pliku, a nie tylko metadane
- Problemy przy próbie użycia treści plików w innych funkcjach systemowych

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dodanie treści tekstowej do GetAttachmentContent | Rozszerzenie funkcji o zwracanie treści plików tekstowych | ✅ Wybrana – poprawa funkcjonalności |
| Osobna funkcja do pobierania treści | Utworzenie nowej funkcji dedykowanej do treści tekstowej | ❌ Odrzucona – niepotrzebne mnożenie funkcji |

### Decyzja

**Status:** 🔍 Do weryfikacji

Funkcja `GetAttachmentContent` powinna zwracać treść tekstową plików tekstowych. Obecnie zwraca metadane (nazwa pliku, email twórcy), co jest nieprawidłowe. Wymaga weryfikacji i poprawy.

**Szczegóły techniczne:**
- Funkcja `GetAttachmentContent` jest używana do indeksowania, więc obecnie zwraca treść dla indeksowania, ale również dodaje metadane (kto stworzył plik, kto go zmodyfikował)
- Problem: na początku zwracane są dodatkowe informacje (nazwa pliku, email), które nie powinny być częścią treści
- Wymagana weryfikacja: sprawdzenie co dokładnie zwraca funkcja i poprawa, aby zwracała czystą treść tekstową

### Zadania

- **[Janusz Bossak]:** Przetestowanie funkcji `GetAttachmentContent` i zgłoszenie problemu → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Weryfikacja i poprawa funkcji `GetAttachmentContent` – zwracanie treści tekstowej zamiast metadanych → termin: [do ustalenia]

### Punkty otwarte

- Czy metadane powinny być dostępne w inny sposób, czy całkowicie usunięte z odpowiedzi funkcji?
- Jak obsłużyć przypadek, gdy plik nie jest tekstowy – czy zwracać pustą treść czy błąd?

---

## 3. Raport Gantt – etykiety na agregowanych kafelkach

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

W raportach typu Gantt występuje problem z wyświetlaniem etykiet na agregowanych kafelkach (zielonych). Etykieta jest kopiowana z pierwszego kafelka wewnętrznego, co może prowadzić do nieprawidłowego wyświetlania (np. liczba zamiast tekstu). Dodatkowo ilość dni na agregowanym kafelku jest błędna – pokazuje wartość z pierwszego kafelka zamiast sumy wszystkich dni z podległych elementów.

Problem dotyczy również zakresu dat (od-do) na agregowanym kafelku, który jest kopiowany z pierwszego elementu zamiast być wyliczany jako zakres od najwcześniejszej do najpóźniejszej daty z wszystkich podległych elementów.

### Zidentyfikowane Ryzyka

- Wyświetlanie błędnych informacji na agregowanych kafelkach (nieprawidłowa liczba dni, zakres dat)
- Nieczytelność raportów – etykiety mogą być nieprawidłowe lub mylące
- Brak możliwości sensownego agregowania etykiet tekstowych (nie da się ich zsumować)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Usunięcie etykiet z agregowanych kafelków | Brak etykiety, tylko tooltip z informacjami | ✅ Wybrana – najprostsze rozwiązanie, etykiety tekstowe nie da się sensownie agregować |
| Wyświetlanie zakresu dat (od-do) | Etykieta z zakresem dat zamiast liczby dni | ⏸️ Odroczona – może być rozważona w przyszłości, ale na razie za mało miejsca na małych kafelkach |
| Wyświetlanie nazwy projektu | Etykieta z nazwą projektu (która jest już w pierwszej kolumnie) | ❌ Odrzucona – powielanie informacji, która jest już widoczna |
| Wyświetlanie wszystkich etykiet po kolei | Wypisanie wszystkich etykiet z podległych elementów | ❌ Odrzucona – nie zmieści się na małych kafelkach |
| Poprawa wyliczania zakresu dat i liczby dni | Wyliczanie prawidłowych wartości z podległych elementów | ✅ Wybrana – poprawa tooltipu z prawidłowymi danymi |
| Wyświetlanie count w nawiasach | Dodanie informacji o liczbie elementów (np. "10") | ❌ Odrzucona – count został usunięty z etykiety |

### Decyzja

**Status:** ✅ Zatwierdzone

**Etykiety na agregowanych kafelkach:**
- Usunięcie etykiet z agregowanych kafelków (zielonych) – etykiety tekstowe nie da się sensownie agregować
- Informacje będą dostępne tylko w tooltipie po najechaniu myszką

**Poprawa tooltipu:**
- Tooltip na agregowanym kafelku musi wyświetlać prawidłowe dane:
  - Zakres dat (od-do) wyliczony z najwcześniejszej i najpóźniejszej daty z wszystkich podległych elementów
  - Ilość dni wyliczona jako suma dni z wszystkich podległych elementów (lub zakres dat, jeśli to bardziej odpowiednie)
- Tooltip nie może być kopiowany z pierwszego kafelka, tylko musi być wyliczany z wszystkich podległych elementów

**Szczegóły techniczne:**
- Agregowane kafelki (zielone) są generowane automatycznie przez DevExpress Gantt i nie są bytami w bazie danych
- Dane pochodzą z tej samej sprawy (projekt i zadanie są polami na sprawie)
- Agregacja jest faktycznie grupowaniem po polu (np. projekt, zadanie), a nie prawdziwą agregacją w bazie danych
- Gantt ma 2 tryby budowania hierarchii – trzeba mieć świadomość obu trybów przy poprawkach
- W drugim trybie istnieje możliwość przeliczania zakresu dat (prawy klawisz myszy)

**Uwaga:** Problem może być częściowo związany z nieprawidłową konfiguracją raportu (2 wiersze zagnieżdżenia zamiast rekurencyjnego budowania hierarchii zadań).

### Zadania

- **[Marek Dziakowski]:** Usunięcie etykiet z agregowanych kafelków w raporcie Gantt → termin: [do ustalenia]
- **[Marek Dziakowski]:** Poprawa tooltipu na agregowanych kafelkach – wyliczanie zakresu dat (od-do) z wszystkich podległych elementów → termin: [do ustalenia]
- **[Marek Dziakowski]:** Poprawa tooltipu – wyliczanie prawidłowej ilości dni z podległych elementów → termin: [do ustalenia]

### Punkty otwarte

- Czy w przyszłości rozważyć wyświetlanie zakresu dat (od-do) jako etykiety na agregowanych kafelkach?
- Czy problem z etykietami jest związany z konfiguracją raportu (2 wiersze zagnieżdżenia vs rekurencyjne budowanie hierarchii)?
- Jak obsłużyć przypadek, gdy agregowany kafelek jest bardzo mały i nie ma miejsca na jakiekolwiek informacje?

---

## 4. Tłumaczenia w raportach – etykiety kolumn i agregacji

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

W raportach występuje problem z tłumaczeniami etykiet kolumn i agregacji. Kolumny pochodzące ze źródeł zewnętrznych (np. "Report created by", "Report tip", "Report category") mają etykiety po angielsku, mimo że interfejs jest po polsku. Dodatkowo agregacje typu "count", "sum", "min", "max" są wyświetlane po angielsku zamiast po polsku.

Pojawiła się również potrzeba możliwości nadawania własnych etykiet dla agregacji w kontekście konkretnego raportu (np. zamiast "sum Report id" wyświetlić "Ilość rekordów" lub "Ilość raportów").

### Zidentyfikowane Ryzyka

- Nieczytelność raportów dla użytkowników polskojęzycznych (mieszanka języków)
- Brak możliwości dostosowania etykiet do kontekstu biznesowego raportu
- Niespójność między różnymi miejscami w systemie (procesy mają tłumaczenia, raporty nie)
- Problemy z wielojęzycznością – każdy raport wymagałby osobnego tłumaczenia wszystkich etykiet

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Tłumaczenia per raport | Definiowanie tłumaczeń dla każdego raportu osobno | ❌ Odrzucona – niepraktyczne, każdy raport wymagałby osobnego tłumaczenia wszystkich etykiet |
| Tłumaczenia na poziomie źródła danych | Definiowanie tłumaczeń dla kolumn na poziomie źródła danych (jak w procesach) | ✅ Wybrana – rozwiązanie systemowe, raz zdefiniowane działa dla wszystkich raportów |
| Tłumaczenia agregacji per raport | Możliwość nadania własnej etykiety dla agregacji w kontekście konkretnego raportu | ✅ Wybrana – potrzeba biznesowa (np. "Ilość rekordów" zamiast "sum Report id") |
| Tłumaczenia agregacji systemowo | Tłumaczenie agregacji (count, sum, min, max) na poziomie systemowym | ✅ Wybrana – podstawowe tłumaczenia powinny być dostępne systemowo |
| Wyświetlanie tłumaczeń, które już są zdefiniowane | Naprawa wyświetlania istniejących tłumaczeń w trybie odczytu | ✅ Wybrana – najprostsze MVP, tłumaczenia są już zdefiniowane, tylko nie są wyświetlane |

### Decyzja

**Status:** 🔍 Do weryfikacji / ⏸️ Częściowo odroczone

**MVP (Minimum Viable Product):**

1. **Wyświetlanie istniejących tłumaczeń:**
   - Naprawa wyświetlania tłumaczeń agregacji (count → suma, sum → suma, min → min, max → max) w trybie odczytu
   - Tłumaczenia są już zdefiniowane, tylko nie są wyświetlane prawidłowo

2. **Tłumaczenia kolumn na poziomie źródła danych:**
   - Dodanie mechanizmu tłumaczeń dla kolumn na poziomie źródła danych (podobnie jak w procesach)
   - Tłumaczenia będą dostępne we wszystkich językach, w których system jest dostępny
   - Raz zdefiniowane tłumaczenie będzie działać dla wszystkich raportów używających tego źródła danych
   - Mechanizm będzie analogiczny do tłumaczeń w procesach (dodanie do źródeł tłumaczeń)

3. **Tłumaczenia agregacji systemowo:**
   - Tłumaczenie podstawowych agregacji (count, sum, min, max, average) na poziomie systemowym
   - Agregacje będą automatycznie przetłumaczone w zależności od języka interfejsu

**Rozwój (kolejne kroki):**

4. **Własne etykiety dla agregacji per raport:**
   - Możliwość nadania własnej etykiety dla agregacji w kontekście konkretnego raportu
   - Przykład: zamiast "sum Report id" wyświetlić "Ilość rekordów" lub "Ilość raportów"
   - Etykiety będą definiowane per raport (np. w konfiguracji osi X/Y wykresu)
   - Dotyczy zarówno raportów systemowych, jak i biznesowych

**Szczegóły techniczne:**
- W procesach już istnieje mechanizm tłumaczeń – należy go rozszerzyć na źródła danych
- Tłumaczenia kolumn będą definiowane na poziomie źródła danych (podobnie jak tłumaczenia pól w procesach)
- Tłumaczenia agregacji będą systemowe (automatyczne w zależności od języka interfejsu)
- Własne etykiety dla agregacji będą definiowane w konfiguracji raportu (np. w ustawieniach osi wykresu)
- Problem dotyczy różnych typów raportów: wykresy słupkowe, kolumnowe, pivot, Gantt

**Uwaga:** Rozważano również możliwość definiowania tłumaczeń per raport, ale uznano to za niepraktyczne – każdy raport wymagałby osobnego tłumaczenia wszystkich etykiet, co prowadziłoby do duplikacji pracy.

### Zadania

- **[Łukasz Bott]:** Przygotowanie PA (Product Analysis) dla tłumaczeń w raportach → termin: [do ustalenia]
- **[Marek Dziakowski / Anna Skupińska]:** Naprawa wyświetlania istniejących tłumaczeń agregacji w trybie odczytu → termin: [do ustalenia]
- **[Marek Dziakowski / Anna Skupińska]:** Implementacja tłumaczeń agregacji na poziomie systemowym (count, sum, min, max, average) → termin: [do ustalenia]
- **[Backend]:** Dodanie mechanizmu tłumaczeń dla kolumn na poziomie źródła danych (analogicznie do procesów) → termin: [do ustalenia]
- **[Frontend]:** Wyświetlanie przetłumaczonych kolumn w raportach → termin: [do ustalenia]
- **[Marek Dziakowski / Anna Skupińska]:** Implementacja możliwości nadawania własnych etykiet dla agregacji per raport → termin: [do ustalenia]

### Punkty otwarte

- Czy wszystkie agregacje powinny być tłumaczone systemowo, czy tylko podstawowe (count, sum, min, max, average)?
- Jak obsłużyć przypadek, gdy użytkownik chce mieć różne etykiety dla tej samej agregacji w różnych miejscach raportu?
- Czy własne etykiety dla agregacji powinny być dostępne tylko dla raportów biznesowych, czy również dla systemowych?
- Jak rozwiązać problem z wielojęzycznością – czy własne etykiety powinny być definiowane per język?

---

## 5. Szablony maili systemowych – ochrona przed nadpisaniem

**Projekt:** `cross-cutting/Szablony-maili-systemowych`

### Kontekst i Problem

Szablony maili systemowych są nadpisywane przy aktualizacji bazy danych, co powoduje problemy u klientów (szczególnie dużych, np. Orlen, LPP), którzy dostosowali szablony do swoich potrzeb. Klienci tracą swoje zmiany przy każdej aktualizacji systemu.

Dodatkowo szablony maili mają przestarzały wygląd (jak z poprzedniej epoki) i wymagają odświeżenia, ale to jest duże wyzwanie wymagające szerokiego podejścia (podobnie jak odświeżenie wyglądu sprawy).

### Zidentyfikowane Ryzyka

- Utrata zmian wprowadzonych przez klientów przy każdej aktualizacji systemu
- Problemy z klientami, którzy dostosowali szablony do swoich potrzeb
- Przestarzały wygląd szablonów maili (szarość, brak spójności z nowym interfejsem)
- Ryzyko kwalifikowania maili jako spam przy zmianach treści (wymagane testy na stronach sprawdzających współczynnik spamu)
- Duża liczba szablonów do przetworzenia (szacunkowo 20+ PBI dla różnych szablonów)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Pomijanie wskazanych maili przy aktualizacji | Dodanie kolumny flagującej, które szablony mają być pomijane przy aktualizacji | ✅ Wybrana dla rozwiązania krótkoterminowego – szybkie rozwiązanie (ok. 1 godzina pracy) |
| Customowy szablon + znacznik | Dodanie kolumny z customowym szablonem i kolumny decydującej, który szablon używać | ⏸️ Odroczona – wymaga więcej pracy (5-20 godzin + testy), może być rozważona w przyszłości |
| Pełny interfejs do zarządzania szablonami | Utworzenie interfejsu w ustawieniach systemowych do zarządzania szablonami | ⏸️ Odroczona – duży projekt (2 sprinty, 2 osoby), przesunięty na przyszły kwartał |
| Globalna zmiana wszystkich szablonów | Odświeżenie wszystkich szablonów maili (nowy wygląd, spójność z interfejsem) | ⏸️ Odroczona – duży projekt, wymaga mapy projektu, przesunięty na przyszły kwartał |

### Decyzja

**Status:** ✅ Zatwierdzone (rozwiązanie krótkoterminowe) / ⏸️ Odroczone (rozwiązania długoterminowe)

**Rozwiązanie krótkoterminowe (MVP):**
- Dodanie kolumny flagującej, które szablony mają być pomijane przy aktualizacji bazy danych
- Jeśli szablon jest oznaczony jako "pomijany", nie jest aktualizowany przy podnoszeniu wersji
- Rozwiązanie ad-hoc, które rozwiąże obecny problem (szacunkowo 1 godzina pracy)
- Klienci mogą zmieniać szablony na własną odpowiedzialność, uwzględniając ryzyko kwalifikowania jako spam

**Rozwiązania długoterminowe (odroczone):**

1. **Customowy szablon + znacznik:**
   - Dodanie kolumny z customowym szablonem i kolumny decydującej, który szablon używać (domyślny vs customowy)
   - Jeśli kolumna customowego szablonu jest wypełniona, używa się customowego, jeśli pusta – domyślnego
   - W przyszłości może być rozbudowane o interfejs z przełącznikiem

2. **Pełny interfejs do zarządzania szablonami:**
   - Utworzenie interfejsu w ustawieniach systemowych do zarządzania szablonami maili
   - Możliwość tworzenia, edycji i zarządzania customowymi szablonami
   - Ochrona przed nadpisaniem przy aktualizacji
   - Szacunkowo 2 sprinty, 2 osoby

3. **Globalna zmiana wszystkich szablonów:**
   - Odświeżenie wyglądu wszystkich szablonów maili (nowy design, spójność z interfejsem)
   - Proste ramki, białe tło (podobnie jak w głównym ekranie)
   - Wymaga mapy projektu i finansowania
   - Szacunkowo 20+ PBI dla różnych szablonów

**Szczegóły techniczne:**
- Rozwiązanie krótkoterminowe: jedna kolumna flagująca (np. `SkipUpdate` lub `IsCustom`), która decyduje, czy szablon ma być pomijany przy aktualizacji
- Rozwiązanie długoterminowe: dwie kolumny – jedna z customowym szablonem, druga decydująca, który używać
- Szablony maili są przechowywane w bazie danych
- Przy aktualizacji bazy danych domyślne szablony są aktualizowane, chyba że są oznaczone jako pomijane
- Wszyscy duzi klienci mają problem z nadpisywaniem szablonów (Orlen, LPP, inni)

**Uwaga:** Temat był już wielokrotnie omawiany w przeszłości, ale nie został zrealizowany. Obecne rozwiązanie krótkoterminowe ma na celu szybkie rozwiązanie problemu, a długoterminowe rozwiązania wymagają mapy projektu i finansowania.

### Zadania

- **[Piotr Buczkowski]:** Implementacja pomijania wskazanych szablonów maili przy aktualizacji bazy danych (kolumna flagująca) → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Przebadanie mechanizmu pomijania szablonów → termin: [do ustalenia]
- **[Product Owner / Janusz Bossak]:** Przygotowanie mapy projektu dla długoterminowych rozwiązań (customowy szablon, interfejs, globalna zmiana) → termin: [do ustalenia]

### Punkty otwarte

- Czy rozwiązanie krótkoterminowe (pomijanie przy aktualizacji) będzie wystarczające do czasu wdrożenia długoterminowych rozwiązań?
- Jak obsłużyć przypadek, gdy klient chce mieć różne szablony dla różnych języków?
- Czy customowe szablony powinny być dostępne tylko dla dużych klientów, czy dla wszystkich?
- Jak zapewnić, że customowe szablony nie będą kwalifikowane jako spam?
- Czy w przyszłości rozważyć przeniesienie szablonów poza bazę danych (np. do plików konfiguracyjnych)?

---

## 6. Backlog – pytania i pomysły rozwojowe

**Projekt:** Nowy temat / do sklasyfikowania

### Kontekst i Problem

Pojawiło się pytanie, gdzie powinny być przestrzeń do wrzucania pytań i pomysłów rozwojowych od konsultantów i wdrożeniowców (szczególnie od starszych wdrożeniowców i Mateusza). Obecnie takie pytania trafiają do backlogu, co zaśmieca go i miesza zadania do realizacji z pytaniami do rozważenia.

### Zidentyfikowane Ryzyka

- Zaśmiecanie backlogu pytaniami i pomysłami, które nie są jeszcze zadaniami do realizacji
- Brak jasnej ścieżki dla pytań i pomysłów rozwojowych
- Mieszanie zadań (które mają finansowanie) z pytaniami (które wymagają najpierw decyzji, czy w ogóle warto się nad tym pochylać)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Tablica analityczna (jak kiedyś) | Wznowienie dedykowanej tablicy dla pytań i pomysłów | 💡 Propozycja do rozważenia – wymaga wznowienia procesu |
| Backlog z kategoriami | Używanie backlogu z kategoriami "pomysł rozwojowy" i "pytanie" | ✅ Częściowo wdrożone – istnieje kategoria "pomysł rozwojowy" |
| Zgłaszanie przez wyceny | Zgłaszanie pytań przez proces wycen z oznaczeniem "pytanie" | ✅ Wybrana – istniejący proces, można oznaczyć jako pytanie |
| Zgłaszanie bezpośrednio do Product Ownerów | Konsultanci zgłaszają pytania bezpośrednio do Product Ownerów (Damian, Kamil, Łukasz, Janusz, Piotr) | ✅ Wybrana – ścieżka dla pytań, które nie są jeszcze wycenami |
| Backlog tylko dla bugów i hotfixów | Ograniczenie dostępu konsultantów do backlogu tylko do bugów i hotfixów | 💡 Propozycja Janusza – wymaga weryfikacji |

### Decyzja

**Status:** 🔍 Do weryfikacji

**Ścieżka dla pytań i pomysłów:**

1. **Pytania (czy coś da się zrobić, jak to działa):**
   - Zgłaszanie przez proces wycen z oznaczeniem "pytanie" (nie wycena)
   - Alternatywnie: zgłaszanie bezpośrednio do Product Ownerów (Damian, Kamil, Łukasz, Janusz, Piotr Buczkowski)
   - Product Ownerzy przetwarzają pytania, analizują na radzie architektów
   - Na podstawie analizy powstaje projekt zapisany na wiki (jeśli pomysł jest wartościowy)
   - Dopiero na podstawie projektu powstają wpisy na backlogu (zadania do zrobienia)

2. **Pomysły rozwojowe (chcą, żeby było zrealizowane, ale nie ma chętnych do zapłacenia):**
   - Zgłaszanie przez proces wycen z kategorią "pomysł rozwojowy"
   - Proces wycen ma już taką kategorię

3. **Backlog:**
   - Backlog powinien zawierać zadania do realizacji, nie pytania i pomysły
   - Jeśli pytania/pomysły trafiają do backlogu, powinny być szybko przetworzone i przeniesione do odpowiedniej ścieżki
   - Możliwość ustawienia statusu "pytanie" lub "pomysł" dla szybkiej identyfikacji

**Szczegóły:**
- Proces wycen ma opcję oznaczenia jako "pomysł rozwojowy" lub "pytanie"
- Konsultanci mogą zgłaszać pytania bezpośrednio do Product Ownerów (zamiast przez backlog)
- Product Ownerzy przetwarzają pytania na radzie architektów
- Jeśli pomysł jest wartościowy, powstaje projekt na wiki, a następnie zadania na backlogu

**Uwaga:** Rozważano również wznowienie tablicy analitycznej (jak kiedyś), ale uznano, że lepiej użyć istniejących procesów (wyceny) z odpowiednimi oznaczeniami.

### Zadania

- **[Damian Kamiński]:** Weryfikacja procesu wycen – czy można oznaczać jako "pytanie" → termin: [do ustalenia]
- **[Damian Kamiński]:** Komunikacja do konsultantów dotycząca ścieżki zgłaszania pytań i pomysłów → termin: [do ustalenia]
- **[Product Ownerzy]:** Przetwarzanie pytań i pomysłów z backlogu (przeniesienie do odpowiedniej ścieżki) → termin: [do ustalenia]

### Punkty otwarte

- Czy wznowić dedykowaną tablicę analityczną dla pytań i pomysłów?
- Czy ograniczyć dostęp konsultantów do backlogu tylko do bugów i hotfixów?
- Jak często przeglądać pytania i pomysły rozwojowe (dedykowane spotkanie czy w ramach istniejących spotkań)?

