# Planowanie Sprintu – 2025-10-31

**Sprint:** [numer sprintu - do uzupełnienia]
**Okres:** [daty sprintu - do uzupełnienia]

**Powiązane projekty:**
- `moduly/Repozytorium-plikow-DMS` – tematy 1, 2
- `klienci/LOT/JRWA` – temat 3
- `cross-cutting/Wzmiankowanie-w-komentarzach` – temat 4
- `moduly/Ustawienia-systemowe` – temat 5
- `cross-cutting/Interfejs-sprawy` – temat 6
- `moduly/Edytor-procesow-formularzy` – tematy 7, 8
- `integracje/Comarch-Hub` – temat 9
- `moduly/e-Nadawca` – temat 10

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| Komunikator | `klienci/WIM/Komunikator` | 🔄 W trakcie | Mateusz ma pracę i przy komunikatorze, i przy repozytorium |
| Repozytorium - frontend | `moduly/Repozytorium-plikow-DMS` | 🔄 W trakcie | Filip już trochę frontendu zrobił |

---

## 2. Plany na sprint

### Repozytorium plików - architektura i struktura backendu

**Projekt:** `moduly/Repozytorium-plikow-DMS`

**Kontekst i cel:**
Damian Kaminski nie ma wystarczającej wiedzy technicznej, żeby dobrze zaprojektować backend dla repozytorium plików. Potrzebne jest wsparcie architektoniczne. Po 8 dniach sprintu powinna być rozkminiona architektura i struktura backendu - to będzie duży wkład. Nie dajemy jeszcze do robienia w rozumieniu pisania kodu, tylko niech się zastanowią porządnie.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Ustalenie architektury aplikacji (odrębna aplikacja vs część AMODIT, komunikacja z systemem AMODIT, użytkownicy, przechowywanie plików, mikroserwisy) | **Piotr** | - | Spotkanie z Damianem (30 minut) |
| Zaproponowanie struktury danych (tabele, kolumny, klucze, relacje) na podstawie założeń ilościowych | **Mateusz** | - | Czeka na architekturę od Piotra |
| Rozpisanie endpointów - jakie będą, do czego | **Mateusz** | - | Rozmowa z Filipem o potrzebach frontendu |
| Dokumentacja architektury - spisanie ustaleń ze spotkania | **Damian** | - | Po spotkaniu z Piotrem |

**Szczegóły techniczne:**
- Struktura folderowa
- Uprawnienia działające w kontekście działów (podobnie jak w JRWA)
- Przenoszenie plików
- Wykorzystanie GdPicture do generowania podglądów (zasobożerne)

**Decyzje podjęte przy planowaniu:**
- Piotr ma zająć się architekturą – jak to ma być zrobione, jaka komunikacja z użytkownikami, jak zapisywanie w folderach. Fundamenty, konstrukcja, a na tych założeniach Mateusz ma opracować backend.
- Damian daje ogólne założenia i wymagania biznesowe (poziom przypadków użycia), nie szczegóły techniczne.
- Spotkanie z Piotrem: nagrywanie, przejście przez transkrypcję, uzupełnienie dokumentacji. Piotr ma opowiadać, a Damian ma go podpytywać.
- Mateusz ma się mocno zaangażować, nawet po godzinach (rozlicza się godzinowo).

**Ryzyka:**
- Mateusz jest przeładowany (komunikator + repozytorium) - może nie starczyć czasu
- Nie ma co zakładać, że repozytorium wyprodukujemy w jeden sprint

---

### macOS

**Projekt:** `moduly/SignApp` (macOS)

**Kontekst i cel:**
Kamil ma projekt, Maca i Szafira do testów. Niezależnie od certyfikacji, powinniśmy dać klientowi do sprawdzenia.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Prace nad macOS | **Kamil** | - | - |
| Przekazanie do testów dla klienta | **Damian** | - | Po zakończeniu prac przez Kamila |

---

### KSeF

**Projekt:** `moduly/KSeF-Connector`

**Kontekst i cel:**
Adrian jest przeładowany (KSeF, macOS, Comarch Hub). Nierealne jest w 8 dni nawet minimalne MVP z tego złożyć. Trzeba okroić do tego, czego faktycznie potrzebujemy biznesowo, żeby nie "doktoryzował" się z konektora KSeF.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Rozpisanie co jest do zrobienia - okrojenie do potrzeb biznesowych | **Damian** + **Adrian** | - | Spotkanie, nagrywanie zeznań |

**Ryzyka:**
- Adrian przeładowany - KSeF, macOS, Comarch Hub - nierealne w 8 dni nawet minimalne MVP

---

### JRWA

**Projekt:** `klienci/LOT/JRWA`

**Kontekst i cel:**
Janusz rozpracowuje temat. Okazuje się, że nie jest tak, że każdy widzi całe JRWA. Nakłada się matryca kompetencji wynikająca ze struktury organizacji. Zgodnie z ochroną danych osobowych, ludzie powinni mieć dostęp do tej części JRWA, która ich dotyczy. Księgowy nie może sobie założyć teczki w radzie nadzorczej.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Ustalenie czy coś robimy z JRWA | **Janusz** | - | - |

**Szczegóły techniczne:**
- Uprawnienia w repozytorium oparte o przypisanie do działów (podobnie jak w JRWA)

---

### Wzmianki

**Projekt:** `cross-cutting/Wzmiankowanie-w-komentarzach`

**Kontekst i cel:**
Fala zgłoszeń odnośnie wzmianek. To kompletnie nie działa, jak powinno. Jest tego na tyle dużo, że najlepiej zrobić to od nowa. Po tym sprincie to ma działać i temat ma być rozwiązany, stabilny.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przebudowa wzmianek od nowa | **Mariusz** | 60% sprintu | - |
| Napisanie testów end-to-end | **Mariusz** | - | - |

**Decyzje podjęte przy planowaniu:**
- To jedyny cel, jaki powinien mieć Mariusz w tym sprincie
- Najlepiej jakby były do tego napisane testy end-to-end

---

### SignApp

**Projekt:** `moduly/SignApp`

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Prace nad SignApp | **Adrian** | - | - |

**Uwagi:**
- Zadanie już rozpisane

---

### 4-eyes w ustawieniach systemowych

**Projekt:** `moduly/Ustawienia-systemowe`

**Kontekst i cel:**
Zamknięcie tematu 4-eyes w ustawieniach systemowych, odtwarzając to, co było. Będzie potrzebny backend.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja 4-eyes w ustawieniach systemowych | **Ania** | - | - |

---

### Podgląd szablonów

**Projekt:** `cross-cutting/Interfejs-sprawy`

**Kontekst i cel:**
W Neuca ładują do każdej sprawy ten sam plik jako załącznik, co generuje tysiące (dziesiątki tysięcy) duplikatów. To jest totalny bezsens. Problem biznesowy: klienci mają pulę stałych dokumentów (instrukcje, regulaminy), które chcą wyświetlać na sprawach bez ich multiplikowania. Drugi aspekt to podgląd szablonu (np. umowa), gdzie po nazwie nie wiem, którą wersję zastosować. Podgląd pozwoli wybrać właściwy szablon, zanim go wyprodukuję.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja podglądu szablonów (backend i frontend) | **Ania** | 15 MD | - |

**Szczegóły techniczne:**
- Stworzenie podglądu szablonu jako JPG mogłoby być zasadne, bo szablonów jest mniej niż plików w repozytorium
- Możliwość generowania podglądu w momencie kliknięcia
- Powinno być "oczko" do podglądu - albo pobierasz, albo podglądasz

**Decyzje podjęte przy planowaniu:**
- Na razie podgląd szablonów tak, żeby zaopiekować ten problem
- Dokument do zapoznania się, stały regulamin – do tego mogłoby być repozytorium (w przyszłości)

---

### Edytor formularza - poprawa UX

**Projekt:** `moduly/Edytor-procesow-formularzy`

**Kontekst i cel:**
Skupić się na super dopracowaniu edytora formularza, żeby konsultanci się na niego przenieśli. Janusz wczoraj w 50% przypadków przełączał się na listę. Trzeba słuchać problemów, które zgłaszają nowi użytkownicy, jak Daniel, a niekoniecznie ich propozycji rozwiązań.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawa UX edytora formularza | **Przemek** | - | - |

**Szczegóły techniczne:**
- Szukanie po typie
- Zapamiętywanie ostatniej zakładki (temat Daniela)
- Zmiana ścieżki dodawania nowego pola
- Obsługa błędów przy edycji pól (zdublował nazwę, zmiana się nie zapisała i nie było informacji o błędzie) - leci do wersji czerwcowej
- Akcje masowe: usuwanie, przenoszenie między sekcjami (zaznaczenie kilku pól, prawy sidebar z menu kontekstowym "przenieś do sekcji")
- Drag and drop przy wielu elementach i długim formularzu będzie słaby

**Decyzje podjęte przy planowaniu:**
- Cel sprintu: poprawa UX edytora formularza
- Diagram na razie zostawiamy (MVP jest)
- Błędy i niedoróbki lecą do wersji czerwcowej. Zmiany koncepcji – do nowszych.

---

### Lista pól

**Projekt:** `moduly/Edytor-procesow-formularzy`

**Kontekst i cel:**
Sporo braków względem starej wersji. To jest naprawdę poziom MVP.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Uzupełnienie braków w liście pól (szybki odnośnik do słownika, ustawienia pola) | **Filip** | - | - |

---

### Matryca uprawnień

**Projekt:** `moduly/Edytor-procesow-formularzy`

**Kontekst i cel:**
Cały czas jest kwestia czytelności. Chciałbym to zaopiekować w przyszłym sprincie.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawa czytelności matrycy uprawnień | **Filip** | - | Przyszły sprint |

**Uwagi:**
- Miejmy na uwadze, że ten sprint zamyka paczkę grudniową, więc powinniśmy stabilizować wersję, a nie dorzucać nowe rzeczy

---

### Comarch Hub

**Projekt:** `integracje/Comarch-Hub`

**Kontekst i cel:**
Nowy temat. Adrian go rozkminia na poziomie koncepcyjnym. Może przekaże to Łukaszowi. Na razie jednak Łukasz jest na urlopie. Musimy poczekać do poniedziałku.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Rozkminienie na poziomie koncepcyjnym | **Adrian** | - | - |
| Przekazanie do implementacji | **Łukasz Brocki** | - | Po powrocie z urlopu (poniedziałek) |

**Ryzyka:**
- Adrian przeładowany - KSeF, macOS, Comarch Hub
- Pytanie: czy ten Comarch Hub musi robić Adrian?

---

### e-Nadawca - poprawki

**Projekt:** `moduly/e-Nadawca`

**Kontekst i cel:**
Poprawki w e-Nadawcy, które ma Adrian. Może przejąć Łukasz? Ktoś musi się też nauczyć e-Doręczeń.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawki w e-Nadawcy | **Łukasz Brocki** (potencjalnie) | - | Po powrocie z urlopu |
| Nauka e-Doręczeń | **Łukasz Brocki** | - | - |

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Piotr ma zająć się architekturą repozytorium (fundamenty, konstrukcja), Mateusz opracowuje backend na tych założeniach | `moduly/Repozytorium-plikow-DMS` | ✅ Zatwierdzone | Damian nie ma wystarczającej wiedzy technicznej, Piotr jako architekt systemowy ma wymyślać architekturę i pilnować jej spójności |
| Dokumentacja projektowa: projekt minimalnie składa się z trzech plików: 1. Uzasadnienie biznesowe, 2. Rozbicie na MVP, 3. Plik architektoniczno-techniczny | `cross-cutting/Automatyzacja-dokumentacji-AI` | ✅ Zatwierdzone | Potrzeba miejsca do przechowywania i edycji dokumentacji projektowej dostępnej dla wszystkich |
| Uprawnienia w repozytorium oparte o przypisanie do działów (podobnie jak w JRWA) | `moduly/Repozytorium-plikow-DMS` | ✅ Zatwierdzone | Zgodnie z ochroną danych osobowych, ludzie powinni mieć dostęp do tej części, która ich dotyczy |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Adrian przeładowany (KSeF, macOS, Comarch Hub) | `moduly/KSeF-Connector`, `moduly/SignApp`, `integracje/Comarch-Hub` | Wysoki | Okrojenie KSeF do potrzeb biznesowych, przekazanie Comarch Hub Łukaszowi po urlopie | **Damian**, **Adrian** |
| Mateusz przeładowany (komunikator + repozytorium) | `klienci/WIM/Komunikator`, `moduly/Repozytorium-plikow-DMS` | Wysoki | Mateusz ma się mocno zaangażować, nawet po godzinach (rozlicza się godzinowo) | **Mateusz** |
| Nie ma co zakładać, że repozytorium wyprodukujemy w jeden sprint | `moduly/Repozytorium-plikow-DMS` | Średni | Po 8 dniach powinna być rozkminiona architektura i struktura backendu - to będzie duży wkład | - |
| Łukasz na urlopie - nie można zaopiekować zadań | Różne | Średni | Poczekać do poniedziałku, wrócić żeby zaopiekować Łukasza i zamknąć plan | - |
| Ten sprint zamyka paczkę grudniową - powinna być stabilizacja, a nie nowe rzeczy | Różne | Średni | Miejmy na uwadze stabilizację wersji | - |

---

## 5. Organizacja pracy

- **Urlopy:** Łukasz Brocki na urlopie, wraca w poniedziałek
- **Spotkania:** 
  - Spotkanie Damian + Piotr (30 minut) - omówienie architektury repozytorium
  - Spotkanie Damian + Adrian - rozpracowanie KSeF (okrojenie do potrzeb biznesowych)
  - Spotkanie 9:40 - kontynuacja planowania (20 minut) - zaopiekowanie Łukasza i zamknięcie planu
- **Przesunięcia:** 
  - Comarch Hub: Adrian rozkminia koncepcyjnie, potem przekazuje Łukaszowi
  - e-Nadawca: poprawki mogą przejąć Łukasz od Adriana

---

## 6. Uwagi dodatkowe

- **Dokumentacja projektowa:** Zaproponowano rozwiązanie na kanałach w Teams. Trzy potencjalne przestrzenie: Teams, backlog i Wiki ażurowe - one się uzupełniają. Projekt minimalnie składa się z trzech plików: 1. Uzasadnienie biznesowe (po co, dlaczego, dla kogo). 2. Rozbicie na MVP (sekwencja dostarczania, przypadki użycia). 3. Plik architektoniczno-techniczny (technologia, komunikacja, aktualne ustalenia). W stanie zerowym mamy pomysł na MVP. Ten plik będzie ewoluował.

- **Praca z Piotrem:** Uczmy Piotra jednej rzeczy: żeby włączał mikrofon i gadał. Wiem, że ma problem z wysławianiem się, szybciej myśli niż mówi, ale niech opowiada. Jak nie potrafi mówić do głuchego telefonu, to niech któryś z was tam będzie i go podpytuje. Z tego powstanie piękny opis architektury. Nagrywasz spotkanie, przechodzisz przez transkrypcję i uzupełniacie. Z czasem nauczymy się, jak rozmawiać i odpytywać Piotra o architekturę, bo to są powtarzalne tematy: uprawnienia, użytkownicy, komunikacja z AMODIT, przechowywanie plików, mikroserwisy.

- **Spotkania są coraz bardziej konstruktywne:** Brakuje tylko jednego miejsca do przechowywania i edycji dokumentacji projektowej, żebyśmy wszyscy mieli do tego dostęp.

