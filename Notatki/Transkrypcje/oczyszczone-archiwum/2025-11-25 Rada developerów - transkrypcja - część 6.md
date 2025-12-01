**Data spotkania:** 25 listopada 2025, 09:00 - część 6

---

**Damian Kaminski:** No źle. Tu w ogóle nie równo, źle wygląda.

**Janusz Bossak:** Trzeba.

**Kamil Dubaniowski:** A tak jest na v0, w sensie nie masz do standardowych rozmiarów kontrolek.

**Damian Kaminski:** To samo. Jest źle, to tak samo powiększenie zachowuje tę proporcję.

**Piotr Buczkowski:** Nie masz jakoś tam jest takie coś, że małe coś, tak mały.

**Damian Kaminski:** Nie, nie jest to procent, mam wyświetlanie, nie, tutaj też jest jakaś niespójność mniejsza, ale jest coś tu jest nie tak z tymi kafelkami.

**Janusz Bossak:** Zrobiliśmy.

**Lukasz Bott:** Nie, nie jest.

**Damian Kaminski:** Nie wiem, czy tu widzicie, ale to jest delikatnie inne.

**Piotr Buczkowski:** Kiedyś był problem, jeżeli przybliżenie było końcówka na 5.

**Lukasz Bott:** Może masz wpływ na ekran?

**Damian Kaminski:** Tak, ale to Piotrze, tak samo jest tutaj. Tylko to wiesz, teraz na takim rozdzielczości nie, nie jest OK, nie jest OK. To jest nierówno, tylko to jest tak mała nierówność, że.

**Piotr Buczkowski:** Nie, teraz jest OK. No nie wiem, mówię, kiedyś. Kiedyś problem był, jeżeli powiększenie było na 20, końcówka no 5 miało ostatnio.

**Janusz Bossak:** I to nie, nie powiększenie ekranu takie tutaj, z ręki, tylko powiększenie, które masz w ustawieniach systemowych.

**Piotr Buczkowski:** Tak, tylko.

**Damian Kaminski:** Nie mam tego powiększenia ustawienia ekranu, to są już wam pokażę.

**Janusz Bossak:** Ale ten podpis to jest źle. W ogóle coś, to to jest całkowicie.

**Piotr Buczkowski:** To.

**Lukasz Bott:** Tak, tak, to widać, nie, się rozjechały pola, tak i jednej z innego rozmiaru, drugiego innego i skalowanie. Skalowanie obrazu powoduje.

**Damian Kaminski:** Mam 100%.

**Janusz Bossak:** Co? No właśnie, tu się ustawiało, lekarz to 20, 125, tak, jak się to ustawia 125, to wtedy się tam zjeżdżało, nie?

**Damian Kaminski:** Zaraz, to mam tutaj ten ekran. Mam 100. Tak, to się. Tak, tak, tak, to to potwierdzam, ale to tego nie mam, no.

**Piotr Buczkowski:** Nie wiem, mi chodziło o wejść do swojego profilu użytkownika.

**Janusz Bossak:** No już tam pokazywał, a jeszcze gdzieś indziej.

**Piotr Buczkowski:** Profil użytkownika pokazywałeś. Bo nie zauważyłem.

**Janusz Bossak:** No ale.

**Damian Kaminski:** AMODIT?

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** Już nie, tego nie pokazywałem, jeszcze już pokazuje. Gotu nie ma chyba procentów, tu jest tylko ten.

**Piotr Buczkowski:** Jest, masz mały rozmiar formularza, zmień na duże rozmiar formularza.

**Lukasz Bott:** Na środku, no.

**Piotr Buczkowski:** No tutaj.

**Damian Kaminski:** Mały, nitu, dobra.

**Piotr Buczkowski:** Czym domyślnie? Teraz wejść na sprawę.

**Damian Kaminski:** Teraz jest równo, masz rad?

**Piotr Buczkowski:** Czyli dla, dla małego nie jest to prawidłowo rozwiązane.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** OK.

**Damian Kaminski:** Teraz jest równiutko wszędzie.

**Anna Skupinska:** Będzie, włosow, zgłosić błąd.

**Damian Kaminski:** Nawet zapomniałem o tym małym, ale tak, no, kiedyś coś tam testowałem i i tak zostało. Dobra, włączę to, będę pamiętał. Rzucę to. Dobra, chyba na dzisiaj wszystko, ta reszta Rady to już są tematy, które tam dłużej sobie czekają, więc pewnie jeszcze poczekają, nikt tu ich nie eskalował.

**Janusz Bossak:** O, dzięki bardzo.

**Kamil Dubaniowski:** Dzięki.

**Damian Kaminski:** To my się słyszymy na designie, jak rozumiem, tak, a Janusz w kontekście, jak masz chwilę.

**Janusz Bossak:** Tak. On jest, mam.

**Damian Kaminski:** To zostańmy, możecie się rozłączać, jak chcecie, bo co tu jeszcze przedstawić, bo to może z Przemkiem pogadajcie sobie. Co z tym robimy, mianowicie? No ja postaram się to przedstawić, jak będzie potrzebny Adrian, to go oddzwonimy, chodzi o sytuację taką, że. Integracja z Connector po nowemu, którą Adrian zrobił, to jest zupełnie wywrócenie, można powiedzieć stolika tego, jak było, czyli do tej pory robiliśmy to na jakieś Handler, ach, wcześniej Handler. Natomiast Adrian przygotował zupełnie nowe endpoint, który jest osadzony na tych naszych standardowych mechanizmach REST API, czyli tak jak połączenia ze sprawami z dowolnego innego narzędzia i teraz, jaka jest tego konsekwencja, dlaczego tak zrobił? Po pierwsze dlatego, że uznał, że te Handlery są krótkowzroczne, że kiedyś i tak przejdziemy na jakiegoś tam .NET Core czy coś takiego, bo to, co to, na czym pracujemy, przestało już być wspierane przez Microsoft, a ten drugi jest. No, jeżeli tak, kiedyś trzeba było do tego dojść.

**Janusz Bossak:** No.

**Damian Kaminski:** Ale pojawia się z tego powodu problem, że teraz każdy, kto kupuje KSeF Connector, musi mieć w licencji REST API. No i teraz konkluzja albo KSeF Connector za darmo dajemy w licencji.

**Janusz Bossak:** Nie. Nie, no.

**Damian Kaminski:** No.

**Janusz Bossak:** Mariana, każdym razem Adrian coś na kombinuje, no. Takie rzeczy absolutnie nie wymagają REST API. No to ma być.

**Damian Kaminski:** No wczoraj miałem podobną reakcję, trochę mnie przekonał tymi Handler, ale no problem jest i teraz albo w niego, tylko że tak powiem, czy napiszę do Kamila, że to.

**Janusz Bossak:** Ponad, ponad. Nie wiem, nie.

**Damian Kaminski:** No to pytanie, trzeba to zaopiekować, zanim w to pójdziemy, bo już tam wiesz, Piotra.

**Janusz Bossak:** Już ile razem wiem, że Adrianowi nie wolno dawać takich tematów do robienia samodzielnie, on musi.

**Damian Kaminski:** No nie, ja tego nie przewidziałem, dopiero wiesz, jak doszło do produktu, wiesz, to jest wszystko przeszło. Doszło do produkcji, ja mówię, ale zaraz, jak to trzeba?

**Janusz Bossak:** Musi też rzeczy. On zawsze wymyśla jakieś kurna bazowe kur. Zmiany, no. Które wprowadzają więcej zamieszania niż pożytku dają. Bo przyszłościowo za 5 lat to tak będzie lepiej. No ja to ledwo prostu. Po pierwsze, absolutnie nie może to wymagać naszego REST API, po prostu ma korzystać. No, to jest nasza wewnętrzna integracja. No, klienta trzeba zmuszać do tego, żeby kupił nasze REST API, skoro kupuje KSeF Connector, no. Zresztą my robimy tę integrację. KSeF Connector, a nie klient sobie robi, do czego ma płacić za REST API.

**Damian Kaminski:** No zgadzam się z tobą, dlatego to wyskalowałem, bo już wczoraj stwierdziłem, że dobra, jest tak, może i to ma sens, natomiast problem licencyjny pozostaje, dlatego zgłaszam to zanim to, że tak powiem, pójdzie szeroko.

**Janusz Bossak:** To nie może być w ogóle przedmiotem problemu licencyjnego. Nie. To jest nasza integracja, do licha ciężkiego, no. Nasza, to my ją robimy? Co to ma wspólnego z REST API? Znaczy w sensie licencji REST API?

**Damian Kaminski:** No bo to znaczy, to jak jest to teraz zrobione? No to w zasadzie próba połączenia z AMODIT Connector, która zakończy się brak licencji na REST API.

**Janusz Bossak:** To ma tak zrobić, to ma tak zrobić, żeby to omijało to.

**Damian Kaminski:** To może go w dzwonimy i niech on powie.

**Janusz Bossak:** To mam być. Nie mam czasu, muszę, idę na ten.

**Damian Kaminski:** OK, to ja z nim pogadam. O jejku. No wszyscy będą niezadowoleni z tego. Z konsekwencji tego, co się wydarzyło, no ale to jest poradzę, no. Nie powiedział o tym. Nie i nie przewidział tego, nie wiem. No nie przewidział, że to jest licencji, no nie wiem, jak to, jak to mu wyszło, tak, że.

**Janusz Bossak:** Coś takiego, że my robimy sobie KSeF? Connector, tak i nagle w związku z tym jest potrzebna licencja REST API, no nie, no po prostu ma tak zrobić, żeby nie trzeba było. Uciekam na razie, pogadaj, możemy potem na design, a go wciągnąć za godzinę, no.

**Damian Kaminski:** No dobra, dobra. Dobra, dobra, OK, pa.

**Janusz Bossak:** Nowej.

