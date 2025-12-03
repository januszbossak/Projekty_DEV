# Rada Architektów – 2025-08-21

> 🛡️ Notatka zweryfikowana i zmapowana (Codex Review) w dniu 2025-12-03

**Powiązane projekty:**
- [[Moduly/Raporty-systemowe/README|Raporty-systemowe]] – tematy 1, 2
- [[Klienci/WIM/Logowanie-powiadomien/README|Logowanie-powiadomien]] + [[cross-cutting/Logowanie-powiadomien/README|Logowanie-powiadomien]] – temat 3
- [[cross-cutting/GTA - dostęp tymczasowy do sparwy/README|GTA]] – temat 4
- [[Klienci/WIM/Repozytorium/README|Repozytorium]] – temat 5

---

## 1. Raporty systemowe – hotfix i funkcjonalność kopiowania

**Projekt:** `Moduly/Raporty-systemowe`

### Kontekst i Problem

Raporty systemowe mają kilka problemów z użytecznością: brak możliwości dodawania do dashboardów, kopiowanie raportu systemowego powoduje przeniesienie flagi "systemowy" na kopię (uniemożliwia edycję), oraz istnieje możliwość edycji raportów systemowych przez nieuprawnionych użytkowników (błąd). Klienci chcą móc kopiować raporty systemowe, aby je dostosować do własnych potrzeb (np. opublikować szerszej grupie użytkowników lub zmodyfikować pod swoje potrzeby).

### Zidentyfikowane Ryzyka

- Ryzyko nadpisywania modyfikacji klientów podczas aktualizacji systemu, jeśli będą edytować raporty systemowe bezpośrednio
- Ryzyko problemów z zarządzaniem kopiami raportów systemowych, jeśli będą one nadal oznaczone jako systemowe
- Ryzyko błędów w działaniu systemu, jeśli nieuprawnieni użytkownicy mogą edytować raporty systemowe

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Kopiowanie z zachowaniem flagi "systemowy" | Kopia pozostaje jako raport systemowy | ❌ Odrzucona – uniemożliwia edycję kopii |
| Kopiowanie bez flagi "systemowy" | Kopia staje się zwykłym raportem | ✅ Wybrana – umożliwia pełną edycję kopii |
| Funkcja "kopiuj" dla raportów systemowych | Nowa dedykowana funkcja kopiowania | ⏸️ Odroczona – wykorzystanie istniejącego mechanizmu grupy uprawnień |
| Wykorzystanie grupy "System Report Managers" | Administratorzy w tej grupie mogą edytować raporty systemowe | ✅ Wybrana – prostsze rozwiązanie, wykorzystanie istniejącego mechanizmu |
| Blokowanie edycji raportów systemowych | Całkowite zablokowanie edycji | ❌ Odrzucona – klienci potrzebują możliwości modyfikacji |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono następujące rozwiązania:

1. **Hotfix – dodawanie do dashboardów:**
   - Odblokowanie możliwości dodawania raportów systemowych do dashboardów
   - Po skopiowaniu na dashboard, raport automatycznie traci status "systemowy" i staje się zwykłym raportem (flaga `rep_lock` ustawiona na 0)
   - Poprawka po stronie bazy danych – zmiana wartości `rep_lock` na 0 dla raportów systemowych

2. **Edycja raportów systemowych:**
   - Wykorzystanie istniejącej grupy uprawnień "System Report Managers"
   - Administratorzy dodani do tej grupy mogą edytować raporty systemowe
   - Grupa jest obsługiwana natywnie przez system (podobnie jak role "emploi"), wymaga tylko zdefiniowania w instalacji
   - Klienci, którzy chcą zarządzać raportami systemowymi, otrzymają instrukcję: dodać grupę "System Report Managers", dodać odpowiednich użytkowników, którzy mogą zarządzać raportami systemowymi
   - Świadomość: raporty systemowe są nadpisywane przy każdej aktualizacji systemu, więc modyfikacje należy robić na kopiach

3. **Funkcja "Zapisz jako" dla raportów systemowych:**
   - Funkcja "Zapisz jako" nie powinna kopiować flagi "systemowy" (kopia staje się zwykłym raportem)
   - Po zapisaniu kopii – pełne przeładowanie widoku (kontekst nowego raportu, poprawne breadcrumbs)
   - Kopiowanie przypisania do folderów/kategorii
   - Kopiowanie wszystkich właściwości raportu (jeden do jeden, z dokładnością do nazwy)

**Szczegóły techniczne:**
- Flaga w bazie danych: `rep_lock` (0 = nie zablokowany, null/1 = zablokowany/systemowy)
- Grupa uprawnień: "System Report Managers" (nazwa musi być dokładnie taka)
- Mechanizm kopiowania: funkcja "Zapisz jako" (istniejąca funkcjonalność, wymaga poprawek)
- Dashboardy: kopiowanie raportu systemowego na dashboard automatycznie usuwa flagę "systemowy"

### Zadania

- **Anna Skupińska:** Hotfix – odblokowanie dodawania raportów systemowych do dashboardów (zmiana `rep_lock` na 0 w bazie danych)
- **Anna Skupińska:** Usunięcie błędu pozwalającego na wejście w tryb edycji raportów systemowych przez nieuprawnionych użytkowników (sprawdzenie uprawnień po stronie backendu)
- **Anna Skupińska:** Poprawka funkcji "Zapisz jako" dla raportów systemowych:
  - Nie kopiować flagi "systemowy"
  - Pełne przeładowanie widoku po zapisaniu kopii (poprawne breadcrumbs, kontekst nowego raportu)
  - Kopiowanie przypisania do folderów/kategorii
- **Damian Kamiński:** Przygotowanie artykułu instruktażowego dla klientów opisującego, jak zarządzać raportami systemowymi za pomocą grupy "System Report Managers" (można wykorzystać nagranie z ostatnich 5-10 minut spotkania)

### Punkty otwarte

- Czy funkcja "Zapisz jako" powinna kopiować wszystkie właściwości raportu, czy tylko wybrane?
- Jak dokładnie powinien działać mechanizm przeładowania widoku po "Zapisz jako" (breadcrumbs, URL, kontekst)?

---

## 2. Prezentacja raportów systemowych na liście głównej

**Projekt:** `Moduly/Raporty-systemowe`

### Kontekst i Problem

Mieszanie raportów systemowych ze zwykłymi na jednej liście jest nieczytelne. Mechanizm folderów do grupowania jest niewystarczający i podatny na błędy (wymaga zarządzania słownikami, zmiana nazw folderów systemowych może rozjeżdżać cały mechanizm). Przemek (klient) miał wymagania dotyczące widoku raportów – filtry typu "moje", "udostępnione dla mnie", które wcześniej były realizowane jako zakładki, a teraz mają być jako filtry lub sekcje.

### Zidentyfikowane Ryzyka

- Ryzyko nieuwzględnienia wymagań klienta (Przemka) dotyczących widoku raportów
- Ryzyko problemów z mechanizmem folderów, jeśli ktoś zmieni nazwy folderów systemowych
- Ryzyko konieczności wycofywania się z decyzji, jeśli nie zostanie skonsultowana z Przemkiem

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Mieszanie na jednej liście | Wszystkie raporty razem | ❌ Odrzucona – nieczytelne |
| Grupowanie folderami | Foldery do grupowania raportów systemowych | ❌ Odrzucona – mechanizm ułomny, podatny na błędy |
| Nowa sekcja "Raporty systemowe" | Osobna sekcja na liście (jak "Ulubione") | 💡 Propozycja – wymaga konsultacji z Przemkiem |
| Zakładki na górze | Filtry jako zakładki | ⏸️ Odroczona – wcześniej były zakładki, teraz mają być sekcje/filtry |
| Filtry zamiast zakładek | Filtry "moje", "udostępnione dla mnie" | 💡 Propozycja – zgodne z wymaganiami Przemka |

### Decyzja

**Status:** 🔍 Do weryfikacji

Ustalono odroczenie decyzji do czasu konsultacji z Przemkiem. Proponowane rozwiązanie:

- **Nowa sekcja "Raporty systemowe"** na liście raportów (analogiczna do sekcji "Ulubione")
- Grupowanie na podstawie flagi w bazie danych (nie folderów)
- Raporty systemowe wyświetlane w osobnej sekcji, niezależnie od folderów/kategorii
- Możliwość dodania raportów systemowych do ulubionych (niezależne od sekcji)
- Filtry "moje", "udostępnione dla mnie" jako osobne filtry (nie zakładki)

**Szczegóły techniczne:**
- Grupowanie: na podstawie flagi w bazie danych (raport systemowy), nie folderów
- Sekcja: stała sekcja "Raporty systemowe" (jak "Ulubione")
- Filtry: "moje", "udostępnione dla mnie" (zgodnie z wymaganiami Przemka)
- Foldery: służą do grupowania tematycznego, nie do wydzielania raportów systemowych

### Zadania

- **Damian Kamiński / Kamil Dubaniowski:** Konsultacja z Przemkiem dotycząca prezentacji raportów systemowych na liście (sekcja vs filtry vs zakładki)
- **Łukasz Bott:** Wstrzymanie tworzenia zadania w backlogu do czasu decyzji po konsultacji z Przemkiem

### Punkty otwarte

- Czy raporty systemowe mają być w osobnej sekcji, czy jako filtry?
- Jak dokładnie mają działać filtry "moje", "udostępnione dla mnie"?
- Czy foldery mają być całkowicie wyłączone dla raportów systemowych, czy mogą być używane do grupowania tematycznego?

---

## 3. Logowanie powiadomień systemowych – szczegóły implementacji

**Projekty:** `Klienci/WIM/Logowanie-powiadomien` + `cross-cutting/Logowanie-powiadomien`

### Kontekst i Problem

Wymagane jest logowanie wszystkich powiadomień systemowych (maili) jako ślad audytowy. Pojawiło się pytanie techniczne: jak rejestrować maile wysyłane do grup – jako jeden wpis z listą odbiorców, czy jako osobne wpisy dla każdego odbiorcy? Dodatkowo, trzeba uwzględnić przypadek, gdy użytkownik ma ustawione powiadomienie raz dziennie (zbieranie powiadomień z całego dnia).

### Zidentyfikowane Ryzyka

- Ryzyko puchnięcia bazy danych przy rejestrowaniu każdego maila osobno
- Ryzyko problemów z późniejszym raportowaniem, jeśli maile będą rejestrowane jako jeden wpis z listą odbiorców
- Ryzyko problemów z określeniem składu grupy w momencie wysłania (grupa może się zmienić w międzyczasie)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Jeden wpis z listą odbiorców | Jeden wpis z kolumną zawierającą adresy mailowe wszystkich odbiorców | ❌ Odrzucona – trudniejsze filtrowanie i raportowanie |
| Osobne wpisy per osoba | Każdy mail rejestrowany osobno dla każdego odbiorcy | ✅ Wybrana – łatwiejsze filtrowanie i raportowanie |
| Jeden wpis z dodatkową kolumną składu grupy | Wpis z informacją o składzie grupy w momencie wysłania | ⏸️ Odroczona – bardziej skomplikowane |

### Decyzja

**Status:** ✅ Zatwierdzone

Ustalono rejestrowanie powiadomień systemowych jako **osobne wpisy dla każdego odbiorcy**:

1. **Rejestrowanie per osoba:** Każdy mail wysyłany do grupy jest rejestrowany jako osobne wpisy dla każdego członka grupy
2. **Mechanizm:** Rozszerzenie istniejącego mechanizmu logowania wejść i pobrania dokumentów o nową kategorię "powiadomienia"
3. **Włączanie:** Logowanie nie jest domyślnie włączone, wymaga włączenia w ustawieniach procesu (podobnie jak logowanie wejść w sprawy)
4. **Rejestrowanie:** Na poziomie `SendMessage` – rejestracja każdego wysłanego maila osobno
5. **Powiadomienia zbiorcze:** Jeśli użytkownik ma ustawione powiadomienie raz dziennie, każde powiadomienie w zbiorczym mailu jest rejestrowane osobno

**Szczegóły techniczne:**
- Mechanizm: rozszerzenie istniejącego mechanizmu logowania (UserActivityLog lub podobny)
- Kategoria: "powiadomienia" (nowa kategoria w istniejącym mechanizmie)
- Rejestrowanie: per osoba (każdy odbiorca = osobny wpis)
- Włączanie: na poziomie procesu (ustawienie w ustawieniach procesu)
- Domyślnie: wyłączone (wymaga świadomego włączenia przez klienta)

### Zadania

- **Piotr Buczkowski:** Implementacja rejestrowania powiadomień jako osobne wpisy per osoba
- **Piotr Buczkowski:** Rozszerzenie mechanizmu logowania o kategorię "powiadomienia"

### Punkty otwarte

- Jak dokładnie będzie działać mechanizm rejestrowania dla powiadomień zbiorczych (raz dziennie)?
- Czy będą dodatkowe kolumny w tabeli logów (np. typ powiadomienia, case ID)?

---

## 4. GTA (Grant Temporary Access) – problemy z zarządzaniem

**Projekt:** `cross-cutting/GTA - dostęp tymczasowy do sparwy`

### Kontekst i Problem

GTA (Grant Temporary Access) to mechanizm udzielania jednorazowego dostępu do sprawy. Obecnie brakuje interfejsu do zarządzania tymi dostępami – nie ma możliwości przeglądu, kto ma dostęp do jakiej sprawy, od kiedy, do kiedy. Dostęp można usunąć tylko z poziomu każdej sprawy osobno, co uniemożliwia centralne zarządzanie. Dodatkowo, brakuje możliwości odbioru dostępu na życzenie (np. w przypadku pomyłki lub zmiany decyzji).

### Zidentyfikowane Ryzyka

- Ryzyko problemów z RODO – kandydaci wyrażają zgodę na obsługę, potem mogą żądać usunięcia danych, a obecnie nie ma możliwości łatwego przeglądu i usunięcia dostępów
- Ryzyko pozostawienia "wiszących" dostępów (np. dostęp pół roku po zakończeniu procesu)
- Ryzyko problemów z bezpieczeństwem, jeśli dostęp nie zostanie odebrany po zakończeniu procesu

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Brak interfejsu | Obecne podejście – dostęp tylko z poziomu sprawy | ❌ Odrzucona – nie spełnia wymagań |
| Interfejs w zakładce użytkowników | Nowa zakładka "Dostęp jednorazowy" w zarządzaniu użytkownikami | 💡 Propozycja – wymaga implementacji |
| Interfejs w ustawieniach systemowych | Zarządzanie dostępami GTA w ustawieniach | ⏸️ Odroczona – do rozważenia |

### Decyzja

**Status:** 🔍 Do weryfikacji

Ustalono, że GTA wymaga rozbudowy o interfejs zarządzania, ale nie jest to pilne (klienci nie cisną). Proponowane rozwiązanie:

- **Nowa zakładka w zarządzaniu użytkownikami:** "Dostęp jednorazowy" (GTA)
- **Funkcjonalności:**
  - Przegląd wszystkich dostępów GTA (kto, do jakiej sprawy, od kiedy, do kiedy)
  - Możliwość odbioru dostępu na życzenie
  - Filtrowanie i wyszukiwanie dostępów
  - Możliwość masowego usuwania dostępów (np. dla RODO)

**Szczegóły techniczne:**
- Lokalizacja: zakładka w zarządzaniu użytkownikami
- Tabela: istniejąca tabela GTA (odrębna tabela)
- Interfejs: read-only do przeglądu, możliwość usuwania dostępów
- Priorytet: niski (klienci nie cisną, ale warto zaopiekować w przyszłości)

### Zadania

- **Do zaplanowania:** Analiza wymagań i projekt interfejsu zarządzania dostępami GTA
- **Do zaplanowania:** Implementacja zakładki "Dostęp jednorazowy" w zarządzaniu użytkownikami

### Punkty otwarte

- Jak dokładnie powinien wyglądać interfejs zarządzania dostępami GTA?
- Czy dostęp GTA powinien być automatycznie usuwany po zakończeniu procesu?
- Jak obsłużyć przypadek RODO (masowe usuwanie dostępów na żądanie)?

---

## 5. Repozytorium – wytyczne do analizy

**Projekt:** `Klienci/WIM/Repozytorium`

### Kontekst i Problem

Otrzymano wytyczne dotyczące repozytorium, ale są nietrywialne i wymagają szczegółowej analizy. Temat nie został szczegółowo omówiony na spotkaniu ze względu na brak czasu i potrzebę eksperckiej dyskusji.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano na tym etapie (temat nie został szczegółowo omówiony)

### Rozważane alternatywy

- Brak (temat nie został szczegółowo omówiony)

### Decyzja

**Status:** ⏸️ Odroczone

Temat został odroczony na odrębne spotkanie eksperckie. Wytyczne zostały przekazane Januszowi do zapoznania się i wrzucone na kanał komunikacyjny.

### Zadania

- **Damian Kamiński:** Przekazanie wytycznych Januszowi do zapoznania się
- **Damian Kamiński:** Wrzucenie wytycznych na kanał komunikacyjny

### Punkty otwarte

- Wszystkie szczegóły wymagają analizy na odrębnym spotkaniu eksperckim

