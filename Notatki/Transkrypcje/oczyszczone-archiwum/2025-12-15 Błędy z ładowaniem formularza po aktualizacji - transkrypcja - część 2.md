**Data spotkania:** 1-2 grudnia 2025 - część 2

---

**Mariusz Piotrzkowski:** Problem został rozwiązany. Okazało się, że przekompilowane / zcachowane pliki DLL w GAC były corrupted i mechanizm tego nie wykrył. Usunęliśmy Newtonsoft* z C:\Windows\assembly\GAC_64, po czym ponownie uruchomiliśmy wszystko i zaczęło działać. Potem napiszę do tego artykuł jak znajdować i wykrywać takie problemy (użyliśmy resmon.exe do znalezienia gdzie znajdował się aktywnie używany plik .dll).

**Daniel Reszka:** Ale to są pliki serwerowe czy AMODITowe? Ogólnie to dziwne, jeśli faktycznie stawiali serwer od zera, że to się tam zadziało ponownie.

**Tomasz Kalinowski:** Wyszło dodatkowo, że postawienie aktywnej dodatkowej witryny psuje ustawienia newtonsoftowe (do działającej produkcji dodano instancję test) i pojawia się ten sam błąd. Żeby znowu mi to zadziałało, musiałem usunąć pliki z lokalizacji c:\windows\assembly\gac_msil\newtonsoft.json\. Będziemy z Mariuszem sprawdzać zachowanie witryn po restarcie w trybie (1 lub 2), (1 i 2), przy wrzuceniu kolejnej witryny na serwer.

**Piotr Buczkowski:** Nie pamiętam kiedy musiałem coś ręcznie usuwać z GAC, chyba to było jeszcze na Windows 2003. Ta DLL to część AMODITa, którą Windows sobie kompiluje i skompilowaną kopiuje do GAC. Tak jak napisałem – dawno nie spotkałem się z problemem z tym mechanizmem.

**Mariusz Piotrzkowski:** Może po prostu jest uszkodzony mechanizm .NET w systemie? Może jakiś `dism /online /cleanup-image /restorehealth` oraz `sfc /scannow` by pomogło?

**Tomasz Kalinowski:** Piotrek, zauważyłem, że u klienta mocno agresywnie pracuje Windows Defender. Przy nowej instancji blokował aplikacje, IT klienta musiało wyłączyć AV na jakiś czas. Może on albo jakieś zmienione polityki wpływają na działanie środowiska w ten sposób, że podmienianie plików powoduje problem z ładowaniem widoków witryny.

**Mariusz Piotrzkowski:** Może być, że po prostu defender blokuje kompilację. Bo kompilacja to taki dosyć "wrażliwy" proces w kontekście antywirusów.

**Daniel Reszka:** Da się dodać jakieś wyjątki na zaporze pod to? (aby to ignorował – czy to zbyt ogólne i nie tylko AMODIT z tego korzysta?)

**Mariusz Piotrzkowski:** Zapora raczej tutaj wiele nie da – to nie problem z połączeniem / siecią. A wyjątki w Windows Defender by można, tylko nie wiadomo co wykluczyć dokładnie.

**Tomasz Kalinowski:** Nie wiem jakie jest severity / protection level po stronie managementu, jeśli jest wysokie, to może blokować wszystko co w jakikolwiek sposób ma wpływ na integralność systemu. Przy asynchronous service pojawiał się komunikat "malicious software".

**Mariusz Piotrzkowski:** Bo nie możemy wszystkiego tak po prostu wykluczyć.

**Tomasz Kalinowski:** Daniel Reszka, takie coś miałem. [Zrzuty ekranu z komunikatami Windows Defender]

**Daniel Reszka:** To moim zdaniem na serwerze błędy w takim razie Defendera.

**Mariusz Piotrzkowski:** Czyli ich wina.

**Piotr Buczkowski:** Jak bardzo ważne jest wskazanie `<bindingRedirect oldVersion="0.0.0.0-12.0.0.0" newVersion="12.0.0.0" />` w web.config? Aktualnie Newtonsoft ma chyba 13.0.3.0, a my mamy w web.config cały czas 12.0.0.0. Ale przy zmianie tego błąd nie ustępował (próbowaliśmy).

**Tomasz Kalinowski:** Ale potem to wyłączyli, błąd był mimo wszystko, w takiej sytuacji trudno stwierdzić czy z poziomu serwera na którym skonfigurowany jest defender dla całej organizacji, czy tam nie było jakiś logów związanych z webapp.

**Mariusz Piotrzkowski:** Sam fakt, że wyłączyli po czasie wiele nie znaczy. Jeżeli się da opracować repro steps, to trzeba sprawdzić z i bez defendera.

**Piotr Buczkowski:** Co do wpisu w web.config, to ważne aby w new nie była nowsza wersja niż jest. Nie pamiętam co się dzieje gdy jest starsza.

**Mariusz Piotrzkowski:** A co jeśli w systemie byłaby jakaś inna aplikacja, która ma Newtonsofta 12, a w AMODITcie jest DLL z wersją 13? Wtedy by chyba z GACa brał tę przekompilowaną z innej apki?

**Piotr Buczkowski:** W GAC może być wiele wersji tej samej biblioteki.

**Tomasz Kalinowski:** Mariusz Piotrzkowski, Piotr Buczkowski, mam ten sam problem w PCBC. [Zrzut ekranu] 1. AMODIT nie był aktualizowany. 2. Wgrywana była nowa wersja konektora (tam plików JSON nie ma). 3. Był aktualizowany klient Symfonia F-K do 2026. Może któraś z tych opcji wpływa jakoś na AMODITa, wywalając pliki newtonsoftowe?

**Piotr Buczkowski:** Ale co jest w logu?

**Tomasz Kalinowski:** [Zrzut ekranu]

**Piotr Buczkowski:** Jak wtedy doszliście, że problem jest w GAC?

**Daniel Reszka:** Tu Mariusz chyba pomagał w tej analizie.

**Tomasz Kalinowski:** Mariusz Piotrzkowski znalazł w resource monitor, zakładka procesor, usługę amodit_asynchronous – gdzie wskazywało na ścieżki biblioteki newtonsoftowej, Mariusz dobrze mówię?

**Tomasz Kalinowski:** [Zrzut ekranu] Usunąłem pliki i teraz jest ok, oba przypadki były wykonywane przy wykorzystaniu AMODIT 250630. W PCBC jest poprawka .99. Może coś jest w plikach AMODITowych co powoduje taki impact?

**Daniel Reszka:** Piotr Buczkowski, musimy tutaj ustalić co i czemu tak się dzieje, aby uniknąć kolejnych takich scenariuszy u pozostałych klientów onprem – najpierw ustalmy czy wina jest po aktualizacji konektora czy Symfonii. Jesteś w stanie Tomek to jakoś stwierdzić?

**Piotr Buczkowski:** Tam są dwie usługi? W jakich wersjach?

**Tomasz Kalinowski:** Tak Piotrek. Obie w wersji czerwcowej. W konektorze nic specjalnego nie ma. [Zrzut ekranu] Jeśli chodzi o Symfo, to czekam na więcej danych.

**Tomasz Kalinowski:** Usunięcie plików Newtonsofta chyba nie pomaga, bo znowu się popsuło.

**Piotr Buczkowski:** Teraz jest tak, restartowałem serwer, to jeszcze jak nie działa, wyślę zaraz update po usunięciu plików. [Zrzut ekranu]

**Piotr Buczkowski:** Czy są jakieś wpisy dotyczące Newtonsoft w web.config?

**Tomasz Kalinowski:** [Zrzut ekranu] Xape twierdzi, że nowa wersja Symfonii może mieć wpływ na działanie webapp – na razie to nic potwierdzonego.

**Piotr Buczkowski:** Usuńcie wpis `<dependentAssembly>`. W sensie całość? Od rozpoczęcia do zakończenia? Czy to na pewno wpis z web.config z aplikacji webowej?

**Tomasz Kalinowski:** Na 100%.

**Piotr Buczkowski:** `<dependentAssembly>` `<assemblyIdentity name="Newtonsoft.Json" publicKeyToken="30ad4fe6b2a6aeed" culture="neutral" />` `<bindingRedirect oldVersion="0.0.0.0-13.0.0.0" newVersion="13.0.0.0" />` `</dependentAssembly>`. Tak jest u nas. Ale u nas nie ma `<applicationSettings>` widocznych na dole.

**Tomasz Kalinowski:** A to tak jak zmieniał Mariusz jak to analizowaliśmy, potem wrócił do 12.0. Najpierw sprawdzaliśmy .NET.

**Piotr Buczkowski:** Usuńcie ten wpis. Czy w Agro też jest Symfonia?

**Tomasz Kalinowski:** Tak.

**Piotr Buczkowski:** Co jest w tym applicationSettings?

**Tomasz Kalinowski:** [Zrzut ekranu] Piotrek, usuwam wszystko co jest w dependentassembly. [Zrzut ekranu] Tu nie wpisywać 13.0.0 tak jak to u was jest?

**Piotr Buczkowski:** Usuń też applicationSettings. Jest błąd w pliku wzorcowym – nie powinno tego być.

**Tomasz Kalinowski:** Git? Piotrek, teraz mam taki wpis w resource. [Zrzut ekranu]

**Piotr Buczkowski:** Czy działa?

**Tomasz Kalinowski:** Tak, ale żeby się upewnić potrzebuję zrestartować serwer.

**Piotr Buczkowski:** Ok.

