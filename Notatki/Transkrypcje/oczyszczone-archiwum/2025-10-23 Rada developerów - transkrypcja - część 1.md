**Data spotkania:** 23 października 2025, 08:02

---

**Damian Kaminski:** Cześć. No dobra, chyba jesteśmy w komplecie akurat dzisiaj, bo Kamil ma jakąś naradę, Słotem mają jakieś kwestie chyba prywatne. Piotrze, jeszcze tak przy okazji, wrzuciłem ci coś, co Przemek zasugerował, że raczej to po twojej stronie. Kryteria akceptacji w zasadzie jest prosty warunek – zakładka "Do wykonania" w ogóle ma się nie wyświetlać we wszystkich procesach, niezależnie od niczego. Ona ma być na górze? Wrzuciłem ci na czacie, to sobie przeczytaj najwyżej. Będziemy – no to znaczy, dobra, to szybko, bo to szybki temat już wyświetla. My zaraz przyjdziemy do Ani. Gdzie jest informacja, że znika "Do wykonania" w zakładce wszystkie procesy i konkluzja jest taka, że w zakładce "Wszystkie procesy" w ogóle ma nie być "Do wykonania" nigdy, w sensie niezależnie od konfiguracji obszarów, bo tu jest to "Do wykonania" ze wszystkich procesów.

**Piotr Buczkowski:** No.

**Damian Kaminski:** Bo myśleliśmy, że to jest na Przemko, a on stwierdził, że ty już, że to tak przychodzi z backendu i że to raczej jest twój temat, więc przypisałem to do ciebie.

**Piotr Buczkowski:** OK.

**Damian Kaminski:** Dobra Aniu, to oddaję ci głos. Co wiemy i co proponujesz w kontekście?

**Anna Skupinska:** Tak, dlatego że ja się przyglądałam tym plikom i musiałam poprawić. Też pamiętasz Piotrze, ten błąd był, że nieważne co ustawiłeś, to się zawsze zwracało w tym samym formacie XSLT.

**Piotr Buczkowski:** Znaczy to rozszerzenie, tak? Dziękuję.

**Anna Skupinska:** Tak, więc okazuje się, że nieważne jakie się rozszerzenie wybierze, to jakby ten szablon zwróci taką samą zawartość pliku, więc można bardzo prosto zrobić taką sytuację, że wpiszesz jakąś...

**Piotr Buczkowski:** Co? Nie, stop, stop. Co znaczy "nieważne jakie rozszerzenie, taką samą zawartość"? Chciałbym – zwraca zawartość taką, jaka jest zaprogramowana.

**Damian Kaminski:** Mówimy o tym przypadku, gdzie tutaj wybieramy sobie jakiś proces, tak?

**Anna Skupinska:** No tak. I włączyłam proces, który Piotr zrobił. On się nazywa "Pusty", część "Blank" chyba.

**Damian Kaminski:** A, to ja.

**Anna Skupinska:** Empty – o, "Empty", tak. Jak wpiszesz "Proces Empty" to ci się pokaże.

**Damian Kaminski:** Poczekaj, poczekaj, poczekaj – gdzie, na develop?

**Anna Skupinska:** Nie, nie, to tak, to develop, a – przepraszam, tak.

**Damian Kaminski:** Bo to ja zacząłem, przepraszam was. Sekundę.

**Anna Skupinska:** Ale właśnie też...

**Damian Kaminski:** Sekundkę, już muszę się przepiąć. No, moment.

**Piotr Buczkowski:** Czy to nie musi zwracać XML? Stąd na przykład tam DOCTA, tak?

**Damian Kaminski:** Mhm. No, celem naszym jest – to znaczy tak – żebyśmy znali kontekst biznesowy, bo to jest bardzo ważne, w sensie żebyśmy wiedzieli, po co my to w ogóle robimy. Ja nie wiem – i to co tu powiedział Piotr – na pewno używamy tego w kontekście XSLT do integracji z Comarch. Nie znam żadnych innych użyć. Nie wykluczam, że one są.

**Piotr Buczkowski:** Co jest słabe, co jest słabo?

**Damian Kaminski:** Mhm, no właśnie. To tu pewnie masz większą wiedzę, Aniu, tak?

**Anna Skupinska:** Tak.

**Damian Kaminski:** No dobrze.

**Anna Skupinska:** Tutaj można w ustawienia eksportu i...

**Damian Kaminski:** I teraz... pamiętam gdzie to było, dawno tego nie robiłem.

**Anna Skupinska:** Tutaj, jeżeli...

**Piotr Buczkowski:** To ustawienia eksportu, ustawienia eksportu.

**Damian Kaminski:** A tu dobra, mhm, tak. I tu się wybiera szablon, tak?

**Piotr Buczkowski:** Wybierasz szablon, tak.

**Anna Skupinska:** Tak, i tutaj poniżej można wybrać rozszerzenie pliku – znaczy, uruchamia się rozszerzenie pliku – i wygląda na to, że nieważne jakie rozszerzenie wybierze, to jakby zawartość tego pliku jest taka sama, tylko się zmienia jego rozszerzenie. Więc taka jest moja uwaga, że ponieważ można...

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** No nie, no zawartość pliku – to zależy od tego, co jest szablonem XSLT, czyli jeżeli XSLT generuje Excel, to... Powiedział... chcemy, jeżeli... XSLT generuje CSV czy text, to będzie TXT.

**Damian Kaminski:** No tak, ale to z tego co mówisz, to to pole nie ma znaczenia, tak?

**Piotr Buczkowski:** To jest tylko jak nazwać plik pobierany i tutaj jest błąd. Tak jak napisałem – w starej wersji jest błąd po prostu.

**Damian Kaminski:** Aha.

**Anna Skupinska:** A, czy – tak, ja sobie lokalnie go naprawiłam, bo znaczy błąd – po prostu ktoś przy poprawce coś popsuł, a to nie jest duża rzecz. A czy ja mogę to poprawić w starej wersji nawet?

**Piotr Buczkowski:** No to jeżeli to jest prosta poprawka, po prostu trzeba wgrać, tak?

**Anna Skupinska:** Tak. To, że właśnie ja się pytałam, bo skoro jakby rozszerzenie pliku jest przydzielone do jakby do szablonu, znaczy w takim sensie, że szablon po prostu nie jest... Aha.

**Piotr Buczkowski:** Nie jest, nie jest. To znaczy, poczekaj – szablon wgrywasz jako szablon XSLT. Po co ją, jakiekolwiek generuje, to po pierwsze jest to, co jest w tym szablonie, a po drugie tutaj ustawiasz jakie byś chciała rozszerzenie pliku mieć wynikowo, że...

**Damian Kaminski:** Czyli inaczej, Piotrze, bym to chyba nazwał – jaką treść generuje, to jest w szablonie, a tu musisz ustawić takie rozszerzenie, żeby ta treść potem była odczytywana, tak? O to chodzi. Mhm, że XSLT nie jest, nie jest...

**Piotr Buczkowski:** No tak, tak, no tak – czy że spodziewasz, spodziewasz się pliku CSV, a nie XML, tak?

**Anna Skupinska:** Wydaje mi się, że to powinno być...

**Damian Kaminski:** Mhm, OK.

**Anna Skupinska:** Tak, bo wydaje mi się, że zapomina się wpisywane, kiedy się wczytuje szablon, w tym miejscu.

**Piotr Buczkowski:** Nie, znaczy...

**Damian Kaminski:** A czy można by było zrobić takie usprawnienie, że szablon jest analizowany i od razu jest podawane jakie będzie rozszerzenie? Tak czy nie?

**Piotr Buczkowski:** Może i tak, tak. Nie, nie, nie, nie, nie, nie, nie – tego nie róbmy, broń boże. Tak, można by to było przy szablonie zapisać, że ten szablon generuje XML, CSV – zostało to zrobione w ten sposób. Czy przerabiamy? Nie wiem.

**Damian Kaminski:** Dobra, dobra, aha, to znaczy...

**Piotr Buczkowski:** Ale tak jak – jak najbardziej można by było to przypisać do szablonu w definicji szablonów w procesie.

**Anna Skupinska:** Tak, mogłabym – to jest coś takiego, że jak się daje szablon, to można jeszcze dać proponowane rozszerzenie pliku, na przykład, i wtedy ona sobie pobiera ten szablon, bo dana szablonie i...

**Damian Kaminski:** No właśnie.

**Piotr Buczkowski:** No to może nie, może nie tyle proponowane rozszerzenie pliku?

**Damian Kaminski:** Dobra, inaczej – wydaje mi się, że rozumiem o co wam chodzi, ale to sobie ustalmy. Czyli z tego co rozumiem i co mówi Piotr, to na poziomie – czekajcie, tylko przejdę na ten ekran.

**Anna Skupinska:** Czy to myślę – może?

**Damian Kaminski:** Na poziomie tutaj szablonów należałoby dołożyć kolumnę, jakie jest rozszerzenie plików oczekiwane, i wtedy na tej podstawie...

**Piotr Buczkowski:** To tak, ja tak. I żeby to, tam co tam wybierasz, było wybierane tutaj.

**Damian Kaminski:** Mhm. Domyślnie z możliwością zmiany, czy nie?

**Piotr Buczkowski:** No ale to – nie, nie ma sensu.

**Damian Kaminski:** Czyli tylko wyświetlane do odczytu.

**Piotr Buczkowski:** Jeżeli, jeżeli, jeżeli szablon – jeżeli szablon generuje Excel, to generuje Excel. Jeżeli szablon generuje CSV, to zawsze generuje CSV.

**Damian Kaminski:** OK. Czyli to jest w zasadzie tutaj albo nawet zbędne do wyświetlania, cały wiersz, tak?

**Piotr Buczkowski:** Tutaj zbędne to, co byłoby – przenieść tam.

**Anna Skupinska:** Dobrze, musimy – musimy być kompatybilni wstecz, wstecznie, a większość teraz – żaden szablon. Wiem, że nie ma przydzielonego rozszerzenia.

**Damian Kaminski:** No.

**Piotr Buczkowski:** Tylko że...

**Anna Skupinska:** A więc...

**Piotr Buczkowski:** Tu...

**Damian Kaminski:** To musiałby mieć przydzielone – to jest drobna poprawka serwisowa. Komuś przestanie działać, bo wyskoczy jakiś – to należy, trzeba obsłużyć.

**Anna Skupinska:** A OK, czy – jeżeli jest przydzielony, to wtedy można wybrać?

**Piotr Buczkowski:** No nie, no nie, bo my to robimy na nowo, tak?

**Damian Kaminski:** Tak, będziemy to robić na nowo, więc...

**Anna Skupinska:** Tak, w React.

**Piotr Buczkowski:** Na starym nie – to na starym nie, to nie, to – to zostanie tak jak jest, czyli to co jest tutaj, jest podpisywane ewentualnie. No, no, niech pobiera z ustawień, z ustawień tego...

**Damian Kaminski:** Szablon.

**Piotr Buczkowski:** Zostawisz, o, blogu?

**Anna Skupinska:** A, to zrobię tak, że jeżeli w ustawieniach szablonu nie ma tej informacji, to że ciągle dawał, pozwalał na wybieranie.

**Damian Kaminski:** Znaczy nie, nie, stop – to tu za dużo to było powiedziane według mnie.

**Piotr Buczkowski:** Nie, w nowym interfejsie nie dodajesz wybierania typu.

**Damian Kaminski:** Znaczy, słuchajcie, ja bym to widział tak?

**Piotr Buczkowski:** O, ty – bo spodziewasz się, że typ będzie tutaj.

**Damian Kaminski:** Jeszcze bym, Aniu, powiedział, że na razie nic nie robimy, bo to jest niezgodne z tym nowym podejściem. Na razie stwórzmy do tego projekt, czyli co my chcemy i jak ma to działać, i tu bym potrzebował właśnie twojego wsparcia w kontekście analizy – jak to działa i co działa – i jak to będzie działać w nowym, żeby to po prostu...

**Anna Skupinska:** Ja się dopiero wczoraj dowiedziałam jak się to, jak to działa. Trochę jestem ekspertem.

**Damian Kaminski:** No dobrze, no ale to ja nie mam pretensji, że tego jeszcze nie ma. Właśnie po to zostało to tobie przydzielone, żeby to przeanalizować.

**Piotr Buczkowski:** Ale...

**Anna Skupinska:** Mhm.

**Damian Kaminski:** Chodzi o to, że...

**Piotr Buczkowski:** Ale coś, coś jest jeszcze niejasne w działaniu tego. Nie wiem, weź wygeneruj.

**Anna Skupinska:** A, czy – wiesz, tak wiele generuje się tylko pomieszczenie. Ma mojej poprawki to...

**Damian Kaminski:** Dobra, jeszcze raz.

