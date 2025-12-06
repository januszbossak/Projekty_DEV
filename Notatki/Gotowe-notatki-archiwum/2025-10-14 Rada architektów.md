> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

# Rada Architektów – 2025-10-14

**Powiązane projekty:**
- `Moduly/e-Doreczenia` – temat 1
- `Moduly/Raporty-systemowe` – temat 2
- `Moduly/Zrodla-danych` – temat 2
- `cross-cutting/Interfejs-sprawy/Formularz-sprawy` – temat 3
- `cross-cutting/Wydajnosc` – temat 4
- `cross-cutting/Wzmiankowanie-w-komentarzach` – temat 5
- `Moduly/Trust-Center` – temat 6

---

## 1. Problem z działaniem e-doręczeń z różnych serwerów AS

**Projekt:** `Moduly/e-Doreczenia`

### Kontekst i Problem

Występuje problem z niespójnością dokumentacji e-doręczeń od Poczty Polskiej – 2 miesiące temu otrzymano inną wersję dokumentacji niż oficjalna. Wszystko wymaga testowania na 2 razy. Teoria: mogą być różne API lub różne intencje z różnymi implementacjami między maszynami Poczty Polskiej, co powoduje przekierowania między różnymi API.

Problem występuje gdy są uruchomione 2 usługi produkcyjne (2 ASy) jednocześnie – wtedy z jednego AS nie działa, z drugiego działa. Gdy jest uruchomiony tylko jeden AS, działa poprawnie. Oba ASy mają to samo wychodzące IP (20.56.84.214), te same certyfikaty, tę samą wersję programowania i ustawienia.

### Zidentyfikowane Ryzyka

- Możliwe ograniczenia po stronie Poczty Polskiej dotyczące liczby równoczesnych połączeń z jednego IP
- Problem konfiguracji po stronie AMODIT (konkurencyjne żądania zbyt szybkie)
- Niespójność dokumentacji API może prowadzić do błędnych implementacji

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ustawienie preferred server (AS-01 lub AS-02) | Zawsze używać jednego konkretnego AS dla tej usługi | 🔍 Do weryfikacji – wymaga testów |
| Analiza konfiguracji serwerów | Sprawdzenie ustawień współpracy między serwerami | ✅ Wybrana – intensywna współpraca Piotra i Adriana |

### Decyzja

**Status:** 🔍 Do weryfikacji

Piotr Buczkowski i Adrian Kotowski będą intensywnie pracować wspólnie nad znalezieniem rozwiązania. Podejrzenie, że problem leży po stronie konfiguracji serwerów AMODIT, a nie po stronie Poczty Polskiej.

**Szczegóły techniczne:**
- Wychodzące IP: 20.56.84.214 (wspólne dla obu ASów)
- Problem występuje tylko gdy oba ASy są uruchomione jednocześnie
- Na testówce potwierdzono, że Poczta może ograniczać połączenia z jednego serwera

### Zadania

- **Piotr Buczkowski, Adrian Kotowski:** Intensywna współpraca nad rozwiązaniem problemu e-doręczeń → termin: do ustalenia

### Punkty otwarte

- Czy Poczta Polska ogranicza liczbę równoczesnych połączeń z jednego IP?
- Czy problem wynika z konfiguracji serwerów AMODIT?
- Czy ustawienie preferred server rozwiąże problem?

---

## 2. Przejście źródeł systemowych z ujemnych ID na GUID i flagę systemową

**Projekt:** `Moduly/Raporty-systemowe`, `Moduly/Zrodla-danych`

### Kontekst i Problem

Źródła systemowe używają ujemnych ID do odróżnienia od źródeł użytkowniczych. To powoduje problemy techniczne:
- Synchronizacja źródeł systemowych wywala się na składni SQL (np. `DPSRC_-22` powoduje błąd składniowy)
- Dashboardy systemowe mają problem z podmianą ID – najpierw tworzone są dashboardy z placeholderami (GUID), potem raporty, a następnie trzeba podmienić GUID na rzeczywiste ID raportów
- Raporty systemowe mają stare GUID, które są rozpoznawane, ale ujemne ID są używane w źródłach danych

Problem z dashboardami został już rozwiązany przez Anię Skupińską (kod wczoraj), ale pojawiła się szersza dyskusja o sensowności używania ujemnych ID.

### Zidentyfikowane Ryzyka

- Migracja istniejących źródeł systemowych z ujemnych ID na dodatnie może popsuć istniejące raporty klientów korzystających ze źródeł systemowych
- Brak kompatybilności wstecznej może wymagać ręcznej konfiguracji u klientów
- Ryzyko jest jednak ocenione jako bardzo niskie – prawdopodobnie nikt nie korzysta z tych źródeł systemowych do tworzenia własnych raportów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zachowanie ujemnych ID | Pozostanie przy obecnym rozwiązaniu | ❌ Odrzucona – powoduje problemy techniczne (synchronizacja, składnia SQL) |
| Przejście na GUID + flaga systemowa | Dodanie kolumny `GUID` i `SystemOrigin` zamiast ujemnych ID | ✅ Wybrana – prawidłowe rozwiązanie techniczne |
| Migracja z kompatybilnością wsteczną | Obsługa zarówno ujemnych jak i dodatnich ID podczas migracji | ⏸️ Odroczona – prawdopodobieństwo użycia przez klientów ocenione jako zerowe |

### Decyzja

**Status:** ✅ Zatwierdzone

Przejście na GUID dla źródeł systemowych zamiast ujemnych ID. Dodanie kolumn: `GUID` i `SystemOrigin` (flaga wskazująca że źródło jest systemowe). Kompatybilność wsteczna zostaje przerwana – jeśli ktoś korzystał ze źródeł systemowych, będzie wymagał ręcznej konfiguracji (w razie potrzeby bezpłatna pomoc serwisu).

**Szczegóły techniczne:**
- Kolumna `GUID` dla źródeł danych (zamiast ujemnych ID)
- Kolumna `SystemOrigin` (flaga systemowa)
- Raporty systemowe już mają stare GUID, które są rozpoznawane
- Dashboardy systemowe: problem z podmianą ID już rozwiązany przez Anię

### Zadania

- **Anna Skupińska, Łukasz Bott:** Zaplanowanie przejścia na GUID dla źródeł systemowych i raportów systemowych → termin: na następną radę (za 2 dni)
- **Anna Skupińska, Łukasz Bott:** Przeanalizowanie wszystkich konsekwencji używania GUID w raportach, dashboardach, starych raportach, skrajnych przypadków

### Punkty otwarte

- Czy przejść na GUID również dla raportów (nie tylko źródeł)?
- Jakie są wszystkie konsekwencje techniczne przejścia na GUID?

---

## 3. Wyświetlanie zagnieżdżonych tabel w formularzu sprawy

**Projekt:** `cross-cutting/Interfejs-sprawy/Formularz-sprawy`

### Kontekst i Problem

W nowej wersji formularza sprawy zagnieżdżone tabelki w trybie formularzowym nie wyświetlają się wcale (błąd krytyczny). W wersji marcowej działały, ale z problemami. W wersji mobilnej zagnieżdżone tabelki są wyświetlane jako formularz (pionowo z przewijaniem poziomym), niezależnie od ustawień.

Problem dotyczy przypadku, gdy tabela nadrzędna jest wyświetlana w trybie formularzowym, a zawiera zagnieżdżoną tabelkę. Kod został mocno przerobiony przez kilka osób, co spowodowało bałagan i utratę funkcjonalności.

### Zidentyfikowane Ryzyka

- Funkcjonalność jest bardzo rzadko używana (ocena: raz na 5 lat w przypadku Damiana, raz w przypadku Łukasza)
- Naprawa może zająć 2-5 dni pracy Mariusza
- Brak zgłoszeń od konsultantów dotyczących tej funkcjonalności sugeruje, że nikt z niej nie korzysta

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Przywrócenie działania jak w wersji marcowej | Naprawa błędu i przywrócenie poprzedniego zachowania | 🔍 Do weryfikacji – wymaga proof of concept (1 dzień) |
| Wymuszenie trybu formularzowego dla podtabel | Jeśli tabela nadrzędna jest formularzowa, podtabela też musi być formularzowa | 💡 Propozycja – do rozważenia |
| Całkowite wyłączenie zagnieżdżonych tabel w trybie formularzowym | Dokumentacja: "w trybie formularzowym nie wspieramy zagnieżdżonych tabel" | 💡 Propozycja – jeśli naprawa okaże się zbyt skomplikowana |
| Zgodność z widokiem mobilnym | Na desktopie tak samo jak na mobilnym (formularz pionowy z przewijaniem) | 💡 Propozycja – do rozważenia |

### Decyzja

**Status:** 🔍 Do weryfikacji

Mariusz Piotrzkowski i Piotr Buczkowski mają 1 dzień na proof of concept – sprawdzenie czy przywrócenie działania jak w wersji marcowej jest proste czy skomplikowane. Na czwartkową radę przedyskutują dalsze kroki.

**Szczegóły techniczne:**
- Problem występuje tylko w nowej wersji formularza
- W wersji mobilnej zagnieżdżone tabelki działają (wyświetlane jako formularz pionowy)
- Kod został mocno zmieniony przez kilka osób, co spowodowało bałagan
- Porównanie plików między wersjami pokazuje duże różnice w renderowaniu

### Zadania

- **Mariusz Piotrzkowski, Piotr Buczkowski:** Proof of concept – sprawdzenie czy przywrócenie działania jak w wersji marcowej jest proste → termin: do czwartku (następna rada)
- **Mariusz Piotrzkowski:** Lista zadań do przekazania innym (jeśli będzie za dużo pracy)

### Punkty otwarte

- Czy przywrócenie działania jest proste czy skomplikowane?
- Czy warto poświęcać czas na funkcjonalność, z której nikt nie korzysta?
- Jakie jest docelowe zachowanie zagnieżdżonych tabel w trybie formularzowym?

---

## 4. Problem z wydajnością List View 2.0 – pobieranie wszystkich użytkowników

**Projekt:** `cross-cutting/Wydajnosc`

### Kontekst i Problem

Przy wejściu na List View 2.0 pobierani są wszyscy użytkownicy systemu, mimo że najpewniej nikt z tego nie skorzysta. Podobny problem występuje w formularzach – pobierane są wszystkie pozycje słownika, wszyscy użytkownicy, wszystkie słowniki przy wejściu, nawet jeśli użytkownik nie skorzysta z tych funkcji.

Przykład: w Enence jest 200 000 użytkowników, co powoduje poważny problem wydajnościowy. Problem występuje również w edytorze uprawnień do pola – pobierani są wszyscy użytkownicy nawet jeśli użytkownik nie dotknie matrycy decyzyjnej uprawnień.

### Zidentyfikowane Ryzyka

- Poważne problemy wydajnościowe w systemach z dużą liczbą użytkowników (np. Enence: 200 000 użytkowników)
- Niepotrzebne obciążenie serwera i bazy danych
- Deweloperzy testują na małych środowiskach i bagatelizują problem

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Pobieranie na żądanie | Dane pobierane dopiero gdy użytkownik rozwinie filtr/menu | ✅ Wybrana – prawidłowe podejście |
| Stronicowanie i wyszukiwanie | Jeśli już pobierać, to ze stronicowaniem i wyszukiwaniem | ✅ Wybrana – dodatkowe ulepszenie |

### Decyzja

**Status:** ✅ Zatwierdzone

Dane powinny być pobierane dopiero gdy użytkownik faktycznie potrzebuje ich użyć (np. rozwinięcie filtra, otwarcie menu). Jeśli już pobierać, to ze stronicowaniem i wyszukiwaniem. Kamil Dubaniowski ma porozmawiać z chłopakami (Filip i inni), żeby sami się pilnowali i zwracali uwagę na takie problemy.

**Szczegóły techniczne:**
- List View 2.0: pobieranie wszystkich użytkowników przy wejściu
- Formularze: pobieranie wszystkich pozycji słownika, wszystkich użytkowników, wszystkich słowników
- Edytor uprawnień do pola: pobieranie wszystkich użytkowników nawet bez dotykania matrycy decyzyjnej
- Edytor graficzny (Przemek): podobny problem

### Zadania

- **Kamil Dubaniowski:** Rozmowa z Filipem i innymi deweloperami o problemie pobierania wszystkich danych → termin: natychmiast
- **Kamil Dubaniowski:** Weryfikacja i poprawa miejsc, gdzie pobierane są wszystkie dane zamiast na żądanie

### Punkty otwarte

- Jak pilnować, żeby takie problemy nie występowały w przyszłości?
- Czy potrzebna jest dodatkowa walidacja code review?

---

## 5. Wzmiankowanie w komentarzach gdy wyłączone DWI

**Projekt:** `cross-cutting/Wzmiankowanie-w-komentarzach`

### Kontekst i Problem

Gdy w ustawieniach procesu wyłączone jest DWI (Dostęp Wewnętrzny Informacyjny) i dodawanie do DWI/contributor, w nowej wersji nie można oznaczać osób w komentarzach. To nie jest błąd, ale pytanie czy to jest prawidłowe działanie.

Problem: jest 50 osób z dostępem do sprawy, mają uprawnienia, ale nie można ich oznaczyć w komentarzach, bo wyłączone jest dodawanie do DWI. Nowych nie można dodawać, ale dlaczego nie można oznaczyć tych 50, które już mają uprawnienia?

Obecna logika: jeśli wyłączone jest dodawanie do DWI, to nie można oznaczać w ogóle (ani nowych, ani obecnych). To jest zależne od ustawienia DWI lub contributor (w zależności od konfiguracji).

Dodatkowy problem: gdy ktoś zostaje wzmiankowany po raz pierwszy, nie dostaje maila. Dopiero przy drugim wzmiankowaniu dostaje maila "został dodany nowy komentarz", a nie "zostałeś wzmiankowany". Brak dedykowanego powiadomienia o wzmiankowaniu.

### Zidentyfikowane Ryzyka

- Niezgodność z oczekiwaniami użytkowników – osoby z dostępem do sprawy powinny móc być wzmiankowane
- Brak powiadomień o wzmiankowaniu może prowadzić do pominięcia ważnych informacji
- Mieszanie logiki DWI i wzmiankowania powoduje niejasności

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rozdzielenie DWI i wzmiankowania | Osobne ustawienie dla wzmiankowania, niezależne od DWI | ✅ Wybrana – docelowe rozwiązanie, ale wymaga większych zmian |
| Wzmiankowanie osób z dostępem do sprawy zawsze możliwe | Jeśli DWI wyłączone, można wzmiankować tylko osoby już mające dostęp | ✅ Wybrana – szybka poprawka na teraz |
| Zmiana nazwy ustawienia | "DWI i wzmiankowanie" zamiast tylko "DWI" | 💡 Propozycja – do rozważenia przy większych zmianach |
| Dedykowane powiadomienie o wzmiankowaniu | Osobny mail "zostałeś wzmiankowany" zamiast "dodano komentarz" | ✅ Wybrana – zadanie już przypisane |

### Decyzja

**Status:** ✅ Zatwierdzone (częściowo), 💡 Propozycja (częściowo)

**Szybka poprawka na teraz:** Wzmiankowanie osób, które już mają dostęp do sprawy, powinno być zawsze możliwe, niezależnie od ustawienia DWI. Wyłączenie DWI oznacza tylko, że nie można dodawać nowych osób do DWI spoza sprawy.

**Docelowe rozwiązanie:** Rozdzielenie logiki DWI i wzmiankowania – osobne ustawienie dla wzmiankowania. To wymaga większych zmian i przepięcia logiki (nie da rady na ten sprint).

**Dodatkowo:** Dodać dedykowane powiadomienie mailowe o wzmiankowaniu (zadanie już przypisane przez Kamil).

**Szczegóły techniczne:**
- Obecnie wzmiankowanie jest zależne od ustawienia DWI lub contributor
- Wzmiankowanie fizycznie dodaje osobę do DWI
- Przy pierwszym wzmiankowaniu nie ma powiadomienia mailowego
- Przy drugim wzmiankowaniu jest mail "dodano komentarz", a nie "zostałeś wzmiankowany"

### Zadania

- **Mariusz Piotrzkowski:** Poprawka logiki wzmiankowania – możliwość wzmiankowania osób z dostępem do sprawy nawet gdy DWI wyłączone → termin: nie da rady na ten sprint (za dużo pracy)
- **Kamil Dubaniowski:** Przeróbka forty pod kątem tego, co zabierać (priorytetyzacja zadań Mariusza)
- **Mariusz Piotrzkowski:** Lista rzeczy do przekazania innym (jeśli będzie za dużo pracy)
- **Kamil Dubaniowski:** Dedykowane powiadomienie mailowe o wzmiankowaniu (zadanie już przypisane)

### Punkty otwarte

- Jak rozdzielić logikę DWI i wzmiankowania w przyszłości?
- Czy zmienić nazwę ustawienia na "DWI i wzmiankowanie"?
- Czy potrzebna jest osobna rola "obserwator" (tylko odczyt, powiadomienia o zmianie stanu)?

---

## 6. Temat odroczony: Blockchain (Marek Dziakowski)

**Projekt:** `Moduly/Trust-Center`

### Kontekst i Problem

Marek Dziakowski zgłasza temat związany z blockchainem. Potrzebna jest decyzja jak to robić, związane z kosztami. Temat wymaga obecności Janusza Bossaka.

### Decyzja

**Status:** ⏸️ Odroczone

Temat przełożony na czwartkową radę. Marek ma przygotowany dokument techniczny i może skonsultować się z kolegami przed radą.

### Zadania

- **Marek Dziakowski:** Przygotowanie postulatu technicznego na czwartkową radę → termin: czwartek

