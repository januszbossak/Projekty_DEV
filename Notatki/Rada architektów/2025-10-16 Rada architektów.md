# Rada Architektów – 2025-10-16

**Powiązane projekty:**
- `moduly/Trust-Center` – temat 1
- `moduly/Zrodla-danych` – temat 2

---

## 1. TrustCenter – wydzielenie funkcjonalności dodawania do blockchaina do osobnego serwisu

**Projekt:** `moduly/Trust-Center`

### Kontekst i Problem

W TrustCenter występuje problem z funkcjonalnością dodawania plików do blockchaina. Aktualnie zadanie jest wykonywane przez 2 serwery webowe, które czasami jednocześnie dodają dokumenty do tego samego ostatniego bloku. W takiej sytuacji jeden z serwerów wisi i nic nie jest do niego dalej podłączane. Problem narasta wraz ze skalą TrustCenter – pół roku temu było 2-4 dokumenty wiszące, obecnie jest ich ponad 50. Skala TrustCenter drastycznie się zmienia z roku na rok, więc rozwiązanie musi być kompleksowe, a nie obejście przez blokady czy inne mechanizmy, które na większej skali się nie sprawdzą.

TrustCenter jest zawsze u nas, tylko na chmurze (nie ma instalacji on-premise u klientów), więc możemy korzystać z rozwiązań chmurowych Azure. W przeciwieństwie do AMODIT, który jest instalowany w kilkudziesięciu lokalizacjach u klientów, gdzie często nie ma nawet administratora i wszystko musiałoby być robione rękami wdrożeniowców.

### Zidentyfikowane Ryzyka

- Rosnąca liczba dokumentów wiszących (z 2-4 do ponad 50 w ciągu pół roku)
- Brak możliwości skalowania przy obecnym podejściu
- Ryzyko psucia blockchaina przy jednoczesnym dodawaniu dokumentów przez wiele serwerów
- Brak możliwości równoległego przetwarzania (musi być po kolei)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Microservice w Dockerze (Azure Container Instances) | Wydzielenie funkcjonalności do osobnego kontenera Docker, działającego na Azure, korzystającego z kolejki | ✅ Wybrana – podobne podejście jak u Mateusza, łatwe zarządzanie, możliwość późniejszego skalowania wertykalnego, brak przestojów przy aktualizacji |
| Lokalna usługa na serwerze | Wydzielenie do osobnej usługi działającej na jednym serwerze, która sprawdza kolejkę w bazie danych | ⏸️ Odroczona – na początku rozważana jako najszybsza opcja, ale ostatecznie wybrano podejście Dockera dla spójności |
| SignalR Service (Azure) | Użycie Azure SignalR Service do powiadamiania przeglądarki o zakończeniu zadania | ⏸️ Odroczona – do drugiego kroku, po wydzieleniu funkcjonalności |
| Service Bus / Event Grid | Użycie Azure Service Bus lub Event Grid jako brokera komunikatów między serwisami | ❌ Odrzucona – Piotr próbował wcześniej OCR przez kolejkowanie, nie udało się; kolejkowanie nie jest do przesyłania plików (za duże), tylko małych komunikatów |
| Druga kolejka zadań wykonanych | Serwery webowe odpytywałyby kolejkę zadań wykonanych | ❌ Odrzucona – lepiej użyć SignalR, żeby użytkownik dostawał automatyczne powiadomienie zamiast ręcznego odświeżania |

### Decyzja

**Status:** ✅ Zatwierdzone

Wydzielenie funkcjonalności dodawania dokumentów do blockchaina do osobnego microservice w Dockerze, działającego na Azure Container Instances. Serwisy webowe będą zgłaszały zadania do kolejki, a worker będzie je przetwarzał po kolei (zachowanie kolejności jest krytyczne). 

**Szczegóły techniczne:**
- Architektura: Microservice w Dockerze (podobnie jak rozwiązanie Mateusza dla AI)
- Kolejka: Azure Queue Storage lub Service Bus (do ustalenia)
- Worker: Jeden worker przetwarzający zadania sekwencyjnie (nie można równolegle, bo psuje blockchain)
- Komunikacja: Na początku bez SignalR – użytkownik będzie musiał odświeżyć stronę lub poczekać na maila z informacją o dodaniu do blockchaina
- Baza danych: Ta sama baza co TrustCenter (worker ma dostęp do tych samych zasobów)
- Skalowanie: Na razie jeden worker, w przyszłości możliwe skalowanie wertykalne (więcej CPU/RAM dla jednej instancji) lub horyzontalne (wiele workerów) jeśli kolejka będzie gigantyczna, ale to wymagałoby zmiany założeń

**Plan wdrożenia:**
- Pierwszy krok: Wydzielenie do microservice bez SignalR (nawet z ograniczeniem funkcjonalności powiadomień)
- Drugi krok (w przyszłości): Dodanie SignalR Service dla automatycznych powiadomień użytkownika
- Możliwe późniejsze przejście na Kubernetes (docker compose jest prostszym rozwiązaniem na razie)

### Zadania

- **Marek Dziakowski:** Wydzielenie funkcjonalności dodawania do blockchaina do microservice w Dockerze → termin: następny sprint
- **Marek Dziakowski:** Uzyskanie akceptacji kosztów Azure Container Instances od Janusza (wysłany dokument do przejrzenia)
- **Marek Dziakowski:** Konsultacja z Łukaszem Podsklepką i Joanną dotycząca doświadczeń z podobnymi rozwiązaniami
- **Adrian Kotowski:** Przesłanie informacji o możliwości powiązania Event Grid z SignalR przez Azure Service Bus (artykuł z dokumentacji Microsoft)

### Punkty otwarte

- Czy użyć Azure Queue Storage czy Service Bus jako kolejki?
- Czy w przyszłości będzie potrzeba wielu workerów (skalowanie horyzontalne) czy wystarczy skalowanie wertykalne?
- Czy obsłużyć sytuację gdy 2 osoby naraz próbują podpisać ten sam dokument? (Marek jest prawie pewien, że to nie jest obsłużone, Rafał kiedyś o tym mówił)
- Czy SignalR będzie działał między microservice a witryną TrustCenter (CORS, konfiguracja)?

---

## 2. Źródła danych systemowe – zmiana identyfikatorów z ujemnych na dodatnie i dodanie GUID

**Projekt:** `moduly/Zrodla-danych`

### Kontekst i Problem

Źródła danych systemowe mają obecnie ujemne identyfikatory, co powoduje problemy z identyfikacją i synchronizacją między środowiskami. Potrzebne jest wprowadzenie dodatnich identyfikatorów oraz GUID dla wszystkich źródeł danych, aby umożliwić łatwe przenoszenie definicji źródeł między środowiskami (testowe, docelowe) oraz eksport-import definicji źródeł i dashboardów poprzez pliki.

### Zidentyfikowane Ryzyka

- Brak możliwości łatwego przenoszenia konfiguracji źródeł danych między środowiskami
- Problemy z identyfikacją źródeł systemowych w module raportowym
- Brak mechanizmu eksportu-importu definicji źródeł i dashboardów

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzenie dodatnich identyfikatorów oraz GUID dla wszystkich źródeł danych systemowych. Dotychczasowe źródła z ujemnymi identyfikatorami pozostaną bez zmian i będą sukcesywnie zamieniane lub pozostawione (w zależności od wymagań zmian).

**Szczegóły techniczne:**
- Nowe kolumny w bazie danych: `czy_systemowe` (flaga), `GUID` (dla wszystkich źródeł)
- Źródła systemowe będą oznaczone jako systemowe, będą miały dodatnie identyfikatory i GUID
- Wszystkie źródła (nie tylko systemowe) będą miały GUID (na wszelki wypadek, nawet jeśli na razie nie będą używane)
- Zmiany wymagane w miejscach korzystających ze źródeł systemowych:
  - Moduł raportowy (głównie backend)
  - Wszystkie miejsca odwołujące się do źródeł danych systemowych po ujemnych indeksach
  - Zmiana logiki pobierania źródeł systemowych z ujemnych na dodatnie indeksy
- Odwołania do źródeł zewnętrznych (typu odnośnik do źródła danych) również będą musiały być zaktualizowane

### Zadania

- **Anna Skupińska:** Dodanie kolumn `czy_systemowe` i `GUID` do tabeli źródeł danych
- **Anna Skupińska:** Generowanie GUID dla wszystkich źródeł danych (nie tylko systemowych)
- **Anna Skupińska:** Zmiana identyfikatorów źródeł systemowych z ujemnych na dodatnie
- **Anna Skupińska / Zespół:** Aktualizacja wszystkich miejsc w kodzie korzystających ze źródeł systemowych (głównie moduł raportowy, backend) – zmiana z ujemnych na dodatnie indeksy
- **Anna Skupińska / Zespół:** Aktualizacja logiki odwołań do źródeł zewnętrznych (typu odnośnik do źródła danych)

### Punkty otwarte

- Które miejsca dokładnie wymagają zmian (wymaga analizy kodu)?
- Czy wszystkie źródła powinny mieć GUID od razu, czy tylko systemowe na początku? (Decyzja: wszystkie na wszelki wypadek)

