**Data spotkania:** 10 grudnia 2025

---

**[Daniel Reszka]:**:** Klient chce zrobić testy bezpieczeństwa i pyta nas, kiedy byłby to dla nas najlepszy moment.

Widzę trzy zasadnicze warunki, które mogą wpłynąć na ten termin:

1) Stabilizacja wersji – musimy mieć pewność, że dana wersja z wydania 2506 jest już stabilna i mogą na niej działać na środowisku TEST. To wydaje mi się, że jesteśmy już w trakcie, ale poczekałbym na hotfixy ostatnio zgłoszone w Arval i Adecco.

2) Toczące się wdrożenia – Mateusz Kolakowski, klient mówił, że obecnie jakieś 2-3 tematy są tam prowadzone i pytanie, czy nie widzisz tu jakichś możliwych komplikacji?

3) Zasoby DEV – myślę, że dobrze wybrać okres, kiedy dział DEV miałby czas na szybkie zareagowanie na takie rekomendacje po pentestach w przypadkach krytycznych.

**[Janusz Bossak]:** Standardowo klienci nasi nie informowali z wyprzedzeniem i nie pytali o terminy, a tutaj mamy taką swobodę. Łukasz Bott, dajcie znać, czy macie w planie jakiś okres, gdzie takie wyniki testów byłyby dla Was wygodniejsze do obsłużenia, aby nie zawalać innych terminów. Z pewnością nie w tym roku. Bardziej chodzi o to, czy ma to dla Was znaczenie, czy styczeń, czy luty, czy jakieś okna w tych miesiącach? Bo ja bym zapytał, ile będzie trwał audyt, kiedy dostaniemy wyniki i np. wtedy potrzebny by był Wasz czas najbardziej – czyli po wynikach, a nie w trakcie.

**[Janusz Bossak]:** Nie pierwszy i nie ostatni raz klienci przysyłają nam wyniki pentestów. Jesteśmy na takie sytuacje przygotowani i ogarnialiśmy je w przeszłości, to i tym razem ogarniemy. Ważne jest, aby zanim przystąpią do tych testów, abyśmy my (AstraFox) sprawdzili tzw. hardening. Tu prośba do Łukasza Bott, aby to sprawdzić, czy wszystko, co zalecamy po poprzednich różnych pentestach, jest odpowiednio skonfigurowane u klienta.

**[Michał Zwierzchowski]:** Może przed testami zrobimy analizy z Sonar Cloud?

**[Janusz Bossak]:** Też dobry pomysł i nie tylko tym narzędziem, ale też tym: https://www.zaproxy.org/

**[Janusz Bossak]:** To dajcie znać, jak możemy to zaplanować. Łukasz Bott, Michał Zwierzchowski.

**[Daniel Reszka]:** Ja będę pilnował wersji – ale to mamy dogadane. Pytanie, kiedy możemy zrobić te nasze wewnętrzne hardeningi, aby po nich jeszcze sobie zrobić analizę i potem pozwolić klientowi.

**[Michał Zwierzchowski]]:** Tu jest wynik skanowania narzędziem, o którym pisałem: http://security_report.amodit.local

**[Łukasz Bott]:** Daniel, w ramach tzw. hardeningu aplikacji proponuję, abyśmy wspólnie przeszli tę checklistę: https://astrafox.amodit.com/forms/mCase.aspx?caseId=136514. Na razie oczywiście dla środowiska testowego w Polpharmie. A czy przypadkiem oni nie mają tego środowiska u nas w wydzielonej chmurze?

**[Tomasz Kalinowski]:** Mają.

**[Janusz Bossak]:** Tomasz Kalinowski, umówisz się z Łukaszem w tym temacie? Tylko ustalmy, na jakiej wersji chcemy to robić jeszcze – który build wersji czerwcowej jest zalecany tutaj?

**[Michał Zwierzchowski]:** A jaką wersję obecnie tam mają?

**[Janusz Bossak]:** Ja dzisiaj korzystałem już z buildu 250603.135.

**[Michał Zwierzchowski]:** 250630.122 Polpharma, 250630.122 Polpharma Test, 250630.133.

**[Janusz Bossak]:** Na razie robimy na Polpharma Test 250630.133. Bo rozumiem, że pentesty będą uruchamiać na tym środowisku?

**[Michał Zwierzchowski]:** Tak, na TEST będą robić.

**[Janusz Bossak]:** To może zaktualizujemy do najnowszej?

**[Michał Zwierzchowski]:** No, zależnie kiedy Łukasz i Tomek się umówią, to można przed tym podnieść do obecnie najnowszego buildu. Teraz jest 135 i dziś będzie 136.

**[Daniel Reszka]:** Michał, z tego, co pamiętam, to aktualizację chmury planujemy w przyszłym tygodniu (15-19 grudnia). Jeśli tak, to zaktualizujcie również Polpharmę TEST do wydania 250630.136.

**[Michał Zwierzchowski]:** Mamy na liście do zaktualizowania Polpharma test.





