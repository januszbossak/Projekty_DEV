**Data spotkania:** 3 grudnia 2025, 10:16 - część 5

---

**Janusz Bossak:** I on nie ma nic wspólnego z jakąś nadrzędną sprawą, do której my chcemy go.

**Damian Kaminski:** Dokładnie, że ten byt jest wirtualny, że to jest równoległe procesy, sprawy są równoległe.

**Janusz Bossak:** Po to jesteśmy w domu. Dobra, ja ciągle ja mam w głowie, że my chcemy spiąć.

**Damian Kaminski:** Z czymś spinać? Nie, nie właśnie, chcemy kontynuować, o tak to nazwijmy.

**Janusz Bossak:** Nie ma ich korespondencja przychodząca i wychodząca i że wszystko to chcemy spiąć, tak jak JRWA do jakiejś teczki tej sprawy. A my chcemy po prostu technicznie śledzić, co się stało z dokumentem, który wpadł do nas z e-Doręczeń.

**Damian Kaminski:** Tak, tak. Teraz dokładnie może na to teraz przełożyć na to, jak działa Orlen. To drugi przykład analogiczny. Wpływa dokument, który wpływa do specjalnego procesu w zasadzie w formie JSON. My w AMODITcie dopiero go tworzymy. To jest jeden proces, potem kolejny proces. Ten dokument biegnie do procesu podpisywania i tam ma pełen obieg procesu podpisywania. A potem ten sam dokument, tam jest dokładnie ten sam. My nie robimy kopii, żeby go nie multiplikować. Na koniec wpływa do e-teczki. I cała historia biznesowa to jest utworzenie dokumentu w jednym procesie, podpisanie dokumentów w drugim procesie, tak wysoko poziomowe, i w trzecim procesie wpięcie do teczki.

**Janusz Bossak:** OK.

**Damian Kaminski:** Nie ma nic nadrzędnego, jest wszystko ciąg.

**Janusz Bossak:** Dobra, ale jakby jedno drugiemu nie przeczy. Teraz mamy tylko rozumienie.

**Damian Kaminski:** Tak, tak, tak.

**Janusz Bossak:** Pomysł Łukasza według mnie trzeba zrealizować. Znaczy wywalić tego message'a, te rzeczy, które są tam powtarzalne, czyli ten subject to ID. Nie wiem czy name. Do tej tabeli osobnej po to, żeby można było po tym raportować. A co my tam będziemy wrzucać w tym type, czy to będzie CaseID, czy tam cokolwiek innego, czy user ID, czy grupa ID, czy może jeszcze jakieś inne rzeczy? Może raport ID, nie wiem, nie mam pojęcia. To będzie nam spinało te rzeczy, które chcemy. I tu w tym przypadku będziesz używał, powiedzmy tej pierwotnej sprawy e-Doręczeń.

**Damian Kaminski:** To będzie rozwojowe.

**Janusz Bossak:** Żeby wiedzieć z czego się to wzięło i tyle i koniec. I będziesz miał historię tego.

**Damian Kaminski:** No właśnie, dobra, to ja jeszcze skomplikuję. Bo czy pierwotnej sprawy, bo teraz załóżmy, że to są faktycznie trzy osobne procesy i trzy osobne sprawy. One jedne z drugich wynikają, ale to nie jest przepisanie AssignProcedure, tylko to są odrębne sprawy. I teraz pytanie, na każdej z tych spraw, jak powinna się prezentować historia biznesowa? Czy ona powinna być spójna dla każdego tego obiektu? Teraz mamy powiedzmy jeden byt wirtualny w postaci dokumentu obsłużony w trzech różnych sprawach.

**Janusz Bossak:** Ale w trzech różnych sprawach, czekaj, zanim się pojawiły te trzy różne sprawy, musi być Big Bang. Czyli pierwszy wielki.

**Damian Kaminski:** Mhm. To pierwsza sprawa, sprawa procesu pobierania korespondencji z e-Doręczeń. To jest pierwsza sprawa.

**Janusz Bossak:** No, no i.

**Damian Kaminski:** Później idzie to do procesu obiegu korespondencji X, potem.

**Janusz Bossak:** Ale jak idzie, ale jak idzie?

**Damian Kaminski:** Automatem.

**Janusz Bossak:** No właśnie.

**Damian Kaminski:** Na podstawie parametrów, przyszło od takiego, od czytania treści czy co tam sobie analizy. Automatem idzie.

**Janusz Bossak:** Ale automat co robi? Robi ten proceder, ten create?

**Damian Kaminski:** Nie, nie, klientka jest, robi.

**Janusz Bossak:** Dobrze i teraz w tym momencie create tą pierwotną sprawę.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** To że powstało w tym ten numerek, ten identyfikator przepisujesz.

**Damian Kaminski:** OK.

**Janusz Bossak:** I to jest ten, to jest to nasza teczka.

**Damian Kaminski:** Dobrze.

**Janusz Bossak:** Tak, to jest ta nasza teczka. I tyle ile teraz dalej, co jeszcze powstaje?

**Damian Kaminski:** Mhm. To teraz powiedzmy powstaje sprawa w procesie obiegu korespondencji X.

**Janusz Bossak:** Mówię, że czyli innym niż ten przed chwilą powiedzieliśmy.

**Damian Kaminski:** Tak, tak, no pobieranie jest w procesie technicznym.

**Janusz Bossak:** Ale dobrze, no i ale to są nie, nie rozumiem.

**Damian Kaminski:** Dobra, momencik, momencik, już rozrysujmy to sobie, bo to będzie łatwiej.

**Janusz Bossak:** Jeszcze raz.

**Damian Kaminski:** Ojej, jak to się nazywa ten program? Dobra, już, już. Czyli mamy tak. W zasadzie to powinniśmy to ustawić tak i tu mamy, czyli tak tu jest. Techniczny pobieranie z e-Doręczeń już powiększa. OK. Tak wygląda nasz przypadek w ujęciu procesów, czyli to też są trzy różne byty, bo w każdym z tych procesów powstaje jedna sprawa. I teraz pytanie jest takie, jak ma wyglądać historia biznesowa dla tych trzech spraw, bo one są ze sobą powiązane, zależnie niezależnie, bezpośrednio, niebezpośrednio. Pytanie czy ona ma być spójna i taka sama dla wszystkich trzech obiektów czy inna?

**Janusz Bossak:** No ale.

**Damian Kaminski:** Rozumiesz?

**Janusz Bossak:** Znaczy to zależy co my chcemy. Według mnie to jest ta sama historia. Bo jeżeli uznajemy, że to jest to samo.

**Damian Kaminski:** No.

**Janusz Bossak:** To powinniśmy posłużyć się tym pierwotnym. Czekaj się przełączę. Dobra.

**Damian Kaminski:** Dobra, załóżmy, że jest ta sama.

**Janusz Bossak:** Wyłączony ten kończyłem na dużym ekranie. I chodzi mi o to, że techniczne pobranie e-Doręczeń jest pierwotnym aktem.

**Damian Kaminski:** Tak wygląda, tak.

**Janusz Bossak:** I tu i tu napisz tam jakiś ID obok tego technicznego pobierania e-Doręczeń na sprawie tam na dole przy tym kwadraciku.

**Damian Kaminski:** OK.

**Janusz Bossak:** To tu jest jakieś ID, jakieś tam.

**Damian Kaminski:** Jeden jest jeden.

**Janusz Bossak:** Powiedzmy, że ID jeden. Obiegu korespondencji X powstanie jakieś ID dwa?

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Ale do historii biznesowej, znaczy będziesz miał pole, który mówi o, nazwijmy je sobie teczka, albo spinacz, albo cokolwiek, bo źródło prawdy, jakkolwiek to nazwać. I tam będzie ten numerek jeden, ten ID jeden. I jak obiegu korespondencji X przejdziesz na obieg korespondencji Y, to też przekażesz ten numerek jeden. To jest ciągle to, co powstało z tych e-Doręczeń. Ja to tak rozumiem.

**Damian Kaminski:** Dobra, czyli tak mamy załóżmy CaseID i mamy connected. Na razie tak to nazwijmy. I dobra, czyli tutaj wstawiamy, czyli tutaj wstawiamy CaseID, tu jest jeden, tu nie ma, tu jest null, bo tu nic nie mamy, czy też stawiamy jeden od razu?

**Janusz Bossak:** No i to nie to jest, tu jest no.

**Damian Kaminski:** Null, OK. Dobra, teraz jedziemy dalej, mamy tutaj.

**Janusz Bossak:** No może tak z punktu widzenia potem przeszukiwania to tak to może być case connected, tam jest jeden. Tak, dobrze mówisz?

**Damian Kaminski:** Dobra, załóżmy, że jest jeden. Mhm. Tutaj mamy dwa.

**Janusz Bossak:** To jest dwa, a tam jest jeden.

**Damian Kaminski:** A tam jest jeden. Tu mamy trzy.

**Janusz Bossak:** Jest jeden, tak.

**Damian Kaminski:** Trzy jest jeden.

**Janusz Bossak:** Dokładnie i to jest ten ID tam SubjectID, który jest tym.

**Damian Kaminski:** Dobra. OK, to jest baza danych teraz. Teraz jak to?

**Janusz Bossak:** No dlatego to ten przypadek nie pasuje do tego, co tam zaprojektowałaś. Bo to co zaprojektowałeś i to jak to powinno być tam wyświetlane, to jest historia biznesowa sprawy. To jest ten pomysł, który był na etapie rozwiązywania problemów MSIT, że w tym procesie, tym konkretnym jednym, nie przechodząc przez te różne inne procesy, w tym konkretnym jednym procesie chcemy uchwycić biznesowe momenty biznesowe zdarzenia, że po 15 iteracjach uzgadniania mamy ostateczną decyzję. I jak ludzie patrzyli na zwykłą historię, to mieli cofnięto, poprawiono, cofnięto, poprawiono, odrzucono, cofnięto i tak dalej. A w historii biznesowej będzie miał wniosek wpłynął wniosek, przeanalizowany wniosek, zatwierdzony. Koniec. I o to chodziło.

**Damian Kaminski:** Mhm. Mhm, dobrze, czyli każda z nich wyświetla.

**Janusz Bossak:** Że był swoją historię biznesową, swoje punkty, które są z tym związane. Natomiast może teraz nie wiem, jak jeszcze. Dlatego mówiłem o tym obiekcie typu raport osadzony na formularzu, który ci pokaże wszystkie connectedCaseID. I ci pokażę zdarzenia tego pierwszego procesu tej sprawy, CaseID jeden. To może tam już było jakieś zatwierdzenie, jakieś przypisanie, jakieś coś. Potem zbierze to co jest pod dwójką, to pójdzie chronologicznie według dat, co tam się wydarzyło. Bo to nie jest tylko tak, że w obiegu korespondencji będzie jeden etap. Może były dwa, może coś tam się dzieje.

**Damian Kaminski:** No właśnie, no właśnie.

**Janusz Bossak:** Może tam się coś działo i dopiero ktoś coś zdecydował. Ale też zdecydował, żeby to się wpisało do tej historii biznesowej. Cała idea tej historii biznesowej bierze się tylko i wyłącznie stąd, żeby tam wpisywać ostateczne te decyzje, nie wszystko co się dzieje w tym.

**Damian Kaminski:** Tak, kluczowe rzeczy.

**Janusz Bossak:** Tak, bo to nie muszą być ostateczne. Może być właśnie ta historia poprzedzająca, jeśli wiemy, że taki jest, że to jest kluczowe, dla rozumienia tego obiegu.

**Damian Kaminski:** Bo tutaj można by wziąć, tak jak masz ten prawy panel. Rozumiem, że mockup na razie, ale historia to nie jest historia formularza, tylko to jest historia szczegółowa, a tu jest biznesowa.

**Janusz Bossak:** Tak, tak, tak.

**Damian Kaminski:** No ja to też wcześniej nazywałem szczegółową właśnie formularza, a biznesowa to jest jakiegoś wyższego. Może być tego bytu, może być właśnie wyższego biznesowa. Nie definiuję czego. To nie musi być to jest ta sprawa, to może być coś więcej. Formularza nazwałem to, bo tak było na projekcie Cristiny, więc wcześniej miałem szczegółowa, biznesowa. Tu pól, to jest przyszłość jakaś, to na razie nic nie ma.

**Janusz Bossak:** Wiesz, może być tak, że jeżeli tutaj wyświetlamy tą historię, to ta historia weźmie to CaseID z tej twojej tam tabelki. Historia biznesowa to weźmie CaseID, czyli jedynkę.

**Damian Kaminski:** Znaczy według mnie powinno brać wszystko, powinno brać CaseConnected i wyświetlać wszystko. Czyli każda z tych spraw wyświetli wszystko. Tylko teraz pytanie pozostaje, czy to wyróżnić i wtedy jak, że.

**Janusz Bossak:** No, no, no. Może tak, chodziło mi o to, żeby był przełącznik, który właśnie przepinać i na to i na to. Znaczy albo na to, albo na to. Albo chcesz obejrzeć historię biznesową tej sprawy pojedynczej tej ID jeden.

**Damian Kaminski:** Chronologicznie. OK.

**Janusz Bossak:** Albo chcesz obejrzeć tą historię tej teczki?

**Damian Kaminski:** Tak.

**Janusz Bossak:** Prawej, którą ta sprawa jest wpięta. Czyli obojętnie, czy będziesz w CaseID 1, 2 czy 3, zawsze możesz się przepiąć, znaczy przełączyć to wyświetlanie na tą jakby teczkę wyższą. I zauważ, to nam rozwiązuje też potem kwestię na przykład JRWA. Bo tak samo w tym connected będzie ta teczka JRWA i będziesz widział wszystko co się z tym wiąże. Nie tylko tą jedną sprawę, ale na przykład tam zobaczysz.

**Damian Kaminski:** Tak.

**Janusz Bossak:** Korespondencję przychodzącą i wychodzącą, cokolwiek innego, umowę. Bo będziesz mógł się w każdej chwili będąc na pojedynczej sprawie amoditowej zobaczyć historię teczki tej sprawy. To jest genialne, po prostu, jeżeli tak będzie.

**Damian Kaminski:** Tak, tylko i jeszcze więcej bym powiedział, że to co powiedziałeś, można mieć tu kontekst. Pokaż tylko tą, pokaż wszystkie. A w tym pokaż wszystkie można mieć jeszcze filtr. Pokaż mi tylko umowy, bo to jest nazwa wpięcie umowy.

**Janusz Bossak:** Na przykład.

**Damian Kaminski:** I to jest jeszcze do jeszcze zagnieżdżenia, bo w kontekście JRWA i teczek tego może być po prostu dużo. I ja chcę zobaczyć tylko pięć, których szukam, a nie 150.

**Janusz Bossak:** Dokładnie, tak, dokładnie. Znaczy to już jest jakby kolejny feature. Ale to przypinanie się pomiędzy kontekstem tej konkretnej sprawy, w której jesteś, a kontekstem sprawy, której ta sprawa dotyczy, jest tutaj kluczowe.

**Damian Kaminski:** OK.

**Janusz Bossak:** I teraz wrócę do wątku wielowymiarowości. To jest wątek jednowymiarowy, że ta sprawa jest połączona z jedną jakąś tam sprawą. A mikrofon?

**Damian Kaminski:** No właśnie, ale powiedz, powiedz.

**Janusz Bossak:** Także jak masz to przyjęcie doręczenie z CaseID, CaseConnected jeden, ale może nie w tym przypadku Rossmanowym, ale jakimś innym, jak chcę to przypiąć do polisy. I napisać, że to jest polisa numer 58. Bo chcę tą samą sytuację widzieć przez pryzmat polisy. Ale tą samą sytuację chcę widzieć przez pryzmat klienta, który o tą polisę. Więc to jest ta wielowymiarowej, że to co tu napisaliśmy sobie CaseConnected, CaseID.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** To musiało być tabelą, bo to mogę po prostu chcieć tą moją pojedynczą amoditową sprawę podpiąć w różne konteksty, to samo zdarzenie.

**Damian Kaminski:** O tak.

**Janusz Bossak:** Na przykład wchodzącym mail albo telefon wykonany, bo to jest telefon od tego klienta. Ten telefon dotyczy polisy czy tam reklamacji czy czegoś. Więc tu może być potrzebna wielowymiarowość.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** To Łukasz, jakbyś planował, to trzeba o tym sobie pamiętać.

**Damian Kaminski:** Czyli wtedy by było tak, o to ci chodzi, że to jest podpisanie polisy dwa. I teraz te kafelki uznaję jako sprawy w jednym procesie, ale tu może być jeszcze trzeci element, czyli nie polisa.

**Janusz Bossak:** Możemy.

**Damian Kaminski:** Czyli już niejako też jako sprawa, ale innego procesu, czyli faktura.

**Janusz Bossak:** Na przykład tak, bo wypłata roszczenia, coś tam.

**Damian Kaminski:** Dokładnie. Dobra, tylko jeszcze to co powiedziałeś, że można się przełączyć w kontekst albo wątku, albo tej sprawy. Bo wątek nazywam tym wirtualnym obiegiem. To teraz się zastanawiam, czy ten kontekst wątku z racji, że tu są trzy procesy, a nie dwa, czy tu czegoś nie przegapiam?

**Janusz Bossak:** Nie bardzo rozumiem wątpliwość. Znaczy mamy ten kontekst connectedCaseID jedynkę, to jest OK. To nam spina te trzy rzeczy. I to nie ma znaczenia, gdyby to powstawało jedno z drugiego.