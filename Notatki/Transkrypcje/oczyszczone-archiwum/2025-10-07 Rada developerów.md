
**Data:** 7 października 2025
**Uczestnicy:** Łukasz Bott, Damian Kamiński, Piotr Buczkowski, Kamil Dubaniowski, Anna Skupińska, Adrian Kotowski

---

## Tematy
- **LOT / Wielospółkowość:** Ograniczenie widoczności użytkowników (współwłaściciele/obserwatorzy) w ramach jednej instancji (PGL/LOT).
- **Filtr "W miesiącu":** Ukrycie wyboru roku w kontrolce filtrującej (mylący UI).
- **Grupowanie integracji:** Omówienie zmian w wyświetlaniu i grupowaniu parametrów integracji (Adrian).
- **Logowanie maili wychodzących:** Rozróżnienie momentu dodania do kolejki vs faktycznego wysłania (nowy status/kolumna).
- **Zmiana typu pola:** Dyskusja o blokadach przy zmianie typu (Feature Toggle/Ostrzeżenia).
- **Walidacja pola z maską (Telefon):** Błąd wyświetlania informacji o niezgodności z maską. Decyzja o dodaniu flagi "Wymuś zgodność z maską" do pola tekstowego.

---

## Transkrypcja

**Łukasz Bott**: Dobra, za chwilę... Inst... Wystąpienie. Dobrze. Taki mamy... takie mamy tematy. Czekam jeszcze na Damiana, czy zaczynamy? Dobra, to zacznijmy, jeżeli ten... kto dołączy w międzyczasie, a jest.
Dobra, zacznę od tego, bo mi się tak przypomniało. To jest troszkę funkcjonalność, którą zgłosił Mateusz. Ona jest troszkę w kontekście LOT-u potrzebna, bo zgłosił z tym... ten kontekst biznesowy to powinien być wcześniej. Chodzi o coś takiego, że tam akurat w LOT-cie są dwie spółki: PGL i LOT. Być może więcej później. No na razie wszystko będzie w jednym środowisku jakoś tam.
I separacja na poziomie uprawnień w **AMODIT**, czy tych funkcjonalności, które daje **AMODIT**. I tutaj jedną funkcjonalność by warto było rozważyć: czy nie rozszerzyć właśnie o możliwość, jak mamy nadawanie uprawnień dla współwłaścicieli, obserwatorów spraw - czyli gdzieś tam ktoś, kto ma dostęp do sprawy, może współwłaściciela lub obserwatora dodać. Chyba, że to się całkowicie ukryje taką funkcjonalność. No ale powiedzmy, że zakładamy, że nie ukrywamy. No to tutaj była sugestia taka, żeby te dwie listy można było - mimo wszystko w ramach danego procesu - ograniczyć do wskazanej grupy osób.

**Damian Kamiński**: Węzła struktury, tak?

**Piotr Buczkowski**: Ale w ramach prac... w ramach procesu, nie w ramach...

**Łukasz Bott**: Tak, w ramach procesu.

**Damian Kamiński**: Ale poczekaj Łukasz, bo ja tu widzę dużo szerszy kontekst i może nie tylko LOT-u. To jest celem, aby oni tu mogli wybrać tylko ludzi ze swojej firmy, tak?

**Łukasz Bott**: Wiesz co, to nawet nie jest celem, bo oni nawet jeszcze nie wiedzą, że taką opcję mają. Tak? No bo to temat dopiero jest na etapie podpisywania umowy i podejrzewam, że aż w takie niuanse to...

**Piotr Buczkowski**: Chodzi o to, żeby nie można było kogoś niewłaściwego tutaj dodać, tak.

**Łukasz Bott**: Tak, to jest... tak, tak, to jest bardziej, że ta funkcjonalność a nuż się przyda. I to zgłoszenie jest takie trochę jakby profilaktyczne, a nie rozwiązujące dany problem tak mrocznie.

**Piotr Buczkowski**: Czyli to nie może być grupa osób, tu musi być jakaś walidacja kogo dodajemy.

**Damian Kamiński**: Trzeba się... nie wiadomo. Ja bym powiedział, że to jeszcze chyba za wcześnie definiujemy faktycznie potrzebę. Bo ja tu widzę szerszy kontekst. Tak mi się wydaje, że to tak czuję, że tak jak mówisz - są dwie spółki i w Orlenie jest podobne wyzwanie, za chwilkę może być. I ogólnie ta wielospółkowość. Czyli żeby ktoś nie mógł przekazać sprawy do kogoś z innej części struktury, albo nie udostępnił tej... Żeby dało się ograniczyć widoczność użytkowników tylko do mojej spółki na przykład. Ale też pewnie nie wszystkim, bo znowu są HR-y, które są te...

**Łukasz Bott**: No tak.

**Piotr Buczkowski**: Tak, ale jest... z mojej spółki do spółki Centrum Usług Korporacyjnych (**CUK**) w Orlenie na przykład, tak?

**Damian Kamiński**: O właśnie, tak. Że Centrum widzi wszystko, czyli pojedynczy użytkownicy mają wgląd we wszystkich, ale pozostali poruszają się nie tylko we "współwłaścicielach", ale w "przekaż do", w polu typu Użytkownik, we wszystkim co jest z tym związane - mają ograniczoną pulę odbiorców, czy pulę wskazywanych użytkowników.

**Łukasz Bott**: Akurat w polu typu Użytkownik to możesz ustawić, z której grupy mają być. Filtrowanie, nie?

**Damian Kamiński**: No nie, bo właśnie chodzi o kontekst tak jak tutaj, że z jednej spółki... to jest jeden proces dla dwóch spółek. I z jednej spółki jak ktoś jest, to może wskazać tylko tych ze swojej spółki, a z drugiej widzi tylko ze swojej. Więc to nie jest grupa. Znaczy pewnie można by **SetUserFilter** zastosować, natomiast no żeby to było po prostu...

**Łukasz Bott**: Ale to nie na... Ale to **SetUserFilters** to zastosujesz na polu typu Użytkownik, a nie na tym [panelu bocznym].

**Damian Kamiński**: No, no właśnie. Tak, zgadzam się z tobą, że to jest dużo szerzej. Bo to tak samo dotyczy struktury, która potem jest używana w raportach, czy jest używana w repozytorium. No ja bym na to spoglądał szerzej.

**Piotr Buczkowski**: Na pewno, na pewno tu nie chodzi o grupy. Biorąc pod uwagę grupy takie... rozwijając grupy jako grupy w **AMODIT**.

**Damian Kamiński**: Tak, może w... powinniśmy w... bo chyba jest...

**Piotr Buczkowski**: I nie jest to ustawienie per proces. Znaczy nie, nie per proces ustawiamy tą grupę, tylko per sprawa tak naprawdę.

**Damian Kamiński**: Znaczy, bo tak jest jakieś zgłoszenie wasze... Ja po swojemu to zinterpretowałem. Nie wiem czy to był zamysł pomysłodawcy, tak żeby to tak ograniczyć? Może Mateusz chciałby to jeszcze bardziej ograniczyć. Tylko pytanie jakie idą za tym powody.

**Łukasz Bott**: Dobra, gdzie się co... to nie mam co...

**Damian Kamiński**: Ale właśnie dla dwóch spółek i to bym rozstrzygnął. I tutaj może po stronie użytkowników powinno powstać dodatkowe pole, w którym przypisujemy jakieś węzły. Nie wiem czy to będą drugiego rzędu, czy nie chcemy tak dzielić. Po prostu można przypisać węzeł i to jest określenie spółki, do której należy użytkownik i po tym potem będzie dziedziczenie w tych wszystkich polach z użytkownikami.

**Kamil Dubaniowski**: Znaczy ja bym szedł w tym wypadku w... Możliwe, że nie wiem jak działa **SetUserFilters**, czy ma filtrowanie po strukturze? I pewnie coś takiego by się przydało, czyli że wskazuję właśnie ten główny węzeł i decyduję, czy tylko on, czy węzeł i węzły w dół.

**Damian Kamiński**: No tak Kamil, tylko to ty mówisz w kontekście powiedzmy tylko tego ekranu.

**Kamil Dubaniowski**: **UserFilter** nawet nie tego ekranu.

**Kamil Dubaniowski**: No to, to akurat do odnośnika tutaj widziałbym pewnie zamiast jakichś ustawień - bo to i tak będzie dynamiczne, jak zauważyliśmy, że zależy jaka sprawa i kto w nią wszedł - no to pewnie przydałaby się jakaś nowa funkcja **SetConFilter** [SetControlFilter] i **SetCFilter**, która będzie właśnie wpływała na te panele w sprawie.

**Damian Kamiński**: No ja bym dalej powiedział, że to jest szerzej. Że na przykład może to co ja mówię, powinno mieć wpływ. Że jeśli ktoś jest użytkownikiem, administratorem pojedynczej grupy i jest w danej spółce, to nie powinien widzieć tam użytkowników innych spółek.

**Łukasz Bott**: No właśnie, tylko pytanie gdzie tą spółkę... gdzie tą spółkę definiujesz, nie?

**Kamil Dubaniowski**: No nie mamy.

**Damian Kamiński**: Jeśli ktoś... No na poziomie użytkownika pewnie, tak? W sensie chodzi mi o to, że to co wy mówicie to jest jakieś konkretne jeden przypadek, tak? Ale jak podejść do wielospółkowości?

**Piotr Buczkowski**: Znaczy zwykle spółki to są u nas powiedzmy departamenty pierwszego poziomu.

**Damian Kamiński**: Mhm. Pierwszego albo drugiego, bo często ja wdrażając robiłem tak, że na przykład jest grupa Veolia, tak? Pierwszy i potem...

**Piotr Buczkowski**: To już... No jak zdefiniujesz w OP.

**Piotr Buczkowski**: To nie jest tak, że na przykład... No tam jest dodane tak, że bieżąca spółka... spółki są pierwszego poziomu w Orlenie? W S... przepraszam.

**Damian Kamiński**: OK, no jest inaczej. Tam nazwałem ten główny węzeł "Struktura organizacyjna" po prostu i dalej są już spółki grupy.

**Łukasz Bott**: Spółki widziałem.

**Piotr Buczkowski**: Jest chyba grupa PK, tak jako pierwsza? Pod spodem są po prostu po kolei spółki.

**Damian Kamiński**: No właśnie. No pytanie czy to powinniśmy też w jakiś sposób tam ograniczać? Może i tak.

**Piotr Buczkowski**: Znaczy według mnie powinno być właśnie rozbudować **SetUserFilter** o specjalne pola **SetCon**, tak? Ewentualnie na przykład **ForwardTo** też tak, jeżeli to coś mówił, żeby jeżeli mamy swobodne przekazywanie.

**Damian Kamiński**: No ale to wtedy trzeba by to robić z poziomu reguł, tak?

**Piotr Buczkowski**: No tak.

**Kamil Dubaniowski**: I tak myślisz to dynamicznie?

**Piotr Buczkowski**: Żeby to powiedzmy na... powiedzmy na etapie składania wniosku czy obsługi wniosku tylko ograniczasz. Jakieś przyjdzie na przykład do jakiegoś księgowości, to Centrum Usług Wspólnych czy Korporacyjnych - to tam już nie na przykład. Albo tam jest inna... Że przy składaniu wniosku tylko osoby ze spółki wnioskodawcy, tak? Czy tam osoby **CreatedBy**.

**Łukasz Bott**: Albo ograniczasz inaczej.

**Piotr Buczkowski**: A jak przejdzie dalej, to na przykład tylko osoby z **CUK-u**, czy tam...

**Damian Kamiński**: No dobra, tylko teraz idąc dalej - bo to jest rozwiązanie tego powiedzmy, tak? A teraz na chwilkę przejmę ekran. Ja będąc pracownikiem jakiejś firmy wchodzę sobie w Użytkownicy i może nie powinienem widzieć tego tak? Tylko powinienem widzieć tylko spółkę albo do niej przynależę i w jej ramach.

**Łukasz Bott**: Ale to czekaj, czekaj, czekaj. Masz ustawienia systemowe **UserProfileAccess** i to tym sterujesz co tu widzisz.

**Piotr Buczkowski**: To jest kwestia ustawienia.

**Kamil Dubaniowski**: Ustawienie systemowe.

**Damian Kamiński**: No nie, bo i tak i nie. Ale czekaj, tam mogę ograniczyć, że widzę tylko swoją jednostkę. A ja mówię o tym, że widzę swoją spółkę.

**Piotr Buczkowski**: No to trzeba może... A to tutaj definicja jest spółką, tak?

**Łukasz Bott**: Tak.

**Damian Kamiński**: No tak, oczywiście to jest definicja, to jest spółka. Ale właśnie zmierzam do tego, że tu widzę swoją spółkę, potem idąc dalej jak mam kartoteki...

**Kamil Dubaniowski**: Co to było? Jedno nowe ustawienie do tamtego ustawienia, czyli "swojej w górę".

**Piotr Buczkowski**: Jest też takie chyba ustawienie, tak?

**Damian Kamiński**: No właśnie, gdzieś trzeba by było wtedy przypisywać tą przynależność do spółki, czyli do jakiegoś węzła, który powiedzmy widzę dalej. Idąc w kontekście wielospółkowości - mamy zatrudnionych i teraz **CUK** czy inny jeszcze tam Centrum jakieś Usług widzi wszystko. A załóżmy, że raport się nazywa "Moi podwładni". Dyrektor czy Prezes spółki A widzi tutaj strukturę, ale znowu nie widzi nawet struktury spółki B.

**Piotr Buczkowski**: Bo to zależy od tego jakie sprawy może dostępne. To nie są wszystkie spółki, tylko wynika z tego jakie sprawy masz dostępne.

**Damian Kamiński**: Nie, nie. No tak, to nie jest... właśnie żeby nie było wyliczania, bo to nie jest te foldery tradycyjne, tylko to jest struktura. Żeby właśnie to nie generowało się na podstawie tego. To na 100% to jest struktura i może trzeba to zmienić. Nie mówię, że nie, może trzeba to przebudować. Natomiast no właśnie patrzymy na tą wielospółkowość według mnie globalnie, a nie przez pryzmat tylko jednej funkcjonalności. I zastanówmy się jak to zaopiekować właśnie zbiorczo, czy to nie powinno być po stronie ustawień.

**Kamil Dubaniowski**: No ale... bo to akurat... Pewnie niezależnie od ustawienia. Bo raporty opieramy o uprawnienia i tego bym nie zmieniał. Czyli to jest oparte o pole Użytkownik. Jeśli tutaj nie ma użytkowników ze spółki B, no to ta spółka B nie powinna się tu zbudować. To jest moim zdaniem do zmiany, to i to jakby nie jest zależne od żadnego ustawienia.
Co do struktury w panelu użytkowników - tak. No to mamy to ustawienie systemowe i możliwe, że ono też wymaga rozwoju. Czyli jeśli tak nie jest, no to żebym widział tylko te węzły, które są nade mną, swój i potencjalnie... No ja rozumiem, że...
Że takie przyjmujemy założenie, że spółka to jest ten drugi poziom. No to wszystkie, które podlegają pod tą spółkę - czyli pod drugi poziom - które są wewnątrz. Jak jest coś na tym samym poziomie drugim, a ja do niego nie należę, to tego poziomu już w ogóle nie widzę.
No i tak i tak teraz, żeby utrzymać kompatybilność wsteczną, musimy przyjąć takie założenie, że tak robili wszyscy, że spółka to jest no ten drugi poziom w strukturze.

**Damian Kamiński**: No i tu może powinniśmy dostawić trzeci poziom, co by było wtedy kompatybilne wstecz, bo wszyscy którzy mają zdefiniowane będą widzieć jak teraz. A tu wprowadzamy **Company** i wtedy na użytkowniku pojawia się dodatkowy parametr **Company**. I trzeba tam przypisać jednostkę.

**Piotr Buczkowski**: Nie, to bardziej trzeba byłoby, że określamy który poziom opisuje spółkę, tak.

**Damian Kamiński**: No OK, no to jak wybierzemy **Company**, to tu gdzieś jest dodatkowy "który poziom", tak?

**Piotr Buczkowski**: Albo ewentualnie tak, że no to dajemy na Departament. Że ten poziom oznacza spółkę? Tak? Że ten Departament to jest spółka, wtedy możesz dowolnie.

**Damian Kamiński**: Aha, tutaj, tak. Tutaj to ustawiamy. Że to jest spółka, prawem ustaw jako spółka?

**Piotr Buczkowski**: Tak. I wtedy to już też jakiś znacznik powinien być, tak.

**Kamil Dubaniowski**: Ale wydaje mi się, że to jakby naturalnie wychodzi, że to będzie zawsze ten drugi poziom, no bo chyba że spółka w spółce.

**Piotr Buczkowski**: No Damian mówił, że robił już na trzeci poziom, tak.

**Damian Kamiński**: Nie, nie, tak jak tu, czyli tu struktura organizacyjna, tu spółka raczej, tak. Ale no czy może być zespół grup? Nie wiem. Dzisiaj pewnie nie. Pytanie czy powinniśmy na sztywno ustawić drugi, czy jednak pozwolić to jakoś zdefiniować? Czy to jest dużo więcej pracy? No na razie rzucamy pomysły.
Natomiast, bo teraz przenosząc to na kanwę Łukasza - no wy tam mówicie, żeby już ustawiać. A może w ogóle to nie jest na ten moment potrzebne? Chyba że mówimy, że to jest przydatne w kontekście wszystkich innych procesów i naszych doświadczeń. Natomiast w kontekście LOT-u może chodzi tylko właśnie o to, co tam napisał - że są dwie spółki i żeby nie wskazać użytkownika innej spółki do podglądu do tej sprawy.

**Łukasz Bott**: Tak, tak, to jest raczej właśnie jako takie minimum zabezpieczające. No bo z rozmów wynikało właśnie tak, że no oni mają te właśnie obawy, że... Ktoś może tutaj... Może nawet może nie być kwestia tego, czy jest jeden proces wspólny dla dwóch spółek, tak? Tylko po prostu są oddzielne procesy dla oddzielnych spółek. No ale to nie znaczy, że jak puszczę sprawę według procesu dla PGL-u, tak? No to ktoś nim we współpracownikach czy w obserwatorach, nie możemy nie dodać kogoś z LOT-u, tak? No bo to...
Bo na poziomie procesu mogę zdefiniować, kto może uruchamiać, nie? Czy ci z PGL-u, czy ci z LOT-u. Tak? No to mogę sobie takie dwie nie wiem, mega grupy zrobić, tak? I użytkowników i ich tam wpisywać w uruchamiaczy procesów, nie? No to to już jakoś tam zabezpieczy. Ale nie zabezpieczy... Właśnie to jest sytuacji tak, że w tych dwóch polach w panelu prawym, tam gdzie mamy ustawienie właśnie tych dostępności dla współpracowników czy obserwatorów, no to tam nie ma żadnej możliwości filtrowania tych pól. I jako minimum to pewnie to miał Mateusz na myśli, tak? Żeby dodać. Więc może potraktujmy to jako minimum, zobaczymy jak się to będzie sprawdzało.

**Kamil Dubaniowski**: Znaczy to jest są ogólnie słuszne zdanie. No bo nie tylko do spółek to się przyda. Mam proces obiegu faktur i chcę tylko wskazać konkretną grupę, która na przykład w tym wypadku powinna być tutaj możliwa do dodania. No bo teraz to jest jeden z efektów, znaczy jeden z powodów, dla których tą obsługę współpracowników robi się na poziomie formularza w polu "tabela". Bo nie da się przefiltrować i tam jest pełna lista, więc to wyłączamy.

**Damian Kamiński**: Tak, tak, no może być tak. Tylko wiesz Kamil, czy to na pewno rozwiąże problem? Bo to nie jest jedyny powód, jest jeszcze kwestia wymagalności i tak dalej. Więc to nie jest jedyny powód. Jednak jak to mamy w kontekście sprawy w prawym panelu, no to ktoś może zapomnieć, nie?

**Kamil Dubaniowski**: A do tego ja cały czas jest tam mam przekonanie, że to powinien być typ pola **Component**, taki tak? Czyli dodaję sobie komponent "Uprawnienia" w tym miejscu na formularzu. Bo to jest też często argument, że "no ja chcę tu w tym miejscu dodać sobie pod właścicielem, czy tam pod osobą opisującą merytorycznie, to ja chcę dodawać teraz współopisujących". Ja pokazuję ten prawy panel, oni mówią, że "nie no, to nie, nie załapie". Jak ktoś kontekstu, że mam w ogóle ten prawy panel odpalić, bo dodaję tu ludzi do opisu.

**Damian Kamiński**: Masz na myśli, żeby tutaj było to, a takim aliasem? Nie polem osadzonym, tylko wyciągnięciem tego tu?

**Kamil Dubaniowski**: Tego tu, tak.

**Damian Kamiński**: Czyli nie zapisuje się to w **CaseDefinition** w jakimś **varcharze**, tylko tak naprawdę w tym polu.

**Kamil Dubaniowski**: Działa jak działa, tylko po prostu jest wyciągnięte w konkretne miejsce formularza. Może mieć określoną wtedy wymagalność.

**Damian Kamiński**: No musi mieć, bo to czasami jest niezbędne.

**Kamil Dubaniowski**: Działa jak zwykłe, tak filtr jak zwykłe pole, tak? Czyli przyjmuje te parametry, może być wymagane, tylko do odczytu na danym etapie, że już nie można. Ale wiesz kto jest, bo to też jest wada.

**Damian Kamiński**: Dobra słuchajcie, ja bym powiedział tak: to trzeba opisać wszystko, zaprojektować i to są też różne aspekty. Według mnie przejdźmy do kolejnych, żebyśmy nie stracili na to całego dzisiejszego spotkania. A to zarówno tu się z tobą zgadzam, że można było to tak obsługiwać i można by było wtedy to filtrować. Pytanie czy właśnie nie zacząć od tego, że powinno być to tu wyciągnięte, a dopiero potem te filtry? Bo jak zastosujemy filtry tu, to mało może to usprawni.

**Kamil Dubaniowski**: Nadmiarowe... od tego bym zaczął, no bo tego wymaga projekt.

**Damian Kamiński**: No dobra, no to to jest **Backend**, tak?

**Kamil Dubaniowski**: A wyciągnięcie tego, to moim zdaniem jest realne przyspieszenie wdrożeń. No bo zbudowanie takiej tabelki, zrobienie całej obsługi wysyłki powiadomień...

**Damian Kamiński**: Ja mam tylko taką obiekcję, że Mateusz coś zdefiniował, ale ja nie wiem czy my już jesteśmy na takim etapie analizy LOT-u, że to jest pewna definicja potrzeby?

**Łukasz Bott**: Nie jest. Dla LOT-u nie jest, nie, nie, nie. To jest analiza się nawet nie zaczęła, bo dopiero zacznie się chyba dwudziestego, czy tam po dwudziestym października. W tej chwili miały się zacząć wczoraj, ale są to dopiero sobie jeszcze dogrywane jakieś niuanse związane z podpisaniem umowy, więc to już się dawno 2 tygodnie opóźnia.
I co no, Mateusz tak jak mówię, ja brałem udział w tych spotkaniach, gdzie te, gdzie te uprawnienia... znaczy nie tyle rozmawialiśmy o uprawnieniach, tak w sensie takim, że to znaczy tak: Chcą zrobić właśnie obsługę - no na razie tych dwóch spółek - od strony architektury systemu będzie to jeden **AMODIT**. No i gdzieś jakoś chcą się właśnie zabezpieczyć. I Mateusz raczej to wrzucił na zasadzie tak jak powiedziałem - prewencji, a nie rzeczywistego wymagania, czy to ono w ogóle będzie potrzebne. Dlatego ja może zrzuciłem to z Rady Architektów. Przypisałem to do siebie. Na razie na **Backlog** mam to podpięte pod ten **Epic** LOT-owy, tak? Więc mi to nie zginie.

**Damian Kamiński**: No. Jak zdefiniujemy dobrze potrzebę... Bo tak to dorzucamy sobie roboty, coś co na razie nie jest wymaganiem. No widzimy, że to trzeba zaopiekować, ale może żebyśmy nie podchodzili do tej roboty 2 czy 3 razy?

**Łukasz Bott**: Tak. Dokładnie tak to napisz.

**Damian Kamiński**: Bo ja to widzę znowu kolejne jeszcze jakieś aspekty tych korzyści tych spółek, że tam w prawym górnym rogu, gdzie mamy Damian Kamiński, to może warto było już na tym poziomie pierwszego widoku, a nie po kliknięciu, pokazać w jakiej spółce teraz jesteśmy. Ale to są już kolejne aspekty wielospółkowości. Więc musimy na pewno do tej wielospółkowości siąść.

**Łukasz Bott**: Tak, więc spółkowość jest.
Choć dobra, to czekajcie, tu wiecie co to by się... on ponownie może przejrzyjmy te co są błędy i ten **Hotfix**, tak? No bo to jakby nie patrząc błąd może być... może coś co jest do naprawienia. To co jest tam PBI, to to być może zrobimy, tak? To to, że jest wrzucone.
Mm, no teraz co ten... Dobra. Zacznę od lżejszej rzeczy, co tam chodzi? Dobra, tutaj jest coś takiego. Ania jest? Nie wiem czy to ja coś dyskutowała się z Mateuszem w ten sposób, czy nie?

**Anna Skupińska**: "Błąd: Data w miesiącu nie uwzględnia roku". A to, to jest takie bardziej, że w tym filtrze chodzi, że on jest tylko w miesiącu. Patrzy na miesiąc, nie patrzy na rok. Więc jeśli chcesz, żeby patrzeć jeszcze na rok, to dodajesz, żeby patrzył też na rok. Jest albo też dwa filtry, chyba nawet jest specjalny filtr obu.

**Damian Kamiński**: Nie mamy czegoś takiego jak "miesiąc i rok". Tylko pytanie jest takie: kiedy wtedy ktoś to używa? Tylko jak porównuje lata, tak? To znaczy no właśnie mi nawet nie jest w stanie porównać lat, bo...

**Kamil Dubaniowski**: No ale to sobie dodasz 2. Data utworzenia w miesiącu sierpień, Data utworzenia w miesiącu w roku 2025. Ten filtr, tak.

**Anna Skupińska**: No ale to jest bardziej problem tego, że ta kontrolka się tu pokazuje. Jeśli zrobiliśmy, żeby po prostu nie było to widoczne, to...

**Łukasz Bott**: Tu macie chodzi o to, że się pokazuje kontrolka i to data w kontrolce roku - numer roku, tak? I to jest mylące. Bo "w miesiącu" i sugestia - i ja przed spotkaniem sobie też tak myślałem - faktycznie to może mylić, że ja oczekuję, że to w tym miesiącu tego roku, tak? Sierpniu bieżącego roku, na przykład jak na tym obrazku. Z drugiej strony ten operator "w miesiącu" zawsze tak działał od zarania dziejów, tak?

**Kamil Dubaniowski**: Nie, operator "w miesiącu" kiedyś podawałeś datę.

**Łukasz Bott**: A, bo wskazywały właśnie... tak, wskazywać datę, tak. Dowolny dzień z danego miesiąca. Tak? I wiadomo było, że to chodziło o ten miesiąc w tym roku. Więc tak to znaczy rozwiązanie słuchajcie?

**Kamil Dubaniowski**: Nie no, jak się da to ukryjmy.

**Damian Kamiński**: Znaczy kasujemy ten nagłówek roku, tak? I tyle jej strzałeczki.

**Łukasz Bott**: Dobra. Dobra, no pytanie jest takie, czy w tej kontrolce jesteśmy w stanie ukryć rok?

**Anna Skupińska**: Czy jeśli ukrywanie akurat można zrobić przy pomocy **CSS**, więc tak.

**Damian Kamiński**: Dobrze, momencik, to tak.

**Łukasz Bott**: Bo wiem nie... czekaj, czekajcie, Damian pozwolisz, bo jest to przejście. Złożenie ja powiem. 2 rozwiązania.
Pierwsze następujące: jeżeli to ma być operator "w miesiącu" - nieważne którego roku - czyli na przykład chcę sobie zrobić faktycznie takie zestawienie i porównać... Mamy dane z iluś tam lat i chciałbym zobaczyć... To jest chyba takie porównanie rok do roku, tak? W danym miesiącu nie jak się to zachowało, a miesiącu zeszłego roku to było tak, a w tym roku już jest lepiej, bo albo gorzej, tak? No bo na przykład jakieś tam wartości to bardziej do KPI pasuje niż w lutym.
Ale jak już, to ja bym tutaj zrobić coś takiego: Operator "w miesiącu" bym pozostawił, ale wtedy nie kontrolka taka kalendarzowa, tylko po prostu lista wyborcza od 12 pozycji, od stycznia do grudnia. I dorzucić nowe "operator w miesiącu i roku" i wtedy ta kontrolka tak i wtedy ona by robiła.

**Anna Skupinska**: Dobrze tak mogło być.

**Kamil Dubaniowski**: Ale to też możesz budować te grupy, więc da się zbudować to co chciałeś. Czyli robisz grupę, że Data utworzenia znaczy data to jest w miesiącu sierpień i w roku 2025. Z 2 osobnymi. Lub nowa grupa "Data utworzenia w miesiącu sierpień 2024", więc też nie jest jakby...

**Łukasz Bott**: No tak. No tak, tak. Pytanie czy słuchajcie, no to pytanie, czy w ogóle warto się tym zajmować? Tak.

**Kamil Dubaniowski**: Tylko zmiana tej w sensie: albo usuwamy tą belkę z wyborem roku, albo tak jak mówisz, wręcz zmieniamy to na listę dropdown z 12 pozycjami. Ja bym więcej nie ruszał, bo resztę da się zbudować tym co mam.

**Łukasz Bott**: Dokładnie tam.

**Anna Skupińska**: Mhm, no dobrze. To tak można zrobić. Myślałam też, że po prostu jak jest "w miesiąc" to żeby usunąć tą część tej kontrolki, żeby nie myląca i dodać nowy filtr "w miesiącu w roku", nie? Że się jest tak z tą kontrolką jak tutaj.

**Kamil Dubaniowski**: Tej drugiej opcji bym na razie nie robił. To nie jest na tyle istotne.

**Łukasz Bott**: Nie, nie, nie, nie, nie. Zostajemy przy tym.

**Damian Kamiński**: No to znaczy w międzyczasie sprawdzam jeszcze, bo według mnie w ogóle nie od tej strony powinniśmy wychodzić, że my to projektujemy, ale nie widzę czegoś takiego, tylko patrzeć na te w **Extreme**, jakie są gotowe rozwiązania do tych potrzeb. I tu jeszcze przypomnę Aniu, że dobrze by było, żebyś zaczęła od AP. Jeśli nie ma żadnych **Hotfixów**, to żebyś zaczęła, oddaj tu tego... odezwała się do Janusza, bo już jest może tam poda te dostępy i żeby to ogarnąć. Ale no nie znajduję... powiem szczerze tego co bym chciał, to o czym mówimy, więc może nie ma.

**Kamil Dubaniowski**: **DevExtreme** znaczy... to my tutaj korzystamy z tym ekstremalnie? To jest...

**Anna Skupińska**: Tutaj ta kontrolka to pamiętam to jest od **Ant Design**.

**Kamil Dubaniowski**: Mi się wydaje...

**Anna Skupińska**: Tutaj nic ze **DevExtreme**. W **Streamie** są tylko niektóre raporty, nie wszystkie.

**Damian Kamiński**: Rozumiem, dobra.

**Kamil Dubaniowski**: Dobra, no to podsumowując: tak, ukrywamy tą belkę i...

**Łukasz Bott**: Dobra, czyli ja chcę tam z kryteriami.

**Kamil Dubaniowski**: No chyba, że **Ant Design** ma jakiegoś gotowca do wyboru miesięcy i chcemy podmieniać, ale to nie mecz.

**Damian Kaminski**: Już sprawdzam czy ma. **DatePicker Select Month**. Nie no, ogólnie system wyświetla się dokładnie tak samo jak u nas, czyli z rokiem. No to trzeba to ukryć ręcznie i tyle. Dobra, to idźmy dalej.

**Kamil Dubaniowski**: Znaczy precyzyjnie już to cała belka, tak? Żeby strzałki też nie zostały, ani numer roku.

**Łukasz Bott**: Dobra, to tam Adriana następny tak trzeba dzwonić i panie... Przekonamy się. Przy czym ja bym to z nią na na... na niski taki pierwszy pytania.

**Damian Kamiński**: Znaczy, poczekaj Ania, ile to jest roboty? Bo według mnie pół godziny.

**Anna Skupińska**: Mhm. Znaczy trzeba trochę pogrzebać w CSS. Powiedziałam, że to maksymalnie 2 jednostki roboty.

**Damian Kamiński**: No właśnie, nie załatwmy to i tyle.

**Łukasz Bott**: Dobry no. Ile tam Aniu mówiłaś jedynka czy...?

**Anna Skupinska**: Maksymalnie 2, jak kto się na tym zna, to jedna.

**Łukasz Bott**: Dobra, 2 maksymalnie i tyle. Dobra, to to... Natomiast ogarnij to... jak zrobisz to od ręki to zrób, a jak nie no to...

**Anna Skupińska**: On się nie dopytał, Ania czego się potrzeba, to ja się napisałam, że potrzeba mi e-maila, czyli loginu i hasła i tyle.

**Damian Kamiński**: No dobra spoko, no to starcie tam co i jak, bo ja po prostu tego nie mam, więc niepotrzebnie tylko będę spowalniał komunikację. Więc jak dostaniesz, to po prostu trzeba to wydać. Mam zrobić na to zgłoszenie też do testów? Bo no bo tu są jakieś ryzyka, trzeba to przetestować na pewno lokalnie, czy to nic nie spowoduje?

**Anna Skupińska**: Chyba tak. Trzeba zobaczyć wszystko może. Mogę sobie Zuzę podać, które raporty są **DevExtreme**, będzie trzeba przetestować po prostu.

**Damian Kamiński**: No i świetnie, już robię w takim razie, no to...

**Łukasz Bott**: Dobra, ale tu co Adriana wydzwaniamy, tak?

**Damian Kamiński**: Mhm.

**Łukasz Bott**: No i dzwonię, dzwonię, Adrian jest. Dobra, Adrian, tak... Cześć, dzwoniliśmy ciebie, bo omawiamy temat integracji kastomowych, błędy, grupowanie parametrów integracji. Ponieważ komentarzach gdzieś z komentarzy wynika, że brałeś udział w dyskusji, to chyba wiesz o co chodzi?

**Adrian Kotowski**: Cześć. Nawet ten... nie.

**Damian Kamiński**: Nie, nie, nie Adrian chyba nie brał udziału w dyskusji. My dyskutowaliśmy to z Kamilem i z Kołakowskim Mateuszem.

**Adrian Kotowski**: Czy to jest ogłoszenie? Piątek przedstawianiu tłoczni, więc kojarzę ten temat, no i nawet to wczoraj zrobiłem. Generalnie, więc nie wiem czy to jest o czym dyskutować.

**Damian Kamiński**: Nie chcemy tylko się upewnić, jakbyś mógł kliknąć na ten na ten **Develop**. Bo tutaj no link pośrodku opisu, bo to jest po to zdefiniowane, żebyśmy nie poprawiali tego drugi raz za chwilę. Bo zgadza się, że była instrukcja do tego jak przygotowywać... jak przygotowywać powiedzmy ten nazwy. Natomiast to było tylko zalecenie, bo to nie miało żadnych zależności w kontekście wyświetlania do tej pory. A teraz jak rozumiem, zaczyna mieć i pytanie, czy to nam po prostu nie zaburzy sposobu wyświetlania tych rozszerzeń? Ale to no, musimy spojrzeć, żeby to dobrze mówić.

**Adrian Kotowski**: Czy to jest tylko ten razowy? Bądźcie się tak. To było przemyślane, że teraz jakby taką bardziej Uniwersytecie [Uniwersalność] no zostanie zachowana, że te grupy powinny być tak samo wyświetlać. Na tym, że teraz osoba, która tworzy nową integrację, to powinna mieć świadomość, że tam no definiuje też nazwę grupy i tyle. Że nazwie integracji grupy, aczkolwiek to może być tak trochę sama nazwa już to niż chodzić, żeby to było.

**Damian Kamiński**: No właśnie, czyli zmierzam do tego, że nazwa grupy jest nazwą biznesową.

**Adrian Kotowski**: Ale nie tak, no bo teraz to jest wyświetlany po prostu w tej zakładce. Nazwa integracji tak, że nazwy integracji.

**Damian Kamiński**: Mhm.

**Adrian Kotowski**: I tu jest tak, tak, nazwy integracji. W ramach tej... czy będą to takie czyste, tylko ułoży to, bo to jest tak nazwa, tak, tak, to prawda, nazwa tak, nazwa tej integracji. I później są te podgrupy. Z tym, że tu teraz jest tak, że dla istniejących starych integracji to została zrobiona tak, że nazwa grupy jest różna nazwy integracji, bo nie było jakby nazwy integracji jako takiej podanej, więc musieliśmy jakoś tę nazwę integracji wymyślić.

**Damian Kamiński**: Okej, więc ją uspójniłeś. Dobra to rozumiem. W sensie czy nie było nazwy integracji? W sensie po prostu ją przekopiować. Tak to masz na myśli.

**Adrian Kotowski**: Ale w sensie? Tak, znaczy, musiałem jakoś to tak... czekać. Czy było tak, tak, tak, no musiałam to być duże kopiować. Znaczy tam był taki problem, jeżeli... lecz ja tego nie zrobiłem, bo to już nazwę parametru. Jest to nazwę integracji, ale zauważcie, że to może być tak, że na przykład mogą być różne grupy generalnie, a... Ee, mogą być właśnie różne grupy i to, to mogą spóźnić.

**Damian Kamiński**: Teraz to nie wiem czy zrozumiałem.

**Adrian Kotowski**: Chodziło to, że po prostu mogą być różne podgrupy. W ramach tego, tego do wyświetlania może. To znaczy jak jest w ogóle właśnie pytanie, bo tak, żeby tutaj nie kluczyć...

**Damian Kamiński**: Sekundę, bo ja tu wgrywałem jak teraz przejść na ustawienia systemowe stare? Ktoś mi podpowie? Jak to czegoś?

**Piotr Buczkowski**: Panie a nie ma linku? Przejdź do poprzedniej wersji.

**Damian Kamiński**: A masz rację, dobrą masz rację. Dobra, to może ja przejmę na chwilkę? Chodziło tylko o to, no chyba, że zostaniemy sami z Adrianem. Chodziło tylko o to, żeby to się nie wykrzaczało, czyli...

**Adrian Kotowski**: No już teraz tak, co tu widzimy, tutaj ten... to nazwy tych... Ale to są nazwy prawdę, nazwy grup. To co tu jest ten, niż jeden **IFace**.

**Damian Kamiński**: No tu, no.

**Adrian Kotowski**: A nazwa integracji jest z kolei zawarta w nazwach parametru, więc już nie ma gwarancji. Wcześniej było dobrze, robiła, że ktoś na przykład nie wiem dodał...

**Damian Kamiński**: No właśnie dokładnie, że nie ma tej gwarancji. O to, o to mi tylko chodzi, żebyśmy jak przejdziemy na nowy wygląd, to żebyśmy obsłużyli ten przypadek, że jak ktoś nie zrobił tego dobrze, to tu się wyświetli jednak dobrze.

**Adrian Kotowski**: No jeżeli ktoś to zrobił źle, w sensie w tych starych, starym widoku, też nowy będzie się tak... od tego nie da się pójść, to obejść.

**Damian Kamiński**: Poczekaj, ale... Ale teraz pytanie, co ty określasz źle? Bo jeśli ktoś nazwał sobie **IFace** i tu zdefiniował domyślne **Endpoint**, a potem nie nazwał "**IFace** kropka" i jakaś tam metoda, tylko nazwał sobie zupełnie inaczej, to jedyny skutek będzie taki, że tu będzie **IFace**, a tu będzie jakieś "wykorzystuje **IFace**", tak? Tylko ta nazwa będzie niespójna i wtedy może to sobie ewentualnie przerobić i wszystko wrzucić w jedno **IFace**, tak?

**Adrian Kotowski**: No to było nie tak.

**Damian Kamiński**: I tak to jest przygotowane, tak? Teraz.

**Adrian Kotowski**: Tak.

**Damian Kamiński**: No dobra, to ja bym powiedział, że jeśli ty to potwierdzasz, to na razie nie mam uwag. To znaczy, że to jest spójne z tym, co my omówiliśmy, jak powinno to zmigrować. Bo tutaj właśnie kluczowe jest to, że też nie wiedzieliśmy, ale... ale już się dowiedzieliśmy, że to jest... tu jest tylko i wyłącznie de facto wyświetlane dedykowanej tabeli do wyświetlania. Tak? Cały mechanizm pozostaje de facto taki, jaki był tutaj. Czyli to co tu widzimy, to jest efekt dodatkowej tabeli dedykowanej do wyświetlania tych, tych zasobów, tak?

**Adrian Kotowski**: No dokładnie, to Goście możesz przed wejść i tak jest systemowy, bo tam jest to lepiej, lepiej, lepiej przykład pokazany. Przed może wejść sobie w jakąś... Nie wiem na przykład możliwe e-Doręczenia.

**Damian Kamiński**: Mhm.

**Adrian Kotowski**: A tu masz przykład: masz po popularnej stronie masz nazwę integrację, natomiast po prawej na górze masz nazwę grupy, gdzie tak to zostało to zrobione, żeby po prostu...

**Damian Kamiński**: No dokładnie i to jest według mnie w porządku. W sensie, że to nie jest spójne z tym i to jest coś, co wywołujemy w kodzie, a to jest coś, co nazywam sobie dowolnie, tak?

**Adrian Kotowski**: I to akurat nic nie wywoływane w kontrakcie, bo to jest integracja jakby, tak, tak.

**Damian Kamiński**: No tak, ale jeśli to by była definiowana i tak by to było przedstawione, tak.

**Adrian Kotowski**: Dokładnie tak, no ale to nie jest jakiś problem, no to tutaj w miarę spójne te nazwy, one się mogą różnić minimalnie. To jednak tu no bardzo zbliżone do siebie.

**Damian Kamiński**: Dobra, ja chyba dla mnie też wyjaśnione. Nie wiem, czy Kamil do czegoś nie uwzględniłem?

**Kamil Dubaniowski**: Nie zgłaszam.

**Damian Kamiński**: No dobra, to dobra wydaje się, że jest to teraz dobrze tak jak opowiedziałeś, więc dobra czekamy na testy. W takim razie ja na razie nie mam uwag, idźmy do kolejny.

**Kamil Dubaniowski**: Znaczy, wydaje mi się, że nawet nie ma co dziewczyn tym obarczać, to powinno to nastąpić...

**Damian Kamiński**: Może iść do nas tak, jak najbardziej możesz nas wskazać do testów. Do tego wydaj to na dewelopera, to pójdzie czy jeszcze na jakieś lokalne?

**Kamil Dubaniowski**: Fajnie jakby poszło na strefowe, bo tam mam realne też przypadki, które teraz są źle grupowane.

**Adrian Kotowski**: Tak.

**Damian Kamiński**: Bo po prostu jak wrzucić gdzie to wrzucisz, to my zaimportujemy tam takie właśnie byty dziwne od różnych klientów i sprawdzimy, czy to jest spójne. Więc pytanie, gdzie będziemy mogli przetestować, to nam napisz po prostu już.

**Adrian Kotowski**: Tak jakby wyroby to można w sensie wrzucić tam na tych różnych wersjach.

**Damian Kamiński**: No to wydaj to na dewelopera, dobra?

**Łukasz Bott**: Dobra, czyli co zgłoszenie zdejmuje z Rady Architektów? Yy, pozostaje u Adriana, ale co jest na etapie **New**? Czyli na jakim czy jaka?

**Adrian Kotowski**: Więc nie powinien być **On Progress**. Ja dzisiaj to już... żałować i dewelopera i tam później by nie wróciły do tych starszych wersji.

**Łukasz Bott**: Dobra to ustawiłem na **In Progress** to jest. Szukajcie testerem to tam wskażę testera albo ten do których to wersji wgrywamy.

**Adrian Kotowski**: Tak.

**Damian Kamiński**: Systemowe z tymi po nowemu.

**Łukasz Bott**: Dobra.

**Adrian Kotowski**: Tam, gdzie jest integracje, zakładki? Tak.

**Łukasz Bott**: Dobra, dobra poszło.

**Damian Kamiński**: Dobra przyjmie z powrotem. Ekran w sensie, bo ja...

**Łukasz Bott**: Jesteśmy, jesteśmy.

**Damian Kamiński**: A czy czy kończymy?

**Łukasz Bott**: No to znaczy, no formalnie mamy 10:40, czyli kończymy tak, no chociaż... Nie wiem, dobra, yy, zostały 2 PBI to... 3 PBI.

**Damian Kamiński**: A tutaj logowanie maili wychodzących? Tu Piotrze, coś się do rady? Bo to produkujesz.

**Piotr Buczkowski**: No to tutaj zostało: czy kiedy to logować, tak? Czy w momencie dodania do kolejki wychodzącej, tak? Czy tam wysłania, czy dodania do kolejki wychodzącej, tak?

**Damian Kamiński**: Mhm.

**Piotr Buczkowski**: Wejść do wysyłania, czy w momencie faktycznego wysłania?

**Damian Kamiński**: No według mnie to drugie by było najbardziej.

**Piotr Buczkowski**: No tylko to jest problem dla zbiorczych.

**Damian Kamiński**: Mhm.

**Piotr Buczkowski**: Wobec zbiorcze ma powiedzmy nasze spraw, tak?

**Damian Kamiński**: No dobrze o k. To załóżmy jakie jest ryzyko, jeśli robimy według pierwszego? Takie, że ktoś usunie z kolejki. Możemy to opisać, że tak to działa, że jeśli ktoś usunie, to mamy fałszywą informację, ale to jest świadome działanie administratora. Samo to nie przepadnie.

**Piotr Buczkowski**: Tak, bo te bo teraz...

**Kamil Dubaniowski**: Znaczy ogólnie mamy tą złą informację, no bo jak job się zatrzymał i nie wysyłamy maili, to i tak będzie, że wysłaliśmy.

**Damian Kamiński**: No to też prawda.

**Łukasz Bott**: Chyba żeby zrobić 2 zdarzenia: "Dodano do kolejki do wysyłki" i potem "Wysłano".

**Piotr Buczkowski**: Tak dokładnie to miałem zaproponować. To miałem zaproponować. Może nie tyle 2 zdarzenia, co aktualizacja tego zdarzenia, że...

**Damian Kamiński**: No też tak. Wysłane.

**Piotr Buczkowski**: Znacznik wysłana.

**Łukasz Bott**: A czyli nawet jest w stanie "Dodano do kolejki wysyłki", "zaplanowane", "zaplanowane do wysłania", a potem OK no.

**Damian Kamiński**: Zaplanowane. Mhm. No to chyba tak musimy to rozwiązać, bo inaczej, no to to powiedział Kamil: jak ktoś usunie świadomie to jeszcze usunął, ale jeśli się zatrzyma, no to to jest powiedzmy nasza wina, jakaś tam błąd aplikacji, potem będzie.

**Piotr Buczkowski**: Znaczy jest też ta funkcjonalność, że maile, które są powiedzmy przez dzień się nie uda wysłać, jest stosowany. [Anulowany]

**Damian Kamiński**: Mhm. Dobra, to zróbmy tutaj dodatkowy jeszcze parametr. Że faktycznie "Wysłane". W sensie no daty pewnie w tą kolumnę musimy wprowadzić, tak? Data czas kiedy jest wysłane.

**Łukasz Bott**: Został.

**Damian Kamiński**: No tak, kiedy zostały już już po faktycznym zdarzeniu.

**Piotr Buczkowski**: OK. Oczywiście ustawiać to po wysłaniu, czy jeżeli kiedy serwer pocztowy nie, nie odpowiem błędem.

**Damian Kamiński**: Tak.

**Kamil Dubaniowski**: Zastanawiam się w takim razie czy... No bo teraz będziemy mieli. Jest jest jakaś tabela **Notification**, tak? I tam jest ta kolejka aktualna. I teraz będzie duplikat trochę tej tabeli plus z otrzymywanie w historii całości, tak? No bo tutaj z tej tabeli się usuwa po wysłaniu, a tam będzie zostawał.

**Damian Kamiński**: No powiedzmy no nie duplikat, to będziemy migrować tak jakby.

**Piotr Buczkowski**: Jakie to, jaki to plik?

**Kamil Dubaniowski**: No nie, no bo nadal będzie dodawało tutaj. Ja nie wiem czy to jest jakaś nowa tabela z wysłanymi? Nadal będzie to dawało od razu w momencie dodania do...

**Damian Kamiński**: No ale to tylko... Masz rację, że będzie przez godzinę tak powiedzmy do wykonania, czy przez 5 minut do wykonania joba. No Kamilowi chodzi o to, że do kolejki i do tej tabeli notyfikacji wskoczy od razu wpis i tu i tu taki sam. W jednym miejscu zaplanowany do wysłania, w drugim miejscu... No właśnie jeszcze zaplanowane do wysłania z danej sprawy, tak.

**Kamil Dubaniowski**: Po prostu... czy tak no jedno to jest po prostu kolejka, która się czyści po wysyłce, a druga to będzie taka kolejka, która się nie czyści po wysyłce jest też historią wysłanych przy okazji. Więc się zastanawiam czy warto robić osobno tabelę na to, czy po prostu nie zmienić zasady zachowania tej tabeli **Notification**, że ona nie usuwa wpisów, tylko właśnie zmieniam status.

**Damian Kamiński**: No tylko ona, no w kontekście joba co wtedy będzie musiała robić selecta no jeszcze nie wysłanych. I to może być obciążające, dla tego joba, bo co 5 minut jest przeszukiwanie, powiedzmy po roku setek tysięcy.

**Kamil Dubaniowski**: No ja no wiecie o co mi chodzi sugeruje.

**Damian Kamiński**: No to nie wiem, to tu Piotr niech się wypowiadać czy to w ogóle dobry kierunek.

**Piotr Buczkowski**: Jak jeszcze raz?

**Damian Kamiński**: No Kamil się zastanawia, czy tabela **Notification** nie powinna być tą historią.

**Kamil Dubaniowski**: Znaczy, bo chodzi o to, że teraz będziemy mieli w 2 miejscach to samo przez chwilę.

**Piotr Buczkowski**: Przez... no tak.

**Kamil Dubaniowski**: A wszystkim OK, no dobra, tylko to chciałem wybrać.

**Piotr Buczkowski**: Znaczy, nie będziemy mieli tego samego, nie dokładnie to samo.

**Damian Kamiński**: No tam trochę się będą różnić.

**Kamil Dubaniowski**: No tak, no bo w tamtej tabeli będą też też inne, tak? Te **SendMessage** i te wszystkie, które wychodzą automat.

**Piotr Buczkowski**: No bo chociażby te te zbiorcze to w tej tabeli będzie będzie w **Notification** będzie zbiorczy, o w tabeli tej **CaseUserAction** będzie rozdzielony.

**Kamil Dubaniowski**: Pojedynczo. Dobra no dobra, to nie mam też.

**Damian Kamiński**: Dobra, to tam mamy jeszcze zerknijmy przynajmniej czy to warto poruszać dzisiaj, czy możemy przesunąć.
Wiecie co to może być pod jednym tylko... a no to jest to co ostatnio nawet chyba narobił. Ostatecznie przegadaliśmy na szybko odrzuciliśmy. No tam Adrian dał komentarz, że kiedyś na razie dyskutowaliśmy o tym, żeby zmiana typu pola właśnie była bardziej ograniczona, czyli żebyśmy pozwalali na przykład tylko zmieniać, jeśli zmieniamy na ten sam typ i nie ryzykujemy utraty danych. Ale no wydaje mi się, że to jest tak jak teraz jest OK, no po prostu to jest raczej wykorzystywane tylko w momencie, kiedy wdrażamy jeszcze. Tam nie ma zazwyczaj danych produkcyjnych, a zmiana taka na produkcji...

**Kamil Dubaniowski**: No to to co Piotr sugerował - to nasi konsultanci powinni wiedzieć, że to trochę praktyka to jest ukrycie pola i dodanie nowego, a nie tej opcji zmiany. Może rozwojowo, jeśli już o tym myślimy, no to ta walidacja, o której Piotrek wspominał, czyli sprawdzenie, czy w polu którego typ zmieniamy, nie ma jakichś danych. I potencjalnie jeszcze raz ostrzec o tej, że te dane zostaną utracone, jeśli wykryjemy, że tak jest, ale tak jak teraz mamy to zabezpieczenie, że trzeba zaznaczyć checkbox, że świadomie zmieniam typ i jestem świadom ryzyko utraty danych, to wydaje mi się, że to już jest wystarczający.

**Damian Kamiński**: Jest to bardzo bezpieczne, aż za bardzo. Tak możemy tylko zajmować właśnie w przypadku, gdy tych danych nie ma, więc to już według mnie niższy priorytet.

**Kamil Dubaniowski**: No to lecimy dalej. To nie ma co.

**Łukasz Bott**: Ale to, to czy zdanie to z radę i rozumiem, że to jest do roboty? Tak czytam jest na...?

**Kamil Dubaniowski**: To jest internet, to już jest zrobione tylko Adrian miał tam właśnie sugestie, jakby podwyższenia jeszcze tego zabezpieczenia.

**Łukasz Bott**: Jest. Ukryj dobra i myśmy już chyba wstępnie wczoraj się kłócili o to.

**Damian Kamiński**: No. Amerykanie wiadomo, to jestem ostatecznie zrobić.

**Łukasz Bott**: Ja bym to po prostu ubił i tyle.

**Piotr Buczkowski**: Dobrze, ja tam wczoraj znalazłem błąd tam Ania miało poprawić. I pytanie, jak poprawienie tego błędu to działa.

**Anna Skupińska**: Przypisałaś jeszcze się tym nie zajmowałam, ale jak chce się tym zająć?

**Piotr Buczkowski**: No tam był błąd wynikający z jakieś tam poprawki, tak.

**Anna Skupińska**: Na to możecie teraz zadanie przypisać pewne przepisami, nie.

**Damian Kamiński**: Ale to czekajcie. To jest związane z tym polem, bo tak mówisz.

**Piotr Buczkowski**: Z tym polem, w tym w tym w tym momencie, jeżeli wpiszesz taką wartość w tym polu. Sensie, pamiętasz zgłoszenia do zgłoszenia, co ja?

**Damian Kamiński**: No właśnie dlatego pytam, żeby tu od razu podpiąć. Weź dodaj link zaraz na nie jest przypisane, tak?

**Piotr Buczkowski**: Tak, tak.

**Anna Skupińska**: Tak, to jest błąd. Przybysz [Przypisz] 22192 - błąd nie niesie dla mnie informacji o błędnej wartości w polu z maską telefon.

**Piotr Buczkowski**: Wczoraj chciałem to sprawdzić i zauważyłem to, tak.

**Kamil Dubaniowski**: Znaczy ja też z chłopakami o tym dyskutowałem jak oni zgłaszali te tematy. OK. Czyli na to Piotrek dodał, a oni też dodali. Może też cię wciągnęli w dyskusję, że to zgłosili osobno jeszcze poza tobą. Bo błąd jest taki, że oni spodziewali by się, że reguła się nie wykona? A my tu komunikujemy, że jest niezgodne.

**Damian Kamiński**: Jest **Field Incorrect**, tak?

**Kamil Dubaniowski**: Tak, bo tam wyskakuje na czerwono.

**Piotr Buczkowski**: Tylko że się nie wyświetla się pole, bo jest błąd przy wyświetlanie tej informacji.

**Damian Kamiński**: Czyli to jest **Field Incorrect** tylko nie wyświetla się ten **Field Info**? Tak?

**Piotr Buczkowski**: No tak. Tak zrozumiałem.

**Łukasz Bott**: Komunikat podpowiem.

**Kamil Dubaniowski**: Znaczy ja jak oni mi to pokazywali, to my zaznaczamy, to znaczy czerwono. W obecnej wersji tą, którą oni testowali, nawet był ten dopisek, mi się wydaje, bo było po prostu niezgodne z maską, ale to nie jest walidacja to jest tylko ostrzeżenie, że masz niezgodne z maską i to jest ostrzeżenia na czerwono i normalnie i reguła się wykonała. Czyli to nie jest tak jak działało pole walidowane, że musi być zgodne z maską, tylko po prostu my tu sugerujemy, że jest niezgodne, ale puszczamy dalej. I wydaje mi się, że to jest w kontekście... to Rafał chyba robił te maski. Nie pamiętam, że nie byliśmy w stanie zrealizować wszystkich numerów z różnych krajów.

**Piotr Buczkowski**: No tak, tak są też jakieś niestandardowe, jak ktoś ma jakiś tam numer wewnętrzny, tak.

**Kamil Dubaniowski**: Więc ja ciężko się odnieść do tego, no ale może chociaż na polskie numery moglibyśmy to jakoś...

**Damian Kamiński**: To jest pierwszy, bo to 90% potrzeb dokładnie, a 2, że...

**Kamil Dubaniowski**: To będzie pewnie dziewięćdziesiątego ósmego.

**Damian Kamiński**: No pytanie czy poza plusem i myślnikiem - bo nie wiem czy tu myślnik nie testowałem - powinny być dopuszczalne w ogóle inne znaki. Może tylko cyfry, chociaż nawet nie wiem czy plus, skoro plus jest z przodu? No właśnie może powinny być tylko dopuszczalny cyfry, ewentualnie może myślniki, chociaż nie wiem czy to nie konfliktuje czy one dzisiaj są możliwe do wpisywania. Teraz mogę sobie sprawdzić.

**Kamil Dubaniowski**: Plus nie, no bo on jest tak.

**Łukasz Bott**: To jest z przodu.

**Piotr Buczkowski**: Często często się wpisze swoje na przykład tak, że jesteś 9, spacja, 129, spacja 8, 9.

**Damian Kaminski**: No to ewentualnie spacja. No dobra to tu się zgadzam, ale wiecie, no nie musimy wprowadzać maski ilości - niech to pozostanie dowolne - ale maskę znaków. W sensie to znaczy walidację znaków, że to mogą być albo białe znaki, albo myślnik, albo cyfra.

**Łukasz Bott**: Myślniki, spacje ewentualnie, tak naprawdę proszę. To znaczy nawet nie nie nie białe znaki, bo że tabulator albo Enter. Tak to jest też biały znak, spacja tylko.

**Damian Kamiński**: No to spacja, no.

**Łukasz Bott**: Spacja, myślnik i cyfry taki.

**Kamil Dubaniowski**: Bo wydaje mi się, że na przykład kod pocztowy jest realizowany tak, no bo jest łatwiej. Jak tam dziś z jakiejś integracji dostawałem bez myślnika, no to to już miałem puste pole, bo nie przyjmowało mi tej wartości.

**Łukasz Bott**: Bo to w Czechach nie działa, bo Czesi mają bez myślnika.

**Damian Kamiński**: No ale to jest polski chyba tak.

**Kamil Dubaniowski**: Albo właśnie w drugą stronę. Tak tak możliwe, że ja dostałem właśnie pole jest bez ja pamiętam, ale tak czy inaczej? No ta maska powinna w jakimś stopniu realizować... Wiadomo, że jakieś wyjątki mogą sobie tam **Regexem** później obsługiwać z poziomu kodu.
Ale ten polski numer, chociaż właśnie żeby tutaj nawet ilość moglibyśmy przy polskim pilnować tak, żeby było to 9 cyfr, to jest stałego.

**Łukasz Bott**: No nie jest to znów niekoniecznie, bo może ktoś...

**Damian Kamiński**: Nie, bo możesz mieć 10, bo możesz mieć nieźle 8 tak dla stacjonarnego, bo możesz wpisać +48 22 111 22 33.

**Kamil Dubaniowski**: No przy +48.

**Łukasz Bott**: Nie, to wtedy, to nie to. To też masz 9.

**Piotr Buczkowski**: Nie, nie ma, nie ma 8 cyfrowych już nie ma, wszystkie są 9-cyfrowe.

**Łukasz Bott**: Wszystkie są 9-cyfrowe, ale ja mówię o numerach na przykład jakiś US [Urząd Skarbowy]. Nie wiem, Warszawa ma tam ten coś tam 19 115 to jest jakiś taki...

**Damian Kamiński**: No taksówki mają czterocyfrowe chyba, tak.

**Łukasz Bott**: No dokładnie tak, no.

**Damian Kamiński**: Znaczy, no, może nie musimy iść aż tak mocno, żeby tutaj wymagać 9, ale bo to można też wtedy wprowadzić - ktoś może sobie odczytać wartości i zrobić to pod reguły, jeśli ustalą w procesie, że tutaj tylko takie znaki mogą wchodzić, to sobie zrobi walidację tego pola ręcznie. Ale żeby tu nie można było wkleić właśnie jakiś takich dziwnych znaczków, bo ktoś kopiuje i nie zauważył, że poszedł mu dwukropek czy coś w tym stylu, no to to to jest banał.

**Łukasz Bott**: Tak, bo to ten dwukropek. Ten dwukropek to mógł się wziąć z tego, że był jakiś formularz: "telefon:", no i ta nie wziął kontrolce tam Shiftem coś tam machnął za bardzo myszką i mu się ten dwukropek gdzieś tam skopiował, nie? To nie było intencjonalne prawdopodobnie.

**Damian Kamiński**: Tak dokładnie.

**Łukasz Bott**: Słuchajcie, jako **MVP** zróbmy w ten sposób: nie mamy walidacji na długość, walidacja jest tylko taka, że pozwalamy tylko wprowadzić cyfry, myślnik bądź spacje jako separator. Ja bym tak to zrobił.

**Damian Kamiński**: Dobrze, ale to teraz tak. Teraz to się... no bo jak rozumiem, Piotr wykrył, że w samym kodzie jest błąd walidacji, czyli to znaczy, że dwukropek nie jest możliwy tak do wprowadzenia już dzisiaj w sensie wyświetli błąd?

**Piotr Buczkowski**: No ale to co mówiłeś tak, to... No właśnie jest tylko informacja, że to jest błędna wartość, ale tylko zapisuje ją.

**Piotr Buczkowski**: No bo to jest, jest taka zasada tak, że nawet jak masz **Form Field Is Valid** tak ustawisz, to i tak to wartości zapisze. To jest tylko informacja, że wartość jest niepoprawna.

**Piotr Buczkowski**: Jak będziesz **FormIsValid** sprawdzać? Być może nie, nie wiem. Ale reguły się wykonują, tak.

**Kamil Dubaniowski**: Tak, przy **Firm is interes** [Form is Incorrect?].

**Piotr Buczkowski**: Czy jeżeli ktoś w regule zrobi, że **SendSMS**, no ten numer to mu spróbuję wysłać. Jeżeli nie sprawdzi, czy **FormIsValid**, czy **IsValid** dla jednego pola wskazującego pola.

**Damian Kamiński**: Bo **Ignoruj ograniczenia puli etapów** to dotyczy tylko **Forwarda**, tak.

**Piotr Buczkowski**: Tak.

**Łukasz Bott**: Zmiany stanu, tak.

**Damian Kamiński**: Część jeden tc ms tego nie nie bierze pod uwagę.

**Piotr Buczkowski**: Znaczy... No nie, nie, nie tylko przez zmianę stanu.

**Damian Kamiński**: No to nie wiem, to co sądzicie? Mamy tutaj wprowadzać totalną blokadę, czy jednak tylko wyświetlić, że jest źle? I to już jest wystarczające.

**Kamil Dubaniowski**: Czy jeśli to ma być tylko ostrzeżenie?

**Piotr Buczkowski**: Ja byłbym za tym, żeby jeżeli w regule używają tego pola, żeby dodawali sprawdzanie wartości, tak.

**Kamil Dubaniowski**: Ja bym ja bym jedynie tak to to to OK, no bo nie jesteśmy w stanie przewidzieć tych przypadków co podaliście, że na przykład czterocyfrowy może to jest OK i to powinien użytkownik zostać poinformowany, że tu jest niezgodne z maską, że spodziewaliśmy się 9, wprowadziłeś 4.
Ale to powinno być ostrzeżenie, bo teraz sugeruje to tak jak mamy właśnie przy **Field Is Incorrect** na czerwono, czyli de facto spodziewają się konsultanci, że to już jest blokada. A jak to będzie tylko ostrzeżenie? Czy wręcz info tak, no to...

**Damian Kamiński**: No ale ale co, co to znaczy ostrzeżenie? Inny kolor?

**Kamil Dubaniowski**: No tak.

**Damian Kamiński**: A jaki? Pomarańczowy to wymagane.

**Anna Skupińska**: Chyba żółty to faktycznie włączać omawiane. Niebieski to bardziej jak bardziej informacja.

**Damian Kamiński**: Nie, to chyba powinien pozostać taki **Warning** jak teraz.

**Anna Skupińska**: No myślę, że po prostu jak jest i redłowo nie przechodzi przez mapę to co? Czerwony.

**Kamil Dubaniowski**: Znaczy on w tym momencie wygląda jeden do jednego jak pole, które blokuje przesłanie formularza na dalsze to.

**Kamil Dubaniowski**: Tak, a ten nie blokuje, więc i też może. No nie wiem.

**Kamil Dubaniowski**: Tak, no dlatego oni zgłosili błąd, no bo oni oni tam jakby to jest to testowali, dostali komunikat, kliknęli i poszło dalej. Chcieli sprawdzić, czy po prostu blokuje. To masz kiedy jest nieprawidłowo wypełniony i stąd zgłoszenie.

**Damian Kamiński**: No dobrze, to to... Bo mamy **Error** i mamy **Warning**. To **Warning**, yy działa tak, że nie blokuje. Jeszcze raz Piotr, jakbyś mógł to przedstawić. Bo w tym momencie, jak rozumiem to co ty tu zasugerowałeś, to jest tylko i wyłącznie kwestia tego **FieldInfo**, które się nie wyświetla.

**Piotr Buczkowski**: No to jest błąd składniowy powodujący wyświetlenie błędów w konsoli, tak czytam w **Visual Studio**, bo **Visual Studio** jak się uruchomi to przejmuje to. Trzeba to poprawić, no bo no bo jest źle źle użyta, zmienna, nie w tym miejscu, które nie jest zdefiniowana.

**Damian Kamiński**: No dobrze, a teraz już jak to poprawimy to skutek jest taki, że działa z tego co powiedział Kamil.

**Piotr Buczkowski**: Nie wiem, nie wiem, ja nie chciałem to przetestować wczoraj, ale pojawił mi się błąd i nie wiem jaki jest skutek.

**Damian Kamiński**: OK. Dobrze, a standardowo **Warning** - **Warning** powinien puścić **Forward Case'a**, a **Error** nie.

**Piotr Buczkowski**: Trzeba przetestować. Tak, tak. Tak.

**Damian Kamiński**: Czyli wtedy powinniśmy to ewentualnie traktować jako **Error**.

**Kamil Dubaniowski**: No ale nie możemy, no bo może być sytuacja, że świadomie masz niezgodnie z maską.

**Piotr Buczkowski**: Musi mówić, trzeba trzeba zobaczyć jak to działa. Po poprawieniu tego błędu, bo nie wiem jak to działa.

**Kamil Dubaniowski**: Czy wiecie, bo ja uznaję to w ten sposób, że...

**Piotr Buczkowski**: Mogę mówić, jak można mówić, jak mi się wydaje, że to działa, ale nie no nie wiem jak to działa.

**Damian Kamiński**: Nie no dobra, tylko pytanie też jak powinno to działać? No bo Kamil mówisz, bo maska tak jak ustaliliśmy przed chwilą jest spacją, myślnikiem lub cyfrą, a nie ilością znaków, więc...

**Kamil Dubaniowski**: Teraz dla mnie, jeśli ktoś na formularzu ustawił sobie pole z maską, to po pierwsze chce ułatwić wprowadzanie. No to dobra, to jest aspekt wizualny, ale wydaje mi się, że kluczowe jest to, żeby zachować spójność danych, żeby właśnie mi nie wprowadzali jedni tych numerów z myślnikiem i inni bez, bo później nie możemy walidować. Mamy problemy, żeby sprawdzić, czy taki numer telefonu już jest. Trzeba czyścić to z myślników przy każdym wykonaniu tak dalej, więc wydaje mi się, że jeśli ktoś już używa pola typu maska, no to maska jest taka i taką stosujemy i to powinna być definicja. Jak ktoś wie, że to będą wprowadzane numery taksówek, to nie używa maski.

**Piotr Buczkowski**: Bo można... to można to dać opcję do pola, że wymuszaj maskę, tak?

**Kamil Dubaniowski**: Tak może w ten sposób?

**Piotr Buczkowski**: Czyli jeżeli, jeżeli wpisano wartość nie jest zgodne z maską, to jest błąd? Tak samo jakbyś dla pola walidowanego wpisał nieprawidłowy NIP.

**Kamil Dubaniowski**: No i wydaje mi się, że tego, tego, tego brakuje. Czyli no bo do tych walidowanych odchodzimy, wręcz nie rozwijamy i dodawaliśmy kolejne nowe maski zamiast rozwoju tych pól walidowanych. Więc no też, warto było to połączyć.

**Piotr Buczkowski**: No bo **Validated** to nie jest, nie tylko maska, że tam musisz wpisać powiedzmy 9 cyfr, ale też na przykład wyliczanie sumy kontrolnej i z NIP-u czy z PESEL-a.

**Kamil Dubaniowski**: Tak.

**Piotr Buczkowski**: Czytam, sprawdzam sprawdzanie NIP-u gdzieś tam w jakimś tam systemie.

**Damian Kamiński**: No tak, przy czym prawda jest taka... No tak, tylko mówiąc szczerze nie rozumieją tego nawet nasi konsultanci. Czy zastosować to czy to, bo te pola są i tu i tu takie same? No no wiem, dlatego o tym mówię, dlatego o tym mówię, że oni nie wiedzą czy powinni stosować to czy to.

**Piotr Buczkowski**: To, to, to, to źle, to źle.

**Damian Kamiński**: Mogę się założyć, że gdyby zrobić test, to to by był słaby wyniki z tego.

**Kamil Dubaniowski**: Znaczy, wydaje mi się, że po pierwsze. Jeśli nadal w polach walidowanych mamy numer telefonu i email, to wydaje mi się, że powinniśmy...

**Piotr Buczkowski**: Nie ma, nie mamy chyba numeru telefonu, no pole walidowane?

**Kamil Dubaniowski**: Już właśnie patrzę co my tam mamy, bo nie pamiętam tam powinny zostać tak jak Piotr powiedziałeś.

**Piotr Buczkowski**: Jest.

**Kamil Dubaniowski**: Sektora liczą sumę kontrolną i to powinny zostać walidowane. A reszta to będzie tak z maską już patrzymy.

**Piotr Buczkowski**: Znaczy według mnie dodanie tej opcji do pola tekstowego, że "wymuszaj". Tak zgodność z maską.

**Kamil Dubaniowski**: Więc to znaczy, jeżeli jest postawiony?

**Piotr Buczkowski**: To i to powoduje błąd, to wtedy też na przykład jeżeli ustawię maskę NIP, to też wylicza sumę kontrolną.

**Damian Kamiński**: My nie mamy telefonu.

**Piotr Buczkowski**: Tak, bo wczoraj sprawdzałem tak, chciałem z tym błędzie, tak telefon walidowany chciałem ustawić, pole walidowane. Ta widać tak, fragment pola to jest **Phone**, że walidacja telefonu a nie była. Zrobiłem tylko, że tam 9 cyfry tak **Regex**, że ten **Regex**, czyli **Regex** 9 razy.

**Łukasz Bott**: Słuchajcie jaka, jaka konkluzja, bo...

**Kamil Dubaniowski**: Dodajemy.

**Kamil Dubaniowski**: Tak jak Piotrek powiedział - nowe ustawienie.

**Piotr Buczkowski**: To jakby opcji dodajemy opcje do pola "Wymuś stosowanie", "Wymuś" tak.

**Damian Kamiński**: Walidacja.

**Piotr Buczkowski**: Sprawdź, sprawdź zgodność z maską tak, jeżeli niezgodne oczywiście może być puste pole, tak. Ale jeżeli jest wypełnione, musi... jeżeli są wypełnione, jest zaznaczone opcje, to zachowuje się jak pole walidowane. Bo tak samo możesz ustawić maskę NIP, wpisać 10 10 cyfr i przejdzie tak.

**Łukasz Bott**: To teraz pytanie, gdzie w tym zgłoszeniem w tym błędzie czy w tym?

**Piotr Buczkowski**: Myślę, że nie ten błąd, to trzeba... to jest niezależny błąd, to jest błąd tej funkcji **SendFieldInfo** że... tam ta zmiana da a i ten jest użyty w miejscu gdzie jest nie zadeklarowana.

**Kamil Dubaniowski**: Bardziej w tym zgłoszeniu Mateuszem.

**Łukasz Bott**: Dobra czy?

**Piotr Buczkowski**: To tam w tamtym pierwszym, tutaj, tak.

**Łukasz Bott**: Czyli w **Acceptance Criteria** piszemy następującym tak?

**Damian Kamiński**: No tylko o czym my nie wprowadzimy trzeciego typu pola w sensie?

**Piotr Buczkowski**: No nie. Znaczy ktoś kiedyś coś było, że odchodzimy od pola walidowanego, no to będzie przejęcie pola walidowanego w polu tekstowym. Funkcji pola walidowanego w polu tekstowym.

**Damian Kamiński**: OK, no właśnie, żebyśmy może to jednak jakoś ujednolicali i wtedy to co powiedziałeś, może ewentualnie dążyli do tego, że pola walidowane zostaną zlikwidowane.

**Piotr Buczkowski**: Możemy jak najbardziej, tylko to jest właśnie krok w tym kierunku.

**Damian Kamiński**: No byłbym za tym, bo to jest naprawdę według mnie... Ludzie tego nie rozumieją.

**Piotr Buczkowski**: No i to rozróżnienie nie jest proste, no tylko...

**Damian Kamiński**: Piotr, wiem, że jest proste, ale nie rozumieją.

**Piotr Buczkowski**: I nie, nie, nie ma komu to nie ma kiedy temu tego wytłumaczyć. Nie wiem, może na spotkanie z konsultantami w piątek tak krótki.

**Damian Kamiński**: Można to poruszyć, ale według mnie i tak zapomną. Nie po prostu systemowo tekstowe, tak jak powiedziałeś. Według mnie jestem za tekstowe matka [maska] plus dodatkowa wtedy walidacja i wtedy jest jeden typ pola, na którym można nałożyć różne cechy. Bo oni po prostu definiując, nie wiedzą, czy użyć tekstowego, czy walidowanego, do tego zmierzam.

**Piotr Buczkowski**: No to niech, niech się dowiedzą, że ktoś im powie. No sorry, nie można być kompletnym laikiem.

**Kamil Dubaniowski**: To tutaj jedyne co ich może mylić, to jest email, że jest tu i tu, bo jest e-mail jako pole walidowane i email jako pole tekstowe z maską, a reszta jest do uzasadnienia. No możemy powiedzieć, że te walidowane, które liczą sumę kontrolną właśnie jak PESEL, NIP, no to mamy jako walidowane domyślnie, bo one wręcz nie wdrożeniową nie powinny być inaczej wdrażane niż bez walidacji. A takie gdzie ta walidacja no może być ale nie musi, bo nie wiemy co jednak oczekuje użytkownik. Ten na przykład numer telefonu są, dyskutowaliśmy przed chwilą taksówkę taksówkarskie, numery, no to niekoniecznie musi być to pole walidowane, maska tylko podpowiada, ale nie jest walidacją.

**Damian Kamiński**: No tak i wtedy i wtedy masz łatwo z poziomu jednego pola. Czyli jak ustawiłeś sobie, że to jest pole tekstowe, nałożyłeś na nim maskę, to możesz trzeci krok zrobić bez konieczności zmiany, że teraz jeszcze chcę do tego dołożyć walidację, a dzisiaj musi zmienić typ pola, żeby to, żeby to wprowadzić tak, no i wtedy...

**Kamil Dubaniowski**: Tylko obawiam się jednej rzeczy. Zauważcie, że jak teraz mamy pole walidowane dedykowane i i ona waliduje, no to waliduje od początku. A jak będzie tekstowe z maską, a walidację ktoś włączy po 5 latach, to sprawy zaczną sypać błędami. Jeszcze mogą być na etapie takim, że już są tylko do odczytu. Więc to też trzeba zabezpieczyć.

**Damian Kamiński**: No a jak zmienisz? A jak zmienisz sposób walidację na polu to też będzie to samo.

**Piotr Buczkowski**: No nie, bo może w każdej chwili zmienić walidację z NIP na PESEL i wykrzaczyć cały proces.

**Damian Kamiński**: Tak. To to to samo, no to znowu można ograniczyć to tak jak nazwę, że pod zmianą walidacji jest ostrzeżenie tak, że możesz stracić dane.

**Kamil Dubaniowski**: Tylko będzie ci sypał błędem, że to ta wartość jest...

**Damian Kamiński**: No czy będzie sypało błędem? No więc jakieś tam ostrzeżenie, wtedy można. Dobra, słuchajcie, warto to zaopiekować według mnie.

**Kamil Dubaniowski**: No tak, no ale to wtedy tak to ktoś zdejmie walidację, taką ujednolici dane i dopiero ją włączymy. To ktoś mu zgłosił, jakby jeśli nie ma tu ryzyka faktycznie utraty danych, no to to OK. Jedyne ryzyko to wysypią proces. Ale to to, co Rossnie [Rossmann?], który zgłosił. Jak się nie da przesłać spraw dalej, a nie da się tych pól edytować.

**Damian Kamiński**: No bo dzisiaj to jest właśnie to, co pokazał tu Piotr. Na tym zgłoszeniu swoim to według mnie jest powód, dlaczego stosujemy pola tekstowe, a nie walidowane, bo na polu walidowanym nie można wyświetlić tego ładnego... Ładnej grafiki z prefiksem tak, że właśnie wtedy ono już sugeruje, że jest...

**Kamil Dubaniowski**: Czyli po prostu nie wyświetlamy tak, bo to była ta decyzja, że idziemy...

**Damian Kamiński**: No po prostu to ładnie determinuje, że od nawet nie czytając już wiem, że tu wskakuje numer, nie? Nawet nie czytając labela a na walidowane no brzydziej to wygląda, więc myślę, że to jest słuszny kierunek, że te walidację powinniśmy przenieść na na pola tekstowe i docelowo i wtedy będzie to spójne.

**Łukasz Bott**: Czyli na na maski taka ten na obsługę masek a ten...

**Damian Kamiński**: Znaczy, niezależnie na polu tekstowym, może zrobić i walidację i maskę.

**Łukasz Bott**: OK dobra. Dobra, zajmujemy się to, w którym sprint?

**Kamil Dubaniowski**: Łukasz, tutaj jeszcze no, bo nie rozwiążemy do końca tematu tak naprawdę tym, co tu opisałeś w momencie, kiedy ktoś nie włączy wymuszania walidacji, to jak zaznaczamy, że jest niezgodne z maską. No bo też trzeba dać sygnał, chyba, że nie właśnie, że wtedy nie ma nic.

**Damian Kamiński**: Tak jak teraz jak dwukropek jest no to to jest znak niezgodny tak, ale on przepuścił. Że masz na myśli, że...

**Kamil Dubaniowski**: Chodzi mi o to, że zaznaczyć, żeby użytkownik zauważył "kurde, wkleiłem dwukropek". A nie ma wymuszania zgodności związku?

**Damian Kamiński**: No ale tam będzie informacja tylko puści dalej. To będzie informacja, że pole jest źle wypełnione, ale przez to, że nie ma walidacji, to masz możliwość zapisania.

**Łukasz Bott**: Także nie nie, jeżeli nie włączył wymuszenia zgodności z maską, to... bo tam pójdzie no.

**Damian Kamiński**: No to już wtedy ktoś, no w sensie wszystkie narzędzia są: albo wprowadza walidację na sztywność, wtedy nie można zapisać, nie przejdzie dalej, albo tylko informuję je, ewentualnie robi walidację pod przyciskiem.

**Kamil Dubaniowski**: Właśnie o to mi chodzi, że że w takiej sytuacji, kiedy konsultant ustalił z klientem, że tu będą czasami numery komórkowe, a czasami będą numery taksówek, no to ja bym nie chciał czerwonego pola jak ktoś pisze 4 4. A będę miał, nie będę nie będzie na pewno tak OK. Tylko błędne znaki.

**Damian Kamiński**: No. Ale nie będzie nie będzie, no nie, nie, nie, nie, tu czerwone pole będzie tak tylko przy dwukropku. O ile nie włączyłeś walidacji, tak która wymagałaby 4-9 cyfr. To będzie tylko maska i maska poinformuje, że masz niezgodne.

**Damian Kamiński**: Nie, bo maska już wprowadza pewien element, może tak maska wprowadza pewien element walidacyjny, ale tylko co do rodzajów znaków tak, czyli maska nie pozwala wprowadzić dwukropka albo inaczej informuję, że dwukropek jest niezgodny z maską, ale to nie ma żadnych konsekwencji wstrzymujących tylko informacyjne.

**Damian Kamiński**: No to nie wiem co w sensie to jeszcze raz, że wprowadzając maskę tylko informujesz, że to jest niezgodne z maską i w takim wypadku informujemy, że numer telefonu posiadający dwukropek jest niepoprawnym według nas, ale puszczamy dalej.

**Anna Skupińska**: Tak.

**Damian Kamiński**: Ale możesz wprowadzić i 4 znaki, 5 znaków i 10 znaków. Numer... numerów w sensie i wtedy będzie to poprawne. Nie będziemy podświetlać tego na czerwono w zależności od ilości znaków, a jak wprowadzisz walidację, że ma być określona ilość znaków? No to wtedy już to ma konsekwencje blokujące.

**Łukasz Bott**: A jest tak szczęśliwa, dobra?

**Anna Skupińska**: A przepraszam, a po prostu jestem trochę chora.

**Damian Kamiński**: Dobra w polu krótkiego tekstu z włączoną maską pojawia się dodatkowy wyznacznik "Wymuś zgodność z maską". Jeśli znacznik jest zaznaczony i pole jest wypełnione... Tylko co to znaczy wymuś zgodny z maską?

**Piotr Buczkowski**: Jeżeli jeżeli niezgodne. No teraz się pojawia czerwony na czerwono, tak? Jak jest niezgodne z maską, ale zapisuje i pozwala przejść dalej. A wtedy nie będzie pozwalał, nie będzie zapisywał, nie będzie pozwalał przez dany przejść dalej tak. Tak gdzieś pisał niepoprawny NIP.

**Damian Kamiński**: No no dobra OK. Ale to teraz jaka jest maska w sensie czy my tą maskę mamy zdefiniowaną per kraj?

**Piotr Buczkowski**: Na pow... Bo przecież w polu masz.

**Łukasz Bott**: Tak.

**Damian Kamiński**: Tak dobra, no po prostu tego nie wiem. Nie, nie testowałem czy...

**Piotr Buczkowski**: To samo, to samo, co powoduje, że teraz jest wyświetlane na czerwono.

**Łukasz Bott**: Tak, tak, tak to jest spójne.

**Damian Kamiński**: OK.

**Piotr Buczkowski**: Dodatkowo będzie powodowało brak możliwości przejścia. Dalej nie będzie zapisana ta wartość.

**Damian Kamiński**: No dobrze, to teraz dodatkowe pytanie: czy... już patrzę jakie tu mamy maski.
W sensie, czy dla każdej maski będzie ta opcja? To jest maska **Number** na przykład.

**Piotr Buczkowski**: Nie wiem.

**Damian Kamiński**: Czy robimy to na razie drobnymi krokami, czyli tylko dla? Opcja tylko dostępna dla...

**Piotr Buczkowski**: Już kwestia przetestowania jak to działa. Czy się da łatwo zrobić dla telefonu? Warto zacząć od telefonu.

**Damian Kamiński**: Telefonu.

**Łukasz Bott**: Dobra.

**Piotr Buczkowski**: Trzeba po prostu według mnie dla wszystkich powinno być, tak. I po kolei przetestować każdą maskę jak się zachowuje i ewentualnie poprawić.

**Damian Kamiński**: Mhm, no dobra, to może to dopiszmy. Żeby to też były jasno napisane, że trzeba to zrobić dla wszystkich masek i trzeba przetestować to dla wszystkich masek.

**Kamil Dubaniowski**: To widzę, że te kredytowe formularze... że jest od razu do zmiany, bo jak wybierzesz pole walidowane, no to...

**Damian Kamiński**: To co?

**Kamil Dubaniowski**: No. W sensie tak jak domyślnie i w ogóle lista od razu jest na sam dół przeskrolowana i też pytanie, czy to nie powinno od razu mnie zapytać? No bo to jest kluczowe akurat w tym wypadku.

**Damian Kamiński**: Wyrażenia regularne. Ta pusta i na pomarańczowo, nie?

**Kamil Dubaniowski**: Ale chcę przetestować właśnie różnicę jak wygląda e-mail na przykład.

**Łukasz Bott**: To słuchajcie, no rozumiem, że co? Zostawiamy to na ten sprint, ktoś się tym zajmie, czy czy dajemy to na kolejny sprint? Nie wiem, to jest PBI.

**Kamil Dubaniowski**: Dobra to... Ja bym to jeszcze chyba wolał lepiej przemyśleć, bo zrobimy znowu tak na szybko.

**Damian Kamiński**: Tak, idzie w **Backlog** i **In Design**. Pytanie: Ty to Kamil bierzesz?

**Kamil Dubaniowski**: Mogę wziąć.

**Łukasz Bott**: **Backlog**. Na Kamila. I **In Design**, tak. Zdejmuję z Rady. Kończymy powoli, tak? Już mocno po czasie jesteśmy.

**Damian Kamiński**: Dobra.

**Łukasz Bott**: No dzięki.

**Damian Kamiński**: Na razie.

**Łukasz Bott**: [zatrzymano transkrypcję]
