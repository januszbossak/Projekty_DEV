**Data:** 2025-12-09
**Typ:** Spotkanie projektowe
**Temat główny:** Postęp roadmapy

**Źródło:** [Transkrypcja](../Transkrypcje/oczyszczone-archiwum/2025-12-09 Spotkanie projektowe - AMODIT UI - transkrypcja.md)

---

## 1. AI - Kolejkowanie dokumentów OCR

**Komponent:** AMODIT AI OCR

### Kontekst i cel

Występuje problem z dokumentami wysyłanymi do OCR-a, które przepadają przy zacięciach Azure. Dokumenty są oznaczone w AMODIT-cie jako wysłane, ale na ścieżce pomiędzy AMODIT-em a usługą OCR przepadają (np. przy zacięciu Azure, restartach). Najgorsze jest to, że po stronie AMODIT-a u klienta są oznaczone jako wysłane, ale nigdy nie wrócą - klient nie wie co wróciło, a co nie wróciło.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Wprowadzenie lokalnej kolejki dokumentów - dokumenty będą przechowywane lokalnie przez 24 godziny po wysłaniu. Dopóki nie ma potwierdzenia, że dokument został naprawdę przetworzony, system będzie się o to pingować. To zapewni, że klient nie będzie miał sytuacji, że coś wysłał i nigdy się nie doczekał.

**Szczegóły techniczne:**
- Mateusz podpiął Google OCR, na razie tylko dla procesu OCR-a
- Kolejka lokalna - przechowywanie przez 24 godziny
- Mechanizm pingowania do potwierdzenia przetworzenia

### Zadania / Dalsze kroki

- **Mateusz:** Wymyślenie i implementacja kolejki dla dokumentów OCR

---

## 2. Repozytorium plików - Status MVP i ryzyka

**Komponent:** Repozytorium

### Kontekst i cel

Repozytorium plików ma być w pełni działające do końca roku w założonym zakresie MVP. Istnieje jednak ryzyko, że WIM nie zaakceptuje rozwiązania, ponieważ ich wymagania są wyższe niż to, co produkujemy w ramach MVP. Wymagania WIM były przekazane wcześniej, ale są bardziej zaawansowane niż MVP.

### Zidentyfikowane ryzyka

- Duże ryzyko, że WIM nie zaakceptuje rozwiązania i skończy się na konsultacjach - że to nie jest repozytorium według ich rozumienia
- MVP było raczej przekazane niż konsultowane z klientem

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (MVP) / ⚠️ Ryzyko akceptacji

MVP będzie dostarczone w założonym zakresie. Cały background, w tym projekt łącznie z bazą danych, jest przygotowany na łatwą rozbudowę - nie będzie potrzeby zaorywania i zaczynania od nowa. Produkujemy mniej, ale background mamy przygotowany pod rozwój.

**Szczegóły techniczne:**
- **Uprawnienia:** Wersja uproszczona - uprawnienia do całej przestrzeni (na poziomie najwyższej gałązki/gałązek). Plan na później: uprawnienia dziedziczone i przerywane w dowolnym miejscu drzewka folderów (nie da się tego zrobić w jeden sprint)
- **Funkcjonalności MVP:** Tworzenie folderów, dodawanie plików, masowe dodawanie plików (wiele plików naraz), organizowanie repozytorium, nadawanie uprawnień na poziomie najwyższej gałązki/gałązek

### Ograniczenia / Poza zakresem

- Zaawansowane uprawnienia (dziedziczenie i przerywanie w dowolnym miejscu drzewka) - przesunięte na później
- Wszystkie wymagania WIM mają sens, ale na razie nie są obsługiwane w MVP

### Punkty otwarte

- Czy WIM zaakceptuje MVP?
- Czy w Q1 będziemy kontynuować rozwój repozytorium?

---

## 3. LOT - Eksport archiwów państwowych (ADE)

**Komponent:** Integracje

### Kontekst i cel

Dla LOT-u eksport archiwów państwowych ma wejść, ale nie w tym roku. Marek jeszcze w tym tygodniu będzie rozwijał strukturę drzewa. MVP 2 będzie zamykane w tym sprincie, MVP 3 prawdopodobnie na przyszły sprint (zależy od urlopów, ale nie jest kluczowe - to już udogodnienia). MVP 2 będzie gotowe do przekazania do LOT-u.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (przesunięcie na Q1)

Eksport archiwów państwowych dla LOT-u wejdzie w Q1. MVP 2 (zamykane w tym sprincie) będzie gotowe do przekazania do LOT-u. Pierwsza wersja będzie walidacją.

**Szczegóły techniczne:**
- Struktura drzewa - Marek rozwija w tym tygodniu
- MVP 2 - zamykane w tym sprincie, gotowe do przekazania
- MVP 3 - prawdopodobnie przyszły sprint (udogodnienia, nie kluczowe)
- Integracja z archiwum państwowym - publiczne endpointy, można wysłać paczkę przez CallRest lub bezpośrednio (bez AMODIT-a)
- Wyzwanie: wygenerowanie paczki (wymaga JRWA, kategorii archiwalnych)

### Ograniczenia / Poza zakresem

- Dział rozwoju nie jest potrzebny do integracji z archiwum państwowym (publiczne endpointy)
- Problem: brak danych do wygenerowania paczki - wdrożenie nie jest na tyle posunięte, żeby mieć dane

### Punkty otwarte

- Kiedy będą dostępne dane do wygenerowania paczki?
- Czy MVP 3 wejdzie w tym sprincie czy następnym (zależy od urlopów)?

---

## 4. Podpisy na Macu - Certyfikacja Apple

**Komponent:** Trust Center

### Kontekst i cel

Prace deweloperskie nad podpisami na Macu są zakończone. Pozostaje tylko certyfikacja Apple. Przemysław Sołdacki wysłał dowód osobisty i KRS do Apple w celu akceptacji.

### Decyzja / Ustalenie

**Status:** 🔍 Do weryfikacji (certyfikacja) / 💡 Propozycja (testy bez certyfikacji)

Prace deweloperskie zakończone - czekamy na certyfikację Apple. Jeśli WIM zgodzi się na testy bez certyfikacji, można przekazać wersję do testów (Basia zaznaczała, że to wisi na liście, ale nie ma Maca do testów).

**Szczegóły techniczne:**
- Wersja gotowa, czeka na certyfikację
- Przemysław Sołdacki sprawdzi czy przyszedł mail z Apple

### Zadania / Dalsze kroki

- **Przemysław Sołdacki:** Sprawdzenie maila z Apple dotyczącego certyfikacji
- **Damian Kamiński:** Weryfikacja czy WIM zgodzi się na testy bez certyfikacji, ewentualne przekazanie wersji do testów
- **Kamil Dubaniowski:** Oddanie swojego Maca do testów (po świętach, gdy będzie miał nowego laptopa)

### Punkty otwarte

- Kiedy Apple zaakceptuje certyfikację?
- Czy WIM zgodzi się na testy bez certyfikacji?

---

## 5. Generowanie dokumentacji

**Komponent:** AMODIT Copilot

### Kontekst i cel

MVP generowania dokumentacji jest gotowe. Potrzebne jest ustalenie wzoru dokumentacji we współpracy z Mateuszem Kołakowskim, ponieważ obecny wzór (od Piotrka Pawłowskiego, sprzed roku/1,5 roku) może być już nieaktualny. Proces jest łatwy do udokumentowania, potem raport, ustawienia systemowe, integracje - wszystko powinno być ładnie przedstawione w dokumentacji.

### Decyzja / Ustalenie

**Status:** 🔍 Do weryfikacji

Janusz ma porozmawiać z Mateuszem Kołakowskim o kierunku wzoru dokumentacji. Potrzebne wsparcie ze strony Mateusza lub kogoś od niego do akceptacji - czy dokumentacja dobrze wygląda, czy jest za szczegółowo, za mało szczegółowo.

**Szczegóły techniczne:**
- Obecny wzór: od Piotrka Pawłowskiego (sprzed roku/1,5 roku)
- Kolejność dokumentowania: proces → raport → ustawienia systemowe → integracje

### Zadania / Dalsze kroki

- **Janusz Bossak:** Rozmowa z Mateuszem Kołakowskim o wzorze dokumentacji
- **Mateusz Kołakowski (lub ktoś od niego):** Akceptacja dokumentacji - czy dobrze wygląda, poziom szczegółowości

### Punkty otwarte

- Czy obecny wzór dokumentacji jest nadal aktualny?
- Jaki poziom szczegółowości powinien mieć dokumentacja?

---

## 6. Vasco - AI OCR

**Komponent:** AMODIT AI OCR

### Kontekst i cel

Vasco ma dostęp do AI OCR na obu środowiskach. Na weekendzie podpisano mikroserwis. Na razie Google OCR dotyczy tylko procesu OCR-a, nie ASK-a.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (OCR) / 🔄 W trakcie (ASK)

Vasco ma dostęp do AI OCR (tylko OCR, nie ASK). Jest o krok od włączenia normalnie jako ASK, ale na razie jest tylko OCR - chciano jak najszybciej udrożnić Vasco.

**Szczegóły techniczne:**
- Google OCR podpięty przez Mateusza
- Dostęp na obu środowiskach
- Mikroserwis podpisany na weekendzie
- Na razie tylko OCR, nie ASK

### Punkty otwarte

- Kiedy zostanie włączony ASK dla Vasco?

---

## 7. MCP - Autentykacja i OAuth

**Komponent:** AMODIT Copilot

### Kontekst i cel

MCP ma PoC zrobiony, ale kluczowe będzie autentykacja. Bez autentykacji nie można używać. Mateusz miał rozmawiać z Piotrkiem Uczniowskim odnośnie tokenów i OAuth.

### Decyzja / Ustalenie

**Status:** 🔍 Do weryfikacji

PoC jest zrobiony, ale wymaga autentykacji. OAuth będzie robione przy okazji innego tematu - rozszerzenia integracji dla Neuca (CallRest). OAuth z CallRest będzie wykorzystane również dla MCP.

**Szczegóły techniczne:**
- PoC zrobiony
- Wymagana autentykacja (tokeny, OAuth)
- Mateusz miał rozmawiać z Piotrkiem Uczniowskim
- OAuth będzie robione przy okazji integracji CallRest dla Neuca

### Punkty otwarte

- Jakie szczegóły autentykacji dla MCP?
- Czy OAuth z CallRest będzie wykorzystane również dla MCP?

---

## 8. Neuca - Rozszerzenie integracji CallRest z OAuth

**Komponent:** Integracje

### Kontekst i cel

Neuca pytała czy mogą korzystać z innych endpointów CallRest-a. Obecna integracja ma mniej funkcjonalności niż te, które są dostępne. Okazało się, że mogą korzystać, pod warunkiem że będzie OAuth na CallRest-cie.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Rozszerzenie integracji CallRest z OAuth dla Neuca. To jest zlecenie - Neuca za to płaci.

**Szczegóły techniczne:**
- OAuth na CallRest-cie
- Rozszerzenie integracji dla Neuca
- Zlecenie płatne

### Ograniczenia / Poza zakresem

- OAuth będzie wykorzystane również dla MCP (przy okazji tego tematu)

---

## 9. MCP serwer - Autentykacja, uprawnienia i bezpieczeństwo

**Komponent:** AMODIT Copilot

### Kontekst i cel

MCP serwer ma być dostarczony w Q1 (im wcześniej tym lepiej, bo klienci chcą to mieć). Kluczowe wyzwanie to bezpieczeństwo - autentykacja, uprawnienia, kontrola dostępu AI do danych. Przykładowe case: klient typu Rossmann czy Polpharma buduje swojego agenta, który chodzi po SharePointcie i innych miejscach, ale powinien znajdować rzeczy również w AMODIT-cie - w kontekście użytkownika i z jego uprawnieniami.

### Zidentyfikowane ryzyka

- Najtrudniejsza część: bezpieczeństwo - uprawnienia, kontrola dostępu, rejestrowanie działań AI
- Ryzyko wycieku danych wrażliwych przez AI
- Potrzeba mechanizmu wyłączenia rejestrowania odczytów ze względów bezpieczeństwa

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone (Q1) / 🔍 Do weryfikacji (szczegóły bezpieczeństwa)

MCP serwer ma być dostarczony w Q1. MVP powinien mieć sensowne logowanie, nawet jeśli na razie nie w pełni zrobione, ale bezpieczne. Lucyna sprzedała Proof of Concept trzymiesięczny - klienci będą mogli korzystać, potrzebują tego co mamy i MCP.

**Szczegóły techniczne:**
- **Dwa kierunki:**
  - AMODIT Copilot/ASK korzysta z zewnętrznych serwerów MCP - autentykacji za bardzo nie potrzeba
  - Zewnętrzny Copilot/GPT odpyta AMODIT-a - wymaga autentykacji i uprawnień
- **Uprawnienia:**
  - Agent działa w kontekście zalogowanego użytkownika - sprawdza z jego uprawnieniami
  - Możliwość konta systemowego - agent zalogowany syntetycznie, z określonymi uprawnieniami (dostęp do tych i tych danych, nie do innych)
- **Mechanizm kontroli:**
  - Checkbox na poziomie procesu: "Pozwól AI dostawać się do tego procesu" (domyślnie nie zaznaczony)
  - Nawet jeśli użytkownik ma uprawnienia, może nie chcieć żeby AI grzebało w procesie
- **Rejestrowanie:**
  - Jeśli AI coś zmienia - musi się odkładać w historii sprawy
  - Możliwość wyłączenia rejestrowania odczytów (ze względów bezpieczeństwa)
  - Jeśli AI potwierdzi dane wrażliwe - powinno być zarejestrowane

### Ograniczenia / Poza zakresem

- Rozwój AI poza AMODIT-a - klienci mają swoje narzędzia (AI Studio, etc.), podpinają się do AMODIT-a
- AMODIT nie musi się martwić rozwojem AI - klienci rozwijają, AMODIT pilnuje bezpieczeństwa

### Punkty otwarte

- Czy ASK będzie miał dostęp do Internetu (wyszukiwarka Bing lub inna)? Mateusz mówił, że generalnie by się dało - trzeba ustalić szczegóły (czy za darmo, czy trzeba płacić za API)
- Jakie szczegóły autentykacji dla kont systemowych?
- Jakie szczegóły mechanizmu checkbox "Pozwól AI dostawać się do tego procesu"?

---

## 10. ASK - Dostęp do Internetu

**Komponent:** AMODIT Copilot

### Kontekst i cel

💭 Pomysł Przemka: ASK na razie nie ma dostępu do Internetu. Prompty często szukają informacji w necie. Mateusz mówił, że generalnie by się dało. To by rozszerzało możliwości - np. w procesie zadań menedżerskich AI mogłoby sprawdzić czy zadanie jest zgodne ze strategią i dać rekomendacje, sprawdzając rzeczy w internecie.

### Decyzja / Ustalenie

**Status:** 💡 Propozycja

💭 Pomysł Przemka: Dostęp do Internetu dla ASK - wymaga rozważenia. Musi być włączane świadomie (pozwalam korzystać z neta albo nie pozwalam). Jeśli chcemy żeby coś poszukało, żeby mogło szukać. To jest temat, który wyszedł po drodze i pewnie nie tylko Przemkowi wyjdzie, klientom też. Na razie do rozpoznania.

**Szczegóły techniczne:**
- Dostęp do wyszukiwarki (Bing lub inna)
- Włączane świadomie przez użytkownika
- Trzeba ustalić szczegóły: czy za darmo, czy trzeba płacić za dostęp do API

### Punkty otwarte

- Czy dostęp do Internetu będzie dostępny w ASK?
- Jakie koszty API wyszukiwarki?
- Jakie szczegóły implementacji?

