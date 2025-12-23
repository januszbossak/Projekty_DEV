**Data spotkania:** 15 grudnia 2025, 08:00

---

**Łukasz Bott:** Zaczynamy.

**Mariusz Piotrzkowski:** Cześć.

**Damian Kamiński:** To jest...

**Barbara Michałek:** Na coś czekamy jeszcze?

**Damian Kamiński:** Nie ma jeszcze Janusza.

**Kamil Dubaniowski:** Janusz i Przemek mówili, że ich nie będzie. Ja czekam bardziej na Marka, ale Damian, możesz zaczynać.

**Damian Kamiński:** Dobrze, zacznę od tematu repozytorium, nad którym pracowaliśmy z Anią, Filipem i Adrianem. W piątek napotkaliśmy błędy przy wdrażaniu części uprawnień, więc nie udało się tego skończyć. To kwestia dnia lub dwóch. Jeśli chodzi o strukturę, tworzenie i usuwanie węzłów, to wszystko już działa. Wprowadziliśmy usprawnienia UX – przy tworzeniu nowego folderu system automatycznie do niego przechodzi. Masowe wgrywanie plików (testowane na 40 plikach jednocześnie) działa sprawnie. Mamy trzy tryby widoku: kafelki, lista i lista kompaktowa, spójne z widokiem załączników na sprawach. Działa podgląd plików PDF i innych formatów obsługiwanych na sprawach. W tym tygodniu planujemy uruchomienie modułu u klienta on-premise w celach testów biznesowych.

**Anna Skupińska:** Udało mi się już utworzyć tabelę uprawnień w bazie danych.

**Damian Kamiński:** Filip musi to teraz podpiąć i zaczniemy testy. Dalsze prace obejmą licencjonowanie. Kamil, przejmujesz?

**Kamil Dubaniowski:** Tak. Zrealizowaliśmy temat JRWA dla LOT-u. W tym sprincie Marek (przy konsultacjach Piotra) przygotował MVP 2 – wyszukiwanie klas i opisów JRWA przez wpisywanie tekstu w polu. Dane o klasie są automatycznie roznoszone na pola formularza za pomocą reguł. To dedykowana funkcjonalność, która przyspiesza wdrożenia w standardzie EZD RP. Drugim elementem MVP 2 jest wybór z drzewa (tree select) prezentujący całą strukturę klas JRWA z bazy danych. Można wybrać odpowiednią klasę, co aktualizuje dane na formularzu. Zastępuje to skomplikowane słowniki i rejestry używane wcześniej. MVP 3 obejmie podpowiadanie 5-10 ostatnio używanych klas oraz wyszukiwarkę wewnątrz drzewa. Obecna wersja jest gotowa do instalacji u klienta.

**Piotr Buczkowski:** Czy interfejs, który proponowałem do implementacji, był wystarczający?

**Kamil Dubaniowski:** Marka jeszcze nie ma, dopytam go później. Założyliśmy, że zaplanował to zgodnie z Twoimi sugestiami. Teraz Przemek zaprezentuje zmiany w prawym panelu edytora.

**Przemysław Rogaś:** W ustawieniach pól i sekcji w prawym panelu zniknęło kilka sekcji. Zarządzanie uprawnieniami jest teraz pod ikonką. Dodaliśmy dropdown z historią pola w edytorze graficznym. Wartość domyślna i opcje widoczności zostały przeniesione. Kod techniczny (GUID) nie edytuje się już bezpośrednio w polu – trzeba kliknąć nową wartość i potwierdzić.

**Piotr Buczkowski:** Zmieniliście sposób wejścia do edycji reguły tabeli? Szukałem tego i to będzie problemem dla konsultantów po aktualizacji. Poprzednio było to bardziej intuicyjne.

**Kamil Dubaniowski:** Jest to teraz dostępne z poziomu listy. Musimus to przemyśleć. Nie chcemy przeładowywać interfejsu przyciskami. Prawy panel prawdopodobnie dostanie cień (shadow) lub zmianę koloru tła, żeby odróżnić go od formularza. Planujemy zrezygnować z sekcji na rzecz jednego spójnego panelu z nagłówkami, gdzie wszystkie właściwości będą od razu rozwinięte. Filip, możesz podsumować edytor reguł?

**Przemysław Rogaś:** Dodaliśmy też podsumowania do tabel dla pól numerycznych i kwotowych.

**Kamil Dubaniowski:** Tak, to zgłoszenie od serwisantów, już zrealizowane.

**Piotr Buczkowski:** Nazwy tabel w drzewie mogą być bardzo długie, sprawdźcie jak to wygląda.

**Kamil Dubaniowski:** Dlatego użyliśmy drzewa, żeby nie powtarzać całej ścieżki (np. "formularz główny > tabela 1 > tabela 2"). To oszczędza miejsce.

**Filip Liwiński:** Edytor reguł tabeli otwiera się teraz w oknie modalnym, a nie w nowej karcie. Poprawiliśmy brak możliwości zamknięcia okna.

**Piotr Buczkowski:** Okno powinno być większe. Pomoc zajmuje połowę ekranu.

**Filip Liwiński:** Możemy je powiększyć.

**Kamil Dubaniowski:** Dajmy maksymalny możliwy rozmiar. Docelowo będzie tam lista powiązanych reguł. Zmieniliśmy też nawigację – nie ma rozwijania zawartości tabeli na liście głównej, trzeba zmienić kontekst, wchodząc do tabeli (podobnie jak w starym edytorze). To rozwiązuje problem nieczytelności przy dużych zagnieżdżeniach. Zarówno w nawigacji górnej, jak i w prawym panelu, można przełączać się między poziomami zagnieżdżenia.

**Kamil Dubaniowski:** Z rzeczy, których nie udało się zrobić: nie powstał standard wyglądu tabel Ant Design i nie skończyliśmy porządków wizualnych na formularzu. Mariusz, co u Ciebie w temacie menu?

**Mariusz Piotrzkowski:** Zmieniłem wygląd przycisków w tabelach, kontury oraz odstępy między wierszami i kolumnami. Poprawiłem przycisk dodawania wierszy i dropdown obok. Są jeszcze drobne błędy do poprawki na testach.

**Kamil Dubaniowski:** Zmieniliśmy przycisk na "+ Dodaj". Wcześniej mały plusik w rogu był nieintuicyjny i wymagał dwóch kliknięć. Teraz dodawanie jest jednostopniowe. Zwiększyliśmy odstępy, żeby uniknąć przypadkowego kliknięcia przy używaniu scrolla. Chcemy też ujednolicić wygląd scrolli (grubość, kolor, efekt hover) w całej aplikacji, żeby użytkownik wiedział, że w nie trafił.

**Łukasz Bott:** Łukasz Brocki, powiedz o integracji z firmami kurierskimi dla LOT-u: Global Express i UPS.

**Łukasz Brocki:** Przygotowaliśmy funkcje reguł do tworzenia, anulowania i śledzenia przesyłek. Dla Global Express jest też zamawianie kuriera. Dokumentacja jest na Wiki. Nie ma jeszcze tego w licencji ani gotowych komponentów sekcji. To osobna biblioteka DLL-ka do wdrożenia u klienta.

**Marek Dziakowski:** Wyszukiwarkę JRWA z przycisku dodałem przez jedną nową funkcję i właściwość. Można to rozszerzyć na inne źródła w przyszłości.

**Damian Kamiński:** Mateusz, co z AI i Gemini?

**Mateusz Kisiel:** Pracowałem nad modelem Gemini i integracją z OCR dla Vasco. Można teraz przesyłać dokumenty do OCR w pełni przez serwery Google-owskie (bez Azure Document Intelligence). Model "AMODIT Invoice Gemini" wybiera się w regułach. LLM ma większe możliwości przy obsłudze specyficznych przypadków odczytu pozycji faktur niż dotychczasowe heurystyki Azure. Vasco już to testuje. Dodałem też opcję generowania obrazków przez Copilota (DALL-E 3 przez API OpenAI). Można np. wygenerować ikonę procesu.

**Łukasz Bott:** Czy Copilot obsługuje już inne formaty niż PDF?

**Mateusz Kisiel:** Na razie tylko PDF. Muszę dorobić obsługę Worda, Excela i plików tekstowych (np. CSV). Sporo czasu zajął kurs Copilota.

**Damian Kamiński:** Dzięki. Sprint był krótszy ze względu na szkolenia i nieobecności. Słyszymy się po południu.

**Łukasz Bott:** Cześć.

zatrzymano transkrypcję
