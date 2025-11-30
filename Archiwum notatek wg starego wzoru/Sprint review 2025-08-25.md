[[2025-10-06 Sprint review]] [[2025-08-25 poniedziałek]]

### Sprint review z dnia 25 sierpnia 2025

---

#### 1. Podpisywanie dokumentów na macOS

- **Dlaczego to robimy**
    - Celem jest umożliwienie składania podpisu kwalifikowanego w module Trust Center użytkownikom pracującym na systemie operacyjnym macOS.

- **Opis funkcjonalności / rozwiązania:**
    - Stworzono działający prototyp aplikacji (tzw. proof of concept), która pozwala na podpisanie dokumentu z Trust Center.
    - Aplikacja została napisana w technologii .NET MAUI. Udało się pokonać kluczową barierę techniczną, jaką był dostęp do certyfikatów na macOS z tego środowiska.
    - Aplikacja jest budowana jako samodzielna paczka (`self-contained`), co oznacza, że nie wymaga od użytkownika instalacji dodatkowego środowiska .NET na komputerze.
    - Pomyślnie przeprowadzono testy podpisywania przy użyciu różnych dostawców: Szafir (podpis fizyczny na czytniku), mSzafir (podpis chmurowy) oraz SimplySign.
    - Podpis złożony za pomocą aplikacji został pomyślnie zweryfikowany przez oficjalny walidator Unii Europejskiej, co potwierdza jego poprawność techniczną.

- **Dalsze kroki:**
    - Zaprezentowana wersja jest prototypem i wymaga gruntownego dopracowania interfejsu, aby był prosty i intuicyjny dla końcowego użytkownika.
    - Docelowo proces musi być w pełni zautomatyzowany – użytkownik nie powinien ręcznie wskazywać ścieżek do bibliotek. System ma sam wykrywać zainstalowane certyfikaty.
    - Konieczne będzie przetestowanie i zapewnienie wsparcia dla wszystkich głównych dostawców podpisów kwalifikowanych w Polsce.
    - Priorytetem jest obsługa podstawowego scenariusza podpisywania w Trust Center. Bardziej zaawansowane funkcje (np. podpisywanie z poziomu raportów) nie są obecnie priorytetem.

---

#### 2. Matryca uprawnień

- **Dlaczego to robimy**
    - Stworzenie bardziej wygodnego i globalnego sposobu definiowania oraz odczytywania uprawnień dla pól w formularzach. Dotychczasowy sposób, wymagający wchodzenia w edycję każdego pola osobno, był nieintuicyjny i nie pozwalał na całościowy przegląd.

- **Opis funkcjonalności / rozwiązania:**
    - Zaprezentowano wczesną wersję nowego, tabelarycznego widoku (matrycy), w którym wiersze reprezentują pola i sekcje formularza, a kolumny – etapy procesu.
    - Matryca zachowuje strukturę formularza, poprawnie grupując pola w sekcjach i tabelach.
    - Użytkownik może bezpośrednio w komórce matrycy zmienić uprawnienie dla danego pola na konkretnym etapie.
    - Zaimplementowano mechanizm dziedziczenia uprawnień z nadrzędnej sekcji, co jest sygnalizowane ikoną "łańcucha" i podpowiedzią (tooltip).
    - Wprowadzono obsługę wyjątków od uprawnień dla konkretnych użytkowników; jeśli wyjątek jest zdefiniowany, ikona otwierająca okno edycji wyjątków zmienia kolor na pomarańczowy.

- **Dalsze kroki:**
    - Planowane jest dodanie "trybu kompaktowego", który ukryje tekstowe opisy uprawnień, pozostawiając same ikony, co pozwoli zmieścić na ekranie więcej etapów procesu.
    - Interfejs użytkownika (np. umiejscowienie ikon) wymaga dalszych konsultacji, ponieważ obecne rozmieszczenie jest mało intuicyjne.
    - Funkcjonalność będzie testowana na bardziej złożonych procesach w celu weryfikacji jej czytelności i wydajności.
    - W planach jest dodanie funkcjonalności filtrowania, która pozwoli na wyświetlanie tylko wybranych etapów procesu.

---

#### 3. Widok Zadań (Jobów)

- **Dlaczego to robimy**
    - Usprawnienie interfejsu do zarządzania zadaniami cyklicznymi (jobami), aby był bardziej intuicyjny i spójny z nowym wyglądem ustawień systemowych.

- **Opis funkcjonalności / rozwiązania:**
    - Stworzono nowy widok w formie tabeli, który zastępuje stary, mniej czytelny interfejs tekstowy.
    - Dodano nowe okno do edycji i dodawania zadań z bardziej intuicyjnym konfiguratorem harmonogramu.
    - Nowy konfigurator ułatwia ustawianie złożonych harmonogramów (np. "co X godzin", "w określonym przedziale czasowym"), automatycznie przeliczając je na format `cron` i wyświetlając podgląd wyliczonej częstotliwości.

- **Dalsze kroki:**
    - Zamiast ręcznego wpisywania nazw bibliotek i klas, zostanie zaimplementowana lista wyboru, która będzie dynamicznie pobierać dostępne w systemie joby. Ma to na celu wyeliminowanie błędów związanych z literówkami.
    - Format wyświetlania daty zostanie ujednolicony z resztą systemu.

---

#### 4. Konfiguracja integracji

- **Dlaczego to robimy**
    - Uproszczenie i zabezpieczenie procesu konfiguracji integracji poprzez wprowadzenie podpowiedzi i walidacji, co ma eliminować proste błędy ludzkie (np. literówki) i usprawnić pracę konsultantów.

- **Opis funkcjonalności / rozwiązania:**
    - Wprowadzono nowy interfejs do dodawania parametrów integracji, podzielony na kategorie: ogólny, endpoint i inny.
    - Dla parametrów "ogólnych" (np. typ autoryzacji) dostępne są predefiniowane listy wyboru, co zapobiega błędom.
    - Dla parametrów niestandardowych ("innych") system pilnuje stosowania odpowiedniego prefiksu i uniemożliwia ręczne tworzenie parametrów, które już istnieją na liście predefiniowanej.
    - Parametry można grupować, co poprawia czytelność konfiguracji przy dużej liczbie parametrów w ramach jednej integracji.
    - Istnieje możliwość włączania i wyłączania poszczególnych integracji.

- **Dalsze kroki:**
    - Należy zwiększyć limit znaków dla nazw parametrów w bazie danych, aby uniknąć problemów z długimi nazwami endpointów.
    - Należy rozważyć ukrycie technicznych prefiksów (np. `external.rest.`) w interfejsie użytkownika, aby poprawić czytelność.
    - Podjęto decyzję o rozdzieleniu "Integracji" (wbudowanych) i "Rozszerzeń" (dedykowanych) na dwie osobne pozycje w menu, aby zachować logiczny podział.

---

#### 5. Gradienty w raportach

- **Dlaczego to robimy**
    - Umożliwienie użytkownikom personalizacji kolorystyki w raportach, w szczególności w wykresach typu Pivot i Treemap, gdzie gradienty kolorów reprezentują skalę wartości.

- **Opis funkcjonalności / rozwiązania:**
    - W edytorze raportu dodano możliwość edycji palety kolorów dla gradientów.
    - Użytkownik może zdefiniować własne kolory dla wartości minimalnych, maksymalnych i środkowych (zero).
    - Dostępna jest opcja resetowania do domyślnej palety kolorów.
    - Funkcjonalność działa zarówno dla wartości dodatnich, jak i ujemnych.

- **Dalsze kroki:**
    - Funkcjonalność gradientów zostanie w przyszłości rozszerzona także na inne typy wykresów (np. słupkowe).

---

#### 6. Komunikator

- **Dlaczego to robimy**
    - Dokończenie prac i stabilizacja nowego modułu komunikatora, w tym poprawa interfejsu i dodanie kluczowych funkcjonalności, m.in. na potrzeby konkretnego klienta.

- **Opis funkcjonalności / rozwiązania:**
    - Komunikator można otworzyć jako nakładkę lub w osobnej karcie przeglądarki.
    - Zaimplementowano mechanizm "infinite scroll" do automatycznego doczytywania starszych wiadomości podczas przewijania w górę.
    - Dodano wskaźnik informujący, że rozmówca aktualnie pisze wiadomość.
    - Niedokończone wiadomości są tymczasowo zapisywane w `localStorage`, dzięki czemu nie są tracone po przełączeniu konwersacji.
    - Wyszukiwanie użytkowników do nowej konwersacji odbywa się z paginacją, co poprawia wydajność.
    - Rozróżniono konwersacje prywatne (bez możliwości zmiany nazwy) i grupowe (z opcją zarządzania uczestnikami i nazwą).
    - Zaimplementowano wzmiankowanie użytkowników.

- **Dalsze kroki:**
    - Należy ujednolicić nazewnictwo w całym module. Obecnie zamiennie używane są terminy "Komunikator", "Czat", "Konwersacja" i "Amodit Tok", co wprowadza chaos.
    - Należy zapewnić spójność wizualną komponentów (np. pola wyszukiwania, awatary) z resztą systemu.
    - Kwestia przechowywania danych zostanie sfinalizowana, z tendencją do używania tej samej bazy danych co reszta systemu, zarówno w chmurze, jak i on-premise.
    - Należy finalnie zweryfikować zabezpieczenia przed atakami XSS.

---

#### 7. Fakturowanie (Billing)

- **Dlaczego to robimy**
    - Usprawnienie wewnętrznego narzędzia do zarządzania organizacjami i rozliczeniami na chmurze, aby ułatwić pracę osobom generującym faktury.

- **Opis funkcjonalności / rozwiązania:**
    - W panelu administracyjnym dodano nowe pola: "Osoba do kontaktu" dla organizacji oraz "Komentarz" dla limitów.
    - Dodano również pole do rozróżnienia środowisk testowych od produkcyjnych.

- **Dalsze kroki:**
    - Celem wprowadzonych zmian jest ułatwienie filtrowania i identyfikacji klientów oraz typów ich środowisk, co przyspieszy proces fakturowania.

---

#### 8. Filtry wymagane i domyślne w raportach

- **Dlaczego to robimy**
    - Rozwiązanie problemu wydajności i czytelności raportów opartych na bardzo dużych zbiorach danych (np. logi systemowe, sprawy ze wszystkich procesów), które bez filtrowania były bezużyteczne.

- **Opis funkcjonalności / rozwiązania:**
    - W edytorze raportu dodano opcję oznaczenia filtra jako "wymagany".
    - Jeśli filtr jest wymagany, a użytkownik nie ustawi jego wartości, raport nie wyświetli danych, a zamiast tego pokaże komunikat z prośbą o ustawienie filtru.
    - Dla każdego filtra można również ustawić "wartość domyślną", która zostanie automatycznie zastosowana przy pierwszym otwarciu raportu.
    - Użytkownik nadal może zmienić wartość filtru lub ją wyczyścić. Jego ostatnie ustawienia są zapamiętywane w `localStorage`, ale wartość domyślna jest ponownie stosowana po wyczyszczeniu i odświeżeniu.

- **Dalsze kroki:**
    - Funkcjonalność jest gotowa i będzie wykorzystywana do poprawy użyteczności nowych raportów systemowych.