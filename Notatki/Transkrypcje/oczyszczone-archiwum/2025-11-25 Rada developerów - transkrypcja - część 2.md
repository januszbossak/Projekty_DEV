**Data spotkania:** 25 listopada 2025, 09:00 - część 2

---

**Damian Kaminski:** Dobra, to kolejny temat, który Piotr, do ciebie pytanie. W Rossmanie ponoć pojawiają się takie informacje – osiągnięto limit spraw dla P.

**Piotr Buczkowski:** Byłem wczoraj, wczoraj się pojawiło.

**Damian Kaminski:** No i to jest związane chyba z jakimś tam restartem, czymś serwera czy aplikacji. Nie wiem dokładnie, tak, tutaj Łukasz zasugerował. Więc pytanie.

**Piotr Buczkowski:** To jest sprawa, której, której nie możemy rozwiązać od wielu lat. Czasami się zdarza po prostu.

**Damian Kaminski:** Może trzeba? OK. Czyli nie znamy przyczyny.

**Piotr Buczkowski:** Trzeba byłoby to dokładnie przeanalizować. Tylko to analizował już wiele było – 3 osoby i żadna nie wpadła. Nie, nie wymyśliła, jak to rozwiązać.

**Lukasz Bott:** Znaczy nie wymyśliła, czy nie, nie, nie.

**Damian Kaminski:** Ale w tym ty, czy ty jeszcze nie podchodziłeś do tego?

**Piotr Buczkowski:** Nie wiem. Zawsze było, że a to, to niech tamten się tak, ja do nich tamte się zajmie, bo nie ma czasu, to.

**Damian Kaminski:** OK.

**Lukasz Bott:** Ale moment, moment – analizowali, ale nie, nie. Nie znamy przyczyny tak naprawdę, tak.

**Damian Kaminski:** No tak, tak, no nie doszli do przyczyn.

**Piotr Buczkowski:** Z jakiś powodów czasami głupi obiekt licencji.

**Lukasz Bott:** No bo.

**Piotr Buczkowski:** To jest, to się działa, to się, to się dzieje w usłudze. Po prostu przed kolejnym wywołaniu, jeżeli uda mu się odświeżyć obiekt licencji i to wszystko działa.

**Lukasz Bott:** No i, i stąd, stąd.

**Piotr Buczkowski:** Najczęściej, najczęściej jest to tak, że po prostu ten obiekt licencji jakiś po prostu w pamięci znika. I nie, nie jest w stanie go odświeżyć, bo jest jakiś błąd.

**Damian Kaminski:** OK. Czyli to może mieć nawet podłoże sieciowe.

**Piotr Buczkowski:** Tak.

**Lukasz Bott:** No to tak, jak mówiłem.

**Damian Kaminski:** A nie aplikacyjne, no właśnie, OK.

**Piotr Buczkowski:** Trzeba byłoby wczoraj to maile było, trzeba byłoby sprawdzić, że na tym serwerze, czy to w powstało, zobaczyć, czy były jakieś błędy dostępu do baz danych w tym momencie, czy tam kilka minut przed wysłaniem tych maili, tak.

**Damian Kaminski:** To jest na serwerze, gdzie stoi usługa? Tak.

**Piotr Buczkowski:** Tak, przepraszam, usługi to są błędy z usługi, LOT mail albo LOT, przynajmniej wczoraj tak było. Tak, jak mówię, kolejne wywołanie usługi najczęściej już wszystko jest OK. Wczoraj też właśnie tylko było jedna seria maili i i tyle. W kolejnej już sobie odczytał.

**Damian Kaminski:** Dobra. Zostawmy to na tej Radzie, może coś tu wpadnie. Idźmy dalej. Tutaj też powinien być temat prosty. Rejestr, synchronizacja sprawy usunięte. I teraz pytanie, czy to w ogóle jest, to jest też zgłoszenie niewynikające gdzieś wdrożenia, albo nic na to nie wskazuje. To jest młody wdrożeniowiec, który nie miał tej świadomości, ale ja się nieraz z doświadczonymi borykałem, że no słuchaj, coś tu nie mogę się synchronizować, bo klucz nie jest unikalny. No to zajrzeć do usuniętych, zagląda do usuniętych, tylko że a w usuniętych nic nie ma, albo trzeba w usuniętych przefiltrować po. Rejestrze, bo domyślnie rejestry się nie wyświetlają, więc to jest kilka aspektów. Pytanie po pierwsze, czy usunięte chcemy wykluczyć spoza klucza, jest ryzyko. Tu już gadaliśmy z Kamilem, że usunięto. No właśnie, więc niekoniecznie to jest słuszne krok.

**Piotr Buczkowski:** Trzeba przywrócić, przywrócić.

**Kamil Dubaniowski:** Ja tam w komentarzu dałem do tego propozycję właśnie do zastanowienia, może na Radzie, czy w momencie, kiedy ponownie pojawia się usunięta sprawa i klucz występuje w źródle, no to czy nie przywrócić tej sprawy usuniętej?

**Piotr Buczkowski:** Przywrócić, przywrócić – nikt o tym nie pomyślał tej pory. No bo to, to ma być, to ma być.

**Damian Kaminski:** Dobra, to znaczy, ja bym powiedział, że też tutaj jest źle, bo powinno być od razu wskazanie, bo te pytania by nie padały. Czyli tak – klucz nie jest unikalny. Przejrzyj wszystkie sprawy w tym usunięte i ktoś sobie zrobi raport ze wszystkimi.

**Piotr Buczkowski:** Młodsze pod, trzeba, trzeba. Trzeba. Trzeba to ujednolicić, nie powinien przywracać, tak, bo jest normalne, że.

**Janusz Bossak:** Znaczy.

**Piotr Buczkowski:** Powiedzmy była jakiś wpis w rejestrze, już nie ma, bo co jakiś powodów w źródle zniknął, ale jest przywracany, no bo jednak jest potrzebny, tak.

**Damian Kaminski:** Mhm, tylko tutaj ja bym powiedział, że to częściej może być też przyczyną coś takiego, że. Ten klucz nie jest unikalny, bo ktoś jak utworzył już kilka spraw, kliknął sobie usuń i to nawet niekoniecznie dotyczy, że to już produkcyjnie coś tu nie działa, tylko ktoś dopiero to odpala i nie może znaleźć, czemu nie może nałożyć klucza, bo tam jest kilka spraw, które mają zera po prostu w tym polach, które są kluczem i nie są unikalne, więc ja bym po pierwsze tu bym dodał z tym komunikacie, że.

**Lukasz Bott:** Dokładnie, tak to jest. Albo tu. Albo puste wartości.

**Damian Kaminski:** Sprawdź wszystkie istniejące sprawy tego rejestru, w tym usunięte i to już będzie samo rozwiązany problem.

**Janusz Bossak:** Słuchajcie, bo tam w ogóle z tym, z tym oznaczaniem z rejestru czegoś jako usunięte to było głębsza myśl z tym związana, to było coś – to usunięte miało symulować dezaktywowane, znaczy one niby jest, tylko jest reaktywowane, tak jak w słowniku jest dezaktywowane.

**Damian Kaminski:** Częściowo. Mhm.

**Janusz Bossak:** I trochę jest takie pomylenie w tej chwili, takie poznawcze, tak, znaczy, że coś jest w usuniętych, to nie jest usunięte, to jest dezaktywowane, tylko my tego nie opisujemy. Ja nawet nie wiem, czy to widać tutaj w tych usuniętych te rzeczy z rejestru.

**Damian Kaminski:** To znaczy widać dopiero, jak zrobisz filtr na rejestrze, czyli jak mam nawet teczkę kartoteka, która jest rejestrem, to dopiero mi się pojawi kartoteka, inaczej nie widać, właśnie i to też powoduje, że no wchodzę w usunięte, tu nie ma. No ma rację, że nie ma.

**Lukasz Bott:** Nie z rejestru nie wiedzieć.

**Janusz Bossak:** No właśnie. To jest, no właśnie, dlatego ich tutaj nie ma, bo ich nie miało być. Bo o to chodziło.

**Damian Kaminski:** No ale gdzie się musimy?

**Janusz Bossak:** O to chodziło, żeby ich nigdy nie usunąć. Bo to jest to samo, co ze słownikiem – chodziło o to, że my uzna. Mieliśmy wtedy parę lat temu. Że oznaczamy sobie coś jako usunięte, ale w kontekście rejestru jako dezaktywowane, tak jak, żeby nie było potem sytuacji, że jeżeli ktoś tego użył gdzieś na sprawach, a potem sobie dezaktywował, czyli usunął. No żeby jednak ten. Wpis był.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Serwowany, czyli usunął. No żeby jednak ten. Wpis był.

**Damian Kaminski:** Dobra, słuchajcie, według mnie z tego wynikają 2 konkluzje, jedna to jest to, co zasugerował Kamil, bo to jest spójne z tym, co powiedział przed chwilą Janusz, czyli filtr.

**Janusz Bossak:** I.

**Damian Kaminski:** Jakie synchronizacja, że. Bytu, który jest, to go po prostu aktywujemy, konsekwencj. Do tego jest to, że jest jakaś historia stara, który ktoś może nie mieć świadomości, no ale ten byt był, więc my zakładamy, że go tak jakby wznawiamy. I tyle, jak ktoś, kto skutecznie usunąć, to taka opcja jest ukryta, tak jak Janusz zasugerował, że to celowo było ukryte, ale jest. Ja bym jeszcze tu jako uzupełnienie dołożył właśnie, że znajdź sprawy w statusie usuniętym. I pozbądź się, jeśli, jeśli po prostu potrzebujesz tej unikalności i chyba tak bym to zostawił te 2 rzeczy.

**Lukasz Bott:** No tutaj do komunikatu to się.

**Damian Kaminski:** Czy się zgadzacie z tym, czy?

**Lukasz Bott:** Do komunikatu ten dopisek to się zgodzę, bo ten scenariusz, który podałeś się Damian, tak, że najczęściej to jest w środowisku jakieś tam testowym, przygotowujesz sobie i zanim robisz to synchronizację, to już wcześniej coś sobie działałeś na tym rejestrze, żeby chociażby sprawdzić, on działa i sobie po usuwałeś sprawy. Ja też się. No ja się też wielokrotnie na tym złapałem, tak?

**Damian Kaminski:** Czy? No 2 sprawy istnieją dokładnie. Tak, tak, tak, no tylko że wiesz, wiedziałeś, co trzeba zrobić. No młodzi nie wiedzą.

**Lukasz Bott:** No nie wiesz, co zanim tym razem to się zastanawiałem, ale o co chodzi?

**Damian Kaminski:** Nie zawsze. OK.

**Janusz Bossak:** Trzeba według mnie rozwiązać, nie znaczy to, to tak jak mówicie, jest OK. Natomiast trzeba do tego wrócić, jakby systemowo, tak, żeby jeżeli chcemy tych rejestrów używać. To właśnie trzeba wyraźnie odróżnić usuwanie, które jest na normalnych sprawach od dezaktywowania, de facto, które jest na rejestrze. I nawet żeby nie trzeba było tego szukać w usuniętych, bo to sugeruje, że to sprawa jest usunięta. Ona nie jest usunięta, ona jest dezaktywowana i trzeba by wprowadzić coś, co jest rzeczywistym usunięciem.

**Damian Kaminski:** Ale co masz na myśli w sensie dezaktywowana, to znaczy, że co, że ona dalej występuje, tylko to tak, no właśnie.

**Janusz Bossak:** Oczywiście, że tak, no, no nie powinno być, ona w ogóle nie powinna tutaj się pojawiać. Takie było założenie, tworzenie rejestru wtedy dawno temu. Ona to nie jest zadanie tej sprawy w rozumieniu usuwania.

**Damian Kaminski:** Tylko. Ja rozumiem Janusz kontekst, taki logiczny biznesowy, tylko to zakładam, co mówisz w tym momencie, to jest szereg zmian, żeby do tego dojść, tak, czyli zamiana przycisk usuń na dezaktywuj i jakaś przestrzeń na wyświetlanie tego, więc powiedziałbym, że zróbmy na razie tyle, żeby to udrożnić, żeby nie było tego typu pytań, bo ja nieraz nie wiem, 5-6 razy miałem, no chcę zrobić klucz na rejestrze od, od wdrożeniowcu, tak i nie, nie mogę, bo jest unikalna, nie ma żadnej sprawy.

**Janusz Bossak:** Tak. Tak, tak, tak. No bo wdrożeniowcy nie wiedzą, tak, no, no zgadzam.

**Damian Kaminski:** No nie wiedzą, więc to trzeba. To, to jest łatwy temat do naprawy, no i pozostaje ten drugi temat, który tu właśnie zaproponował Kamil, czyli. Czy jeśli już mamy kontekst biznesowy, czyli powiedzmy, to nie jest ten start, tylko coś było, zostało usunięte, czyli dezaktywowane, jak, jakkolwiek to nazwiemy? I ktoś z tym wraca, tak i teraz, żeby nie było konfliktu i zatrzymania synchronizacji wskutek właśnie nieunikalności klucza. To czy wznawiamy? Są. Sprawę rejestru, która już była.

**Janusz Bossak:** Jeżeli ona powoduje nieunikalność klucza, to nie powinniśmy jej wznowić, tak.

**Damian Kaminski:** Nie, nie, inaczej. Chodzi o to, że tak? Mieliśmy, mamy jakiś rejestr kontrahentów, jest firma X. Teraz ktoś podejmuje decyzję, a ja to wywalam. No to wywalam, OK, jest to dezaktywacja i teraz następuje kolejna synchronizacja i ta firma X jeszcze raz powstaje. A ja wchodzę tutaj, stwierdzam, ale zaraz, ta firma i ja potem patrzę, że ta firma X miała w dodatku jakieś podpięcia stare, a teraz już jest nowy byt firmy X, jak wejdę na ten usunięte firmy X, będę chciał przywrócić, to spowoduje wtedy duplikat klucza, więc ja bym był za tym, żeby przywracać, a nie. Tworzyć nowe, a nie wykluczać sprawy usunięte z klucza. Według mnie to, co tu chłopaki zaproponowali, jest lepszym rozwiązaniem.

**Janusz Bossak:** Znaczy obawiam.

**Damian Kaminski:** Czyli jeśli ona jest w koszu, ale jest w źródle, to z powrotem trafia do. Do spraw normalnie zarejestrowanych po prostu.

**Janusz Bossak:** No OK, no jeżeli to jest dokładnie to samo.

**Damian Kaminski:** Tak, tak, no klucz jest jednoznaczny, nie?

**Janusz Bossak:** A czy to? No nie, bo klucz, no, no jeżeli klucz jest jednoznaczny, bo jeżeli klucz ktoś wpisał zero.

**Damian Kaminski:** Nie, no to, to już jest odrębny przypadek. No jeśli istnieją 2 sprawy, no to zerem, no to nie można ustawić klucza, no i tyle, to, to, to już rozwiąże nam ten komunikat, tak, że wy przy najpierw przygotujcie dobrze dane, czyli wyczyśćcie wszystkie sprawy istniejące. I tyle.

