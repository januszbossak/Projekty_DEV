# Planowanie Sprintu – 2025-11-07

**Sprint:** [nie określono]
**Okres:** [nie określono]

**Powiązane projekty:**
- `klienci/WIM/Repozytorium` – temat 1
- `klienci/WIM/Komunikator` – temat 2
- `klienci/WIM/KAS` – temat 3
- `klienci/LOT/JRWA` – temat 4
- `klienci/LOT/UPS` – temat 5
- `klienci/LOT/Global-Express` – temat 6
- `klienci/LOT/AD` – temat 7
- `klienci/WIM/Szafir` – temat 8
- `klienci/PKF` – temat 9

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| Komunikator | `klienci/WIM/Komunikator` | 🔄 W trakcie | Mateusz kończy, są drobne błędy (nie funkcjonalne, tylko przesuwanie, zmiana nazwy), grupy działają |
| Repozytorium - opis | `klienci/WIM/Repozytorium` | ✅ Ukończone | Piotr napisał opis koncepcyjny |
| Integracja z KAS | `klienci/WIM/KAS` | 🔄 W trakcie | Piotr dostał wytyczne wczoraj, ma kompletny opis, powiedział że to kilka godzin pracy |

---

## 2. Plany na sprint

### Repozytorium plików (MVP)

**Projekt:** `klienci/WIM/Repozytorium`

**Kontekst i cel:**
Moduł repozytorium plików w systemie ma na celu umożliwienie przechowywania plików poza sprawami. Kluczowe założenie: moduł będzie częścią AMODIT, jednak pliki będą zapisywane w tabeli `CaseAttachment`, tak jak pliki załączone do spraw. To rewolucyjna zmiana koncepcji w stosunku do początkowych założeń, ale wykorzystuje istniejącą infrastrukturę (około 50% rzeczy już mamy). Frontend w zasadzie mamy, trzeba go połączyć z backendem.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja MVP repozytorium (podstawowa struktura organizacyjna, CRUD, system uprawnień dla folderów pierwszego poziomu) | **Adrian** (proponowany) | [nie określono] | Czeka na zakończenie innych zadań Adriana |
| Dodanie kolumn w `CaseAttachment` określających, że wpis jest plikiem repozytorium | [do przypisania] | [nie określono] | - |
| Dodanie tabel: `RepositoryFolder`, `Repository`, `RepositoryRights`, `RepositoryHistory` | [do przypisania] | [nie określono] | - |
| Implementacja struktury fizycznej plików (podział na lata) | [do przypisania] | [nie określono] | - |
| Indeksowanie plików repozytorium (Lucene) | [do przypisania] | [nie określono] | - |

**Szczegóły techniczne:**
- Tabela: `CaseAttachment` (wykorzystanie istniejącej)
- Nowe tabele: `RepositoryFolder`, `Repository`, `RepositoryRights`, `RepositoryHistory`
- Struktura fizyczna: główny katalog "Repository", podział na lata (2025, 2026, etc.)
- Klasa: `AmodThumbnail` – generowanie podglądu standardowo jak teraz
- Konfiguracja: zgodnie z konfiguracją załączników (dysk, Blob)
- Mechanizm skanów: wykorzystanie istniejącego mechanizmu skanów (pliki nieprzypisane do sprawy, luźne elementy)

**Decyzje podjęte przy planowaniu:**
- Wykorzystanie istniejącej tabeli `CaseAttachment` zamiast tworzenia nowej struktury
- Struktura fizyczna po latach (możliwość dodatkowego podziału na miesiące)
- Struktura logiczna w aplikacji (przestrzenie, foldery) będzie rozbieżna ze strukturą fizyczną (lata)
- System uprawnień tylko dla folderów pierwszego poziomu w MVP
- Nazwy plików będą modyfikowane (dodawany AttachmentID jako prefiks) aby uniknąć konfliktów

**Ryzyka:**
- Ryzyko konfliktów nazw plików (rozwiązane przez dodanie AttachmentID jako prefiks)
- Struktura logiczna vs fizyczna może być myląca przy odtwarzaniu systemu w innym systemie (zaakceptowane jako trade-off)

**Uwagi:**
- MVP 1: podstawowa struktura organizacyjna (przestrzenie, foldery, pliki), system uprawnień tylko dla folderów pierwszego poziomu, CRUD, przechowywanie fizyczne plus metadane w bazie
- MVP 2 (przyszłość): podstawowe wyszukiwanie po nazwach, wersjonowanie, historia zmian, przenoszenie plików, przerywanie dziedziczenia, możliwość ustawienia plików jako nieusuwalne, integracja ze sprawami, metadane plików

---

### Integracja z KAS (WIM)

**Projekt:** `klienci/WIM/KAS`

**Kontekst i cel:**
Integracja z systemem KAS (centralny system zarządzania uprawnieniami) dla klienta WIM. W momencie autentykacji/autoryzacji można: po pierwsze autoryzować użytkownika, po drugie – jeśli go nie ma – w ogóle go utworzyć i w dodatku jeszcze przypisać mu od razu odpowiednie uprawnienia. KAS to centralny system zarządzania uprawnieniami, więc jeśli określą grupę AMODITową (odtworzą te same nazwy), to jak ktoś się loguje, może mu założyć konto i przypisać go od razu do odpowiednich grup albo też ról. Rola administratora musi być na sztywno ustawiona. Każde zalogowanie późniejsze może aktualizować te uprawnienia. To odpowiednik rozwiązania z Rossmanna (własny system proxy między Active Directory a AMODIT).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja integracji z KAS (autentykacja, autoryzacja, tworzenie użytkownika, przypisywanie uprawnień) | **Piotr Buczkowski** | Kilka godzin | Ma już wytyczne i kompletny opis |

**Szczegóły techniczne:**
- Autentykacja vs autoryzacja: autentykacja stwierdza że ty jesteś ty, autoryzacja daje prawa/dostęp
- Mechanizm: przy logowaniu sprawdzanie w KAS, jeśli użytkownik nie istnieje – tworzenie, przypisywanie do grup/ról
- Aktualizacja uprawnień przy każdym logowaniu

**Decyzje podjęte przy planowaniu:**
- Piotr powiedział, że to nie jest wyzwanie i mamy na to według wyceny aż 10 dniówek, więc z dużym zapasem
- Mechanizm podobny do rozwiązania z Rossmanna

**Ryzyka:**
- Brak zidentyfikowanych ryzyk

---

### Integracje dla LOT

**Projekt:** `klienci/LOT/UPS`, `klienci/LOT/Global-Express`, `klienci/LOT/AD`

**Kontekst i cel:**
Dla klienta LOT trzeba zrealizować trzy integracje do końca roku (przynajmniej w zakresie MVP):
1. **UPS** – integracja z firmą kurierską UPS (nie rozszerzenie e-Nadawcy o kolejny typ przesyłki, tylko dedykowana firma kurierska)
2. **Global Express** – kolejna firma kurierska, z którą LOT ma podpisaną umowę
3. **AD (Active Directory)** – integracja z archiwum państwowym (JRWA)

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja z UPS | **Łukasz Borowski** (proponowany) | [nie określono] | Czeka na kontakt z osobą opiekującą się LOT ze strony UPS |
| Integracja z Global Express | [do przypisania] | [nie określono] | Trzeba rozpoznać, czy mają jakieś API |
| Analiza integracji z AD (scenariusze użycia, przypadki użycia) | Dział wdrożeń | [nie określono] | Muszą pozyskać scenariusze użycia od klienta |
| Ewentualna implementacja integracji z AD (jeśli nie da się przez COLA REST) | [do przypisania] | [nie określono] | Po analizie scenariuszy użycia |

**Szczegóły techniczne:**
- UPS: podobnie jak FedEx czy DHL, jako kolejny moduł
- Global Express: trzeba rozpoznać API
- AD: możliwe że wystarczy użycie COLA REST API (dział wdrożeń może to zrobić bez dedykowanego modułu AMODIT)

**Decyzje podjęte przy planowaniu:**
- UPS i Global Express: trzeba zrobić jako dedykowane integracje (LOT ma konkretne umowy z tymi firmami)
- AD: alternatywa – czy robić jako moduł AMODIT (interfejs, backend, funkcje, reguły) czy jako MVP przez COLA REST API (dział wdrożeń może to zrobić samodzielnie)
- Decyzja o AD: najpierw analiza scenariuszy użycia, potem decyzja czy robić dedykowany moduł czy wystarczy COLA REST
- Jeśli AD przez COLA REST: możemy pomóc kolegom skonfigurować, przygotować COLA REST, powiedzieć jak wykorzystywać, jakie parametry przekazywać

**Ryzyka:**
- Łukasz Borowski może być przeciążony (UPS, Global Express, AD, inne integracje dla LOT)
- Brak kontaktu z UPS (rozwiązane – pozyskano kontakt do osoby opiekującej się LOT)
- Nie wiadomo czy Global Express ma API (wymaga rozpoznania)

**Uwagi:**
- Pomysł na przyszłość: integracja z brokerem kurierskim "Apaczka" (ma integrację ze wszystkimi firmami kurierskimi w Polsce) – wymaga zbadania kosztów i prowizji
- W LOT są jeszcze inne integracje, ale są pomniejsze i raczej da się ogarnąć

---

### JRWA dla LOT

**Projekt:** `klienci/LOT/JRWA`

**Kontekst i cel:**
JRWA (Jednolity Rzeczowy Wykaz Akt) to działanie normatywne, uregulowane ustawą i rozporządzeniem. Każdy dokument – dosłownie każdy – musi być podpięty pod JRWA. To będzie wykonywane setki razy dziennie, więc musi być robione płynnie i wygodnie – nie może być 15 kliknięć. Główne zastrzeżenie do systemów z DI: niewygodnie, nielogiczne, trzeba bardzo wiele klikać. Główna kwestia to pole "Odnośnik", które by po strukturze JRWA się poruszało (hierarchiczne przedstawienie). To będzie czynność wykonywana przy każdym dokumencie w każdym procesie (korespondencja przychodząca, wychodząca, wewnętrzna, wniosek na zarząd, delegacja, wniosek urlopowy, notatki – wszystko podlega JRWA).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Projektowanie i implementacja "Asystenta klasyfikacji" (pole odnośnik z okienkiem klasyfikatora JRWA) | [do przypisania] | [nie określono] | Wymaga dedykowanego spotkania designowego |
| Implementacja mechanizmów wyszukiwania w okienku klasyfikatora | [do przypisania] | [nie określono] | - |
| Implementacja pokazywania struktury jako drzewko | [do przypisania] | [nie określono] | - |
| Implementacja uwzględniania uprawnień do odpowiednich węzłów JRWA | [do przypisania] | [nie określono] | - |

**Szczegóły techniczne:**
- Pole "Odnośnik do procesu" z dodatkowym guzikiem "JRWA"
- Okienko klasyfikatora JRWA z mechanizmami wyszukiwania, pokazywaniem jako drzewko, uwzględnianiem uprawnień
- Logika: użytkownik szuka teczki sprawy (nie węzła JRWA), teczki są przypięte do węzłów JRWA
- Jeśli użytkownik nie wie pod co wpiąć lub stwierdza że to nowa sprawa, tworzy nową teczkę (jeśli ma uprawnienie)

**Decyzje podjęte przy planowaniu:**
- To wymaga dedykowanego spotkania designowego (pilnie, bo trzeba już zacząć robić)
- To jest rozwiązanie systemowe AMODIT (nie tylko dla LOT) – przyda się do wielu klientów (RPIK Tychy, komunalne spółki, uczelnie, szpitale)
- To jest centralny kluczowy punkt każdego procesu dla LOT

**Ryzyka:**
- Jeśli UX będzie niewygodny (15 kliknięć), klienci nie będą używać (główne zastrzeżenie do systemów z DI)
- To musi być zrobione naprawdę dobrze od strony UX-owej, żeby było najprostsze jak się da

**Uwagi:**
- Janusz wygenerował około 100+ przypadków użycia dla JRWA (są uproszczone, trzeba je zgłębiać i ewentualnie dopisywać nowe, rozdrabniać na mniejsze)
- Dla AD też są przypadki użycia wygenerowane (około 5), ale trzeba dopytać i upewnić się
- Ważne: nie my mamy robić za nich wdrożenie – teraz muszą to pociągnąć sami (daliśmy bardzo duży wkład)

---

### Podpisywanie na Macu przez Szafira (WIM)

**Projekt:** `klienci/WIM/Szafir`

**Kontekst i cel:**
Klient WIM potrzebuje obsługi podpisywania na Macu przez Szafira. To jest znane grono (2 dyrektorów), a nie nieznane grono osób. Istnieje gotowe rozwiązanie: SimpleSign (245 zł), które obsługujemy na Macu i ma działającą integrację po stronie AMODIT i TrustCenter.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja obsługi podpisywania na Macu przez Szafira | **Adrian** | [nie określono] | Adrian już to ogarnięte |

**Szczegóły techniczne:**
- Alternatywa: SimpleSign (245 zł, gotowa integracja)
- Szafir: wymaga implementacji specjalnego oprogramowania

**Decyzje podjęte przy planowania:**
- Janusz proponował kupienie SimpleSign (245 zł) jako najprostsze rozwiązanie, ale klient się uparł na Szafira

**Ryzyka:**
- Niepotrzebna praca nad funkcjonalnością, która mogłaby być rozwiązana gotowym produktem za 245 zł

---

### Konfiguracja folderów per proces (PKF)

**Projekt:** `klienci/PKF`

**Kontekst i cel:**
PKF chce konfigurować, w którym folderze mają być pliki załączone do spraw – per proces. Okazuje się, że Piotr Myszkowski mówi, że już mamy taki mechanizm na poziomie pola typu dokument. Można to łatwo rozszerzyć na poziomie procesu.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Rozszerzenie mechanizmu konfiguracji folderów na poziomie procesu | [do przypisania] | [nie określono] | Czeka na wyjaśnienie potrzeby biznesowej |

**Szczegóły techniczne:**
- Obecnie: konfiguracja na poziomie pola typu dokument
- Proponowane: rozszerzenie na poziomie procesu
- Możliwa konfiguracja mieszana: część plików w bazie danych, część w domyślnej strukturze folderu, część we wskazanych folderach per proces

**Decyzje podjęte przy planowaniu:**
- Technicznie da się zrobić, ale brakuje informacji biznesowej – po co? Co oni chcą osiągnąć?
- Łukasz Bott ma dopytać klienta o potrzebę biznesową

**Ryzyka:**
- Możliwe że jest rozwiązanie kompletnie inne, w innym miejscu
- Bez zrozumienia potrzeby biznesowej nie można podjąć właściwej decyzji technicznej

**Uwagi:**
- Przykład z Mateuszem Pietrzakiem: chciał wydobywać link do TrustCenter, żeby wysłać maila użytkownikowi że dokument jest podpisany. Odpowiedź: rola obserwator. To pokazuje wagę pytania "po co?" przed implementacją.

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Wykorzystanie tabeli `CaseAttachment` dla repozytorium zamiast nowej struktury | `klienci/WIM/Repozytorium` | ✅ Zatwierdzone | Wykorzystuje istniejącą infrastrukturę (około 50% rzeczy już mamy) |
| Struktura fizyczna plików repozytorium po latach (rozbieżna ze strukturą logiczną) | `klienci/WIM/Repozytorium` | ✅ Zatwierdzone | Zabezpiecza przed jednym wielkim workiem, użytkownik nie widzi struktury fizycznej |
| System uprawnień tylko dla folderów pierwszego poziomu w MVP | `klienci/WIM/Repozytorium` | ✅ Zatwierdzone | Ograniczenie zakresu MVP |
| AD dla LOT przez COLA REST API zamiast dedykowanego modułu (jeśli wystarczy) | `klienci/LOT/AD` | 💡 Do weryfikacji | Zależy od analizy scenariuszy użycia – jeśli wystarczy REST API, dział wdrożeń może to zrobić samodzielnie |
| JRWA jako rozwiązanie systemowe AMODIT (nie tylko dla LOT) | `klienci/LOT/JRWA` | ✅ Zatwierdzone | Przyda się do wielu klientów (RPIK Tychy, komunalne spółki, uczelnie, szpitale) |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Łukasz Borowski przeciążony (UPS, Global Express, AD, inne integracje LOT) | `klienci/LOT/UPS`, `klienci/LOT/Global-Express`, `klienci/LOT/AD` | Wysoki | Rozdzielenie zadań między różnych deweloperów | Damian Kaminski |
| Brak kontaktu z UPS | `klienci/LOT/UPS` | Średni | Rozwiązane – pozyskano kontakt do osoby opiekującej się LOT | Łukasz Bott |
| Nie wiadomo czy Global Express ma API | `klienci/LOT/Global-Express` | Średni | Trzeba rozpoznać | Łukasz Bott |
| JRWA wymaga bardzo dobrego UX (nie może być 15 kliknięć) | `klienci/LOT/JRWA` | Wysoki | Dedykowane spotkanie designowe, pilne rozpoczęcie prac | Janusz Bossak |
| Brak informacji biznesowej dla konfiguracji folderów per proces (PKF) | `klienci/PKF` | Średni | Łukasz Bott ma dopytać klienta o potrzebę biznesową | Łukasz Bott |
| Adrian może być niedostępny dla repozytorium (kończy inne zadania) | `klienci/WIM/Repozytorium` | Średni | Możliwość przypisania do innych deweloperów (Piotr, Ania, Łukasz Borowski, Adrian) | Damian Kaminski |

---

## 5. Organizacja pracy

- **Urlopy:** Łukasz Błoński na urlopie (wraca po weekendzie)
- **Spotkania:** 
  - Dedykowane spotkanie designowe dla JRWA (pilne)
  - Spotkanie z działem wdrożeń dotyczące AD (scenariusze użycia)
- **Przesunięcia:** 
  - Mateusz kończy komunikator, może zacząć działać z repozytorium w poniedziałek (jeśli nie będzie przypisany do JRWA)
  - Adrian kończy inne zadania, może być dostępny dla repozytorium
  - Łukasz Borowski zaangażowany w integracje dla LOT (UPS, Global Express, ewentualnie AD)
- **Uwagi:**
  - Janusz przygotował kompendium wiedzy o JRWA (dużo materiału)
  - Wycena dla PKF na etapie akceptacji przez Janusza
  - Wycena dla PKF zahacza o repozytorium (chcą konfigurować foldery per proces)

