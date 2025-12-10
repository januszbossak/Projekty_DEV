> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-10

# Planowanie Sprintu – 2025-11-28

**Sprint:** 49
**Okres:** 2025-12-01 - 2025-12-12 (przybliżone)

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Status | Uwagi |
|-------|--------|-------|
| Edytor formularza – Prawy panel ustawień pola | ✅ Ukończone (częściowo) | Zmieniono nagłówek, zaokrąglenia, ikony. |
| Edytor formularza – Wyszukiwanie po atrybutach technicznych | ✅ Ukończone | Wyszukiwanie pól po ID, nazwie kolumny, GUID. |
| Edytor formularza – Zamykanie prawego panelu po zmianie kontekstu | 🔄 W testach / W trakcie | Problem z widokiem tabel/podformularzy w edytorze. |
| Integracja KSeF Connector – rozszerzenie API | ✅ Ukończone | Adrian dostarczył, Piotr zatwierdził. |
| Global Express | ✅ Ukończone (funkcje) | Łukasz Brodzkiego kończy dokumentację. |
| Comarch Hub | ➡️ Przeniesione | Łukasz Brodzkiego dopiero dziś dostał odpowiedzi, przeniesiono na kolejny sprint. |
| Moduł raportowy – Hotfixy (masowe akcje, scroll) | 🔄 W testach / W trakcie | Damian przejął zadanie. |
| Repozytorium plików | ✅ Ukończone (min. MVP) | Backend w dużej mierze gotowy. |
| Link do nowej sprawy (brak uprawnień) | ➡️ Przeniesione | Kamil przejął, zidentyfikowano jako bug. |
| Błąd w parserze reguł | ✅ Ukończone | Piotr poprawił krytyczny błąd. |
| Wyświetlanie tabel w tabelach (CSS) | 🔄 W trakcie | Mariusz pracuje nad poprawką. |
| Problemy z publish | 🔄 W trakcie | Mariusz bada problem. |
| Sprawa z Lewiatanem (podpis) | 🔍 Do weryfikacji | Piotr bada problem konfliktu bibliotek. |
| GUS integracja – PKD | ✅ Ukończone | Adrian wycenił i dostarczył. |
| KSeF konto | 🔍 Do weryfikacji | Czeka na zatwierdzenie. |
| SignApp – ikona | ✅ Ukończone | Adrian dodał. |
| Proxy dla funkcji `AMODIT.com` | 🔍 Do weryfikacji | Lukasz Bott do dalszego wyjaśnienia. |

---

## 2. Plany na sprint (2025-12-01 - 2025-12-12)

### Repozytorium plików

**Kontekst i cel:**
Dostarczenie funkcjonalności repozytorium plików do klienta do końca sprintu. Jest to kluczowy projekt.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Frontend – wdrożenie endpointów | **Filip** | | Testy Ani, backend |
| Frontend – poprawki wizualne (tabelki, kafelki) | **Filip** | | Po wdrożeniu endpointów |
| Historia zmian (audyt trail) | **Adrian** | | |

**Szczegóły techniczne:**
- Celujemy w wdrożenie grudniowej wersji funkcjonalności repozytorium.
- Skupiamy się na minimalnym MVP, aby dowieźć do klienta.

---

### Moduł raportowy – rozszerzenie okna dialogowego dla akcji masowych

**Kontekst i cel:**
Umożliwienie interaktywnego zbierania danych od użytkownika podczas masowego uruchamiania reguł z poziomu raportu. Jest to kluczowe dla funkcjonalności takich jak masowe przesunięcie terminu o N dni lub masowe podpisywanie.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| **MVP 0:** Umożliwienie działania funkcji `Wykonaj przed wykonaniem reguły` w akcjach masowych z raportu (obsługa istniejących typów: Użytkownik, Komentarz) | **Kamil** | | Zapewnienie, że okno z pierwszej sprawy zbiera dane i automatycznie przekazuje do wszystkich pozostałych |
| **MVP 1:** Rozszerzenie `Wykonaj przed wykonaniem reguły` o nowe typy pól (liczbowe, data, lista wyboru) | (do wyceny) | | |
| Definicja pól zbierania danych na poziomie raportu (alternatywna koncepcja) | (do wyceny) | | Decyzja Piotra Buczkowskiego |

**Decyzje podjęte przy planowaniu:**
- Pierwsze okno dialogowe z danymi z pierwszej sprawy będzie wyświetlane i jego wartości będą używane dla wszystkich kolejnych spraw w masowej akcji.
- Błędy wykonania reguły muszą być obsługiwane i wyświetlane (np. czerwony wiersz).
- Reguły z warunkiem `Wykonaj przed wykonaniem reguły` powinny być domyślnie ukryte w opcjach akcji masowych, chyba że są specjalnie oznaczone jako kompatybilne.
- Konieczność walidacji kontekstu (czy wszystkie sprawy mają ten sam kontekst dla okna dialogowego).

**Szczegóły techniczne:**
- Istniejąca funkcja `Wykonaj przed wykonaniem reguły` zostanie rozszerzona.
- Dyskusja o uniwersalności (pole tekstowe, numeryczne, data, lista wyboru) vs. specyficzne rozwiązania.

**Ryzyka:**
- Niespójność działania w różnych kontekstach.
- Zbyt duża złożoność funkcji "Execute before rule" w kontekście masowym.

---

### Edytor formularza – porządek w polu typu Tabela

**Kontekst i cel:**
Uporządkowanie wyglądu i działania pola typu Tabela oraz zagnieżdżonych tabel, w tym scrolli, marginesów i spójności wizualnej.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Ujednolicenie wyglądu i działania tabel | **Przemek Rogaś** | | |
| Poprawki scrolli (pionowy/poziomy) | **Kamil** | | |
| Marginesy i spójność wizualna | **Kamil** | | |
| Wygląd zagnieżdżonych tabel (tła, nagłówki) | **Kamil** | | |

**Decyzje podjęte przy planowaniu:**
- To zadanie jest priorytetem na przyszły sprint.

---

### Inne tematy / Plany krótkoterminowe

| Temat | Osoba | Cel/Uwagi |
|---|---|---|
| Koncepcja proxy (Bank Pekao) | **Adrian**, **Damian**, **Lukasz Bott** | Badanie i propozycja rozwiązania dla obsługi proxy w modułach AMODIT. |
| Testowanie środowiska baz danych (AMODIT.com) | **Michal Zwierzchowski**, **Lukasz Brocki** | Ukończenie planu aktualizacji baz danych i środowiska testowego. |
| Comarch Hub | **Łukasz Brodzkiego** | Przeniesiono na przyszły sprint. |
| Global Express | **Łukasz Brodzkiego** | Kończy funkcje, następnie dokumentacja i testy. |
| SM Integracja (firma kurierska) | **Łukasz Brodzkiego** | Do zrobienia przez analogię. |
| Kushina (OAuth2 dla Coloristica) | **Janusz**, **Ania** | Wycena wymaga poprawy. Rozważyć dwie opcje: tylko OAuth2 dla Coloristica lub pełna integracja z Envelope/Datacom. |

---

## 3. Decyzje architektoniczne (ad-hoc)

- **Zmiana struktury Daily:** Zamiast opowiadać o indywidualnych zadaniach, Daily będzie skupiać się na postępach w kluczowych projektach (np. Repozytorium, Moduł raportowy).
- **Kolorystyka w menu głównym:** Ikony menu głównego (systemowe) pozostają szare. Foldery/pliki w głównej części widoku mogą być kolorowe.
- **Brak Piotra:** Przez następny tydzień brak instalacji i aktualizacji AMODIT, aby uniknąć problemów bez bieżącego monitoringu Piotra. Adrian lub Mateusz jako zastępstwo w nagłych przypadkach.

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Kontekst | Wpływ | Mitygacja | Właściciel |
|---------------|----------|-------|-----------|------------|
| Brak konta KSeF | KSeF Connector | Zatrzymanie testów i wdrożenia | Dopytać Przemka o status | **Adrian** |
| Problemy z podpisem w Orlenie | Lewiatan | Brak możliwości podpisywania | Badanie problemu (konflikt bibliotek GdPicture/ITX, proxy) | **Piotr** |
| Niezdefiniowane wymagania dla PI | Nowe zgłoszenia | Wydłużony czas realizacji, błędne wdrożenia | Edukacja nowych członków zespołu w zakresie precyzyjnego opisu wymagań. Zapewnienie edytowalności PI dla PM/Analityków. | **Lukasz Bott** |
| Niespójność ścieżek w bazie transkrypcji | Wewnętrzny | Problemy z przetwarzaniem transkrypcji przez agentów | Weryfikacja i poprawa skryptów dodających pliki do bazy. | **Agent Gemini** |

---

## 5. Organizacja pracy

- **Urlopy:** Piotr Buczkowski nieobecny przez następny tydzień.
- **Zmiany w harmonogramie:** Spotkanie "Design" może być przesunięte. Planowanie sprintu na 12:00.
- **Mateusz Kołakowski:** Obecnie na uczelni, ograniczona komunikacja. Prawdopodobnie będzie dostępny po 12.
- **Wyceny:** Tematy wyceny "Kushina" i "rozszerzenie okna dialogowego" do ponownej analizy i aktualizacji estymacji.

---

## Powiązane projekty

- `Klienci/WIM/Repozytorium-plikow-DMS`
- `Moduly/Modul-raportowy/Masowe-akcje`
- `Moduly/Edytor-procesow`
- `Moduly/Ustawienia-systemowe`
- `Klienci/Lewiatan/Comarch-HUB`
- `Klienci/LOT/Integracja-Global-Express`
- `cross-cutting/Design-System`
- `Organizacja-DEV/Dokumentacja-organizacyjna`
- `Organizacja-DEV/Automatyzacja-dokumentacji-AI`

