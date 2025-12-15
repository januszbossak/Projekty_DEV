**Autor**: Janusz Bossak
**Data**: 2025-12-12

Przez ostatnie miesiące obserwuję istotną zmianę w tym, jak działają modele AI. To nie jest kolejny marketingowy hype – zmiana jest techniczna i ma realne konsekwencje dla naszych produktów.

## Czemu piszę tę notatkę?

Wiem, że część z Was zniechęciła się do AI po doświadczeniach sprzed kilku miesięcy – płytkie odpowiedzi, błędy, halucynacje. To było uzasadnione. Ale modele z końca 2025 roku działają zauważalnie inaczej i warto to zobaczyć na własne oczy.

Do niedawna modele językowe działały jak intuicja – odpowiadały natychmiast, bez "zastanowienia" (tzw. System 1). W skomplikowanych zadaniach biznesowych takie podejście generowało błędy.

Nowe modele (GPT-5.2, Gemini 3, Opus 4.5) przed odpowiedzią wchodzą w fazę wewnętrznego rozumowania – generują hipotezy, weryfikują je, planują (System 2). Model "myśli" dłużej, ale wynik jest znacznie bardziej wiarygodny. I to nie jest subtelna różnica – to skok jakościowy.

## Jak już wykorzystujemy AI wewnętrznie?

Zanim przejdę do planów produktowych, warto podkreślić że jako firma już intensywnie korzystamy z AI w codziennej pracy. To nie jest teoria – to praktyka.

**Sprzedaż:**
- Klasyfikator klientów – AI pomaga ocenić potencjał leadów
- Analizator zapytań ofertowych – automatyczna analiza wymagań i rekomendacje

**Spotkania:**
- Wielu z nas korzysta z automatycznych podsumowań spotkań przez AI
- Transkrypcje, wyciąganie action items, przypomnienia spotkan farmingowych zarzadu

**Zespoły techniczne:**
- Analiza kodu, wykrywanie przyczyn błędów, propozycje poprawek
- Pisanie dokumentacji i testów jednostkowych
- Generowanie całych aplikacji pomocniczych (np. dashboard kosztów Azure)
- Analiza problemów sieciowych i infrastrukturalnych

To powoli staje się standardem. Zachęcam każdego do eksperymentowania – narzędzia są dostępne, a krzywa uczenia się jest coraz łagodniejsza.

## Co to zmienia w AMODIT?

### 1. OCR: od specjalizowanych modeli do LLM

Obecnie nasz OCR opiera się na Azure Document Intelligence – modelach wytrenowanych przez Microsoft dla faktur i paragonów, wspieranych przez nas modelami LLM w post-procesingu do "doczytywania" trudniejszych przypadków.

Trend jest jednak taki, żeby przejść na pełne przetwarzanie dokumentów przez modele LLM, bez warstwy specjalizowanego OCR. Testowaliśmy to na Gemini 3 i rezultaty są obiecujące. Microsoft sam idzie w tym kierunku – promuje teraz Azure Content Understanding zamiast Document Intelligence.

Dla nas to oznacza możliwość uproszczenia architektury i lepszego radzenia sobie z dokumentami, które są bardziej złożone. Dla klientów przekłada się to na wyższą skuteczność i dokładność, szczególnie w przypadku skomplikowanych i nietypowych faktur, gdzie tradycyjne metody często zawodzą.

### 2. Walidacja merytoryczna

Dotychczasowe reguły walidacyjne sprawdzają formę: czy pole jest wypełnione, czy format jest poprawny, czy wartość mieści się w zakresie. Modele z rozumowaniem potrafią sprawdzić treść.

Przykład: faktura za "Usługi doradcze – etap 3". Agent AI może:
- Znaleźć w repozytorium umów kontrakt z tym dostawcą
- Sprawdzić w harmonogramie, czy etap 2 został odebrany protokołem
- Porównać stawkę na fakturze ze stawką w umowie
- Wstrzymać płatność i opisać rozbieżność, jeśli coś się nie zgadza

Choć teoretycznie można by to zrealizować za pomocą reguł, wymagałoby to przewidzenia każdego możliwego przypadku. Może okazać się, że wystarczy zdefiniować zasady dla AI oraz wdrożyć kryteria oceny jej odpowiedzi.

Tak, generuje to koszty związane z wykorzystaniem AI. Ale w ostatecznym rozrachunku prawdopodobnie będzie to rozwiązanie tańsze niż wielomiesięczne wdrożenie tradycyjnymi metodami – a także bardziej elastyczne w utrzymaniu i rozwoju. Co najważniejsze, nowe modele znacząco redukują problem "halucynacji", który był największym kontrargumentem. Tempo zmian jest tak dynamiczne, że to, co jeszcze 2-3 miesiące temu wydawało się odległą perspektywą, dziś jest już rzeczywistością. Nie twierdzę, że jest to już w pełni wykonalne, ale biorąc pod uwagę ten wyścig, może stać się możliwe szybciej, niż nam się wydaje.

### 3. "Vibe Coding" w AMODIT Copilot

Zamiast rysować diagramy procesów, administrator opisuje proces w języku naturalnym: "Stwórz proces obiegu faktur kosztowych. Jeśli kwota przekracza budżet MPK, wyślij do dyrektora pionu."

AMODIT Copilot już teraz potrafi na tej podstawie wygenerować schemat procesu oraz formularze. Kolejnym krokiem jest rozszerzenie jego możliwości o generowanie skryptów reguł, które opisują logikę biznesową. Dodatkowo, intensywnie myślimy o wprowadzeniu Agentów, którzy będą autonomicznie wykonywać określone operacje, co jest naturalnym rozwinięciem koncepcji "myślących" modeli AI i kluczowe dla podążania za trendami w branży.

### 4. AMODIT jako uczestnik ekosystemu AI (MCP i narzędzia)

Planujemy uruchomić serwer MCP (Model Context Protocol), aby umożliwić zewnętrznym systemom AI komunikację z AMODIT. MCP to uniwersalny standard komunikacji, działający jak API dla sztucznej inteligencji.

Z drugiej strony, w AMODIT Copilot wbudowaliśmy już możliwość korzystania z zewnętrznych narzędzi, takich jak przeszukiwanie sieci, bazy wiedzy oraz integracja z dowolnymi dostępnymi serwerami MCP. Obecnie pracujemy nad warstwą bezpieczeństwa, zanim użycie tych funkcji będzie możliwe produkcyjnie. W kontekście AskAI chcemy wyposażyć te funkcje w zdolność do inteligentnego korzystania z narzędzi – na przykład, aby AI samo wiedziało, kiedy i za pomocą jakiej funkcji sprawdzić kontrahenta w GUS, po prostu wywołując naszą funkcję. Wiem, już słyszę głosy, iż to bez sensu, że lepiej napisać skrypt, który to robi – że to taniej, pewniej itd.

Tak, dzisiaj tak, ale za kilka miesięcy może jednak tak już nie być.
#### Rozmawiające systemy – przyszłość czy futurystyka?

MCP otwiera ciekawą perspektywę: systemy takie jak AMODIT i np. SAP czy Comarch ERP mogłyby "rozmawiać" przez AI, bez tradycyjnych sztywnych integracji API. Użytkownik w AMODIT prosi: "Sprawdź w SAP czy faktura od Budimex została zaksięgowana". Agent AI wie, że ma dostęp do SAP przez MCP, sam formułuje zapytanie, interpretuje odpowiedź i zwraca wynik w zrozumiałej formie.

Czy to futurystyka? Częściowo – duzi vendorzy ERP są konserwatywni i pełna adopcja potrwa. Ale kierunek jest jasny: Anthropic i OpenAI promują MCP, a elastyczność takiego podejścia może w perspektywie kilku lat przeważyć nad tradycyjnymi integracjami punkt-po-punkcie. Dla nas to oznacza: warto przygotować AMODIT zarówno jako klienta MCP (korzystającego z zewnętrznych systemów), jak i serwer MCP (udostępniającego nasze funkcje innym AI).

### 5. Raportowanie i filtrowanie w języku naturalnym

Chcemy, żeby użytkownik mógł po prostu zapytać: "Ile urlopu mi zostało?" albo "Kiedy wpłynęła faktura od Budimex i na jaką kwotę była?" – bez znajomości filtrów i struktury bazy, bez budowania raportów, po prostu w oknie AMODIT Copilot.

A biorąc pod uwagę otwarcie AMODIT poprzez MCP, można wyobrazić sobie zadawanie takich pytań z poziomu ChatGPT, Claude lub innych narzędzi AI.
### 6. Autodiagnostyka systemu

To obszar, w którym modele z rozumowaniem mogą pokazać swoją wartość. Chodzi o łączenie kropek z różnych źródeł: logów systemowych, monitora wydajności, historii zmian w regułach, wykonywania jobów.

Zadaniem AI będzie dostrzeganie potencjalnych problemów zanim się objawią. Nie reaktywne "coś się zepsuło", ale proaktywne "ten wzorzec sugeruje, że za tydzień możemy mieć problem z X". To naturalne rozwinięcie koncepcji AI które "myśli" – zamiast reagować na symptomy, analizuje przyczyny.

## Podsumowanie dla Zarządu

 Opisane kierunki są zgodne ze strategią rozwoju Astrafox i przynoszą wymierne korzyści biznesowe:

**Szybsze wdrożenia:**
- Vibe coding i generowanie procesów w języku naturalnym skracają czas konfiguracji systemu
- Mniej pracy konsultantów = niższy koszt wdrożenia dla klienta i krotszy Time-to-market

**Niższe koszty utrzymania:**
- Autodiagnostyka pozwala wykrywać problemy zanim eskalują
- Mniej interwencji supportu = niższe koszty operacyjne

**Wyższa skuteczność produktu:**
- Lepszy OCR = mniej ręcznych korekt = wyższe zadowolenie użytkowników
- Walidacja merytoryczna wyłapuje błędy, których tradycyjne reguły nie wykryją

**Zwiększona adopcja:**
- Interfejs w języku naturalnym obniża barierę wejścia dla użytkowników
- Raportowanie bez znajomości filtrów = więcej osób korzysta z systemu

**Zainteresowanie rynku:**
- Wielu klientów, szczególnie dużych, wykazuje aktywne zainteresowanie AI w AMODIT
- Funkcje AI stają się elementem przewagi konkurencyjnej w przetargach

**Wewnętrzna sprawność:**
- Już teraz intensywnie wykorzystujemy AI w sprzedaży, R&D i infrastrukturze
- To przekłada się na szybszą pracę i lepsze decyzje

Inwestycja w AI to nie eksperyment – to strategiczny kierunek, który już przynosi rezultaty.

## Co dalej?

**W najbliższym półroczu:**
- Testy pełnego OCR opartego na LLM (moze odejście od Document Intelligence)
- Rozwój Copilota: generowanie skryptów reguł, narzędzia (tools), MCP
- Raportowanie i filtrowanie w języku naturalnym, czyli dostep do danych z poziomu AMODIT Copilot i zwracanie wyników w formie raportu w oknie Copilot
- Pierwsze eksperymenty z autodiagnostyką

**Dla nas jako zespołu Astrafox:**

Zachęcam do ponownego przetestowania nowych modeli. To co widzieliście pół roku temu, to nie jest to samo co jest teraz. A za kolejne pół roku będzie jeszcze lepiej. Warto być na bieżąco, bo te narzędzia realnie przyspieszają pracę – jeśli wie się, jak z nich korzystać.

  