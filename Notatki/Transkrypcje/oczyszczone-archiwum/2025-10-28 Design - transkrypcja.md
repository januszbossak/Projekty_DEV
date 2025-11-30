**Data spotkania:** 28 października 2025, 11:47

---

**Damian Kamiński:** Pewnie tak, jeśli przyjmiemy założenie, że nie będą to sprawy.

**Janusz Bossak:** Tak.

**Damian Kamiński:** No więc to jest decyzja, którą musimy po prostu podjąć na najwyższym poziomie. Czy to będą odrębne byty, czy to będzie jeden byt? Natomiast teraz dalej. Przestrzenie – to najwyższy poziom organizacji repozytorium. Tu raczej chodzi o kwestię nomenklatury. To jest jakaś pierwsza moja propozycja, żeby rozróżniać łatwo, co jest tym najwyższym bytem, żeby nie stosować – to, co zasugerował pan Piotr, czyli obszarów, bo obszary, słowo „obszary" mamy już przypisane do innej funkcjonalności w AMODIT, więc ja zaproponowałem przestrzenie. Możemy to określić dowolnie. Można definiować dowolną liczbę przestrzeni. Każda przestrzeń może zawierać foldery i pliki. Jeśli chodzi o foldery – możliwość tworzenia struktury folderów wewnątrz przestrzeni, foldery mogą być zagnieżdżone do ustalenia. Maksymalna głębokość zagnieżdżenia, ograniczenia Windows – i to było jedno z wyzwań. Zaraz przejdziemy, jakie tu są propozycje, w związku z tym, co tu jest do ustalenia. Pliki przechowywane wewnątrz folderów – i różne pliki. Tutaj zakładam, że to będzie jakaś spójność z tym, jakie pliki są dozwolone w AMODIT, a jakie nie. System jest oparty na dziedziczeniu – możliwość przerwania dziedziczenia na każdym poziomie, zarówno przestrzeń – to akurat jest to niepoprawne – przyjęte na poziomie folderu lub też pliku. Gdy dziedziczenie jest przerwane, wyświetlana jest specjalna ikona ludzików. Na ten moment po prostu jest to jakaś ikona, która informuje zarówno administratora systemu, jak i administratora przestrzeni na poziomie drzewka, jakie na poziomie tej przestrzeni roboczej, czyli listy folderów. Nie wiem, czy mam pokazywać ci w międzyczasie projekt, czy wszystko to, co mówię, to kojarzysz z tym projektem, czy nie, bo możesz nie kojarzyć.

**Janusz Bossak:** Nie, coś pamiętam.

**Damian Kamiński:** Coś pamiętasz, mogę w razie co od razu odpalić, żeby to móc się szybko przełączyć? Więc tu chodzi tylko o to, żeby usprawnić pracę zmian uprawnień w ramach drzewa. To, co przed chwilą powiedziałem, czyli będąc jakimś administratorem na poziomie drzewka, już widzimy, że zmieniając uprawnienia, dlatego tu się nic nie zmieni, bo tu jest przerwanie. Oczywiście, jeśli wejdziemy, tu taki sam ludzik jest, żeby to też było z tego poziomu widoczne, że jeśli zmienimy uprawnienia dla tego folderu, w którym jesteśmy. To one nie będą się propagować dla tego folderu, więc tu chodzi o pewne usprawnienie widoków. Dobrze, idźmy w takim razie dalej. Typy uprawnień – to jest podstawowe – odczyt, zapis, modyfikacja, usuwanie. To może nie jest precyzyjnie opisane, one są zdefiniowane na poziomie przypisywania uprawnień, czyli możemy. Może pokażę to na najwyższym szczeblu. Możemy te uprawnienia dawać jako administrator obszaru. Pełne dodawać. Pełne dodawanie – to dodawanie, usuwanie dowolnych – to znaczy, że można ustawiać flagę nieusuwalności, dodawanie i usuwanie tylko tych, które nie są ograniczone i po prostu odczyt. Pytanie, czy usuwanie ewentualnie nie powinniśmy rozdzielać jako możliwość dodawania, niekoniecznie usuwania, i też widoczność folderu, przy czym widoczność folderu to jest uprawnienie wynikowe, a nie definiowane, to znaczy, że ono nie powinno być na tej liście. To jest akurat moje niedopatrzenie, muszę to poprawić. Ono jest wynikowe. Co to oznacza? To oznacza, że jeśli mamy na jakimś poziomie przypisane uprawnienia konkretnej osobie do danego pliku. Jak tutaj wskażą? Jana Nowaka. I ten Jan Nowak ma odczyt tego dokumentu w folderze API Documentation, to teraz tutaj. Może niefortunnie ten Jan Nowak jest akurat w grupie. Czy ja nie zapisałem tego? Jeszcze raz – Jan Nowak, odczyt dokumentu. Zapisz. OK. To teraz wynikowym uprawnieniem dla folderu API Documentation jest po prostu to, że on ma widoczność folderu po to, żeby jak Jan wejdzie do systemu, to będzie widział Dokumentacja projektu Alfa, Dokumentacja techniczna, API Documentation i ten konkretny plik. Natomiast właśnie w tych wyższych po prostu ma dziedziczone w górę, jakby uprawnienia wynikające z tego, że musi jakoś dojść do tego pliku. Więc widzi całe drzewko.

**Janusz Bossak:** Mhm.

**Damian Kamiński:** Dobrze, już kontynuujemy. Do ustalenia, czy ma sens nadawanie samej widoczności folderów. No to to już właśnie wtedy Piotrowi to samo powiedziałem. Dziedziczenie uprawnień – domyślne uprawnienia są dziedziczone z węzła nadrzędnego – przestrzeń, folder, podfolder, plik. Przerywanie dziedziczenia – zaznaczenie checkbox przerywa i tam jest akurat switch. No ale to jest to samo – przerwij dziedziczenie uprawnień. Uprawnienia na poziomie plików – możliwość zerwania dziedziczenia dla pojedynczego pliku, można nadać dostęp do pliku użytkownikowi, który nie ma dostępu do folderu nadrzędnego. To wtedy w takim przypadku widzi strukturę folderów w górę. Właśnie status uprawnień – to jest widoczność do folderu wynika z dostępu do plików i tylko konkretny plik, do którego ma uprawnienia, tylko to widzi, tak – pozostałe foldery są dla niego puste. Wyświetlanie uprawnień – widoku uprawnień w folderu przestrzeni wyświetlane są uprawnienia bezpośrednie i wynikające z dostępów do pliku niżej, tak, czyli oznaczone właśnie widoczność folderu, właśnie wynikające z dostępu do tego, co jest niżej. To jakaś sugestia – uprawnienia wynikające z dostępu do plików powinny być tylko do odczytu w interfejsie uprawnień folderu. No i tak jest, to akurat jest zaopiekowane, tam nie można tego edytować, jest po prostu informacja tylko, że to jest dostęp do widoku. No i teraz kwestia, która była poddawana dyskusji, że po pierwsze pliki nie będą przechowywane w bazie danych. To jest nasze MVP, czyli do tego trzeba zdefiniować przechowywanie plików lokalnie na zasobach sieciowych. Natomiast powinno być to spójne z resztą według Piotra. Czyli tak, jak dzisiaj przechowujemy attachment, to w ramach tego naszego attachment powinien być dodatkowy folder o nazwie, powiedzmy, Repository Files – czy jakkolwiek jak sobie zdefiniujemy – i tam przechowywane są te pliki. Co jest ryzykiem przy takim podejściu, że trzeba migrować wszystkich, u których wdrażalibyśmy repozytorium, którzy przechowują pliki w bazie, ale mówimy tu raczej o użyciu tej funkcjonalności u większych klientów, gdzie faktycznie pliki są przechowywane nie w bazach, tylko i wyłącznie w przestrzeniach on-premise'owych, bo jeśli mamy cloudowe rozwiązania, to nie trzymamy tego w bazie, a w większości dużych klientów on-premise'owych też definiujemy, że pliki są przechowywane w zasobach sieciowych, więc to jest jakaś nisza, której nie pokryjemy. I oczywiście jest do tego wyjście. Tak, można migrować te pliki z bazy do zasobów sieciowych. No tutaj jest propozycja już wynikowa z naszej dyskusji, czyli oddzielne uprawnienia lokalizacji plików repozytorium, możliwość wskazania tego samego folderu co dla plików ze spraw. Natomiast tego samego w cudzysłowie, bo w ramach tego folderu po prostu byłby to jakiś oddzielny subfolder, tak. Jeśli chodzi o strukturę, to z racji na to, co było napisane tutaj wcześniej – ta ścieżka w Windowsie kiedyś kończy możliwość swojej rozbudowy. To propozycja jest taka, żeby opierać to na ID węzłach. W jaki sposób łatwy sposób, w jaki sposób łatwo dostać się do fizycznego miejsca przechowywania danego pliku? Patrząc na repozytorium, propozycja Piotra była taka, że jeśli jestem w REST API, to tutaj w linku, tak jak w raportach, buduje mi się adres tej lokalizacji w postaci właśnie jakiegoś file, repository, slash, ID przestrzeni, slash, ID folderu, slash, ID podfolderu. No i jestem w tym folderze. Wtedy mamy. No załóżmy, że 4 znaki per folder, bo pewnie tysiąca węzłów mało kto przekroczy, tak – 10 000 węzłów raczej będą to. Setki, tak, czyli raczej w 3 znakach ograniczymy się do pojedynczej instancji folderu.

**Janusz Bossak:** OK.

**Damian Kamiński:** No właśnie, jeszcze była alternatywa, że pierwsze znaki nazwy, ale. Doszliśmy do wniosku, że chyba nie ma to sensu, czyli przyjdę, bo potem i tak będzie to tak, że będzie dokumentacja, powiedzmy, działu pielęgniarek, dokumentacja działu handlowego, dokumentacja jakiegoś innego działu i te pierwsze litery. Pierwsze znaki nazw będą w żaden sposób nie rozróżniane. No właśnie, to zresztą jest tu wymienione – dokumentacji projektu Alfa, dokumentacja projektu Beta, więc alternatywa jest tylko ID. Ostatecznie tylko ID. Identyfikacja plików w interfejsie – w adresie URL powinien być widoczny identyfikator lokalizacji. To jest właśnie to, o czym powiedziałem, czyli mamy jakąś, powiedzmy, piątkę tego – niekoniecznie. Mamy coś w tym stylu, tak? I w zasadzie na tym się kończy, bo możemy dojść roboczo tylko i wyłącznie do danego folderu. Potem jest ewentualnie na podglądzie jakiś tam preview, tak, i byłoby jakiś tam numer tego konkretnego pliku. No to umożliwi po prostu łatwe kopiowanie, jeśli trzeba by było debugować jakieś problemy, żeby przejść bezpośrednio do danego zasobu. Metadane w bazie danych – to jest kwestia do ustalenia, ale w zasadzie jako minimum w ramach MVP. Ustaliliśmy z Piotrem, że to mogło być spójne z tym, co jest w case. Jeśli chodzi o odwołania do plików, tak, bo tam te dane są tak, czyli jest jakieś ID przestrzeni, ID folderu, ID pliku. No, pozostaje jeszcze kwestia zapisywania uprawnień, ale to też może rozwiązać w jakiś sposób, pewnie JSON nowy, bo nie wiem – to pozostawiam już deweloperom, bo to już jest mocno, mocno techniczna kwestia, po prostu trzeba to proszę.

**Janusz Bossak:** To mam. Tu mam pytanie, bo to jest kluczowe w całym tym rozwiązaniu – metadane, czy mamy na myśli tylko metadane techniczne, to jest systemowe tego pliku, czy jakieś metadane właśnie definiowane tak jak na formularzu sprawy, tak, czyli takie, które z jakiegoś powodu użytkownik chce sobie przy tym pliku zapamiętać?

**Damian Kamiński:** Mhm. Tak. No na ten moment wykluczyliśmy takie w ramach MVP. Ale to jest kwestia rozwojowa, czyli że można dodać opis do pliku, na podstawie którego można by było go wyszukiwać, czyli poza tym, że jest nazwa, to mamy jeszcze jakiś dodatkowy opis, możemy mieć jakieś daty, które będą jakimiś, powiedzmy, datami obowiązywania i kiedy się one wygaszają, czy ustawiają jakiś tryb niedostępny, ale to jest. To są tylko propozycje, a nie wymagania.

**Janusz Bossak:** OK. Dobra. No wiesz, bo w odróżnieniu od procesów to tu mamy dużą zmienność, tak? Bo właściwie co każdy plik miałby mieć inne metadane. Czy mógłby potencjalnie mieć inne, czy jakieś w danym katalogu mają mieć takie same?

**Damian Kamiński:** Chodzi ci o zestaw metadanych? Tak, bo ja powiedziałem o opisie, a ty masz na myśli jakieś konkretne.

**Janusz Bossak:** Zestaw, nie.

**Damian Kamiński:** Opis, jeszcze jakieś cechy, które będą zdeterminowane per dany plik. No to nie jest, to nie jest zdefiniowane.

**Janusz Bossak:** Dobrze, czekam. Tutaj coś pisze, pisze ten Przemek, że tam to spotkanie, które mamy za 2 minuty.

**Damian Kamiński:** To jest perspektywa.

**Janusz Bossak:** Czy można przełożyć na trzynastą 30? No nawet dobrze by było. Odpiszę. Jak to jest w kalendarzu? Co to jest? Trzynasta 30? Kalendarz. Możemy. 30.

**Damian Kamiński:** Jeszcze raz, czy ja mogę tak?

**Janusz Bossak:** Spotkanie projektowe z Przemkiem, nie to.

**Damian Kamiński:** Tak, tak, tak.

**Janusz Bossak:** Dobra. No dobra, czyli inaczej mówiąc, bo jakby. Przepraszam za zamieszanie, takie wprowadzam, ale chodzi mi o jakby. Połączenie w sensie takim mentalnym albo właśnie rozdzielenie w sensie mentalnym pomiędzy tym, co robimy, czyli taki DMS typowy – taki Document Management System, czy to są dokumenty i tak dalej. A tym, co mamy w AMODIT jako takim, i w tym drugim repozytorium, gdzie jakby nośnikiem jest sprawa, proces, tak, a to – ten dokument – jest tylko elementem tej sprawy. Elementem procesu. Tu mamy odwrotnie – to mamy dokument. I tyle, tak. I pytanie, czy on w przyszłości, ten dokument stąd, może stawać się elementem sprawy. Tak, znaczy, jakie będzie powiązanie pomiędzy tym DMS a AMODIT jako takim? Ale może to jest pytanie na przyszłość. Stawiam.

**Damian Kamiński:** No tak, tu może być jakiś opis, mogą być jakieś tagi, to jest jakaś przestrzeń do, do właśnie, powiedzmy, definiowania tagów przy dokumencie i tej funkcjonalności. Natomiast.

**Janusz Bossak:** No tak, no mogą być jakieś ogólne. Ogólnie słuszne jakby metadane, tak, gdzie właśnie, jak mówisz, opis, nazwa, tak – jakieś tego typu rzeczy można sobie wymyślać.

**Damian Kamiński:** Tak.

**Janusz Bossak:** No dobra, dobra, rozumiem, OK.

**Damian Kamiński:** Dalej mamy interfejs użytkownika, czyli widok drzewa folderów po lewej stronie – nie opcjonalnie, tylko jako MVP – główny obszar to jest właśnie zawartość aktualnego folderu. Ścieżka breadcrumbs na górze. No to tu już mówimy stricte o linkowaniu. To ścieżka wynika stąd, więc według mnie nie trzeba tu jej jakoś przedstawiać, tak jak, tak jak, powiedzmy, tutaj. Coś jeszcze. I domyślnie – tutaj konsultowałem to jeszcze z Kamilem. 2 widoki, czyli kafelkowy i alternatywnie lista – niekoniecznie te 2 typy listy, jeden jest do usunięcia. Wydaje się, że ta lista niekoniecznie nawet jest potrzebna. Kto jest właścicielem, data modyfikacji, rozmiar – raczej jako MVP może wystarczy nam po prostu lista plików. Takie formy, ale to też jest – mówiłem – możemy to rozbudowywać dowolnie. Pytanie, czy te dane w ogóle jakkolwiek są zasadne? Może jedynie data modyfikacji? Bo to, kto jest właścicielem, czy jaki jest rozmiar tego pliku, to już są, powiedziałbym, ciekawostki. Ale nie wykluczam, że one mogą być przy rozwoju przydatne, żeby wiedzieć, kto dany plik dodał. No ale do tego za chwilę jeszcze dojdziemy, bo to też jest kluczowy element. Aspektów technicznych. Zarządzanie uprawnieniami – to już po części pokazywałem, czyli przycisk uprawnienia na każdym folderze, pliku. Do tu mamy model paneli, tu użytkowników i grup. Checkbox – przerwij dziedziczenie – i wskaźnik wizualny, gdy to dziedziczenie jest przerwane. Operacje na plikach – dodawanie, usuwanie tego nie mamy. Przenoszenia plików między folderami – to powiedziałbym, że jest poza MVP. No i do ustalenia – wersjonowanie plików, historia zmian. To według mnie też jest poza MVP.

**Janusz Bossak:** No dobra, znaczy to koniec tych.

**Damian Kamiński:** Nie, nie, nie. Nie, jesteśmy za połową.

**Janusz Bossak:** Zgodzę się, że to wydaje się, że tak gigantycznym projektem.

**Damian Kamiński:** Nie.

**Janusz Bossak:** W mojej skromnej ocenie to jest pół roku, a nie sprint czy 2. Pół roku. Więc tutaj, jeżeli chcemy to w miarę szybko zrobić, to przegrupowanie sił polegające na tym, że wszyscy praktycznie biorą się za to. Wszyscy.

**Damian Kamiński:** Mhm. No dobrze, to na razie przejdźmy do końca. Zgodność z systemem – tutaj jest, tu w zasadzie to już, już chyba nadmiarowe. Zgodne z systemem uprawnień – to znaczy, tu w zakresie może definiowania. Użytkowników, ale w zasadzie zakładam, że uprawnienia, czyli nadawaniu uprawnień, dotyczy tylko i wyłącznie administratorów albo systemu, albo obszarów. Wszyscy pozostali użytkownicy to są użytkownicy, którzy są użytkownikami samego repozytorium, a nie nadawania uprawnień, więc w tym zakresie zgodności co do uprawnień. No to taka osoba, która ma nadawać uprawnienia, prawdopodobnie musiałaby mieć też możliwość edycji użytkowników, tak, po to, żeby ich wszystkich widzieć, jeśli ma tym zarządzać globalnie. Więc tutaj w tym zakresie ewentualnie ta zgodność musi być utrzymana i widzieć wszystkie grupy. No tutaj możliwość nadawania uprawnień pojedynczym użytkownikom, grupom – rolą to nie jest dobra. Grupą i użytkownikom. Logi, audyt – i tu już się zaczynają zagadnienia, które poprosiłem Piotra o to, żeby precyzował. To według niego w takim kontekście jest nieumówione. Czyli właśnie, czy logować operacje na plikach? Kto, kiedy, jaką operację wykonał? No i jeszcze jest 16-17 punktów, które należy doprecyzować, tak, czyli czy ustawiamy maksymalną ilość zagnieżdżenia? To jest pytanie otwarte, tak. Nie wiem, czy teraz będziemy na nie odpowiadać, czy pozostawiamy to.

**Janusz Bossak:** Znaczy, na pewno trzeba wprowadzić jakieś ograniczenie tych zagnieżdżeń.

**Damian Kamiński:** Może.

**Janusz Bossak:** To mi się wydaje. Ile to jest? Nie mam pojęcia. 5-10 poziomów. Może się wiązać z długością tej ścieżki, którą potencjalnie można wolę pokazać, tak, bo jak tam – tej ścieżce – nie wiem, to ta cała ścieżka ma być widoczna, czy tylko jest ID tego dokumentu? On już wie, gdzie on jest.

**Damian Kamiński:** No to jest do ustalenia. Nie wiem, ja nie jestem w stanie na to pytanie wprost odpowiedzieć. Natomiast zakładam też, że tych zagnieżdżeń nawet jakby było 6, no to to maksymalnie będzie skutkować 24 znakami w adresie. Bo 6 x 4 – przy, powiedzmy, setkach folderów, bo mamy, powiedzmy, raz, 2, 3, 4 – jeszcze jest 5, 6 – jak wchodzimy w ten szósty, no to tu w adresie mamy wtedy ID pierwszego, drugiego, trzeciego i tak do szóstego. No i tyle. I potem dodaje się jakieś hash, wywołując już sam podgląd, tak jak to wygląda dzisiaj w raportach. Widoczność folderu jako osobne uprawnienie – to nie ma sensu. To jest już, bym powiedział, powtórzenie. To nie może być osobne uprawnienie, to jest tylko uprawnienie wynikowe już oddolnie, nadając uprawnienie do podglądu do jakiegoś pliku. Struktura katalogów na dysku – tutaj jako propozycja jest, żeby było tylko ID, więc tu w zasadzie to jest rozwiązane. Wersjonowanie plików. Ja bym to wykluczył poza MVP. Historia zmian. Przynajmniej w zakresie tego, kto plik załadował. Albo, właśnie, jeśli usuwał, to pytanie, co logujemy – nad tym trzeba było się zastanowić. Raczej jakiś deweloper – w sensie architekt techniczny tego rozwiązania – powinien zaproponować. Jeśli chodzi o współdzielenie, to zakładam, że czy linki publiczne – nic takiego nie robimy – to jest tylko i wyłącznie wynikowe z tego, jak administrator danego repozytorium nadał te uprawnienia.

**Janusz Bossak:** Czyli nie ma linków publicznych.

**Damian Kamiński:** Nie ma. Limity rozmiaru – to bardzo dobre pytanie, czy. Mamy limit dla pojedynczego pliku.

**Janusz Bossak:** No to tak.

**Damian Kamiński:** Tak, to jest pewna analogia do tego, co teraz mamy. API. Że, właśnie, do dużych plików trzeba robić odrębne endpointy, więc tutaj pytanie, ile przejdzie przez ten, powiedzmy, interfejs przeglądarkowy, ale to w jaki sposób pewnie może być spójne z tym, jakie pliki możemy załadować przez interfejs, a wydaje mi się, że o tym Piotr mówił właśnie, bo ostatnio w związku z tym robi to i tam oni próbowali to obejść, czyli dzisiaj są to 2 giga. To jest do potwierdzenia. Typy plików – zakładam, że to będzie spójne z tym, co w sprawach. Podgląd plików będzie dostępny na zasadzie analogicznej jak obecnie w raportach, czyli wykorzystujemy gotowy komponent. Wyszukiwanie – nie wiem, czy tu jest jakiekolwiek ryzyko odpalenia wyszukiwania, pełnotekstowego – to mogłoby być ewentualnie rozwoju.

**Janusz Bossak:** Według mnie nie powinno być. Jakoś.

**Damian Kamiński:** Tylko, czy na wszystkich plikach, tak, czy to powinno być też?

**Janusz Bossak:** Nie wyobrażam sobie repozytorium bez – znaczy nie. Wyszukuję. I ona – znaczy powinno działać tak jak w oparciu, chyba o ten Lucene, jaką mamy.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** I uprawnienia, które będą na tym repozytorium, tak, czyli wyszukuję mi, czy inaczej – pokażę mi. Wyszukam wszystkich. Ewolucji nie ma przecież uprawnień, więc luźno – i wyszuka we wszystkim. Ale później to się jakby zderzą z moimi uprawnieniami i pokaże mi tylko te wyniki, które są zgodne z moimi uprawnieniami.

**Damian Kamiński:** Tak, tak, tak. Ale tu ewentualnie myślę, że dobrze by było, żeby takie pytania padły, czyli jakie są ryzyka bezpieczeństwa, jakie są ryzyka wydajnościowe, tak, czyli ktoś wrzuca 2-gigowy plik Word'owy, czyli załóżmy książkę, która ma 1000 stron. No i pytanie, jak to szybko się przetworzy? Czy to będzie odrębny job, czy to będzie ten sam job, co? Dla spraw, czy to będzie odrębny plik Lucene, bo tak raczej zakładam, czy to będzie jakoś spójne z tym, co mamy, czy w ogóle da się zrobić to odrębnym plikiem?

**Janusz Bossak:** To jest trzeba zaadresować tak dokładnie.

**Damian Kamiński:** Jeśli to jest. Tak, to są pytania, które trzeba postawić i określić. Etykiety, tak – i no to, to w zasadzie to, co padło – to tutaj też podpowiedział – dla łatwiejszego wyszukiwania. Poza MVP. Powiadomienia – to też według mnie w ogóle nie, nie wiem, czy to jest kluczowe, ale mogłoby być gdzieś kiedyś w przyszłości, jeśli nas ktoś, kto zasponsoruje. Obecnie nie mamy, więc nie dotyczy, ale może niech będzie też sprecyzowane, że nikt tu nie migrujemy. Żadnych rozwiązań. Uprawnienia do samej struktury, czy oddzielić uprawnienie do tworzenia, usuwania folderów od usuwania plików? No i to jest w zasadzie słuszne. Może po prostu. Samo uprawnienie usuwania powinno być de facto wyodrębnione, tak, czyli czy można? Poza dodawaniem usuwać, a jeśli tak, to może tylko swoich plików, tak, tak bym to widział. W kontekście biznesowym, czyli jak się pomyliłem na bieżąco, czyli coś wgrałem i chcę usunąć, to ten swój mogę usunąć, natomiast żadnych cudzych nie. Żeby nie ktoś nie przyszedł i nie zrobił. Bałaganu. Co w sumie też kolejne słuszne – czy powinien być coś takiego jak kosz? Zakładam, że. Osobiście uważam, że raczej tak, tak jak mamy to dla spraw, przy czym ten kosz pewnie.

**Janusz Bossak:** Zaznaczymy, tak, oznaczamy jako usunięte, ale fizycznie jeszcze nie usuwamy.

**Damian Kamiński:** Tak, przy czym może tutaj od razu ten kosz powinien być zaopiekowany jakimś okresem czasu, tak, czyli nie trzymamy w nieskończoność. Tylko. Może tutaj dopiszę w. Kosz. Uprawnienia do usuwania. Myślę, usuwanie tylko swoich plików. I tutaj. Tak. Może dobra. Jako MVP. W przyszłości czyszczenie okresowe, na przykład 30 dni. W ten sposób, bo to też nie musimy na starcie tego mieć. To nie jest krytyczne, bym powiedział. Eksport, import struktury – według mnie nie. Integracja z szablonami XLT. Obecna dyskusja. To już było akurat. To w ogóle nie dotyczy. Tam na koniec rozmawialiśmy o czymś innym i on to zaciągnął. Do ustalenia – scheduled job. Czyli które funkcjonalności swojego MVP, które mogą być zrobione w kolejnych? No to to zrobiliśmy. No dobrze, dziękuję za wsparcie. Pytanie, czy ty widzisz jeszcze coś, co nie zostało poruszone?

**Janusz Bossak:** Ja miałem temat dotyczący bezpieczeństwa tych plików. Tam mówiłeś, że one będą trzymane poza AMODIT i pytanie, czy przewidujemy, ale chyba tak – zgodnie z tym, co robi – szyfrowanie tych plików, tak, czy one są szyfrowane?

**Damian Kamiński:** Mhm, słusznie.

**Janusz Bossak:** To jest pierwsza. Druga kwestia to, jak mówiłeś o strukturze tych plików tam, właśnie, czyli gdzieś są przechowywane.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** I tam – sugerowali, że będą według ID – właściwie w takiej strukturze płaskiej, tak. Się zastanawiam. Pod kątem też potencjalnego jakiegoś backupu, zyskiwania i tak dalej, i tak dalej. Czy jednak nie lepiej jest tam, w tym miejscu, gdzie to będzie fizycznie przechowywane? Żeby jednak to było zgodne ze strukturą tych folderów tutaj? Czy to nie ułatwi w jakiś sposób zarządzania potencjalną awarią, odzyskiwaniem fragmentu i tak dalej? Nie, bo jak one wszystkie takie w jednej kupie, no to nie wiesz jeszcze – jak będą zaszyfrowane, to już w ogóle nie wiesz, co jest. Czy?

**Damian Kamiński:** Nie, nie, poczekaj, poczekaj. Tu się coś nie zrozumieliśmy. Tam zrobiłem przykład, to może się cofnę do tego.

**Janusz Bossak:** OK.

**Damian Kamiński:** Tak by wyglądała ścieżka, czyli żebyśmy to tak.

**Janusz Bossak:** Gdzieś w momencie powiedziałeś, że nie – to w innym miejscu pokazywałeś, że – ja źle zrozumiałem. Czyli to jest?

**Damian Kamiński:** To powiedz jeszcze raz.

**Janusz Bossak:** To jest struktura, rozumiem, fizyczna na dysku, tak? Tak będzie.

**Damian Kamiński:** Tak, tak. Tak to widzę. Powiedzmy, AMODIT, Attachment, dalej. AMODIT to są lata – do myślenia najpierw są ID procesu, potem lata i potem już sprawy – a tu by było po prostu dodatkowy folder, na przykład coś takiego, i dalej jest ID przestrzeni, ID folderu, które może być wielokrotnie powielone, czyli.

**Janusz Bossak:** No tak, tak. To gdzieś w innym miejscu.

**Damian Kamiński:** W ten sposób. Czy tak by to, tak by to wyglądało?

**Janusz Bossak:** No może źle zrozumiałem.

**Damian Kamiński:** Więc. Czy jest to odtwarzalne? No jest, w sensie nie mamy w tych nazwach nazw tych przestrzeni, folderów, ale struktura jest zachowana pełna, tak. Wtedy należy odtworzyć właśnie strukturę przydziału.

**Janusz Bossak:** No dobra.

**Damian Kamiński:** OK? Tak.

**Janusz Bossak:** OK, no dobra. Mam tam więcej.

**Damian Kamiński:** Dobrze, czy coś jeszcze przychodzi ci do głowy?

**Janusz Bossak:** Znaczy, to, co mówiłem już tutaj, w międzyczasie będący, że tak powiem, przy zapoznaniu z tym, co tu jest napisane i powiedziane. I to jest gigantyczny projekt. I trzeba do tego sprytnie podejść, jeżeli to chcemy zrobić, nie wiem, w 3 sprinty, to naprawdę musimy to dobrze przemyśleć, co my chcemy. Na pewno trzeba wykorzystać AI. I niestety zgodzić się z tym, że zrobi tak jak komunikator, że będą jakieś tam większe, mniejsze kwaczki i to będzie takie, a nie inne. Ale inaczej to tego sobie nie wyobrażam – jak do tego byśmy mieli podejść tak po bożemu i to robić jako normalny projekt. To jest pół roku roboty. Dobrze, że masz ten projekt wizualny, tak, bo ten projekt wizualny już dla AI byłby. Dobrą, że tak powiem. Bazą, tak, dobrym odnośnikiem. Żeby go tam wrzucić i liczę na to, że ten AI nam tutaj już skróci czas wytworzenia od co najmniej 50%, tak, czyli zamiast tam 6 miesięcy będziemy robić 2-3 miesiące, ale. To się nie da.

**Damian Kamiński:** Znaczy, ja nie wiem, jak wydajny jest Filip w tym zakresie, ale patrząc na to, co i jak szybko robi Przemek, to Filip już zaczął tam to klepać w cudzysłowie.

**Janusz Bossak:** Tak, ale wiesz, wizualne efekty to jest jedno, ale tu jest backendu sporo, tak.

**Damian Kamiński:** Tak, tak, zgadza się. Sam backend, to to jest już kwestia do zaopiekowania.

**Janusz Bossak:** I trzeba sprawnie ten backend zrobić, żeby to wszystko elegancko tam. To funkcjonowało. Wgryzło się, że tak powiem, w ten model i tak dalej. My – znaczy, wiesz, z jednej strony mi się to strasznie nie podoba, tak, znaczy robimy rzecz, która. Jest dla jednego klienta.

**Damian Kamiński:** Czekają już, czy? Przepraszam, że tak przerywam, ale czy uważasz, że jeszcze będziemy poruszać kwestie merytoryczne, czy kończymy nagrywanie?

**Janusz Bossak:** Kończymy. Nagrywanie, tak.

