**Data spotkania:** 2 grudnia 2025, 11:59 - część 3

---

**Przemysław Sołdacki:** No, ale.

**Janusz Bossak:** Bo nie wiadomo jak to MCP będzie sobie wewnętrznie działał i co on tam będzie próbował odpytywać i tak dalej. Więc to, że je mamy jakieś proof of concept, technicznie da się jedno z drugim połączyć – to jest jeszcze daleka droga do produkcyjnej.

**Przemysław Sołdacki:** No tak, tylko Janusz chodzi o to, że taki Rosman o to prosi, Polpharma, AmRest – możemy im dać na środowisku testowym, bo oni na przykład powiedzą, że spoko, ale mamy 10 uwag, albo na przykład to bez sensu, bo coś tam, albo jakąś inną uwagę. To będziemy przynajmniej wiedzieli gdzie jest problem, bo tak to sobie możemy teoretyzować. Więc tą wersję jakąś, nawet taką podstawową dobrze byłoby dać.

**Janusz Bossak:** No dobrze, to możemy się tym zajmować, tylko chodzi mi o to, żeby.

**Przemysław Sołdacki:** No bo oni tam powiedzą czego im najbardziej brakuje. No bo mamy innych klientów, którzy by z tego skorzystali, nawet jako PoC płacąc jakieś minimalne pieniądze i to jest do zrobienia.

**Janusz Bossak:** Jeszcze jedna. Tak znaczy, trzeba mieć jeszcze jedną ważną rzecz na uwadze – to MCP, ten serwer, Model Context Protocol. W tej chwili to jest podłączone do AMODIT Copilot'a, to nie jest podłączone do AMODIT'a jako takiego. To znaczy, że przez MCP mogę wykonywać takie polecenia, jakie mogę robić przez samo Copilot'a.

**Przemysław Sołdacki:** I tak będzie.

**Janusz Bossak:** To nie jest podłączone, żebyśmy się rozumieli. Tak, to nie jest podłączenie pod API, gdzie ja się przez API zapytam, jakie są moje ostatnie urlopy? Nie, to jest tak, jakbym wpisał tekst do Copilot'a i Copilot mi odpowiada i ten wynik dostaniemy, a nie prawdziwe dane z spraw.

**Przemysław Sołdacki:** Znaczy, o ile ja dobrze zrozumiałem moją rozmowę z Mateuszem, to jest tak, że Mateusz robi te takie endpointy, z nich korzysta nasz Copilot i te same endpointy będą wystawione przez MCP na zewnątrz.

**Janusz Bossak:** Tak, ale.

**Przemysław Sołdacki:** Więc to nie jest pełne API, ja rozumiem i to jest dobrze, bo my wtedy możemy w tych funkcjach śledzić na przykład, że AI coś spytało i mieć w logu, że AI coś tam mieszało, albo nawet odczytywało informacje. Czyli my świadomie mówimy co my wystawiamy, a czego nie wystawiamy – nie całe API. I to jeszcze powinno działać w kontekście użytkownika, czyli mój agent, żeby spytał w moim imieniu, a nie do wszystkiego miał dostęp.

**Janusz Bossak:** Oczywiście, oczywiście. Tak, tak, tak, tak. Nie, no absolutnie, no absolutnie – to musi być właśnie.

**Przemysław Sołdacki:** Więc słuchajcie, więc ja zakładam, że te rzeczy łącznie z tym MCP też robi głównie dla filmu – i to są rzeczy, które po prostu trzeba dowieść. I rozumiem, że mamy trzeci wątek zwany Mateuszem, który się bawi tutaj rzeczami. A jeśli my to dowieziemy w tym roku to spoko. No bo rzeczywiście skrócimy sobie wdrożenia, a ja bardzo chcę zacząć mieć przychody na AI, w których mamy na razie zero. Strategia jest taka, żeby jednak mieć na przykład 10% przychodów z licencji AI. A 10% to wcale nie jest mało, bo to oznacza, że musimy na przykład kilkaset 1000 rocznie zrobić na tym, co jest możliwe. Tylko ktoś musi wiedzieć, po co kupuje to. Niektórzy klienci powiedzą, po co mi generowanie dokumentacji, wy będziecie pisać, mówię, no dobrze, ale my będziemy pisać, to zapłacicie, a tak sobie będziecie generować na podstawie tej licencji. Samo MCP powinno być dla zaawansowanych klientów, którzy chcą płacić więcej. Generowanie dokumentacji może w wersji podstawowej – do jeszcze do ustalenia. Ale jest jeszcze jeden aspekt, który chyba też z wami powinienem ustalić, jak wygląda temat – żeby AI klient, który nie kupił AI – żeby nasi konsultanci mogli użyć AI. Czyli klient nie ma załóżmy licencji na generowanie dokumentacji, ale nasz konsultant, żeby nie pisał tego ręcznie, to żeby mógł się w jakiś sposób potwierdzić, że to jest nasz konsultant i żeby mógł użyć AI, mimo że klient tego AI nie posiada.

**Janusz Bossak:** No my mamy tam takie przecież funkcjonalność. Myślę, że AMODIT ma świadomość tego, że to jest zalogowany nasz pracownik po adresie mailowym – bo AMODIT albo AstroFox PL.

**Przemysław Sołdacki:** Pod warunkiem, że się logował przez jakieś OAuth, a nie wpisane ręcznie adres e-mail.

**Janusz Bossak:** Nie wiem, bo obojętnie jak wpisał.

**Przemysław Sołdacki:** No ale żeby klient nie oszukał zmieniając sobie tymczasowo adres e-mail i sobie korzystając z AI. Może nie jest to duże ryzyko, ale.

**Janusz Bossak:** A no.

**Przemysław Sołdacki:** Można by to jeszcze.

**Janusz Bossak:** Nie, nie znaczy – nasz konsultant ma założone konto u klienta. To konto tam jeszcze dawno temu było tak, że ono było oznaczane w ogóle jako serwisowe. Nie wiem czy nadal funkcjonuje czy nie. No i wtedy ktoś z takim kontem z naszym adresem mailowym, bo to było robione jeszcze w czasach, kiedy potencjalnie mieli być partnerzy i żeby partnerzy mieli takie konta serwisowe. No ale powiedzmy, że na razie pozostało przy naszych adresach, no i to można by wykorzystać ten fakt, że to jest nasz adres i wtedy możemy wygenerować.

**Przemysław Sołdacki:** Znaczy. Trzeba wykorzystać tylko, żeby właśnie nie było czegoś takiego, że klient sam sobie założył użytkownika z adresem AstroFox PL i sobie coś tam, gdzie mieszka.

**Janusz Bossak:** Musiałby wpaść, to musiałby wpaść na to.

**Przemysław Sołdacki:** Ja wiem, ja wiem, dlatego to nie jest duże ryzyko, ale na przykład jak byśmy ograniczyli, że to musi się ktoś zalogować przez OAuth, czyli na przykład naszym kontem firmowym, to wtedy tylko działa – jak ma po prostu takie login hasło to ta funkcja nie zadziała.

**Janusz Bossak:** Ale w kontekście jakiejś premiumowych użytkowników to.

**Przemysław Sołdacki:** No dobra, znaczy, słuchaj, możemy tak zrobić, że jeśli jest AMODIT albo AstroFox, to funkcje AI działają, o ile, że tak powiem, klient to umożliwia.

**Damian Kaminski:** No ale to też nie musi być automat, tylko w międzyczasie jeszcze robię co innego, się ze wszystkim wyrabiają. Można przecież zwiększyć koszty licencji – też to nie jest tak, że to musi być automat.

**Przemysław Sołdacki:** Koszty licencji.

**Damian Kaminski:** Że, bo mówisz, że jak jest chmura, to działa tak?

**Przemysław Sołdacki:** Nie chodzi o co innego, że klient nie kupił. Tak, ale chcemy, żeby nasz konsultant używał AI na przykład do generowania procesu, do pisania dokumentacji.

**Damian Kaminski:** No.

**Przemysław Sołdacki:** I żeby on mógł, ale klient sam, żeby nie mógł – dopiero jak kupi. Czyli konsultant mówi, proszę bardzo, ja tu się zalogowałem, ja mam specjalne uprawnienia, wygenerowałem dokumentację, chcecie sobie generować dokumentację? No to tam macie opłatę miesięczną i będziecie robić. No i to jest jakby.

**Damian Kaminski:** Już teraz rozumiem.

**Janusz Bossak:** No pytanie, to będziemy...

**Damian Kaminski:** Tylko żeby oni, żeby oni tego nie wyczaili w ten sposób, że sobie zmienią hasło i się zalogują, tak.

**Janusz Bossak:** No tak, no ale to musieliby się logować na konto naszego konsultanta, no to już trochę jest, wiecie.

**Przemysław Sołdacki:** No. No właśnie.

**Janusz Bossak:** Nie fer.

**Przemysław Sołdacki:** Znaczy, wiecie to – jakiś mechanizmy, w razie czego można dodatkowy zrobić, że ktoś musi jeszcze nasze wewnętrzne hasło jakieś podać, żeby to zadziałało.

**Janusz Bossak:** Natomiast. Które ryzyko jest większe, takie, że klient powie, no to jakby możecie tak łatwo generować tą dokumentację, to proszę mi – w ramach umowy serwisowej – generować dokumentację.

**Damian Kaminski:** Serwisu tak.

**Przemysław Sołdacki:** No powiemy, że tak możemy, tylko tak czy inaczej będzie opłata. No słuchajcie, ale nie ma, że tak powiem, bez dwóch zdań, my to potrzebujemy mieć i chcemy, żeby nasi konsultanci pracowali szybciej, żeby mieli gotowe takie narzędzia i to będziemy robić im kolejne narzędzia do tego. I cały przyszły rok to jest właśnie skracanie wdrożeń i zwiększanie przychodów poprzez różnego rodzaju narzędzia AI.

**Janusz Bossak:** No właśnie to że. Dokładnie.

**Przemysław Sołdacki:** I ja sprawę.

**Damian Kaminski:** No najbezpieczniejszym rozwiązaniem byłby jakiś token czasowy.

**Przemysław Sołdacki:** Coś do ustalenia, ale znaczy wiecie – na początku to nawet niech nas klient oszuka, później dodamy zabezpieczenie. Na razie zróbmy, żeby to jakoś działało, bo jest jeszcze taki aspekt, że.

**Damian Kaminski:** Nawet. No tak. Ja się przełączę, mam spotkanie z klientem, dzięki.

**Przemysław Sołdacki:** Dobra, kończymy generalnie zaraz, więc. Jakby podsumowując – robimy to, jeśli Janusz uważa, że na przykład nie wiem – te rzeczy to mają być w kolejnym sprincie. No to, żeby to było jasne, albo na przykład podzielone, że nie wiem – MCP to w tym sprincie zrobi Mateusz, a to zrobi w drugim sprincie. Chodzi mi o to, żeby był jakiś plan, żeby cały zespół wiedział, jaki ten plan jest. Tak, żebym wiedział, ale żeby zespół wiedział, bo wtedy oni mają świadomość, że OK – celem jest to, a nie coś innego. Więc minimalizują wątki poboczne. My się skupić na tym na tym sobie dowiezienia. Dalsze rzeczy to tutaj już. No tutaj MCP jest smaku jeden, ale jak się uda to zrobić to zajęliście będziemy. Rosman prosi, mówi, dawajcie nam wcześniej – będziemy testować na środowisko testowe i to, jak będziemy mieli, co damy. No dobra tyle, no bo rozumiem, że tam cały czas te prace trwają też na wykończenie brzechwy.

**Janusz Bossak:** Tak, no teraz – mówię, dzisiaj Vasco wróciło z tym tematem integracji z Google'em. To już z Mateuszem chwilę tam na Teams'ie rozmawiałem. No to mówię, żeby podłączyć po prostu – tak, ma już podłączone. No to mówi tam dzień-dwa i będzie. Natomiast jeżeli mamy wrzucić tą całą heurystykę, którą mamy teraz. Czyli tam kontrolowanie tych tabelek, sum w tych tabelkach, obliczanie VAT'u, sprawdzanie różnych rzeczy, no to już mówiłem – trochę dłużej, bo to trzeba mówić na nowo. Pod tamten model, to jak on zwraca dane – zrobić te heurystyki wszystkie.

**Przemysław Sołdacki:** Ale właśnie – tak na logikę, jeśli załóżmy Azur wychodzi w jakimś formacie, a my byśmy dostawali z Gemini'a w innym formacie – to jest kwestia transformacji do tego samego formatu, który daje Azur i wtedy reszta zadziała.

**Janusz Bossak:** No.

**Przemysław Sołdacki:** Tak, tak jakby.

**Janusz Bossak:** To nie wiem, czy to nie będzie trudniejsze niż zrobienie tych heurystyk – znaczy odwzorowanie ich po tamtej stronie. Tak, to kombinowanie.

**Przemysław Sołdacki:** Czy wiesz, to możemy zrobić najpierw tą prostą rzecz, bo możemy uruchomić Gemini'a – możemy użyć nawet tego promptu, którego oni nam dali tutaj poufnie. I i zobaczyć, czy to im rozwiązuje problem, albo zrobić to po swojemu, ale jakby zacząć od czegokolwiek. Jak oni bardzo chcą mieć Google'a, zrobimy tego Google'a, podepniemy.

**Janusz Bossak:** Znaczy ten ten prompt?

**Przemysław Sołdacki:** Gdzie my się będziemy chwalić, że nasza OCR działa na różnych modelach.

**Janusz Bossak:** Ten ich prompt i ich kierunek świadczy o tym, że oni to robią inaczej. Oni po prostu odczytują LLM'em, tak – nie modelem OCR'owym, tylko LLM'em od samego początku.

**Przemysław Sołdacki:** Wojna. Tak i tak zróbmy.

**Janusz Bossak:** No my mamy te dwa modele, czyli model inny visionowy i model do paragonów – kombinujemy najpierw z nimi jak one zwrócą niepełną informację, to modelem tam tanim tym LLM 4.1 dopytujemy o jakieś tam drobiazgi, uzupełniamy, kombinujemy z tabelkami, żeby posprawdzać te sumy i tak dalej.

**Przemysław Sołdacki:** Byłem, no ale, ale słuchaj – klient zrobił proof of concept, jemu zadziałało. Jeśli my to uruchomimy tak jak oni chcą, a najwyżej zmodyfikujemy tego promptu, żeby nam zwracał w formacie, jakim my chcemy i jak Google twierdzi, że odwołują.

**Janusz Bossak:** I to, co jest cały proces?

**Przemysław Sołdacki:** Są tańsze niż do tego jakiegoś dedykowanego modelu, to może będziemy mieć alternatywne rozwiązania.

**Janusz Bossak:** Chodzi mi tylko o to, żeby przy tych tutaj ustalaniu tych właśnie celów sprintu, no to się czasami tak okazuje – jak tutaj. Że wpada jakiś temat, który trzeba nagle robić, bo coś tam.

**Przemysław Sołdacki:** Ale to rozumiem, Janusz – to jakby jest uzasadnienie, chcemy utrzymać tego klienta. Jesteśmy w stanie przeliczyć to na złotówki. Jesteśmy w stanie, bo mamy jakiś przychód roczny od tego klienta – kilkadziesiąt 1000 rocznie. Chcemy, żeby klient pozostał, jeszcze nawet chętnie, żeby więcej płacił. Więc no tak, trzeba – zrobimy i zróbmy. Jeśli musi być na Google'u, to niech będzie na Google'u. Google się cieszy, może jeszcze coś tam mieli z Google'em. No a zawsze będziemy też się chwalić. Współpracujemy z różnymi modelami, łącznie z Google'owymi, OpenAI.

**Janusz Bossak:** Nie. Dokładnie, że to akurat uważam za dobry kierunek, żebyśmy poszli w tego Google'a i bardziej, że ten model Gemini jest naprawdę fajny i czemu nie. Tak, no skoro.
