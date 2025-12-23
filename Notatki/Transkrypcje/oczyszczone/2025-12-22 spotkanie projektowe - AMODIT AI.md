**Data spotkania:** 22 grudnia 2025, 11:00

---

**Mateusz Kisiel:** Cześć.

**Przemysław Sołdacki:** Zastanawiam się, czy ktoś jeszcze do nas dołączy.

**Mateusz Kisiel:** Można by wziąć Kamila albo Łukasz Poskrobko mówił, że chciałby brać udział w tych spotkaniach.

**Przemysław Sołdacki:** Pozmienialiśmy coś w kalendarzu. Czy to spotkanie nie jest już odwołane? Chyba mamy teraz jedno spotkanie w tygodniu zamiast trzech czy czterech. Skoro jednak już tu jesteśmy i się nagrywa, to opowiedz, co się udało zrobić.

**Mateusz Kisiel:** Pokażę ekran. W ustawieniach procesu doszła nowa zakładka: "Agenci". Jest tam lista reguł agentowych. Możemy napisać prompt określający działanie agenta, np.: "Ustaw w polu tekstowym wartość 'Ala ma kota', następnie zapisz do pola 'Dokument' plik Word z opisem pól w obecnej sprawie, na koniec uruchom funkcję przypisującą obecnego użytkownika". Formularz ma pola tekstowe, dokument i obserwatora. Agent ma dostęp do wybranych funkcji, takich jak `GetProcesInfo`, `GetCaseData`, `SetCaseData`, `GetRules` czy wywoływanie konkretnych reguł (np. przypisanie obecnego użytkownika). Można ręcznie wybierać, do których funkcji agent ma dostęp ze względów bezpieczeństwa.

**Przemysław Sołdacki:** Z punktu widzenia bezpieczeństwa ma to sens, ale od strony UX-owej brzmi to na zbyt zaawansowane i trudne. Może lepiej zrobić to tak: piszesz prompta, a system sam analizuje, czego agent potrzebuje i pyta o zgodę na dostęp? Tak jak przy instalacji aplikacji na telefonie, która pyta o dostęp do GPS-a czy aparatu. Wtedy użytkownik nie musi się zastanawiać, co zaznaczyć na start.

**Mateusz Kisiel:** Tak, zaznacz wszystko jest opcją domyślną, ale można by to faktycznie zautomatyzować przy zapisywaniu prompta.

**Przemysław Sołdacki:** Dokładnie. Lista uprawnień mogłaby być w ustawieniach zaawansowanych. Ważne, żeby przy zapisywaniu agent sam zweryfikował potrzeby i wyświetlił komunikat: "Aby to zrealizować, potrzebuję dostępu do tych i tych funkcji. Czy się zgadzasz?". Jeśli tak – zapisuje. Jeśli nie – informuje, że nie będzie w stanie wykonać zadania. Dzięki temu użytkownik nie musi się tym martwić za każdym razem, a administrator może później przejrzeć i ewentualnie odebrać uprawnienia.

Fajnie, że to zrobiłeś. Wygląda to zdecydowanie lepiej niż obecne reguły. Rozumiem, że zapisuje się to w tej samej tabeli co reguły?

**Mateusz Kisiel:** Tak, dodaliśmy dwie dodatkowe kolumny. Funkcja tworzenia dokumentu Word w locie i zapisywania go do pola dokumentu też już działa.

**Przemysław Sołdacki:** Nazwy funkcji są techniczne, ale dobrze opisują działanie. Docelowo będzie ich coraz więcej, więc automatyczne dobieranie uprawnień przez agenta to będzie podstawa.

**Mateusz Kisiel:** Można też dawać uprawnienia do uruchamiania starych reguł zdefiniowanych w procesie.

**Przemysław Sołdacki:** Super. Co do wyglądu – ta lista funkcji zajmuje 1/3 ekranu. Powinna być domyślnie schowana lub w osobnym pop-upie, bo najważniejszy jest prompt.

Musimy to też ograć biznesowo i od strony bezpieczeństwa. W kluczu licencyjnym musi być opcja włączania AI per proces. Dodatkowo w ustawieniach procesu i pól powinna być flaga "niewidoczne dla AI", aby chronić poufne dane (np. HR-owe czy finansowe) przed dostępem agentów. Użytkownik biznesowy chce napisać prompta i ma działać, bez wchodzenia w szczegóły techniczne.

Pokaż jeszcze listę agentów. Zrobiłeś to jako kafelki?

**Mateusz Kisiel:** Tak, to kafelki. Można dodawać nowe i edytować istniejące.

**Przemysław Sołdacki:** Docelowo pewnie zrobimy to podobnie do listy reguł, może z wyborem widoku (kafelki/tabela). Na razie w Reactowym edytorze to wygląda dobrze. Pokaż jak to działa na sprawie.

**Mateusz Kisiel:** Jest przycisk "Ustaw Ala ma kota". Po kliknięciu pod spodem uruchamia się prompt i odpowiednie funkcje. Agent wypisuje raport z działania: "Wykonałem operacje: wpisałem wartość, wygenerowałem plik Word, przypisałem użytkownika. Wszystko przebiegło pomyślnie". Po odświeżeniu widzimy zmiany na formularzu i nowy załącznik.

**Przemysław Sołdacki:** Dla użytkownika biznesowego, który nie zna AMODIT Scriptu, to rewelacja. Będzie to jednak mocno zżerać tokeny. Ile to kosztowało?

**Mateusz Kisiel:** Sumarycznie około 8000-10000 tokenów za te kilka requestów.

**Przemysław Sołdacki:** Przy naszej cenie 100 zł za milion tokenów, jedno kliknięcie kosztuje około 1 zł. To sporo dla 2000 użytkowników klikających codziennie.

**Mateusz Kisiel:** Im większy proces i więcej pól, tym będzie drożej.

**Przemysław Sołdacki:** To świetne narzędzie do prototypowania. Użytkownik bez wiedzy programistycznej sprawdza czy pomysł działa, a potem możemy dodać opcję "konwertuj agenta na regułę", co przepisze prompta na tańszy AMODIT Script.

Marketingowo cel osiągnięty. Potrzebuję teraz od Ciebie dwóch ładnych screenshotów do marketingu: jeden z listą agentów (zrób ze trzy sensowne przykłady: "Weryfikuj poprawność faktury", "Sprawdź zgodność z zamówieniem", "Analiza SIWZ") i drugi z edycją prompta dla jednego z nich. To będzie nasze paliwo marketingowe, żeby pokazać, że AMODIT ma agentów tak jak Webcon.

**Janusz Bossak:** (dołącza do spotkania) Nie zauważyłem tego spotkania w kalendarzu.

**Przemysław Sołdacki:** Bo je skasowaliśmy i robimy teraz rzadziej, ale Mateusz właśnie pokazuje Agentów. Janusz, chcę mieć kafelki z agentami i ich opisami do marketingu. Mateusz, ukryj te techniczne listy funkcji na screenach, żeby nie straszyć ludzi.

Mateusz, spróbuj też zrobić to automatyczne dobieranie uprawnień (o czym mówiłem – jak w aplikacjach na telefon). To kluczowe dla użyteczności.

**Janusz Bossak:** Poklikam to u siebie. Ważne, żeby to nie był tylko marketing, ale żeby realnie działało.

**Przemysław Sołdacki:** Musimy być na pierwszej linii i ścigać się z rynkiem. Nawet jeśli na początku ludzie nie do końca rozumieją, czym jest agent, to muszą wiedzieć, że AMODIT go ma. Cały świat idzie w dane dostępne przez API i napędzane przez AI. Nawet firmy nietechnologiczne udostępniają teraz serwery MCP.

**Janusz Bossak:** Nie musisz nas przekonywać. Mateusz jest niezwykle szybki w dowożeniu tych rzeczy.

**Przemysław Sołdacki:** Będę zapraszał Mateusza na nasze cotygodniowe spotkania "Postęp roadmapy", żeby synchronizować AI z resztą systemu (np. z edytorem reguł).

**Janusz Bossak:** Powinniśmy też wprowadzić "Design OS" – nadzorcę nad systemem designu, żeby AI generowało komponenty od razu zgodnie z naszymi standardami (np. Ant Design czy nasze customowe style), aby wszystko było spójne wizualnie (kafelki, listy, kompaktowe widoki).

**Przemysław Sołdacki:** Zgadzam się. I na koniec dwie pilne rzeczy:
1.  **Licencjonowanie:** Musimy móc w kluczu ustawiać "AI Standard" (np. Copilot, AskAI) i "AI Advanced" (np. Agenci, serwer MCP, baza wiedzy).
2.  **Uprawnienia/Prywatność:** Globalna możliwość wyłączenia AI, dostęp do danych per proces i per pole (flaga "niewidoczne dla AI"). Klient musi mieć pewność, że AI nie namiesza w poufnych danych.

**Mateusz Kisiel:** W ustawieniach systemowych mamy już pole "kto ma dostęp do Copilota". Dodamy analogiczne dla agentów.

**Przemysław Sołdacki:** Może być podział na Copilota i Agentów, plus flaga dostępu do danych. Zastanówcie się, jak to najlepiej zorganizować w ustawieniach procesu. To ważne, bo zaraz wejdą pilotaże i musimy mieć nad tym kontrolę.

To wszystko na dziś?

**Mateusz Kisiel:** Tak. Podeślę te screeny. Cześć.

**Przemysław Sołdacki:** Dzięki, cześć.

**Janusz Bossak:** Hej, dzięki.

zatrzymano transkrypcję
