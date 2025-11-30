**Data spotkania:** 23 października 2025, 08:02 - część 6

---

**Piotr Buczkowski:** Tak, tak.

**Damian Kaminski:** OK, no dobra, dobra. To – to dużo puszczał, bo wtedy można skopiować, wkleić do Explorera i – Eksploratora – i w zasadzie jesteśmy w miejscu.

**Piotr Buczkowski:** Się zastanawiać, czy – czy tutaj w ogóle obsługiwać przechowywanie plików w bazie danych, tak? Czy nie, czy nie – że muszą być na – no, to jest albo na Blob.

**Damian Kaminski:** No, ma to sens. W sensie, no – nie wiem, chociaż z kolei powiem ci, że słyszę – wiem, że teraz, że w Alfresco – to oni wszystko trzymają w bazie danych w najnowszej wersji, tylko jest oddzielna baza danych, no ale to...

**Piotr Buczkowski:** A później jest takie coś, że – co zrobić – jakimiś – i jak mi baza też?

**Damian Kaminski:** Chyba – baza waży 100 gigant, daj...

**Piotr Buczkowski:** A, 300 giga – tak, była taka przypadek.

**Damian Kaminski:** No, no, nie wiem, czemu oni tak podeszli. Byłem też zdziwiony, ale gościu, z którym rozmawiałem, bo tam mamy projekt – to powiedział, że wszystko w bazie w nowych wersjach.

**Piotr Buczkowski:** No już, bądźmy tak – chociażby jest też...

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Bo to jest łatwiej, tak? Jest łatwiej zaprogramować, różnie to archiwizować, tak?

**Damian Kaminski:** No tak, a to spada na kliencie.

**Piotr Buczkowski:** O, tak.

**Damian Kaminski:** No nie wiem, ja – ja się skłaniam ku temu, co...

**Piotr Buczkowski:** Właśnie my – w środowiskach chmurowych mamy jeszcze tego Blob, na przykład, tak.

**Damian Kaminski:** Mhm, mhm.

**Piotr Buczkowski:** Mamy Google – no, ale to też jakieś Ania robiła jego, pamiętam.

**Anna Skupinska:** Tak, to było dosyć dawno temu.

**Damian Kaminski:** Znaczy, powiem tak – nikt z naszych klientów nie protestuje, a wszędzie, gdzie mówimy o dużych klientach, to zalecamy, żeby te pliki były poza bazą, więc wydaje mi się, że możemy tutaj tak samo podejść.

**Piotr Buczkowski:** No tak, to – dziękuję.

**Damian Kaminski:** No dobra, to – to chyba na tym skończymy, bo jesteśmy po czasie. To znaczy ja mam jeszcze krótkie, bardzo pytanie, bo tu mnie serwis dopytuję – już pewnie do Piotra też, ale – zainstalowali, ja próbuję odpalić i w zasadzie dostają "Said can't build" – uprawnienia puli aplikacji są nadane do folderu, gdzie znajduje się AMODIT.

**Piotr Buczkowski:** To...

**Damian Kaminski:** Co sugerujesz? Co szukać?

**Piotr Buczkowski:** Która to firma?

**Damian Kaminski:** Tomasz Kalinowski – nawet która to firma – może, może gdzieś wrzucał na też, na serwis.

**Piotr Buczkowski:** Tak, to wczoraj chyba żeśmy rozmawiali – SMS – tak, sens.

**Damian Kaminski:** Mhm, tak.

**Piotr Buczkowski:** Do dziś mnie tam – telki to skopali.

**Damian Kaminski:** Ale w sensie przy instalacji?

**Piotr Buczkowski:** Nie wiem. Nie – to jest konkretnie, nie – rozumiesz – chodzi to – powiem tak.

**Damian Kaminski:** Mhm. No dobra, nie, nie, nie, nie – wskazę, żeby sprawdzić to, to i to.

**Piotr Buczkowski:** Znaczy – ty – czy – TLS the space – to próbuje się – Adapter – TLS do Alfresco dostać, a nieskonfigurowany – TLS – lokalność.

**Damian Kaminski:** A.

**Piotr Buczkowski:** A przeglądarka – do – organizmu – szachty TLS – czyli pewnie przeglądarka – być może trzeba coś w przeglądarce zrobić, żeby Adapter to powiedział.

**Damian Kaminski:** OK, no dobra, no to już jest...

**Piotr Buczkowski:** No tak – sorry – no, nowsze przeglądarki dodają jakieś tam ograniczenia, tak – nowsze Windowsy dodają jakieś ograniczenia.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Typu, że – localhost – na Windows 10 – milionów – takie coś, na przykład – nie, nie – ja takie, takie zarejestrowałem sobie swoją domenę.

**Damian Kaminski:** Nie zrobisz HTTP.

**Piotr Buczkowski:** Info, tak – bo albo jest – no, wiadomo testowe – a potrzebowałem jakiejś domeny, żeby móc rejestrować, stosować mechanizm, na przykład, że mamy bazę...

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Której adres – jest – bazę wybiera na podstawie – drastycznie, na przykład – "astrafox.mod.com", tak – że ta testowa u siebie. I chyba na Windows 10 nie było tak, że domyślnie nie mogła użyć AMODIT – powiedzmy – "astrafox.amod.info", żebym przekierował na localhost, ale mogłem to wyłączyć, tak – znaczy wyłączyć sprawdzanie – te loopback. 11 – wygląda, że nie mogę tego wyłączyć, tak? Jest to duży problem, bo jeżeli chciałbym coś modyfikować w tym mechanizmie wyboru bazy na podstawie adresu.

**Damian Kaminski:** Windows 11 – ja jeszcze nie przeszedłem, ale wczoraj miałem przypadek, gdzie – nie można odpalić Outlooka na Windows 11.

**Piotr Buczkowski:** Tam – tamto, to tamto – trzeba po prostu zdiagnozować, tak – więcej uwagi niż Tomek Kalinowski. Co się dzieje?

**Damian Kaminski:** Mhm, mhm.

**Piotr Buczkowski:** Starannie. Potrzeba – w trakcie – trzeba patrzeć, co się dzieje i analizować, tak.

**Damian Kaminski:** No dobra, ale z tym HTTPS – to jest może słuszne spostrzeżenie – na to nie zwróciłem uwagi wczoraj, bo też tam poświęciłem chwilę tylko, jak miałem...

**Piotr Buczkowski:** No właśnie, przez to – przed – dlatego mówię, że – całą – mieć więcej uwagi – i co się stało, co, co tak naprawdę jest – co jest zwracany – lepiej, adresu – jest błąd, tak. A nie to, że jest błąd i pytanie.

**Damian Kaminski:** No, to na razie to i nie działa.

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** I – i powiedzcie – magicznie to nie działa. Dobra, spróbuję – może się z nim jeszcze w ciągu dnia złapać i coś tam go wesprzeć. To tyle, bo już i tak jesteśmy mocno po czasie. No, dzięki za to – za tą konsultację w sprawie tego repozytorium. Dopiszę to też do wymagań. No, to chyba wszystko na ten moment. Na razie.

**Anna Skupinska:** No, cześć.

