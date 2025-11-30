Data spotkania: 14 listopada 2025

**Damian Kaminski**: Dobrze, to w takim razie. Przede wszystkim, repozytorium jest to element systemu AMODIT. Sama struktura jest wielopoziomowa. Można ją budować, dodając kolejne podfoldery. Te najwyższe foldery, nomenklaturę przyjąłem, że nazywamy przestrzeniami, żeby można było je jakoś wyróżnić. To łatwo można zrobić po stronie frontendu, żeby przydzielać im jakąś inną ikonkę.

Możliwość tworzenia struktury wewnątrz, foldery zagnieżdżone – tutaj było ustalone wstępnie, że 20 poziomów. Możemy to w jakiś sposób ograniczyć, chociaż Piotr nie dał co do tego, wydaje mi się, uwarunkowań technicznych. Raczej wynikało to po prostu z kwestii ścieżki windowsowej. Foldery maksymalnie 2000 obiektów. Pliki przechowywane w dowolnej gałęzi, czyli albo w najwyższych folderach, albo w podfolderach.

Jeśli chodzi o obsługę plików, to w zakresie podglądów i wczytywania tych plików nie zmieniamy nic względem tego, jak to jest obecnie, łącznie z uploadem. Bazujemy na tych zasadach, które są w AMODIT na poziomie sprawy obsługiwane. I tutaj z racji, że będziemy to robić reactowo, zakładam, że nie będzie żadnego problemu, żeby wykorzystać to, co reactowo już zrobiliśmy jako podgląd dla raportów, bo to już powstało, zostało zaktualizowane. Mam nadzieję, że to jest już w zasadzie tylko przeniesienie komponentu w podstawowym zakresie.

Jeśli chodzi o uprawnienia, na ten moment ustaliliśmy sobie, że MVP1 to jest definicja uprawnień dla poziomu najwyższego, czyli dla tej przestrzeni. Wszystko reszta jest dziedziczona w dół. Nie istnieje możliwość przerywania dziedziczenia. Jeśli chodzi o typy uprawnień, to mamy:
-   **Pełny dostęp (administrator)**: odczyt, zapis, usuwanie, tworzenie struktury i nadawanie dostępów.
-   **Edycja**: odczyt, zapis, usuwanie **swoich** plików i folderów oraz tworzenie struktury.
-   **Odczyt**: tylko przeglądanie.

Administrator systemu dziedziczy uprawnienia administratora przestrzeni. Jest też inicjatorem pierwszej przestrzeni, bo nie zakładałem, że będzie czegoś takiego jak rola administratora repozytorium. Czyli to administrator systemu musi utworzyć przestrzeń i nadać w jej ramach uprawnienia administratora przestrzeni. I wtedy ten administrator przestrzeni może tym zarządzać. Dziedziczenie, tak jak opowiedziałem, od góry w dół.

**Janusz Bossak**: Mhm.

**Damian Kaminski**: Wyświetlanie uprawnień to już jest, bym powiedział, frontend. Jak już będziemy je mieli zaopiekowane, to de facto... będą przechowywane tak jak załączniki. Już mi się miesza z szablonami. Spojrzę na to, co Piotr pisał, żeby nic nie przekłamać. Moduł będzie częścią AMODIT. Należy dodać kolumnę. Pliki będą zapisywane zgodnie z konfiguracją dla załączników. OK, dobrze.

Przechowywanie w systemie plików podobnie jak dla załączników. Lokalizacja fizyczna – można skopiować to z opisu zapisywania na dysku. Identyfikacja pliku w interfejsie – do tego Piotr się nie odniósł, ale zakładam, że skoro przechowujemy to tak jak załączniki, to pewnie tak będzie. Tu można by Piotra dopytać. Szyfrowanie – zakładam, że skoro przechowujemy je tak samo, to będzie to natywnie, ale też nie wiem, to jest moje założenie.

**Janusz Bossak**: No dobra.

**Damian Kaminski**: Jeśli chodzi o metadane w bazie, to Piotr już to określił. Będą spójne z tym, co mamy dzisiaj. Pewnie trzeba będzie przejrzeć bazę danych przy spisywaniu tego.

Dalej interfejs użytkownika, czyli bardziej frontend. Nawigacja w formie drzewa, operacje na plikach: upload, usuwanie tylko swoich, usuwanie wszystkich przez administratora przestrzeni albo systemu. Przenoszenie plików między folderami – poza zakresem. Wersjonowanie – poza zakresem. Historia zmian – poza zakresem. Podgląd tak jak dzisiaj. Wyszukiwanie – do tego Piotr się nie odniósł. Zakładam, że tak jak rozmawialiśmy wcześniej, musi być do tego jakiś inny proces, np. Lucene. Ale to niekoniecznie musi być częścią pierwszego MVP, więc na potrzeby testów nie jest może niezbędne. I jeśli będzie, to zakładam, że tak jak w Lucene, czyli po nazwie i po treści. Cała reszta jest nieistotna. Tak to wysokopoziomowo wygląda.

**Janusz Bossak**: Dobrze, no to teraz trzeba to przenieść do backlogu i zacząć materializować w postaci naszych MVP i ficzerów, które mają wejść w którym MVP. To jest całkiem dobrze rozpracowane na takim ogólnym, wysokim poziomie.

**Damian Kaminski**: OK, tylko jak sugerujesz, według Twojej polityki, powinno być to podzielone? Pierwszy ficzer to powinna być struktura.

**Janusz Bossak**: Najpierw trzeba spisać ficzery, możemy to robić już na naszym backlogu. Zastanawiam się, w którą strukturę to wrzucić. Tematy związane z realizacją zobowiązań to jest jeden sposób zapisu, że to jest nasza inicjatywa.

**Damian Kaminski**: Masz na myśli inicjatywę? Przyznam szczerze, mi się to średnio podoba. Wolałbym, żeby inicjatywy... Inicjatywa z założenia ma być skończona.

**Janusz Bossak**: Nie, inicjatywa to jest raczej cel biznesowy, np. "skrócenie czasu wdrożeń o 30%".

**Damian Kaminski**: Czyli nie traktujemy jej jako coś rozliczalnego w kontekście statusu?

**Janusz Bossak**: Nie. Inicjatywa to jest wytyczna. Opracowałem sobie inicjatywę "wzrost satysfakcji użytkownika poprzez modernizację interfejsu" i cel biznesowy to "80% pozytywnych ocen w ankietach in-app". I mierzylibyśmy satysfakcję klienta z tego, że dostał nowy interfejs użytkownika, na przykład na sprawie. Moglibyśmy stwierdzić, czy osiągamy ten cel i czy podejmujemy działania, żeby podnieść ten wskaźnik. On może być obserwowany przez 2-3 lata.

Opracowałem też cel dla "zwiększenia stabilności modułu raportowego". AI podpowiedział, że cel to redukcja błędów w rozumieniu wskaźnika P1 do P2, czyli błędy krytyczne do błędów ważnych. P1 to jest, jak w ogóle wszystko się zatkało i nie można działać, a P2 to są błędy ważne, które uniemożliwiają jakąś pracę, ale istnieją jakieś obejścia. Chcemy zmniejszyć ten wskaźnik o 40%. Będziemy liczyć, ile jest błędów z modułu raportowego i stwierdzać, czy osiągamy wskaźnik. To jest poziom inicjatywy.

Teraz może być inicjatywa dotycząca monetyzacji. Robimy to repozytorium, bo klient na nas to wymusza, ale z drugiej strony to jest powód do monetyzacji tego. Takie repozytorium można by sprzedawać.

**Damian Kaminski**: Może nie mieszajmy już tych wątków, to jest wtórne.

**Janusz Bossak**: Tak.

**Damian Kaminski**: Próbujemy w narzędziu do zarządzania backlogiem ująć cele biznesowe, bardzo wysokopoziomowe. To, czy my to potrafimy ująć, zależy od nas i nie ma na nic wpływu. Pewnie w łatwy sposób można to też przepiąć. Mamy jeden epik, który przekleimy do innej inicjatywy, jak uznamy, że tak będzie lepiej. Te inicjatywy mają ten minus... Ja wiem, że to jest tu, ale wolałbym, żeby to był taki poziom jak... to, co ci pokazywałem. Łatwo jest poruszać się tu po drzewku. Wybierając tutaj, fajnie mogę się po tym poruszać, ale niestety nie ma tu tak wygodnych filtrów. To by definiowało, że w administracji mamy to i to, możemy uznać, że coś jest planowane, projektowane. Jeśli poruszamy się po inicjatywach, to za 5 lat będziemy ich mieli tyle, że ciężko się będzie odnaleźć.

**Janusz Bossak**: Nie, inicjatywy muszą być ograniczone i powiązane z naszą strategią. Skrócenie czasu wdrożenia o 30% to bardzo dobra inicjatywa. Powinniśmy mierzyć, czy skróciły się te wdrożenia o 30%. To pewien miernik biznesowy i ja się pod tym podpisuję. Ten poziom inicjatywy pomaga nam też w myśleniu, pod co to podpiąć. No właśnie, ten Comarch Hub, albo ten JR-Wa, albo teraz to repozytorium – pod co to podpiąć? Dlaczego my to robimy? To jest pytanie "dlaczego?".

Masz budżet pieniędzy w ręku, jesteś w sklepie, który ma dużo błyskotek, i musisz te pieniądze, czyli nasz czas, przeznaczyć na coś konkretnego. Nie masz kupować byle czego, co jest fajne, tylko to, po co cię żona wysłała. Miałeś kupić szafę, miałeś pieniądze na szafę i masz tę szafę przywieźć do domu. To jest nasz cel. Po to są te inicjatywy.

Obszar (Area) z kolei, i tu się podpisuję pod tym, co mówi AI, mówi o tym, w której części AMODIT będą wykonywane jakieś prace. Area na poziomie ficzera czy PBI może być inna. Możemy mieć ficzer w jednym obszarze, ale do tego MVP musimy zrobić zmiany np. w jobach, co jest innym obszarem AMODIT, i zmiany na frontendzie na sprawie, co jest jeszcze innym obszarem, ale ciągle dostarczamy jedną wartość.

AI ciągle mi to powtarza, żebym nie traktował tych MVP jako worka funkcjonalności. To są wartości, które dostarczasz. Zresztą MVP ma w nazwie "Value".

Na razie zrobiłem ogólny epik "Osiągnięcie nowego strumienia przychodów z modułów dodatkowych". Dla mnie repozytorium jest modułem dodatkowym. W ramach tego możemy zaraz utworzyć sobie MVP.

**Damian Kaminski**: Nie zrozumiałem, gdzie ty to zapisujesz.

**Janusz Bossak**: [Janusz pokazuje ekran] Na razie tu będziemy dodawali ficzery, czyli rzeczy, które ogólnie trzeba zrobić.

**Damian Kaminski**: Mhm.

**Janusz Bossak**: Co tam masz w tym pliku?

**Damian Kaminski**: Powiedziałbym, że wszystko to wrzucamy do epika, bo to jest opis wszystkiego.

**Janusz Bossak**: Można podejść dwojako. Albo w epiku dać tylko opis ogólny, a potem opisywać kolejne elementy, albo wrzucić wszystko, a potem kopiować i rozwijać na poziomie ficzera.

**Damian Kaminski**: Zarządzanie strukturą można to nazwać.

**Janusz Bossak**: Najpierw wypiszemy wszystkie ficzery. Na razie nie zastanawiamy się, czy to będzie w MVP 1. Jak wypiszemy ich 15-20, to zdecydujemy, które z nich zostają w MVP 1, a które idą do MVP 2. Kryterium jest to, że MVP 1 musi być zrobione w jeden sprint.

**Damian Kaminski**: Dzisiaj pan Piotr, co było do przewidzenia, nie był w tak dobrym humorze. Skomentował to tak, że "wy możecie sobie opisywać, a wymagania są zapisane w Service Request". Ale według mnie wymagania w SR sprowadzają się do dwóch zdań odnośnie repozytorium. Pytanie, kto jak interpretuje, co to jest repozytorium.

**Janusz Bossak**: No właśnie, niech też nie będzie niegrzeczny.

**Damian Kaminski**: Z komunikatorem powiedział, że dobrze, ale jak to jest na HTTP, to nie dotykamy. Nie wyświetlił się im, bo mają ustawione automatyczne przekierowanie, więc nawet oni na HTTP nie są w stanie się połączyć do testów. Napisałem już maila do pana Andrzeja po spotkaniu, żeby rozwiązać ten temat.

**Janusz Bossak**: To jest problem po ich stronie.

**Damian Kaminski**: Powiedziałbym, że wspólny, ale tak, oni muszą nam pomóc. Muszą nam wysłać certyfikaty do osadzenia lokalnie, bo oni je przechowują na gatewayu. Jak łączysz się z zewnątrz, certyfikat jest dokładany na poziomie bramki. Ale jak AMODIT i komunikator komunikują się lokalnie na jednym serwerze, to nie mają certyfikatów i to powoduje problemy.

**Janusz Bossak**: To jest problem tego, że tak to zostało wymyślone. Dlatego Piotr dla repozytorium bardziej sugeruje podejście, że to jest część AMODIT-a. Według mnie komunikator też powinien być częścią AMODIT-a.

**Damian Kaminski**: Jeśli chodzi o bazę danych, Mateusz powiedział, że może być jedna. Powiedziałem mu, żeby na razie zrobił tak, żeby działało, a najwyżej poprawimy i wyciągniemy wnioski. Zapytałem go o nazwy tabel, powiedział "dowolne". Mi się taka odpowiedź nie podoba, bo wiem, co Piotr na to powie. Muszą być odgórnie ustalone, żeby nie konfliktowały w przyszłości.

**Janusz Bossak**: Dokładnie. Wracamy tutaj. Z panem Piotrem wiadomo, jak jest, raz ma lepszy humor, raz gorszy. Musimy robić swoje.

**Damian Kaminski**: Dobrze, mamy te ficzery. Myślę, że możemy je od razu nazywać. Ja po prostu potem to pouzupełniam. Mamy strukturę, którą można zarządzać: dodawać węzły, usuwać węzły pod warunkiem, że są puste.

**Janusz Bossak**: To są przypadki użycia.

**Damian Kaminski**: No właśnie. Widziałbym to tak, jak proponowałeś: jest ficzer "zarządzanie strukturą", gdzie opisujemy, jak jest zbudowana, a potem mamy rozbicie na przypadki użycia, z których wynikają konkretne PBI.

**Janusz Bossak**: Tak, "zarządzanie strukturą folderów".

**Damian Kaminski**: Jak ty to widzisz? Bo ja tu cały czas mogę mieć jakieś niezrozumienie. Czy przypadek użycia to jest "dodanie nowego folderu"?

**Janusz Bossak**: Nie muszą być tak rozbijane. Może być przypadek użycia na wyższym poziomie, gdzie opisujemy, że będąc zalogowanym do repozytorium, mogę dodać nowy folder, usunąć pusty folder itd. To jest przypadek użycia "zarządzanie strukturą". Jeżeli są bardziej skomplikowane przypadki, np. związane z usuwaniem, to opisuję inny przypadek użycia.

**Damian Kaminski**: Pytam, bo chciałbym unikać takich jednowymiarowych ścieżek, gdzie tworzymy dwa przypadki użycia i oba mają po jednym PBI. Wtedy mogę pominąć przypadki użycia i stworzyć od razu PBI.

**Janusz Bossak**: Pewnie tak. Chodzi o to, że np. w JR-Wa masz przypadek użycia "klasyfikacja pisma, które wpłynęło". To jest ficzer. I masz przypadki użycia: pismo, które nie tworzy akt sprawy, pismo, które trzeba zaklasyfikować do istniejącej teczki, i pismo, dla którego trzeba utworzyć nową teczkę. Przypadek tworzenia nowej teczki może mieć 15 PBI, bo muszę sprawdzić uprawnienia, daty, skopiować klasyfikację archiwalną itd. To jest ten poziom.

**Damian Kaminski**: Czyli teraz, czy tego nie skorygować? Można napisać ficzer "zarządzanie strukturą" i z tego będą dwa PBI, albo zrobić ficzer "struktura folderów" i z tego use case "zarządzanie" i use case "przeglądanie". I dla przeglądania dać wytyczne, że domyślnie wyświetlają się tylko przestrzenie, a przy kolejnym wejściu zapamiętuje ostatnio rozwinięte węzły.

**Janusz Bossak**: Dobrze, bardzo dobrze. Możemy patrzeć na to od strony dokumentacyjnej, jakbyśmy pisali instrukcję. Jedną z instrukcji byłoby "przeglądanie struktury folderów". I tu mogą być use case'y, np. "wyszukiwanie folderu", "wyszukiwanie pliku".

**Damian Kaminski**: To jest akurat rzecz, której nie miałem w głowie, trzeba to ustalić. Wyszukiwanie plików ma zadanie z gwiazdką.

**Janusz Bossak**: Coś jeszcze do przeglądania struktury ci się kojarzy?

**Damian Kaminski**: Kojarzy mi się po prostu przeglądanie, czyli opisanie, jak to działa, jaki jest domyślny widok, czy zapamiętuje stan itd. Czy mogę stworzyć PBI bezpośrednio z ficzera "przeglądanie" oraz osobne PBI z use case'ów podpiętych pod ten ficzer?

**Janusz Bossak**: Gdzie teraz spisać wytyczne co do standardowego wyglądu struktury, zapamiętywania stanu w local storage? Można to zrobić jako osobny ficzer, np. "Drzewo folderów".

**Damian Kaminski**: Czyli niezależnie od przeglądania?

**Janusz Bossak**: Tak. Może być ficzer "Sposób przechowywania folderów i dokumentów (tak jak dla załączników)". To jest ten techniczny ficzer, który opisuje pomysł Piotra, jak to będzie przechowywane. Potem "Opracowanie endpointów". Potem "Zapewnienie wyświetlania hierarchicznego drzewa folderów uwzględniającego uprawnienia". To ostatnie to w zasadzie to, co mamy zrobione na frontendzie.

**Damian Kaminski**: Ale ja bym tu dopisał backend. Sposób przechowywania to czysty kod, stałe zasady. A drzewo folderów – po stronie frontendu mamy, a po stronie backendu to jest tabela, która opisuje folder, nazwę, nadrzędnik.

**Janusz Bossak**: Ale trzeba to zrobić.

**Damian Kaminski**: Z tego można zrobić zadanie i frontendowe, i backendowe. Zapewnienie wyświetlania to jedno, ale żeby to zrobić, musi istnieć tabela, muszą być endpointy GET. Czyli 3-4 PBI.

**Janusz Bossak**: Nie schodziłbym w tej chwili na poziom PBI. Niech deweloperzy to rozpiszą.

**Damian Kaminski**: Obawiam się tego, ale OK, można spróbować.

**Janusz Bossak**: Nie wiem, czy jesteśmy na tyle kompetentni, żeby ustalać, jakie endpointy mają być. Możemy napisać na tym poziomie "zapewnienie współpracy frontendu z backendem". Nie naszą rolą jest pisanie, jaki endpoint ma być.

**Damian Kaminski**: Ale walidacja tego... To jest przejście z analizy biznesowej do systemowej.

**Janusz Bossak**: Dokładnie, to jest ten krok.

**Damian Kaminski**: Czyli robię PBI i piszę "proszę opisać endpointy i wycenić effort"? A wymagania biznesowe są poziom wyżej, na poziomie ficzera?

**Janusz Bossak**: Trzeba ich wziąć na spotkanie i powiedzieć: "Słuchajcie, co według was jest do zrobienia, żeby zadziałało wyświetlanie tego, co jest tu zrobione?".

**Damian Kaminski**: Zgadzam się z tobą, ale mam tę samą rozterkę, co ty wczoraj. Przechodzisz od funkcjonalnych ficzerów, jak "drzewo folderów", do podziału na obszary: tu backend, tu endpointy, tu frontend. Co w takim razie ująć w ficzerze "drzewo folderów"?

**Janusz Bossak**: W tym podświetlonym, według mnie, jest to, co mamy gotowe, czyli tylko front.

**Damian Kaminski**: OK. Można to tak przedstawić: najpierw zbudujcie całą bazę i wszystko, a potem, jak się okaże, że czegoś brakuje, to w ramach pojedynczego ficzera "drzewo folderów" stworzymy dodatkowe PBI, bo nie przewidzieliśmy czegoś na początku.

**Janusz Bossak**: Przesunąłem to wyżej, bo biznesowo będzie to potrzebne jako pierwsze: "Wyświetlanie i poruszanie się po drzewie folderów". Mamy już poruszanie się po drzewie folderów, czyli rozwijanie, zwijanie. Może nie będziemy robić w pierwszej iteracji wyszukiwania folderów i plików.

**Damian Kaminski**: Wiesz, tu można łatwo skopać projekt. Skopaliśmy w kontekście Orlenu. Jest drzewo struktury i ktoś wymyślił, że załaduje od razu wszystko. Ale nikt nie pomyślał, że to drzewo może mieć 10 000 elementów. Zanim to się zbuduje, użytkownik czeka 30 sekund.

**Janusz Bossak**: I to właśnie w tym use case'ie mogłoby być napisane.

**Damian Kaminski**: Tu trzeba napisać, że poruszanie się oznacza wyświetlenie tylko najwyższych węzłów, albo najwyższych i ostatnio rozwiniętych, żeby zbudować widok maksymalnie 100 pozycji, a nie 10 000.

**Janusz Bossak**: Dobrze. Napiszemy "poruszanie się po drzewie folderów, które może mieć 1000 pozycji". To jest przypadek, który trzeba uwzględnić, np. lazy loading. Jak to napiszemy, jest duża szansa, że deweloper też o tym pomyśli.

**Damian Kaminski**: W strukturze najprostsze jest to, że jak ktoś wchodzi, wyświetlamy górne wiersze (przestrzenie) i nie wiemy, co jest wewnątrz. Dopiero jak klika strzałkę "rozwiń", idzie zapytanie "podaj mi potomków tego".

**Janusz Bossak**: Dobrze. Co jeszcze mieliśmy?

**Damian Kaminski**: Omawialiśmy na razie tylko środkową kolumnę, a trzeba jeszcze omówić obszar roboczy.

**Janusz Bossak**: To jest już w AMODIT zrobione.

**Damian Kaminski**: Tak. I tutaj, na tym obszarze roboczym, jak najbardziej lazy loading musi być zastosowany. I kto widzi przyciski "Dodaj plik", "Nowy folder"? Tylko ci, co mają uprawnienia edycji albo są administratorami.

**Janusz Bossak**: A to są przypadki użycia.

**Damian Kaminski**: No właśnie. I teraz pytanie, czy tego nie łączyć. Jak to połączymy, ten ficzer będzie bardzo duży. Jakbyśmy się skupili na ficzerze w kontekście tylko struktury, to jeśli struktura się buduje i wyświetla zgodnie z uprawnieniami, to mamy strukturę zamkniętą. To, że w obszarze roboczym wyświetla się to, co wynika z folderu, na którym jesteśmy, to już jest wtórne.

**Janusz Bossak**: Dobrze, możesz ty przejąć i pisać tutaj to, co ja piszę, a potem możemy zrobić test za pomocą AI, czy on to uznaje za właściwy ficzer, czy za duży, za mały.

**Damian Kaminski**: Jak to zrobisz?

**Janusz Bossak**: Mogę go po prostu zapytać. [Janusz pokazuje rozmowę z AI]. On ma tę wiedzę, którą wypracowałem: przewodnik klasyfikacji, opis paczki wartości. Jak masz wątpliwość, jak coś nazwać, on ci podpowiada. Działa w trybie strażnika zasad.

**Damian Kaminski**: Dobra, wszystko wiem, działam. Dam znać, jak skończę.

**Janusz Bossak**: Daj znać, jak dasz radę dzisiaj.

**Damian Kaminski**: Dzisiaj będę pracował do 16:30. Zamierzam jutro i pojutrze jeszcze coś pozaglądać, bo w WIM też trzeba nadgonić. Chcę mieć to na poniedziałek rozpisane przynajmniej do pełnej walidacji przez ciebie.

**Janusz Bossak**: Dobrze, będę zaglądał. Miłego weekendu.

**Damian Kaminski**: Będę pisał. Hejka.