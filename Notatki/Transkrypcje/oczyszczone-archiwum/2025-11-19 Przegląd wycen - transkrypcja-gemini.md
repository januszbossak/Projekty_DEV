**Data spotkania:** 19 listopada 2025

---

**Janusz Bossak:** Patrzę na ten projekt interfejsu dla certyfikatów. Czy wyświetlamy wszystkie, czy tylko aktywne?

**Kamil Dubaniowski:** Teraz tylko aktywne. W starej wersji był przełącznik, ale nie do końca rozumiem jego sens. Po co ktoś ma oglądać swoje nieaktywne certyfikaty?

**Janusz Bossak:** Może się zdziwić, że nie widzi certyfikatu, który jego zdaniem powinien tam być, a jest już na przykład nieaktywny.

**Kamil Dubaniowski:** W takiej sytuacji ma komunikat, że nie ma żadnych aktywnych certyfikatów. To nie jest miejsce do sprawdzania pełnej listy certyfikatów.

**Janusz Bossak:** Pytanie, czy obecne zachowanie nie jest nieintuicyjne? Skoro funkcjonalność już jest, nie widzę powodu, żeby ją zabierać. Może to zmniejszyć liczbę pytań do serwisu o 10%.

**Kamil Dubaniowski:** Dobra, to może wstrzymam tę zmianę. Przesunę ten przełącznik gdzieś niżej, bo teraz niepotrzebnie świecił na samej górze.

**Janusz Bossak:** Zrób to na dole, w stylu, w jakim jest "tryb deweloperski". Np. "Pokaż wszystkie dostępne certyfikaty".

**Kamil Dubaniowski:** Słusznie. Podjęliśmy też decyzję, żeby domyślnie pokazywać tylko certyfikaty służące do podpisu, bo np. Szafir Adriana pokazywał trzy, a tylko jeden z nich służył do składania podpisu.

**Janusz Bossak:** Tak. Dyskutujemy nad projektem, jak ma wyglądać SignApp w momencie dochodzenia do podpisu. Wyświetlamy certyfikaty, użytkownik wybiera jeden i klika "podpisz wybranym certyfikatem".

Tryb deweloperski w wersji produkcyjnej nie powinien być widoczny.

**Kamil Dubaniowski:** Włączyłem go tylko po to, żeby Adrian zobaczył, jak ma wyglądać interfejs w dwóch sytuacjach: kiedy nie ma certyfikatów i kiedy ma je pokazać.

**Janusz Bossak:** A propos raportów, ten komunikat "Nie znaleziono certyfikatu w systemie" jest bardzo ładny.

**Lukasz Bott:** Dodałbym "żadnego *aktywnego* certyfikatu".

**Janusz Bossak:** Ważne jest to drugie zdanie, które jest podpowiedzią, co zrobić: "Podłącz urządzenie z certyfikatem i kliknij przycisk Odśwież". To samo trzeba zrobić w module raportowym. Jest opis sytuacji i jest podpowiedź co robić. To wzorcowy przykład.

**Damian Kaminski:** Zgadzam się. Mam jeszcze jedną uwagę. Jeśli certyfikat ma krótką datę ważności, np. miesiąc, kojarzę, że wyświetlało się to na czerwono. To ważne, bo ktoś może nie zauważyć, że certyfikat mu wygasa. Może ten checkbox "pokaż wszystkie" byłby tu pomocny, bo użytkownik zobaczyłby, że jego certyfikat jest, ale nieaktywny.

**Janusz Bossak:** Ale czy my robimy teraz MVP, czy jakieś super-duper rozwiązanie?

**Damian Kaminski:** Dobra, nie upieram się, to może być rozwój.

**Janusz Bossak:** Niech to po prostu podpisuje na Macu, to jest nasze MVP. Jak pójdzie i będą uwagi ulepszające, będziemy je robić.

Wracamy do naszego tematu.

**Kamil Dubaniowski:** Przeglądałem wczoraj szkolenia z EZD, żeby podszkolić się w tematach JRWA. Wydaje mi się, że samo JRWA to kropla w morzu. Jest cały wątek archiwizacji, który, jeśli obsłużymy niewydajnie, będzie klapą. Podobnie temat składów chronologicznych i pudeł. To wszystko można by oprzeć na dedykowanym rozwiązaniu, bo inaczej sprowadzi się to do rzeźby na rejestrach i polach "odnośnik". Skoro zarzucają nam, że w JRWA odnośnik się nie sprawdził, to z kartonami i składami będzie to samo.

**Janusz Bossak:** Nie sądzę, żeby LOT miał więcej dokumentów w obiegu niż Rossmann w dokumentach pracowniczych. W Locie nie robimy e-teczki jako takiej, prawda?

**Damian Kaminski:** Nie dotyczy. W JRWA jest na to przestrzeń, ale akta kadrowe są obsługiwane przez odrębne rozporządzenie. Można uznać, że cały moduł e-teczki to ta kategoria z JRWA, ale jest obsługiwana odrębnie i ma inny sposób eksportu.

**Janusz Bossak:** Dobra, przejdźmy do wycen, bo JRWA będziemy mieli na osobnym spotkaniu.

**Damian Kaminski:** Nie ma wycen bez opiekuna, ale mam prośbę. Czy możemy rozbudować ten dashboard "Wyceny", skopiować go i usunąć filtr "aktywne", żebyśmy mogli przeszukiwać wszystko i dokładać własne filtry, np. po kliencie?

**Janusz Bossak:** Kto jest twórcą tego raportu?

**Kamil Dubaniowski:** Chyba ja.

**Janusz Bossak:** Nasunął mi się przypadek użycia. Czy osoba mogąca tworzyć raporty mogłaby do tego dashboardu dodać swój, widoczny tylko dla niej raport?

**Damian Kaminski:** Na razie bym w to nie szedł.

**Kamil Dubaniowski:** Dobrze, poprawię ten dashboard.

**Janusz Bossak:** Wracając do zleceń do rozliczenia. Widzę tu Orlen, który wisi od czerwca.

**Damian Kaminski:** Dostali na to ofertę, nie ma informacji zwrotnej, ale bardzo możliwe, że to wezmą.

**Janusz Bossak:** Tu wisi na mnie zlecenie "rejestrowanie pobierania PDF z raportu".

**Damian Kaminski:** To jest zamknięte w ramach głównej umowy, wszystko jest już dawno rozliczone. To trzeba zamknąć.

**Janusz Bossak:** OK, dodaję cię jako odpowiedzialnego, żebyś domknął temat.

**Kamil Dubaniowski:** Trzeba by przejrzeć te stare wyceny. Znalazłem wczoraj dwa parkingi od czerwca, które nie były przekazane do wyceny.

**Damian Kaminski:** Zgłoszenie dla Rossmanna o powiadomieniach i zamykaniu - nie daliśmy wyceny, bo we wrześniu zapytałem, czy klient tego dalej oczekuje i nie dostałem odpowiedzi. Przy projekcie dla LPP było dużo pomysłów, ale nie było na wszystko budżetu. Jak powiedzieliśmy, że coś jest do wyceny, to stwierdzili, że skończyły im się fundusze.

**Lukasz Bott:** Trzeba te wyceny anulować, jeśli nie ma pieniędzy.

**Damian Kaminski:** A ten temat dla Rossmanna jest ważny, ale stoi od marca.

**Lukasz Bott:** To jest w kategorii "ważne, ale nie pilne".

**Damian Kaminski:** Co do historii spraw powiązanych dla Rossmanna, mam się z nimi spotkać.

**Lukasz Bott:** Chodzi o to, żeby dowiedzieć się, jakie są ich oczekiwania biznesowe.

**Damian Kaminski:** Tak, bo narzucono nam wyświetlanie całej historii, ale może oni potrzebują z niej tylko jednej konkretnej informacji. Po co zaśmiecać ekran? Chcę ustalić, o jaką informację chodzi, i na tej podstawie zdecydujemy, czy idziemy w pomysł Kamila (wyświetlanie całej historii sprawy powiązanej), czy rozbudowujemy interfejs historii biznesowej, co Rossmann mógłby nam zasponsorować.

**Lukasz Bott:** Sugerowałbym iść w tym drugim kierunku, a nie wyświetlać historii technicznej.

**Damian Kaminski:** Też bym tak chciał. Zadeklarowałem się, że mogę pójść na to spotkanie.

**Kamil Dubaniowski:** Przerwę, ale mam temat błędu w raportach. Jak wejdę na sprawę, zrobię coś na niej i wrócę do raportu, ona dalej tam jest, chociaż według filtrów nie powinno jej być. Czy możemy to wrzucić na ten sprint? Moim zdaniem to krytyczne i irytujące. Wcześniej po powrocie raport odświeżał się automatycznie i sprawa znikała.

**Lukasz Bott:** To chyba dotyczy tylko dashboardu. Jakby ten raport był otwarty jako osobny, to pewnie by działało.

**Damian Kaminski:** Sprawdźmy. Mam przykład w raporcie, który nie jest na dashboardzie. Wchodzę w sprawę nr 666, zmieniam etap, klikam "wstecz" - nie ma jej. Klikam "odśwież" - działa. Zniknęło po odświeżeniu. A teraz to samo w pop-upie. Wchodzę w sprawę 667, zmieniam, zamykam pop-up - wisi. Klikam "odśwież" - znika. To jest minimum, które powinno działać.

**Lukasz Bott:** Rzekomo było to naprawione w zgłoszeniu, które podesłałem na czacie.

**Damian Kaminski:** W kryteriach akceptacji jest tylko: "Kliknięcie przycisku Odśwież w dashboardzie powoduje również odświeżenie zawartości raportu w aktywnej zakładce". To nie dotyczy automatycznego odświeżenia po zamknięciu pop-upu czy po powrocie strzałką.

**Janusz Bossak:** Trzeba zrobić zgłoszenia na kilka przypadków użycia. Pierwszy: jestem na raporcie, wchodzę w sprawę, robię coś (zapisuję lub wykonuję akcję), wracam. Jeśli rekord nadal spełnia kryteria raportu, powinienem wrócić w to samo miejsce na liście, a dane w tym rekordzie powinny być odświeżone. Drugi przypadek: robię coś, co powoduje, że rekord znika z raportu. Co ma się wtedy wydarzyć?

**Damian Kaminski:** Idziesz za daleko. Ja, jako praktykant, mam za zadanie uzupełnić puste nazwiska. Mam filtr "nazwisko jest puste". Wchodzę w sprawę, uzupełniam, zapisuję, zamykam. Spodziewam się, że ta sprawa zniknie z mojego widoku.

**Janusz Bossak:** Nie mieszajmy przypadków użycia. Najpierw przypadek bez filtrów. Wchodzę, zmieniam, wracam, chcę być w tym samym miejscu z odświeżonymi danymi. Kolejny przypadek to sytuacja z sortowaniem. Zmieniam wartość w kolumnie, po której jest sortowanie - co ma się stać? Według mnie rekord powinien się zaktualizować, ale pozostać na swoim miejscu do czasu, aż ręcznie kliknę "odśwież" i cały raport się przesortuje.

**Damian Kaminski:** To jest wyzwanie. Myślę, że na razie jedyne, co musimy zrobić, to naprawić przycisk "odśwież", który nie działa na dashboardzie. Resztę trzeba głębiej przemyśleć i opisać w osobnych przypadkach użycia, żeby nie wprowadzać niespójnych zachowań.

**Janusz Bossak:** Zgadzam się. To co mówiliśmy o Mateuszu - on ma opisać przypadek użycia. Tego samego dotyczy nasza dyskusja. Co ma się wydarzyć, jeśli użytkownik w konkretnej sytuacji coś zrobi. Ważne jest też, jak to odbierze użytkownik końcowy, który nie zna logiki w backendzie.

**Damian Kaminski:** Dokładnie.
