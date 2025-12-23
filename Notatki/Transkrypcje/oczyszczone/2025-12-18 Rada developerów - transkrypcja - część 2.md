**Janusz Bossak:** Dokładnie. System powinien wysyłać meila dopiero, gdy błąd odczytu licencji powtórzy się np. 3 razy w określonym czasie. Nie przy pierwszym "strzale", bo to robi niepotrzebne zamieszanie.

**Damian Kamiński:** Wszyscy administratorzy w LPP to dostali. Musimy to przemyśleć. Wiemy, co jest przyczyną – błąd odczytu informacji o licencjach w pewnych okolicznościach. System uznaje wtedy, że licencji brak i wysyła komunikat o osiągnięciu limitu spraw.

**Piotr Buczkowski:** Trzeba rozróżnić przypadek, gdy licencja została odczytana i limit faktycznie osiągnięto, od sytuacji, gdy licencji nie udało się odczytać.

**Janusz Bossak:** Prawdopodobnie trzeba to obsłużyć w `try-catchu` i np. zanotować błąd w cache'u. Kluczowe jest, aby nie uznawać braku odczytu za brak licencji. Błąd dostępu do bazy nie może skutkować blokadą zakładania spraw. Dopiero fizyczny brak klucza w miejscu, do którego mamy dostęp, powinien uruchamiać ograniczenia.

**Damian Kamiński:** Co z tym robimy?

**Janusz Bossak:** Trzeba to zaopiekować w ramach stabilizacji wersji. To denerwuje klientów i konsultantów, zabiera czas.

**Piotr Buczkowski:** Przypisz to do mnie, bo tak się to skończy. Nie zrobię tego teraz, ewentualnie w przerwie między świętami a Nowym Rokiem.

**Janusz Bossak:** To idealny przykład zadań do "stabilizacji systemu".

**Damian Kamiński:** Zgadzam się. Skoro wiemy, że to problem z dostępem do bazy, a nie brakiem licencji, musimy podjąć próbę naprawy. Pytanie tylko, czy przy braku odczytu licencji system blokuje zakładanie spraw, czy to tylko komunikat.

**Piotr Buczkowski:** Blokuje.

**Damian Kamiński:** Jeśli dotyczy to spraw z maila lub skanu, to pół biedy – one czekają na kolejną iterację, dane nie giną. Ale w instalacjach on-premise, gdzie licencja jest stała, nie powinno to tak drastycznie działać.

**Janusz Bossak:** Całą ścieżkę należy przerobić. Dopiero po kilkukrotnym upewnieniu się, że licencji brak, system powinien ograniczać funkcjonalność.

**Damian Kamiński:** Przypisuję do Piotra na sprint zaczynający się 29 grudnia. Kolejny temat: Ania zgłaszała błąd braku sprawdzania uprawnień przy tworzeniu sprawy z procesu.

**Piotr Buczkowski:** Jest funkcja sprawdzająca uprawnienia użytkownika. Zapomnieliśmy dodać jej wywołanie w tym konkretnym miejscu.

**Damian Kamiński:** OK. Kolejny temat – wyświetlanie sekcji na telefonie jako strony (z przewijaniem strzałkami i krótką walidacją). Zostawmy to na razie na mnie, przedstawię propozycję po świętach.

Dalej mamy aktualizację integracji. To temat dla Michała. I kwestia eksportu/importu danych z tabel. Omawialiśmy to ostatnio.

**Damian Kamiński:** Ustaliliśmy, że przy eksporcie kluczem jest co innego niż to, co wyświetlamy (np. pole Odnośnik). Eksportujemy wartości wyświetlane, co skutkuje niekompatybilnością przy imporcie – nie da się wczytać danych z powrotem, bo ID pozycji są inne niż ich nazwy.

**Janusz Bossak:** Tu jest szerszy problem. Po pierwsze, niektórzy nasi konsultanci i klienci nie rozumieją mechanizmu AMODIT. Wydawało im się, że import danych do tabeli tylko uzupełnia wiersze, a on kasuje dotychczasowe i tworzy nowe. Daniel stworzył na to jakiegoś hot-fixa, ale problemem jest brak zrozumienia podstaw. Klient chce mieć w AMODIT funkcjonalność Excela (copy-paste, rozciąganie wartości na 100 pozycji). Moja propozycja: powinniśmy eksportować CaseID wiersza, aby przy imporcie system nie tworzył nowych wierszy, tylko aktualizował istniejące.

**Damian Kamiński:** To byłby zupełnie nowy mechanizm – nie import, a aktualizacja tabeli. Pytanie, dlaczego klient chce to robić w Excelu, a nie bezpośrednio w AMODIT.

**Janusz Bossak:** Bo nasza tabela nie ma wszystkich funkcji Excela. Drugie niezrozumienie dotyczy pól "tylko do odczytu". Przy imporcie system nie powinien pozwalać na ich nadpisywanie, bo to złamanie zasad bezpieczeństwa. Daniel i serwis tego nie rozumieją i mają pretensje, że import nie działa na tych polach. Ręce opadają. Trzeba zbadać, dlaczego klienci chcą masowo edytować te dane na zewnątrz. Może brakuje nam funkcji typu "uzupełnij wszystkie wiersze w kolumnie określoną wartością".
