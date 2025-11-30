**Data spotkania:** 18 listopada 2025

---

**Lukasz Bott:** Mam jedno zagadnienie na radę. W Dentsu, którzy mają około 500 kont w AMODIT synchronizowanych z Active Directory, jest zapotrzebowanie na hurtowe blokowanie użytkowników. Mają około 300 pracowników, którzy korzystają z systemu sporadycznie, np. raz na rok, żeby zaakceptować fakturę. Administrator chciałby ich blokować, żeby nie zużywali licencji, a potem w razie potrzeby odblokowywać.

**Janusz Bossak:** Jaki jest w tym nasz interes? Nasz interes to sprzedawać licencje.

**Damian Kaminski:** Czyli on chce zablokować jednych, żeby dać licencje innym i tak przełączać?

**Janusz Bossak:** To niezgodne z intencją.

**Damian Kaminski:** Dla nas to nie jest interes, bo doprowadza do tego, że nie kupują licencji. Zresztą, jakby był kumaty, to sam by to zrobił, bo jest widoczna data ostatniego logowania.

**Janusz Bossak:** Nie wspierajmy takich rzeczy. To nie w naszym interesie. Zgodnie z umową, każdy, kto używa AMODIT, musi mieć licencję. Kwestie biznesowe są nadrzędne wobec technicznych. Moglibyśmy pójść w model licencji jednoczesnych (concurrent), ale wtedy są one wielokrotnie droższe.

**Damian Kaminski:** Powinniśmy przekazać, że nie wspieramy takich działań. Pozwalamy na przenoszenie licencji, gdy ktoś kończy pracę, ale nie na dynamiczne przełączanie kont aktywnych pracowników. Jak klient chce się w to bawić, niech robi to na własną rękę.

**Piotr Buczkowski:** Był kiedyś plan na licencje na jeden proces. Na przykład 100 osób pracuje w AMODIT na co dzień, a 1000 tylko przy wnioskach urlopowych.

**Damian Kaminski:** Biznesowo to mamy, dokładając do umowy odpowiednie zapisy, ale nie jest to rozwiązane systemowo. Sprzedajemy licencje po niższej stawce przy dużej skali, jak dla Orlenu, ale jest to obwarowane zapisem, że użytkownicy korzystają tylko z określonego modułu, np. e-teczki.

**Lukasz Bott:** OK, czyli przedstawię im nasze stanowisko. I tak mają licencje kupione lata temu na bardzo preferencyjnych warunkach.

**Janusz Bossak:** Więc niech nie marudzą. Dobra, co dalej na radzie?

**Damian Kaminski:** Mam zgłoszenie od Mateusza. W raporcie bez pilnowania uprawnień, filtr nie podpowiada wartości ze spraw, do których użytkownik nie ma uprawnień.

**Piotr Buczkowski:** Jak są generowane te podpowiedzi? Mam nadzieję, że nie robicie `SELECT DISTINCT` na `CaseDefinition`.

**Anna Skupinska:** Robimy nowe zapytanie do raportu, bierzemy tylko jedno pole i dodajemy ewentualny filtr, jeśli ktoś coś wpisuje.

**Piotr Buczkowski:** Dlaczego nie myślicie o wydajności? Robicie `LIKE` z procentami po obu stronach na kolumnie, która nie ma prawa być indeksowana.

**Janusz Bossak:** Piotr, to jak to powinno być zrobione?

**Piotr Buczkowski:** Powinien być zrobiony słownik. Dla danego pola powinien być zbudowany słownik dostępnych wartości i na nim powinny działać podpowiedzi, a nie na `CaseDefinition`.

**Damian Kaminski:** Czyli ten słownik powinien się tworzyć natywnie w kontekście raportu?

**Piotr Buczkowski:** Nie chodzi o słownik jako encję. Trzeba oznaczyć pole, że ma być wyszukiwalne, i przygotować strukturę danych, która to ułatwi. Kiedyś proponowałem jakieś rozwiązanie oparte na JSON, ale nikt tego nie podjął.

**Anna Skupinska:** Ale można zrobić raport oparty o pola indeksowane.

**Piotr Buczkowski:** Trzeba ten mechanizm indeksowania zrobić dobrze. Mój pomysł polegał na tym, żeby w definicji procesu można było zaznaczyć, które pola mają być indeksowane. Obecnie nie da się tego edytować, bo nie było czasu tego dokończyć. Raport nie powinien pozwalać wyszukiwać po polach, które nie są indeksowane.

**Damian Kaminski:** Czyli najpierw trzeba włączyć indeksowanie dla wybranych pól w procesie, a dopiero potem można ich używać w filtrach raportów?

**Piotr Buczkowski:** Tak, wtedy można zbudować odpowiedni indeks na tej kolumnie w JSON-ie i po nim szukać. Oczywiście nie "procent coś procent", tylko od początku wyrazu, tak jak to działa w polu "Odnośnik". Można do tego użyć Lucene.

**Damian Kaminski:** Ale czy nie moglibyśmy pozwolić na wyszukiwanie w środku frazy, jeśli ktoś świadomie tego chce? Czasami szuka się po końcówce numeru.

**Janusz Bossak:** Chciałbym wrócić do tego indeksowania. Piotr, gdzie te dane się zapisują i jak wygląda ich aktualizacja?

**Piotr Buczkowski:** W tabeli `Case`. Powinno się to aktualizować przy zapisie sprawy. Niestety, mechanizm nie został dokończony. To był tylko pomysł, jak podejść do usprawnienia wydajności.

**Janusz Bossak:** Ale to jest mechanizm czysto techniczny. Z punktu widzenia użytkownika, który tworzy raport, on powinien w ustawieniach filtra, np. dla pola "Nazwisko", mieć opcję "za indeksuj".

**Damian Kaminski:** To bardziej naturalne. Nie musi wchodzić w definicję procesu.

**Janusz Bossak:** Ta akcja indeksowania może chwilę potrwać. Ale jak raz to zrobi, to w każdym innym raporcie korzystającym z tego samego pola z tego samego procesu, te dane już będą zaindeksowane.

**Damian Kaminski:** Trzeba by też pomyśleć o ograniczeniu liczby indeksowanych kolumn na proces, żeby nie przesadzić. Ale 10 to już bardzo dużo, realnie potrzeba kilku: numer faktury, kontrahent, NIP, PESEL.

**Piotr Buczkowski:** Dla pól słownikowych nie ma tego problemu, bo to oddzielne obiekty, w których można szybko szukać.

**Damian Kaminski:** Aniu, w przypadku filtrów na polach słownikowych, lista podpowiedzi też jest budowana z wyników raportu, a nie ze słownika?

**Anna Skupinska:** Tak, chyba wszystkie są traktowane tak samo.

**Damian Kaminski:** No to tu jest ten sam problem. Na liście mam A, B, C, D, E, a wyświetla się tylko A, bo tylko ta wartość występuje w pierwszych 20 wierszach zwróconych przez raport.

**Janusz Bossak:** W przypadku małych słowników, jak "kategoria A, B, C", powinno wyświetlać wszystkie opcje. Ale jak słownikiem są klienci i jest ich 10 000, a w raporcie tylko 10, to nie ma sensu ładować wszystkich.

**Damian Kaminski:** Dokładnie. No dobrze, czyli mamy tu problem do rozwiązania. Najpierw trzeba poprawić pobieranie listy wartości dla filtrów, żeby używało `DISTINCT` i nie było ograniczone do 20 pierwszych rekordów z wyniku. To jest do zrobienia na teraz. A długofalowo trzeba zaimplementować ten mechanizm indeksowania, który zaproponował Piotr.

**Janusz Bossak:** Dobrze, że o tym rozmawiamy. Lepsze projektowanie na początku oszczędza nam masę pracy później. To, co teraz analizujemy dla filtrów, muszę dopracować w przypadkach użycia i dać wam do zweryfikowania.

**Damian Kaminski:** Dobrze. Ja muszę się przełączyć na spotkanie z Mateuszem w sprawie WIM. Na dzisiaj kończymy.

**Janusz Bossak:** Dzięki, to było bardzo konstruktywne spotkanie.
