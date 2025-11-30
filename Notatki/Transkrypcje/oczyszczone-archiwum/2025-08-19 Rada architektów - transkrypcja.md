**Rada architektów 2025-08-19 - Transkrypcja**

**Data:** 2025-08-19
**Uczestnicy:** Damian Kamiński, Janusz Bossak, Marek Dziakowski, Łukasz Bott, Anna Skupińska, Piotr Buczkowski, Kamil Dubaniowski

---

**Damian Kamiński:** Tak już włączyłem, tak?

**Janusz Bossak:** Proponuję wypowiedzieć to podsumowanie, niech ktoś to opowie swoimi słowami jeszcze raz, żeby się nagrało, żeby potem można było sobie to przekopiować. Marek, opowiedz, jak ty to rozumiesz.

**Damian Kamiński:** No dobrze, to Marek mówisz?

**Marek Dziakowski:** To tak. Jeżeli chodzi o administratorów organizacji, zostawiamy tak jak jest. Jeżeli chodzi o nasze przejście serwisowe, no to robimy tak jak wspomniał Piotr, czyli dodajemy logowania Auth (OAuth) i na tej podstawie będziemy weryfikować, czy ktoś ma dodatkowo jeszcze dostęp poza tą domyślną grupą użytkowników. Tak, a jeżeli chodzi o przycisk to tutaj... Właśnie zostajemy tak jak było, czy dodatkowo to jeszcze?

**Damian Kamiński:** Zostaje. Tylko Janusz ma uwagi co do nazwy tego przycisku, ale ja nie mam lepszego pomysłu. "Zarządzaj dokumentem w Trust Center".

**Marek Dziakowski:** Tylko zmiana. W zasadzie klarowne dosyć, wiadomo do czego służy wtedy. Tak samo "Przejdź", to jak ktoś nie miał styczności za dużo, no to nie będzie wiedział o co chodzi w "Przejdź".

**Janusz Bossak:** Znaczy, wydaje mi się, że tak, "Zarządzaj dokumentem w Trust Center" byłoby bardziej zrozumiałe.

**Marek Dziakowski:** Coś jeszcze? Coś pominąłem?

**Damian Kamiński:** Znaczy kliknięcie tego przycisku powoduje walidację, czy [użytkownik] jest wysyłającym lub też czy jest w puli administratorów organizacji. Jeśli nie jest, to dostaje już na tym etapie komunikat, że nie może przejść i "skontaktuj się z administratorem". Jeśli jest, to pytanie, czy jest ten etap, gdzie wprowadza maila, czy od razu już robimy tak jak tu "wprowadź kod", czyli od razu wysyłamy maila? Ja bym robił tak.

**Marek Dziakowski:** Automatycznie, czy żeby jeszcze podał?

**Damian Kamiński:** Żeby było mniej klikania, ale no nie wiem czy jest jakieś ryzyko.

**Marek Dziakowski:** Może być automatycznie. Raczej nie wydaje mi się... tylko tyle, że no trzeba będzie wtedy podnieść wersję, żeby to działało tak. A ten ta zmiana wcześniejsza, czyli wpisanie kodu, no to wtedy działa na dowolnym AMODITcie dla wszystkich.

**Damian Kamiński:** No to pytanie do której wersji... nie wtedy czy jeszcze do... nie wiem.

**Marek Dziakowski:** Znaczy to nie tyle do której wersji, tylko nie zmusimy klientów, chyba żeby zrobili teraz wszyscy aktualizacje, bo wiadomo, niektórzy nie chcą, bo im działa.

**Damian Kamiński:** No ale to wiesz, to wejdzie swoim rytmem.

**Marek Dziakowski:** I nie wejdą już na dokument.

**Damian Kamiński:** Aha, bo Trust Center podniesiesz, OK.

**Marek Dziakowski:** Ale no to swoim... no właśnie, tak tak.

**Damian Kamiński:** To jak tego nie zablokować, jak to zrobić, żeby to było [kompatybilne]?

**Marek Dziakowski:** Można zrobić tak, że jeżeli jest wysyłany email w query stringu, no to wtedy nie pokazuj [pola], tylko od razu wyślij. A jak nie ma, no to pokaż, o tak. Że jeżeli nikt nie podał, no to wtedy można podać, tak, tu się pojawi ten input. Jeżeli ktoś podał, znaczy został wysłany z AMODITa adres e-mail, wtedy nie pokazujemy tylko od razu wysyłamy i to będzie ta automatyzacja.

**Damian Kamiński:** OK. No to mamy. Ktoś ma jakieś uwagi?

**Marek Dziakowski:** OK.

**Damian Kamiński:** Dobra to kolejny temat, Marek, jeszcze masz jakiś jeden?

**Marek Dziakowski:** Nie, to wszystko.

**Damian Kamiński:** No dobrze, czy ktoś chce coś poruszyć? Jak ja mam ekran, to mogę pokazać ten news feed, jakbym to widział, żebyście to skomentowali, ewentualnie poprawię i można to dawać na realizację. Więc tak, to jest prototyp, jakby to mogło wyglądać. Pytanie, czy tak powinno? Wstępnie umieściłem to w menu powiadomienia. Może nazwa "powiadomienia" powinna ulec zmianie w przyszłości, albo nie wiem, może możemy tutaj dodać jakiś kolejny węzeł? W ramach tych głównych "Do wykonania", "Powiadomienia" i jeszcze jakieś "Wiadomości" do zastanowienia. Na razie wrzuciłem to tak.

**Łukasz Bott:** To miałem pytanie... To co pokazujesz, czy ten omawiany news feed, to chodzi o zastąpienie tego starego mechanizmu newsów?

**Damian Kamiński:** Tak, tak, tak, tak. Wczoraj z Piotrem rozmawiałem, CIT tego nie używa, Deutsche Bank... Czekam na informacje od serwisanta, miał się z nimi skontaktować i dać mi znać, póki co jeszcze nie odpowiedzieli. No i tu jest po prostu, jak dzisiaj mamy tylko aktywności, to tu jest zakładka "Ogłoszenia". Po włączeniu tej zakładki pojawia się dodatkowa belka, szukaj i oznacz wszystko jako przeczytane. Można utworzyć nowe ogłoszenie, gdzie wskazujemy temat i treść i odbiorców na podstawie działów. Pytanie, czy tutaj czegoś nie ma... Nie ma tutaj wskazywania na ten moment w tym projekcie organizacji zewnętrznych. Można to dodać. Pytanie, czy teraz to opiekujemy, bo jak się nikt z tego nie korzysta, to może na razie to nie jest nasz MVP. Więc tu jest prosty model wysyłający...

**Łukasz Bott:** Zaczekaj. Dlaczego... jeszcze jedno pytanie, bo tutaj padło hasło, skoro z tego nikt nie korzysta, to po co my się w ogóle zajmiemy tym feedem?

**Damian Kamiński:** Nie no, bo WIM ma takie wymaganie. Ja mówię, że on istniał i z jednej części, której tu nie zrobiłem, nikt nie korzystał po prostu, więc na razie jeszcze nie projektowałem. To można dołożyć zawsze.

**Łukasz Bott:** A WIM potrzebuje, OK. Dobra, dobra.

**Damian Kamiński:** Natomiast prosty model, tak jak tworzenie maila, no i w zasadzie podgląd tak. Klikamy, mamy po prawej stronie podgląd. Tabelkami się jeszcze nie suwa, ale powinna. No i tyle, oznaczenie jako przeczytane i odebrane i możliwość usunięcia. Wszystko. Nie ma tu nic specyficznego.

**Anna Skupińska:** No pytanie, osoba, która tworzy zgłoszenie, może usunąć? Jak usunie to wtedy usunie od wszystkich czy tylko swoje?

**Damian Kamiński:** Bardzo dobre pytanie, nie wiem. Na razie pytanie ogólne tak, czy jeśli ktoś wyśle, to czy może to wywalić? No tak jak na mailu, poszło to poszło.

**Łukasz Bott:** Nie no, swoje.

**Damian Kamiński:** Nie można usunąć z cudzej skrzynki.

**Janusz Bossak:** No ale wywala u siebie, nie u wszystkich, nie?

**Damian Kamiński:** Tak.

**Janusz Bossak:** Znaczy, to jest trochę jak mail, tak? "Utwórz ogłoszenie". To jest jak utworzenie maila, tak, czyli piszę wiadomość i klikam wyślij, no i poszło. Różnica jest taka, że tutaj nie ma kopii 50 dla wszystkich osób z jakiegoś działu, tylko widać to po prostu, te wszystkie osoby to widzą. I jedyne co taka osoba widząca (nie ta która tworzy) może zrobić, no to przeczytać. I ewentualnie tak jak maila zarchiwizować. Tak, no bo, ale dla siebie.

**Łukasz Bott:** Oznaczyć jakoś tak, oznaczyć jako przeczytane i już na przykład nie wyświetla się tej osobie.

**Damian Kamiński:** Znaczy to... Oznaczyć jako przeczytany albo po prostu się odpiąć? Tak, bo ja zakładam, że to jest jedna treść, tylko tu są jakieś powiązania w bazie i tyle, czyli usunięcie powoduje odpięcie tej wiadomości od tego użytkownika i tyle.

**Janusz Bossak:** No właśnie zastanawiam się, czy to jest sensowne, bo potem ktoś będzie się tłumaczył "ale ja nie widziałem tego".

**Damian Kamiński:** Też się zastanawiam. Dodałem to, bo to było tam... możemy tego się pozbyć, cała historia jest, możesz oznaczyć jako odebrane. Można tu dodać jeszcze ewentualnie "oznacz jako nieprzeczytane", można dać jeszcze jeden kafelek "pokaż tylko nieprzeczytane", żeby móc odfiltrować. No i jest to jakieś wyszukiwanie proste, tak?

**Janusz Bossak:** Także no słuchajcie, bo mi chodzi o to, żeby jak najmniej zmieniać backendu. Nie wiem, to pewnie jest tam w WEB API.

**Piotr Buczkowski:** W .NET Core? Tak, trzeba napisać na nowo, bo nie ma kontrolerów, jest tylko kod WIM Web API [niezrozumiałe] MVC. Znaczy klasy zostaną do zapisywania do bazy danych tak, ale backend tego, kontrolery trzeba napisać.

**Janusz Bossak:** No dobra, to i tak i tak coś tam możemy tutaj zmieniać. Bo wiecie co mi tu brakuje? Terminów. Bo mogę napisać ogłoszenie, które ma być publikowane na przykład od 1 września.

**Damian Kamiński:** Zaplanowane, tak. Aha.

**Łukasz Bott:** Zaplanowane, ale też czy nie może mieć terminu ważności?

**Janusz Bossak:** Nie może mieć terminu... na przykład...

**Damian Kamiński:** Ale termin ważności to co, że ma zniknąć?

**Łukasz Bott:** No no tak, no jeżeli ogłaszasz na przykład nie wiem, zapisy na wycieczkę firmową, tak, no to żeby to nie wisiało permanentnie.

**Damian Kamiński:** No to będzie... No dobra, ale ja to sobie odznaczam, przychodzę po urlopie "o była wycieczka", się dowiaduje... ale w [niezrozumiałe] po temacie i sobie wisi. To ma na pewno tak znikać?

**Janusz Bossak:** Ale, ale termin ogłoszenia byłby chyba przydatny, tak?

**Damian Kamiński:** Planowanie jak najbardziej zgadzam się. To znaczy wiecie, znowu Janusz, może i twój pomysł jest słuszny, ale róbmy to po minimum, tak jak powiedziałeś, żeby zaliczyć, a potem będziemy się zastanawiać nad rozwojem.

**Janusz Bossak:** No tak. Znaczy ciągle mi się wydaje... znaczy to jest pytanie do pana Piotra też Murawskiego? Czym się różni anons od newsfeeda? Bo dla mnie to są te same, to jest to samo.

**Damian Kamiński:** Może tak być, to musimy z nim jeszcze przegadać.

**Łukasz Bott:** Może on ma na myśli RSS-y?

**Damian Kamiński:** Znaczy, wiecie jedyne co tu widzę, to już mówiłem, jeśli tworzymy nowe ogłoszenia, to ja zakładam, że na poziomie procesu jest łatwiej zarządzać odbiorcami, bo tutaj mamy ograniczenie tylko na działy. Ale znowu, musimy i tak to stworzyć, więc nic nie stoi na przeszkodzie, że "wybierz odbiorców". Tutaj dajemy listę rozwijaną czy jakieś checkboxy? Pokaż działy. Pokaż grupy, bo działy niekoniecznie pokrywają się z grupami. I wtedy może im to wystarczy. Tak jak powiedziałeś, że... i może wtedy dołożenie tych 2 dat ma większy sens, bo wtedy w kontekście takiego ogłoszenia... "No właśnie mam dostępne łóżko, to jest od danego dnia do danego dnia" i wtedy ono znika. I wtedy tym tematem jednym obsługujemy wszystko. Natomiast odbiorcy jako grupy, bo pielęgniarki mogą być w dziale "45 testach" i w tych testach, ale tam mogą być jeszcze inni użytkownicy w ramach tej struktury i niekoniecznie oni powinni być odbiorcami.

**Łukasz Bott:** No to... To nie tyle... A nie dajemy możliwości wysłania ogłoszenia do wskazanych osób? Po prostu.

**Damian Kamiński:** Znaczy ja zrobiłem tak jak było.

**Łukasz Bott:** OK, dobra.

**Janusz Bossak:** Znaczy wiecie, że można pójść... No no ale znowuż MVP, tak, to jest tak jak było. Ale można pójść po całości, czyli tak jak mamy w raportach, nie? Że na przykład tylko dla administratorów, bo może jakieś ogłoszenia dla administratorów są ważne. Dla wszystkich, które nic nie wybieramy (tylko dla wszystkich) i dla wybranych grup, tak jak mamy w raportach. I wtedy sobie wybierają grupę lub osoby...

**Damian Kamiński:** Albo struktura. I wtedy mamy wszystko.

**Janusz Bossak:** Znaczy właśnie to jest albo... albo dla administratorów, albo dla wszystkich.

**Damian Kamiński:** Tak, tak, tak, ale chodzi mi o to, że mamy wszystkie możliwości przypisania odbiorców.

**Janusz Bossak:** Albo według [wyboru] tak.

**Damian Kamiński:** Tak, tak, tak możemy tak zrobić. Mamy te modele w zasadzie gotowe, no z wyborami jedynie. No tak struktura... Też mamy.

**Janusz Bossak:** No i to co powiedział Łukasz, to wydaje mi się nabiera sensu. Jeżeli tam mówimy o jakiś nie wiem, wymianie łóżek czy monitorów, że osoba, która daje to ogłoszenie, może to ogłoszenie zdjąć. No to jest tak trochę jak dajesz na OLX, tak, że już to zostało sprzedane, no to zaznaczasz "zdejmij to ogłoszenie". Teraz jak to powiedziałem, to dopiero chyba do mnie dotarło, czym się różni anons od ogłoszenia? Bo oni naprawdę ogłoszenie to traktują jak OLX-a, bo to były nawet przykłady takie, że wiem, że mam monitory do wydania, mam łóżka do wydania. I to w tym rozumieniu jest ogłoszenie. To nie jest ogłoszenie o wycieczce, tylko to są dosłownie, wydaje mi się, takie OLX-owe ogłoszenia, że mam coś na wydanie, mam coś na wymianę.

**Damian Kamiński:** No dobrze, to pytanie jest takie: mam zadzwonić do pana Piotra i podpytać o różnicę w jego rozumieniu między newsfeedem a tą tablicą ogłoszeń? Jeśli okaże się, że ona jest na tyle trywialna, że to ma być tylko data publikacji i możliwość zdjęcia, to robimy to wszystko w ramach takiej tablicy ogłoszeń.

**Janusz Bossak:** Wydaje mi się, że tak. Znaczy, bo słuchajcie jeszcze jest jedno rozwiązanie, które pan Piotr nie bardzo chciał jakby akceptować, a o którym chyba tutaj z Damianem wczoraj rozmawialiśmy. To jest wykorzystanie jakiegoś procesu. Tak, robimy sobie proces pod tytułem "Anonse" czy "Ogłoszenia", który ma pewne cechy, na przykład, że sprawę można udostępniać odpowiedniej grupie osób. Może to trzeba tam ułatwić tylko. No i tyle. Może mamy dokładnie to samo, tak, w powiadomieniach tu się pojawiają rzeczy z tego procesu, który byłby tutaj jak gdyby podpięty. Tyle, nie? No ale możemy tak robić, no że to jest wyspecjalizowana funkcjonalność, którą robimy specjalnie i ona tu będzie po prostu niezależnie od obiegu spraw. No bo jednak obieg spraw niesie cały ten ciężar dodatkowy, tak, czyli historię... Ale z drugiej strony jest to jakiś plus też, no bo mamy gotowe różne rzeczy. Pytanie, czy potrzebne. Tak, bo ja już teraz tak... A niech ktoś powie, że tu w tym ogłoszeniu chce dodać zdjęcie tego telewizora albo tego łóżka.

**Damian Kamiński:** No a to jest kolejne pytanie, co tu można wrzucić? Nie.

**Janusz Bossak:** No właśnie, no i budujemy pewien formularz... "Dodać to, dodać tamto", tak? A może to ktoś będzie chciał komentarz do tego ogłoszenia dać? "Ja to bym wziął, ale nie 5 tylko 3". I tak dalej, i wiecie, zaczyna [powstawać] cały mechanizm, który trzeba zrobić. Co mamy?

**Damian Kamiński:** To znaczy, to jest formularz w formie mailowej. Tak, wysłane - poszło. Nie ma edycji. Sprawa daje kontekst właśnie wprowadzenia jakiegoś stanu, jakiegoś aktualizacji. No tu nie można. Jak teraz mam już tylko 3, bo ktoś już się zgłosił po minucie, to muszę wysłać kolejne ogłoszenie, nie?

**Marek Dziakowski:** Link do sprawy można dodać, specjalny proces, jakiś ogłoszenie.

**Damian Kamiński:** No właśnie, ale oni nie chcieli, żeby to była sprawa. Niemniej no można ich pewnie przekonać pokazując coś, tylko...

**Piotr Buczkowski:** Że można podpiąć dyskusję z tego Talka albo AMODIT Talk.

**Janusz Bossak:** No właśnie na przykład. Wiecie? W którą stronę idą moje obawy? Moje obawy idą w tą stronę, że na podstawie parcia pana Piotra, takiego uporu, produkujemy jakieś takie... wrzody na tyłku. Żeby tylko go zaspokoić, nie? Takie nie wiadomo co, takie funkcjonalności, które potem będzie albo ciężko obronić, [albo] ciężko rozwijać. Bo każda ma coś... Tak jak tutaj jest ten Talk, w którym w sumie mogę przecież zrobić sobie taką grupę jak wziąć tam Pielęgniarki i napisać: "Słuchaj, mam monitor do wydania".

**Damian Kamiński:** Wszystkim się pojawi.

**Janusz Bossak:** Wszystkim się pojawi, dokładnie realizuje tą samą funkcjonalność, nie? Więc o to mi chodzi, żeby z nim naprawdę usiąść...

**Piotr Buczkowski:** Znaczy pierwotnie to mechanizm Ministerstwa Sportu miał być właśnie ogłoszenie o naborach czy coś.

**Damian Kamiński:** Znaczy konkluzja jest taka, że na pewno trzeba to z nimi przegadać, żeby nie robić 3 funkcjonalności, które będą to samo realizować.

**Janusz Bossak:** Dokładnie. I ja bym panu Piotrowi powiedział, że panie Piotrze, my możemy zrobić naprawdę na różne sposoby. I tak i siak, i tak. Chodzi o to, żeby oni byli zadowoleni, tak, a z drugiej strony, żeby to było w ogóle jako jakkolwiek sensowne i przydatne w AMODITcie też dla innych.

**Damian Kamiński:** Bo ktoś nas potem zapyta, a to jaka jest różnica między tym a tym, i my sami nie będziemy umieli odpowiedzieć.

**Janusz Bossak:** Tak więc trzeba taką trochę analizę biznesową zrobić, nie? Czym się różni to od tego i czy dają się wykorzystać na przykład tego AMODIT Talka. W tej chwili takim jak on jest. Do tych ogłoszeń, no bo to idealnie się nadaje do tego, żeby nie wiem, wydać monitor czy wydać łóżka, których jest za dużo. Tak, robię grupę, pojawia się, ktoś może dyskutować i pisać "nie, to nie o to chodziło" i tak dalej.

**Damian Kamiński:** Znaczy to bym widział w kontekście właśnie takich ogłoszeń, które mają nie mieć dyskusji, ewentualnie już abstrahując... o co chodzi w firmie, tak? Powstał nowy regulamin jakiś i tutaj jest link i każdy dostaje takie powiadomienie w ramach systemu. No to jest jakaś alternatywa dla maili, to jest skuteczniejsze, to ja już tego nie oceniam. To jest kolejne gdzieś narzędzie, które trzeba przeglądać, więc dla jednych będzie to wygodniejsze, bo będą tu jakieś tylko rzeczy związane z AMODITem, a dla drugich mniej wygodne, bo wolą mieć wszystko na mailu.

**Łukasz Bott:** No jak na razie słuchaj, jak na razie praktyka chyba pokazała, że niewiele firm korzysta z tego mechanizmu newsów, z tego obecnego starego, nie?

**Damian Kamiński:** Niemniej.

**Łukasz Bott:** A przy okazji on nam wychodzi, zawsze jest tak jak w GO... podatny, ale to już jest kwestia technologiczna.

**Damian Kamiński:** Dobra, mamy mockup według mnie, który jest sensowny, każdy już widzi mniej więcej jak będzie to wyglądać. Trzeba to pokazać, skonfrontować to z AMODIT Talkiem, czyli trzeba Mateusza poprosić, żeby przygotował tego AMODIT Talka na jakąś prezentację. I pokazać mu jedno, drugie, powiedzieć, że w zasadzie można pokryć funkcjonalności obu tych rzeczy jednym narzędziem, tym AMODIT Talkiem. W zasadzie to ująć w Talku i pytanie, czy to im wystarczy i może z tego zrezygnujemy. Przynajmniej no na razie może taka potrzeba się gdzieś tam jeszcze w przyszłości zrodzi. Ja bym na tym zamknął tą dyskusję, przeszedłbym do kolejnej kwestii. Czyli powiadomień, miejsca składowania powiadomień systemowych. Czyli jeśli wychodzi jakiekolwiek powiadomienie z Workflow, to jego treść, odbiorcy i czas... według WIM-u powinien być po naszej stronie zanotowany. Z Piotrem już wstępnie o tym rozmawialiśmy. Ja zaraz odnajdę to zgłoszenie, ono gdzieś gdzieś jest na górze. I będę od razu spisywał konkluzje z tej dyskusji. Natomiast z tego, co z Piotrem rozmawialiśmy, to musiałoby być włączane na poziomie pojedynczego procesu. Pytanie, co z zapychaniem się, czy jakkolwiek czyścimy tą tabelę? Czy to ma być nie wiem, jakiś parametr w ustawieniach systemowych? No otwieram dyskusję, co sądzicie na ten temat?

**Łukasz Bott:** Rozumiem, że punktem wyjścia jest potrzeba tego, żeby coś w rodzaju takiego śladu audytowego, tak? Że taki mail po prostu kiedykolwiek wyszedł. Wiemy do kogo, kiedy i o jakiej treści. Tak, to siłą rzeczy trzeba to pewnie permanentnie rejestrować.

**Damian Kamiński:** Tak.

**Łukasz Bott:** No nie może być to w tabeli Notification, która jest czyszczona, nie? Bo to jest taka typowo techniczna kolejka, tylko po to, żeby ten mechanizm wysyłki działał. Więc trzeba by to było pewnie kopiować do odrębnego zasobu.

**Anna Skupińska:** Mhm.

**Łukasz Bott:** Przy tej okazji to w ogóle trzeba było się zastanowić, być może o wyodrębnieniu jakiejś struktury w AMODITcie, która by w ogóle przechowywała tego typu rzeczy. Właśnie to zaraz pod to się kwalifikują logi systemowe, też nie wiem, logi z monitora wydajności, mamy trochę takich rzeczy, które byśmy chcieli.

**Damian Kamiński:** Nie, nie, nie, to poczekaj, nie, nie, nie wchodźmy tak głęboko. To jest odrębna rzecz, która... oczywiście każda z nich masz rację, że może być logowana, ale mówimy tutaj tylko i wyłącznie o mailach i tu już wtedy na dyskusji wyszło nam tak... w sumie mamy już coś spisane: "w ustawieniach procesu, ustawienie logowania, mailingi systemowe, forward, dodanie CC, SendMessage i przypomnienia, dodatkowo checkbox 'loguj z treścią maila'". Co logujemy? Data, do kogo, tytuł, treść, typ, czyli z czego wynika?

**Damian Kamiński:** Z takiego zdarzenia rodzaj, czy to jest indywidualny, czy zbiorczy, czy to jest wynikające z ustawień konta (czyli czy ktoś sobie oznaczył, że to jest w ramach powiadomienia z całego dnia wszystkich powiadomień), czy w ramach pojedynczego workcase'a no i case'a, z którego to wynika? No ja już też nie pamiętałem, że tu tyle wypisaliśmy, więc...

**Piotr Buczkowski:** Znaczy ten mechanizm rejestrowania wejść, pobrania dokumentów czy coś, no to to jak najbardziej do tego trzeba dodać tak. Kolejne jakieś tam kategorie. To jak najbardziej to pasuje.

**Damian Kamiński:** OK. Bez czyszczenia tego, zostaje tak jak historia na wieczność.

**Piotr Buczkowski:** No nie no tak tego nie czyścisz, tak tak.

**Janusz Bossak:** Dobra, słuchajcie, ja muszę się przełączyć, bo Justyna mnie tam potrzebuje, także działajcie. Na razie.

**Damian Kamiński:** Dobra to dopiszę też może.

**Piotr Buczkowski:** To jest ten sam mechanizm, tylko trzeba go rozszerzyć tak o tę... o kategorię kolejną.

**Anna Skupińska:** Ja też muszę niestety kończyć, to cześć.

**Damian Kamiński:** Cześć. Dobrze, Piotr, czy to jesteśmy w stanie komuś przekazać, czy ty będziesz się tym zajmował?

**Piotr Buczkowski:** Pewnie jesteśmy.

**Damian Kamiński:** No to musimy wytypować jakąś osobę, to może jutro na Daily.

**Piotr Buczkowski:** Znaczy, ja to znaczy to robił Adrian, ale pamiętam ten mechanizm, ja tam nie do końca go znam, tak? No ale trzeba, trzeba. Ja po prostu muszę się przyjrzeć jak to jest, czy wymaga jakiegoś rozszerzenia, coś coś inaczej zrobić, tak. Czy dodać jakieś coś do bazy danych czy coś...

**Damian Kamiński:** No dobra, to tu już będziesz to jeszcze weryfikował na przykład przed jutrem?

**Piotr Buczkowski:** Tak, jeszcze zweryfikuję.

**Damian Kamiński:** No dobra, to skup się na tym, tak, co logujemy w kontekście właśnie tego, co do bazy ma trafić i ustaw to na "Ready to do". Możesz przypisać do mnie i jutro to komuś przekażemy, żeby to ja wrzucę to na ten sprint. Żeby to już produkować, no żebyśmy się z tym wyrobili.

**Piotr Buczkowski:** Mhm. No dobrze.

**Damian Kamiński:** Dobra. Skończył nam się czas, nie wiem czy coś jeszcze mamy. Ja nie zdążyłem wczoraj skończyć tego repozytorium.

**Łukasz Bott:** Wiesz co? Damian, przejrzyj tę listę "Rada architektów na bieżący sprint", bo tam jest kopa zgłoszeń twoich, czy to były tworzone przez ciebie, czy przypisane do ciebie. Być może nad niektórymi myśmy już dyskutowali więc to odepnij.

**Piotr Buczkowski:** Zgłoszenie 21681.

**Damian Kamiński:** 16 nie ma.

**Piotr Buczkowski:** Nie ma tutaj, nie jest napisane. 21681. Nie wiem, pamiętacie kto to projektował?

**Damian Kamiński:** Kamil.

**Piotr Buczkowski:** Że zakładka "Do wykonania" tylko ze wszystkich procesów powinna być tak wyodrębniona. Jeżeli nie ma "Wszystkie procesy", to którą zakładkę "Do wykonania" ma pokazywać?

**Kamil Dubaniowski:** No to też "Wszystkie procesy" w takim wypadku, bo to o to chodziło, żeby jakby tą zakładkę "Do wykonania" z całego AMODITa wyjęć przed nawias. Więc jeśli obszar jest wyłączony, to mimo to, ta zakładka powinna zostać.

**Piotr Buczkowski:** Ale co ma w niej być dostępne?

**Damian Kamiński:** To co w zakładce "Wszystkie do wykonania" we wszystkich procesach.

**Kamil Dubaniowski:** Tak. Tak, czyli wszystkie zadania z wszystkich procesów, niezależnie od obszaru. Tak jakby był obszar "Wszystkie procesy", tylko ktoś uznaje, że nie chce tego obszaru "Wszystkie procesy", a no teraz jak to się wyłączy to znika też zakładka "Do wykonania" ta globalna, a ona miała być trochę od tego niezależna. Czyli ktoś nie potrzebuje obszarów "Wszystkie procesy", bo tam jest taki śmietnik i po prostu lista przypiętych raportów jakaś mega długa, nie chce tego ktoś, no ale to skutkuje [tym, że] też znika mu zakładka "Do wykonania", a powinna zostać w tej sytuacji.

**Damian Kamiński:** Dobra, ma być widoczna zawsze niezależnie od włączonych [obszarów].

**Piotr Buczkowski:** Ale ma działać jako zakładka z "Wszystkich procesów" nawet jak obszar jest wyłączony?

**Kamil Dubaniowski:** Tak, tak.

**Piotr Buczkowski:** Nie, bo ja pamiętam specjalnie oprogramowywałem tak, że jak "Wszystkie procesy" wyłączone, to nie pokazuj.

**Damian Kamiński:** To nie wiem o co chodziło.

**Kamil Dubaniowski:** OK, no to nie to, to gdzieś nam to umknęło. Właśnie no no bo ja chciałem sobie wyłączyć, bo w ogóle nie korzystam z tego obszaru, ale jak najbardziej korzystam z tej globalnej zakładki "Do wykonania", no i ona mi nagle zniknęła, a cel był [inny].

**Piotr Buczkowski:** Bo tam też jest taki mechanizm, że wybierz bieżący obszar. No to on wybiera tylko z dostępnych. Tak no dobrze, to cięcie, to też jakoś specjalnie traktować te wszystkie procesy w zakładkę.

**Damian Kamiński:** Czyli tak, to jest chyba jasne tak? "Do wykonania" główna ma być widoczna niezależnie od włączonych obszarów i wyświetlać treść taką jak zakładka "Do wykonania" w obszarze "Wszystkie procesy".

**Piotr Buczkowski:** Czyli tak naprawdę bez sprawdzania procesów.

**Kamil Dubaniowski:** Tak.

**Piotr Buczkowski:** Dobrze, weź tam jest tam... in Design się tam zmieni, czy Ready to do?

**Damian Kamiński:** To do. Dobra. Ja nie wiem czy to jeszcze powinno wisieć. Tu jest jeszcze Piotra. Aha, bo to była twoja propozycja z tymi... OK. To w sumie omawialiśmy, ale chyba nie na teraz to. Dobra, zostawmy to na razie. Wyświetlanie grup, to to jest do zdjęcia. Wprowadzenie kontroli do reguł... to jest do zdjęcia. To też jest wyjaśnione, to w sumie jest do zamknięcia.

**Łukasz Bott:** To zdaj mi ten tak raz jeszcze.

**Damian Kamiński:** A tu to Łukasza.

**Łukasz Bott:** To moje tam, to znaczy 2 zgłoszenia są tam zrealizowane tak, bo dotyczą tych ustawień tych wartości, filtrów domyślnych. Czy tam wartości domyślnej dla filtrów raportów, a tam dużo rzuciłem w ogóle jakoś taką listę różnych tam pomysłów. No to może na kolejnej Radzie przedyskutować.

**Damian Kamiński:** Dobra, to też na kolejnej. Kluczowe powiadomienia, bo to...

**Łukasz Bott:** Nie są [pilne].

**Damian Kamiński:** To jest dobry pomysł, ale to nie jest pilne. To nie jest pod WIM, to jest Janusza. I tu jeszcze coś Piotra. "Osoba wykonująca akcję na sprawie jako współpracownik powinna zachować dostęp do odczytu do sprawy, gdy przestanie być współpracownikiem".

**Piotr Buczkowski:** To jest ma być takie jak...

**Damian Kamiński:** No ja uważam, ja tu uważam, że chyba powinna akurat.

**Piotr Buczkowski:** Znaczy to tutaj pytanie, czy jest tak jak zastępstwa, czy nie, bo w zastępstwie to się włącza na procesie.

**Damian Kamiński:** A no to jeśli byłoby włączalne, to też spoko.

**Piotr Buczkowski:** Taka była odpowiedź Janusza, że powinno być dokładnie tak samo jak na zastępstwo, bo w sumie to będzie ten sam mechanizm, tak.

**Damian Kamiński:** No dobra, mam to od razu notować?

**Piotr Buczkowski:** Tak możesz, znaczy, poczekaj to może być... Ja mogę wpisać odpowiedź.

**Damian Kamiński:** A no to jak jest to wpisuj. Już stąd wychodzę.

**Piotr Buczkowski:** Które to było zgłoszenie?

**Damian Kamiński:** 21722. No dobra, to chyba możemy nad tym dzisiaj skończyć. Będziemy kontynuować resztę w czwartek.

**Łukasz Bott:** Na razie.

**Damian Kamiński:** To dzięki miłego dnia, cześć.

**Kamil Dubaniowski:** Cześć.
