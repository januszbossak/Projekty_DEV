**Data spotkania:** 6 listopada 2025

---

**Anna Skupinska:** Cześć.

**Lukasz Bott:** Słuchajcie, jak jesteśmy w takim gronie, to ja może od razu zadam pytanie. Wyszło takie zapotrzebowanie i na szczęście prawie obiecałem coś klientowi, ale wstrzymałem się do weryfikacji. Czy widać ekran?

**Marek Dziakowski:** Tak.

**Lukasz Bott:** Mamy pole typu "Odnośnik do procesu". Można je skonfigurować, aby wyświetlić dodatkowe kolumny do wyszukiwania, ale na chwilę obecną wybór tych kolumn dotyczy tylko i wyłącznie pól typu tekstowego. Pytanie, na ile skomplikowane byłoby dorzucenie tu innych typów, w szczególności słownikowych?

**Piotr Buczkowski:** Skomplikowane.

**Janusz Bossak:** Omawialiśmy to kiedyś.

**Lukasz Bott:** Dlatego wstrzymałem konsultanta. Chciał zastosować obejście, tworząc tekstowy odpowiednik pól słownikowych, ale to głupie. Ewentualnie w skrajnym przypadku zrobić jedno pole tekstowe, gdzie mielibyśmy wszystkie wartości, po których można wyszukiwać.

**Piotr Buczkowski:** Pamiętaj, że to wyszukuje tylko od początku. Chyba że zrobimy z Lucene, ale wtedy wyszukujesz po pełnych słowach.

**Janusz Bossak:** Czy jak teraz napiszesz "abc" to znajduje?

**Piotr Buczkowski:** Nie powinien. Domyślnie jest `LIKE` od początku. Jest opcja "wyszukiwanie przez Lucene", którą można włączyć w ustawieniach tego pola w procesie.

**Janusz Bossak:** Ten temat wraca po raz enty. Już przy projekcie dla Rossmanna ograniczyliśmy to do pól tekstowych. Uważam, że trzeba się tym zająć. Nawet jeżeli to jest trudne, trzeba wymyślić jak to zrobić i zrobić.

**Piotr Buczkowski:** Na tej zasadzie (Lucene) nie będzie to trudne, bo w Lucene wszystko jest tekstem.

**Janusz Bossak:** Czyli jak wrzucisz pole słownikowe, to też zadziała, bo będzie tekstem?

**Piotr Buczkowski:** Tak, ale będzie ten sam problem co normalnie przy polach tekstowych przypisujących dane ze słownika. Jeżeli słownik się zmieni, w sprawie zostanie stara wartość.

**Lukasz Bott:** OK, natomiast powiedziałem konsultantowi Kamilowi, że wstrzymam się z tym i przedyskutuję na radzie.

**Piotr Buczkowski:** Trzeba określić, jakie pola obsługujemy. Obsługa pól słownikowych to co innego niż pól typu data czy liczbowych. Dla słownikowych wyszukujemy tekst. Dla dat i liczb najpewniej trzeba by dodać obsługę zakresów.

**Lukasz Bott:** To podsumowując, czy w ogóle podchodzimy do tego i rozszerzamy tę funkcjonalność? To jest dla klienta PKF, gdzie grupa użytkowników mocno upiera się, żeby to dorzucić.

**Piotr Buczkowski:** Dodanie pola słownikowego będzie w miarę proste. Dodanie innych pól będzie skomplikowane.

**Janusz Bossak:** Spróbujmy wylicytować, co się da zrobić. Słowniki mówisz, że są w miarę proste. Lista wyboru?

**Piotr Buczkowski:** Można dodać od ręki. Będzie to wpisywanie z palca, a nie wybór z listy. Tak samo dla słownika.

**Janusz Bossak:** Co z polem kwota, numerycznym?

**Piotr Buczkowski:** Bardziej skomplikowane, bo trzeba by zrobić jakiś zakres, a nie wyszukiwać po dokładnej kwocie.

**Janusz Bossak:** Co z datami i użytkownikiem?

**Piotr Buczkowski:** Daty tak jak liczbowe. Użytkownik w zasadzie jak słownik – po nazwie wyświetlanej, jako tekst.

**Janusz Bossak:** To może liczbowe i daty na razie zostawmy. Zróbmy te pozostałe.

**Lukasz Bott:** Czyli podsumowując, w miarę prosto jest zrobić listę wyboru, słownik i użytkownika.

**Piotr Buczkowski:** Ja bym zrobił tylko te dwa pierwsze: słownik i listę wyboru.

**Lukasz Bott:** OK, dzięki. To jest najbardziej przydatne i niezbyt skomplikowane.

**Janusz Bossak:** Warunek jest taki, że musi być włączone Lucene?

**Piotr Buczkowski:** Zależy. Dla listy wyboru wszystko jedno. Dla słownika trzeba oddzielnie oprogramować obie opcje (z Lucene i bez), bo to będzie trochę inaczej.

**Janusz Bossak:** No dobrze, to mamy konkluzję.

**Lukasz Bott:** Powiedzcie mi jeszcze o perspektywie czasowej. Na pewno nie w najbliższym sprincie?

**Janusz Bossak:** Musimy to dopiero włożyć do jakiegoś sprintu. Na pewno nie w tym. Mamy teraz do przemyślenia JRWA i ważne tematy dla LOT, które musimy zrealizować w tym roku. Wydaje się, że tam są pilniejsze rzeczy.

**Lukasz Bott:** Rozumiem. Odpowiemy klientowi, że da się to zrobić, ale wymaga to nakładu pracy i nie będzie na jutro.

**Janusz Bossak:** Powiedziałbym, że będzie po pierwszym kwartale przyszłego roku. Chyba że chcą sfinansować przyspieszenie prac.

**Marek Dziakowski:** Mam temat z Trust Center od wtorku, odnośnie tego, jak długo dokumenty wiszą z możliwością podpisu. Z tego, co ustaliłem, nie ma ram czasowych. Można ręcznie ustawić datę, do której jest możliwość podpisania, i wtedy po jej przekroczeniu dokument się blokuje. Jeżeli się tego nie poda, to dokument wisi w Blob storage, a z hot storage jest usuwany po 21/30 dniach.

**Damian Kaminski:** Ale proces w Trust Center wisi jako aktywny w nieskończoność?

**Marek Dziakowski:** Tak, dokument wisi w bazie jako możliwy do podpisania.

**Damian Kaminski:** Oczekuje na podpis. I pytanie, czy to właściwe? Robiłeś analizę, ile jest takich dokumentów starszych niż 3 miesiące?

**Marek Dziakowski:** Jest ich 106, które mają status 0 i nie mają już podglądu, bo zostały usunięte z hot storage. Ta ścieżka nie jest oprogramowana – przy próbie wejścia na taki dokument Trust Center próbuje od razu pobrać plik podpisany, zakładając błędnie, że po takim czasie powinien być podpisany. Nie da się wejść na te dokumenty.

**Damian Kaminski:** Czyli ślepa uliczka.

**Marek Dziakowski:** Pytanie, czy blokujemy takie porzucone dokumenty, czy obsługujemy ścieżkę, żeby można było do nich wrócić.

**Damian Kaminski:** Według mnie najpierw trzeba ustalić biznesowy termin ważności.

**Marek Dziakowski:** Aktualnie, jeśli jest taki problem, klient wysyła dokument jeszcze raz, a stary wisi jako śmietnik.

**Damian Kaminski:** Dobrze, ale jaki termin przyjąć? Jak ustawimy 30 dni, to będzie to tożsame z terminem przenoszenia do bloba?

**Marek Dziakowski:** To jest 21 dni od daty ostatniej modyfikacji lub 30 dni, jeśli nic się nie działo.

**Damian Kaminski:** Powinniśmy sprawdzić, jakie są faktyczne przypadki użycia. Czy ktoś wysyła dokumenty z datą podpisania dłuższą niż 30 dni? Jeśli nie, możemy to wprowadzić i udokumentować, że termin dłuższy niż 30 dni (lub niezdefiniowany) zostanie nadpisany na 30 dni.

**Janusz Bossak:** Według mnie, jeśli klient ustawił jakąkolwiek datę, to powinna ona obowiązywać, nawet 180 dni. Jeśli nie ustawił, to my ustawiamy domyślnie, np. 30 dni.

**Marek Dziakowski:** Ale to dla nas koszty, bo te dokumenty wiszą w hot storage.

**Damian Kaminski:** Nie, one mogą wisieć na blob storage, tylko musimy obsłużyć ścieżkę ich pobierania, której teraz nie ma.

**Janusz Bossak:** Trzeba dać maksymalny, nieprzekraczalny czas, np. 90 lub 180 dni, po którym dokument jest usuwany.

**Damian Kaminski:** Żeby określić tę datę, musimy sprawdzić realne dane. Marku, przygotuj zestawienie, jakie są najdłuższe terminy i jaki jest faktyczny czas od wysłania do zamknięcia procesu.

**Janusz Bossak:** Można też to monetyzować. Standardowy dostęp 14 dni jest w cenie. Chcesz 30 dni, płacisz 50 groszy więcej. Chcesz 180 dni, płacisz 5 zł więcej.

**Marek Dziakowski:** Rozmawialiśmy o tym z Łukaszem. Warto kogoś skasować za dłuższe trzymanie dokumentów.

**Janusz Bossak:** Pewnie i tak wszyscy będą wystawiać na 14 dni. Nie zarobimy, ale zaoszczędzimy, wyrzucając dokumenty z hot storage.

**Damian Kaminski:** Zróbmy tę analizę i wtedy będziemy działać.

**Marek Dziakowski:** Co z dokumentami, które już są w blob storage, niepodpisane? Mamy dawać do nich dostęp? Bo ta ścieżka nie jest obsłużona.

**Piotr Buczkowski:** Dajmy dostęp.

**Damian Kaminski:** Jeśli ustalimy, że takie procesy będą wygaszane po określonym czasie, to nie ma sensu. Sprawdźmy najpierw dane. Może to są stare testowe dokumenty i nikt do nich nie wróci, a zrobimy funkcjonalność, której nikt nie użyje.

**Piotr Buczkowski:** W AMODIT jest tak, że jak coś przejdzie do bloba, to w razie potrzeby da się to stamtąd pociągnąć. To rzadki przypadek, ale jest obsłużony. Nie wiem, dlaczego tu zrobiono inaczej.

**Damian Kaminski:** To ma niski priorytet. Najpierw ustalmy, co robimy z datą graniczną i cennikiem, a potem to obsłużymy. Ale najpierw analiza danych.

**Anna Skupinska:** Wracając do filtrów w raportach, przeanalizowałam to. Dane do filtrów są pobierane z dwóch miejsc. Jeśli polem jest "etap", to pobierane są wszystkie etapy bez ograniczenia do 20 pozycji, ale jeśli etapy mają tę samą nazwę, są zwijane do jednej pozycji.

**Damian Kaminski:** Czyli jeśli filtr jest na etapie, zawsze wyświetlamy wszystko?

**Anna Skupinska:** Tak. Dla każdego innego pola jest inaczej: zapytanie bierze pod uwagę tylko to jedno pole i pobiera 20 pierwszych pozycji z wyniku raportu.

**Damian Kaminski:** To nie jest prawda, bo Janusz pokazywał, że raport pobierał 2 wyniki, a powinny być 3.

**Janusz Bossak:** To dwa różne zagadnienia. Jedno, że na liście nie wyświetla się wszystko, mimo że dane są (co widać na legendzie). Drugie, to co mówi Ania, że jeśli pozycji jest więcej niż 20, to "zaznacz wszystko" zaznaczy tylko te widoczne 20.

**Damian Kaminski:** Aniu, według twojej analizy, jeśli pole nie jest etapem, wyświetla 20 pozycji. To nieprawda w przypadku Janusza.

**Marek Dziakowski:** Obstawiam, że nie jest robiony `DISTINCT` i po prostu zwraca np. 10 razy "BI", co zajmuje 10 z 20 pozycji, a reszty nie widać. Trzeba dodać `DISTINCT`, żeby brał tylko pojedyncze wystąpienia.

**Janusz Bossak:** To musi być grupowanie.

**Marek Dziakowski:** Tak, trzeba dodać flagę w zapytaniu, żeby brało `DISTINCT`. Kod, który to zwraca, był pisany pod dane do raportu, a nie do filtrów.

**Janusz Bossak:** Musimy zrobić refaktoryzację, żeby to działało, jak powinno. Jak poprawiamy filtry, to nie psujemy legendy i na odwrót.

**Damian Kaminski:** Aniu, czy jesteś w stanie opisać w tym zadaniu, co dokładnie trzeba zrobić, wraz z kryteriami akceptacji?

**Anna Skupinska:** Tak, mogę.

**Damian Kaminski:** Super. A co z problemem, gdy jest więcej niż 20 unikalnych pozycji?

**Anna Skupinska:** No właśnie, "zaznacz wszystko" zaznaczy tylko te 20.

**Janusz Bossak:** "Zaznacz wszystko" nie powinien być tylko frontendowo obsłużony. To oznacza, że użytkownik chce wybrać wszystkie opcje.

**Marek Dziakowski:** Wtedy trzeba by zmienić logikę, żeby "zaznacz wszystko" działało jak `LIKE` w SQL.

**Anna Skupinska:** Mamy problem z ilością parametrów w `IN (...)`. Nie powinno być więcej niż 500-1000. Musimy dodać jakieś ograniczenie.

**Damian Kaminski:** Zgadzam się. To podejście jest krótkofalowe. Zamiast "zaznacz wszystko", powinniśmy mieć "zawiera", ale to nie jest dostępne dla pól numerycznych.

**Marek Dziakowski:** Aktualnie dla szóstki wyszukuje wszystkie kombinacje (6, 16, 60), więc działa jak `LIKE`. Ten sam mechanizm trzeba użyć dla "zaznacz wszystko".

**Damian Kaminski:** Ale co z wydajnością przy milionie spraw?

**Anna Skupinska:** Wtedy jest problem z liczbą parametrów.

**Marek Dziakowski:** Wyniki i tak są dzielone na strony, więc nie pobierze się miliona naraz.

**Damian Kaminski:** OK, czyli "zaznacz wszystko" zamienia operator `=` na `zawiera`?

**Anna Skupinska:** Tak.

**Janusz Bossak:** To powinno działać inaczej. Jeśli w filtrze nic nie wpisano, "zaznacz wszystko" powinno oznaczać brak filtrowania. Jeśli wpisano "6", "zaznacz wszystko" powinno zaznaczyć wszystko, co pasuje do "6".

**Damian Kaminski:** Jeśli nic nie wpisano, przycisk "zaznacz wszystko" nie powinien być w ogóle widoczny.

**Janusz Bossak:** Słusznie.

**Damian Kaminski:** Nie jestem przekonany, czy jesteśmy w stanie to dzisiaj ustalić. Tu jest za dużo wątków.

**Anna Skupinska:** To temat na osobną radę architektów. Na razie zrobię zadanie z `DISTINCT`, a potem omówimy resztę.

**Damian Kaminski:** Dobrze, ale przygotuj proszę propozycje rozwiązań na następne spotkanie.

**Anna Skupinska:** OK. Rzeczy do omówienia: 1. Jak i czy dodawać ograniczenie liczby parametrów w filtrze. 2. Czy dodać przycisk "Załaduj więcej". 3. Jak ma działać "Zaznacz wszystko". 4. Dodanie filtra "zawiera" dla wartości liczbowych.

**Damian Kaminski:** W Excelu to działa tak, że filtry na siebie oddziałują. Jak ograniczę zbiór danych jednym filtrem, to w drugim widzę tylko opcje pasujące do już okrojonego wyniku.

**Marek Dziakowski:** To rodzi problemy wydajnościowe, bo po zmianie jednego filtra trzeba by przeliczać wszystkie inne.

**Damian Kaminski:** To wyzwanie. Trzeba zobaczyć, jak to działa w Excelu i zastanowić się. Podsumowując: Aniu, zrób zadanie na `DISTINCT`, a resztę rozbij na osobne PBI w ramach nowego feature'a, będziemy je dalej omawiać.

**Anna Skupinska:** OK, czyli to PBI zamieniamy na feature.
