**Data spotkania:** 2 grudnia 2025, 08:20

---

**Oktawia Ostrowska:** Oprócz wczorajszych spotkań testowałam zadania ze swojej tablicy, między innymi moduł raportowy. Filip miał też zadania związane z listą. Na dzisiaj mam zadanie odnośnie SimplySign plus zadania z Repozytorium. Dzisiaj będzie odnośnie tego spotkanie, więc będę zagłębiać się w temat. Blokerów nie mam.

**Barbara Michalek:** Jeśli chodzi o mnie, to wczoraj zadania z modułu raportowego, z konfiguracji procesów (naprawy gwarancyjne) i ogólnie widoku formularza. Dzisiaj retest tych zadań.

**Patrycja Walaszczyk:** Ja wczoraj głównie testowałam internal testy edytora graficznego. Na dzisiaj mam retesty, głównie bugi. Blokerów nie mam.

**Filip Liwiński:** U mnie wczoraj Repozytorium plików i spotkanie. Dzisiaj też Repozytorium plików.

**Anna Skupinska:** Wczoraj było sporo spotkań. Pracowałam też nad Repozytorium, czyli API usuwania plików. Chciałam o tym dzisiaj porozmawiać, bo chciałam je trochę zmodyfikować. Pracowałam też wczoraj nad tym, żeby dostosować te API, które już mamy od wyświetlania i pobierania plików, do tego co już jest w Repozytorium, bo używamy `CaseAttachment`. Chciałam Filip, żebyś spróbował te dwa endpointy, które znalazłam. Napiszę później na czacie, o które mi chodzi.

**Filip Liwiński:** Już widziałem, tam jest tylko problem z wyświetleniem podglądu.

**Anna Skupinska:** Czyli nie będzie problemu.

**Filip Liwiński:** Do pobierania plików jeszcze nie sprawdzałem.

**Anna Skupinska:** W takim razie będę się skupiać nad pisaniem testów, bo jeszcze żadnych nie pisałam.

**Adrian Kotowski:** Wczoraj poza planowaniem zajmowałem się projektowaniem mechanizmu uprawnień. Mieliśmy dzienne spotkanie do wprowadzenia do projektu i podziału zadań. Przeglądałem istniejące materiały dotyczące projektu Repozytorium. Mieliśmy już jedną sesję, dzisiaj będziemy kontynuować. Mamy dzisiaj zaplanowane oddzielne spotkanie na podsumowanie moich uwag. Później spotkanie w sprawie BLS w Deutsche Banku w kontekście integracji z e-Poleconym. Będą też inne spotkania na 1:1. Głównie będę się zajmował projektowaniem tego algorytmu.

**Mariusz Piotrzkowski:** Próba z Tomaszem Kalinowskim. Dużo spędziłem czasu na ogarnianiu, czemu na jakimś tam kliencie nie działa po update serwer. Wydaje mi się, że rozkminiłem już co jest problemem. Dzisiaj będę z nim dotestowywał. Oprócz tego były spotkania. Zrobiłem, tylko nie wpisałem, poprawkę internal test z przyciskiem, bo tam się okazało, że czegoś nie dopatrzyłem. Dzisiaj będę się zajmować zmianami na tabelach.

**Lukasz Bott:** Mariusz, taka prośba – jak z Tomkiem ustalicie w końcu co było przyczyną, jeżeli się uda to faktycznie wykryć i naprawić, zróbcie z tego podsumowanie.

**Mariusz Piotrzkowski:** Zrobię podsumowanie i zobaczymy co z tym zrobimy.

**Janusz Bossak:** To jest wsparcie SLA.

**Lukasz Bott:** Wsparcie SLA. Rozumiem, że Piotr Buczkowski też się udzielał wczoraj?

**Mariusz Piotrzkowski:** Trochę pisałem z Piotrem, ale dużo nie wygraliśmy, bo on już się zbierał około 15:00-16:00, a jeszcze z Tomaszem siedziałem do 18:00 i kombinowaliśmy, co może być nie tak.

**Lukasz Bott:** Jak będziecie mieli konkluzje, to daj znać. Może to trzeba gdzieś w jakiejś dokumentacji umieścić.

**Janusz Bossak:** To jest najwyższej rangi hotfix w tej chwili, bo od czwartku im nie działa. W ogóle nie mogą uruchomić. Nie ma nic ważniejszego niż zajęcie się tym. Klient od 3 dni nie może pracować. Dlatego Piotra ściągnąłem z urlopu wczoraj, żeby się też tym zajął. Nie można uruchomić środowiska klienta. Dziwię się trochę Tomaszwowi, że on nie ma backupu, żeby wrócić. Zrobił kilka rzeczy na raz: aktualizację i odtworzył bazę z backupu. Położył sobie kłody pod nogi. Zamiast trzymać się jednej zmiany na raz, to zaczął robić różne rzeczy jednocześnie. Pisałem w którymś momencie tego wątku, żeby się cofnął do wersji, która działała, żeby uruchomić klientowi, a potem dopiero rozpoznawać co się dzieje i na nowo zrobić aktualizację.

**Damian Kaminski:** Nie podeszli do tego w ten sposób jeszcze do tej pory.

**Mariusz Piotrzkowski:** Z tego co mi Tomasz mówi, to było tak, że on podniósł wersję AMODIT, przestało działać, potem cofnął wersję i również nie działało. Nie wiem czy przywracał całą bazę danych do wcześniejszej wersji. Moja teoria jest taka, że coś w `web.config` zostało namieszane, bo od wersji czerwcowej powinno być też dla Reacta uwzględnione folder `reach` (React), że jest dostępny w hostingu IIS. W marcowej tego jeszcze nie ma. Możliwe, że coś się z tymi `web.configami` popsuło, bo wszystkie pozostałe możliwości już sprawdziliśmy. Umówiłem się z nim za niecałe pół godziny ogarnąć.

**Janusz Bossak:** Możesz się wyautować już z tego daily i iść tam z Tomaszem to naprawiać. Naprawdę musimy uruchomić tą instalację.

**Lukasz Brocki:** Ja wczoraj zajmowałem się trochę Comarch Hubem, ale wcześniej był problem z paczką przelewów. Według mnie wszystko działa prawidłowo, czekam na dokładne kroki u klienta, bo u mnie lokalnie wszystko się prawidłowo generuje. Wydaje mi się, że nie ustawiają prawidłowo banku, przez co zły plik tekstowy się generuje. Muszę poczekać na dokładne kroki od nich. Dzisiaj będę kontynuować Comarch ERP.

**Mateusz Kisiel:** Wczoraj robiłem usprawnienia w generowaniu dokumentacji procesu. Wrzuciłem swoją witrynę, więc jak Janusz czy Damian macie czas, to możecie przetestować. Dzisiaj zajmę się rozwojem indeksowania i filtrów użytkownika.

**Marek Dziakowski:** Wczoraj zajmowałem się głównie JRWA. Dzisiaj zostało mi dokończyć od strony formularza, żeby się odpowiednio wyświetlało w polu typu Odnośnik. Poza tym będę dodawał usługę do Sentry Demo, czyli przeniesienie tego, co wydałem na teście, na demo. Mam jeden fail test na Reactcie, więc też się nim zajmę.

**Janusz Bossak:** Odnośnie JRWA – Kamil, do ciebie: dobrze by było, gdybyśmy od razu nawet na tej wersji testowej u Marka zasilili prawdziwym LOT-owskim JRWA.

**Marek Dziakowski:** Zasiliłem kilka pozycji do testów, żeby sprawdzić jak się wyświetla i czy działa. Myślę, że jak będę to wrzucał gdzieś na jakąś witrynę, to tam od razu zasilę wszystkim. Kamil jeszcze miał kilka uwag, żeby to przegadać odnośnie wyświetlania.

**Lukasz Bott:** Kamila nie ma, napisał, że musiał się przełączyć na spotkanie.

**Lukasz Bott:** Jeśli chodzi o wczorajszy dzień, to mieliśmy organizacyjne. Wsparcie wdrożeń i wsparcie sprzedaży. Marcin Staniek poprosił o przygotowanie odpowiedzi do ankiety bezpieczeństwa na firmy Kirchhoff i LOT. Dzisiaj będę aktualizował changelogi dokumentacji, bo trochę tego zalega, zwłaszcza że Mateusz Kołakowski przypomniał w piątek, że bardzo im zależy na tej dokumentacji. No i wsparcie dla wdrożeń, głównie LOT.

**Damian Kaminski:** Jeśli chodzi o wczoraj, to dwa spotkania w kontekście repozytorium. Dzisiaj kontynuujemy działania na backlogu. Poza tym jeszcze dwa spotkania. Jedno w kontekście wsparcia sprzedaży w Pandamed. Skomplikowany temat, klient mocno wkurzony. Poza tym wsparcie w kontekście analizy wyników monitora wydajności w tym kliencie z piątku – CEZ (teraz REP Polska). Spotkałem się wczoraj z Erykiem i trafiliśmy na solidny trop. Dzisiaj jest spotkanie z klientem, Eryk poprosił mnie, żebym w nim uczestniczył. Możliwe, że na tym się zakończy cała analiza. Znaleźliśmy obciążenie serwera w pierwszych dwóch dniach miesiąca, zakładam, że jest to skutek wpływania dużej ilości faktur z poprzedniego miesiąca (rozliczeniowych). W pierwszych 4 godzinach doby działają nieprzerwanie. Jeśli klient potwierdzi, że niewydajność serwera jest cykliczna, to jedyną sugestię, jaką możemy dać, to zmiana zakresu wykonywania tych reguł cyklicznych, albo podniesienie wydajności środowiska bazodanowego.

**Janusz Bossak:** I tak trzeba rozwiązywać – jeden problem na raz. Jak rozwiążemy ten problem, to zobaczymy czy to się poprawi. Dopiero wtedy można decydować co dalej. Po tym wczorajszym chciałem wam pokazać – pracowałem z transkrypcjami i pokażę wam wynik AI-owej obróbki. Wrzuciłem na nasz kanał PM jak powinno wyglądać określanie celów sprintu.

**Janusz Bossak:** Cel sprintu pierwszy: Repozytorium WIM działa jako kompletne MVP u klienta. Cel biznesowy: klient może realnie korzystać z repozytorium dokumentów, tworzyć, edytować, usuwać foldery, zarządzać plikami oraz kontrolować uprawnienia. Kryteria sukcesu: repozytorium zostało zainstalowane u klienta, działa tworzenie/edycja/usuwanie folderów, wgrywanie/pobieranie/podgląd plików, zarządzanie uprawnieniami. Opcjonalnie historia zdarzeń. Zespół: Damian, Ania, Filip, Adrian, Oktawia.

**Janusz Bossak:** Cel sprintu drugi: JRWA dla LOT gotowy do użycia przez konsultantów i klienta. Konsultanci mogą zainstalować i uruchomić moduł JRWA u klienta LOT, a użytkownicy mogą wybierać kategorie oraz automatycznie przenosić dane do pól w sprawie. Kryteria sukcesu: przygotowano struktury JRWA w bazie, funkcjonalność została osadzona w polu Odnośnik do źródła zewnętrznego, użytkownik może wybrać kategorię JRWA, przygotowano paczkę instalacyjną dla LOT, dane z wybranego JRWA poprawnie wpisują się do pól tekstowych na poziomie sprawy. Zespół: Kamil, Marek i testerka.

**Janusz Bossak:** Tak sformułowane cele są zrozumiałe, mierzalne, biznesowe. Tak powinniśmy pracować. Nie trzeba na siłę robić wielu celów sprintu. Jeżeli są dwa istotne, to te dowozimy. To, że mamy więcej zadań drobnych, to OK, robimy pozostałymi osobami.

**Anna Skupinska:** Ja bym chciała jedną rzecz omówić na razie.

*Część spotkania w węższym gronie (Damian, Janusz, Łukasz Bott):*

**Damian Kaminski:** Ostatni raz przeglądaliśmy 28-go. Tu jest Kamila, nie ruszamy. Tu mamy: dokumentacja aktualizacji, artykuły, pole statyczny tekst – zaktualizowanie o używanie funkcji `CreateColor` ze screenami przykładów użycia (prośba od Mateusza).

**Lukasz Bott:** To do mnie dopisz.

**Damian Kaminski:** Dalej mamy: Repozytorium podwójny hover (stare). Stokado – brak wyświetlania powiększ, może słabo widzicie.

**Lukasz Bott:** To trzeba ogarnąć, bo już to przypisałem na ten sprint 49. To niby zostało naprawione i wróciło jak bumerang. Robił to Piotr. Ola znalazła to na 130, a Piotrek wydał to w czerwcowej (66). Może coś innego zepsuło. Piotrek jest nieobecny. Łukasz Brocki tego tematu też wcześniej nie diagnozował, może spróbować jemu to dać? Jest jakaś dziwna zależność między słownikami zagnieżdżonymi.

**Damian Kaminski:** Czy tutaj od razu jesteśmy w stanie kogoś przypisać? Może Marek, jak JRWA skończy?

**Janusz Bossak:** Podejrzewam, że Marek to ogarnie dziś/jutro.

**Lukasz Bott:** To Markowi. Będę monitorował ten temat.

**Damian Kaminski:** Repozytorium – dodawanie klas (Marek sam sobie robi). Dokumentacja: aktualizacja artykułu o serwis do wizualizacji faktury z KSeF.

**Janusz Bossak:** Czyli jest usługa do wizualizacji faktury.

**Damian Kaminski:** Nie do końca rozumiem. To się dzieje lokalnie. Musisz wgrać XSLT zgodnie ze standardem wydanym przez Ministerstwo i dzięki temu masz to lokalnie, a nie jakiś serwis.

**Lukasz Bott:** Przypisz zgłoszenie do mnie, ja spróbuję wyjaśnić o co chodzi. Może chodzi o sytuację, że jest instalacja lokalna u klienta i trzeba dodać na firewallu komunikację z naszym KSeF Connectorem zewnętrznym. Ale gdyby tak było, to by w ogóle nie było mowy o KSeFie.

**Damian Kaminski:** Wyślę mu link od razu na czacie.

**Damian Kaminski:** Kolejne: Błędny wpis z usuniętego wiersza tabeli blokuje historię etapu. Zgłasza Mateusz. W przypadku gdy użytkownik doda wiersz do tabeli zawierającej pole typu plik, wgra plik, a następnie usunie ten wiersz i przekaże sprawę do osoby niebędącej administratorem, to w tabeli `CaseHistoryChanges` pozostaje błędny wpis odnoszący się do CaseID usuniętego wiersza. Skutkiem jest brak możliwości wejścia w historię konkretnego etapu dla zwykłego użytkownika.

**Janusz Bossak:** Niedawno były jakieś poprawki dotyczące pamiętania historii usuniętych rzeczy. To mi pachnie sprawą dla Mariusza.

**Damian Kaminski:** Sprawdziłem na szybko. Przy przekazaniu sprawy, jak nie mam uprawnień administratora, to się nie wyświetla w ogóle ten etap. Wywala się `Object reference not set to an instance of an object` w funkcji `GetCaseHistory`.

**Janusz Bossak:** To może być frontendowy problem. Sprawa dla Mariusza, on sobie sprawdzi i backend i frontend.

**Damian Kaminski:** Poprawki to moje. Mariusz ready to do – to wczoraj wyszło, to co Ola z EA24 zgłosiła. Faktycznie jest niekonsekwencja – jest przycisk "Usuń" widoczny dla administratora dla otwartych spraw, a w tym nowym interfejsie nie jest widoczny dla spraw zamkniętych.

**Janusz Bossak:** Chodzi o to, że my zmieniliśmy miejsce położenia tego czerwonego przycisku.

**Lukasz Bott:** Ola zgłosiła, bo korzystają z chmury, myśmy zaktualizowali chmurę i nagle się w tym interfejsie nie połapali. Oczekiwała, że ta funkcjonalność pozostała pod literką "i".

**Janusz Bossak:** Przenieśliśmy już tam, trzymajmy się tej nowej koncepcji. Poprawka tego błędu powinna polegać tylko na tym, żeby to "Usuń" tam było dla zamkniętych spraw. A zupełnie odrębnym tematem jest to, czy nie zmienić tego UX-owo – po pierwszym etapie przenieść to do tych 3 kropek "Więcej". Według mnie to nie powinna być tak łatwo dostępna czynność.

**Lukasz Bott:** Zastanawiam się, czy nie powinno być tam potwierdzenia "czy na pewno chcesz usunąć?".

**Damian Kaminski:** Jest potwierdzenie. Tylko ten komunikat jest inny, za mały niż wszystkie inne. Wszystkie inne są jak `ShowMessage`, a to jest inna czcionka, większa.

**Janusz Bossak:** To trzeba zgłosić jako osobną poprawkę.

**Damian Kaminski:** Omówiliśmy wszystko. Ostatnie to moje związane z Repozytorium, więc wszystkie są zaopiekowane.
