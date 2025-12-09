> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-08

# Planowanie Sprintu – 2025-11-17

**Data:** 2025-11-17
**Sprint:** 47 (okres: 2 tygodnie)
**Uczestnicy:** Damian Kaminski, Kamil Dubaniowski, Janusz Bossak, Łukasz Bott, Adrianowski, Anna Skupinska, Filip Liwiński, Łukasz Brocki, Mariusz Piotrzkowski, Mateusz Kisiel, Przemysław Rogaś, Piotr Buczkowski, Michal Zwierzchowski

## Kontekst

Spotkanie poświęcone planowaniu sprintu 47 według nowego podejścia – praca oparta o tablice w Teams z wysokopoziomowym podziałem zadań na projekty i osoby. Główny nacisk na realizację zadań rozwojowych oraz systematyczne nadrabianie zaległych bugów. Zespół potwierdził, że nowe podejście jest bardziej czytelne niż poprzednie metody planowania.

---

## Główne cele sprintu

### Repozytorium plików – MVP 1

**Projekty:** [[Klienci/WIM/Repozytorium-plikow-DMS]]

Zespół rozpoczyna prace nad MVP repozytorium plików w nowym podejściu architektonicznym. Janusz przygotował pełną rozpiską w Azure (epik → ficzery → PBI). Na jutro (18 listopada) zaplanowane spotkanie z Adrianem, Anią i Filipem w celu omówienia szczegółów technicznych przygotowanych przez Damiana na podstawie wytycznych Piotra.

**Kluczowe założenie:** zmiany w strukturze bazy danych i endpointach. Damian zaznacza, że dokumentacja jest obszerna i wymaga wspólnej weryfikacji, czy wszystko jest potrzebne w MVP.

**Zaangażowani:**
- **Adrian Kotowski** – architektura i implementacja backend
- **Anna Skupinska** – implementacja backend
- **Filip Liwiński** – implementacja frontend

---

### Integracje dla LOT

**Projekty:** [[Klienci/LOT/Integracja-UPS]], [[Klienci/LOT/Integracja-Global-Express]], [[Klienci/Lewiatan/Comarch-HUB]]

**Comarch Hub (Lewiatan):**
Integracja z Comarch Hub to priorytet numer 1 dla Lewiatana. Łukasz Brocki ma dostęp do dokumentacji API, potrzebne są jeszcze dostępy do środowiska. Michał wysłał wytyczne od klienta dotyczące mapowania. Adrian będzie wspierać doradczo, Łukasz realizuje całość implementacji.

**UPS i Global Express:**
Łukasz Bott po spotkaniu w kontekście LOT-u potwierdza, że czekamy na pytania od Łukasza Brockiego. Ustalono, że w pierwszej kolejności kończymy Comarch Hub, potem Global Express i UPS. Łukasz Brocki opracował listę pytań i wątpliwości.

**Założenie realizacji:**
Integracje z UPS i Global Express wykonywane analogicznie jak z DHL czy FedEx – po stronie AMODIT zestaw funkcji umożliwiających wysyłkę, odbiór, sprawdzenie statusu, anulowanie przesyłki (tak jak API pozwala). Robimy MVP – tyle, ile jest wymagane dla klienta i co API pozwala.

**Zaangażowani:**
- **Łukasz Brocki** – implementacja
- **Adrian Kotowski** – wsparcie doradcze (Comarch Hub)

**Status:** Czekamy na potwierdzenie zakresu z klientem.

---

### Podgląd szablonów – uproszczenie MVP

**Projekt:** [[cross-cutting/Interfejs-sprawy/Podglad-szablonow]]

Ania kończyła implementację obracania i refaktoryzacji kodu podglądu szablonów. Problem: kod jest bardzo dostosowany do załączników, wyciągnięcie go wymaga znacznej refaktoryzacji. Zespół podjął decyzję o **rezygnacji z obracania szablonów**.

**Uzasadnienie:**
Szablony to pliki cyfrowe (DOCX, PDF), nie skany – nikt nie wgrywa ich odwrotnie. Obracanie ma sens tylko przy skanowaniu dokumentów. Piotr Buczkowski: "Nie ma sensu podglądanie i obracanie, ponieważ nigdy nie zostanie to użyte."

**Zakres MVP:**
- Prosty podgląd DOCX i PDF ze stronicowaniem
- Brak dolnej belki (przechodzenie na kolejny szablon)
- Przycisk odświeżania podglądu zostaje

Damian zaznacza, że dawali takie wytyczne (kopia funkcjonalności z załączników), ale po analizie rzeczywistych potrzeb stwierdzili, że to zbędne. Janusz podkreśla wagę krytycznego myślenia: "Aniu, do ciebie, jeżeli jest jakaś funkcjonalność, to warto się zastanowić, czy ona ma sens z punktu widzenia użytkownika."

**Zaangażowani:**
- **Anna Skupinska** – dopracowanie uproszczonego MVP
- Damian zwróci uwagę na nowe oszacowanie po wyrzuceniu dolnej belki

---

### Trust Center – przenoszenie wywołań na poziom usługi

**Projekt:** [[Moduly/Trust-Center]]

Marek kontynuuje przenoszenie różnego rodzaju wywołań na poziom usługi w ramach Trust Center. Status do ustalenia na Daily.

**Uwaga:** Marek ma urlop do piątku (wraca w piątek), więc Mariusz przejmuje odpowiadanie na pytania w Trust Center. Mariusz szacuje 1-3 godziny dziennie na wsparcie.

---

### Projekt Piotra Buły – uprawnienia i powiązania spraw

**Projekt:** [[Moduly/Edytor-procesow/Matryca-uprawnien]]

Kamil Dubaniowski: zakres tego projektu jest nieznany, możliwe że będzie bardzo mały. Im dalej w analizę, tym bardziej okazuje się, że można osiągnąć cel tym, co już mamy.

**Potencjalne prace:**
- Wizualizacja struktury powiązań między sprawami na raporcie tabelarycznym (dla Marka) – **nie jest w MVP**
- Kwestia uprawnień (Mariusz) – wymaga konsultacji z Piotrem i Januszem
- Modyfikacja/nowy typ pola "odnośnik" do pokazania struktury powiązań (drzewko) – **nie jest w MVP**

Kamil zaznacza, że coraz więcej rzeczy, które planowaliśmy, schodzi na dalszy tor. Kluczowe są uprawnienia – to trzeba omówić w pierwszej kolejności (spotkanie jutro 18 listopada). Marek na razie nie będzie angażowany.

**Uwaga:** Początek sprintu to raczej prace koncepcyjne nad projektem Piotra Buły, żeby nie narobić za dużo bez potrzeby. Klient ma stały schemat od 97. roku, więc nie ma co skupiać się nad super panelem do zarządzania tym schematem.

**Zaangażowani:**
- **Mariusz Piotrzkowski** (po konsultacjach)
- **Kamil Dubaniowski** (koordynacja)
- **Marek** (wsparcie, jeśli będzie potrzebne po powrocie z urlopu)

---

### Komunikator – finalizacja wdrożenia WIM

**Projekt:** [[Klienci/WIM/Komunikator]]

Mateusz kończy wdrożenie komunikatora dla WIM. Są drobne błędy (nie funkcjonalne – przesuwanie, zmiana nazwy), grupy działają. Czekamy na wytyczne z WIM-u odnośnie konfiguracji. Trzeba podpiąć odpowiednie certyfikaty.

**Kwestia bazy danych:**
Mateusz ma przedyskutować z Piotrem kwestię połączenia komunikatora z AMODIT. Komunikator może być częścią AMODIT bazodanowo (mimo że jest odrębną aplikacją). Damian: "Warto ustalić, jak ma być tą częścią, i na przykładzie WIM-u tutaj to w odpowiedni sposób już na teście zrobić."

**Chmura:**
Mateusz pyta, czy chcemy teraz robić obsługę dla chmury? Wymaga to zmian specjalnie pod chmurę (pobieranie danych organizacji z osobnej bazy). Na chmurze komunikator musi być w tej samej bazie co AMODIT – nie ma sensu robić nowej.

**Decyzja:** Nie na ten sprint, ale warto przemyśleć na poziomie koncepcyjnym. Pytanie do Janusza i Łukasza w kontekście tego, ile to nas będzie kosztowało.

**Zaangażowani:**
- **Mateusz Kisiel** – finalizacja wdrożenia, konsultacja z Piotrem

---

### Dokumentacja procesu – generowanie przez AI

**Projekt:** [[Moduly/AMODIT Copilot]]

Zespół planuje spotkanie (Mateusz, Łukasz, Janusz) w celu omówienia automatycznego generowania dokumentacji procesu przez AI (Copilot).

**Cel:** Dać konsultantom narzędzie do tworzenia gotowej dokumentacji powdrożeniowej dotyczącej procesu. W ustawieniach procesu przycisk "Generuj dokumentację", który powoduje, że AI za pomocą dostępu do całej definicji procesu i posiadając właściwie skonstruowany prompt, generuje dokumentację w określonej strukturze (tytuł, wstęp, historia zmian, gotowy szablon).

**Drugie miejsce:** Ustawienia systemowe – "Przygotuj dokumentację konfiguracji AMODIT-u" (generowanie na podstawie wiedzy).

Janusz zaznacza, że bliżej nam jest do dokumentacji procesowej, bo tu już wiele rzeczy jest zrobionych – potrzeba tylko schematu i odpowiednio skonstruowanego promptu. "Robiliśmy ćwiczenia i to się da zrobić już teraz z AMODIT i Copilotem, tylko trzeba napisać sensowny prompt."

**Zaangażowani:**
- **Mateusz Kisiel** – implementacja
- **Łukasz Bott, Janusz Bossak** – konsultacje i wymagania

---

### Moduł raportowy – stabilizacja i błędy

**Projekt:** [[Moduly/Modul-raportowy]]

Przemek nie ma na razie zadań rozwojowych. Zespół postanowił skupić się na błędach i niestabilności modułu raportowego. Janusz robi porządki na backlogu dotyczące modułu raportowego, żeby mieć przegląd wszystkich błędów i pomysłów, spriorytetyzować i ustalić, co robimy najpierw.

**Prace refaktoryzacyjne:**
Janusz pyta Przemka o zaplanowanie spotkania dotychczasowego zespołu (Mateusz, Marek, Ania, Przemek) w celu przemyślenia, co warto refaktoryzować w nowym module raportowym, żeby działał lepiej i był bardziej stabilny.

**Zadania:** Basia, Janusz i Kamil zagregują problemy i przekażą Przemkowi. Łukasz Bott dopisuje się do tego zadania (zgłaszał różne rzeczy podczas robienia raportów systemowych).

**Zaangażowani:**
- **Przemysław Rogaś** – naprawa błędów
- **Basia, Janusz, Kamil, Łukasz Bott** – agregacja problemów

---

## Inne ustalenia

### MFA dla użytkowników zewnętrznych

- **Projekt:** [[cross-cutting/Logowanie-do-amodit]]

Damian ma zadanie "investigating/evaluating" dotyczące dodania ustawień MFA dla użytkowników zewnętrznych (brak sekcji "Bezpieczeństwo" dla nich, nie mogą zresetować MFA). Trzeba to obsłużyć dla MCIT.

Damian: "Chodzi tylko o to, żeby sekcja 'Bezpieczeństwo' wyświetlała się dla użytkowników zewnętrznych, jak już MFA jest włączone dla wszystkich." MCIT już włączyli MFA dla wszystkich.

**Status:** Damian poprawi opis i oszacowanie.

---

### Zarządzanie sprintem – filozofia planowania

**Projekt:** [[Organizacja-DEV/Dokumentacja-organizacyjna]]

**Tablice w Teams:**
Zespół używa nowego podejścia do planowania sprintu – tablice w Teams z wysokopoziomowym podziałem na projekty (bardziej po projektach niż po zadaniach). Cel: pokazanie, kto się czym zajmuje i jakie są główne cele sprintu, abstrahując od bugów i hotfixów.

**Korelacja z Azure DevOps:**
Docelowo: Inicjatywa → Epik → MVP → Ficzery. Repozytorium plików – przykład: na backlogu jest "Repozytorium MVP 1" (epik). W ramach tego jest opisane MVP 1. Jutro najpóźniej w połowie dnia będziemy wiedzieli, co jest MVP 1, i na tej podstawie określimy, że ten punkt zakończymy.

**Zasady pracy w sprincie:**
1. **Nie ma wrzutek** – oprócz hotfixów (gdy u klienta coś padło). Każdy inny przypadek wpisujemy na listę, PM-owie decydują o priorytecie.
2. **Tylko PM-owie przypisują zadania** – deweloperzy nie mogą dostawać zgłoszeń bezpośrednio od konsultantów. Jedyna ścieżka: deweloper sam sobie dodaje zgłoszenie na bieżący sprint.
3. **Codziennie rano na Daily** – PM-owie poświęcają 20 minut na przegląd zgłoszeń z poprzedniego dnia i decydują, czy są na tyle ważne, że robimy je teraz, czy planujemy na kolejny sprint.
4. **Wyjątek: serwisy** – Trust Center, OCR (Mateusz reaguje).

**Feedback zespołu:**
- **Adrian:** "To jest takie wysokopoziomowe, nie pokazuje questów czy dodatkowych zadań, pojedynczych PBI, jakiś bugów." Pyta o korelację z Azure.
- **Mariusz:** "Rozumiem w taki sposób, że na Azure mamy zadania konkretne, a w Teams mamy jakie są ogólne założenia."
- **Mateusz:** "Mi się podoba, że jest krótsze, bardziej konkretne."
- **Kamil:** "Będą się przewijały te wrzutki, ale ważnych hotfixów nie pomijamy. Dla nas to jest ułatwienie, że wy macie cel. Nikt was nie zapyta, czy zrobiliście hotfixa, to musicie po prostu zrobić. Celem jest pokazanie progresu, więc rozliczamy was z tego."

**Ochrona przed wrzutkami:**
Kamil: "Musimy się bronić przed tymi wrzutkami. Wy musicie się bronić trochę nami. Jak konsultanci próbują wam coś wcisnąć poza sprintem, a wy wiecie, że to mnóstwo roboty, to nie podejmujecie decyzji samodzielnie. Jakiekolwiek wrzutki od konsultantów bez naszej wiedzy nie są wytłumaczeniem, że nie zrobiliście celu sprintu."

---

## Wydania

### Wersja grudniowa

**Status:** Powinna już wyjść (umawialiśmy się do połowy listopada) z dopiskiem "beta" oficjalnie.

**Nowości:**
- Lista pól
- Matryca uprawnień

**Plany:**
- Pakowanie UPS i wszystko pod LOT
- Usunięcie komunikatu i opcji przełączania się na stare ustawienia systemowe
- Testowanie u nas, czy wszystko zaopiekowaliśmy

**Integracje (UPS, Global Express):**
Łukasz Bott: "Jeśli koledzy to dobrze robią jako rozszerzenia (osobne DLL-ki), to wpięcie tego, czy pojawi się w grudniowej czy marcowej, to będzie tylko kwestia podpięcia."

Kamil: "Buła może trochę namieszać jutro (uprawnienia), bo to zaingeruje, ale zobaczymy w jakim zakresie."

**Wersja marcowa (2026):**
Pojawiła się też marcowa przyszłoroczna.

---

## Porządkowanie poprzedniego sprintu

**Mateusz:** Ma wyczyscić listę "Ready to sprint" (sprint 45) – przypinać na kolejny sprint (47) lub na backlog. Pierwszeństwo: dokumentacja procesu.

Kamil: "Głównie te dotyczące bazy wiedzy, jakieś pomysły, dodanie opcji automatycznego tworzenia artykułów na podstawie linku do strony. One mają duży effort, właściwie na cały sprint."

**Ania:** Zostają do dyskusji dwa tematy odnośnie podglądów (decyzja: wyrzucamy dolną belkę).

**Damian:** Przejrzy swoje pozostałości.

**Wszyscy:** Rzućcie okiem na wyceny (strefa "estimate"), czy nie macie żadnych zleconych wycen do zrobienia.

---

## Blokery i uwagi

- **Marek** – urlop do piątku (wraca w piątek). Mariusz przejmuje wsparcie Trust Center (1-3h dziennie).
- **Łukasz Brocki** – przeciążony (Comarch Hub, UPS, Global Express). Trzeba rozpisać zadania i podjąć decyzję, czy robimy UPS czy Global Express, żeby nie miał nierealnie wpisanych celów.
- **Uprawnienia (Buła)** – jutro spotkanie (Kamil, Janusz) w celu omówienia.
- **Dokumentacja procesu** – Damian przypisuje Mateusza, Łukasza i Janusza, planuje spotkanie.
- **Repozytorium plików** – spotkanie techniczne jutro (18 listopada) – Damian, Adrian, Ania, Filip.

---

## Projekty dotknięte sprintem

- [[Klienci/WIM/Repozytorium-plikow-DMS]]
- [[Klienci/LOT/Integracja-UPS]]
- [[Klienci/LOT/Integracja-Global-Express]]
- [[Klienci/Lewiatan/Comarch-HUB]]
- [[Moduly/Trust-Center]]
- [[Moduly/Edytor-procesow/Matryca-uprawnien]]
- [[Klienci/WIM/Komunikator]]
- [[Moduly/AMODIT Copilot]]
- [[Moduly/Modul-raportowy]]
- [[cross-cutting/Interfejs-sprawy/Podglad-szablonow]]
- [[cross-cutting/Bezpieczenstwo-pentesty]]
- [[Moduly/Ustawienia-systemowe]]
