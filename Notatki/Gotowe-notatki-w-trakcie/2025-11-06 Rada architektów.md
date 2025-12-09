# Rada Architektów – 2025-11-06

**Powiązane projekty:**
- `moduly/Edytor-procesow-formularzy` – temat 1
- `moduly/Trust-Center` – temat 2
- `moduly/Modul-raportowy` – temat 3

---

## 1. Rozszerzenie funkcjonalności pola "Odnośnik do procesu" o obsługę pól słownikowych i listy wyboru

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

Pole typu "Odnośnik do procesu" można skonfigurować, aby wyświetlić dodatkowe kolumny do wyszukiwania, ale na chwilę obecną wybór tych kolumn dotyczy tylko i wyłącznie pól typu tekstowego. Zapotrzebowanie pochodzi od klienta PKF, gdzie grupa użytkowników mocno upiera się, żeby dodać obsługę innych typów pól, w szczególności słownikowych. Konsultant Kamil chciał zastosować obejście, tworząc tekstowy odpowiednik pól słownikowych, ale to głupie rozwiązanie. Ewentualnie w skrajnym przypadku zrobić jedno pole tekstowe, gdzie mielibyśmy wszystkie wartości, po których można wyszukiwać. Ten temat wraca po raz enty – już przy projekcie dla Rossmanna ograniczyliśmy to do pól tekstowych.

### Zidentyfikowane Ryzyka

- Brak elastyczności w konfiguracji wyszukiwania dla klientów wymagających pól słownikowych
- Potrzeba obejść technicznych (tworzenie tekstowych odpowiedników pól słownikowych) zamiast natywnej obsługi

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dodanie obsługi wszystkich typów pól (słownikowe, lista wyboru, daty, numeryczne, użytkownik) | Pełna obsługa wszystkich typów pól z odpowiednimi mechanizmami wyszukiwania | ⏸️ Odroczona – zbyt skomplikowane dla dat i pól numerycznych (trzeba by dodać obsługę zakresów) |
| Dodanie tylko pól słownikowych i listy wyboru | Obsługa pól słownikowych i listy wyboru z wyszukiwaniem tekstowym | ✅ Wybrana – w miarę proste do zaimplementowania |
| Dodanie również pola użytkownika | Obsługa pola użytkownika po nazwie wyświetlanej jako tekst | ⏸️ Odroczona – Piotr Buczkowski zaproponował tylko słownik i listę wyboru |
| Dodanie pól numerycznych i dat | Obsługa z zakresami dla dat i liczb | ❌ Odrzucona – bardziej skomplikowane, trzeba by zrobić jakiś zakres, a nie wyszukiwać po dokładnej wartości |

### Decyzja

**Status:** ✅ Zatwierdzone

Rozszerzona zostanie funkcjonalność pola "Odnośnik do procesu" o obsługę pól słownikowych i listy wyboru. Dla słownikowych wyszukujemy tekst (po nazwie wyświetlanej). Dla listy wyboru będzie to wpisywanie z palca, a nie wybór z listy (tak samo jak dla słownika). Pola numeryczne i daty zostają na razie bez obsługi.

**Szczegóły techniczne:**
- Warunek: musi być włączone Lucene dla słowników (dla listy wyboru wszystko jedno)
- Dla słownika trzeba oddzielnie oprogramować obie opcje (z Lucene i bez), bo to będzie trochę inaczej
- W Lucene wszystko jest tekstem, więc wrzucenie pola słownikowego zadziała, ale będzie ten sam problem co normalnie przy polach tekstowych przypisujących dane ze słownika – jeżeli słownik się zmieni, w sprawie zostanie stara wartość
- Domyślnie jest `LIKE` od początku, jest opcja "wyszukiwanie przez Lucene", którą można włączyć w ustawieniach tego pola w procesie

### Zadania

- **[Piotr Buczkowski]:** Zaimplementować obsługę pól słownikowych w polu "Odnośnik do procesu" (z obsługą obu opcji: z Lucene i bez)
- **[Piotr Buczkowski]:** Zaimplementować obsługę listy wyboru w polu "Odnośnik do procesu"

### Punkty otwarte

- Perspektywa czasowa: na pewno nie w najbliższym sprincie, będzie po pierwszym kwartale przyszłego roku (chyba że klient chce sfinansować przyspieszenie prac)
- Czy w przyszłości dodać obsługę pól numerycznych i dat z zakresami?

---

## 2. Termin ważności dokumentów w Trust Center i wygaszanie porzuconych dokumentów

**Projekt:** `moduly/Trust-Center`

### Kontekst i Problem

Nie ma ram czasowych dla dokumentów wysyłanych do Trust Center na czas nieokreślony. Można ręcznie ustawić datę, do której jest możliwość podpisania, i wtedy po jej przekroczeniu dokument się blokuje. Jeżeli się tego nie poda, to dokument wisi w Blob storage, a z hot storage jest usuwany po 21/30 dniach (21 dni od daty ostatniej modyfikacji lub 30 dni, jeśli nic się nie działo). Proces w Trust Center wisi jako aktywny w nieskończoność – dokument wisi w bazie jako możliwy do podpisania. Jest 106 dokumentów starszych niż 3 miesiące, które mają status 0 i nie mają już podglądu, bo zostały usunięte z hot storage. Ta ścieżka nie jest oprogramowana – przy próbie wejścia na taki dokument Trust Center próbuje od razu pobrać plik podpisany, zakładając błędnie, że po takim czasie powinien być podpisany. Nie da się wejść na te dokumenty (ślepa uliczka). Aktualnie, jeśli jest taki problem, klient wysyła dokument jeszcze raz, a stary wisi jako śmietnik.

### Zidentyfikowane Ryzyka

- Dokumenty mogą wisieć w Trust Center w nieskończoność bez sensu biznesowego
- Koszty związane z trzymaniem dokumentów w hot storage
- Brak dostępu do dokumentów przeniesionych do blob storage (niepodpisanych)
- Brak jasnych ram czasowych dla dokumentów bez określonego terminu podpisania

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ustawienie domyślnego terminu 30 dni dla dokumentów bez określonej daty | Jeśli klient nie ustawił daty, automatycznie ustawiamy 30 dni | 🔍 Do weryfikacji – wymaga analizy danych |
| Ustawienie maksymalnego nieprzekraczalnego czasu (np. 90 lub 180 dni) | Po określonym czasie dokument jest usuwany, nawet jeśli klient ustawił dłuższą datę | 🔍 Do weryfikacji – wymaga analizy danych |
| Monetyzacja dłuższych terminów | Standardowy dostęp 14 dni jest w cenie, chcesz 30 dni – płacisz 50 groszy więcej, chcesz 180 dni – płacisz 5 zł więcej | 💡 Propozycja – do rozważenia po analizie danych |
| Obsługa ścieżki dostępu do dokumentów w blob storage | Dajemy dostęp do dokumentów przeniesionych do blob storage (niepodpisanych) | ⏸️ Odroczona – najpierw ustalmy datę graniczną i cennik |
| Wygaszanie dokumentów bez dostępu | Jeśli ustalimy, że takie procesy będą wygaszane po określonym czasie, to nie ma sensu dawać dostępu | 🔍 Do weryfikacji – wymaga analizy danych |

### Decyzja

**Status:** 🔍 Do weryfikacji

Najpierw trzeba ustalić biznesowy termin ważności na podstawie analizy danych. Marek Dziakowski ma przygotować zestawienie:
- Jakie są najdłuższe terminy faktycznie używane przez klientów
- Jaki jest faktyczny czas od wysłania do zamknięcia procesu
- Czy ktoś wysyła dokumenty z datą podpisania dłuższą niż 30 dni

Na podstawie tej analizy zostaną podjęte decyzje:
- Jaki termin przyjąć jako domyślny dla dokumentów bez określonej daty
- Czy wprowadzić maksymalny nieprzekraczalny czas (np. 90 lub 180 dni)
- Czy monetyzować dłuższe terminy
- Czy obsłużyć ścieżkę dostępu do dokumentów w blob storage (jeśli okaże się, że są potrzebne)

**Szczegóły techniczne:**
- Dokumenty z hot storage są usuwane po 21 dniach od daty ostatniej modyfikacji lub 30 dniach, jeśli nic się nie działo
- W AMODIT jest tak, że jak coś przejdzie do bloba, to w razie potrzeby da się to stamtąd pociągnąć (to rzadki przypadek, ale jest obsłużony)
- Jeśli klient ustawił jakąkolwiek datę, powinna ona obowiązywać, nawet 180 dni (Janusz Bossak)
- Jeśli nie ustawił, to my ustawiamy domyślnie, np. 30 dni (Janusz Bossak)

### Zadania

- **[Marek Dziakowski]:** Przygotować zestawienie: jakie są najdłuższe terminy faktycznie używane przez klientów, jaki jest faktyczny czas od wysłania do zamknięcia procesu, czy ktoś wysyła dokumenty z datą podpisania dłuższą niż 30 dni → termin: do następnej rady
- **[Marek Dziakowski]:** Po analizie danych – zaimplementować mechanizm wygaszania dokumentów zgodnie z ustalonymi ramami czasowymi
- **[Marek Dziakowski]:** Po ustaleniu ram czasowych – ewentualnie obsłużyć ścieżkę dostępu do dokumentów w blob storage (jeśli okaże się potrzebna)

### Punkty otwarte

- Jaki termin przyjąć jako domyślny dla dokumentów bez określonej daty?
- Czy wprowadzić maksymalny nieprzekraczalny czas (np. 90 lub 180 dni)?
- Czy monetyzować dłuższe terminy?
- Czy obsłużyć ścieżkę dostępu do dokumentów w blob storage (jeśli okaże się, że są potrzebne, a nie są to stare testowe dokumenty)?

---

## 3. Problemy z filtrami w raportach – "zaznacz wszystko" i DISTINCT

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

Funkcja "zaznacz wszystko" nie zaznacza wszystkiego. Przykład: na raporcie były 3 elementy, a wyświetlały się 2 z 3. Dane do filtrów są pobierane z dwóch miejsc. Jeśli polem jest "etap", to pobierane są wszystkie etapy bez ograniczenia do 20 pozycji, ale jeśli etapy mają tę samą nazwę, są zwijane do jednej pozycji. Dla każdego innego pola jest inaczej: zapytanie bierze pod uwagę tylko to jedno pole i pobiera 20 pierwszych pozycji z wyniku raportu. Problem: jeśli pozycji jest więcej niż 20 unikalnych, "zaznacz wszystko" zaznaczy tylko te 20 widoczne. Dodatkowo, prawdopodobnie nie jest robiony `DISTINCT` i po prostu zwraca np. 10 razy "BI", co zajmuje 10 z 20 pozycji, a reszty nie widać. Kod, który to zwraca, był pisany pod dane do raportu, a nie do filtrów.

### Zidentyfikowane Ryzyka

- Nieprawidłowe działanie funkcji "zaznacz wszystko" może powodować problemy użytkowników
- Brak `DISTINCT` powoduje duplikaty w liście filtrów
- Ograniczenie do 20 pozycji powoduje, że nie wszystkie opcje są widoczne
- Problem z ilością parametrów w `IN (...)` – nie powinno być więcej niż 500-1000

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dodanie `DISTINCT` do zapytania | Grupowanie wyników, żeby brało tylko pojedyncze wystąpienia | ✅ Wybrana – pierwszy krok do poprawy |
| Zmiana logiki "zaznacz wszystko" na `LIKE` w SQL | "Zaznacz wszystko" zamienia operator `=` na `zawiera` | 🔍 Do weryfikacji – wymaga dalszej analizy |
| Dodanie przycisku "Załaduj więcej" | Umożliwienie załadowania kolejnych 20 pozycji | 🔍 Do weryfikacji – wymaga dalszej analizy |
| Dodanie ograniczenia liczby parametrów w filtrze | Ograniczenie do 500-1000 parametrów w `IN (...)` | 🔍 Do weryfikacji – wymaga dalszej analizy |
| Dodanie filtra "zawiera" dla wartości liczbowych | Umożliwienie wyszukiwania po części wartości | 🔍 Do weryfikacji – wymaga dalszej analizy |
| Filtry oddziałujące na siebie (jak w Excelu) | Jak ograniczę zbiór danych jednym filtrem, to w drugim widzę tylko opcje pasujące do już okrojonego wyniku | 🔍 Do weryfikacji – rodzi problemy wydajnościowe, bo po zmianie jednego filtra trzeba by przeliczać wszystkie inne |

### Decyzja

**Status:** 🔍 Do weryfikacji

Najpierw zostanie zrobione zadanie z dodaniem `DISTINCT` do zapytania (dodanie flagi w zapytaniu, żeby brało `DISTINCT`). Reszta tematów zostanie rozbita na osobne PBI w ramach nowego feature'a i będzie dalej omawiana na osobnej radzie architektów. Trzeba zrobić refaktoryzację, żeby poprawianie filtrów nie psuło legendy i na odwrót.

**Szczegóły techniczne:**
- Dla pola "etap" pobierane są wszystkie etapy bez ograniczenia do 20 pozycji
- Dla każdego innego pola zapytanie bierze pod uwagę tylko to jedno pole i pobiera 20 pierwszych pozycji z wyniku raportu
- Trzeba dodać flagę w zapytaniu, żeby brało `DISTINCT`
- Kod był pisany pod dane do raportu, a nie do filtrów
- Aktualnie dla szóstki wyszukuje wszystkie kombinacje (6, 16, 60), więc działa jak `LIKE`
- Wyniki i tak są dzielone na strony, więc nie pobierze się miliona naraz
- Jeśli w filtrze nic nie wpisano, "zaznacz wszystko" powinno oznaczać brak filtrowania (Janusz Bossak)
- Jeśli nic nie wpisano, przycisk "zaznacz wszystko" nie powinien być w ogóle widoczny (Damian Kaminski)

### Zadania

- **[Anna Skupinska]:** Opisać zadanie z dodaniem `DISTINCT` do zapytania wraz z kryteriami akceptacji
- **[Anna Skupinska]:** Przygotować propozycje rozwiązań na następne spotkanie dla tematów: 1. Jak i czy dodawać ograniczenie liczby parametrów w filtrze, 2. Czy dodać przycisk "Załaduj więcej", 3. Jak ma działać "Zaznacz wszystko", 4. Dodanie filtra "zawiera" dla wartości liczbowych
- **[Anna Skupinska]:** Zamienić PBI na feature i rozbić resztę tematów na osobne PBI w ramach tego feature'a

### Punkty otwarte

- Jak dokładnie ma działać "zaznacz wszystko" – czy zamienia operator `=` na `zawiera`?
- Czy dodać przycisk "Załaduj więcej" dla list z więcej niż 20 pozycjami?
- Jak obsłużyć problem z ilością parametrów w `IN (...)` przy więcej niż 500-1000 pozycjach?
- Czy dodać filtr "zawiera" dla wartości liczbowych?
- Czy filtry powinny oddziaływać na siebie (jak w Excelu), czy to rodzi zbyt duże problemy wydajnościowe?

