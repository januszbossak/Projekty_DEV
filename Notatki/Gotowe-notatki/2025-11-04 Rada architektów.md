# Rada Architektów – 2025-11-04

**Powiązane projekty:**
- `moduly/Trust-Center` – tematy 1, 2
- `moduly/Copilot-Baza-wiedzy-AI` – tematy 3, 4
- `cross-cutting/System-mailowy` – temat 5
- `cross-cutting/Szablony-maili-systemowych` – temat 6
- `moduly/Modul-raportowy` – temat 7
- `moduly/Ustawienia-systemowe` – temat 8

---

## 1. Problem z niespójnością statusów dokumentów w Trust Center

**Projekt:** `moduly/Trust-Center`

### Kontekst i Problem

W Trust Center pojawiają się dokumenty, których status nie zgadza się z etapem w procesie podpisywania. Wszystkie procesy są zgłoszone, nie jest to oddzielny tryb podpisywania. Problem polega na tym, że wszystkie osoby podpisały dokument, ale dokument nie został dodany do blockchaina, ponieważ status nie zmienił się na "1" albo zmienił się i potem z powrotem ustawił na "0". Możliwe przyczyny to problemy na Azure z dostępem do bazy danych (niektóre daty zgadzały się z awariami) lub skrajne przypadki, których nie uwzględniono. Problem występuje sporadycznie – przez prawie miesiąc po dodaniu dodatkowego logowania nic się nie działo, dopiero parę dni temu zdarzył się jeden przypadek. Przykład: dokument wisiał od lipca, dopiero teraz ktoś się o to upomniał.

### Zidentyfikowane Ryzyka

- Dokumenty mogą wisieć w nieskończoność bez zakończenia procesu podpisywania
- Brak automatycznego wykrywania i naprawy takich przypadków
- Możliwe problemy z dostępem do bazy danych mogą powodować niespójność statusów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ręczna weryfikacja w panelu administracyjnym | Osoba wchodząca do panelu mogłaby zweryfikować poprawność statusu i kliknąć guzik do poprawy | ❌ Odrzucona – nie jest profesjonalnym rozwiązaniem, to jest łatanie |
| Automatyczny job raz na miesiąc | Job skanujący dokumenty raz na miesiąc i weryfikujący statusy | ⏸️ Odroczona – zbyt rzadko, dokumenty nie mogą leżeć miesiąc |
| Automatyczny job raz dziennie | Job skanujący dokumenty raz dziennie (w nocy) i automatycznie poprawiający statusy | ✅ Wybrana – rozwiązuje problem systematycznie |
| Wywołanie ręczne przez administratora | Funkcja `TrustCenter_CheckStatus` lub `TrustCenter_FinishSigning` do ręcznego wymuszenia zakończenia procesu | ✅ Wybrana – dla przypadków krytycznych |
| Automatyczne sprawdzenie po 10-15 minutach | Po każdym podpisaniu tworzyłaby się kolejka, którą job obsługuje i po 15 minutach sprawdza, czy blockchain się wygenerował | ⏸️ Odroczona – obawy o obciążenie bazy danych |

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzone zostaną dwa mechanizmy równoległe:
1. **Job automatyczny** – będzie wykonywany codziennie w godzinach wieczornych, skanując dokumenty pod kątem niespójności statusów i automatycznie poprawiając je (wymuszając zakończenie procesu podpisywania).
2. **Wywołanie ręczne** – funkcja `TrustCenter_FinishSigning` (lub `TrustCenter_CheckStatus` z aktywnym sprawdzaniem) będzie dostępna dla administratorów dokumentów w AMODIT, umożliwiając wymuszenie zakończenia procesu dla przypadków krytycznych.

Dla klientów używających Trust Center poza monolitem (bezpośrednio przez REST API) – mogą skorzystać z endpointu `Finishing`, ale muszą się sami zabezpieczyć. Warunki użycia powinny być wpisane w ogólnych warunkach użytkowania AI OCR.

**Szczegóły techniczne:**
- Funkcja w regułach: `TrustCenter_FinishSigning`
- Endpoint: `Finishing`
- Kwerenda do wyszukiwania błędnych spraw już istnieje (Marek)

### Zadania

- **[Marek Dziakowski]:** Opisać scenariusz użycia funkcji `TrustCenter_FinishSigning` na Wiki oraz przygotować kącik szkoleniowy dla wdrożeniowców na piątkowych spotkaniach → termin: do następnej rady
- **[Marek Dziakowski]:** Zaprojektować i zaimplementować job automatyczny skanujący dokumenty raz dziennie w godzinach wieczornych i poprawiający niespójne statusy
- **[Marek Dziakowski]:** Sprawdzić możliwość wysłania dokumentu do Trust Center na czas nieokreślony oraz czy istnieje mechanizm wygaszania dokumentów po określonym czasie (np. pół roku) → termin: do następnej rady (temat poruszony przez Damiana Kaminskiego)

### Punkty otwarte

- Dokładna przyczyna problemu – czy to problemy z dostępem do bazy danych, czy skrajne przypadki nieuwzględnione w logice
- Czy potrzebne jest narzędzie do monitorowania dokumentów wiszących dłużej niż np. 5 dni (pomysł Łukasza Bott) – wymaga dalszej analizy

---

## 2. Mechanizm wygaszania dokumentów w Trust Center

**Projekt:** `moduly/Trust-Center`

### Kontekst i Problem

Czy istnieje możliwość wysłania dokumentu do Trust Center na czas nieokreślony? Czy można wysłać dokument, który będzie wisiał 10 lat? Trzymanie dokumentów w nieskończoność nie ma sensu biznesowego. Jeśli termin podpisania nie jest określony, czy powinien być wprowadzony mechanizm automatycznego wygaszania dokumentów po określonym czasie (np. pół roku).

### Zidentyfikowane Ryzyka

- Dokumenty mogą wisieć w Trust Center w nieskończoność bez sensu biznesowego
- Brak jasnych ram czasowych dla dokumentów bez określonego terminu podpisania

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Marek Dziakowski ma sprawdzić, czy istnieje możliwość wysłania dokumentu do Trust Center na czas nieokreślony oraz czy jest już zaopiekowany mechanizm wygaszania dokumentów. Jeśli nie, trzeba będzie zdefiniować sensowne ramy biznesowe (np. pół roku) i zrobić wpis na Wiki, że nie będziemy trzymać dokumentów w nieskończoność.

### Zadania

- **[Marek Dziakowski]:** Sprawdzić możliwość wysłania dokumentu do Trust Center na czas nieokreślony oraz czy istnieje mechanizm wygaszania → termin: do następnej rady

### Punkty otwarte

- Jakie są sensowne ramy biznesowe dla dokumentów bez określonego terminu podpisania?

---

## 3. Moduł dla usług AI i kwestie RODO

**Projekt:** `moduly/Copilot-Baza-wiedzy-AI`

### Kontekst i Problem

Mateusz dorobił moduł dla usług AI, normalizując to, co jest przetwarzane. Okazało się, że może to zahaczać o RODO. Temat wymaga omówienia z Mateuszem na dedykowanym spotkaniu, ponieważ są zadania po stronie serwisu bilingowego i samego AMODIT.

### Zidentyfikowane Ryzyka

- Możliwe problemy z RODO związane z przetwarzaniem danych w module AI
- Potrzeba weryfikacji zgodności z przepisami o ochronie danych

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Temat został wstępnie omówiony wczoraj z Januszem i Mateuszem. Powstały z tego konkluzje, które trzeba spisać i pochylić się nad tym na dedykowanym spotkaniu. Trzeba to rozpiąć na PBI.

### Zadania

- **[Damian Kaminski]:** Spisać konkluzje z wstępnej rozmowy i rozpiąć na PBI z zadaniami po stronie serwisu bilingowego i AMODIT

### Punkty otwarte

- Jakie konkretnie kwestie RODO wymagają rozwiązania?
- Jakie zadania są potrzebne po stronie serwisu bilingowego i AMODIT?

---

## 4. Zapobieganie wysyłaniu tych samych plików do AI OCR

**Projekt:** `moduly/Copilot-Baza-wiedzy-AI`

### Kontekst i Problem

Problem polega na tym, że te same pliki mogą być wysyłane wielokrotnie do AI OCR, co powoduje niepotrzebne koszty. Przykład: ten sam dokument był wysyłany wielokrotnie z reguły okresowej co minutę przez cały weekend, co kosztowało około 20 000 zł. Obecnie istnieje parametr `force`, który musi być ustawiony, żeby ponownie się dokument OCR-ował. Jeśli parametru `force` nie ma, system wie, że już taki dokument był i drugi raz go nie robi. Problem: w regułach ręcznych parametr `force` jest dodawany domyślnie, ale w regułach automatycznych nie jest dodawany. Drugi przypadek: zakładanie sprawy z maila – ten sam mail może co 5 minut powodować założenie nowej sprawy z tym samym dokumentem (problem z zaznaczaniem maila jako odczytanego).

### Zidentyfikowane Ryzyka

- Duże koszty związane z wielokrotnym przetwarzaniem tych samych dokumentów
- Możliwość zapętlenia w regułach okresowych wysyłających te same dokumenty
- Problem z zakładaniem duplikatów spraw z tego samego maila/pliku

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zabezpieczenie tylko po stronie AMODIT | AMODIT sam zaopiekuje się dodawaniem lub niedodawaniem `force` w zależności od typu reguły | ⏸️ Odroczona – niewystarczające zabezpieczenie |
| Zabezpieczenie tylko po stronie OCR | OCR przechowuje listę hashy przetworzonych plików i zwraca błąd przy duplikacie | ⏸️ Odroczona – niewystarczające zabezpieczenie |
| Zabezpieczenie po obu stronach | AMODIT zarządza parametrem `force` (dodaje do ręcznych, usuwa z automatycznych), OCR sprawdza hash i zwraca błąd przy duplikacie bez `force` | ✅ Wybrana – podwójne zabezpieczenie |

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzone zostaną zabezpieczenia po obu stronach:
1. **Po stronie AMODIT:** Parametr `force` będzie automatycznie kasowany z reguł okresowych i dodawany do reguł ręcznych. To zapewni, że reguły okresowe nie będą wysyłały tych samych dokumentów wielokrotnie.
2. **Po stronie OCR:** OCR będzie przechowywać listę hashy przetworzonych plików w zaindeksowanej tabeli. Przychodzi dokument, wyliczamy hash, sprawdzamy czy jest w tabeli. Jeśli jest i nie ma parametru `force`, zwracamy błąd że duplikat. Jeśli nie ma w tabeli lub jest `force`, przyjmujemy do przetworzenia.

Dla klientów korzystających bezpośrednio z REST API mikroserwisu OCR (poza AMODIT) – powinna być dokumentacja, że reguły cykliczne nie mogą wysyłać parametru `force`. Jeśli ktoś wyśle, to jego odpowiedzialność. Warunki powinny być wpisane w ogólnych warunkach użytkowania AI OCR.

**Szczegóły techniczne:**
- Parametr: `force=true`
- Funkcja: `SendToOcr`
- Mechanizm: tabela z hashami przetworzonych dokumentów w mikroserwisie OCR

### Zadania

- **[Piotr Buczkowski]:** Zaimplementować mechanizm automatycznego kasowania parametru `force` z reguł okresowych i dodawania do reguł ręcznych po stronie AMODIT
- **[Piotr Buczkowski]:** Zaimplementować mechanizm sprawdzania hashy przetworzonych dokumentów po stronie OCR (tabela z hashami, sprawdzanie przy każdym wywołaniu, zwracanie błędu przy duplikacie bez `force`)
- **[Kamil Dubaniowski]:** Zweryfikować, czy w nowym `Skanuj` również działa mechanizm dodawania `force` do reguł ręcznych

### Punkty otwarte

- Jak obsłużyć duże pliki (np. 100 stron) – w `Skanuj OCR` był mechanizm ograniczenia liczby stron idących do OCR, jak to zrobić z nowym OCR? (pytanie Janusza) – wymaga dalszej analizy

---

## 5. Zapobieganie zakładaniu duplikatów spraw z maila/pliku

**Projekt:** `cross-cutting/System-mailowy`

### Kontekst i Problem

Problem polega na tym, że ten sam mail może powodować zakładanie wielu spraw z tym samym dokumentem (np. co 5 minut). Przyczyna: błąd komunikacyjny, gdzie niby ustawiamy mail jako odczytany, a on się nie zapisuje jako odczytany. Analogiczny problem może wystąpić przy zakładaniu spraw z pliku – jeśli nie ma uprawnień do zapisu na zasobie sieciowym, odczytujemy plik, nie możemy go skasować, znowu odczytujemy.

### Zidentyfikowane Ryzyka

- Duplikaty spraw zakładane z tego samego maila/pliku
- Niespójność danych w systemie
- Możliwe problemy z dostępem do zasobów sieciowych

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rozwiązanie tylko dla maili | Pośrednia tabela z ID maila, ID sprawy, status – sprawdzanie przed przetworzeniem | ✅ Wybrana – rozwiązuje problem dla maili |
| Rozwiązanie dla plików | Hash pliku + data modyfikacji + nazwa jako identyfikator | ✅ Wybrana – rozwiązuje problem dla plików |

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzone zostaną dwa mechanizmy:
1. **Dla maili:** Pośrednia tabela z ID maila (`Message-ID` jako unikalny GUID), ID sprawy utworzonej, status. Job pobiera nieodczytane maile, wczytuje mail, zapisuje w tabeli jego identyfikator, przetwarza, zaznacza że przetworzyliśmy. Przy ponownym wczytaniu maili sprawdzamy w tabeli, czy był już przetwarzany. Jeśli nie, przetwarzamy. W przypadku błędu połączenia, przy ponownym sprawdzaniu zostanie wykryte, że już go przetwarzaliśmy.
2. **Dla plików:** Hash pliku + data modyfikacji + nazwa jako identyfikator (`ScanID`). Jeśli plik ma taki sam hash i datę modyfikacji, nie zakładamy nowej sprawy.

**Szczegóły techniczne:**
- Dla maili: `Message-ID` jako unikalny identyfikator
- Dla plików: hash + data modyfikacji + nazwa

### Zadania

- **[Damian Kaminski]:** Rozpiąć na dwa odrębne zadania (PBI) z wyższym priorytetem
- **[Piotr Buczkowski]:** Zaimplementować mechanizm pośredniej tabeli dla maili z `Message-ID`, ID sprawy, status
- **[Piotr Buczkowski]:** Zaimplementować mechanizm sprawdzania hashy plików + data modyfikacji + nazwa dla plików

### Punkty otwarte

- Czy plik ma jakiś identyfikator w NTFS, który można wykorzystać? (pytanie Piotra)

---

## 6. Zmiana kategorii maili o zmianie na sprawie

**Projekt:** `cross-cutting/Szablony-maili-systemowych`

### Kontekst i Problem

Maile o edycji dokumentu, dodaniu komentarza są teraz traktowane jako powiadomienia główne, tak samo jak o przekazaniu sprawy. Propozycja z AmRest: żeby były traktowane jako dodatkowe, aby można było je wyłączyć w panelu użytkownika.

### Zidentyfikowane Ryzyka

- Użytkownicy mogą być przeciążeni powiadomieniami o mniej istotnych zmianach
- Brak elastyczności w konfiguracji powiadomień

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Szybka zmiana kategorii | Zmienić kategorię maili o zmianie na sprawie na dodatkowe | ⏸️ Odroczona – zbyt szybka zmiana, może być większa sprawa |
| Przemyślenie całego systemu powiadomień | Może trzeba więcej grup, może customowe zasady wysyłania powiadomień | 🔍 Do weryfikacji – wymaga analizy |

### Decyzja

**Status:** 🔍 Do weryfikacji

Janusz Bossak uważa, że to większa sprawa. Może trzeba więcej grup, może customowe zasady wysyłania powiadomień. To do przemyślenia, nie robiłbym szybkich zmian. Trzeba to spiąć i ustalić, co tam jest do zdefiniowania. Trzeba określić, co to jest "itd." i zrobić wpis na Wiki. Trzeba zaopiekować to całościowo i opublikować na głównej Wiki, żeby ktoś wiedział, na co ma wpływ zmiana ustawień w profilu.

**Szczegóły techniczne:**
- Tabela z konfiguracją powiadomień istnieje (Janusz przekazywał komuś, może jest na wewnętrznej Wiki)
- Artykuł na wewnętrznej Wiki może być lekko nieaktualny (tworzony z Rafałem lata temu)

### Zadania

- **[Damian Kaminski]:** Przeanalizować temat zmiany kategorii maili i całego systemu powiadomień, określić co to jest "itd." i zrobić wpis na Wiki
- **[Janusz Bossak]:** Sprawdzić i zweryfikować aktualność tabeli z konfiguracją powiadomień (może być na wewnętrznej Wiki)

### Punkty otwarte

- Jakie są wszystkie kategorie powiadomień i co można konfigurować w panelu użytkownika?
- Czy potrzebne są dodatkowe grupy powiadomień?
- Czy potrzebne są customowe zasady wysyłania powiadomień?

---

## 7. Problem z "zaznacz wszystko" w module raportowym

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

Funkcja "zaznacz wszystko" nie zaznacza wszystkiego. Przykład: na raporcie były 3 elementy, a wyświetlały się 2 z 3. Trzeba sprawdzić, na podstawie czego jest generowana ta lista.

### Zidentyfikowane Ryzyka

- Nieprawidłowe działanie funkcji "zaznacz wszystko" może powodować problemy użytkowników
- Możliwe problemy z generowaniem listy elementów w module raportowym

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Anna Skupinska ma sprawdzić temat. Trzeba sprawdzić, na podstawie czego jest generowana ta lista. Janusz pokazywał przykład, gdzie na raporcie były 3, a wyświetlały się 2 z 3. To jeden z wielu błędów w module raportowym.

### Zadania

- **[Anna Skupinska]:** Sprawdzić temat z "zaznacz wszystko" – na podstawie czego jest generowana lista → termin: do następnej rady

### Punkty otwarte

- Jaka jest dokładna przyczyna problemu z generowaniem listy?
- Czy są inne podobne problemy w module raportowym?

---

## 8. Mechanizm bezpiecznego zatrzymywania jobów w serwisie

**Projekt:** `moduly/Ustawienia-systemowe`

### Kontekst i Problem

W jobach wykonywanych przez serwis jest mechanizm, który sprawdza, czy serwis się nie zatrzymuje, i wtedy przerywa działanie. Mechanizm został zrobiony dla jobów, które istniały 2-3 lata temu. Przyszło wiele nowych jobów: do AI, do e-Nadawcy. Trzeba przejrzeć wszystkie joby, czy potrafią prawidłowo przerwać działanie. Chodzi o to, żeby przy zatrzymaniu usługi job potrafił się zatrzymać, był świadomy, że usługa się zatrzymuje. Jeśli ma do wykonania 100 zadań i jest po 5-6, to nie robi następnego, tylko kończy to, co robi i się przerywa bezpiecznie, żeby `kill` nie zatrzymał go w środku zadania, co może powodować niespójność danych.

### Zidentyfikowane Ryzyka

- Niespójność danych przy nieprawidłowym zatrzymaniu jobów
- Brak mechanizmu bezpiecznego zatrzymywania w nowych jobach (AI, e-Nadawca)
- Problem będzie ważny przy wprowadzeniu mechanizmu ograniczenia wydajności serwerów (np. serwisowych na czas, żeby oszczędzić pieniądze) – wymaga zatrzymania i restartu serwera

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ✅ Zatwierdzone

Trzeba przejrzeć wszystkie joby zarejestrowane w serwisie i sprawdzić, czy potrafią prawidłowo przerwać działanie. Mechanizm ma być zaimplementowany dla wszystkich jobów, które tego nie mają. Piotr Buczkowski ma przejrzeć, jakie joby są zarejestrowane i wypisać, które trzeba prześledzić.

### Zadania

- **[Piotr Buczkowski]:** Przejrzeć wszystkie joby zarejestrowane w serwisie i wypisać, które trzeba prześledzić pod kątem bezpiecznego zatrzymywania
- **[Piotr Buczkowski]:** Zgłosić ogólne PBI dla wszystkich jobów, a pod spodem PBI dla każdego joba osobno (będą przydzielane)

### Punkty otwarte

- Które konkretnie joby wymagają implementacji mechanizmu bezpiecznego zatrzymywania?

---

## 9. Wytyczne do repozytorium

**Projekt:** `moduly/Repozytorium-plikow-DMS`

### Kontekst i Problem

Piotr Buczkowski ma opisać wytyczne do repozytorium.

### Zidentyfikowane Ryzyka

Nie zidentyfikowano.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Piotr Buczkowski ma opisać wytyczne do repozytorium po spotkaniu.

### Zadania

- **[Piotr Buczkowski]:** Opisać wytyczne do repozytorium → termin: po spotkaniu

### Punkty otwarte

- Jakie konkretnie wytyczne mają być opisane?

---

## 10. Zgłoszenie "Nie wyszukuje spraw"

**Projekt:** Do sklasyfikowania

### Kontekst i Problem

Zgłoszenie dotyczące problemu z wyszukiwaniem spraw. Czekamy na odpowiedź. Tomek dostał wytyczne. W Rossmanie testowali naprawianie indeksu. Możliwe, że Kacper przez pomyłkę uruchomił `fix-index` na produkcji zamiast na kopii i naprawił.

### Zidentyfikowane Ryzyka

- Problem z wyszukiwaniem spraw może wpływać na funkcjonalność systemu
- Możliwe problemy z indeksem wyszukiwania

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Czekamy na odpowiedź. Tomek dostał wytyczne. Wiedza jest w dziale serwisu. W Rossmanie testowali naprawianie indeksu. Możliwe, że Kacper przez pomyłkę uruchomił `fix-index` na produkcji zamiast na kopii i naprawił.

### Zadania

- **[Tomek]:** Odpowiedzieć na zgłoszenie zgodnie z wytycznymi

### Punkty otwarte

- Jaka jest dokładna przyczyna problemu z wyszukiwaniem spraw?
- Czy problem został rozwiązany przez naprawienie indeksu?

