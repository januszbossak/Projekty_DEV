**Data spotkania:** 31 października 2025

---

**Damian Kaminski:** Mam takie przemyślenie, że nie mam na tyle wiedzy technicznej, żeby dobrze zaprojektować backend dla repozytorium plików i tutaj potrzebujemy równorzędnego partnera. Chciałbym ustalić, jak do tego podejść. Kamil, jak ty to robisz? Chociaż teraz pewnie bardziej poprawiamy, niż tworzymy coś nowego.

**Kamil Dubaniowski:** Przy edytorze Reactowym było sporo nowego, ale ja działam na takiej zasadzie, że daję temat Przemkowi czy Filipowi. Głównie Przemek robił pierwowzór, a Filip na przykład po nim miał przejąć, więc Przemek był wiodący i on ustalał z Piotrem, co trzeba po stronie backendu.

**Damian Kaminski:** Dalej bym powiedział, że to jest odtwórcze. Mamy backend w kontekście struktury danych, ale brakuje funkcjonalności odczytu i zapisu. Mówię tu o samej strukturze, czyli jakie tabele powinny być definiowane w ramach repozytorium. Nawet coś tutaj już zaproponowałem na poziomie tabel, ale nie chcę wchodzić w szczegóły, jakie mają mieć kolumny, klucze i relacje, bo to nie moje zadanie. Pytanie, czy do tego przypisujemy Piotra, czy innego dewelopera? Z Mateuszem mam taki problem, że nie jest dostępny wystarczająco dużo czasu i pytanie, czy z nim zdążymy i zaprojektować, i zrobić? Czy raczej potrzebne jest wsparcie kogoś innego, kto ustali architekturę, a Mateusz będzie bardziej wykonawcą?

**Janusz Bossak:** Mateusz ma tu pewne ryzyko, ale myślę, że powinien się mocno zaangażować. Nawet po godzinach, jak mu powiemy, żeby robił, to będzie robił, bo i tak rozlicza się godzinowo.

**Damian Kaminski:** Sugerujesz, żeby powiedzieć Mateuszowi, aby to przeanalizował, dał uwagi i przygotował, jak powinno być? Czy ktoś ma to po nim weryfikować?

**Janusz Bossak:** Co do backendu i architektury, mam największe zaufanie do Piotra. Wolałbym, żeby Piotr przynajmniej wyznaczył ramy, że robimy to w określony sposób, a resztę niech sobie Mateusz czy ktoś inny kombinuje, np. endpointy. Chodzi mi o to, żeby Piotr zajął się architekturą – jak to ma być zrobione, jaka komunikacja z użytkownikami, jak zapisywanie w folderach. Fundamenty, konstrukcja, a na tych założeniach Mateusz ma opracować backend.

**Damian Kaminski:** W ramach tego repozytorium zrobiłem cały backend, tu są główne wytyczne i z tego wynikają PBI, na przykład struktura danych i model bazodanowy. Wymieniłem, jakie te tabele mogą być.

**Janusz Bossak:** Z całym szacunkiem do Twojej wiedzy, ale to już jest za duży poziom szczegółowości. Ty jesteś od biznesu. Twój poziom to wymagania: chcę mieć strukturę folderową, uprawnienia działające tak i tak, przenoszenie, itp. To jest Twój poziom przypadków użycia.

**Damian Kaminski:** Czy ten poziom szczegółowości ma być tu opisany? Nie muszę w niego wchodzić, ale czy mam poprosić Piotra, żeby wypisał, jakie mają być tabele i kolumny?

**Janusz Bossak:** Tak. Na podstawie założeń ilościowych, co do liczby poziomów czy wielkości pliku, deweloperzy mają zaprojektować i zaproponować strukturę danych. To jest jedno zadanie. Drugie, może nawet wcześniejsze, to zaproponowanie architektury aplikacji. Czy to jest odrębna aplikacja, jaka komunikacja z systemem AMODIT? To jest ten poziom. Z architektury aplikacji będzie wynikać architektura bazy danych. Jeżeli w architekturze aplikacji zapiszemy, że to jest część AMODIT, to pewnie struktura będzie inna, tabele będą w AMODIT. A jeśli to odrębna aplikacja, to struktura będzie inna. Trzeba rozkminić na przykład to, co było w komunikatorze: czy użytkownicy są kopiowani? To jest pewien ból. Brakuje opisu architektury komunikatora, jak to jest zrobione.

**Damian Kaminski:** Nie odpowiem ci, nie chcę zmyślać.

**Janusz Bossak:** I to jest poziom, który potrzebujemy tutaj, a to mają rozkminić deweloperzy, w szczególności Piotr jako architekt systemowy. To jego zadanie: wymyślać architekturę systemu i pilnować jej spójności. Jak on tę architekturę zapoda, to następnym zadaniem dewelopera jest zaproponowanie, jak to zaimplementuje, co powinno podlegać weryfikacji Piotra. Ty dajesz ogólne założenia i wymagania biznesowe.

**Damian Kaminski:** Czuję, że nie pracowaliśmy tak do tej pory. Piotr to bierze i mówi: "wiem w głowie, jak to trzeba zrobić" i to robi.

**Janusz Bossak:** On ma to wiedzieć, ale ma to napisać. Uczmy Piotra jednej rzeczy: żeby włączał mikrofon i gadał. Wiem, że ma problem z wysławianiem się, szybciej myśli niż mówi, ale niech opowiada. Jak nie potrafi mówić do głuchego telefonu, to niech któryś z was tam będzie i go podpytuje. Z tego powstanie piękny opis architektury.

**Damian Kaminski:** OK, czyli zrobić z nim spotkanie i omówić punkt po punkcie, co trzeba zrobić w ramach PBI?

**Janusz Bossak:** To jest najszybsze. Jak mu powiesz, że ma to zrobić, to powie, że nie ma czasu. A jak go weźmiesz i powiesz "potrzebuję z tobą 30 minut, omówimy architekturę", to powstanie jakaś wersja pierwsza, którą uporządkujesz. Nagrywasz spotkanie, przechodzisz przez transkrypcję i uzupełniacie. Z czasem nauczymy się, jak rozmawiać i odpytywać Piotra o architekturę, bo to są powtarzalne tematy: uprawnienia, użytkownicy, komunikacja z AMODIT, przechowywanie plików, mikroserwisy.

**Damian Kaminski:** Dobra, to poproszę go, żebyśmy się dzisiaj spotkali. Wracając do planu, co proponuje Kamil?

**Kamil Dubaniowski:** Wyszedłbym od tego, że niektórzy w planie są już przeładowani, na przykład Adrian, który ma KSeF, macOS i Comarch Hub. Nierealne jest w 8 dni nawet minimalne MVP z tego złożyć.

**Damian Kaminski:** Zgadzam się. To samo chciałbym zrobić z Adrianem, co z Piotrem. Chcę z nim rozpisać, co jest do zrobienia, żeby nie "doktoryzował" się z konektora KSeF, tylko okroił to do tego, czego faktycznie potrzebujemy biznesowo.

**Janusz Bossak:** Pytać, nagrywać zeznania, zbierać. Jesteśmy jak prokuratura.

**Damian Kaminski:** Dokładnie. Wracając do roadmapy, chciałbym w tym sprincie skończyć komunikator, rozpisać repozytorium i zająć się macOS i KSeF.

**Kamil Dubaniowski:** Ale to nie angażuje deweloperów.

**Damian Kaminski:** Angażuje Mateusza, który ma pracę i przy komunikatorze, i przy repozytorium. Tu widzę konflikt. Obawiam się, że Mateusza nie starczy. Z drugiej strony nie ma co zakładać, że repozytorium wyprodukujemy w jeden sprint.

**Kamil Dubaniowski:** Co chcemy osiągnąć w tym sprincie w kontekście repozytorium?

**Janusz Bossak:** Mamy trochę wyprzedzenie, bo Filip już trochę frontendu zrobił. Zróbmy jakiś element backendowy. Myślę, że jeżeli po 8 dniach będziemy mieli naprawdę rozkminioną architekturę i strukturę backendu, to będzie duży wkład. Wolałbym nie dawać jeszcze do robienia w rozumieniu pisania kodu, tylko niech się zastanowią porządnie.

**Damian Kaminski:** Rozpisanie.

**Janusz Bossak:** Jakie endpointy będą, do czego. Mają już ten frontend, więc z Filipem można porozmawiać, w którym miejscu potrzebuje jakich danych. Niech to wszystko rozkminią i spróbują zrobić tak, jak powinno się to robić, podręcznikowo.

**Damian Kaminski:** Dobrze. A czy my to jakoś spisujemy? Czym się zajmujemy w tym sprincie na wysokim poziomie?

**Kamil Dubaniowski:** Robiłbym to w perspektywie na ludzi, bo wtedy będzie widać, kto jest obłożony. Na przykład nie mam żadnego sprecyzowanego celu dla Łukasza Brockiego. I pytanie: czy ten Comarch Hub musi robić Adrian?

**Damian Kaminski:** To dobre pytanie. Odpalę Excela i zróbmy to na wysokim poziomie.

**Kamil Dubaniowski:** Damian bierzesz na siebie macOS?

**Damian Kaminski:** Mogę, ale uważam, że skoro ty masz projekt, Maca i Szafira do testów, to powinno być u ciebie. Ja będę tylko pośredniczył w przekazaniu do testów dla klienta. Niezależnie od certyfikacji, powinniśmy im to dać do sprawdzenia.

**Kamil Dubaniowski:** Dobrze, ja to miałem w planie.

**Damian Kaminski:** Zostaje kwestia JRWA.

**Janusz Bossak:** Ja to rozpracowuję.

**Damian Kaminski:** Czyli tobie Janusz przypisać, że ustalisz, czy coś robimy?

**Janusz Bossak:** Tak. To jest coraz trudniejsze. Dziś rano pomyślałem o jeszcze jednym problemie. Okazuje się, że nie jest tak, że każdy widzi całe JRWA. Nakłada się matryca kompetencji.

**Damian Kaminski:** Wynikająca ze struktury organizacji.

**Janusz Bossak:** Dokładnie. To jest obowiązek wynikający z rozporządzenia. Zgodnie z ochroną danych osobowych, ludzie powinni mieć dostęp do tej części JRWA, która ich dotyczy. Księgowy nie może sobie założyć teczki w radzie nadzorczej.

**Damian Kaminski:** To jest to, o co Kamil oparł uprawnienia w repozytorium – przypisanie do działów.

**Kamil Dubaniowski:** Miałem przesłanki, żeby to tak działało, chociaż nie podobało mi się, że to jest per dział.

**Damian Kaminski:** Dobra, Kamil, co poza tym widzisz na ten sprint?

**Kamil Dubaniowski:** Jest fala zgłoszeń odnośnie wzmianek. To kompletnie nie działa, jak powinno. Mam w planie na Mariusza wzmianki, i jest tego na tyle dużo, że najlepiej zrobić to od nowa. Szacuję, że to 60% jego sprintu, więc to jedyny cel, jaki powinien mieć.

**Janusz Bossak:** Dokładnie. To jest zadanie dla niego i on ma to dowieźć. Po tym sprincie to ma działać i temat ma być rozwiązany, stabilny. Najlepiej, jakby były do tego napisane testy end-to-end.

**Kamil Dubaniowski:** Dla Adriana miałem SignApp, to już jest rozpisane. Dla Przemka, jako że nie widzę dla niego ważniejszych tematów, chciałbym zamknąć temat 4-eyes w ustawieniach systemowych, odtwarzając to, co było. Będzie potrzebny backend.

**Damian Kaminski:** A kto to zrobi?

**Kamil Dubaniowski:** Patrząc, kto będzie wolny, może Ania albo Łukasz. Ania i Łukasz na razie nie są zaopiekowani.

**Damian Kaminski:** Dajmy Ani.

**Kamil Dubaniowski:** Łukasza widziałbym w tym Comarch Hubie. Co do Ani, chciałbym jej dać jedno z zadań Mariusza. Było tam szacowane na 15 MD, więc może stanowić cel, a jest istotną zmianą: podgląd szablonów, bo teraz w Neuca ładują do każdej sprawy ten sam plik jako załącznik, co generuje tysiące duplikatów.

**Damian Kaminski:** Tak, dziesiątki tysięcy. To jest totalny bezsens.

**Janusz Bossak:** Czekajcie, to ciekawy wątek. Mając repozytorium plików takie jak w Zimbrze, klient umieściłby tam taki dokument i tu byśmy go linkowali. Ale czy to zgodne z filozofią AMODIT? Nie bardzo. AMODIT jest procesowy. Taki dokument powinien być wrzucony jako tekst w panelu pomocy dla danej procedury.

**Damian Kaminski:** Ale jeśli są grafiki?

**Janusz Bossak:** Podgląd szablonów to dobry pomysł. Jest dużo przypadków, gdzie trzeba pokazać dokument, a nie go wypełniać.

**Damian Kaminski:** Powinno być "oczko" do podglądu. Albo pobierasz, albo podglądasz.

**Janusz Bossak:** My nie robimy podglądów dla dokumentów, bo one powstają jako np. JPG. Piotr chce w repozytorium wykorzystać GdPicture, który generuje podgląd w locie, ale to jest zasobożerne.

**Damian Kaminski:** Stworzenie podglądu szablonu jako JPG mogłoby być zasadne, bo szablonów jest mniej niż plików w repozytorium. Ale to wtórne. Możemy zrobić, że ktoś klika i generuje w tym momencie.

**Janusz Bossak:** Powinniśmy zdefiniować problem biznesowy. Klienci mają pulę stałych dokumentów (instrukcje, regulaminy), które chcą wyświetlać na sprawach bez ich multiplikowania. To jest problem do rozwiązania.

**Damian Kaminski:** Patrząc szeroko, mamy dwa aspekty. Jeden to dokument do zapoznania się, stały regulamin – do tego mogłoby być repozytorium. Inny aspekt to podgląd szablonu (np. umowa), gdzie po nazwie nie wiem, którą wersję zastosować. Podgląd pozwoli mi wybrać właściwy szablon, zanim go wyprodukuję.

**Kamil Dubaniowski:** Na razie podgląd szablonów tak, żeby zaopiekować ten problem. Ania backend i frontend. Dla Przemka mam diagram, ale nie wiem, czy chcemy coś z tym robić.

**Janusz Bossak:** Diagram na razie spada na niższy priorytet. MVP jest.

**Damian Kaminski:** A co Przemek ma robić?

**Kamil Dubaniowski:** Może zająć się dalszymi usprawnieniami edytora formularza. Mam kilka pomysłów: szukanie po typie, zapamiętywanie ostatniej zakładki (temat Daniela), zmiana ścieżki dodawania nowego pola.

**Janusz Bossak:** Lepiej zostawić diagram tak, jak jest, i włączyć go do AMODIT, a skupić się na super dopracowaniu edytora formularza, żeby konsultanci się na niego przenieśli. Ja wczoraj w 50% przypadków przełączałem się na listę.

**Damian Kaminski:** Ale czy my wiemy, czego brakuje w edytorze formularza? Trzeba te zadania wytyczyć.

**Kamil Dubaniowski:** Myślę, że dałbym na ten sprint cel: poprawa UX edytora formularza. Tam jest dużo do zrobienia.

**Damian Kaminski:** Trzeba słuchać problemów, które zgłaszają nowi użytkownicy, jak Daniel, a niekoniecznie ich propozycji rozwiązań.

**Kamil Dubaniowski:** Diagram na razie zostawiamy. A co z listą pól?

**Damian Kaminski:** Kto ją opiekuje?

**Kamil Dubaniowski:** Filip. Tam jest sporo braków względem starej wersji. Nie ma szybkiego odnośnika do słownika, nie ma ustawień pola. To jest naprawdę poziom MVP.

**Damian Kaminski:** A przenoszenie wielu pól do innej sekcji? Wczoraj Janusz rzucił pomysł, żeby zaznaczać pola z Controlem i je przeciągać.

**Kamil Dubaniowski:** Na razie przenosimy pojedynczo. Akcje masowe, jak usuwanie czy przenoszenie między sekcjami, mam zapisane. Drag and drop przy wielu elementach i długim formularzu będzie słaby.

**Damian Kaminski:** Zgadzam się. Może po zaznaczeniu kilku pól zmieniałby się prawy sidebar i tam pojawiałoby się menu kontekstowe z opcją "przenieś do sekcji"?

**Janusz Bossak:** Trzeba zaopiekować wszystkie problemy, które są. Piotr napisał, że brak obsługi błędów przy edycji pól – zdublował nazwę, zmiana się nie zapisała i nie było informacji o błędzie. To ten sam problem co u Przemka, gdy dodawał pole, a nie było już miejsca. Wgrajmy nowsze wersje, Przemek ma już pewnie taką bez tych linii.

**Kamil Dubaniowski:** Decyzja: błędy i niedoróbki lecą do wersji czerwcowej. Zmiany koncepcji – do nowszych.

**Damian Kaminski:** Dla Przemka jest formularz, sporo pracy.

**Kamil Dubaniowski:** Mam dla Filipa matrycę uprawnień. Tam cały czas jest kwestia czytelności. Chciałbym to zaopiekować w przyszłym sprincie. Miejmy na uwadze, że ten sprint zamyka paczkę grudniową, więc powinniśmy stabilizować wersję, a nie dorzucać nowe rzeczy.

**Damian Kaminski:** Dobra. Został Łukasz i Ania, którzy są niedoszacowani.

**Kamil Dubaniowski:** Adrian ma dużo, Filip jest zamknięty, Marek też, Mariusz ma wzmianki, Mateusz komunikator i projekt repozytorium, Piotr ma swoje zadania, Przemek ma edytor. Łukasz nie jest opakowany.

**Janusz Bossak:** A Comarch Hub?

**Kamil Dubaniowski:** Jest u Adriana.

**Janusz Bossak:** A te poprawki w e-Nadawcy, które ma Adrian, może przejąć Łukasz? Ktoś musi się też nauczyć e-Doręczeń.

**Damian Kaminski:** Comarch Hub to nowy temat. Adrian go rozkminia na poziomie koncepcyjnym. Może przekaże to Łukaszowi. Na razie jednak Łukasz jest na urlopie. Musimy poczekać do poniedziałku.

**Kamil Dubaniowski:** Dobra, czyli wrócimy, żeby zaopiekować Łukasza i zamknąć plan.

**Damian Kaminski:** Zróbmy 5 minut przerwy. Spotykamy się 9:40 i mamy jeszcze 20 minut.

*(po przerwie)*

**Janusz Bossak:** Te nasze spotkania są coraz bardziej konstruktywne. Brakuje mi tylko jednego miejsca do przechowywania i edycji dokumentacji projektowej, żebyśmy wszyscy mieli do tego dostęp.

**Damian Kaminski:** Zaproponowaliśmy rozwiązanie na kanałach w Teams.

**Janusz Bossak:** Właśnie. Tam w repozytorium plików jest opis MVP1. Powinna teraz powstać rozmowa z Piotrem i spisanie architektury.

**Damian Kaminski:** Mamy trzy potencjalne przestrzenie: Teams, backlog i Wiki ażurowe. Myślę, że one się uzupełniają.

**Janusz Bossak:** Projekt minimalnie składa się z trzech plików: 1. Uzasadnienie biznesowe (po co, dlaczego, dla kogo). 2. Rozbicie na MVP (sekwencja dostarczania, przypadki użycia). 3. Plik architektoniczno-techniczny (technologia, komunikacja, aktualne ustalenia). Chciałbym do takich plików zaglądać.

**Damian Kaminski:** Chcesz mieć stan obecny projektu, a historyczne zmiany zapisywać jako stan na dany dzień?

**Janusz Bossak:** Nie do końca. W stanie zerowym mamy pomysł na MVP. Ten plik będzie ewoluował.
