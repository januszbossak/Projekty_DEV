# Rada Developerów – 2025-12-02

**Tematy:**
- Limity REST API i pobieranie danych hurtowo
- Zachowanie filtrów i akcji masowych w raportach

---

## 1. Limity REST API i pobieranie danych hurtowo z raportów

### Kontekst i Problem

Klient Ellie Stage (oraz wcześniej inni klienci) zgłaszają potrzebę pobierania dużych wolumenów danych z raportów AMODIT przez REST API. Problem polega na tym, że obecna architektura REST API nie jest przygotowana wydajnościowo na obsługę masowych zapytań. Klienci strzelają co minutę zapytaniem o raport zawierający np. 100 000 pozycji, co znacząco obciąża AMODIT na chmurze. Na roadmapie w Q2 jest wpis dot. standardu Open Data (wyciąganie danych do Tableau/BI), który należałoby przyspieszyć do Q1. Obecnie nie ma endpointa pozwalającego na hurtowe pobranie danych z raportu - brakuje koncepcji asynchronicznego generowania raportu, zapisu wyników i przekazania całej paczki danych.

### Zidentyfikowane Ryzyka

- Rosnące obciążenie chmury przez klientów wykonujących masowe zapytania REST API (przykład: klient pobierający "milion danych" i obciążający infrastrukturę)
- Wprowadzenie limitów może być odebrane negatywnie przez klientów, którzy już korzystają z API bez ograniczeń
- Brak wiedzy o faktycznej skali problemu - ile klientów faktycznie wykonuje takie zapytania i jaki jest wolumen
- Możliwe problemy z usługami zewnętrznymi (Trust Center) - klienci mogą tam również strzelać bezpośrednio

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wprowadzenie limitów zapytań (rate limiting) | Limity godzinne, minutowe, dzienne na wywołania REST API z mechanizmem HTTP 429 (przekroczony limit) | 💡 Propozycja - wymaga najpierw analizy skali problemu |
| Model licencyjny z płatnymi progami | Np. 10 000 lub milion zapytań miesięcznie w podstawowej licencji, więcej = wyższa licencja (wzór z rynku: 1000 zł → 15 000 zł za większą skalę) | 💡 Propozycja - rozważane jako długofalowe rozwiązanie biznesowe |
| Endpoint do asynchronicznego pobierania raportu | Wywołanie endpointa → raport generuje się po stronie AMODIT → wyniki zapisywane gdzieś → cała paczka przekazana klientowi (mechanizm kolejkowania) | 💡 Propozycja - wymaga całej koncepcji (obecnie nie istnieje) |
| Przyspieszenie wdrożenia standardu Open Data do Q1 | Standard Open Data dla Tableau/Power BI zaplanowany na Q2 przesunąć na Q1 | 💡 Propozycja - zmniejszy obciążenie przez eliminację wielokrotnych requestów typu "podaj dane z tej sprawy" × 100 000 |

### Decyzja

**Status:** 🔍 Do weryfikacji

Zanim podejmą się decyzje o limitach lub rozwiązaniach technicznych, konieczna jest analiza faktycznej skali problemu. Należy zbadać:
- Kto faktycznie wykorzystuje REST API do masowych zapytań (lista klientów)
- Jaki jest wolumen zapytań (skrajne przypadki)
- Czy dotyczy to jednego klienta czy szerszej grupy
- Jakie limity byłyby adekwatne

Monitoring ruchu można przeprowadzić przez Azure Monitor (rejestruje ruch wchodzący i wychodzący).

**Koncepcja rozwiązania dla Ellie Stage:** Tymczasowe obejście z dedykowanym endpointem lub kolejkowanie na chmurze - do zgłębienia po analizie skali.

### Zadania

- **Łukasz Poskrobko:** Przygotowanie zestawienia klientów wykorzystujących REST API do masowych połączeń (lista + statystyki wywołań zewnętrznych)
- **Adrian Kotowski:** Weryfikacja możliwości zbadania ruchu przez Azure Monitor (wchodzący vs wychodzący, filtrowanie po witrynach)
- **Damian Kaminski:** Zapoznanie się z tematem zgłoszenia Ellie Stage (kanał z klientem)
- **Zespół:** Analiza skali problemu po otrzymaniu statystyk → termin: przed powrotem Piotra

### Punkty otwarte

- Czy limity zapytań REST API są technicznie możliwe do wdrożenia na obecnej architekturze? (pytanie do Piotra)
- Jak zakomunikować klientom wprowadzenie limitów bez negatywnego odbioru?
- Jaka powinna być strategia migracji - czy stopniowe wprowadzanie limitów tylko dla nowych klientów?
- Czy system Trust Center również wymaga limitów zapytań?
- Jak dokładnie ma działać endpoint do asynchronicznego pobierania raportu? (brak koncepcji)

---

## 2. Zachowanie filtrów i akcji masowych w raportach (issue #22411)

### Kontekst i Problem

Zgłoszenie #22411 (prawdopodobnie LPP) dotyczy zachowania filtrów w raportach po wykonaniu akcji masowych. Janusz zaproponował rozwiązanie cząstkowe dotyczące tylko filtrów lewych (drzewko), ale brak kontekstu dla filtrów górnych. Problem polega na niespójności zachowania systemu po wykonaniu operacji masowych (podpisywanie z akcją, wykonanie reguły, akcje masowe). Obecnie: po podpisaniu z akcją wyświetla się popup "czy odświeżyć raport?", ale po samym wykonaniu akcji masowej takiego okienka nie ma. Gdy na raporcie zaznaczona jest pozycja w drzewie filtrów (lewy panel) i po wykonaniu akcji masowej wszystkie sprawy z tej pozycji znikają (np. zostały przeniesione do innego stanu), system traci kontekst - użytkownik nie wie, co się stało z jego sprawami.

### Zidentyfikowane Ryzyka

- Utrata orientacji użytkownika - po wykonaniu akcji masowej sprawy znikają z ekranu bez możliwości zobaczenia co się zmieniło
- Brak możliwości "Cofnij" dla akcji masowej - użytkownik nie może anulować błędnej operacji
- Niespójność UI - różne zachowanie dla podpisywania z akcją vs samo wykonanie akcji masowej
- Edge case: kombinacja filtra drzewkowego (lewy panel) + filtr górny - jeśli w połączeniu nie ma nic do pokazania, system może się zachować nieprzewidywalnie

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Przeniesienie zaznaczenia do najbliższego rodzica (tylko filtry lewe) | Gdy z drzewka znikają wszystkie pozycje, system automatycznie przenosi zaznaczenie w drzewie do najbliższego rodzica i wyświetla sprawy odpowiadające temu nowemu zaznaczeniu | ⏸️ Odroczona - to rozwiązanie cząstkowe, nie uwzględnia filtrów górnych ani edge case'ów |
| Pozostawienie stanu po akcji masowej bez odświeżania | Po wykonaniu akcji masowej (podpisywanie, reguły) rekordy aktualizują się inline (np. kolorem na zielono), zmiany w kolumnach są widoczne (data przekazania, stan), ale raport się nie odświeża automatycznie. Użytkownik widzi co się zmieniło. Dopiero "Odśwież" przebudowuje raport i stosuje filtry. | ✅ Zatwierdzone (koncepcja Janusza) - długofalowa wizja |
| Ekran podsumowania po każdej akcji masowej | Wyświetlenie ekranu podsumowania z pytaniem "Zamknij" vs "Zamknij i odśwież" dla wszystkich akcji masowych (nie tylko podpisywanie z akcją) | 💡 Propozycja - wymaga uspójnienia zachowania dla wszystkich typów akcji masowych |
| Poprawka "Wyczyść wszystkie" dla pustego filtru | Obecnie jeśli filtr ustawiony domyślnie "nie zawiera" (ale bez wartości), to "Wyczyść wszystkie" powoduje zniknięcie rekordów mimo że faktycznie filtr nie był ustawiony | ✅ Zatwierdzone - niepożądany skutek do naprawy |

### Decyzja

**Status:** 💡 Propozycja (wymaga akceptacji zespołu i Piotra)

**Wizja Janusza (długofalowa):**

Akcja masowa (podpisywanie, wykonywanie reguł, indeksacja) NIE powinna zmieniać kontekstu raportu. Po wykonaniu:
1. Pojedyncze rekordy aktualizują się inline (np. zielony kolor oznaczający sukces)
2. Zmiany w kolumnach widoczne natychmiast (data przekazania, stan) - nawet jeśli nowe wartości nie pasują do aktywnych filtrów
3. Sprawy pozostają na ekranie - użytkownik widzi co się zmieniło
4. Użytkownik może przejrzeć stronę, ocenić rezultat, zrobić screenshot jeśli coś poszło źle
5. Dopiero kliknięcie "Odśwież" lub zmiana filtru → pełne odświeżenie raportu, stosowanie filtrów, znikanie spraw

**Uspójnienie zachowania:**
- "Zamknij" → powrót do raportu z widocznymi zmianami (sprawy pozostają)
- "Zamknij i odśwież" → pełne odświeżenie, sprawy znikają zgodnie z filtrami
- Bez znaczenia czy to podpisywanie z akcją, bez akcji czy sama akcja masowa

**Kolejność implementacji (propozycja Damiana):**
1. Najpierw naprawić zachowanie filtra lewego (drzewko) - przeniesienie do rodzica gdy pozycja znika
2. Rozwiązać edge case: drzewko + filtr górny (co się dzieje gdy w połączeniu nie ma co pokazać?)
3. Dopiero potem dołożyć popup dla akcji masowych ("Zamknij" / "Zamknij i odświeżyć")

**Acceptance criteria:** Do dopisania przez Damiana w #22411.

### Zadania

- **Damian Kaminski:** Dopisanie acceptance criteria do #22411
- **Damian Kaminski:** Przegląd implementacji i weryfikacja edge case'ów (drzewko + filtry górne)
- **Zespół:** Przygotowanie przypadku testowego dla kombinacji filtrów (drzewko + górne) przed implementacją

### Punkty otwarte

- Co dokładnie powinno się wydarzyć gdy po wykonaniu akcji masowej w połączeniu filtra drzewkowego i górnego nie ma nic do pokazania?
- Czy możliwa jest implementacja "Cofnij" dla akcji masowych? (obecnie nie ma takiej opcji)
- Czy rozwiązanie Janusza (pozostawienie zmian bez odświeżania) jest kompatybilne z obecną architekturą raportów?
- Kiedy dokładnie odświeżają się filtry lewe (drzewko) - po każdej akcji czy tylko po "Odśwież"?

---

## 3. Błąd #22816 - Brak połączenia do bazy danych przy API

### Kontekst i Problem

Issue #22816 dotyczy sporadycznego błędu w API - z jakiegoś powodu przy wywołaniu REST API nie ma połączenia do bazy danych. Błąd pojawia się raz na jakiś czas (nieregularnie), poza tym API działa normalnie. Brak Piotra na spotkaniu uniemożliwił dogłębną analizę.

### Zidentyfikowane Ryzyka

- Negatywne komunikaty dla biznesu - klienci mogą doświadczyć błędów w integracjach
- Trudność w diagnozie - błąd sporadyczny, może już nie występować w momencie analizy

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ⏸️ Odroczone (oczekiwanie na informacje od klienta/supportu)

Issue #22816 przekierowany do Jarka z prośbą o więcej informacji. Status: `waiting for information`. Jeśli błąd już nie występuje lub jest przejściowy, prawdopodobnie nie będzie wymagał dalszych działań ("po ptakach").

### Zadania

- **Damian Kaminski:** Wysłanie zapytania do Jarka bezpośrednio o szczegóły błędu #22816
- **Zespół:** Zmiana statusu w Azure DevOps na `waiting for information` (bez zmiany assignee z Piotrka na Jarka)

### Punkty otwarte

- Czy błąd nadal występuje u klienta?
- Jakie są dokładne warunki reprodukcji błędu?
- Czy błąd dotyczy konkretnego endpointa API czy występuje losowo?
- Czy problem związany jest z architekturą connection pooling na serwerze?
