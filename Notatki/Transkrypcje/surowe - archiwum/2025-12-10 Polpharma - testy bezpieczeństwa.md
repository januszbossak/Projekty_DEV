Polpharma - testy bezpieczeństwa

Klient chce zrobić testy bezpieczeństwa i pyta nas kiedy były to dla nas najlepszy moment.

Widzę trzy zasadnicze warunki, które mogą wpłynąć na ten termin:

1) Stabilizacja wersji - musimy mieć pewność, że dana wersja (z wydania 2506) jest już stabilna i mogą na niej działać na środowisku TEST (to wydaje mi się, że jesteśmy już w trakcie, ale poczekałbym na hotfixy ostatnio zgłoszone w Arval i Adecco) DW Michal Zwierzchowski

2) Toczące się wdrożenia - Mateusz Kolakowski klient mówił, że obecnie jakieś 2-3 tematy są tam prowadzone i pytanie, czy nie widzisz tu jakichś możliwych komplikacji?

3) Zasoby DEV - myślę, że dobrze wybrać okres kiedy dział DEV miałby czas na 'szybkie' zareagowanie na takie rekomendacje po pen-testach w przypadkach krytycznych.

Standardowo kliencie nasz nie informowali z wyprzedzeniem i nie pytali i terminy, a tutaj mamy taką swobodę - więc Janusz Bossak Lukasz Bott dajcie znać czy macie w planie jakiś okres, gdzie takie wyniki testów byłby dla Was wygodniejsze do obsłużenia, aby nie zawalać innych terminów z pewnością nie w tym roku ![🙂](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/smile/default/20_f.png "Uśmiech")   bardziej chodzi o to, czy ma to dla Was znaczenie czy styczeń czy luty, czy jakieś okna w tym miesiącach? bo ja bym zapytał ile bedzie trwał audyt, kiedy dostaniemy wyniki i np wtedy potrzebny by był Wasz czas najbardziej czyli po wynikach, a nie w trakcie Daniel Reszka nie pierwszy i nie ostatni raz klienci przysyłają nam wyniki pentestow ![🙂](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/smile/default/20_f.png "Uśmiech")

Jesteśmy na takie sytuacje przygotowani i ogarnialiśmy je w przeszłości to i tym razem ogarniemy ważne jest, aby zanim przystąpią do tych testów, abyśmy my (astrafox) sprawdzili tzw hardening. Tu prośba do Lukasz Bott aby to sprawdzić, czy wszystko co zalecamy (po poprzednich różnych pentestach) jest odpowiednio skonfigurowane u klienta Może przed testami zrobimy analizy z Sonar Cloud? też dobry pomysł i nie tylko tym narzędziem ale tez tym [https://www.zaproxy.org/](https://www.zaproxy.org/ "https://www.zaproxy.org/")

The ZAP Homepage

Welcome to ZAP! To dajcie znać jak możemy to zaplanować Lukasz Bott Michal Zwierzchowski

ja będę pilnował wersji - ale to mamy dogadane, pytanie kiedy możemy zrobić te nasze wewnętrzne 'hardeningi', aby po nich jeszcze sobie zrobić analizę i potem pozwolić klientowi Tu jest wynik skanowania narzędziem o którym pisał Janusz Bossak [http://security_report.amodit.local](http://security_report.amodit.local "http://security_report.amodit.local/") Daniel, w ramach tzw. hardening-u aplikacji proponuję, abyśmy wspólnie przeszli tą checklistę: [https://astrafox.amodit.com/forms/mCase.aspx?caseId=136514](https://astrafox.amodit.com/forms/mCase.aspx?caseId=136514 "https://astrafox.amodit.com/forms/mcase.aspx?caseid=136514"). Na razie oczywiście dla środowiska testowego w Polpharmie. A czy przypadkiem oni nie mają tego środowiska u nas w wydzielonej chmurze?

AstraFox Login page mają Tomasz Kalinowski umówisz się z Łukaszem w tym temacie? Tylko ustalmy na jakiej wersji chcemy to robić jeszcze (który build wersji czerwcowej jest zalecany tutaj) a jaką wersję obecnie tam mają? ja dzisiaj korzystałem już build'u 250603.135 250630.122 Polpharma 250630.122 Polpharma Test 250630.133 Na razie robimy na Polpharma Test 250630.133. Bo rozumiem, że pentesty będą uruchamiać na tym środowisku? tak na TEST będą robić To może zaktualizujemy do najnowszej?  no zależnie kiedy Łukasz i Tomek się umówią to można przed tym podnieść do obecnie najnowszego buildu Teraz jest 135 i dziś będzie 136 Michal, z tego, co pamiętam, to aktualizację chmury planujemy w przyszłym tygodniu (15-19 grudnia). Jeśli tak, to zaktualizujcie również Polpharmę TEST(!!!) do wydania 250630.136. Mamy na liście do zaktualizowania Polpharma test