**Data:** 2025-12-10
**Typ:** Spotkanie projektowe
**Temat główny:** Omówienie wyceny dla Neuca

**Źródło:** [Transkrypcja](../Transkrypcje/oczyszczone-archiwum/2025-12-10 Omówienie wyceny dla Neuca - transkrypcja - część 1.md)

---

## 1. Widok kafelków procesów - Rozdzielenie wizualne folderów i procesów

**Komponent:** Interfejs użytkownika

### Kontekst i cel

Neuca zgłasza, że w widoku kafelków procesów brakuje wyraźnego wizualnego podziału między kafelkami folderów a kafelkami procesów. Obecnie kafelki procesów lecą zaraz w tej samej linii co kafelki folderów, a klient chce żeby kafelki folderów leciały, a od nowej linii zaczynały się kafelki procesów (tak jak było poprzednio).

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Wprowadzenie wyraźnego wizualnego podziału - odstęp pomiędzy kafelkami folderów a kafelkami procesów. Kafelki folderów w jednej linii, kafelki procesów od nowej linii. Dotyczy zarówno zakładki Procesy jak i Raporty.

**Szczegóły techniczne:**
- Rozdzielenie sekcji folderów i procesów
- Rozważenie integracji z repozytorium (spójność kafelków)

### Zadania / Dalsze kroki

- **Zespół:** Wprowadzenie rozdzielenia sekcji (design)

---

## 2. Widok kafelków procesów - Pogrubienie czcionki na kafelkach folderów

**Komponent:** Interfejs użytkownika

### Kontekst i cel

Neuca wnioskowała o pogrubienie czcionki na kafelkach folderów (tak jak było wcześniej), żeby foldery były bardziej wyróżnione od procesów.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Pogrubienie czcionki | Dodanie bolda na kafelkach folderów | ❌ Odrzucona - różnica prawie niewyczuwalna |
| Opcja w ustawieniach systemowych | Możliwość włączenia/wyłączenia pogrubienia per system | ❌ Odrzucona - zbyt drobna zmiana |
| Opcja per użytkownik | Każdy użytkownik ustawia sobie | ❌ Odrzucona - niepotrzebne komplikowanie |

### Decyzja / Ustalenie

**Status:** ❌ Odrzucona

Nie wprowadzamy pogrubienia czcionki na kafelkach folderów. Rozdzielenie sekcji (folderów i procesów) już wystarczająco wyróżnia foldery. Pogrubienie jest zbyt drobną zmianą, która nie wnosi wartości.

**Uzasadnienie:**
- Różnica między boldem a normalną czcionką jest prawie niewyczuwalna
- Rozdzielenie sekcji już rozwiązuje problem wyróżnienia
- Nie warto komplikować systemu takimi drobnymi opcjami

---

## 3. Widok kafelków procesów - Skalowanie kolumn na szerokich ekranach

**Komponent:** Interfejs użytkownika

### Kontekst i cel

Neuca chce odblokowanie liczby kolumn na szerokich ekranach. Obecnie jest limit 6 kolumn, a klient chce więcej kolumn na dużych monitorach.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (już zrobione)

Odblokowanie liczby kolumn - kafelki będą skalować się do szerokości ekranu (dodawanie nowych kolumn zamiast rozszerzania istniejących). To już zostało zrobione w grudniowej wersji.

**Szczegóły techniczne:**
- Usunięcie limitu 6 kolumn
- Kafelki skalują się do szerokości ekranu
- Na bardzo dużych monitorach (32 cale) może być więcej niż 6 kolumn

### Punkty otwarte

- Czy funkcjonalność działa poprawnie na środowisku dev? (Kamil sprawdzi zgłoszenie)

---

## 4. Widok kafelków procesów - Skracanie długich nazw procesów

**Komponent:** Interfejs użytkownika

### Kontekst i cel

Neuca ma wiele procesów z długimi nazwami (do 255 znaków), które nie mogą być skrócone biznesowo. Obecnie nazwy są ucinane na końcu (2 linie + "..."), co powoduje utratę kluczowych informacji (np. rok w nazwie procesu). Często kluczowa informacja jest na końcu nazwy.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Zawijanie na 3-4 linie | Zwiększenie liczby linii z 2 do 3-4 | ⏸️ Częściowo - zwiększenie do 5 linii |
| Ucinanie od środka | Wyświetlanie początku, wielokropek i końca | ✅ Wybrana - algorytm jak na załącznikach |
| Dodatkowe pole "wersja" | Osobne pole na kafelku dla kluczowej informacji | ❌ Odrzucona - zbyt skomplikowane |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Wprowadzenie dwóch zmian:
1. **Zwiększenie liczby linii z 2 do 5** - nazwa może być wyświetlona na maksymalnie 5 liniach
2. **Ucinanie od środka** - jeśli nazwa nie mieści się w 5 liniach, wyświetlanie początku, wielokropek i końca (algorytm taki sam jak na załącznikach w prawym panelu sprawy - dzielenie po połowie)

**Szczegóły techniczne:**
- Maksymalnie 5 linii (6 już za sztywno, 5 jest jeszcze sensownym paddingiem)
- Algorytm ucinania: dzielenie po połowie (mniej więcej po połowie, uwzględniając spacje, nawiasy)
- Dzielenie pełnymi wyrazami (nie ciurkiem, bo źle się czyta)
- Jeśli nazwa mieści się w 5 liniach - pełna nazwa, jeśli nie - ucinanie od środka

### Ograniczenia / Poza zakresem

- Skrajne przypadki (np. "konstantynopolitańczykiewiczówna" na początku) - wtedy będzie kłopot, ale to rzadkie przypadki
- Dzielenie po wyrazach zamiast po połowie - jeśli ktoś się będzie czepiał, będziemy się zastanawiać, ale na razie algorytm po połowie jest wystarczający

### Punkty otwarte

- Czy 5 linii wystarczy dla skrajnych przypadków Neuca i MSiT? (najpierw zrobić 5 linii i zobaczyć czy wystarcza)

---

## 5. Widok kafelków procesów - Tooltips (dymki) - pozycjonowanie i logika wyświetlania

**Komponent:** Interfejs użytkownika

### Kontekst i cel

Neuca zgłasza problem z tooltipami na kafelkach procesów:
1. Tooltipy zasłaniają przycisk "Dodaj proces" i strzałkę wstecz (szczególnie w pierwszym rzędzie)
2. Tooltipy wyświetlają się zawsze, nawet gdy pełna nazwa się mieści w kafelku (błąd w kryteriach akceptacji - nie napisano że tooltip ma być tylko gdy pełna nazwa się nie mieści)

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Tooltip w dół dla pierwszego rzędu | Wyświetlanie tooltipa pod kafelkiem w pierwszym rzędzie | ✅ Wybrana - część rozwiązania |
| Tooltip tylko dla skróconych nazw | Wyświetlanie tooltipa tylko gdy nazwa została skrócona | ✅ Wybrana - część rozwiązania |
| Opóźnienie wyświetlania | Tooltip pojawia się po dłuższym pobycie na polu (np. 1 sekunda) | ✅ Wybrana - część rozwiązania |
| Tooltip zawsze | Wyświetlanie tooltipa zawsze (dla kopiowania nazwy) | ❌ Odrzucona - irytujące, przeszkadza |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Wprowadzenie trzech zmian:
1. **Tooltip w dół dla pierwszego rzędu** - jeśli kafelek jest w pierwszym rzędzie, tooltip wyświetla się pod kafelkiem (zamiast nad), aby nie zasłaniać przycisku "Dodaj proces" i strzałki wstecz
2. **Tooltip tylko dla skróconych nazw** - tooltip wyświetla się tylko gdy nazwa została skrócona (nie mieści się w 5 liniach), jeśli pełna nazwa jest widoczna - brak tooltipa
3. **Opóźnienie wyświetlania** - tooltip pojawia się po dłuższym pobycie na kafelku (nie od razu, żeby nie "faluje" przy szybkim przesuwaniu kursora)

**Szczegóły techniczne:**
- Heurystyka pozycjonowania: jeśli kafelek blisko góry - tooltip w dół, jeśli blisko dołu - tooltip w górę (jak na sprawie)
- Tooltip tylko gdy nazwa skrócona (ma kropeczki)
- Opóźnienie wyświetlania (nie ułamek sekundy, ale też nie za długo - 1 sekunda może być za długo)

### Ograniczenia / Poza zakresem

- Kopiowanie nazwy z tooltipa - jeśli ktoś potrzebuje skopiować nazwę, może użyć opisu procesu (gdy kliknie w kafelek)
- Link do uruchomienia sprawy - jest już funkcjonalność w ustawieniach procesu, ale wymaga poprawy bezpieczeństwa (link nie trzyma uprawnień)

### Punkty otwarte

- Jakie dokładne opóźnienie wyświetlania tooltipa? (1 sekunda może być za długo, ale ułamek sekundy za krótko)

---

## 6. Formularz sprawy - Pola wymagane - walidacja na starcie

**Komponent:** Interfejs sprawy

### Kontekst i cel

Neuca chce, żeby pola wymagane były widoczne od razu po wejściu w sprawę (nie dopiero po próbie zapisu). Obecnie jest ustawienie systemowe, które wyłącza górną belkę "Formularz nie jest kompletny", ale pola wymagane nie są podświetlone na starcie.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Wprowadzenie wyświetlania pól wymaganych na starcie sprawy - jeśli ustawienie systemowe jest wyłączone, po wejściu w sprawę od razu wyświetlamy belkę "Formularz nie jest kompletny" i komunikaty pod polami wymaganymi (tak jakby użytkownik próbował zapisać nieuzupełnioną sprawę).

**Szczegóły techniczne:**
- Ustawienie systemowe per system (nie per użytkownik)
- Jeśli ustawienie wyłączone - od razu po wejściu w sprawę wyświetlamy walidację
- Endpoint już istnieje, to tylko zadanie dla Reactowca (Mariusz) - wyświetlenie na starcie

### Ograniczenia / Poza zakresem

- Podświetlanie pól wymaganych na różne sposoby - zostajemy z jednym podświetleniem (belka + komunikaty pod polami)

### Zadania / Dalsze kroki

- **Mariusz:** Wyświetlenie walidacji pól wymaganych na starcie sprawy (jeśli ustawienie systemowe wyłączone)

---

## 7. Formularz sprawy - Przycisk "Zapisz" - możliwość ukrycia

**Komponent:** Interfejs sprawy

### Kontekst i cel

Neuca chciałaby mieć w ustawieniach procesu możliwość ukrycia przycisku "Zapisz" w ogóle. Według nich nie powinno być czegoś takiego jak "Zapisz" - są akcje: "Przekaż", "Stwórz", "Pobierz", ale nie "Zapisz".

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Ukrycie przycisku "Zapisz" | Opcja w ustawieniach procesu do ukrycia przycisku | 💡 Propozycja - wymaga CR od klienta |
| Zostawienie jak jest | Przycisk "Zapisz" zawsze widoczny | ⏸️ Domyślnie - dopóki klient nie złoży CR |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (wymaga CR od klienta)

Neuca ma wystawić zgłoszenie CR na możliwość ukrycia przycisku "Zapisz" w ustawieniach procesu. W CR-ce mają napisać po co im to (przypadek biznesowy).

**Uzasadnienie:**
- Zespół ma wątpliwości co do sensu biznesowego (co jeśli ktoś zacznie sprawę, musi się zastanowić, skonsultować, przejść na inne narzędzie - bez "Zapisz" nie może zostawić stanu)
- Jeśli klient za to płaci i ma przypadek biznesowy - OK
- Podejrzenie że klient sam się z tego wycofa później, ale to ich sprawa

### Ograniczenia / Poza zakresem

- Ukrycie tylko na pierwszym etapie - nie ma sensu, bo to będzie niespójny system

### Punkty otwarte

- Jaki przypadek biznesowy Neuca poda w CR-ce?

---

## 8. Formularz sprawy - Przycisk "Usuń" dla administratora

**Komponent:** Interfejs sprawy

### Kontekst i cel

Przycisk "Usuń" dla administratora był wcześniej pod ikoną "i" (informacje), a teraz został przeniesiony do 3 kropek. Neuca twierdzi, że dyskusja była dłuższa i im się podobało poprzednie rozwiązanie, ale to jest kwestia przyzwyczajeń.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Przycisk "Usuń" dla administratora pozostaje w 3 kropkach, ale:
- Na pierwszym etapie - normalne "Usuń" (z roli użytkownika który rozpoczął proces) + czerwone "Usuń" w 3 kropkach (z roli administratora)
- Na kolejnych etapach - tylko czerwone "Usuń" w 3 kropkach (dla administratora)

**Szczegóły techniczne:**
- Czerwone "Usuń" w 3 kropkach - wyświetlane tylko administratorowi
- Wyświetlane zawsze (tak samo jak było w "i")
- Taki sam tekst jak do tej pory (nie "Usuń..." tylko "Usuń")
- Czcionka w innych komunikatach jest inna - to niezależny temat do zgłoszenia

### Ograniczenia / Poza zakresem

- Zmiana czcionki w komunikatach - to osobny temat (Damian zapomni zgłosić, ale to niezależne)

---

## 9. Historia biznesowa - temat do dalszej dyskusji

**Komponent:** Moduł raportowy / Koncepcje

### Kontekst i cel

Podczas spotkania z Neuca Janusz opowiadał o koncepcji historii biznesowej. Temat bardzo się klientowi podobał - mówią że to jest coś czego potrzebują. To jest szansa na wciągnięcie klienta w analizę i pozyskanie większego budżetu.

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (wymaga dalszej dyskusji)

Temat wymaga dalszej dyskusji z Neuca:
- Spotkanie z klientem - pokazanie co mamy, co kombinujemy, co myślimy żeby zrobić
- Ustalenie jakie oni widzą sensowne zastosowania (potrzeby)
- Możliwość współpracy z Rossmannem (szersza perspektywa, nie tylko potrzeby jednego klienta)

**Szczegóły:**
- Historia biznesowa to koncepcja która może być wykorzystana w różnych kontekstach
- Może być powiązana z JRWA i teczkami sprawy (patrz sekcja 10)

### Punkty otwarte

- Jakie zastosowania widzi Neuca dla historii biznesowej?
- Czy współpraca z Rossmannem jest możliwa?
- Jak to wpisuje się w roadmapę?

---

## 10. JRWA i teczki sprawy - koncepcja

**Komponent:** Koncepcje

### Kontekst i cel

Podczas rozmowy o JRWA (dla LOT) pojawiła się koncepcja "teczki sprawy" - podobna do teczki e-Sądowej, która łączy wiele elementów. To jest kierunek na którym powinniśmy myśleć - patrzenie na klienta (Klient 360), sprawy związane z polisami, roszczeniami, różnymi rzeczami.

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (koncepcyjna)

Koncepcja teczki sprawy:
- Podobna do JRWA (konkretna, sztywna potrzeba urzędowa)
- Teczka klienta - podpinamy umowę na maintenance, umowę na wdrożenie projektowe, umowę na licencję, umowę na moduły itd.
- Może być powiązana z historią biznesową (sekcja 9)

**Pytania do rozważenia:**
- Czy potrzebujemy czegoś specjalnego od AMODIT żeby ułatwić robienie takiej teczki?
- Jakie elementy mogą być w teczce? (pracownicy, klienci, sprawy)
- Czy to jest w naszej roadmapie? (to będzie kosztować)

### Ograniczenia / Poza zakresem

- To jest temat rozwojowy, nie pilny
- Wymaga znalezienia przestrzeni i dyskusji
- Musimy się cofnąć krok wyżej - czy to jest nasza Roadmapa?

### Punkty otwarte

- Czy potrzebujemy czegoś specjalnego od AMODIT dla teczek sprawy?
- Jakie elementy mogą być w teczce?
- Czy to jest w roadmapie?

---

## 11. Komunikacja z klientami o nowościach

**Komponent:** Organizacja pracy / Dokumentacja

### Kontekst i cel

Problem: klienci nie wiedzą o nowościach które wchodzą w AMODIT. Przykład: funkcjonalność zarządzania polami wymaganymi była już zrobiona, ale klient o tym nie wiedział. Nawet zespół DEV nie zawsze wie co zostało zrobione (Janusz miał wątpliwości czy funkcjonalność jest zrobiona).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Prezentacje raz na kwartał | Co wchodzi w wersji - za rzadko i za dużo na raz | ❌ Odrzucona |
| Prezentacje w piątki na spotkaniu z konsultantami | Pokazywanie nowości z PBI (Done, wydane) | 💡 Propozycja |
| Krótkie filmiki (2 minuty) | Filmik o jednym zagadnieniu (np. zarządzanie polami wymaganymi) | 💡 Propozycja |
| Kanał "Nowości w AMODIT" w Teams | Powiadomienia o nowościach | 💡 Propozycja (już jest zakładka Powiadomienia) |
| Certyfikacja | Wymaganie certyfikacji - ci którzy słuchali pierwszym razem nie będą karani | 💡 Propozycja |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (wymaga dalszej dyskusji)

Potrzebne są różne kanały prezentacji nowości:
- **Prezentacje w piątki** - na spotkaniu z konsultantami, pokazywanie PBI które są Done i wydane
- **Krótkie filmiki** - 2-minutowe filmiki o jednym zagadnieniu (np. zarządzanie polami wymaganymi)
- **Zakładka Powiadomienia** - już istnieje, miała się wypełniać z bloga, ale blog nie jest robiony
- **Certyfikacja** - wymaganie certyfikacji, żeby nie karać tych którzy słuchali pierwszym razem

**Szczegóły:**
- Lista PBI (Done, wydane) jest dla zespołu DEV - narzędzie do znalezienia, do wzięcia na warsztat
- Zespół DEV powinien pokazywać nowości konsultantom
- Wiki/instrukcje - bardzo słabo zaopiekowane, powinno powstawać dużo (4 dziennie), Łukasz Bott przechodzi do Serwisu/Daniela

### Ograniczenia / Poza zakresem

- Blog na AMODIT.pl - nie jest robiony
- Wiki - bardzo słabo zaopiekowane, ciągle bardzo słabo mimo że to główne zadanie Łukasza przez ostatnie 2 lata

### Punkty otwarte

- Jak najlepiej komunikować nowości klientom?
- Czy certyfikacja jest rozwiązaniem?
- Jak poprawić Wiki/instrukcje?

---

## 12. Planowanie urlopów/nieobecności

**Komponent:** Organizacja pracy

### Kontekst i cel

Potrzeba planowania urlopów i nieobecności w zespole. Problem: brak kanału komunikacji (większość na szkoleniu), potrzeba ustalenia urlopów na przyszły tydzień i dalej. Jest zgoda Przemka, żeby można było odbierać zaległe urlopy w następnym roku.

### Decyzja / Ustalenie

**Status:** 💡 Propozycja

Wykorzystanie procesu "Planowanie urlopów" (lub "Planowanie nieobecności") z Portalu Pracownika:
- Proces do uruchomienia w AMODIT
- Ganttowy raport - widzimy czy coś konfliktuje czy nie
- Możliwość wpisania nieobecności (nie tylko urlopy) - np. Mateusz ma studia w poniedziałki

**Szczegóły:**
- Nazwa: "Planowanie nieobecności" (zamiast "Planowanie urlopów") - bo obejmuje też inne nieobecności
- Proces prosty, jak gdzieś go mają w dodatku
- Można dać za darmo klientom którzy biorą teczkę z portalem

### Zadania / Dalsze kroki

- **Zespół:** Spotkanie organizacyjne po 15:00 (po szkoleniu) - ustalenie urlopów na przyszły tydzień

### Punkty otwarte

- Czy proces "Planowanie urlopów" jest dostępny w AMODIT?
- Jak najlepiej komunikować nieobecności w zespole?

---

## Podsumowanie ustaleń dla Neuca

### Priorytetowe zmiany (do grudniowej wersji):

1. ✅ Rozdzielenie wizualne folderów i procesów w widoku kafelków
2. ❌ Pogrubienie czcionki - nie robimy
3. ✅ Skalowanie kolumn - już zrobione
4. ✅ Skracanie nazw - 5 linii, ucinanie od środka
5. ✅ Tooltips - pozycjonowanie w dół dla pierwszego rzędu, tylko dla skróconych nazw, opóźnienie
6. ✅ Pola wymagane - walidacja na starcie sprawy
7. 💡 Przycisk "Zapisz" - ukrycie (wymaga CR od klienta)
8. ✅ Przycisk "Usuń" - pozostaje w 3 kropkach, czerwone dla administratora

### Tematy do dalszej dyskusji:

- Historia biznesowa - spotkanie z Neuca, pokazanie co mamy, ustalenie potrzeb
- JRWA i teczki sprawy - koncepcja do rozważenia
- Komunikacja z klientami o nowościach - różne kanały prezentacji

### Zadania:

- **Damian Kamiński, Kamil Dubaniowski:** Redakcja notatki dla Neuca - co już jest, co jeszcze dorobimy, konkretne zmiany (nie ogólniki), wysłanie do Neuca w celu ostatecznego zatwierdzenia
- **Mariusz:** Wyświetlenie walidacji pól wymaganych na starcie sprawy
- **Zespół:** Wprowadzenie zmian w widoku kafelków (rozdzielenie, skracanie nazw, tooltips)

