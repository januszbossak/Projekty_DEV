**Transkrypcja**

18 grudnia 2025, 09:08AM

**Anna Skupinska** 0:06  
Cześć.

**Janusz Bossak** 0:08  
Cześć.

**Anna Skupinska** 0:09  
Czy jesteś nagrodę?

**Janusz Bossak** 0:12  
Podobno jest.

**Damian Kaminski** 0:12  
Jest bardziej taki temat koncepcyjny niż deweloperski.  
Ja chciałbym po prostu przedstawić pewien.  
Aspekt i zapytać, czy czy się zgadzacie z moją wizją tego, czy czy czy są to jakieś zagrożenia. Dobra, więc przechodząc do rzeczy.  
Na przykładzie tego, że za chwilę nam wejdzie i mamy właśnie te obiegi faktur poufnych powiedzmy to i ogólny obieg faktur.  
No to trzeba to w jakiś sposób dzielić najprostsze co mi przychodzi do głowy.  
Mm.  
Pewnymi.  
W pewnym poziomem wejścia jest to, żeby jeśli.  
Proces faktur poufnych jest, jeśli jeszcze nie istnieje, to z natury był kopią procesów faktur ogólnych, żeby zachowywać wszystkie pola.  
Jednocześnie, jeśli jest to zintegrowane z krzewem, to ten proces faktur poufnych powinien być procesem, który jest zasilany przez ksf. Natomiast później na tym procesie działa jakaś reguła cykliczna, która.  
Powoduje, że jeśli nip kontrahenta wystawiającego fakturę nie znajduje się w jakiejś puli określonych nip, ów to następuje, a sejm proceder.  
I jest przepisanie tej sprawy do procesu docelowego.  
Z przeniesieniem wszystkich pólce do ich wartości i tak dalej.  
Można ewentualnie czy też alternatywnie zrobić 3%, czyli sam proces taki inicjujący.  
I proces faktur poufnych i zwykłych, ale nie wiem czy to jest potrzebne, bo w zasadzie tu mamy wtedy zachowaną taką.  
Sytuacja, że nic na faktury ogólne nie wpadnie przypadkowo, bo tylko, bo najpierw wpada na na faktury poufne i potem jest dopiero przekazywane jeśli.  
Jest spoza, powiedzmy jakiegoś określonego zbioru wyników.  
Testowałem nawet stoi, działa.  
Akurat na przypadku takim uproszczonym, ale, ale sprawdziliśmy to i no i pytanie czy.  
Czyli widzicie jakieś zagrożenia w tym kontekście czy jakieś ryzyka? Czy macie lepszy pomysł jakiś inny?

**Janusz Bossak** 2:45  
Znaczy, ja nie mam pomysłu na razie jakoś.  
Znam się trochę, że pół uchem słuchałem, może dlatego.

**Damian Kaminski** 3:08  
Okej, no to znaczy problem. Pojawi się wtedy, że gdy to znaczy może inaczej generał problemu jest to, że no teraz mamy po prostu jeden jedno źródło.  
Danych tak w postaci sefa, więc wszystko musi trafiać do jakiegoś jednego miejsca, no i.  
I klienci po prostu będą od nas oczekiwać, żeby to zaopiekować.

**Janusz Bossak** 3:38  
Kiedyś w ogóle była koncepcja.  
By różnego poziomu poufne.  
Różnych dokumentów.  
To jest jedna rzecz, którą można tu rozważać, druga.  
To jest jakaś klasyfikacja ta, która powinna się odbywać.  
Najlepiej automatyczna.  
Która powoduje, że coś trafia na kod, że tak powiem poufny i idzie ścieżką poufną, a druga, że trafia na jakiś kot normalnej idzie normalność ciężką.  
Przy czym?  
Pamiętam jak w PE nie to było jak.  
Bardzo to było rozdzielone.  
To tam chodziło akurat o faktury bitu, czyli pracownicy, którzy są znaczy współpracownicy tak, którzy są na bip bip.  
To do tego stopnia, że jak oni przynosili faktury ręcznie.  
To chodziło o to, żeby mają zanosić w ogóle do innego sekretariat.  
Do sekretariatu działu kadr, a nie do sekretariatu głównego.

**Damian Kaminski** 4:48  
No bo.  
Mhm.

**Janusz Bossak** 4:55  
I cały ten proces był zdublowany. W sensie był drugi proces identyczny jak proces normalny do obiegu faktur.

**Damian Kaminski** 5:03  
I tak to wygląda.

**Janusz Bossak** 5:04  
Tylko, że służył do bitu bi no tam po prostu były.

**Damian Kaminski** 5:06  
Tak tak, tak, żeby odrębne raportowanie i wszystko.

**Janusz Bossak** 5:09  
Tak odrębne raportowanie, inne osoby do akceptacji, tak?

**Damian Kaminski** 5:10  
I też uproszczona ścieżka przeważnie, bo to jest poufne, to my mniejsza ilość osób jest zaangażowanych.

**Janusz Bossak** 5:16  
I tam nawet nie chodziło o poufność w rodzaju, że są jakieś pola szyfrowane i tak dalej, tylko że proces jest rozdzielony tak procesie uczestniczą zupełnie inne osoby.

**Damian Kaminski** 5:17  
No.  
Tak, tak.  
I tylko o to mi chodzi to jako baza, bo wtedy ten proces można kliknąć. On jest niedostępny w kontekście danych administratorowi. Oczywiście pozostaje cała kwestia dostępu do danych z poziomu bazy danych, ale to już jest kolejny poziom gdzieś tam wtajemniczenia i tego i tak nie rozwikłamy. To jest często poza nami, jeśli chodzi o on premises, a z kolei chmurową, no wtedy ktoś nie ma dostępu, a nasi serwisanci mogą mieć, że tak powiem mi i tutaj wspierać, więc to by wystarczyło. No jeśli nie macie lepszego pomysłu to bym bym to tak zostawił.

**Janusz Bossak** 5:32  
Do.

**Damian Kaminski** 5:55  
Czy też nie widzicie jakieś rydzyk natomiast.

**Janusz Bossak** 5:59  
Znaczy, potrzebujesz tego klasyfikatora, który stwierdzi, jeżeli to wszystko przyjdzie jednym korektorem krzew.

**Damian Kaminski** 6:05  
No to Jeszcze raz powtórzę, bo może nie dobrze słuchałeś to Jeszcze raz. Ja proponuję, żeby w przypadku 2 procesów, czyli procesu obiegu faktur tajnych i po prostu procesu obiegu faktur.

**Janusz Bossak** 6:05  
No to.  
Że jakoś mi umknęły ten moment, no.

**Damian Kaminski** 6:17  
To proces faktur tajnych był inicjowa.  
Wskutek połączenia chce connector, czyli chce w connector ładuje do procesu faktur tajnych. Tam działa reguła cykliczna, która sprawdza, czy nip kontrahenta, który wystawił fakturę, jest w puli użytkowników w kontrahentów tajnych. Jeśli nie jest to następuje przepisanie sprawy do innego procesu, czyli ja sam proceder do tego głównego do głównego procesu, a jeśli nie, no, to zostaje na tym procesie i tyle.

**Janusz Bossak** 6:38  
No.  
No i bardzo dobrze.

**Damian Kaminski** 6:49  
Dobra natomiast.

**Kamil Dubaniowski** 6:50  
20. Też pod uwagę, że to nie zawsze jest kwestia kontrahenta, nie to się trochę skomplikuje i.

**Damian Kaminski** 6:55  
Mino to już kwestia reguł, nie?

**Kamil Dubaniowski** 6:57  
Tak no bo wszystkie gdzieś tam wystawione na prezesa często idą tajnym, żeby tam ludzie nie wiedzieli co tam. Prezes na delegacji wydał.

**Damian Kaminski** 7:05  
No to już wtedy muszą to powiedzmy jakieś dodatkowe warunki uwzględnić.

**Janusz Bossak** 7:06  
Ale to.  
Znaczy może być taka lista?  
Słownik czy coś tych ników i tam można dopisać nie prezesa, tak.  
Czy cokolwiek tam no nie wiem jakoś.

**Damian Kaminski** 7:21  
Będę no tutaj bardziej wydaje mi się, że kamilowi chodzi o koszty, które prezes wygenerował i nie chce się z nimi tutaj chwalić wszystkim działom, bo faktura powiedzmy wpada to takie, ale według mnie to i tak wpadnie do grupy księgowości, która wie najwięcej i wie też o tych kosztach, bo ktoś musi ustalić z tego odbiorcy tej faktury, a to wtedy wpadnie do właśnie takiej grupy, która no ma najszerszą wiedzę w kontekście kosztów. Nie ma, ona będzie musiała zdecydować na podstawie swojego doświadczenia.

**Janusz Bossak** 7:24  
Czy to może nie?

**Damian Kaminski** 7:52  
Gdzie i jak?

**Janusz Bossak** 7:53  
Znaczy z tym psem jest więcej problemów? Tak, no bo teraz to fizycznie ktoś przynosi papier i wiadomo kto przynosi.

**Damian Kaminski** 8:02  
Tak.

**Janusz Bossak** 8:03  
A i tak samo.

**Damian Kaminski** 8:03  
No dlatego wariancie robimy ten projekt.

**Janusz Bossak** 8:05  
Dokładnie, a tak i tak samo, nawet jeżeli wysyłam mailem taki prezes do sekretariatu to też wiadomo, że to mail, że to prezes przysłał i to jego delegacja nie albo jego.

**Damian Kaminski** 8:16  
Znaczy w ogóle ten kontekst aliansu, to według mnie powinniśmy dobrze było popełnić o tym jakieś takie.  
Jej study jak my opiekujemy, bo mogło to być dobrem marketingową i się tym pochwalić, że właśnie mamy taką matrycę, gdzie?  
Gdzie ta cała ścieżka faktur będzie zarządzana na podstawie różnych parametrów od kontrahenta, poprzez nazwy pozycji, poprzez Informacje dodatkowe na fakturze? Tam mogą różne kwestie określić i na tej podstawie definiujemy ścieżki biznesowe. Tam jedną z 20.

**Janusz Bossak** 8:33  
Znaczy.  
Znaczy mi to.  
Znaczy, my tu wręcz wiesz idealnie pasuje agent jainy, który to robi agent, który dostaje jakby instrukcje.

**Damian Kaminski** 8:57  
No tak, tylko na razie go nie mamy, nie wszystkie duże firmy chcą wpuszczać agenta. Ja do takich danych nie.

**Janusz Bossak** 9:00  
Ja wiem, no wiem, ale.  
Masz aż się prosi, że tak powiem o to jest dokładnie takie. No takie agent klasyfikacyjne nie czyli.

**Damian Kaminski** 9:10  
Dobra, to jeszcze jeszcze na wracając do wątku głównego, bo tak we wszystkich nowych wdrożeniach albo w miarę nowych, gdzie one już były dostosowane pod krzew, czyli powiedzmy do ostatniego 1,5 roku.  
Ee to nie ma problemu, natomiast we wszystkich starych.  
Może być z tym problem, bo te procesy mogą istnieć niekonieczne mogą być kopiuj, to już omawiałem wstępnie z Piotrem, tylko chciałbym piotrze, żebyś jeszcze mi potwierdził, bo jak dla mnie to.  
Takim najniższym progiem wejścia i bym zrobił zaraz na to zgłoszenie, to jest dodanie fory, czołg gdzie już obsługujemy xm LI pub tylko żeby ten xm l mógł być definiowany jako nazwa pola.  
Czy to tutaj w jakiś sposób?

**Lukasz Bott** 9:59  
Z Opola z plikiem tak.

**Damian Kaminski** 10:01  
Nazwa pola z plikiem, czyli kse fin wojska fail tak czy jak tam one się nazywają?  
Tak, bo dzisiaj niestety tak to nie działa w żaden sposób. W ogóle tam mamy te.  
Xx paw mocno, a to tak Przepraszam, bo to nie to pokazuje ten x pan w ogóle źle działać, to już rozmawialiśmy z prawem, natomiast mi się nie udało ustalić gdzie i kto i jak z tego korzysta.  
Ee więc możemy podejmować ryzyko, żeby ten ich spaw przerabiać.

**Piotr Buczkowski** 10:33  
O nie pisałem do kogo to było zrobione.

**Damian Kaminski** 10:36  
No pisałeś dla dojcze banku tylko jak ja zebrałem informacje o tym jak my pracujemy z dojcze banku to załamałem ręce bo nikt nie wie jak wygląda ich środowisko. Kamil tam pracował serwis, tam pracował Tomek, tam pracował nikt nie ma wiedzy jakie tam są procesy, każdy nie nie mamy czegoś takiego jak.  
Dojcze bank nasze demo czy dojcze bank death amo dicom gdzie mamy odtworzonych środowisko tylko każdy kto pracował zebrał na jakieś swoje środowisko, jakieś procesy jeden ma tu drugi, ma tu trzeci ma tu.  
No i w zasadzie nie wiemy co oni tam używają gdzie?  
Poprosił Amerykę, żeby uzyskał informację, czy używają tej funkcji, ale na razie jeszcze nie dostałem odpowiedzi. Pytanie, czy twory czy Object.  
Mm w tym parametrze xml mógłby mieć zdefiniowaną definiowane.  
Pole.

**Piotr Buczkowski** 11:31  
Tak, tak.

**Damian Kaminski** 11:34  
Bo to była najprostsza taka takie rozwiązanie, które już by.  
Dawało wtórnie odczytywać z iksem mela, czyli właśnie z tej faktury z sefa.

**Piotr Buczkowski** 11:43  
Znaczy tutaj trzeba poprawić to co to pisałem tak, że ten mix pack źle zwraca.  
Powinno zwracać to co x pad a nie czy children no tego co zwrócić co jest z expat.

**Damian Kaminski** 11:56  
No o k natomiast tutaj to to mówisz już o o samej funkcji ich spraw.

**Piotr Buczkowski** 12:02  
No tak, to tam jest cały jeden różnica, to czas czuwali się oprócz tego czytania, ale odczytywanie pliku to nie będzie nie spowoduje żadnych problemów.  
Czy?  
Zgodności owych z dotychczasowym, a ta zmiana zachowania inspekt tą, którą tam opisałem spowoduje, że trzeba będzie w tym wdrożeniu zmienić x pa.

**Damian Kaminski** 12:19  
No spowoduje no iteraz.

**Piotr Buczkowski** 12:25  
Ale to będzie sensowniejsze, bo teraz jest bezsensownie zrobione.

**Damian Kaminski** 12:25  
No i.

**Piotr Buczkowski** 12:33  
Albo jakiś sposób, także stare ich spad, tak?

**Damian Kaminski** 12:36  
No właśnie, bo to jest też alternatywa, że wygłaszamy tą funkcję robimy nową.

**Piotr Buczkowski** 12:41  
No nie, nie jakoś inaczej oznaczyć, tak.

**Damian Kaminski** 12:44  
Ale to mówisz o tym trzecim przypadku, gdzie mamy to tak?

**Piotr Buczkowski** 12:45  
Ale to nie.

**Damian Kaminski** 12:52  
Czyli o o takim przypadku mówi się na przykład tak i że to inaczej powinno być interpretowane.

**Piotr Buczkowski** 12:55  
No to.  
No tak, bo no tak jak napisałem tak wtedy z drobna różnica, że z 3 innych trzeba zrobić 2.

**Damian Kaminski** 13:00  
To nie wiem może.  
No no tu jest jakieś ryzyko, bo nie mamy wiedzy gdzie i kto tego korzysta to to tu można tylko nawiązać do tego, że powinniśmy może zbierać jakieś dane analityczne, ale to już szybsze wywija któryś raz, może w końcu trzeba do tego podejść.  
W taki sposób.

**Piotr Buczkowski** 13:28  
Znaczy, to nie było tam jakieś odczytywanie tych ich wyciągów.

**Damian Kaminski** 13:35  
Nie, nie, teraz mówię o danych analitycznych, żebyśmy my wiedzieli jakich funkcji, jaki klient używa.

**Piotr Buczkowski** 13:42  
No ale tutaj trzeba banku, odczytywanie wyciągów jakiś tam.

**Damian Kaminski** 13:45  
Nie wiem może.  
Na razie zadałem pytanie, zaraz się przypomnę, ale nie dostałem odpowiedzi, czy tego używają i do czego.  
Poprosiłem po prostu w prosto.  
O to, żeby wyszukali w bazie danych.  
Tą funkcję darwin gotowe zapytanie rynkowi, żeby wysłali nam te funkcje, jak z tego korzystają.

**Janusz Bossak** 14:14  
Tak mi się wydaje, że apropos teraz tego co powiedziałeś czy gromadzenia informacji o klientach według mnie w ramach usługi serwisowej.  
Czyli u Daniela?  
Powinni mieć obowiązek.  
Pobrania.  
Wszystkich definicji procesów okresowo co jakiś czas tak nawet po prostu nawet te zwykłe xml i już mielibyśmy jakąś bazę wiedzy co się u klienta dzieje. Tak to przecież tego nie chodzi o to, że o tam on codziennie ten klient coś zmienia i tak dalej pani to zrobią raz na kwartał.  
Bo biorą te x mele i będziemy gromadzić taką informację, to będziemy tą wiedzę, o którą mówisz mieli.  
Tak, czyli jakich funkcji używają klienci? Głównie o to chodzi. No jakich funkcji używają?  
Jak często używają możemy zobaczyć jakość kodu, ocenić jak procesy są budowane i tak dalej i tak dalej.  
Więc.  
A to nie jest żadna jakaś tajemnica, jeżeli mówimy, że my serwisujemy, to my chcemy wiedzieć co oni mają tak jakby element serwisu element u działania usługi jakiejś to to, że my powinniśmy mieć ten cover base ich u siebie, tak.  
Nie damy, bo na dane nas nie interesują, ale definicje procesów jak najbardziej tak.

**Damian Kaminski** 15:36  
No tym bardziej, jeśli byśmy ich nie serwisowanie, no to k wasza sprawa, ale.

**Janusz Bossak** 15:42  
Tak, tak.

**Damian Kaminski** 15:42  
Eks serwisujemy no to powinniśmy mieć po prostu po naszej stronie, tak jak dla każdego innego postulowałem dla każdej innej chmury mamy 2 środowiska.  
I te starej produkcyjnej tak samo tu to, że nie mamy wejścia do nich, to nie znaczy, że nie powinniśmy wiedzieć co tam im produkujemy.

**Janusz Bossak** 16:00  
Dokładnie.  
To jest też pewnego rodzaju backup. Tak można powiedzieć przynajmniej definicji procesów, no i po prostu prowadzimy usługowo.  
My taki właśnie backup definicji procesów u nas.

**Damian Kaminski** 16:14  
To już nawet nie nie można to tak określić, że mamy back up, a po drugie, że no właśnie rozwijamy pewne rzeczy wygłaszamy pewne rzeczy zmieniamy, więc jeśli mamy tą wiedzę, to zmniejszamy ryzyko, że coś będzie nie kompatybilne wstecznie, bo czasami no technologia wymusza podjęcie takiej decyzji. Możemy ostrzec albo od razu zrobić akcję serwisową, żeby w biznes tego nie odczuł. No jak nie mamy tego, no to to nie mamy. No nie zrobimy żadnej akcji.

**Janusz Bossak** 16:41  
No ale.  
Z tego, co Daniel mówił, to mamy zaopiekowany ich ponad setkę klientów.  
Ponad setka umów.  
Serwisowy no to już jest dużo tak.

**Damian Kaminski** 16:57  
No dobra, to tak podsumowując, żeby może nie ciągnąć tego tematu, że żeby skończyć ten temat tego xml, a to tak eryk napisał, że ich pinguje, że nie dostał odpowiedzi na ten moment zrobię tylko zgłoszenie na forum hobby, tutaj podać nazwę, no właśnie pola z plikiem tak czy.  
Bo często mamy pole z plikiem albo albo plik po prostu pole z plikiem w kwadratowych, tak.  
W ten sposób dobra, no to takie zgłoszenie.

**Piotr Buczkowski** 17:26  
No bo jak streaming to jeszcze, bo to jeszcze x mela tak w tym stringu to jest to odczytałeś skąś.

**Damian Kaminski** 17:29  
Tak, tak, tak, ale no niestety.  
To problem polega na tym chyba, że co innego, ale właśnie to jest związane z tym, że no dzisiaj nie jesteśmy w stanie odczytać znikąd poza pola tekstowego. X mela forum xml, a tylko treść.

**Piotr Buczkowski** 17:42  
No to.  
Ja nie ma gta tasmy to kontent jakiegoś.

**Damian Kaminski** 17:49  
Wiesz co no nie działa, ja to testowałem, to wszystko wycina węzły xml owe wszystko co mi przychodziło do głowy, wycina węzły xml owe.

**Piotr Buczkowski** 17:56  
Są.

**Damian Kaminski** 17:58  
No.

**Piotr Buczkowski** 17:58  
Dobrze sprawdzę być może warto.

**Damian Kaminski** 18:05  
To jest się ucięło.

**Piotr Buczkowski** 18:07  
To nie nie.

**Damian Kaminski** 18:10  
Wszystko co mi przychodziło do głowy.

**Piotr Buczkowski** 18:11  
A nie bo to content tropik tata content pobiera furtek wstecz kontent.

**Damian Kaminski** 18:17  
No właśnie.  
Chyba.

**Piotr Buczkowski** 18:20  
Dobrze myślę wymyśleć coś.

**Damian Kaminski** 18:22  
O k. No to jeśli masz na to alternatywę, no to wtedy może to nie jest niezbędne czy czyli tak to robimy?

**Piotr Buczkowski** 18:30  
Próżno i tak i tak.

**Damian Kaminski** 18:37  
No dobra, to zgłoszę, żeby to szło, jeśli wymyślić na to lepszy rozwiązanie, to dasz tam w komentarzu już dzisiejsze, że tak powiem, że można tak dzisiaj zrobić. No bo ja ja nie wymyśliłem.  
Jeśli było w polu długiego tekstu, to nie ma problemu. Da się to przekazać, natomiast jeśli było kilku, to nie byłem w stanie odczytać wartości z węzłami ximer.  
Dobra, ja więcej tematów swoich nie mam.  
No dobrze, mogło być pokryte pt.  
Komar już musi się.  
Dlatego stosunkowo jest to już sobie mówiliśmy.  
Co w sumie też.  
To też musimy wrócić na radę.  
No dobra, no to są bardziej takie tematy, które czekają. Aha, to osiągnięto limit spraw.  
Tylko ciekawostka, dostałem z innej instancji. Ostatnio ten sam mail.  
Ale nie wiem, nie wiem czy to cokolwiek wyjaśni. Mogę tylko podać przykład.  
Pierwszy raz mi się to zdarzyło.

**Piotr Buczkowski** 20:33  
No co w tym było?  
Nikt nie potrafi tego rozwiązać.

**Damian Kaminski** 20:40  
O k po prostu może w jakiś sposób da się to, ale to jest związane z bardzo udanych po prostu tak.

**Piotr Buczkowski** 20:46  
No jeżeli pewnym momencie osiągnie.  
Być może po prostu wystarczy inaczej obsłużyć logo, błąd logo, błąd od czytania licencji na przykład zignorować na razie nie wysyłać tego, ponieważ.  
Nie, nie udał nie to, że licencji temat tylko nie udało się odczytać.

**Janusz Bossak** 21:05  
Tak to chyba powinno być tak, że.

**Piotr Buczkowski** 21:05  
One są tym razem może się doczekać już nikt nie będzie takiego czegoś widział, nikt nie będzie.  
Yy drążyła jak raz przy jednym przebiegu się nie przeczytają, to cóż.

**Janusz Bossak** 21:16  
Dokładnie to powinno być tak, że jeżeli to nie wiem w ciągu jakiegoś czasu nie wiem 3 razy się powtórzy, że nie ma licencji czy coś takiego, to dopiero wtedy wysyłać, a nie tam, że przy pierwszym strzale tak jak tu Piotr mówi od razu wysyłać i robi się zamieszanie zupełnie niepotrzebne.

**Piotr Buczkowski** 21:19  
Czy?

**Damian Kaminski** 21:32  
No bo widzicie, Jestem tam gdzieś w tym LP jako administrator i też i wszyscy administratorzy po prostu to dostali, więc no właśnie może takie rozwiązanie jak mówi.

**Piotr Buczkowski** 21:41  
No wiesz, ktoś musi ciąż przemyśleć jak to dobrze zrobić nie może.

**Damian Kaminski** 21:47  
No o KOK, czyli no wiemy co jest przyczyną? Pytanie tylko czy coś tu wymaga jeszcze omawiania dalej na razie architektów. Co z tym robimy? Po prostu.

**Janusz Bossak** 21:55  
Właśnie nie wiemy, co jest przyczyną, że tak się dzieje. Tak znaczy wiemy tylko tyle, że w jakiś okolicznościach nie wiadomo, jakich właśnie tego nie wiemy. Nie odczytują się te informacje o licencjach, tyle i stąd i od razu idzie komunikat, że osiągnięto.  
Limit sprawny, bo system uznaje, że nie ma licencji, skoro on nie odczytał.

**Piotr Buczkowski** 22:15  
No.  
Rozróżnić przypadek, że licencja została odczytana i osiągnięto limit spraw od sytuacji, jeżeli licencja z jakiś powodów nie została odczytana i nie wiadomo, czy osiągnięta nic spraw.

**Janusz Bossak** 22:30  
Właśnie dokładnie dokładnie o to chodzi.  
Czyli prawdopodobnie obsługa w jakimś trajkę czu gdzie coś tam nie udało się odczytać, a my to od razu uznajemy, że to jest brak licencji, a może to nie jest brak licencji, tylko brak dostępu do bazy chwilowo tak z jakiegoś powodu i nie można tego odczytać.

**Damian Kaminski** 22:53  
No o k.

**Janusz Bossak** 22:53  
No to trzeba przywrócić to cię obsłużyć trajkę.  
I sobie gdzieś tam notować, nie wiem nawet w keszu, że jak on to zrobi dla.

**Piotr Buczkowski** 23:04  
Są już tam już tak, nie coś jest, tylko jakoś pewnie to jest źle źle obsłużone tak widziałam chciałam, bo nie pamiętam kto to robił.

**Janusz Bossak** 23:14  
Ale kluczowe jest to, co Piotr powiedział dopóty, dopóki się nie uda fizycznie odczytać licencji.

**Piotr Buczkowski** 23:14  
Nie pamiętam.

**Janusz Bossak** 23:21  
To nie uznajemy tego za brak licencji.

**Piotr Buczkowski** 23:24  
Albo da się dostać, że sprawdzić, że rzeczywiście licencja nie jest wpisanym na przykład tak nie to, że.

**Janusz Bossak** 23:31  
No tak, no ale to nadal jest.

**Piotr Buczkowski** 23:32  
Pani a nie to, że wystąpił błąd przed trzeciej licencji o.

**Janusz Bossak** 23:35  
Tak tak, czyli wszelkiego rodzaju błędy dostępu do bazy danych, próby odczytania licencji nie mogą być traktowane jako brak licencji i tyle.  
Dopiero fizyczne odczytanie licencji czy odczytanie braku licencji, czyli nie ma klucza, ale to nie było żadnych błędów. Tak dostaliśmy się do miejsca, gdzie klucz powinien być i tego klucza tam nie ma. No to jest brak licencji.

**Damian Kaminski** 24:05  
No dobrze.  
To co z tym robimy dalej?

**Janusz Bossak** 24:11  
No to trzeba dać zaopiekować to w ramach tej stabilizacji wersji to jest jeden z takich właśnie elementów.

**Piotr Buczkowski** 24:17  
Przepisz to piwo, to tak się skończy.

**Damian Kaminski** 24:20  
Dobra, ale to już może na przyszły rok.

**Piotr Buczkowski** 24:23  
No tak, tak, tak to teraz tego nie zrobię.  
Ewentualnie może w przerwie pomiędzy świętami i nowym rokiem.

**Janusz Bossak** 24:28  
Ale to.  
Ale to to wracam. Kamil Damian, Łukasz, do tej rozmowy naszej wcześniejszej, tak, czy to właśnie ten obszar stabilizacji wersji to jest bardzo ładny punkt dokładnie do stabilizacji, bo to denerwuje klientów.  
Denerwuje naszych konsultantów, wszystkim zabiera czas i tak dalej.  
Idealnie.

**Piotr Buczkowski** 24:50  
No już któryś raz odpowiadam na pytanie, że poczekajcie chwilę zaraz będzie dobrze.

**Janusz Bossak** 24:52  
Dokładnie.  
To jest perfekcyjny przykład do tego hasła stabilizacja systemu.

**Damian Kaminski** 25:00  
Nie no tak ja się zgadzam po prostu wiecie, chodzi mi o to, że przypisujemy sobie wtedy i kończymy temat, bo wisi to po prostu na razie długo, więc musimy podjąć jakąś decyzję, że tak realizujemy to albo przynajmniej podejmujemy próbę, skoro wiemy. No właśnie, że to jest raczej w tym wypadkach, których to zgłaszają klienci braku dostępu do bazy, a nie braku licencji.

**Piotr Buczkowski** 25:26  
Może?  
Problemem z odczytaniem licencji tak, a nie braku licencji.

**Damian Kaminski** 25:31  
Mhm.

**Janusz Bossak** 25:33  
Tak dokładnie dokładnie problem brak. Znaczy no czytania niż wszyscy są świadomi, że jest znaczy tam jeszcze ja nie wiem czy to skutkuje, czy nie skutkuje tym, bo tu jest osiągnięto limit spraw i czy to tylko jest kwestia komunikatu, czy rzeczywiście przez pewien moment z jakiegoś powodu nie można zakładać kolejnej sprawy, bo jest jak gdyby nie ma licencji, tak.

**Damian Kaminski** 25:37  
Dobra, to zdejmuje program.

**Piotr Buczkowski** 25:57  
No tak tylko jest usługi.

**Damian Kaminski** 25:58  
Znaczy, no nie, nie można zakładać, ale to nie znaczy, że ta sprawa nie powstanie, bo bo inaczej może to dotyczy przypadku, kiedy sprawy są zakładane na podstawie maila lub też skanu. I zakładam też, że mamy to tak zaopiekowane, że jak nie udało się założyć sprawy na podstawie tego skanu, to skan nie znika, tylko czeka do kolejnych iteracji po prostu. No właśnie więc tu się nic złego nie dzieje z danymi.

**Piotr Buczkowski** 26:17  
No tak, tak tak.

**Janusz Bossak** 26:23  
Ale to całą tą ścieżkę, czyli nie tylko wysyłanie komunikatu do admina, ale w ogóle funkcjonowanie systemu.  
Należy tak przerobić, żeby chwilowe braki dostępu do licencji.  
Nie powodowały jakiś skutków ubocznych takich tego typu żywność i nie można założyć sprawy z maila czy cokolwiek innego tak, że tak według mnie to przemyśleć, szczególności takich instalacjach, on premise gdzie, no raczej ta licencja tam jest tak no.

**Damian Kaminski** 26:47  
Tego.  
No tak, bo ciekawe jest też to, że tak.  
Nie dostał się właśnie gdzieś do jakiejś zasobów bazodanowych, ale udało mu się to robi usługa, bo jakby klient wszedł no to raczej by nie wszedł do aplikacji, gdyby nie było dostępu do bazy, tak natomiast tu powstaje taki przypadek i teraz, a ten mail nie jest generowany. Najpierw w bazie danych, więc.  
Nie odczytało licencję, a z kolei maila było w stanie zapisać i potem wysłać.

**Janusz Bossak** 27:23  
No właśnie niby coś działa.

**Damian Kaminski** 27:24  
Czyli to było jakaś sekundowa niedostępność czy mili sekundowa, a już kolejne wywołanie wygeneruj maila, żeby coś takiego wysłać to to już to działo, czy to jest po prostu obsługiwany w 100 procentach po stronie obsługi usługi?  
Taki mail.

**Lukasz Bott** 27:40  
Wiesz co? Bo są maile. Tam są 2 kategorie maili, niektóre są natychmiastowe i być może ten jest tak interpretowany.

**Damian Kaminski** 27:49  
Mhm.

**Janusz Bossak** 27:51  
No słuchajcie, temat jest szerszy, znaczy.

**Damian Kaminski** 27:52  
No dobra, to jest tylko.

**Janusz Bossak** 27:54  
Też chodzi mi o to, żeby nie poprawić tylko jednego objawu znaczy, że administrator dostaje maila tylko żeby poprawić wszelkie objawy z tym związane, że skutki tego.

**Damian Kaminski** 27:54  
Pewne spojrzenie.

**Janusz Bossak** 28:06  
Tego chwilowego braku dostępu do informacji o licencji, bo to dokładnie o to chodzi, to są skutki chwilowego braku dostępu do licencji, żeby one nie były takie rygorystyczne i drastyczne, żeby system działał.  
I dopiero jak sprawdzi parokrotnie i upewni się system, że rzeczywiście tej licencji tam nie ma. No to wtedy dopiero wdraża system te różne działania tak, czyli ogranicza liczbę spraw do zakładania i tak dalej i tak dalej, ale przy chwilowych takich odcinkach i niemożliwości odczytania, żeby to tak się nie działo.

**Damian Kaminski** 28:45  
Dobra, przypisane do Piotra na ten, tak jak powiedziałeś, to jest sprint. Pierwszy zaczyna się dwudziestego tam 9 grudnia.  
Czy po świętach w poniedziałek?  
Jeśli będziesz miał przestrzeń, to to podejmiesz, dobra?  
Co my tu mamy jeszcze jakieś miarę świeżych tematów, to w sumie też już odpinam.  
Ten temat jest tematem też takim bardziej koncepcyjnym, wrzuconym przeze mnie. Ja wrzucałem tam wam też, ile tych zapytań idzie. No dobrze, było pewnie tutaj te skriny, powrzucać i.  
Myślę, że to nie no niekoniecznie na dzisiaj.  
A to już chyba mamy omówione.  
No to mówiliśmy już na razie tylko trzeba.  
Przypisać numer.  
Kto jeszcze tam mówiliście, że ktoś nie ania tylko nie miała tak.

**Anna Skupinska** 30:07  
Mhm.

**Damian Kaminski** 30:10  
No to jest chyba dość prosty temat, bo wszystkie mechanizmy 100 z tego, co ostatnio Piotr opisywał.

**Piotr Buczkowski** 30:15  
No jest funkcja, która sprawdza, czy dany Użytkownik może utworzyć sprawy z tej.

**Damian Kaminski** 30:17  
Tak, tak.

**Piotr Buczkowski** 30:21  
Z tego procesu i po prostu trzeba.  
Przy takim wywołaniu też dodać sprawdzania tego.

**Anna Skupinska** 30:27  
Mhm.

**Piotr Buczkowski** 30:27  
Zapomnieliśmy o tym.

**Damian Kaminski** 30:30  
Mhm.  
No dobra.  
Co ty mamy dalej?

**Anna Skupinska** 30:41  
To jeszcze jest ewakuowane widzę.

**Damian Kaminski** 30:43  
Jeszcze raz.

**Anna Skupinska** 30:45  
To na damianie jest ewaluacja.

**Damian Kaminski** 30:47  
No widzę właśnie już coś kojarzę, ten temat chyba nie dokończyłem jego opisów czy oświetlenie sekcji na telefonie jako strony, bo tu mieliśmy ten pomysł z przewijaniem.  
Z przewijaniem strzałkami dalej dalej z walidacją od razu krótką.  
Dobra, zostawmy to na mnie.  
Przedstawię jakoś propozycję, właśnie może po świętach i do tego wrócimy.  
Yy to widzę, że też na mnie.  
No dobra, to nie będę tym zajmował.  
Dalej mam aktualizację, no to temat otwarty raczej na Michała, że tutaj pogadać.  
To już jest to.  
Chyba że teraz, a nie dobra to dotyczy repozytorium. To wcześniej było przypięte.  
Przed tym jeszcze coś robimy, Łukasz.  
To też omawialiśmy na ostatniej Radzie.

**Lukasz Bott** 32:31  
Nie.

**Damian Kaminski** 32:34  
Zostajemy bo.

**Lukasz Bott** 32:34  
Mamy stałe zapisane.  
Jakieś ustalenia?

**Damian Kaminski** 32:39  
Ustaliliśmy nie, no ustaliliśmy, że to tak po prostu nie działa w sensie m.  
Można zastosować to obejście, które tu Piotr podał.

**Lukasz Bott** 32:48  
Mhm.

**Damian Kaminski** 32:48  
Natomiast no.  
To tak zawsze było, no i.

**Lukasz Bott** 32:53  
Na razie zostawiamy to.

**Damian Kaminski** 32:55  
Myśli kluczem jest coś innego niż to, co wyświetlamy. Eksportujemy jednak dane, które wyświetlamy, więc no nie, nie taki był cel tego tego mechanizmu, on.  
Żeby obsługiwać to poza poza systemem. Tak tam było pytanie, czemu nie to tak robią?  
Czemu oni?

**Lukasz Bott** 33:13  
Weźmy.

**Janusz Bossak** 33:13  
Czy?

**Damian Kaminski** 33:17  
Pamiętasz?

**Lukasz Bott** 33:17  
Może od tak?

**Janusz Bossak** 33:17  
To mówicie o tej sytuacji, gdzie tam zniknęło niby ileś danych co Daniel dyrektor.

**Damian Kaminski** 33:22  
Nie, nie, nie, nie, nie tyle, co, zniknęło bardziej to dotyczy przypadku takiego, że mamy mamy tabelę i mamy import i export, i teraz jeśli w tej tabeli jest Odnośnik do źródła zewnętrznego, albo jeśli w tej tabeli jest Odnośnik do w sumie po prostu pole typu Odnośnik, czyli ono wyświetla co innego, niż faktycznie przechowuje.

**Lukasz Bott** 33:23  
Nie, nie, nie, to jest spokojnie.  
No przy próbuję unikalny klucz tak to jak się identyfikator.

**Damian Kaminski** 33:44  
To.  
To eksport i import tych danych po prostu skutkuje nie kompatybilnością w sensie.  
No nie da się wczytać wtedy tych danych w takiej postaci, w jakiej one były wyświetlone, bo to co było pod spodem te klucze, po których zdefiniowana ta dana pozycja jest inna niż ich wartość. Tak wartość tych pozycji.

**Janusz Bossak** 33:54  
No tam.

**Damian Kaminski** 34:07  
No i tyle i.  
Alternatywą jest zawsze przechowywanie klucza klucza właśnie w jakimś polu tech, no i wtedy jakieś obejścia. Natomiast tu Piotr słusznie skomentował i ja też o to Łukasza. Dopytywałem natomiast no.  
Klient zawsze ma swoją jakąś rację, czemu oni chcą eksportować dane z tabeli i importować.  
Czyli mówiąc wprost, co jest problemem w modlitwie, żeby nie zrobić z tego a modlicie tylko robić to w excelu?

**Janusz Bossak** 34:31  
Bo.  
Całości tłumaczy, bo to jest problem ten, który Daniel namieszał któregoś tam któryś od niego z ludzi u klientów. Po pierwsze nie rozumieją mechanizmu homomilitia. To jest pierwszy mój wniosek.  
Bo się wydawało.  
Wszystkim znaczy wszystkim mówię o danielu, że jak on wyeksportuj je.  
Uzupełni.  
Kolumnach innych niż te, które zostały wyeksportowane i to za importuje z powrotem to mu się uzupełnią dokładnie w tych samych wierszach, o tych samych ideach te dane, no nie, to jest mechanizm, który kasuje wszystkie dotychczasowe wiersze tabeli i twarzy i tworzy nowe. No i tutaj Daniel, tam 2 czy 3 tygodnie temu, że to cała dyskusja była na ten temat, stworzył hot fixa, że system dane i tak dalej, no nie po prostu nie nie rozumieją.

**Damian Kaminski** 35:17  
Albo dopisuje, no tak.  
Tak.  
Dowiedziałem, ale to to to rozumiem.

**Janusz Bossak** 35:34  
Natomiast jest taka widać potrzeba.

**Damian Kaminski** 35:35  
Tylko jest przyczyna jakaś nie czemu ktoś wtedy robić na zewnątrz?

**Janusz Bossak** 35:37  
Jest.  
No bo się bo bo nasza tabelka no nie jest excelem, w których robisz sobie kopii playlist tak i rozciągasz na 100 pozycji, czy na 50.  
Tylko tyle nie, czyli oni chcą wyeksportować. Ja tam podałem propozycję, że powinniśmy eksportować razem z tym kasa itd.  
Które jest wiersza?  
Niech sobie uzupełniają zewnętrznie jakieś dane, które potrzebują i niech spowrotem, ale już nie jakby importują tylko aktualizują tak czyli wtedy ten mechanizm powinien brać pod uwagę to klasa i d powinien brać pod uwagę co się zmieniło i nie ruszać tych rzeczy, które się nie zmieniły i aktualizować. Ten tam jeszcze była jedna.

**Damian Kaminski** 36:23  
No tak.  
Wtedy ten nie jest import, tylko tylko właśnie aktualizacja tabeli. Inaczej trzeba było to to jakoś powinien rozpoznawać.

**Janusz Bossak** 36:32  
Tak zupełnie tak zupełnie nowy mechanizm, no i kolejne.

**Damian Kaminski** 36:36  
Ale według mnie to nie jest przyczyna. W sensie dalej idziemy w kontekstu życia klienta, a nie rozwiązanie problemu.

**Janusz Bossak** 36:40  
Ja wiem, ja wiem, no wiem.  
Wiem, ale idąc tym tropem, jeszcze drugiej wątek niezrozumienia i to mówię to w specjalnie wyraźnie głośnie głośno, bo jeżeli no sorry, ale dział serwisu jest na podstawowych zasad funkcjonowania morita to mnie po prostu przeraża momentami.  
Pomijając już inne rzeczy drugą.  
I drugim zastrzeżeniem było to, że przy tym imporcie tych danych.  
Nie na podpisują się Polak tylko do odczytu ja mówię, no nie no.  
Pole do odczytu, do czego ono służy do odczytu?  
No ale skoro sobie wyeksportowały i teraz chcę importować Daniel po to jest pole do odczytu, żeby ten człowiek, który teraz właśnie patrzy na ten.  
Na tą tabletkę nie mógł tam czegoś wpisać to dlaczego import, który on robi miałby tam wpisać? Przecież to jest złamanie zasad bezpieczeństwa.

**Damian Kaminski** 37:40  
No tak.

**Janusz Bossak** 37:42  
No ale to.  
Po prostu ręce mi opadają momentami.  
No ale masz rację Damian tam ten temat trzeba by zgłębić co jest nie tak, że ktoś chce to robić tak masowo tak, bo może powinna być funkcja na przykład.  
Uzupełnij wszystkie kolumny w danym małej tabelce o coś nie mam jedną wartość 58.

**Damian Kaminski** 38:06  
Jednak w nagłówku określasz, co ma być w każdym wierszu tak no to jest jakaś alternatywa.

**Janusz Bossak** 38:09  
I chcę poprowadzić wszystkich wszystkich wierszy, w tym w tej kolumnie wartość tam jakąś datę na przykład stawić nie wszędzie.

**Damian Kaminski** 38:17  
Mhm.  
Dobra, to jeśli jesteśmy przy tabelach, to jeszcze wam pokażę praktyczne użycia morita.  
Ee no i pytanie co z tym robimy? Bo.  
Bo to zostało po prostu wymyślone przez wdrożenia owca.  
I wszystkim się to podoba, bo już tym się pochwalił.  
Mamy tabelkę.  
Mamy przyciski osadzone w tabelce.  
I teraz te przyciski osadzone w tabelce są oczywiście przyciskami procesu, ale osadzone w tabelce natomiast zrobił dodatkową funkcjonalność javascript ową, która powoduje, że klika tutaj.  
To tu się przenosi. Pokażę wam, żebyście wiedzieli.  
To faktycznie zadanie wykonane.  
Przycisk wykonuje się tylko na tym wierszu.

**Anna Skupinska** 39:15  
A czyli podmienia Lejdis yy sprawy.

**Damian Kaminski** 39:19  
Niebo no nie wiem co on tam mogę wam pokazać jak wygląda. Natomiast no wiecie to jest.

**Janusz Bossak** 39:24  
Czy?

**Piotr Buczkowski** 39:26  
Wpisuje ip i wybranej sprawy w tym polu, a później w regule fortes robi czyta horrory nie wiem.

**Damian Kaminski** 39:31  
Tak.

**Anna Skupinska** 39:32  
Mhm.

**Damian Kaminski** 39:33  
Tak.  
Tak no i pytanie, czy nie możemy tego zaopiekować globalnie lepiej, bo ja już mógł. Ja już mu powiedziałem, jaki jest, no.

**Janusz Bossak** 39:37  
Musimy musimy.

**Piotr Buczkowski** 39:38  
Ale to, ale to to przecież od dawna już jest.

**Janusz Bossak** 39:43  
Od dawna to mamy do zrobienia i trzeba to zrobić. To jest też jeden z elementów przyspiesza.

**Damian Kaminski** 39:47  
No bo zobaczcie jaka jest konsekwencja powiedziałam.

**Janusz Bossak** 39:49  
Wdrożeń.

**Damian Kaminski** 39:50  
Pokaż historię, no i historii niestety jest informacja niespójna z tym tu się chyba faktycznie to co on zrobił dobrze działa, natomiast sama historia pokazuje, że nastąpiła modyfikacja wszystkich wierszy. Tak przed chwilą dziesiąta 47 wierszy, jeden wiersz 2 wiersz, mimo że tu chyba nie nastąpiły jakieś żadne zmiany i faktycznie wykonało się to tylko na na tym jednym natomiast no historia za tym nie nadąża.  
Więc trzeba by było to pewnie do opiekować przez nas lepiej. No to wprowadził jakiegoś krótkiego java scripta, który tam odczytuje kontekst, konto wywołuje i.  
I przypisuje to kej di tak do feel dwali.

**Janusz Bossak** 40:36  
To to trzeba to zaopiekować.

**Lukasz Bott** 40:36  
To trzeba to.  
Tak, bo co do.

**Damian Kaminski** 40:39  
No bo wiecie, to on to zrobił. Pochwalił się tym i już tam słyszałem, że dział wdrożeń już jest.

**Janusz Bossak** 40:41  
Przy pierwszy.  
Nie zabronić zabronić takich sztuczek.

**Piotr Buczkowski** 40:45  
I i przecież i przestanie i przestanie to działać. Jeżeli coś zmieniły w konstrukcji.

**Janusz Bossak** 40:48  
Absolutnie zabronić takich sztuczek.

**Damian Kaminski** 40:51  
Dlatego dlatego to poruszam, słuchajcie, no to.

**Lukasz Bott** 40:51  
No dokładnie ten.

**Janusz Bossak** 40:54  
Zabronić takich sztuczek i tyle.

**Damian Kaminski** 40:56  
Jak coś nie jest, nie jest zablokowane, no to zawsze kombinują tak natomiast, no po prostu musimy to zaopiekować w takim razie.

**Janusz Bossak** 41:06  
Często się przedłużają wdrożenia.

**Lukasz Bott** 41:09  
A potem, a potem utrzymanie serwisowe były święta nagle okazuje, że kurne tam się okazuje, że jest jakiś javascript jakiś porąbany CS.

**Janusz Bossak** 41:11  
I serwis dokładnie.

**Lukasz Bott** 41:17  
I nawet nie wiem, że to tak działa, nie?

**Janusz Bossak** 41:19  
Dokładny sami sobie robią.

**Piotr Buczkowski** 41:21  
A czemu? Bo mówię aktualizacja, modlitwa możemy spowodować, ja to przestanie działać, bo to jest minimum.

**Lukasz Bott** 41:26  
No tutaj to jest, no ale do kogo będą pretensje do nas byśmy zaktualizowali amanita.

**Janusz Bossak** 41:30  
Tak.

**Damian Kaminski** 41:31  
No ale to słuchajcie, no temu temu to poruszamy, no więc chcemy to zaopiekować, tak?

**Piotr Buczkowski** 41:31  
Będzie hotfix.

**Janusz Bossak** 41:37  
Po pierwsze niech on tego nie rozpowszechnia.

**Damian Kaminski** 41:41  
Mhm.

**Janusz Bossak** 41:41  
Niech Tomek tak marzec niech nie rozpowszechnia, niech nie zachęca innych do robienia tego typu.  
Rzeźby.

**Damian Kaminski** 41:49  
Nie, to nie tyle, że może zachęca tak bardziej gdzieś tam się tym komuś pochwalił i tyle.

**Janusz Bossak** 41:55  
Bo to znaczy, no dobra, no.  
Natomiast tak my to musimy zaopiekować. To jest jeden, to jest z kolei temat w ramach skracania wdrożeń.  
Temat, który wraca dziesiątki razy.  
Był wielokrotnie omawiany w różnych konfiguracjach. Trzeba to zrobić, żeby były reguły.  
No takie w tabeli.  
Tak, który można uruchomić na tej pojedynczej sprawie w tabeli, która coś tam zrobi.  
Bardziej zaawansowany.  
Przypadek to są reguły takie świetlane w raporcie tym osadzonym, który tutaj by był, bo też można wyobrazić, że masz raport, który pokazuje jakieś tam cokolwiek listę czegoś.  
I ty wybiórczo na tym raporcie chcesz coś kliknąć tu zatwierdzam tutaj podrzucam tu Akceptuję tu coś tam tak mam, tak jak on tutaj właśnie wyświetlił, nie.

**Damian Kaminski** 42:57  
To to akurat mamy, tak?

**Janusz Bossak** 42:59  
No nie no, na raporcie osadzonym możesz wyświetlić przyciski.

**Damian Kaminski** 43:04  
Nie, ale możesz wyświetlić czeboksary, a podczas boksami przyciężki wywołać wydarzenie no danym czy w boksie?

**Janusz Bossak** 43:09  
Tak, ale ludzie tak chcą.

**Damian Kaminski** 43:11  
O k. Rozumiem dobra, czyli że mają być ma być tak jak tu 20 przycisków takich samych tak na 20 pierwszych.

**Janusz Bossak** 43:17  
Bo wybiorczo sobie tutaj robisz tu aktualizujesz tu odrzucam tu coś tam poczytasz to i wiecie, a nie tam będę za każdym razem teraz musiał trafiać w odpowiednie czy jak boxy nawet na najczęściej w jeden, bo ten chce akurat tylko zrobić tak taka niewygoda, nie.

**Damian Kaminski** 43:20  
O KOK.  
No.  
Z jednej strony tak z drugiej zaraz będzie, że i tak zróbcie nam i to i to, bo czasami chcemy zaznaczyć wszystko i kliknąć jeden, czyli 20 razy, ale no to mamy to możemy dołożyć jak najbardziej dobra, ale to po kolei, czyli zacznijmy czy zaczynamy od tabeli? Tak.

**Piotr Buczkowski** 43:48  
Znaczy zrobienie takiego czegoś, że.  
Jeżeli teraz dodam pole typu przyciski to tabeli.  
I ten ta reguła zostanie wykonana w kontekście tego wiersza. To jest drobiazg, coraz to zrobię.  
Jeżeli jeżeli jest takie decyzje.

**Damian Kaminski** 44:05  
No dobrze, tylko tylko.

**Lukasz Bott** 44:05  
Ale ale czekaj, ale regułę, gdzie definiujesz pod tym przycisku na zewnątrz tabeli?

**Damian Kaminski** 44:09  
Procesie w procesie.

**Piotr Buczkowski** 44:11  
No na procesie tak.

**Damian Kaminski** 44:12  
Tak, tak tak, czyli czy to właśnie pytanie jest takie, czy wtedy ta reguła powinna być od razu zaznaczona, że to jest reguła tabeli? Ona się nie będzie pojawiać tutaj. Nie mam być to tak samo wszystko jak teraz, tak tylko jeśli wykryje swój kontekst, tak.

**Piotr Buczkowski** 44:21  
Nie, nie.  
Nie.  
Tylko będzie będzie będzie kontekst wiersza tabeli.

**Janusz Bossak** 44:31  
Jeszcze raz, bo nie zrozumiałem.

**Damian Kaminski** 44:31  
No dobra.  
Czyli tak jak tutaj jest zrobione przez Tomasza?

**Piotr Buczkowski** 44:35  
Teraz teraz do domyślnie reguła ręczna ma kontekst głównej sprawy, jeżeli umieścisz w polu przyciski, to regułę wierszu tabeli będzie miała kontekst tego wiersza tabeli czyli.  
Tekst, powiedzmy tak pole tekst się nazywa w nawiasie kwadratowym będzie się odwoływała, odwołało odwoływało do polartec w tym wierszu to będzie.

**Janusz Bossak** 45:00  
No i dobrze pytanie.

**Damian Kaminski** 45:02  
Nie trzeba będzie robić tylko tylko widzisz tutaj.  
Pod kątem takiego walidatora według mnie, który no ja cały czas za nim postuluje, że powinniśmy mieć walidatora ja i który będzie sprawdzał, czy te reguły są dobrze napisane i tak dalej. No to jeśli byłoby oznaczenie, że to jest jednak reguła tabeli.

**Lukasz Bott** 45:06  
No dobra.

**Damian Kaminski** 45:22  
Ja wiem, że to trochę więcej będzie kosztować, ale może to powinno być vi 2 to wtedy wiesz, nie ma literowania Nie możesz tam użyć forge row na tej tabeli, bo on już ma tylko kontekst tego wiersza.

**Piotr Buczkowski** 45:24  
Znaczy.

**Janusz Bossak** 45:36  
No ale to wtedy nie musisz takiej reguły używać w tym pierwszym to są znaczy, bo ja się zastanawiam trochę inaczej.  
Bo w ramach tego nowego layoutu edytora reguł i tak dalej i tak dalej jest pomysł, był pomysł i jest nadal, żeby były reguły ręczne tabeli.

**Damian Kaminski** 45:55  
No.  
Czyli to, co tu widzimy?

**Janusz Bossak** 45:57  
Bo.  
To co tu widzimy tylko, że chodzi też o to, w którym miejscu je się definiuje, no bo.  
To co teraz przynajmniej tak to rozumiem, Piotr, że robimy normalną regułę.

**Damian Kaminski** 46:10  
Tak.

**Janusz Bossak** 46:10  
I pisząc tą normalną regułę musimy mieć w głowie sami dla siebie, że robimy ją i ona będzie używana w kontekście wiersza tabeli i potem jeszcze ona musi zostać użyta w polu typu przeciski.  
Były tabeli, żeby to wszystko zadziałało, więc proces myślowy jest po prostu karkołomny.

**Lukasz Bott** 46:36  
Jest jeszcze jeden problem, bo jeżeli to tak jak teraz masz tą regułę ręczną uruchamiano w kontekście głównego formularza.  
Tak no to tutaj walidacja pól, bo jeżeli ja się odwołuję do tutaj wchodzi, odwołam się do nazwy kolumny.

**Piotr Buczkowski** 46:55  
To myśmy ciała walidacja to na kolumny też.

**Lukasz Bott** 46:55  
Z tabeli.  
Tak działa o k.

**Damian Kaminski** 46:58  
Tak działa, działa natomiast działa tylko nie jak jest duplikat to wtedy nie pamiętam które bierze chyba z głównej nie sprawy.

**Lukasz Bott** 47:05  
Z głównym.

**Janusz Bossak** 47:07  
We.

**Piotr Buczkowski** 47:07  
Znaczy jeżeli.

**Janusz Bossak** 47:07  
Na ten.

**Damian Kaminski** 47:08  
To znaczy, słuchajcie to, co mówi Janusz, to w mojej opinii, żeby jak to wprowadzimy, żeby to potem było kompatybilne wstecz, to raczej powinniśmy podejść do tego, że jest nowy typ reguły, która jest ręczna tabeli. Wtedy ona się nie wyświetla na Górze, jedynie gdzie można ją ustawić, to pole typu przycisk i to w kontekście tabeli i w przyszłości. Jak zrobimy to, co już jest w filmie, czyli wiele reguł na tabelach, bo tak to projektujemy.  
To przeniesiemy to na tamtą listę, czyli to na razie będzie widoczne tu jak wszystkie inne.  
A jak wprowadzimy kontekst, reguły formularza i reguły konkretnej tabeli to od razu tam ją prze filtrujemy, więc dzisiaj wprowadzając tą zmianę, że to jest reguła.  
Ręcz nad tabeli to nawet jeśli zachowamy, powiedziałbym, że nawet jak zachowamy te same skutki, co tutaj.  
To to już potem będzie nam łatwiej będzie większa kompatybilność wstecz, żeby to odfiltrować, bo możemy później dopiero wprowadzić, że taki typ wybierzesz, to tu już ci się nigdy nie wyświetli. Domyślnie musisz ją osadzić, żeby to się wyświetliło, ale już będziemy mieli zdefiniowany ten typ.  
A na początku nawet niech ten typ dziedziczy z tego co jest tutaj.  
Tylko potem nie będzie akcji serwisowej wymiany.

**Piotr Buczkowski** 48:24  
Znaczy, to musiałby być to musiało być typ, że reguła.  
Formuła formularza.  
Żeby że tak samo tak, bo to, bo teraz masz takie coś, że w polu polu przeciw ej możesz wypaść z reguły ręczno i zaznaczał, że nie wyświetlają na głównej ta ta tru barze.

**Damian Kaminski** 48:43  
Tak.

**Piotr Buczkowski** 48:46  
To albo zrobić, że to jest reguła.  
Zrobić typ, że to jest właśnie reguła do do pola przycisk i wtedy, gdzie ten pole przycisku mieście to wszystko jedno, czy na głównym formularzu, czy na formularzu czy na.  
Znaczy w tabeli.

**Damian Kaminski** 49:02  
To nie o to mi wiesz. To inaczej o co innego mi troszeczkę chodzi, że.  
Jak to wprowadzimy po prostu ten nowy typ, to potem będziemy mieli kompatybilność wsteczna. Jak wprowadzimy nową listę reguł przefiltruj tylko po regułach tabel.  
Bo mamy dzisiaj reguły tabel automatyczne, no ale rozmawialiśmy, że tam mogą być tak automatyczne, może być wiele automatyczny w przyszłości.  
No i zakładam też, że jeśli określimy, że to jest ręczna tabeli, no to wtedy już będziemy mogli to odfiltrować.  
Nie mam tego teraz jak pokazać?

**Piotr Buczkowski** 49:36  
No chyba, że tak no.

**Damian Kaminski** 49:38  
Ale wiesz o co mi chodzi, że po prostu jak ten typ będzie to już potem będziemy nie, nie będziemy musieli wstecz poprawiać serwisowo.  
Tylko to już będzie z filcu przefiltrowany, że pokaż mi reguły tabeli, pokażę tą, którą ja oznaczyłem jako tabeli, nawet jeśli ona ma te same skutki, ale ja wiem, że to jest. Używam jej w tabeli.

**Janusz Bossak** 49:58  
Znaczy tak znaczy, dążę do tego, że reguły tabeli powinni być regułami tabeli. Koniec kropka.  
A jak nie mogą być użyte jako reguły tabeli, znaczy nie, nie chciałbym doprowadzić doprowadzać do takiej sytuacji, że mamy jakąś ogólną regułę, którą można prze.  
Zabić poprzez jakąś opcję, że ona staje się regułą tabeli. Ona ma być konstruowana przez konsultanta od razu z myślą, że robię regułę dla tabeli, ona działa tylko i wyłącznie w tabeli. Ma kontekst tabeli, żeby im do głowy nie przychodziło odwoływać się do danych z formularza głównego i tak dalej, i tak tu jesteś w środku tabelki w jednym wierszu i robisz sobie regułę dla tej tabelki nie.

**Kamil Dubaniowski** 50:40  
Czy spodziewam się, że.  
Możesz potrzebować odwołać się do formularza głównego, dodanych do pól do wyborów, jakie tam kryzys?

**Piotr Buczkowski** 50:47  
No ale to jak najbardziej możesz.  
W regule.

**Kamil Dubaniowski** 50:51  
Tak no to to o tym wspominam, tak, żeby to znaczy tak ona ma działać na tabeli, ale jak najbardziej może sięgać po dane z formularza głównego? No bo.

**Piotr Buczkowski** 50:58  
To to myśle to.

**Damian Kaminski** 50:58  
Ale nawet jeszcze dokładnie ma działać na wierszu, bo to jest to trzeba im tłumaczyć, że to nie jest na tabeli tylko na wierszu.

**Kamil Dubaniowski** 51:00  
Tak, tak.

**Janusz Bossak** 51:04  
Pierwszy to tak.  
No tutaj mogą być potrzeby tak jak mówicie dostawania się do.

**Damian Kaminski** 51:11  
No ale jest przecież main kasy, więc albo przez main cast, albo przez albo przez natywne połączenie. Z racji, że wiemy, że ten wiersz jest osadzony w tej tabeli, to już nie wiem jak tu zaproponuję.

**Janusz Bossak** 51:14  
Tak, tak.  
Słuchaj, dobra.

**Kamil Dubaniowski** 51:23  
Znaczy ja bym od razu jeszcze zaznaczył, że spodziewam się, że taka reguła tabeli powinna mieć parametr, że pozwala na uruchomienie masowe.  
I wtedy zaznaczasz jak boksami już tymi jakimiś systemowymi, tak jak mamy masowe reguły na raporcie to zaznacza, że pierwsze materii i wykonujesz to gdzieś tam z poziomu górnej belki, znaczy tej belki tabeli, no bo no wiemy jak się skończy belki i tak będziemy musieli to zrobić i tak.  
No ktoś będzie chciał masowo zaakceptować swoje, na przykład rozpisane koszty.

**Damian Kaminski** 51:50  
No ale to mamy dzisiaj w sensie tylko tyle rzecz musisz osadzić czego.

**Janusz Bossak** 51:55  
No tak, ale musisz zrobić regułę znowu, że ogólną.

**Kamil Dubaniowski** 51:58  
Tak.

**Damian Kaminski** 51:59  
Mhm.

**Janusz Bossak** 51:59  
Tak jakby na formularzu głównym, która zawiera w sobie fori ich row i ją wykonać dla każdego amfory trolla nie i.

**Kamil Dubaniowski** 52:08  
A jeśli tutaj planujemy, że ta reguła ma być do wiersza, no to osadzanie w niej foreo, to powinno być z góry zabronione.

**Damian Kaminski** 52:12  
Mhm.  
I dlatego właśnie postuluję za tym, żeby był to ten typ określony.

**Piotr Buczkowski** 52:18  
Chyba że chcesz, chyba, że masz tabelę zagnieżdżone i Chcesz na ten dobry i zagnieżdżony i coś zrobić.

**Damian Kaminski** 52:23  
No właśnie, albo chyba, że wiesz odwołasz się do tej sprawy, która tu jest Odnośnik i tam będziesz robić, ale to też, a jest w stanie wykryć, czy on robi to w kontekście czegoś innego albo czegoś co istnieje, a nie w kontekście po prostu czystej reguły. I próbuję tu literować.

**Janusz Bossak** 52:39  
Muszę uciekać, bo Przemek już bym tam była. To jest w ogóle szerszy temat. Wczoraj jechałem z jednym z wrażenia owców takich młodszych i mówi dla niego na przykład problemem jest to, że on nigdy nie wie, którą funkcję, w której w którym typie reguły można zastosować i ona się nadaje do tego.

**Damian Kaminski** 52:56  
No właśnie i to może robicie jaj.

**Piotr Buczkowski** 52:57  
Bo to zależy.  
Bo to zależy.

**Damian Kaminski** 52:59  
Jak jak dobrze to określimy, to ja będzie w stanie to im podpowiadać albo raczej przynajmniej pokazywać lampki. To nie jest standardowe zużycie na zastanów się czy to powinno być tak, a a kiedyś dojdziemy do dopracowania takiego, że będzie w stanie od razu dać alternatywę, no ale to małymi krokami.  
Dobra, to podsumowując, co robimy na teraz, robimy ten jakiś nowy znacznik, jakkolwiek kto określimy, czy to będzie nowy typ, czy to będzie tutaj jakieś zaznaczenie, że to dotyczy tej tabeli?  
Ale według mnie powinniśmy to podzielić jakoś to wyróżnić, żeby już wiedzieć w przyszłości, że to dotyczy tabeli.  
Potem możemy dokładać konsekwencje, że jak to jest zaznaczone, to się nie wyświetla na górnej belce albo.

**Lukasz Bott** 53:45  
Jest to jak już.  
Tak no pytanie jest takie, na ile to jest nacji to potrzebny tak no.  
Bo.  
To, że Tomek tak sobie tam zrobił czy coś to powinien dostać burę za to tak chwalicie, a z drugiej strony to też trzeba to uczynić i pewnie jutro o piętnastej na na spotkanie trzeba uczulić, że jeżeli macie tego typu potrzeby, a nie możecie ich zrealizować, no to się cholera skonsultujcie z nami tak i to jest obligatoryjne.

**Damian Kaminski** 54:16  
No ale to konsultuje to nowy wymyślił to pokazał, ja bym nie dawał bury bo to ogranicza ich kreatywność, gdzieś tam coś wymyślił niech ma. No i jeszcze to nie jest produkcyjnie no mamy czas, żeby to zaopiekować, pokazał jak on jak on to sobie rozwiązał.

**Lukasz Bott** 54:21  
Nie, nie no.  
No to o k dobra no no to, no to no dobra, no to teraz trzeba to może inaczej dobra Bożej, może nie, no to my mamy mamy pewien pomysł w tej chwili tak, czy trzeba się z tomkiem dogadać, chłopie, na ile ci, na ile to jest tobie pilne i potrzebne nie.

**Piotr Buczkowski** 54:44  
Znaczy mówię, zrobienie tego co proponowałem, to jest szybkie. Tak, no dzisiaj to zrobię, mogę zrobić.

**Lukasz Bott** 54:50  
Tak, ale to przy założeniu takim, że po prostu jest reguła ręczna i ty jakoś tam kontekst, tak wykrywacz, tak, że jest odpalana w kontekście wiersza.

**Piotr Buczkowski** 54:59  
No.  
Inny cait przekazuje przywołaniu z pola Odnośnik.  
Powoli Przepraszam was pola z pola przycisk.

**Lukasz Bott** 55:11  
Po przycisk.

**Damian Kaminski** 55:12  
Dobra, to znaczy, słuchajcie, to nie jest Tomek jest w ogóle na urlopie, to nie jest coś co co jest uruchomione produkcyjnie z tego co ja wiem.

**Piotr Buczkowski** 55:12  
Umieszczonego w tabeli.

**Damian Kaminski** 55:23  
Aha, on już jest na urlopie do końca roku. Ja propos to tym bardziej ja proponuję tak przedstawmy ten kontekst jutro na spotkaniu z konsultantami.  
Zapytajmy, bo oni już o tym z tego co wiem słyszeli przynajmniej jakaś jakaś część tych ludzi, bo mi nawet na spotkaniu mówili, że Tomek fajną rzecz wymyślił i to by się nam przydało. W sensie właśnie z sugestią, żebyśmy my to zaopiekowali, zrealizowali. Jak to jest moja powiedziała. Mimo od razu słuchajcie, to jest.  
Na podstawie tego, co Tomek zrobił już spojrzenie w historię jest pokazuje, że to ma wady. Tak historia.  
To właśnie jest niepoprawnie zapisane i tak dalej.  
Więc możemy to z nimi przegadać, czy to faktycznie im się przydaje i na spokojnie w przyszłym tygodniu to zaopiekować? To nie, nie musimy teraz rzucać wszystkiego, żeby to zrobić, bo to nie żaden hotfix.  
A i co więcej no.

**Lukasz Bott** 56:13  
Więc to nie od razu to?

**Damian Kaminski** 56:13  
Tak naprawdę ten ekran to jest ekran, który będzie wam modlicie. Według mnie jeszcze max pół roku raczej to przerobimy na reach w ciągu pół roku, więc jakkolwiek tutaj to obsłużymy warto by było, żeby tylko dodać ten znacznik, że jak zacznę z tego korzystać, żeby potem można było to przenieść z drugiej strony, jak zrobimy to dopiero w reakcie możemy to na razie zaprojektować to sobie nagraj, potem serwisowo przepchnął trudno.  
Zastanówmy się nad tym chwilę, jakbym to można było zrobić. Może wróćmy do tego na na kolejnej Radzie, może coś tam wpadnie, chociaż mnie na kolejnej będzie wtorek.  
No to najwyżej będziemy omówimy to nie wiem. W przyszłym tygodniu ty jesteś rozumiem Piotr między świętami a nowym rokiem tak.  
No to będzie pewnie więcej przestrzeni, bo będzie mniej ludzi, więc możemy się spotkać wtedy i do tego wrócić i się zastanowić, bo to nie jest coś, co musisz dzisiaj się tym zajmować.  
Już bardziej pilne bym powiedział, że jest ten xm l, bo który przed chwilą omawialiśmy to też pewnie nic trudnego. Zaraz co zrobił bo tam.  
Yy, bo tam będą pracować przez Weekend i tam już klient wchodzi na testy, więc to by się nam przydało.  
Dobra.  
Myślę, że na tym zakończymy.  
I tyle.  
A do tego wrócimy w przyszłym tygodniu czy tam po świętach? Dobra to dzięki w takim razie.

**Anna Skupinska** 57:45  
No cześć.

**Damian Kaminski** 57:46  
To jest.

**Janusz Bossak** zatrzymano transkrypcję