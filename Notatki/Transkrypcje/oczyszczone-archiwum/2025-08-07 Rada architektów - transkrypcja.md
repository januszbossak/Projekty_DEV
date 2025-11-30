Data spotkania: **7 sierpnia 2025**

**Janusz Bossak:** Dobrze, że ta dyskusja się wywiązała, bo jak widać, jest wiele różnych aspektów do przedyskutowania – ten aspekt rejestru companies [firm] i w ogóle obsługi, tak jak Łukasz jeszcze podał, wielu spółek-gości. To jest zupełnie odrębny temat. Trzeba się nad tym zastanowić i to opracować. Natomiast wróćmy na ziemię i do tego, co robi Przemek, co [Kamil?], w czym ewentualnie Adrian ma pomóc, jeśli chodzi o backend. Musimy znaleźć MVP. Czyli co my chcemy minimalnie zrobić, żeby to się nadawało do używania, a później będziemy to dalej rozwijać, przerabiać i powiększać.

**Janusz Bossak:** Może ja podsumuję wnioski z tej dyskusji, o ile dobrze zrozumiałem. Jeżeli zgadzacie się na ten mój pomysł, to proponuję, żeby w tej drugiej kolumnie nie było od razu widać wszystkich potencjalnych integracji, tylko żeby tutaj były dodawane te integracje, które chcę skonfigurować w tej instancji AMODIT-a. Wybieram sobie po kliknięciu „Nowa” – czy „Skonfiguruj nową”, czy „Dodaj nową” – z listy standardowych. Mam przycisk dodatkowy „Skonfiguruj własną”. Jak wybieram „Skonfiguruj własną”, to pojawia się to, co teraz widzimy, na przykład Custom CRM, tak że mamy jakieś parametry i tu jeszcze mogę sobie dokonfigurować. Jeżeli uznam, że potrzebuję jeszcze jakichś parametrów, to w tym miejscu mogę to zrobić. I na tej liście w drugiej kolumnie będę widział tylko i wyłącznie te integracje, które są aktualnie skonfigurowane i których używam. Tak?

**Damian Kaminski:** Ja jestem za. Czyli w rozwiązaniach „Skonfiguruj własną” lub też wszystkie te, które tu mamy wymienione, w ładny sposób zaprezentowane w formie grafiki i krótkiego opisu.

**Piotr Buczkowski:** Czyli „Nowa” to jest wybór: albo standardowa, albo niestandardowa, tak? OK.

**Kamil Dubaniowski:** Trzeba by pewnie wyłapać to tak, żeby zachować kompatybilność – te, które klient już ma jakoś pouzupełniane, żeby one domyślnie były na liście, byle nie zginęły.

**Damian Kaminski:** Wiesz co, ja bym powiedział tak: w MVP po prostu możliwość usunięcia. I tak musimy to zabezpieczyć, więc potem ktoś może wejść i usunąć. Możemy jako kolejny element ustalić to, co powiedziałeś: jeśli nic nie jest wypełnione, to usuwamy to z listy.

**Janusz Bossak:** Przyjąłbym takie założenie, że jeżeli dana integracja ma skonfigurowane parametry – nawet nie w całości, że ktoś zaczął konfigurować, ale nie dokończył – to się pojawia. Jeżeli jest „czysta”, czyli nie ma nic skonfigurowanego, a coś powinno być, no to się tu nie pojawia. Integracja, która nie wymaga żadnej konfiguracji, a istnieje – tego chyba tu w ogóle nie mamy uzgodnionego. Mówię właśnie o tych kursach walut, VIES-ach, jakichś tam GUS-ach i tak dalej, które nie wymagają żadnej konfiguracji, a istnieją. To ja bym też tutaj pokazywał.

**Damian Kaminski:** Ale ja bym ich chyba nie instalował. Ja bym dał to na górze jako stałą pierwszą pozycję, po prostu „Integracje wbudowane” – może to jest właściwe słowo. Po kliknięciu, w tym środkowym oknie, pojawia nam się tak jak z tej listy „Nowa”, czyli ikonka i krótki opis co to jest, jak to działa i tyle. Bo tam nie ma co konfigurować, więc głupio by było, żeby to była taka pozycja i na środku nie wiadomo co – chyba że opis na środku wtedy.

**Janusz Bossak:** Masz może gdzieś pod ręką ten projekt z Krystianem [projekt Krystyny]? Nie twierdzę, że mamy go wykorzystać, ale chodzi o to, żeby większość osób też na to spojrzała. Tam właśnie były te rzeczy, o których tutaj rozmawiamy. Nie twierdzę, że cały ten projekt Krystyny należy zrealizować, ale na pewno wieloma elementami można się zainspirować, bo te dyskusje już wtedy były. Pamiętam, z Krystianem, z Adrianem i z Kamilem dyskutowaliśmy i ten mockup gdzieś tam powstawał, więc może warto z niektórych przynajmniej elementów w tym momencie skorzystać. A jakbyś Piotr mógł rozszerzyć, żeby wytłumaczyć większemu gronu – co to są osobne integracje, czy to są konfiguracje pod integrację z systemami?

**Piotr Buczkowski:** To jest konfiguracja pod integrację. Chodzi o logowanie. Możecie pokazać obecne ustawienia?

**Lukasz Bott:** Czyli pierwsze, to byłoby podobne do tego, co w tej chwili mamy – ten edytor nazwanych połączeń do baz danych? Takie repozytorium?

**Piotr Buczkowski:** Tak, tak.

**Janusz Bossak:** No i to właściwie też by się przydało do tych integracji włączyć – to, co jest teraz w ustawieniach bazy danych.

**Piotr Buczkowski:** Wejdź na integracje, na „Poczta przychodząca”. Tylko tyle, nic nie masz w tym wygórowanego.

**Janusz Bossak:** Taka poczta przychodząca też powinna być w integracjach. Też jest integracją.

**Lukasz Bott:** Poczta wychodząca tak samo. Active Directory też.

**Piotr Buczkowski:** Dobrze, po pierwsze: żeby nie trzeba było takiego wpisu dlaczego [connection stringa] wpisać, tylko po prostu wpisujesz te 3-5 parametrów. A po drugie: dla każdego takiego czegoś możesz definiować token. I na przykład tutaj tylko wybierasz, że logujesz się tym wybranym tokenem, który się generuje na podstawie tego ustawienia. To jest poczta przychodząca, ale tak samo, jeżeli dla Microsoftu jest tutaj, to takie samo można wpisać tylko z odpowiednimi danymi z Microsoftu.

**Janusz Bossak:** Czy będzie to to, co też tutaj mówi Piotr i to, co wspomniał Łukasz? Ogólnie te ustawienia systemowe się zmienią, bo wiele rzeczy trafi pod hasło integracji. Bo czy Active Directory to jest integracja? Tak. I teraz jest kwestia decyzyjna: czy lepiej trzymać konfigurację Active Directory gdzieś właśnie jako specyficzną zakładkę, tak jak jest tutaj „Poczta przychodząca”? Jest pytanie, czy to utrzymywać, że mamy w ustawieniach systemowych konfigurację dla poczty przychodzącej, bo każdy wie o co chodzi.

**Piotr Buczkowski:** To jest tak specyficzne i tak duży moduł, że warto.

**Janusz Bossak:** No właśnie, tak samo Active Directory.

**Lukasz Bott:** Active Directory jest związane ogólnie z uwierzytelnianiem użytkowników. Więc ja nie mówię, że nie – możliwe, że faktycznie trzeba, tylko może powinno być to bardziej, w starym interfejsie, jako odrębna zakładka „Uwierzytelnianie użytkowników” i wszystkie te kwestie związane z uwierzytelnianiem tam wyłączyć.

**Piotr Buczkowski:** Dobrze, to może jeszcze powiem, jak ja widzę te integracje. Definicja tego: po pierwsze dodajesz aplikację (OAuth). Dziś definiujesz te 5 parametrów. Plus, dla tej aplikacji możesz wygenerować ilość tokenów, ile chcesz. A później, na przykład tutaj, tylko wybierasz token. Nie masz tych 3 [parametrów], tylko od ciebie zależy – musisz wybrać token, który zdefiniowałeś, na przykład dla Microsoftu czy dla Google’a. Już nie będzie takich 3 [parametrów], tylko jeden Auth Token.

**Janusz Bossak:** Te ustawienia systemowe, to co zrobił Przemek, widać, że są różne od tego, co jest teraz. One i tak wymagają uporządkowania i to takiego głębokiego. Nawet teraz, jak patrzę na to, co Przemek zrobił – tam się pojawiło Autenti, ale oprócz Autenti mamy na przykład DocuSign. Może to powinno być dzielone według zastosowań? Czyli integracje z systemami do podpisywania – i mamy Autenti, DocuSign, AMODIT Trust Center. Może coś tam jeszcze będzie, jak integracja z systemami przechowywania dokumentów: SharePoint, KSeF [?], Alfresco. Może tak to trzeba podzielić, żeby była jakaś logika biznesowa, jak np. e-Nadawca i e-Doręczenia obok siebie, a jakiś ePUAP czy coś w tym rodzaju obok.

**Adrian Kotowski:** Kategorie integracji.

**Janusz Bossak:** Bo tak to jest tam pomieszane: jest Autenti, jest Trust Center, e-Doręczenia i taka niewiadoma właściwie.

**Kamil Dubaniowski:** No, wpadają w takiej kolejności, jak dodawaliśmy.

**Janusz Bossak:** Wtedy realizujemy tę opcję, o której tutaj też mówiliśmy – że mamy integracje związane z użytkownikami i wtedy tam byłoby to Active Directory czy na przykład integracja przez bazę danych, bo też mamy taką, że użytkownicy czy inne informacje są synchronizowane przez bazę danych. I czemu to nie miałoby być tutaj? Mamy tę zakładkę a propos „Baza danych” i tam trzymamy ten Connection String. Connection String jest też elementem integracji, tyle że innym sposobem – nie przez API, tylko przez bazę danych, więc to kojarzy się z integracją. Pytanie, jak to uporządkować, żeby to miało ręce i nogi, żeby to było zrozumiale dla użytkownika, żeby wiedział, gdzie czego ma szukać. Wywołałeś Kamil bardzo poważny temat z tymi integracjami. Nieprosty. Albo na zasadzie MVP po prostu w Reactcie odwzorowujemy to, co mamy teraz i tyle – tyle że jest trochę ładniej.

**Kamil Dubaniowski:** Tak, nawet więcej, bo dodajemy te opcje konfiguracji i dodawania parametrów z poziomu interfejsu, a to już jest też duży plus dla konsultantów, bo często nie ma tego dostępu do bazy.

**Janusz Bossak:** I według mnie tego się chyba powinniśmy trzymać – takiego MVP – i to uruchomić, żeby w ogóle zaczęło funkcjonować. A potem, mając już to, trzeba uruchomić – nie wiem, w kolejnym kwartale czy w przyszłym roku – projekt reorganizacji ustawień systemowych i wtedy to dzielimy, ustawiamy w innych miejscach. Pełna reorganizacja, dodanie funkcjonalności i tak dalej. Ale na razie powinniśmy iść taką ścieżką MVP absolutnie, bo inaczej tego nie dowieziemy w jakimś sensownym czasie.

**Kamil Dubaniowski:** W międzyczasie znalazłem to, co kiedyś proponowała Krystyna. Trzeba by pewnie było podzielić... To był pomysł tego Marketplace, gdzie możesz sobie coś „dokupić” i to było już tak wysoko.

**Damian Kaminski:** Kamil, weź wejdź na to z czata, jeszcze otwórz sobie w drugiej zakładce. W międzyczasie to wyklikałem. Nie jest jeszcze to ładne z grafikami, coś tam się rozjechało, ale...

**Janusz Bossak:** To jeszcze zauważcie proszę – tam były te „Raporty zaawansowane”, co nie jest integracją, jest modułem. Bo to też bym rozróżniał: integracja to jest integracja, czyli z czymś się łączymy, a moduł jak „Raporty zaawansowane” – to on się tu akurat nie nadaje.

**Damian Kaminski:** To powinno być w licencji, a nie w zakładce po lewej stronie.

**Janusz Bossak:** Ale już KSeF czy właśnie ten OpenAI czy „VAT-owcy” [Biała Lista] – to jak najbardziej, to są integracje.

**Adrian Kotowski:** Jeśli to można by wskazać, że jakaś integracja wymaga licencji, np. czy to się wiąże z abonamentem.

**Kamil Dubaniowski:** To jest w planach, że to wręcz pozwala ci wygenerować jakąś prośbę o licencję do działu handlowego.

**Damian Kaminski:** No to w zasadzie mojego linku możesz nie odpalać. Ja przygotowałem w międzyczasie w v0 [Vercel v0] dokładnie to, co teraz pokazało się. Jak to jest zwizualizowane i jeszcze ma grafiki, tak jak tutaj, to jest bardzo ładne, to co Kamil pokazał, i według mnie tak to powinno wyglądać. I to się po prostu sprzedaje.

**Janusz Bossak:** Tak. To jest według mnie dobry projekt. Nie twierdzę, że on jest taki jeden do jednego do przełożenia, ale koncepcje i elementy w nim zawarte są jak najbardziej słuszne. Może odszedł zbyt daleko i pewnie tego nie wykorzystamy – tego, że od razu mogę kupić czy wysłać prośbę do Astrafoxu – ale samo uporządkowanie uważam za słuszne. Musimy zwrócić uwagę jeszcze na jedną rzecz – my ten system sprzedajemy, co oznacza, że konsultanci czy handlowcy to prezentują. Mając taką „podkładkę” elegancką: „Proszę bardzo, zobaczcie państwo, szanowny kliencie, ile mamy integracji, a jeżeli jakiejś integracji nie ma, to mogą państwo sobie kliknąć Dodaj i skonfigurować własną”. To jest zupełnie inna forma sprzedaży, bo pokazuje, że jest to całkowicie opanowane. Integracji wbudowanych mamy, nie wiem, 20, a jeżeli nie ma tutaj jakiejś, a mają państwo jakiś swój własny system, to proszę bardzo – jedno kliknięcie, dodają państwo parametry. Mało tego, można właśnie wybrać jakiego typu to będzie konfiguracja – czy przez API, czy przez bazę danych (wpisujecie państwo Connection String).

**Kamil Dubaniowski:** Tak jest.

**Janusz Bossak:** Dzięki temu inaczej się to sprzedaje. Nawet dyrektor finansowy zrozumie, o co chodzi – że tu mogę wejść i sobie szybko, łatwo skonfigurować.

**Janusz Bossak:** Dobra słuchajcie, żeby nie przedłużać. Idziemy w kierunku wersji MVP. Kamil i Przemek – to co zrobiliście jest OK. Upraszczamy tą drugą kolumnę w ten sposób, że: po pierwsze – pierwsza pozycja to są integracje wbudowane i tam siedzi wtedy ten VIES, kursy walut, Biała Lista, bo tego nie trzeba konfigurować. Druga część to są integracje, które są wbudowane, ale wymagają konfiguracji – i te powinny się na tej liście w drugiej kolumnie pojawiać tylko wtedy, gdy zostaną skonfigurowane, a normalnie siedzą pod guzikiem „Dodaj integrację”. I też w tej drugiej kolumnie pojawiają się integracje własne, customowe.

**Piotr Buczkowski:** Tylko to się używa w integracjach. O to mi chodzi.

**Janusz Bossak:** Tak, trzeba to przemyśleć, jak wpleść to, co mówił Piotr. Czy to powinno być w tych integracjach, czy to raczej powinna być właśnie osobna zakładka do definiowania, tak jak teraz jest zakładka do definiowania tych Connection Stringów – to mi bardziej pod to podchodzi.

**Adrian Kotowski:** Interesuje mnie jeszcze ten szybki wątek. Mamy taki panel zasobów chronionych [Azure Key Vault?], gdzie trzymamy te dane. Według mnie tam jest takie dość specyficzne, utrudnione wejście do tego widoku. Nie wiem, czy może byśmy ewentualnie rozważyli, żeby ten przycisk umieścić gdzieś w tym widoku integracji? Bo to jest skonfigurowane w e-Doręczenia...

**Janusz Bossak:** Możliwe. No właśnie, czy w jakiejś zakładce pod tytułem „Bezpieczeństwo”? Może powinna być osobna zakładka „Bezpieczeństwo” i tam to powinno siedzieć. Ale znowuż – słuchajcie, panowie i panie – MVP i „dowozimy”. To są nasze najważniejsze hasła na dzień dzisiejszy. Ten temat wstrzymuje nam w ogóle publikację ustawień systemowych na tym etapie.

**Kamil Dubaniowski:** Tak, bo to jest jedyna niezrobiona zakładka.

**Janusz Bossak:** Więc te dwa hasła nam przyświecają: „dowozimy”. A sposobem na dowiezienie jest MVP. Mamy to wszystko w głowie, wiemy jakie piękne różne rzeczy moglibyśmy zrobić, natomiast dowozimy minimalną rzecz, która jest niezbędna, żeby można było z tego korzystać.

**Kamil Dubaniowski:** Ok, czyli rozszerzamy tak naprawdę to tylko i wyłącznie o to, żeby na liście nie pokazywały się te [integracje], których klient nie używa. I dodajemy ten panel do potencjalnego pokazania – tak ładnie wizualnie z opisem, że to możesz sobie włączyć. Zmieniamy nieco sposób dodawania nowych, ale baza zostaje – nadal korzystamy z Parameters na ten moment.

**Janusz Bossak:** Chodzi mi jeszcze o wykorzystanie AI do tworzenia tych nowych integracji. Czyli jeżeli dostaję jakąś specyfikację REST API, endpointów i tak dalej – czy dając link do tego sztucznej inteligencji, ona sama by „wyczaiła” jakie parametry, jaki sposób logowania trzeba by skonfigurować, żeby to działało? No i to jest zadanie oczywiście nie w ramach tego MVP, ale takiego trochę „MVP rozszerzonego” i tej całej naszej ścieżki używania AI w różnych miejscach na ułatwienie dla integratorów i konsultantów. Czyli dostaję jakieś API, trzeba się z tym połączyć, wrzucam tam link do Swaggera i mówię: „tu mi weź przygotuj konfigurację parametrów”. I on tam wymyśla, jakie powinieneś mieć tutaj parametry, żeby się z tym zintegrować. Super sprawa.

**Adrian Kotowski:** No teraz przydałoby się... Mamy teraz Copilota, jest w momencie tego core'a [?]. Mamy i przykład, dokumentację, mamy też właśnie dobrze opisany kod. Ja myślę, że tu można by łatwo takie wynikowe wypluwać.

**Piotr Buczkowski:** Znaczy tam nie jest tak, że dowolna lista parametrów, tylko ze zdefiniowanej listy parametrów, bo ileś tam tylko obsługujemy.

**Adrian Kotowski:** Tak, no tam już wsadziłem przykład jak to można wyszukiwać, jak te parametry są interpretowane. Myślę, że tutaj pewnie sobie da radę, skoro jest ten model językowy. Już tam jest jakby wrzucony ten opis taki „ludzki” tej dokumentacji. To nie jest jakieś trudne zadanie.

**Damian Kaminski:** Ja jeszcze mam krótkie pytanie, żebym nie musiał pisać. Słuchajcie, jest tak: pod takim linkiem jest dostępna ta cała lista helpa. Takie pytanie od klienta: czy mogę to jakkolwiek mu wyciągnąć, żeby on miał w formie jednego ciągu, pliku, _add command_ [?], niżej kolejny?

**Janusz Bossak:** Za przeproszeniem, po jaką potrzebę?

**Damian Kaminski:** Nie pytaj mnie.

**Janusz Bossak:** Odpowiedź brzmi: nie.

**Lukasz Bott:** Inna sprawa – moim zdaniem to, co pokazujesz, to w ogóle trzeba by było jakoś wyciągnąć sensownie w AMODIT-cie. Bo żeby do tego się dostać, to musisz przeklikać przez jakieś reguły, procesy i tym podobne rzeczy. I może to jest bolączka [WIKI? / VM-u?].

**Damian Kaminski:** Tak, tak, tak. Nie, nie, nie – oni chcą po prostu to mieć w formie jak PDF. To z plików wyciągnę, tam mogę nawet Piotrka spytać, jak to odczytać.

**Janusz Bossak:** Ale po co?

**Piotr Buczkowski:** Niech sobie jakiegoś screen scrapera zapuszczą i im to zrobi.

**Janusz Bossak:** Dokładnie. Mają to w tym naszym AMODIT Copilocie, mają to w tych plikach YAML. Możemy im dać te pliki YAML.

**Piotr Buczkowski:** Przecież to się co chwilę zmienia.

**Damian Kaminski:** Ale ja się z wami zgadzam. Tylko wiecie, ja powiedziałem jak co i dalej mam pytania. Oni są uparci i po prostu dlatego dałbym im to i powiedziałbym: każda wersja będzie miała nowe, to jest już ich problem.

**Janusz Bossak:** Jeżeli będą chcieli – wycenimy to na 15 000 zł, żeby to zrobić i tyle.

**Adrian Kotowski:** Przecież jest ten dostęp w ramach AMODIT-u, czemu po prostu nie wejść na tę stronę? Nie wiem.

**Janusz Bossak:** Uwierz mi Damian, że podawanie kwot za wykonanie pewnych prac leczy z takich pomysłów.

**Damian Kaminski:** Ja już raz wysłałem kwoty do nich, to się skończyło aferą, więc... Dobra, nie da się i tyle na razie.

**Kamil Dubaniowski:** Uciekamy, no bo już tam Lucyna wypisuje.