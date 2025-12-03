# Rada Architektów – 2025-08-12

> 🛡️ Notatka zweryfikowana i zmapowana (Codex Review) w dniu 2025-12-03

**Powiązane projekty:**
- [[Integracje/Integracje-REST-multipart/README|Integracje-REST-multipart]] – temat 1
- [[Moduly/Ustawienia-systemowe/README|Ustawienia-systemowe]] – temat 2
- [[cross-cutting/Testy-kompatybilnosci-API/README|Testy-kompatybilnosci-API]] – temat 3
- [[cross-cutting/Zastepstwa-grupy/README|Zastepstwa-grupy]] – temat 4
- [[Moduly/Edytor-procesow/Edytor-formularzy/README|Edytor-formularzy]] – temat 5
- [[Moduly/Modul-raportowy/README|Modul-raportowy]] – temat 6

---

## 1. Usprawnienie mechanizmu przesyłania załączników przez API

**Projekt:** `Integracje/Integracje-REST-multipart`

### Kontekst i Problem

Obecna metoda przesyłania plików przez funkcję `callRest` oparta na indywidualnych parach klucz-wartość w nagłówkach (np. `CustomHeaderKey1`, `CustomHeaderValue1`) jest nieelastyczna, nieintuicyjna i generuje nadmiarową liczbę parametrów. Potrzebna jest możliwość przesyłania wielu plików w jednym żądaniu, szczególnie dla formatów `multipart/form-data` i `x-www-form-urlencoded`.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Indywidualne pary klucz-wartość | Obecne podejście z `CustomHeaderKey1`, `CustomHeaderValue1` | ❌ Odrzucona – nieelastyczne, generuje nadmiar parametrów, trudne w zarządzaniu |
| Zmienna dla listy załączników | Wprowadzenie zmiennej, która odnosi się do listy załączników na sprawie | ✅ Wybrana – elastyczne, upraszcza konfigurację |
| Tablica `documents` | Tablica obiektów z `DocumentName` i `DocumentValue` (Base64) | ✅ Wybrana – ustrukturyzowane podejście dla wielu dokumentów |
| Obsługa multipart/form-data | Natywne wsparcie dla formatu `multipart/form-data` | ✅ Wybrana – standardowy format, wymagany przez klientów |
| Obsługa x-www-form-urlencoded | Obsługa formatu `x-www-form-urlencoded` | ✅ Wybrana – również wymagany format |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono wprowadzenie usprawnień mechanizmu przesyłania załączników przez API:

1. **Zmienna dla listy załączników** – możliwość odwołania się do listy załączników na sprawie zamiast definiowania indywidualnych parametrów
2. **Tablica `documents`** – ustrukturyzowana obsługa wielu dokumentów jako pojedynczego parametru, gdzie każdy obiekt zawiera `DocumentName` i `DocumentValue` (Base64)
3. **Obsługa formatów** – natywne wsparcie dla `multipart/form-data` i `x-www-form-urlencoded`
4. **Mechanizm podobny do headers** – wykorzystanie podejścia podobnego do dynamicznego definiowania nagłówków, gdzie pary klucz-wartość są przekazywane przez nową linię (przełamanie linii = kolejna para)

**Szczegóły techniczne:**
- Funkcja: `callRest`
- Format: `multipart/form-data`, `x-www-form-urlencoded`
- Parametry: `DocumentName`, `DocumentValue` (Base64)
- Mechanizm: pary klucz-wartość przekazywane przez nową linię (podobnie jak w headers)
- Tablica `documents` – możliwość przekazania wielu dokumentów w jednym parametrze

### Zadania

- **Adrian Kotowski:** Implementacja usprawnień mechanizmu przesyłania załączników zgodnie z ustaleniami
- **Piotr Buczkowski:** Weryfikacja i przegląd implementacji

### Punkty otwarte

- Brak

---

## 2. Problem kompatybilności wstecznej interfejsu IJob

**Projekt:** `Moduly/Ustawienia-systemowe`

### Kontekst i Problem

Rozszerzenie istniejącego interfejsu `IJob` o nowe pole `Owner` spowodowało błędy wykonania we wszystkich istniejących implementacjach jobów, które nie zostały zaktualizowane. Problem dotyczy zarówno jobów budowanych w projekcie w solucji AMODIT, jak i jobów budowanych poza solucją (np. wszystkie joby integracji). Problem wystąpił na środowisku Stage w Rossmannie, na szczęście nie na produkcji.

### Zidentyfikowane Ryzyka

- Ryzyko łamania kompatybilności wstecznej przy modyfikacji publicznych interfejsów
- Ryzyko awarii istniejących implementacji jobów przy zmianach w interfejsie
- Ryzyko problemów na produkcji przy braku odpowiednich testów kompatybilności

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Modyfikacja istniejącego interfejsu IJob | Dodanie pola `Owner` do istniejącego interfejsu | ❌ Odrzucona – powoduje problemy z kompatybilnością wsteczną |
| Nowy interfejs dla jobów wymagających Owner | Stworzenie nowego interfejsu implementowanego tylko przez joby wymagające nowej funkcjonalności | ✅ Wybrana – bezpieczne rozwiązanie, nie łamie kompatybilności |
| Domyślna implementacja w klasie bazowej | Dodanie domyślnej wartości pola w klasie bazowej z wymaganiem nadpisania | ⏸️ Odroczona – mniej bezpieczne niż nowy interfejs |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono utrzymanie rozwiązania polegającego na wykorzystaniu nowego, osobnego interfejsu dla jobów wymagających pola `Owner`. Istniejące joby nie będą musiały implementować nowego interfejsu, co zapewnia kompatybilność wsteczną.

**Szczegóły techniczne:**
- Interfejs: `IJob` (istniejący) – pozostaje bez zmian
- Nowy interfejs: dla jobów wymagających pola `Owner`
- Istniejące joby: nie wymagają modyfikacji
- Nowe joby wymagające `Owner`: implementują nowy interfejs

### Zadania

- **Marek:** [Do ustalenia po powrocie z urlopu] – weryfikacja rozwiązania i ewentualne dopracowanie

### Punkty otwarte

- Czy można to zrobić lepiej? – wymaga dalszej analizy po powrocie Marka z urlopu

---

## 3. Test jednostkowy do wykrywania zmian w publicznych metodach

**Projekt:** `cross-cutting/Testy-kompatybilnosci-API`

### Kontekst i Problem

Częste problemy z kompatybilnością wsteczną wynikają z braku automatycznej kontroli nad zmianami w publicznych interfejsach i metodach kluczowych bibliotek (np. `AMODIT.Classes`). Potrzebny jest mechanizm wykrywania przypadkowych zmian w publicznym API, które mogą łamać kompatybilność wsteczną.

### Zidentyfikowane Ryzyka

- Ryzyko przypadkowego łamania kompatybilności wstecznej przy modyfikacji publicznych metod
- Ryzyko braku wykrycia zmian w publicznym API przed wdrożeniem

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Test snapshotowy | Test jednostkowy zapisujący snapshot wszystkich publicznych metod do pliku i porównujący z aktualnym stanem | ✅ Wybrana – proste rozwiązanie, łatwe do zrealizowania |
| Brak automatycznej kontroli | Ręczna weryfikacja zmian w publicznym API | ❌ Odrzucona – nieefektywne, łatwo o przeoczenie |

### Decyzja

**Status:** 💡 Propozycja

Zaproponowano wprowadzenie testu jednostkowego, który:
1. Zapisuje snapshot wszystkich publicznych metod z całej biblioteki `AMODIT.Classes` (lub innych kluczowych bibliotek) do pliku
2. Przy każdym uruchomieniu porównuje aktualny stan z zapisanym snapshotem
3. Wykrywa zmiany w publicznych metodach (modyfikacje, usunięcia)
4. Wymaga okresowej aktualizacji snapshota przy świadomych zmianach

**Szczegóły techniczne:**
- Biblioteka: `AMODIT.Classes` (lub inne kluczowe biblioteki)
- Mechanizm: snapshot wszystkich publicznych metod zapisany w pliku przypiętym do projektu
- Test jednostkowy: porównuje aktualny stan z snapshotem przy każdym uruchomieniu
- Aktualizacja snapshota: ręczna, gdy zmiany są świadome i zamierzone

### Zadania

- **Adrian Kotowski:** Przygotowanie testu jednostkowego do wykrywania zmian w publicznych metodach (jeśli znajdzie czas)

### Punkty otwarte

- Które biblioteki powinny być objęte testem snapshotowym?
- Jak często aktualizować snapshot?
- Czy rozszerzyć test również na interfejsy (nie tylko metody)?

---

## 4. Zastępstwo za grupę – różnice między starym a nowym mechanizmem

**Projekt:** `cross-cutting/Zastepstwa-grupy`

### Kontekst i Problem

Wykryto niespójność między starym a nowym mechanizmem zastępstw dotyczącą obsługi zastępstw za grupy. W starym mechanizmie, jeśli użytkownik jest zastępcą osoby należącej do grupy, widzi również sprawy przypisane do tej grupy. W nowym mechanizmie tego nie ma – zastępca widzi tylko sprawy przypisane bezpośrednio do osoby, którą zastępuje, ale nie sprawy przypisane do grup, do których ta osoba należy.

### Zidentyfikowane Ryzyka

- Ryzyko niespójności funkcjonalnej między starym a nowym mechanizmem
- Ryzyko problemów dla użytkowników korzystających ze starego mechanizmu przy przejściu na nowy
- Ryzyko problemów wydajnościowych przy obsłudze zastępstw za grupy w nowym mechanizmie

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Obsługa zastępstw za grupy w nowym mechanizmie | Dodanie obsługi zastępstw za grupy do nowego mechanizmu (jak w starym) | ⏸️ Odroczona – wymaga kilku godzin pracy, wymaga przemyślenia |
| Obsługa tylko dla grup jednoosobowych | Obsługa zastępstw za grupy tylko dla grup jednoosobowych (gdzie grupa = rola) | ✅ Wybrana – najbardziej sensowny przypadek użycia |
| Parametr "uwzględnij zastępstwa dla grupy" | Dodanie parametru do grupy określającego, czy uwzględniać zastępstwa | ✅ Wybrana – elastyczne rozwiązanie dla grup wieloosobowych |
| Brak obsługi zastępstw za grupy | Usunięcie obsługi zastępstw za grupy z obu mechanizmów | ❌ Odrzucona – grupy jednoosobowe (role) wymagają zastępstw |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono następujące podejście do obsługi zastępstw za grupy:

1. **Domyślnie dla grup jednoosobowych** – zastępstwa za grupy jednoosobowe (gdzie grupa = rola, np. Dyrektor Finansowy, RODO) są domyślnie uwzględniane w obu mechanizmach
2. **Parametr dla grup wieloosobowych** – możliwość dodania parametru do grupy określającego, czy uwzględniać zastępstwa (np. "Uwzględnij zastępstwa dla tej grupy")
3. **Ujednolicenie mechanizmów** – docelowo oba mechanizmy powinny działać tak samo (wymaga kilku godzin pracy)

**Szczegóły techniczne:**
- Stary mechanizm: obsługuje zastępstwa za grupy
- Nowy mechanizm: obecnie nie obsługuje zastępstw za grupy
- Grupy jednoosobowe: domyślnie uwzględniają zastępstwa (gdzie grupa = rola)
- Grupy wieloosobowe: opcjonalnie przez parametr (np. HR z 20 osobami – nie potrzebuje zastępstw, bo zawsze ktoś z grupy się zajmie)
- Mechanizm: w nowym mechanizmie są 2 zapytania (`CASE...` dla spraw przypisanych do użytkownika lub jego grup `UNION` z działaniami kategorii, gdzie dozwolone zastępstwo)

### Zadania

- **Piotr Buczkowski:** Dodanie obsługi zastępstw za grupy jednoosobowe domyślnie w nowym mechanizmie
- **Piotr Buczkowski:** Dodanie parametru "Uwzględnij zastępstwa dla tej grupy" dla grup wieloosobowych (wymaga interfejsu i kolumny w bazie lub logiki SQL)

### Punkty otwarte

- Czy dodać nową kolumnę do tabeli grup, czy można to obsłużyć bezpośrednio w SQL (np. przez sprawdzenie liczby członków grupy)?
- Jak będzie wyglądał interfejs do ustawiania parametru "Uwzględnij zastępstwa dla tej grupy"?
- Czy docelowo przejść całkowicie na nowy mechanizm zastępstw?

---

## 5. Ustawianie szerokości kolumn w formularzu

**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`

### Kontekst i Problem

Często powtarzające się zapytanie klientów (m.in. Zbigniew Szymanowski, PKF) o możliwość ustawiania szerokości kolumn w tabelach w formularzu. Obecnie kolumny mają domyślną szerokość, co jest problematyczne szczególnie dla kolumn z krótkimi wartościami (np. jednostki miary typu KG, SZT, ilości ograniczone do 999), które zajmują niepotrzebnie dużo miejsca.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Brak możliwości ustawiania szerokości | Obecne podejście – kolumny mają domyślną szerokość | ❌ Odrzucona – częste zapytania klientów, potrzeba elastyczności |
| Ustawianie szerokości w pikselach | Możliwość wpisania szerokości kolumny w pikselach (np. 50px) | ✅ Wybrana – proste i intuicyjne |
| Pełna kontrola CSS | Możliwość wpisania dowolnego stylu CSS | ❌ Odrzucona – ryzyko bezpieczeństwa (możliwość wstrzyknięcia JavaScript) |
| Ograniczona kontrola CSS | Tylko wybrane właściwości CSS (width, zawijanie tekstu) | ✅ Wybrana – bezpieczne, wystarczające na początek |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono wprowadzenie możliwości ustawiania szerokości kolumn w formularzu:

1. **Szerokość kolumny** – możliwość wpisania szerokości w pikselach (np. 50px) w definicji kolumny tabeli
2. **Zawijanie tekstu** – opcja określająca, czy tekst ma się zawijać w kolumnie
3. **Ograniczona kontrola CSS** – tylko wybrane właściwości CSS (width, zawijanie), nie pełna kontrola CSS ze względów bezpieczeństwa
4. **Bezpieczeństwo** – backend odczytuje tylko oczekiwane właściwości (width z odpowiednią liczbą), ignoruje wszystko inne (np. próby wstrzyknięcia JavaScript)

**Szczegóły techniczne:**
- Definicja kolumny: możliwość wpisania szerokości w pikselach
- Właściwości CSS: tylko `width` i zawijanie tekstu (na początek)
- Bezpieczeństwo: backend interpretuje tylko oczekiwane właściwości, ignoruje resztę
- Oddzielne ustawienia: dla wyświetlania i dla wydruku (jak w starym systemie)
- Tabelka w tabelce: nie określa się szerokości (jest w nowej linii)

### Zadania

- **Piotr Buczkowski:** Implementacja możliwości ustawiania szerokości kolumn w formularzu zgodnie z ustaleniami
- **Anna Skupińska:** Testy bezpieczeństwa – weryfikacja, że nie można wstrzyknąć złośliwego kodu przez CSS

### Punkty otwarte

- Czy w przyszłości rozszerzyć o więcej właściwości CSS?
- Jak będzie wyglądał interfejs do ustawiania szerokości kolumn?

---

## 6. Kolory w raportach tabelarycznych z agregacją

**Projekt:** `Moduly/Modul-raportowy`

### Kontekst i Problem

Obecny mechanizm kolorowania wartości w raportach tabelarycznych z agregacją działa nieprawidłowo – patrzy tylko na wartości z danej strony, zamiast pobierać wszystkie wartości dla prawidłowego obliczenia gradientu kolorów. Potrzebne jest poprawienie mechanizmu, aby kolorowanie było oparte na wszystkich wartościach w raporcie, nie tylko na wartości z aktualnej strony.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Kolorowanie tylko wartości z danej strony | Obecne podejście – kolorowanie oparte tylko na wartościach z aktualnej strony | ❌ Odrzucona – nieprawidłowe działanie gradientu |
| Kolorowanie oparte na wszystkich wartościach | Pobieranie wszystkich wartości z raportu i kolorowanie na podstawie min/max | ✅ Wybrana – prawidłowe działanie gradientu |
| Kolorowanie tylko dla raportów bez agregacji | Ograniczenie kolorowania do raportów tabelarycznych bez agregacji | ⏸️ Odroczona – na razie tylko dla raportów bez agregacji |
| Więcej opcji kolorowania | Dzielenie zakresów na więcej elementów z różnymi kolorami (nie tylko gradient) | ⏸️ Odroczona – przyszłościowo |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono poprawienie mechanizmu kolorowania wartości w raportach tabelarycznych:

1. **Pobieranie wszystkich wartości** – mechanizm pobiera wszystkie wartości z raportu (nie tylko z aktualnej strony) przed kolorowaniem
2. **Gradient oparty na min/max** – kolorowanie oparte na maksymalnej i minimalnej wartości oraz wartości zerowej
3. **Zakres na razie** – tylko dla raportów tabelarycznych bez agregacji (głównie pod wymaganie WIM i pana Piotra)
4. **Obsługa typów raportów** – obecnie tylko dla typu Pivot i mapy, dla innych typów z agregacją kolorowanie nie ma sensu

**Szczegóły techniczne:**
- Typy raportów: Pivot, mapa (na razie)
- Mechanizm: pobieranie wszystkich wartości przed kolorowaniem
- Gradient: oparty na min/max/zero
- Przyszłościowo: możliwość dzielenia zakresów na więcej elementów z różnymi kolorami (nie tylko gradient)

### Zadania

- **Anna Skupińska:** Finalizacja zmian kolorów i gradientów (oddane do testowania na AMODIT Local)
- **Janusz Bossak:** Testowanie zmian i zwracanie uwag

### Punkty otwarte

- Jak będzie wyglądać mechanizm dzielenia zakresów na więcej elementów z różnymi kolorami w przyszłości?
- Czy rozszerzyć obsługę kolorowania na inne typy raportów?

