# Rada Architektów – 2025-08-19

> 🛡️ Notatka zweryfikowana i zmapowana (Codex Review) w dniu 2025-12-03

**Powiązane projekty:**
- [[Moduly/Trust-Center/README|Trust-Center]] – temat 1
- [[Klienci/WIM/News-Feed-Anonse/README|News-Feed-Anonse]] + [[Koncepcje/Tablica-ogloszen/README|Tablica-ogloszen]] – temat 2
- [[Klienci/WIM/Logowanie-powiadomien/README|Logowanie-powiadomien]] + [[cross-cutting/Logowanie-powiadomien/README|Logowanie-powiadomien]] – temat 3
- [[cross-cutting/Zakladka-Do-wykonania/README|Zakladka-Do-wykonania]] – temat 4
- [[cross-cutting/Dostep-bylych-wspolpracownikow/README|Dostep-bylych-wspolpracownikow]] – temat 5

---

## 1. Trust Center – przycisk zarządzania dokumentem i automatyczne wysyłanie kodu

**Projekt:** `Moduly/Trust-Center`

### Kontekst i Problem

W AMODIT  w zarządzaniu organizacją TrustCenter istnieje przycisk umożliwiający przejście do zarządzania dokumentem w Trust Center. Obecna nazwa przycisku ("Przejdź") jest nieintuicyjna dla użytkowników, którzy nie mają wcześniejszego doświadczenia z systemem. Dodatkowo, proces wymaga ręcznego wprowadzenia adresu e-mail przed wysłaniem kodu dostępowego, co zwiększa liczbę kliknięć i utrudnia użycie.

### Zidentyfikowane Ryzyka

- Ryzyko problemów z kompatybilnością wsteczną przy wprowadzeniu automatycznego wysyłania maila – starsze wersje AMODIT mogą nie przekazywać adresu e-mail w parametrze
- Ryzyko braku dostępu do dokumentu dla użytkowników starszych wersji AMODIT, jeśli Trust Center zostanie zaktualizowany bez zachowania kompatybilności

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Nazwa przycisku "Przejdź" | Obecna nazwa przycisku | ❌ Odrzucona – nieintuicyjna, nie wiadomo dokąd prowadzi |
| Nazwa przycisku "Zarządzaj dokumentem w Trust Center" | Dłuższa, ale bardziej opisowa nazwa | ✅ Wybrana – jasno określa cel przycisku |
| Ręczne wprowadzenie maila | Użytkownik musi wpisać adres e-mail przed wysłaniem kodu | ❌ Odrzucona – zwiększa liczbę kliknięć |
| Automatyczne wysyłanie maila | System automatycznie wysyła kod na adres e-mail użytkownika | ✅ Wybrana – upraszcza proces, mniej kliknięć |
| Kompatybilność wsteczna przez sprawdzenie parametru | Jeśli e-mail w query string → automatycznie, jeśli nie → pokaż pole | ✅ Wybrana – zapewnia działanie dla wszystkich wersji |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono następujące zmiany w Trust Center:

1. **Zmiana nazwy przycisku:** "Zarządzaj dokumentem w Trust Center" (zamiast "Przejdź")
2. **Walidacja użytkownika:** Po kliknięciu przycisku system weryfikuje, czy użytkownik jest wysyłającym dokument lub administratorem organizacji
3. **Komunikat błędny:** Jeśli użytkownik nie spełnia warunków, otrzymuje komunikat "skontaktuj się z administratorem"
4. **Automatyczne wysyłanie maila:** Jeśli walidacja pozytywna, system automatycznie wysyła kod dostępowy na adres e-mail użytkownika (bez konieczności ręcznego wprowadzenia)
5. **Kompatybilność wsteczna:** 
   - Jeśli e-mail jest przekazywany w query string (nowsze wersje AMODIT) → automatyczne wysłanie kodu bez pokazywania pola
   - Jeśli e-mail nie jest przekazywany (starsze wersje AMODIT) → pokazanie pola do ręcznego wprowadzenia adresu e-mail

**Szczegóły techniczne:**
- Przycisk: "Zarządzaj dokumentem w Trust Center"
- Walidacja: sprawdzenie czy użytkownik jest wysyłającym lub administratorem organizacji
- Mechanizm kompatybilności: sprawdzenie obecności e-mail w query string
- Trust Center: wymaga podniesienia wersji dla nowej funkcjonalności (automatyczne wysyłanie)

### Zadania

- **Marek Dziakowski:** Implementacja zmian zgodnie z ustaleniami

### Punkty otwarte

- Brak

---

## 2. Tablica ogłoszeń / News feed – wymagania i alternatywy

**Projekty:** `Klienci/WIM/News-Feed-Anonse` + `Koncepcje/Tablica-ogloszen`

### Kontekst i Problem

WIM wymaga funkcjonalności tablicy ogłoszeń (news feed), która zastąpi przestarzały mechanizm newsów. Obecny stary mechanizm newsów jest przestarzały technologicznie i nie jest używany przez kluczowych klientów (CIT nie używa, Deutsche Bank – oczekiwanie na informacje). Damian przygotował prototyp modułu "Ogłoszenia", jednak pojawiły się pytania o rzeczywiste wymagania biznesowe i różnice między "news feedem", "tablicą ogłoszeń" a systemem anonsów (typu OLX – "mam monitor do wydania").

### Zidentyfikowane Ryzyka

- Ryzyko stworzenia funkcjonalności powielającej możliwości istniejących narzędzi (AMODIT Talk, dedykowane procesy)
- Ryzyko nieuwzględnienia kluczowych wymagań biznesowych w prototypie (planowanie publikacji, termin ważności, elastyczny dobór odbiorców)
- Ryzyko niejasności co do różnic między "news feedem" a "tablicą ogłoszeń" w wizji Piotra Murawskiego
- Ryzyko tworzenia "wrzodów na tyłku" – funkcjonalności trudnych do obrony i rozwoju, tylko po to, żeby zaspokoić klienta

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dedykowany moduł "Ogłoszenia" | Nowa zakładka w menu powiadomień z prototypem Damiana | ⏸️ Odroczona – wymaga doprecyzowania wymagań |
| AMODIT Talk | Wykorzystanie istniejącego komunikatora do ogłoszeń | 💡 Propozycja – gotowe mechanizmy (załączniki, komentarze, historia) |
| Dedykowany proces AMODIT | Wykorzystanie standardowego procesu workflow do obiegu ogłoszeń | 💡 Propozycja – gotowe mechanizmy, ale niesie "ciężar" obiegu spraw |
| RSS feed | Zewnętrzne źródło newsów (jak obecny blog AMODIT) | ⏸️ Odroczona – na później |

### Decyzja

**Status:** 🔍 Do weryfikacji

Ustalono wstrzymanie prac deweloperskich nad nową funkcjonalnością do czasu precyzyjnego zdefiniowania wymagań biznesowych. Konieczna jest analiza biznesowa z Piotrem Murawskim (WIM) w celu:

1. **Wyjaśnienia różnic** między "news feedem", "tablicą ogłoszeń" a systemem anonsów (typu OLX)
2. **Weryfikacji możliwości wykorzystania AMODIT Talk** do realizacji wymagań (grupy, dyskusje, załączniki)
3. **Określenia rzeczywistych potrzeb** – czy potrzebny jest dedykowany moduł, czy można wykorzystać istniejące narzędzia

**Szczegóły techniczne:**
- Prototyp Damiana: zakładka "Ogłoszenia" w menu powiadomień
- Obecne funkcjonalności w prototypie: tworzenie ogłoszenia (temat, treść, odbiorcy na podstawie działów), oznaczenie jako przeczytane, usunięcie, wyszukiwanie
- Brakujące w prototypie: planowanie publikacji (data startu), termin ważności, wybór odbiorców przez grupy (nie tylko działy), organizacje zewnętrzne
- Stary mechanizm newsów: przestarzały technologicznie, nieużywany przez kluczowych klientów

**Proponowane rozszerzenia prototypu (jeśli będzie kontynuowany):**
- Mechanizm wyboru odbiorców: dla administratorów / dla wszystkich / dla wybranych grup (jak w raportach) / dla wybranych osób / struktura organizacyjna
- Planowanie publikacji: data i godzina startu publikacji
- Termin ważności: automatyczne ukrycie/archiwizacja po dacie wygaśnięcia
- Usuwanie ogłoszeń: tylko dla siebie (odpięcie od użytkownika), nie dla wszystkich odbiorców

### Zadania

- **Damian Kamiński:** Skontaktowanie się z Piotrem Murawskim w celu doprecyzowania wymagań biznesowych i wyjaśnienia różnic między news feedem a tablicą ogłoszeń
- **Mateusz Kisiel:** Przygotowanie prezentacji AMODIT Talk do konfrontacji z wymaganiami dotyczącymi ogłoszeń
- **Damian Kamiński:** Pokazanie prototypu ogłoszeń i AMODIT Talk Piotrowi Murawskiemu, weryfikacja czy AMODIT Talk może pokryć wymagania

### Punkty otwarte

- Jaka jest różnica między "news feedem" a "tablicą ogłoszeń" w wizji Piotra Murawskiego?
- Czy potrzebny jest system anonsów (typu "sprzedam/oddam") czy tylko ogłoszenia informacyjne?
- Czy AMODIT Talk może pokryć wymagania dotyczące ogłoszeń?
- Czy potrzebny jest dedykowany moduł, czy można wykorzystać istniejące narzędzia (AMODIT Talk, dedykowane procesy)?
- Jakie są rzeczywiste potrzeby biznesowe – czy to ma być jak OLX (ogłoszenia z możliwością dyskusji) czy jak news feed (jednokierunkowa komunikacja)?

---

## 3. Logowanie powiadomień systemowych – ślad audytowy

**Projekty:** `Klienci/WIM/Logowanie-powiadomien` + `cross-cutting/Logowanie-powiadomien`

### Kontekst i Problem

WIM wymaga, aby treść, odbiorcy i czas wysłania każdego powiadomienia systemowego (maila) z Workflow były zapisywane po stronie AMODIT jako ślad audytowy. Obecny mechanizm logowania wejść i pobrania dokumentów wymaga rozszerzenia o nową kategorię dla powiadomień e-mail.

### Zidentyfikowane Ryzyka

- Ryzyko zapychania się tabeli logów przy dużej liczbie powiadomień
- Ryzyko problemów wydajnościowych przy braku mechanizmu czyszczenia starych logów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Logowanie w tabeli Notification | Wykorzystanie istniejącej tabeli Notification | ❌ Odrzucona – tabela jest czyszczona, to kolejka techniczna, nie audytowa |
| Osobna tabela dla logów powiadomień | Nowa tabela dedykowana do przechowywania logów powiadomień | ✅ Wybrana – trwałe przechowywanie, nie czyszczone |
| Rozszerzenie istniejącego mechanizmu logowania | Dodanie kategorii "powiadomienia" do istniejącego mechanizmu logowania | ✅ Wybrana – wykorzystanie istniejącego mechanizmu |
| Czyszczenie starych logów | Parametr w ustawieniach systemowych określający czas przechowywania | ⏸️ Odroczona – na razie bez czyszczenia, logi pozostają na wieczność |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono wprowadzenie logowania powiadomień systemowych jako rozszerzenie istniejącego mechanizmu logowania:

1. **Włączanie na poziomie procesu:** Ustawienie w ustawieniach procesu "Loguj mailingi systemowe" z opcją "loguj z treścią maila" (checkbox)
2. **Co logujemy:** Data, odbiorca (do kogo), tytuł, treść (jeśli włączone), typ (z czego wynika), rodzaj (indywidualny/zbiorczy/wynikający z ustawień konta), case ID (z którego case'a wynika)
3. **Mechanizm:** Rozszerzenie istniejącego mechanizmu logowania wejść i pobrania dokumentów o nową kategorię "powiadomienia"
4. **Przechowywanie:** Logi pozostają na wieczność, bez czyszczenia (jak historia)

**Szczegóły techniczne:**
- Ustawienie procesu: checkbox "Loguj mailingi systemowe" + checkbox "Loguj z treścią maila"
- Typy powiadomień do logowania: forward, dodanie CC, SendMessage, przypomnienia
- Mechanizm: rozszerzenie istniejącego mechanizmu logowania (UserActivityLog lub podobny) o kategorię "powiadomienia"
- Tabela: osobna tabela lub rozszerzenie istniejącej (nie tabela Notification, która jest czyszczona)

### Zadania

- **Piotr Buczkowski:** Weryfikacja istniejącego mechanizmu logowania i określenie co dokładnie logować oraz jak rozszerzyć mechanizm
- **Piotr Buczkowski:** Przygotowanie zadania na sprint (status "Ready to do", przypisane do Damiana)
- **Damian Kamiński:** Przekazanie zadania do realizacji na Daily (jutro)

### Punkty otwarte

- Która dokładnie tabela będzie używana do logowania powiadomień?
- Czy w przyszłości będzie potrzebny parametr określający czas przechowywania logów (czyszczenie starych)?
- Jakie dokładnie typy powiadomień mają być logowane (wszystkie czy tylko wybrane)?

---

## 4. Zakładka "Do wykonania" – widoczność niezależnie od obszarów

**Projekt:** `cross-cutting/Zakladka-Do-wykonania`

### Kontekst i Problem

Zgłoszenie 21681: zakładka "Do wykonania" powinna być widoczna niezależnie od włączonych obszarów procesów. Obecnie, jeśli obszar "Wszystkie procesy" jest wyłączony, zakładka "Do wykonania" znika, co jest niepożądane – użytkownik może nie chcieć obszaru "Wszystkie procesy" (ze względu na długą listę przypiętych raportów), ale nadal potrzebuje globalnej zakładki "Do wykonania".

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zakładka zależna od obszaru | Obecne podejście – zakładka znika gdy obszar wyłączony | ❌ Odrzucona – nie spełnia wymagań użytkownika |
| Zakładka zawsze widoczna | Zakładka "Do wykonania" widoczna niezależnie od włączonych obszarów | ✅ Wybrana – spełnia wymagania użytkownika |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono, że zakładka "Do wykonania" ma być widoczna zawsze, niezależnie od włączonych obszarów procesów. Zakładka ma wyświetlać treść taką samą jak zakładka "Do wykonania" w obszarze "Wszystkie procesy" (wszystkie zadania z wszystkich procesów, niezależnie od obszaru).

**Szczegóły techniczne:**
- Zakładka "Do wykonania": zawsze widoczna w głównym menu
- Zawartość: wszystkie zadania z wszystkich procesów (jak w obszarze "Wszystkie procesy")
- Logika: bez sprawdzania obszarów, wyświetla wszystkie zadania niezależnie od konfiguracji obszarów
- Zgłoszenie: 21681

### Zadania

- **Piotr Buczkowski:** Implementacja zmiany – zakładka "Do wykonania" zawsze widoczna, wyświetla wszystkie zadania niezależnie od obszarów

### Punkty otwarte

- Brak

---

## 5. Dostęp byłych współpracowników do sprawy

**Projekt:** `cross-cutting/Dostep-bylych-wspolpracownikow`

### Kontekst i Problem

Zgłoszenie 21722: osoba wykonująca akcję na sprawie jako współpracownik powinna zachować dostęp do odczytu do sprawy, gdy przestanie być współpracownikiem. Obecnie, gdy osoba przestaje być współpracownikiem, traci dostęp do sprawy, co może być problematyczne dla osób, które wykonały akcje i powinny mieć możliwość wglądu w historię.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Brak dostępu po zakończeniu współpracy | Obecne podejście – osoba traci dostęp | ❌ Odrzucona – nie spełnia wymagań |
| Dostęp do odczytu po zakończeniu współpracy | Osoba zachowuje dostęp do odczytu sprawy | ✅ Wybrana – zgodne z wymaganiami |
| Włączalne na poziomie procesu | Mechanizm podobny do zastępstw – włączalne w ustawieniach procesu | ✅ Wybrana – elastyczne rozwiązanie, zgodne z mechanizmem zastępstw |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono, że osoba wykonująca akcję na sprawie jako współpracownik powinna zachować dostęp do odczytu do sprawy, gdy przestanie być współpracownikiem. Mechanizm ma działać analogicznie do zastępstw – włączalny w ustawieniach procesu.

**Szczegóły techniczne:**
- Mechanizm: podobny do zastępstw – włączalny w ustawieniach procesu
- Dostęp: tylko do odczytu (nie pełny dostęp)
- Warunek: osoba musiała wykonać akcję na sprawie jako współpracownik
- Zgłoszenie: 21722

### Zadania

- **Piotr Buczkowski:** Wpisanie odpowiedzi w zgłoszeniu 21722

### Punkty otwarte

- Jak dokładnie będzie działać mechanizm włączania w ustawieniach procesu?
- Czy dostęp do odczytu będzie dotyczył wszystkich spraw, na których osoba wykonała akcję, czy tylko wybranych?

