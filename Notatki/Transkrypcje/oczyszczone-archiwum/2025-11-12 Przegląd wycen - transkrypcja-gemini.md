**Data spotkania:** 12 listopada 2025

---

**Lukasz Bott:** Mam zgłoszenie dotyczące źródeł opartych na bazie Oracle. Mateusz dopytuje, czy źródła online w ogóle nie będą działały w nowych raportach. Przed chwilą przetestowałem i źródło online działa. Być może to specyfika bazy Oracle? Możemy mieć problem z przetestowaniem tego.

**Damian Kaminski:** Poruszałem to z Mateuszem. On wrzucił loga, ale nie ma tam zapytania SQL-owego.

**Lukasz Bott:** Sądząc po treści, to jest jakieś konkretne zapytanie do konkretnych tabel w konkretnej bazie. Byłbym zdziwiony, bo skoro mamy źródło online opierające się o sterownik ODBC do bazy Oracle, to komunikacja powinna być transparentna. Po to jest sterownik ODBC, żeby on tłumaczył komunikację z danym silnikiem.

**Damian Kaminski:** Ja to inaczej rozumiem. Sterownik ODBC odpowiada za połączenie, ale nie za tłumaczenie składni. Musimy zadać pytanie w języku Oracle'owym. To, co wzbudza podejrzenia, to oświadczenie Mateusza, że stare raporty działają.

**Lukasz Bott:** No właśnie, o to chodzi.

**Damian Kaminski:** Tu jest coś innego, na końcu jest `LIMIT ?`. Może tu czegoś brakuje?

**Lukasz Bott:** To `INVALID_CHARACTER`. Może przekazujemy jakiś parametr, którego nie powinniśmy, albo brakuje wartości jakiegoś parametru. Sterownik przekazuje znak zapytania do silnika Oracle'a, a ten go nie rozumie.

**Damian Kaminski:** Ktoś z deweloperów musi na to spojrzeć. Można zasugerować, żeby włączyć logowanie zapytań SQL i porównać zapytanie, jakie leci ze starego raportu, a jakie z nowego. Może to jest tylko ten `LIMIT`, który powinien być jakimś parametrem liczbowym.

**Lukasz Bott:** Możliwe, `LIMIT ?` to składnia MySQL-owa. Powinna tam pójść konkretna liczba.

**Damian Kaminski:** Nie mamy wszystkich przypadków biznesowych po stronie testów. Ten Oracle był dowożony przez ostatnie lata, poprawiane były drobnostki, żeby był kompatybilny dla prostych zapytań.

**Lukasz Bott:** Trzeba by skontaktować się z Mateuszem, żeby jakoś tę sesję z naszymi ludźmi od Rossmanna sprawdzić. Nie sądzę, że to problem z Oracle jako takim, tylko my niepoprawnie budujemy zapytanie.

Kolejny temat - permanentne przechowywanie wartości w lupce do wyszukiwania procesów. To jest zgłoszenie z Neuca. Chodzi o to, że jak przefiltrujemy listę procesów czy raportów, to ten filtr zostaje na stałe, nawet po wylogowaniu. Propozycje są takie, żeby czyścił się po wylogowaniu.

**Damian Kaminski:** W Neuca jest logowanie przez AD, więc nie ma typowego wylogowania.

**Lukasz Bott:** Jak zamkniesz przeglądarkę.

**Damian Kaminski:** Całą przeglądarkę, nie zakładkę. To ma sens. Mamy parametr związany z czasem trwania sesji, więc można to trzymać do końca sesji.

**Janusz Bossak:** Trzeba to rozpisać: które momenty czyszczą filtr. Na pewno wylogowanie i zalogowanie.

**Damian Kaminski:** I zamknięcie całego okna przeglądarki.

**Janusz Bossak:** Trzeba to rozpisać i powiedzieć, jak będzie. Czy to jest hotfix?

**Lukasz Bott:** Nie jest to hotfix.

**Janusz Bossak:** To nie jest hotfix. Nie wywala danych, nie ma błędów, powoduje tylko niewygodę. Może być w następnym wydaniu. Można by się zastanowić szerzej i zrobić z tego paczkę wartości, np. "poprawa zachowania systemu przy wybranych filtrach i wyszukiwaniach", która dotyczyłaby raportów, procesów itd.

**Lukasz Bott:** Dobra. Kamil, zostawiamy to u ciebie do ogarnięcia?

**Kamil Dubaniowski:** Tak. Jak znacie inne tematy w tym zakresie, to przypinajcie na mnie.

**Lukasz Bott:** Kolejny temat: wyświetlanie linku w mailu o dostępie tymczasowym. Bartek zgłosił, że zrobił trik z dodaniem `div`-a w `before` i `after`, i wtedy link formatuje się dobrze i jest widoczny we wszystkich klientach poczty. Piotr sugerował, żeby to dodać na stałe.

**Damian Kaminski:** Dobra, jeśli Piotr to widział i zatwierdził, to nie mam uwag. Przepiszę to, jak ma być zrobione. Pozostaje pytanie, na ilu skrzynkach to testować?

**Lukasz Bott:** Gmail, Outlook stacjonarny, i z polskich serwisów Wirtualna Polska i Onet.

**Damian Kaminski:** Dobrze, zostawiam to u siebie.

**Lukasz Bott:** I jeszcze jedno: funkcja `setFieldInfo` a pola wymagane. W wersji czerwcowej, jeśli pole jest wymagane, komunikat z `setFieldInfo` się nie wyświetla. W wersji marcowej działało to poprawnie.

**Damian Kaminski:** To pewnie Kamil, Mariusz albo Ania, kto opiekował się ukrywaniem "pole jest wymagane". Za mocno to ukryli.

**Kamil Dubaniowski:** Albo Mariusz, albo Ania.

**Lukasz Bott:** Kamil, przypiszę to do ciebie. Zmień ewentualnie klasyfikację, bo nie wiem, czy to hotfix. Nie ma utraty danych.

**Damian Kaminski:** Mamy coś jeszcze?

**Lukasz Bott:** To wszystko, dzięki.

**Kamil Dubaniowski:** Przejdźmy przez zaległości. Zgłoszenie od Daniela, że wyszukiwarka w backlogu otwiera się na fullscreenie, a lista przewija do góry. To jest do poprawy. Dalej, Mateusz ma błędy w komunikatorze do poprawy, żeby dowieźć go do końca. Np. wysłana wiadomość nie pojawia się od razu. To musi zrobić w tym sprincie. Co do `setRadioValue` - jest problem z wyczyszczeniem wartości w radio buttonach w regule automatycznej. Zawsze tak było.

**Lukasz Bott:** Zgadza się. W zwykłej liście wyboru da się wyczyścić, w radio buttonach nie. Obejściem było dodanie "pustej" opcji typu "--".

**Kamil Dubaniowski:** Niespójność. Zostawiamy to do zrobienia.

Co do błędów przy tworzeniu dashboardu - to wina starej wersji czerwcowej.

Na koniec, kwestia właściciela na poziomie feature'a i epica. Zazwyczaj ja byłem właścicielem, bo deweloperzy nie zaglądali na ten poziom, a statusy zostawały. Jak wszystkie PBI-e były zrealizowane, zamykałem feature. Czy tak robimy dalej?

**Janusz Bossak:** Przy nowej nomenklaturze to deweloper powinien domykać feature. Jego zadaniem na sprint jest "zrób ten feature", a w ramach tego są 3 PBI. On je robi i mówi "dowoiozłem feature w całości". Wy, jako delivery managerowie, powinniście decydować na poziomie paczki (prezentu), czyli zbioru feature'ów. Problemem jest to, że pojedyncze PBI-e idą do wersji, a nie całe paczki. Powinniśmy pracować na branchach per paczka. Jak robimy jakąś funkcjonalność, to otwieramy branch na tę paczkę. Wszystkie PBI do tego wchodzą na ten branch. Dopiero jak paczka jest gotowa, cały branch jest mergowany. To by uprościło pracę.

**Damian Kaminski:** Poniekąd tak robimy, bo są lokalne branche, na których możemy testować, a wydajemy w całości, gdy jest gotowe.

**Janusz Bossak:** Zgadza się, branż lokalny jest taką paczką wartości. Chodzi o to, żeby był nakierowany na jedną rzecz. A jakie było pytanie Kamil, bo odbiegliśmy?

**Kamil Dubaniowski:** Kto ma być właścicielem na poziomie feature'a i epica?

**Damian Kaminski:** Według mnie my, jako opiekun biznesowy.

**Janusz Bossak:** Teraz tak, ale docelowo powinien deweloper.

**Damian Kaminski:** OK.
