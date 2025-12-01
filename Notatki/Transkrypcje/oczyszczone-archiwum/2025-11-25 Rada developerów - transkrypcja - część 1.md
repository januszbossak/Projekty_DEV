**Data spotkania:** 25 listopada 2025, 09:00

---

**Anna Skupinska:** Cześć.

**Damian Kaminski:** Cześć.

**Anna Skupinska:** Jeśli chodzi o to szkolenie GitHub, tak szybko, zanim zaczniemy – dobra, to, że nie do wszystkich doszły maile i chyba jest przestawione.

**Damian Kaminski:** To napisz to do Przemka, dobra, bo to powinno wcześniej wybrzmieć tam w czacie, ktoś napisał tak.

**Anna Skupinska:** A jeszcze już, już, już napisałam, jest to, jest to tym rozmowa chyba.

**Damian Kaminski:** No to OK. Także już.

**Janusz Bossak:** Generalnie tego szkolenia.

**Anna Skupinska:** Tak, ja Mateuszowi Kisielowi napisałam.

**Janusz Bossak:** Tak, teraz nie ma tego szkolenia. Wczoraj dowiedziałem się od Przemka Sołdackiego. I ono jest przeniesione na grudzień. Pytam, bo były 2 tury? Nie, nie – zapisywali się na teraz, drudzy na grudzień, ale jest przeniesione na grudzień. I na styczeń, przy czym lista osób uczestników jest inna niż ta, co byście zgłaszali, bo wysłał po swojemu. Nie czekał na to, co ja mu wysłałem, tylko wysłał już jakiś tam inny podział, więc trzeba sprawdzić, kto jest na którym przykład.

**Anna Skupinska:** A to, to mam nadzieję, że jako Marek nie będzie nam wysyłał zaproszenia, a nie gdzieś potwierdzenia. Te maile, które nie działają.

**Janusz Bossak:** Nie, podobno wszystkie działają.

**Anna Skupinska:** Te są nie nasze. I AM.

**Janusz Bossak:** I twierdzi, że Lemon Pro sprawdził i na dowolnie skonstruowany email przychodzi, czyli albo na astrafox.pl albo na amodit.com. Zależności od tego, kto ma to na każdy z tych i jeszcze na.

**Piotr Buczkowski:** Do kogo, do kogo przechodzi?

**Janusz Bossak:** Nie wiem, Przemek twierdzi, że Lemon Pro sprawdzili i wszyscy mają.

**Piotr Buczkowski:** Oczywiście sprawdzenie polegało na tym, że wysłali coś na ten mail i te osoby to zauważyły, potwierdziły.

**Janusz Bossak:** Przekierowany. Nie wiem.

**Piotr Buczkowski:** Wiedziałem, że to po sobie jak twierdzi, OK.

**Janusz Bossak:** Wątpię, wątpię, ponieważ ja mam AMODIT i do mnie nie przyszedł żaden mail na astrafox.pl z pytaniem, czy dochodzi do ciebie ten mail. Więc to jest rzecz do przetestowania i sprawdzenia jeszcze.

**Damian Kaminski:** Dobra, zacznijmy od tematów, powiedzmy, prostszych, zakładam, że tu będzie odpowiedź. Tak, nie Piotrze, kwestie licencyjne, integracja z AD. Czy tu jest jakieś różne, czyli taki mamy? Tu użyto licencję na to użytkowników konta zwykłe, to znaczy, że można mieć 100 kont aktywnych, czyli takich, na które można się zalogować. Jak wyłączymy 100 pierwsze, to 100 czy tam setne, to 100 pierwsze możemy wtedy włączyć. Czy inna zasada panuje w kontekście integracji z AD?

**Piotr Buczkowski:** Jak dokładnie to samo?

**Damian Kaminski:** No to dla mnie to, to nie wiem, skąd to Łukasz wziął.

**Kamil Dubaniowski:** Za szybko, za szybko zaczęłaś piłkarzem.

**Piotr Buczkowski:** No, czy może możesz się zalogować tylko na pierwsze konta, ile, tyle ile masz licencji? Przed czym konta administracyjne są brane?

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Priorytetowe, tak, że po pierwsze konto administracyjne.

**Damian Kaminski:** Jasne.

**Piotr Buczkowski:** A po drugie, a dalej konta zwykłe, no także by administrator mógł się zalogować i coś tam zmienić, tak?

**Damian Kaminski:** I to jest. OK, ale pojdzie jest tak, bo, bo.

**Piotr Buczkowski:** Tak, tak, tak, jeżeli dodasz to jakieś nowe konto poza limit, no to ten użytkownik nie będzie mógł się zalogować. Czyli musisz od ministra – to musi wejść i zablokować jakieś inne konto wcześniejsze.

**Lukasz Bott:** Dobra, przepraszam, bo ja się dopiero teraz włączyłem. Czyli jaka jest konkluzja z tym AD i tymi kontami?

**Damian Kaminski:** Konta aktywne – nie ma znaczenia, jakie jest źródło kont, jest ilość kont aktywnych.

**Piotr Buczkowski:** Nie ma znaczenia i nie ma znaczenia. Jest to, jest dokładnie ta sama zasada. Synchronizacja dotyczy tylko tworzenia kont przez synchronizację. Nie jest, nie jest prowadzona licencja, konto otworzone albo blokowane na podstawie stanu z tego źródła zewnętrznego. Czy to jest AD? Czy to jest tabela, czy to jest cokolwiek innego?

**Lukasz Bott:** Czyli tak jak napisałem o tym, czy ktoś w danym momencie się może zalogować, czy nie decyduje ten mechanizm. Kontrola jest w momencie próby zalogowania się.

**Piotr Buczkowski:** Tak.

**Lukasz Bott:** Do końca.

**Piotr Buczkowski:** Tam jest takie coś, że konto zablokowane z powodu braku licencji. To nie jest to, że jest związane z blokadą, to jest tylko. W pamięci zablokowane z powodu braku licencji, tak, nie w bazie danych. Jeżeli ktoś odda, jeżeli ktoś zablokuje jakieś konto wcześniejsze, to to tematycznie się odblokowuje.

**Damian Kaminski:** Tak, ale to oznacza, że. Mhm. O ile jest jedynym kontem zablokowanym i ma?

**Piotr Buczkowski:** No tak, tak, tak jeszcze.

**Damian Kaminski:** Bo jeśli są 2 zablokowane, to też niższe ID się odblokuje.

**Piotr Buczkowski:** Tak, dokładnie, tak.

**Damian Kaminski:** OK. Dobra, Kamil, czy to wymaga jeszcze tu między wami? To była Łukaszem ty. Nie, to nagra.

**Lukasz Bott:** Rozumiem, że to nagrywamy, tak?

**Janusz Bossak:** Tak, tak.

**Kamil Dubaniowski:** Tak, tak, tak, ale no teraz konkluzja Łukasz, tak, no bo to dopóki nie zablokujesz jakiegoś konta, to tamto takie zablokowane przez brak licencji się nigdy nie zaloguje. Nie, nie ma znaczenia sesja, że teraz ktoś się tam wylogował, no bo to ja to tak zrozumiałem. Odpowiedź do LOTU, która poszła, nie ma znaczenia sesja, dopóki nie zablokujesz konta komuś, to ten zablokowany przez brak licencji nigdy się nie zaloguje i to zawsze będzie ta sama zablokowana osoba przez brak licencji, to się nie zmieni.

**Piotr Buczkowski:** No nie.

**Damian Kaminski:** Tak.

**Piotr Buczkowski:** No tak.

**Damian Kaminski:** Tak i niezależnie, że to jest blokada ręczna czy synchronizacja AD.

**Piotr Buczkowski:** Chyba, że chyba, że ustawisz tego zablokowanego użytkownika jako administrator, to trafi w do puli tych odblokowanych, a wypnij jakiegoś zwykłego użytkownika do blokowanych.

**Damian Kaminski:** Mhm.

**Lukasz Bott:** No.

**Damian Kaminski:** Ale to też, to o tych administratorach to nie wiedziałem, to też dobrze wiedzieć, tak, tak słusznie.

**Piotr Buczkowski:** Chodzi o to, żeby administrator mógł się zalogować i.

**Damian Kaminski:** Mimo że ma konto z wysokim ID.

**Piotr Buczkowski:** No i pozmieniać, tak.

**Lukasz Bott:** Dobra, to czekajcie, to bo mówisz, bo człowiek się tak pod końcówkę jeszcze raz, czyli scenariusz następujący – synchronizuję 1000 kont z AD, one będą w bazie danych oznaczone jako aktywne.

**Kamil Dubaniowski:** Tak.

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** W zakładce.

**Lukasz Bott:** Dobry i to jest dobrze, zapłacę w bazie danych zakładce, wam wolicie, widzę jako aktywne.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Jeżeli, jeżeli AD aktywne jest ustawione, jeżeli AD aktywne jest. Bo może być tak ustawione, że synchronizuj też nieaktywny, z AD, tak.

**Lukasz Bott:** OK, dobra, synchronizujemy aktywne, tak, chodzi mi o scenariusz taki, że zaimportowałem 1000, synchronizowałem 1000 kont aktywnych z AD, tyle mi się kont utworzyło w AMODIT i teraz mamy sytuację taką, że w kluczu licencyjnym jest 750 licencji dla nazywanych użytkowników. No i teraz mamy dzień w taki, w którym 750 użytkowników się zalogowało do systemu.

**Damian Kaminski:** Mhm.

**Lukasz Bott:** I pytanie, co, jeśli co się dzieje w momencie, gdy 751 spróbuje się zalogować?

**Damian Kaminski:** Nie ma to znaczenia, Łukasz, logowanie samo nie ma znaczenia. Jeszcze raz – trwa synchronizacja. Masz 1000 użytkowników.

**Piotr Buczkowski:** Nie ma to znaczenia żadnego.

**Damian Kaminski:** Załóżmy, że powiedzmy jest czysto, taka teoretyczna, nie ma, że nikogo więcej nie ma, żadnego admina, jest powiedzmy, ładujesz. 1000 użytkowników – pierwszych 750, których powstanie będzie odblokowany, bo według ID to idzie i ostatnich 250 domyślnie zostaną zablokowani jako przekroczenie licencji.

**Lukasz Bott:** Tak, no bo to jest tego, czy.

**Kamil Dubaniowski:** Czyli to nie będzie konto zablokowane?

**Piotr Buczkowski:** Nie będą mogli się zalogować, niezależnie czy wchodzicie akurat będzie działać 10, 20 czy czy 707, 3, 10, 7, 70, 50 użytkowników.

**Damian Kaminski:** Tak w m. Czy nikt?

**Lukasz Bott:** OK. Czyli, czyli. Czyli OK. Czyli, czyli dobra, bo ja Piotrek, ciebie zrozumiałem jak to gdzieś tam wcześniej ten wywód w piątek na konsultantów mówiłeś, że wszyscy będą wszy. Będą mieli prawo tak jakby dostępu, tylko że.

**Piotr Buczkowski:** Wiem, wiem. Wszyscy będą blokowani.

**Lukasz Bott:** Ten nadmiar będzie blokowany.

**Piotr Buczkowski:** Ale tylko, tylko ci, którzy się mieszczą w tym limicie, się 750 po i to mogli się zalogować. Innym będzie pojawiał się błąd, że nie możesz się zalogować, bo przekroczono limit licencji, czy tam jakoś tak?

**Lukasz Bott:** OK, no to. Czyli innymi słowy, mamy 1000?

**Damian Kaminski:** Dobra, wam wyjaśnione.

**Lukasz Bott:** Pierwszy raz 1000 synchronizowałem licencji, skrócie licencji jest 750, to 250.

**Damian Kaminski:** No.

**Kamil Dubaniowski:** Ostatnich.

**Piotr Buczkowski:** 250 o najwyższej AD nie będzie mogło się zalogować, nieważne ilu innych użytkowników będzie aktualnie pracować.

**Lukasz Bott:** 250 ostatnich będzie miało, nie będzie mogła się zalogować. Dobra, OK, dobra, dzięki. No to mamy 2 ściany.

