**Data spotkania:** 9 października 2025, 08:00

---

**Piotr Buczkowski:** Cześć.

**Anna Skupinska:** Cześć.

**Łukasz Bott:** Ponieważ zgłoszeń na radę jako takich, w sensie zakwalifikowanych, nie mamy. Rozumiem, że chciałaś porozmawiać o tych licencjach całych, tak?

**Anna Skupinska:** Tak, tylko pytanie właśnie, bo to zadziała, jeżeli się postawi tę licencję w taki sposób. Wtedy przestaje krzyczeć, że coś jest nie tak. Mogę wam pokazać, bo to jest w miarę proste. Czy widać już?

**Piotr Buczkowski:** Tak.

**Anna Skupinska:** Więc po prostu trzeba się odwołać do DevExtreme Config i podać mu klucz licencji w ten sposób. To jest klucz, który skopiowałam z tej witryny. Okazuje się, że ten program – spróbował coś innego, ale nieważne. To działa, on sobie to konfiguruje. Ważne, żeby ten config uruchomić przed czymkolwiek z DevExtreme, żeby on miał dostęp, bo inaczej uzna, że nie ma dostępu. Tego właśnie tu uruchamiamy w main.tsx w tym miejscu. I to jest pytanie, bo ponieważ to jest JavaScript, to pomimo tego, że kod będzie zminifikowany czy nieco trudniej będzie odczytać, ale ciągle można go odczytać. Więc tak podali, żeby to zrobić w witrynie DevExtreme, gdzie są podawane te wszystkie instrukcje DevExtreme nawet. Jak to chyba było tutaj? Nie, to nie to. Tak, tu jest instrukcja jak to zrobić i ogólnie rzecz biorąc, zrobiłam tak samo. I to działa, tylko że oczywiście nie mam doświadczenia z tym, nie wiem czy to jest w porządku, bo wcześniej my nie sprawdzaliśmy tego klucza licencyjnego. Wygląda na to, że wcześniej nie sprawdzali tego klucza licencyjnego tutaj, że mieliśmy wcześniej wersję 22, a od wersji 23 zaczęli go sprawdzać. Więc pytam się czy są jakieś przeciwwskazania, żeby umieszczać tak bezpośrednio w kodzie klucz licencyjny?

**Damian Kaminski:** Przepraszam, że się spóźniłem. Słuchajcie, pozwolę sobie pokazać to co wczoraj nie wysłałem, bo tak będzie chyba najszybciej.

**Łukasz Bott:** Znaczy tak, jeżeli ja się mogę odnieść co do zasady – chyba nie powinniśmy hardcodować tego typu kluczy.

**Damian Kaminski:** Poczekaj, poczekaj, Łukasz. Dobra, pozwólcie, że przeczytamy to co jest napisane.

**Janusz Bossak:** On nie ma instrukcji, ale...

**Anna Skupinska:** Czy jest instrukcja? Instrukcja jest tutaj.

**Łukasz Bott:** Dobry.

**Damian Kaminski:** Instrukcja mówi, że tak jest – jak Ania powiedziała, nie byłem od początku, ale zakładam, że właśnie to powiedziała. Czyli dla tych wszystkich bibliotek frontendowych właśnie tak wygląda ten temat. Zaraz. "Klucze licencyjne są publiczne ze względu na kliencki charakter aplikacji JavaScript. Jeśli odkryjesz, że twój klucz licencyjny został skradziony, naruszony, możesz skontaktować się z naszym działem do spraw zgodności". Więc oni mają świadomość, że to tak działa i tyle. Według mnie olewamy ten temat totalnie.

**Janusz Bossak:** Dzień dobry.

**Łukasz Bott:** Dobra, no to...

**Janusz Bossak:** Dobrze, koniec dyskusji. Szkoda czasu na to.

**Damian Kaminski:** Dokładnie.

**Janusz Bossak:** Czyli mój wniosek jest taki jeszcze, żeby wziąć i kupić po prostu jeszcze nowszą wersję, bo teraz ta, co instalujemy, to jest 24.1, a już jest chyba 25.2. Więc pewnie kolejne jakieś zmiany i ulepszenia są. I po prostu dbajmy o to – jak będziemy mieli już kupioną licencję, to bym chciał, tak jak tutaj Piotr dobija się zawsze do GdPicture, żeby po pierwsze była osoba odpowiedzialna za tą bibliotekę. Możesz to być ty, Ania, obojętnie Marek czy ktoś, ale ta osoba ma obowiązek śledzenia zmian w tej bibliotece. I w momencie, kiedy mamy jakiś problem, jakiś błąd – tak jak tutaj tego się to wszystko zaczęło od natury podwójnych nagłówków – żeby w pierwszej kolejności sprawdzać, czy to nie jest przypadkiem błąd biblioteki. I jeżeli jest to błąd biblioteki, to absolutnie natychmiast skontaktować się z tą firmą, wysyłać zgłoszenia na support. Za to płacimy. I od tego oni są. Nie oznacza to, że oni natychmiast za tydzień poprawią, ale może za miesiąc poprawią, w następnym wydaniu poprawią, ale przynajmniej są świadomi.

**Piotr Buczkowski:** Albo przynajmniej podadzą jakiś sposób rozwiązania.

**Janusz Bossak:** Albo podadzą jakieś workaround czy coś takiego. To już Piotr...

**Damian Kaminski:** Dokładnie, bo mogą być alternatywne. Ale to jest jedno co Janusz powiedział, i drugie to kwestia – w ogóle, niezależnie od błędów – wydajemy wersję, wydajemy ją z najnowszą wersją biblioteki. Czyli tak jak robimy te testy bezpieczeństwa co jakiś czas, to według mnie trzeba co jakiś czas zerknąć, czy wyszła nowa wersja. Oni, z tego co zobaczyłem, wychodzą 2 razy w roku. Więc to nie jest jakaś częstotliwość niesamowita. Musimy po prostu o tym pamiętać i mieć może takich kilka punktów na miesiąc przed wydaniem czy na 2 tygodnie, żeby sprawdzić to, to, to, tę bibliotekę, jakieś tam przeprowadzić testy bezpieczeństwa, jeśli to robimy też w jakimś cyklu.

**Janusz Bossak:** Dokładnie. Na przykład z tego, co widzieliśmy – tak przynajmniej pobieżnie, tu chyba z Damianem – że tematy w DataGrid są rozwiązane, przynajmniej częściowo. Może nie w 100 procentach, ale w jakichś tam, powiedzmy, 70 procentach mają ogarnięte w DataGrid. Więc wiecie, zastanawiamy się nad jakimiś tematami, że jakie tu robić, ile to czasu. No to okazuje się, że po prostu biblioteka konsekwentnie ma to wdrażane. I po prostu tego trzeba się trzymać, także żeby nie bić piany. Ania, zostajesz szefem tej biblioteki. I na Twojej głowie jest to, żeby tam co kwartał, albo w ramach kwartału, sobie zajrzeć na stronę DevExpress, DevExtreme, zobaczyć co tam w najnowszym wydaniu. I zdecydować, czy aktualizujemy, czy nie. I w momencie, kiedy pojawiają się błędy związane z tym obszarem, żeby to sprawdzić – po prostu zajrzeć na ich forum, wysłać maila, zapytać się o cokolwiek, skontaktować się, sformułować zagadnienie. Po prostu trzeba się opiekować tym, żebyśmy korzystali w miarę zawsze z najnowszej wersji, żebyśmy na siłę nie poprawiali po swojej stronie czegoś, co może już jest poprawione po stronie biblioteki. I tak zrobimy z każdą biblioteką, jaką mamy, że będzie osoba odpowiedzialna. To tak naturalnie, jakby Piotr jest odpowiedzialny za GdPicture, bo w sumie na niego jest...

**Piotr Buczkowski:** Bo tam jest sprawdzane przy kompilacji. Na komputerze, na którym się kompiluje, mamy tylko jedno licencję, stąd...

**Janusz Bossak:** Tak, tak, tak, tak.

**Damian Kaminski:** I tu jest tak samo, tylko tu jest właśnie ta natura. I wcześniej jakoś tam inaczej była, lecz z racji, że to jest klucz publiczny... Więc tam nie jest to sprawdzane, ale jest...

**Piotr Buczkowski:** No, no, no.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Jest tak, że ja kompiluję bibliotekę i załączam już gotową bibliotekę, a inni programiści nie kombinują, stąd nie jest wymagany klucz.

**Damian Kaminski:** Dokładnie.

**Janusz Bossak:** Tak, tak, tak, tak.

**Damian Kaminski:** I tam też to jest opisane. Natomiast tylko dopowiem jeszcze, bo tam, Aniu, zgłoszony jest po prostu Michał jako właśnie ten developer. Według mnie powinnaś przepiąć w ramach tego konta Janusza na siebie. Jak nie masz, to założyć konto, wpiąć siebie i mieć to pod swoim mailem, a te Janusza dane niech będą Janusza.

**Janusz Bossak:** To tak, który będzie też wystawał. Ja teraz to nawet tutaj postaram się...

**Damian Kaminski:** Dokładnie i tam pewnie to, co Janusz powiedział, pewnie można ustawić, żeby był newsletter. A oni pewnie jak wydają 2 razy w roku, to tam częściej nie puszczają tego newslettera, więc nawet nie trzeba wchodzić, tylko sami się przypomną, że jest nowa wersja.

**Janusz Bossak:** Tak, tak, tak. Oni wysyłają, dostaję tam na maile od czasu do czasu jakąś informację. Nie pamiętam, Markowi to przesyłałem jakoś, może nie pamiętam, nieważne. Bynajmniej, jeżeli my będziemy mieli osobę przypisaną – pytanie, czy się zgadzasz na takie przypisanie?

**Anna Skupinska:** Dobrze.

**Janusz Bossak:** To teraz się na tym drugim... Dobra, to jedźmy dalej. A ja tutaj staram się... Do konta przypisać. A jeszcze kolejny wątek z tego, co chciałem powiedzieć – to kupmy po prostu najnowszą wersję. Teraz nas będzie kosztować trochę więcej, bo 800... Ja stanąłem – nie, prawie 900 dolarów. A jak tam jest aktualizacja, czyli upgrade, to chyba jest o 200 dolarów mniej.

**Damian Kaminski:** Ja już ci, Janusz, wystawiłem tam zgłoszenie wczoraj.

**Janusz Bossak:** To jest też tak, apropos w ogóle wątek dyskusji mojej z Przemkiem i z Piotrkiem, w ogóle z działem handlowym na temat cennika po naszej stronie. Bo taka firma jak tutaj właśnie DevExtreme sprzedaje coś za 900 jednostek na rok, ale jak chcesz aktualizować, to sprzedaje ci za 600 jednostek za rok. A my sprzedajemy, powiedzmy, za 100 jednostek, a bierzemy za 35 jednostek. Więc ta skala jest tutaj zupełnie inna – proporcja pomiędzy ceną sprzedaży a ceną aktualizacji. Ale tutaj dyskusja... Temat naszych cen... Dobra, temat zamknięty. Co dalej?

