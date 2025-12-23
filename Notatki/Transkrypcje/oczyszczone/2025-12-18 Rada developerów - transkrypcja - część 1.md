**Data spotkania:** 18 grudnia 2025, 09:08

---

**Anna Skupińska:** Cześć.

**Janusz Bossak:** Cześć.

**Anna Skupińska:** Czy jest nagrywanie?

**Janusz Bossak:** Podobno jest.

**Damian Kamiński:** To jest temat bardziej koncepcyjny niż deweloperski. Chciałbym przedstawić pewien aspekt i zapytać, czy zgadzacie się z moją wizją, czy widzicie jakieś zagrożenia.

Przejdźmy do rzeczy. Na przykładzie faktur – za chwilę wejdą nam obiegi faktur poufnych i ogólnych. Najprostsze rozwiązanie, jakie mi przychodzi do głowy, to aby proces faktur poufnych (jeśli jeszcze nie istnieje) był kopią procesu faktur ogólnych, aby zachować wszystkie pola. Jeśli jest to zintegrowane z KSeF, to ten proces powinien być zasilany przez KSeF Connector. Następnie na tym procesie działałaby reguła cykliczna: jeśli NIP kontrahenta nie znajduje się w określonej puli, następuje akcja "assign procedure" i przepisanie sprawy do procesu docelowego z przeniesieniem wszystkich wartości pól.

Można ewentualnie zrobić trzeci proces inicjujący obiegi, ale nie wiem czy to potrzebne. W moim pomyśle mamy zachowaną sytuację, że nic na faktury ogólne nie wpadnie przypadkowo, bo najpierw wszystko trafia do procesu faktur poufnych. Testowałem to na uproszczonym przypadku i działa. Co o tym sądzicie?

**Janusz Bossak:** Na razie nie mam pomysłu, tylko uchem słuchałem.

**Damian Kamiński:** Problem polega na tym, że mamy jedno źródło danych w postaci KSeF-a i wszystko musi trafiać do jednego miejsca. Klienci będą od nas oczekiwać zaopiekowania tego tematu.

**Janusz Bossak:** Kiedyś była koncepcja różnego poziomu poufności dokumentów. Druga rzecz to klasyfikacja, najlepiej automatyczna, która decyduje czy coś trafi na proces poufny, czy normalny. Pamiętam jak w PZU było to mocno rozdzielone – faktury B2B (współpracownicy) trafiały nawet do innego sekretariatu (działu kadr), a nie do głównego. Cały proces był zdublowany, miał inne osoby do akceptacji i odrębne raportowanie.

**Damian Kamiński:** Dokładnie tak to wygląda. Często ścieżka poufna jest też uproszczona, bo zaangażowanych jest mniej osób. O to mi chodzi. Proces poufny byłby niedostępny dla administratorów (poza poziomem bazy danych, ale tego nie rozwikłamy). Jeśli nie macie lepszego pomysłu, to bym to tak zostawił.

**Janusz Bossak:** Potrzebujesz klasyfikatora, jeśli wszystko przychodzi jednym konektorem KSeF.

**Damian Kamiński:** Powtórzę: proponuję, aby KSeF Connector ładował faktury do procesu faktur tajnych. Tam reguła cykliczna sprawdza, czy NIP kontrahenta jest w puli kontrahentów tajnych. Jeśli nie – następuje "assign procedure" do procesu głównego.

**Janusz Bossak:** Bardzo dobrze.

**Kamil Dubaniowski:** Weź pod uwagę, że to nie zawsze kwestia kontrahenta. To się skomplikuje, gdy np. faktury wystawione na prezesa mają iść ścieżką tajną, żeby pracownicy nie widzieli kosztów delegacji.

**Damian Kamiński:** To już kwestia reguł.

**Janusz Bossak:** Można dopisać NIP prezesa do słownika.

**Damian Kamiński:** Kamilowi chodziło pewnie o koszty prezesa. Faktura i tak wpadnie do grupy księgowości, która wie najwięcej. To oni zdecydują na podstawie doświadczenia.

**Janusz Bossak:** Z KSeF-em jest więcej problemów. Przy papierze lub mailu wiadomo, kto przyniósł fakturę.

**Damian Kamiński:** Dlatego robimy ten projekt. Warto by było przygotować case study o tym, jak to opiekujemy. To dobry temat marketingowy – mamy matrycę, gdzie ścieżka faktur jest zarządzana na podstawie parametrów: kontrahenta, nazw pozycji czy informacji dodatkowych.

**Janusz Bossak:** Tutaj idealnie pasuje agent AI, który dostaje instrukcje.

**Damian Kamiński:** Tak, ale nie wszystkie duże firmy chcą wpuszczać agenta AI do takich danych.

Wracając do wątku: w nowych wdrożeniach (dostosowanych pod KSeF) nie ma problemu. W starych procesy mogą nie być kopiami. Omaiwałem to z Piotrem. Najprostszym progiem wejścia byłoby dodanie do `foreach Object` (gdzie obsługujemy XML) możliwości definiowania pola z plikiem jako źródła. Dzisiaj to nie działa. Mamy tam funkcje XPath, które źle działają (rozmawiałem o tym z Markiem), ale nie udało mi się ustalić, kto z tego korzysta.

**Piotr Buczkowski:** Pisałem do kogo to było zrobione.

**Damian Kamiński:** Pisałeś, że dla Deutsche Banku. Ale nikt nie wie, jak wygląda ich środowisko. Kamil, serwis, Tomek – nikt nie ma pełnej wiedzy o ich procesach. Nie mamy odtworzonego ich środowiska u nas. Poprosiłem Marka, żeby sprawdził czy używają tej funkcji, ale nie mam odpowiedzi. Pytanie, czy `foreach Object` w parametrze XML mógłby mieć zdefiniowane pole z plikiem?

**Piotr Buczkowski:** Tak, mógłby. Trzeba też poprawić funkcję XPath – powinna zwracać to, co wynika z XPath-a, a nie dzieci (children). Odczytywanie pliku nie spowoduje problemów ze zgodnością, ale zmiana zachowania funkcji XPath wymusi poprawki we wdrożeniu.

**Damian Kamiński:** To jest ryzyko. Powinniśmy zbierać dane analityczne, żeby wiedzieć, jakich funkcji używają klienci.

**Piotr Buczkowski:** W Deutsche Banku to było chyba do odczytywania wyciągów.

**Damian Kamiński:** Na razie poprosiłem Marka, żeby wyszukał w bazy danych jak klienci korzystają z tej funkcji.

**Janusz Bossak:** A propos gromadzenia informacji o klientach – w ramach usługi serwisowej u Daniela powinni mieć obowiązek pobierania definicji procesów. Nawet raz na kwartał. Mielibyśmy bazę wiedzy o tym, jak procesy są budowane i jakich funkcji używają. To nie jest tajemnica, skoro to serwisujemy. Interesują nas definicje, nie dane. To też dodatkowy backup dla klienta.

**Damian Kamiński:** Ryzykowne jest wygaszanie funkcji bez tej wiedzy. Jeśli wiemy, jak klient z tego korzysta, zmniejszamy ryzyko niekompatybilności lub możemy ostrzec o konieczności akcji serwisowej.

Podsumowując: Marek sprawdza zapytania. Zrobię zgłoszenie, żeby w `foreach Object` można było podać pole z plikiem.

**Piotr Buczkowski:** A XML w stringu?

**Damian Kamiński:** Problem polega na tym, że nie jesteśmy w stanie odczytać XML-a z pola innego niż tekstowe bez wycinania węzłów. Próbowałem pobrać content i wycina węzły XML-owe.

**Piotr Buczkowski:** Sprawdzę to. Być może warto pomyśleć o lepszym rozwiązaniu.

**Damian Kamiński:** OK, jeśli masz alternatywę, to daj znać w zgłoszeniu. Ja nie wymyśliłem, jak odczytać wartości z węzłami XML z pola pliku.

Kolejny temat: limit spraw. Dostałem ostatnio maila z innej instancji o osiągnięciu limitu. Pierwszy raz mi się to zdarzyło.

**Piotr Buczkowski:** Nikt nie potrafi tego rozwiązać. Być może wystarczy inaczej obsłużyć błąd odczytu licencji – zignorować go chwilowo zamiast wysyłać maila, że osiągnięto limit. System uznaje, że limit został osiągnięty, bo nie odczytał licencji z bazy.

**Janusz Bossak:** System powinien wysyłać komunikat dopiero, gdy błąd powtórzy się np. 3 razy, a nie przy pierwszym strzale.
