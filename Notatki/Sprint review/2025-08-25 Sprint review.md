# Sprint Review – 2025-08-25

**Powiązane projekty:**
- `klienci/WIM/Podpis-kwalifikowany-macOS` – temat 1
- `moduly/Modul-raportowy` – tematy 2, 5
- `klienci/WIM/Komunikator` – temat 3
- `moduly/Ustawienia-systemowe` – temat 4
- `moduly/Silnik-regul` – temat 6

---

## 1. Podpisywanie dokumentów na macOS

**Projekt:** `klienci/WIM/Podpis-kwalifikowany-macOS`

### Cel biznesowy

Umożliwienie użytkownikom macOS składania podpisów kwalifikowanych w module Trust Center. Obecna aplikacja działa wyłącznie na Windows, co zmusza użytkowników macOS do szukania obejść lub korzystania z innych komputerów. Główny scenariusz: użytkownik otrzymuje mail z Trust Center, że ma dokument do podpisania, wchodzi na macOS i powinien móc podpisać dokument z jak najmniejszą liczbą pytań i kroków.

### Co zaimplementowano

- **Prototyp aplikacji** (.NET MAUI) umożliwiający podpisywanie dokumentów na macOS
- **Pokonanie bariery technicznej:** dostęp do certyfikatów na macOS z .NET MAUI (problem, którego nie udało się rozwiązać wcześniej)
- **Build self-contained:** aplikacja nie wymaga instalacji środowiska .NET przez użytkownika końcowego
- **Testy z dostawcami podpisów:**
  - Szafir (podpis fizyczny na czytniku)
  - mSzafir (podpis chmurowy)
  - SimplySign
- **Walidacja przez oficjalny walidator Unii Europejskiej:** podpis został pozytywnie zweryfikowany

### Jak to działa (jeśli omówiono)

Aplikacja jest 3-krokowa:
1. Wybór biblioteki dostawcy podpisu (Szafir, SimplySign, etc.)
2. Ładowanie certyfikatów z czytnika/Keychain
3. Podpisanie dokumentu (wymagany PIN)

Na macOS każda biblioteka dostawcy znajduje się w miejscu instalacji aplikacji obsługującej dany certyfikat. System będzie automatycznie wykrywał zainstalowanych dostawców i ładował odpowiednie biblioteki.

### Ograniczenia / Known issues

- **Prototyp techniczny:** obecna wersja jest bardzo techniczna i nieprzyjazna dla użytkownika końcowego
- **Ręczny wybór biblioteki:** użytkownik musi ręcznie wybierać bibliotekę dostawcy (docelowo ma być automatyczne wykrywanie)
- **Brak automatycznego wykrywania:** system nie wykrywa jeszcze automatycznie zainstalowanych certyfikatów
- **Obsługa wielu certyfikatów:** jeśli użytkownik ma 2 podpisy, będzie musiał mieć 2 biblioteki (do obsłużenia)
- **UI wymaga przebudowy:** interfejs wymaga dopracowania, aby był prosty i intuicyjny
- **Brak obsługi podpisywania z raportów:** priorytetem jest tylko podpisywanie z Trust Center

### Feedback z demo

- **💭 Pomysł Przemka:** Aplikacja powinna działać tak, jak użytkownik oczekuje – z jak najmniejszą liczbą pytań. Jeśli użytkownik ma podpis chmurowy i zwykły, powinno być jasne, który wybrać (np. "podpis kwalifikowany na urządzeniu" vs "podpis chmurowy"). Użytkownik powinien być prowadzony za rękę: kliknąć OK, wpisać PIN i podpisać.
- **💭 Pomysł Przemka:** Nie należy rozszerzać funkcjonalności zbyt szeroko – skupić się na jednym konkretnym przypadku (Trust Center), ale zrobić go jak najwygodniej.
- **Piotr Buczkowski:** Trzeba przejść przez wszystkich dostawców podpisów i przygotować obsługę. Jeśli przypadek nie jest obsługiwany, można zrobić SELECT (wybór ręczny) i raportować, czego ludzie używają.

### Dalsze kroki

- **Przebudowa UI:** dopracowanie interfejsu, aby był prosty i intuicyjny dla użytkownika końcowego
- **Automatyczne wykrywanie certyfikatów:** system ma automatycznie wykrywać zainstalowanych dostawców i ładować odpowiednie biblioteki
- **Obsługa wszystkich głównych dostawców:** przetestowanie i zapewnienie wsparcia dla wszystkich głównych dostawców podpisów w Polsce
- **Przechowywanie bibliotek:** rozwiązanie kwestii przechowywania bibliotek (systemowa lokalizacja na maszynie lub pobieranie przy starcie)
- **Szacowany czas:** około półtora miesiąca intensywnych testów i dopracowania (zakładając, że publikowanie zrobimy)

---

## 2. Edycja gradientów w raportach

**Projekt:** `moduly/Modul-raportowy`

### Cel biznesowy

Umożliwienie użytkownikom personalizacji kolorystyki w raportach, szczególnie w wykresach typu Pivot i Treemap, gdzie gradienty kolorów reprezentują skalę wartości. Wymaganie od klienta (Piotr Murawski) – chciał mieć możliwość zadawania własnych kolorów zamiast tylko niebieskiego do brązowego.

### Co zaimplementowano

- **Edycja palety gradientów** w edytorze raportu
- **Definiowanie kolorów:**
  - Kolor dla wartości minimalnych
  - Kolor dla wartości maksymalnych
  - Kolor dla wartości środkowych (zero)
- **Resetowanie do domyślnej palety:** opcja przywrócenia domyślnych kolorów
- **Obsługa wartości dodatnich i ujemnych:** możliwość ustawienia różnych kolorów dla wartości dodatnich i ujemnych
- **Obsługa w typach wykresów:** Treemap i Pivot (na razie)

### Jak to działa (jeśli omówiono)

Użytkownik w edytorze raportu może wybrać kolory z palety (w stylu v0) lub wprowadzić własne kolory. Po zastosowaniu kolory są zapisywane i używane w raporcie. Gradient jest generowany automatycznie między wartościami minimalnymi, maksymalnymi i środkowymi.

### Ograniczenia / Known issues

- **Tylko Treemap i Pivot:** funkcjonalność działa na razie tylko w tych typach wykresów
- **Brak obsługi w kolumnowych:** kolory gradientowe w wykresach kolumnowych nie zostały jeszcze skorygowane (wymaga konsultacji z Markiem)
- **Brak możliwości przesuwania skali:** na razie nie można przesunąć środka skali (zero) na inną wartość (może być w przyszłości)

### Feedback z demo

- **Przemysław Sołdacki:** Wygląda podobnie jak Tableau – można ustawić gradient w sposób ciągły lub w krokach. Dobrze widać, które wartości są dodatnie, które ujemne, a które bliskie zera (szare). Warto dodać to do wszystkich typów wykresów, np. słupkowych.
- **Przemysław Sołdacki:** Gradient może być używany na dwa sposoby: jako spektrum palety (nasilenie koloru) lub jako przypisanie koloru do konkretnej kategorii (np. marchewka = pomarańczowy, pomidor = czerwony). W Treemapie już działa przypisanie do kategorii.

### Dalsze kroki

- **Rozszerzenie na inne typy wykresów:** dodanie obsługi gradientów w wykresach słupkowych i innych typach
- **Konsultacja z Markiem:** dopracowanie kolorów gradientowych w wykresach kolumnowych
- **Możliwość przesuwania skali:** dodanie opcji przesunięcia środka skali (zero) na inną wartość
- **Więcej punktów kontrolnych:** możliwość dodania większej liczby punktów kontrolnych w gradiencie (więcej kolorów pośrednich)

---

## 3. Komunikator (AMODIT Talk) – stabilizacja i poprawki

**Projekt:** `klienci/WIM/Komunikator`

### Cel biznesowy

Dokończenie prac i stabilizacja nowego modułu komunikatora, poprawa interfejsu i dodanie kluczowych funkcjonalności na potrzeby klienta (WIM). Komunikator ma umożliwić szybką komunikację wewnętrzną między użytkownikami systemu.

### Co zaimplementowano

- **Otwarcie w nowym oknie:** opcja w ustawieniach systemowych do otwierania komunikatora w osobnym oknie zamiast osobnej karty
- **Zmiana ikony:** ikona zmieniona z Messengera na Outlook z MD
- **Licznik nowych wiadomości:** wyświetlanie liczby nowych wiadomości po prawej stronie (nie w nawiasie)
- **Infinite scroll:** automatyczne doczytywanie starszych wiadomości przy przewijaniu do góry
- **Przycisk przejścia w dół:** automatyczny przycisk do przewinięcia na dół do najnowszych wiadomości
- **Wskaźnik "rozmówca pisze":** informacja, że ktoś aktualnie pisze wiadomość
- **Zapis niedokończonych wiadomości:** automatyczne zapisywanie w localStorage, aby nie tracić treści przy zmianie czatu
- **Paginacja użytkowników:** zmiana pobierania użytkowników na paginację (przy przewijaniu w dół pobierają się kolejni)
- **Konwersacje prywatne i grupowe:**
  - Konwersacja prywatna: nie można zmieniać nazwy ani zarządzać nią
  - Konwersacja grupowa: można usuwać użytkowników, dodawać, zmieniać nazwę grupy
- **Wzmiankowanie użytkowników:** możliwość wzmiankowania osób w grupie (@)
- **Strona z logami:** strona do przeglądania logów błędów AMODIT Talk (filtrowanie po typie błędów)

### Jak to działa (jeśli omówiono)

Komunikator działa jako osobna aplikacja SignalR. W środowisku on-premises łączy się bezpośrednio z bazą danych klienta. W środowisku chmurowym pobiera informacje z centralnej bazy o tym, na jakiej bazie jest trzymany klient, i łączy się z odpowiednią bazą. Dane są przechowywane w tych samych tabelach co reszta AMODIT (nie w osobnej bazie).

### Ograniczenia / Known issues

- **Niespójność nazewnictwa:** w różnych miejscach używane są różne nazwy: "komunikator", "AMODIT Talk", "czat", "konwersacja", "grupa" – wymaga ujednolicenia
- **Brak awatarów:** na razie bez awatarów użytkowników
- **Wzmiankowanie:** funkcjonalność wzmiankowania nie działa szczególnie (użytkownik i tak dostanie powiadomienie o nowej wiadomości)
- **Logi w oddzielnej tabeli:** logi są zapisywane w oddzielnej tabeli (Serilog), nie w standardowych logach AMODIT
- **Brak pełnej zgodności WCAG:** kontrast jest zgodny, ale dla niewidomych mogą być problemy z odczytaniem (do dopracowania)
- **Brak limitu znaków:** na razie brak limitu znaków na pojedynczą wiadomość (do dodania)
- **Różnice w komponentach:** niektóre komponenty (np. search) różnią się od standardowych komponentów AMODIT (warto używać tych samych)

### Feedback z demo

- **💭 Pomysł Przemka:** Ujednolicenie nazewnictwa – wszędzie powinna być jedna nazwa (np. "komunikator" lub "AMODIT Talk"), nie można używać różnych pojęć w różnych miejscach. Przykłady niespójności: "komunikator", "AMODIT Talk", "czat", "konwersacja", "grupa", "obecni członkowie czatu".
- **💭 Pomysł Przemka:** Logi powinny być w jednym miejscu z resztą logów AMODIT, nie w oddzielnej tabeli. Dla użytkownika to kłopot, a dla AI diagnostycznego będzie problem, że część funkcjonalności szuka w jednym miejscu, a część w drugim.
- **Łukasz Bott:** Zabezpieczenie przed atakami XSS – czy tekst jest odpowiednio zabezpieczony przed wstrzyknięciem kodu?
- **Piotr Buczkowski:** React automatycznie encoduje HTML, więc nie ma ryzyka XSS (cały HTML jest traktowany jako tekst).
- **Kamil Dubaniowski:** Warto używać tych samych komponentów co w reszcie AMODIT (np. search w menu po lewej), aby zachować spójność.
- **Adrian Kotowski:** Czy jest limit znaków na pojedynczą wiadomość? (Odpowiedź: można dodać limit, np. 30 000 znaków)

### Dalsze kroki

- **Ujednolicenie nazewnictwa:** przejrzenie wszystkich ekranów i ujednolicenie nazw (jedna nazwa wszędzie: "komunikator" lub "AMODIT Talk")
- **Dodanie awatarów:** implementacja awatarów użytkowników
- **Limit znaków:** dodanie limitu znaków na pojedynczą wiadomość
- **Ujednolicenie komponentów:** użycie standardowych komponentów AMODIT (np. search)
- **Pełna zgodność WCAG:** dopracowanie zgodności z WCAG dla niewidomych użytkowników
- **Integracja logów:** rozważenie przeniesienia logów do standardowych logów AMODIT lub dodanie linku/przełącznika między logami

---

## 4. Ustawienia systemowe – zarządzanie Jobami

**Projekt:** `moduly/Ustawienia-systemowe`

### Cel biznesowy

Usprawnienie konfiguracji zadań systemowych (Jobów) poprzez intuicyjny interfejs zamiast ręcznego wpisywania wartości w bazie danych. Obecne wartości w bazie nie są przejrzyste i nie są intuicyjne do dodawania, edytowania czy usuwania. Dodatkowo, konsultanci często nie potrafią poprawnie skonfigurować harmonogramu (np. włączają regułę co minutę, która chodzi w weekendy niepotrzebnie po północy).

### Co zaimplementowano

- **API do zarządzania Jobami:** dodawanie, usuwanie, edycja, wykonywanie akcji
- **Formularz dodawania Joba:**
  - Wybór biblioteki i klasy (z listy rozwijanej, nie ręczne wpisywanie)
  - Nazwa klasy preferowanym serwerem
  - Ustawienie częstotliwości działania (z podglądem godziny startu)
  - Wybór minuty startu (jeśli dotyczy)
- **Intuicyjna konfiguracja częstotliwości:** zamiast wpisywania wartości w minutach od północy, użytkownik wybiera:
  - Typ częstotliwości (co ile godzin, raz dziennie, etc.)
  - Godzinę startu
  - Godzinę zakończenia (jeśli dotyczy)
- **Podgląd harmonogramu:** wyświetlanie na dole, jak będzie wyliczana częstotliwość

### Jak to działa (jeśli omówiono)

System skanuje wszystkie klasy implementujące interfejs `IJob` przy starcie procesu i tworzy słownik dostępnych opcji. Użytkownik wybiera z listy rozwijanej, nie wpisuje ręcznie. Harmonogram jest przeliczany w tle na podstawie ustawień częstotliwości.

### Ograniczenia / Known issues

- **Prototyp:** obecna wersja jest prototypem, wymaga dopracowania
- **Format daty:** format daty nie jest spójny z resztą systemu (do poprawy)
- **Wyświetlanie daty:** data wyświetlana w dwóch linijkach zamiast jednej (do poprawy)
- **Brak walidacji:** na razie brak walidacji poprawności wpisanych wartości (do dodania)

### Feedback z demo

- **💭 Pomysł Przemka:** Dwie ikonki "Integracje" i "Rozszerzenia" wyglądają jak błąd (ta sama ikonka dwa razy). Warto zmienić jedną z ikonek lub połączyć w jedną zakładkę "Integracje".
- **Piotr Buczkowski:** Zachować format daty spójny z resztą systemu. Data powinna być w jednej linijce, nie dwóch.
- **Damian Kamiński:** Bardzo istotne, aby od razu zdefiniować wybór z listy (słownik), aby wyeliminować błędy wpisywania. To jest około 20-30 pozycji, więc łatwo o pomyłkę.
- **Łukasz Bott:** Uspójnienie z częstotliwościami reguł okresowych w procesach (ale wycofano się z tego ze względu na kompatybilność wsteczną).

### Dalsze kroki

- **Poprawa formatu daty:** ujednolicenie formatu daty z resztą systemu, wyświetlanie w jednej linijce
- **Walidacja:** dodanie walidacji poprawności wpisanych wartości
- **Słownik klas:** automatyczne skanowanie i tworzenie słownika dostępnych klas przy starcie systemu
- **Ujednolicenie ikonek:** zmiana jednej z ikonek "Integracje"/"Rozszerzenia" lub połączenie w jedną zakładkę

---

## 5. Filtry wymagane i domyślne w raportach

**Projekt:** `moduly/Modul-raportowy`

### Cel biznesowy

Rozwiązanie problemu raportów opartych na bardzo dużych zbiorach danych (np. logi systemowe), które bez filtrowania były bezużyteczne i powolne. Dodatkowo, wyświetlanie danych z wszystkich procesów i wszystkich etapów na jednym wykresie tworzyło "sieczkę" nieczytelnych danych. Idea: nie wyświetlać zawartości, dopóki użytkownik nie zdefiniuje wyraźnie wartości jakiegoś filtru.

### Co zaimplementowano

- **Filtry wymagane:**
  - Oznaczenie filtra jako "wymagany" w edytorze raportu
  - Raport nie wyświetla danych bez ustawienia wartości w wymaganym filtrze
  - Komunikat z prośbą o ustawienie filtru (border w kolorze żółtym)
  - Nie można schować filtra wymaganego (jeśli był schowany, zostanie pokazany)
- **Wartości domyślne dla filtrów:**
  - Automatyczne stosowanie wartości domyślnej przy pierwszym otwarciu raportu
  - Zapamiętywanie ostatnich ustawień w localStorage
  - Przywracanie wartości domyślnej po wyczyszczeniu i odświeżeniu (jeśli użytkownik nie ustawił własnej wartości)
- **Mechanizm sprawdzania:** wszystkie filtry są sprawdzane przy każdym wejściu w raport

### Jak to działa (jeśli omówiono)

Jeśli filtr jest oznaczony jako wymagany, użytkownik musi ustawić wartość, zanim zobaczy dane. Jeśli filtr ma wartość domyślną, jest automatycznie stosowana przy pierwszym otwarciu. Jeśli użytkownik zmieni wartość na inną niż domyślna, localStorage zapamięta jego wybór. Jeśli użytkownik wyczyści filtr i odświeży, wartość domyślna zostanie przywrócona.

### Ograniczenia / Known issues

- Brak (funkcjonalność działa zgodnie z założeniami)

### Feedback z demo

- **Mateusz Kisiel:** Czy wartość domyślna nadpisuje localStorage? (Odpowiedź: tak, ale localStorage zapamięta własne ustawienia użytkownika, a wartość domyślna jest stosowana tylko gdy filtr jest pusty)
- **Łukasz Bott:** W szczególności, że filtr "ogranicza zakres danych" na dole może być niewidoczny dla użytkownika, jeśli nie jest gdzieś wyraźnie zaznaczony w tytule lub opisie raportu.

### Dalsze kroki

- **Informowanie o ograniczeniach:** rozważenie dodania informacji o ustawionych filtrach "ograniczających zakres danych" w tytule lub opisie raportu
- **Rozszerzenie na więcej raportów:** zastosowanie filtrów wymaganych w raportach systemowych i innych raportach z dużymi zbiorami danych

---

## 6. Funkcja `foreach attachment` w silniku reguł

**Projekt:** `moduly/Silnik-regul`

### Cel biznesowy

Umożliwienie iteracji po załącznikach dodawanych swobodnie do sprawy (w prawym panelu) z poziomu reguł. Do tej pory nie było metody na dostęp do tych załączników i wykonywanie operacji na nich (np. stworzenie ZIP-a, znalezienie konkretnego pliku, zmiana nazwy).

### Co zaimplementowano

- **Funkcja `foreach attachment`:** możliwość iteracji po liście załączników w sprawie
- **Prototyp:** funkcjonalność jest w fazie prototypu, gotowa do pokazania po zakończeniu

### Jak to działa (jeśli omówiono)

Funkcja pozwala na iterację po załącznikach dodanych do sprawy i wykonywanie operacji na każdym z nich (np. stworzenie archiwum ZIP, przetworzenie plików, zmiana nazw).

### Ograniczenia / Known issues

- **Prototyp:** funkcjonalność jest jeszcze w fazie prototypu, nie została jeszcze zaprezentowana

### Feedback z demo

- Brak (funkcjonalność nie została jeszcze zaprezentowana)

### Dalsze kroki

- **Zakończenie prototypu:** dokończenie prac nad prototypem i prezentacja funkcjonalności
- **Dokumentacja:** przygotowanie dokumentacji użycia funkcji `foreach attachment`

---

## 7. Uwagi ogólne ze Sprint Review

### Roadmapa

**💭 Pomysł Przemka:** Brakuje powiązania prezentowanych funkcjonalności z roadmapą. Wiele rzeczy prezentowanych na Sprint Review nie ma na roadmapie, a rzeczy z roadmapy nie mają komentarza, co się z nimi dzieje. Warto aktualizować roadmapę, gdy robimy coś, co nie było zaplanowane (np. komunikator) – dopisać do roadmapy i zaznaczyć jako wykonane. Na koniec każdego kwartału warto mieć informację, co się udało, co się nie udało, co zmieniliśmy i czego nie robimy.

**Decyzja:** Damian zobowiązał się do spotkania w dedykowanym gronie w celu aktualizacji roadmapy.

### Kontekst biznesowy

Wiele funkcjonalności prezentowanych na Sprint Review było realizowanych pod wymagania klienta WIM, co częściowo wywraca roadmapę, ale jest to akceptowalne ze względu na potrzeby biznesowe.

