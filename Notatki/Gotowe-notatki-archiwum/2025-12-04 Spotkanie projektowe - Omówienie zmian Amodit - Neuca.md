# Spotkanie projektowe – 2025-12-04 – Omówienie zmian Amodit - Neuca

**Data:** 2025-12-04  
**Typ:** Spotkanie projektowe  
**Temat główny:** Omówienie zmian wizualnych w AMODIT (widok procesów, pola wymagane) - feedback klienta Neuca

**Uczestnicy:**
- **AMODIT:** Janusz Bossak, Przemysław Sołdacki, Daniel Reszka
- **Neuca:** Miłosz Śliwiński, Michał Mirończuk, Paulina Wesołowska

---

## 1. Widok kafelków procesów i folderów - zmiany wizualne

**Komponent:** UI systemu AMODIT - widok listy procesów

### Kontekst i cel

Klient Neuca zgłosił uwagi do nowego widoku kafelków procesów wprowadzonego w najnowszej wersji AMODIT. Zmiany obejmowały: rozszerzenie kafelków, usunięcie przerwy między folderami a procesami oraz usunięcie pogrubienia nazw folderów. Spotkanie miało na celu omówienie argumentów obu stron i wypracowanie kompromisu.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Powrót do starego widoku | Przywrócenie poprzedniego wyglądu z węższymi kafelkami, pogrubieniem folderów, przerwą między sekcjami | ❌ Odrzucona – konflikt z uwagami innych klientów (200 klientów, różne preferencje) |
| Nowy widok bez zmian | Pozostawienie aktualnego wyglądu bez modyfikacji | ❌ Odrzucona – nie rozwiązuje problemów Neuca |
| Kompromis z opcjami konfiguracyjnymi | Wprowadzenie opcji sterowania per klient/proces dla wybranych elementów | ✅ Wybrana – balans między potrzebami różnych klientów |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (kompromis)

**Uzgodnione zmiany:**

1. **Rozdzielenie folderów od procesów** – przywrócenie wizualnej przerwy między sekcją folderów a sekcją procesów (jak w starej wersji)
2. **Odblokowanie ilości kolumn** – usunięcie limitu 6 kolumn, kafelki będą skalować się do szerokości ekranu (dodawanie nowych kolumn zamiast rozszerzania istniejących)
3. **Pogrubienie nazw folderów** – rozważenie opcji konfiguracyjnej per klient w ustawieniach systemowych (do analizy)
4. **Wyśrodkowanie vs ikona z lewej** – pozostaje bez zmian (ikona z lewej strony, tekst obok) – uzasadnienie: lepsza estetyka przy wielu kafelkach, ikony w kolumnach są równo w linii

**Szczegóły techniczne:**
- Maksymalna ilość kolumn: obecnie 6 (sztywno ustawiony parametr) → zmiana na dynamiczne skalowanie
- Pogrubienie folderów: do rozważenia jako opcja w ustawieniach systemowych

**Uzasadnienie zmian (AMODIT):**
- Szersze kafelki: wielu klientów ma długie nazwy procesów (np. "Program badawczy związany z rozwojem dziedzin sportowych na lata 2025-2028"), które się nie mieściły i zawijały na małych kafelkach
- Usunięcie pogrubienia: feedback od klientów, że "po co takie grube, przecież każdy widzi co to jest"
- Badania UX: tendencja do lżejszego wyglądu wizualnego

### Ograniczenia / Poza zakresem

- Pełna personalizacja wyglądu per użytkownik – zbyt duże rozdrobnienie opcji zwiększa ryzyko błędów i konfliktów
- Powrót do starego widoku jako domyślnego – konflikt z potrzebami większości klientów

### Zadania / Dalsze kroki

- **Zespół AMODIT:** Odblokowanie ilości kolumn (usunięcie limitu 6) → brak terminu
- **Zespół AMODIT:** Przywrócenie wizualnej przerwy między folderami a procesami → brak terminu
- **Zespół AMODIT:** Analiza możliwości dodania opcji konfiguracyjnej dla pogrubienia nazw folderów → do rozważenia
- **Daniel Reszka:** Przesłanie podsumowania ustaleń mailem do klienta → po spotkaniu

---

## 2. Długie nazwy procesów - zawijanie i ucinanie tekstu

**Komponent:** UI systemu AMODIT - kafelki procesów

### Kontekst i cel

Problem z ucinaniem długich nazw procesów na kafelkach. W nowej wersji nazwy są ucinane po 2 liniach z "..." na końcu, co powoduje utratę kluczowych informacji (np. rok w nazwie "Elektroniczna akceptacja materiałów promocyjnych - ulotki 2025" vs "czasopisma 2026"). Dla Neuca jest to istotne, ponieważ mają wiele procesów z długimi nazwami, które nie są możliwe do skrócenia biznesowo.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Zwiększenie liczby wierszy do 3-4 | Zawijanie nazwy na więcej linii z wyśrodkowaniem wizualnym | ✅ Wybrana (priorytet 1) – rozwiązuje większość przypadków |
| Kropki w środku zamiast na końcu | Wyświetlanie początku i końca nazwy, środek zastąpiony "..." (jak w nazwach plików) | ✅ Wybrana (priorytet 2) – dla skrajnie długich nazw (powyżej 4 wierszy) |
| Zmniejszanie czcionki | Automatyczne zmniejszanie rozmiaru czcionki dla długich nazw | ❌ Odrzucona – zły UX, problemy z czytelnością |
| Limit znaków w nazwie | Ograniczenie długości nazwy procesu (np. do 150 znaków) | ❌ Odrzucona – kompatybilność wsteczna, klienci już mają długie nazwy (255 znaków) |
| Status quo (2 linie + "...") | Pozostawienie obecnego rozwiązania, pełna nazwa w tooltipie | ❌ Odrzucona – niewystarczające dla użytkowników Neuca |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

**Rozwiązanie dwuetapowe:**

1. **Zawijanie na 3-4 wiersze** z wyśrodkowaniem wizualnym (jeśli nazwa zajmuje 3 linie, to kafelek jest wizualnie wyważony - tekst lekko przesuwa się do góry)
2. **Dla skrajnie długich nazw (powyżej 4 wierszy):** kropki w środku – wyświetlanie maksymalnie początku i końca nazwy, środek zastąpiony "..." (analogia do wyświetlania nazw plików w sprawach)
3. **Pełna nazwa zawsze dostępna w tooltipie** (bez zmian)

**Szczegóły techniczne:**
- Obecny limit: 2 linie + "..." na końcu
- Nowy limit: 3-4 linie (do przetestowania na nazwach 255 znaków)
- Algorytm dla skrajnych przypadków: wyświetlanie po słowach (nie znakach), aby zachować kluczowe informacje na końcu nazwy (np. rok)

**Uzasadnienie:**
- Kluczowe informacje często są na końcu nazwy (rok, typ materiału)
- Użytkownicy Neuca mają ~200 procesów dziennie do obsługi, tooltip nie wystarcza dla szybkiej nawigacji
- Kompatybilność wsteczna - nie można ograniczyć długości nazw, które już istnieją w systemie

### Zadania / Dalsze kroki

- **Przemysław Sołdacki / Zespół AMODIT:** Implementacja zawijania na 3-4 wiersze z wyśrodkowaniem wizualnym → brak terminu
- **Zespół AMODIT:** Testowanie na skrajnych przypadkach (nazwy 255 znaków) → brak terminu
- **Zespół AMODIT:** Implementacja algorytmu "kropki w środku" dla nazw dłuższych niż 4 wiersze → brak terminu

---

## 3. Tooltips/dymki zasłaniające elementy nawigacji

**Komponent:** UI systemu AMODIT - tooltips na kafelkach

### Kontekst i cel

Dymki (tooltips) wyświetlane nad kafelkami w pierwszym wierszu zasłaniają strzałkę cofania i przycisk "Dodaj proces", co utrudnia nawigację. Problem szczególnie widoczny przy długich nazwach folderów.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Dla kafelków w pierwszym wierszu tooltip będzie wyświetlany **pod kafelkiem** (zamiast nad), aby nie zasłaniać elementów nawigacji.

**Szczegóły techniczne:**
- Detekcja pozycji kafelka (pierwszy wiersz)
- Zmiana kierunku wyświetlania tooltipa: nad → pod

### Zadania / Dalsze kroki

- **Zespół AMODIT:** Poprawka wyświetlania tooltipów dla pierwszego wiersza kafelków → brak terminu

---

## 4. Pola wymagane - wizualizacja i UX

**Komponent:** Formularz sprawy - pola wymagane

### Kontekst i cel

W nowej wersji AMODIT zmieniono sposób oznaczania pól wymaganych: z intensywnego pomarańczowego tła + obwódki + napisu "pole jest wymagane" na delikatne podkreślenie kolorem. Zmiana była odpowiedzią na liczne zgłoszenia od ~70-80% klientów, którzy narzekali na "żar miast" formularza. Neuca zgłosiła obawy o czytelność dla użytkowników, szczególnie przy procesach obsługowych z dużą liczbą pól.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Powrót do starego widoku (pełne pomarańczowe tło) | Przywrócenie intensywnego oznaczenia pól wymaganych | ❌ Odrzucona – "bez szans" (Janusz), konflikt z potrzebami 70-80% klientów |
| Nowy widok (tylko podkreślenie) | Delikatne podkreślenie + komunikat dopiero po próbie zapisu | ❌ Odrzucona – niewystarczające dla Neuca |
| Gwiazdka czerwona przy nazwie pola | Standard formularzy webowych | 💡 Propozycja Neuca – do rozważenia |
| Kompromis: opcja per proces | Możliwość włączenia komunikatu o brakujących polach od razu (bez konieczności kliknięcia "Zapisz") | ✅ Wybrana – balans między nowoczesnością a potrzebami użytkowników |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (kompromis)

**Rozwiązanie:**
- **Opcja 1 (domyślna - nowa):** Delikatne podkreślenie pól wymaganych + komunikat o brakujących polach dopiero po kliknięciu "Zapisz" + panel z listą pól wymaganych (możliwość kliknięcia i przejścia do pola)
- **Opcja 2 (konfigurowalna per proces):** Delikatne podkreślenie + komunikat o brakujących polach **wyświetlany od razu** (bez konieczności kliknięcia "Zapisz") + panel z listą pól wymaganych

**Szczegóły techniczne:**
- Panel z listą pól wymaganych: po prawej stronie, klikalne linki do pól, dynamiczna aktualizacja (pole znika z listy po wypełnieniu)
- Sterowanie: opcja per proces (w ustawieniach procesu)
- Kolejność pól w panelu: do sprawdzenia (obecnie nie odpowiada kolejności w formularzu)

**Uzasadnienie (AMODIT):**
- Nowoczesne standardy UX: pola wymagane nie są oznaczane intensywnie, komunikat pojawia się dopiero przy próbie zapisu
- Użytkownik powinien wiedzieć co ma wypełnić (założenie)
- Kompromis: delikatne podkreślenie + panel z listą pól

**Uzasadnienie (Neuca):**
- Użytkownicy często robią proces pierwszy raz, nie wiedzą co jest wymagane
- Procesy złożone, wielopoziomowe, instrukcje nie wystarczają
- Doświadczenie z własnym systemem (WinBiuro): zmiana kolorystyki na pastelową spowodowała strajk użytkowników (spadek targetów o 30%, mniejsze premie) – musieli przywrócić stary widok
- Obawa przed podobną sytuacją przy wdrożeniu nowej wersji AMODIT

### Feedback / Uwagi uczestników

- **Miłosz Śliwiński:** "Panel z listą pól wymaganych to mega fajne rozwiązanie" (pierwszy raz widział tę funkcjonalność)
- **Miłosz Śliwiński:** Obawa przed reakcją użytkowników - "połowa osób będzie miała problem z uzupełnieniem i zasypie nas zgłoszeniami"
- **Paulina Wesołowska:** "Daliśmy coś użytkownikom (255 znaków), a teraz im zabierzemy (pola wymagane)" - niekonsekwencja
- **Michał Mirończuk:** Nowe rozwiązanie pasuje, ale dostosowuje się do zdania zespołu

### Zadania / Dalsze kroki

- **Zespół AMODIT:** Dodanie opcji konfiguracyjnej per proces (wyświetlanie komunikatu o polach wymaganych od razu vs po zapisie) → brak terminu
- **Zespół AMODIT:** Sprawdzenie kolejności pól w panelu z listą pól wymaganych (powinna odpowiadać kolejności w formularzu) → brak terminu
- **Zespół Neuca:** Przygotowanie komunikacji dla użytkowników o zmianach wizualnych, aktualizacja dokumentacji → przed wdrożeniem

---

## 5. Przyciski akcji - kolorystyka

**Komponent:** Widok sprawy - przyciski akcji

### Kontekst i cel

Zmiana wyglądu przycisków akcji z ciemnych (ciemnozielone, ciemnoczerwone) na jasne z obwódką. Weryfikacja akceptacji przez klienta.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Nowa kolorystyka przycisków (jasne z obwódką) jest akceptowalna dla Neuca. Zmiana była odpowiedzią na zgłoszenie Neuca.

**Kontekst:**
- Poprzednia wersja: białe ikonki bez kolorów → natychmiastowy negatywny feedback od klientów
- Obecna wersja: jasne przyciski z kolorami i obwódką → akceptowalne

### Ograniczenia / Poza zakresem

- Powrót do ciemnych przycisków – odrzucone

---

## 6. Dynamiczne wyświetlanie przycisków akcji

**Komponent:** Widok sprawy - przyciski akcji

### Kontekst i cel

Zmiana heurystyki wyświetlania przycisków akcji. Wcześniej: maksymalnie 4 przyciski widoczne, reszta w "3 kropkach". Teraz: dynamiczne dostosowanie do szerokości ekranu (przy szerokim ekranie więcej przycisków, przy wąskim mniej).

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Nowa funkcjonalność jest pozytywnie odbierana przez Neuca. Rozwiązuje problem zgłaszany przez biznes: "czemu tylko 4 przyciski, a nie można dodać więcej?".

---

## 7. Reorganizacja zakładki "i" (informacje o sprawie)

**Komponent:** Widok sprawy - zakładka informacyjna

### Kontekst i cel

Uporządkowanie zakładki "i" (informacje o sprawie), która była przeciążona. Przeniesienie uprawnień i historii do osobnych sekcji.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Reorganizacja jest zrozumiała, choć wymaga przyzwyczajenia użytkowników. Uprawnienia przeniesione do ikony użytkowników, historia do osobnej sekcji.

**Uzasadnienie (AMODIT):**
- Zakładka "i" była przeciążona niekontekstowymi elementami
- Inne ścieżki dostępu do historii i diagramu już istnieją

### Feedback / Uwagi uczestników

- **Miłosz Śliwiński:** Początkowo nieintuicyjne, ale nikt nie zgłaszał błędów – kwestia przyzwyczajenia

---

## 8. Przycisk "Usuń sprawę" - przeniesienie do menu

**Komponent:** Widok sprawy - przycisk usuwania

### Kontekst i cel

Zmiana lokalizacji przycisku "Usuń sprawę" dla administratora. Wcześniej: czerwony przycisk w panelu informacyjnym na dole. Obecnie (w wersji testowej Neuca): widoczny u góry. Planowana zmiana: przeniesienie do menu "3 kropki".

### Decyzja / Ustalenie

**Status:** 🔍 Do wdrożenia (w następnej wersji)

Przycisk "Usuń sprawę" (dla administratora) zostanie przeniesiony do menu "3 kropki" i oznaczony na czerwono. Cel: utrudnienie przypadkowego usunięcia (miss-click zamiast "Zapisz").

**Szczegóły techniczne:**
- Użytkownik na pierwszym etapie: może usunąć sprawę (przycisk widoczny)
- Administrator: przycisk "Usuń" w menu "3 kropki" (na czerwono)

### Punkty otwarte

- **Miłosz Śliwiński:** Czy będzie opcja ukrycia przycisku "Zapisz" w ustawieniach procesu? (obecnie można ukryć "Usuń", ale nie "Zapisz")
  - **Janusz Bossak:** Tak, można zgłosić CR-kę, możliwe do zrobienia

---

## 9. Obrazki na kafelkach procesów - propozycja rozwojowa

**Komponent:** UI systemu AMODIT - widok listy procesów

### Kontekst i cel

Propozycja Neuca: dodanie możliwości wstawiania obrazków na kafelki procesów (zamiast ikony) + opis pod spodem. Wzorowane na wewnętrznym systemie Neuca (Asystent) oraz funkcjonalności "Obszary" w AMODIT (demo, obecnie nieaktywna).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Obrazki na wszystkich kafelkach | Każdy proces ma własny obrazek | ❌ Odrzucona – przy 200 procesach to szum informacyjny, nie pomoc |
| Obrazki w folderach (8-10 procesów) | Grupowanie procesów w foldery, obrazki tylko w folderach | 💡 Propozycja – do rozważenia |
| Opcja konfigurowalna (sterówka) | Możliwość włączenia/wyłączenia obrazków per klient/proces | 💡 Propozycja – do rozważenia jako rozwój osobny (wycena) |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja – do rozważenia

Funkcjonalność do analizy jako osobny rozwój (wycena). AMODIT nie będzie robić rozwiązania indywidualnego tylko dla Neuca, ale może rozważyć opcję konfigurowalną dla wszystkich klientów.

**Szczegóły techniczne:**
- Funkcjonalność "Obszary" (demo) miała podobny mechanizm – obrazki, nazwa pod spodem, przełączanie
- Możliwość wczytania obrazka zamiast ikony już istnieje w AMODIT

**Uzasadnienie (Neuca):**
- Pozytywny feedback użytkowników (głównie kobiety) - "im bardziej kolorowo, tym chętniej się klika"
- Pokrewne procesy miałyby tę samą ikonkę w różnych kolorach – łatwiejsze szukanie

**Uzasadnienie (AMODIT):**
- Przy dużej liczbie procesów (100-200) obrazki stają się szumem informacyjnym
- Funkcjonalność "Obszary" nie spotkała się z dobrym odbiorem innych klientów

### Zadania / Dalsze kroki

- **Daniel Reszka:** Znalezienie screenów z propozycji Neuca i przekazanie Januszowi → po spotkaniu
- **Zespół AMODIT:** Analiza możliwości i zastosowania funkcjonalności obrazków na kafelkach → do rozważenia

---

## 10. Historia Biznesowa - nowa funkcjonalność (informacyjnie)

**Komponent:** AMODIT - nowa funkcjonalność (w rozwoju)

### Kontekst i cel

Prezentacja nowej funkcjonalności "Historia Biznesowa" (AddEvent) - mechanizm zapisywania kluczowych zdarzeń biznesowych na sprawie, niezależnie od standardowej historii technicznej. Funkcjonalność już istnieje w regułach, ale brak GUI do wyświetlania.

**Dwa warianty:**

1. **Historia biznesowa na sprawie** - kluczowe zdarzenia w ramach jednej sprawy (np. "ostateczna akceptacja", "wysłano do księgowości")
2. **Historia międzysprawowa (Teczka sprawy)** - powiązanie zdarzeń z różnych procesów dotyczących tej samej sprawy biznesowej (np. reklamacja: korespondencja przychodząca → odpowiedź wychodząca → pismo prawnika)

### Decyzja / Ustalenie

**Status:** 💡 Propozycja – w rozwoju

Funkcjonalność w fazie kształtowania, AMODIT zbiera feedback od klientów. Mechanizm AddEvent już działa (zapisuje do bazy), ale brak interfejsu do wyświetlania.

**Szczegóły techniczne:**
- Funkcja w regułach: `AddEvent` - dodaje wpis do historii biznesowej
- Historia standardowa: automatyczna (każde kliknięcie, przekazanie sprawy, wypełnienie pola)
- Historia biznesowa: manualna (trzeba wywołać AddEvent w odpowiednich miejscach procesu)
- Możliwość integracji z zewnętrznymi systemami (np. call center) przez API

**Przykłady zastosowania:**
- Księgowość: "kto ostatecznie zaakceptował fakturę" (bez 15 cofnięć i poprawek)
- JRWA: Teczka sprawy - powiązanie korespondencji, pism, skarg dotyczących jednej sprawy
- Klient 360 stopni (ubezpieczenia): historia polis, rozmów, roszczeń klienta z różnych procesów

### Feedback / Uwagi uczestników

- **Michał Mirończuk:** Czy AddEvent już działa w wersji 2.506.30? (Neuca ma 122)
  - **Janusz Bossak:** Tak, ale tylko zapisywanie do bazy, brak GUI
- **Michał Mirończuk:** Czy można dodawać wpisy do standardowej historii sprawy funkcją?
  - **Janusz Bossak:** Do przemyślenia, ciekawa funkcjonalność
- **Daniel Reszka:** Zespół Neuca (Tomek/Artur) już pytał o historię biznesową 2-3 tygodnie temu

### Zadania / Dalsze kroki

- **Zespół Neuca:** Zebranie uwag i potrzeb dotyczących historii biznesowej, konsultacja z Tomkiem/Arturem → brak terminu
- **Zespół AMODIT:** Rozwój GUI dla historii biznesowej → w trakcie

---

## Podsumowanie spotkania

**Główne ustalenia:**

1. ✅ **Widok kafelków:** Rozdzielenie folderów od procesów, odblokowanie ilości kolumn, pogrubienie folderów do rozważenia jako opcja
2. ✅ **Długie nazwy:** Zawijanie na 3-4 wiersze + kropki w środku dla skrajnych przypadków
3. ✅ **Tooltips:** Wyświetlanie pod kafelkiem dla pierwszego wiersza
4. ✅ **Pola wymagane:** Opcja konfigurowalna per proces (komunikat od razu vs po zapisie)
5. ✅ **Przyciski akcji:** Nowa kolorystyka akceptowalna
6. 💡 **Obrazki na kafelkach:** Do rozważenia jako rozwój osobny (wycena)
7. 💡 **Historia biznesowa:** Funkcjonalność w rozwoju, Neuca zbierze uwagi

**Ton spotkania:** Konstruktywny, obie strony prezentowały argumenty i szukały kompromisu. AMODIT podkreślał konieczność balansowania potrzeb ~200 klientów, Neuca przedstawiał konkretne problemy użytkowników obsługowych.

**Następne kroki:**
- Daniel Reszka przygotuje podsumowanie mailem
- Zespół AMODIT wdroży uzgodnione zmiany (bez terminów)
- Zespół Neuca przygotuje komunikację dla użytkowników przed wdrożeniem
