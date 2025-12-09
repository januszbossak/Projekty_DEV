# CHANGELOG - Podgląd dokumentów

## 2025-09-09 - Rada architektów

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-09-09 Rada architektów|2025-09-09 Rada architektów]]

**Kategoria:** #Problem #Funkcjonalność

### 1. Podgląd plików tekstowych – naprawa i rozszerzenie

**Problem:**
Występuje problem z wyświetlaniem plików tekstowych (.txt) w systemie AMODIT. Pliki .txt nie wyświetlają się w podglądzie, tylko są pobierane, mimo że wcześniej działały poprawnie. Dodatkowo występuje niespójność w zachowaniu między podglądem na sprawie a podglądem w raporcie.

**Zidentyfikowane Ryzyka:**
- Brak spójności w zachowaniu podglądu między różnymi miejscami w systemie (sprawa vs raport)
- Utrata funkcjonalności, która wcześniej działała (regresja)
- Brak wsparcia dla popularnych formatów tekstowych (JSON, XML, Markdown)
- Ryzyko bezpieczeństwa przy wyświetlaniu HTML bez odpowiednich zabezpieczeń
- Problemy wydajnościowe przy niektórych typach plików (np. pliki .xlsm z makrami generują podgląd przez 5 minut)

**Decyzja:** ✅ Zatwierdzone

**Naprawa błędu z plikami .txt:**
- Przywrócenie wyświetlania plików .txt w podglądzie (naprawa regresji)
- Ujednolicenie zachowania między podglądem na sprawie a podglądem w raporcie
- Przemek zajmie się podglądami w raportach w Reactcie i zweryfikuje problem

**Rozszerzenie o dodatkowe formaty:**
- Dodanie wsparcia dla plików tekstowych: **JSON, XML, Markdown (.md), HTML, pliki logów**
- Wszystkie formaty tekstowe powinny być wyświetlane w podglądzie
- Dla Markdown w pierwszej wersji (MVP) wyświetlanie jako surowy tekst (z hashami i znacznikami)
- W przyszłości można rozważyć renderowanie Markdown z formatowaniem

**Szczegóły techniczne:**
- Pliki tekstowe należy wyświetlać w `iframe` z parametrem `sandbox` (bez `allow-script` i innych `allow-*`)
- Parametr sandbox zapewnia bezpieczeństwo przy wyświetlaniu HTML (ogranicza możliwość wykonywania skryptów i ataków)
- Lista rozszerzeń plików: **.txt, .json, .xml, .md, .html, .log**
- Możliwość wyłączenia generowania podglądu dla niektórych typów plików (np. .xlsm z makrami)
- Pliki MSG i EML nie będą obsługiwane (wymagają Outlooka lub innego klienta pocztowego)

**Zadania:**
- **Przemysław Sołdacki:** Weryfikacja i naprawa podglądu plików .txt w raportach (React)
- **Piotr Buczkowski:** Weryfikacja backendu podglądu plików tekstowych
- **Piotr Buczkowski:** Implementacja wyświetlania plików tekstowych w iframe sandbox
- **Piotr Buczkowski:** Dodanie listy rozszerzeń plików tekstowych do wyświetlania
- **Piotr Buczkowski:** Implementacja możliwości wyłączenia generowania podglądu dla niektórych typów plików

**Punkty otwarte:**
- Czy w przyszłości renderować Markdown z formatowaniem zamiast surowego tekstu?
- Czy rozważyć zastąpienie edytora Quill edytorem Markdown?
- Jakie dokładnie parametry sandbox powinny być ustawione dla iframe?

---

## 2025-11-03 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-03 Sprint review-codex.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-03%20Sprint%20review-codex.md)
**Kategoria:** #Funkcjonalność #UI

- Dolny pasek nawigacji dokumentu: przełączanie między dokumentami strzałkami lewo/prawo, dezaktywacja gdy brak poprzedniego/następnego.
- Pliki bez podglądu (np. MKV) ukrywane z listy; nazw plików przycinane dla czytelności.
- Klienci oczekują zachowania przełączania dokumentów (powrót funkcji w nowej lokalizacji interfejsu).

### 2. GetAttachmentContent – brak treści tekstowej

**Problem:**
Funkcja `GetAttachmentContent` nie zwraca treści tekstowej plików tekstowych. Zamiast tego zwraca metadane (nazwa pliku, email twórcy pliku), co jest problematyczne przy próbie użycia tej funkcji do przetwarzania treści plików tekstowych (np. w kontekście AI).

**Decyzja:** 🔍 Do weryfikacji

Funkcja `GetAttachmentContent` powinna zwracać treść tekstową plików tekstowych. Obecnie zwraca metadane (nazwa pliku, email twórcy), co jest nieprawidłowe. Wymaga weryfikacji i poprawy.

**Szczegóły techniczne:**
- Funkcja `GetAttachmentContent` jest używana do indeksowania, więc obecnie zwraca treść dla indeksowania, ale również dodaje metadane (kto stworzył plik, kto go zmodyfikował)
- Problem: na początku zwracane są dodatkowe informacje (nazwa pliku, email), które nie powinny być częścią treści
- Wymagana weryfikacja: sprawdzenie co dokładnie zwraca funkcja i poprawa, aby zwracała czystą treść tekstową

**Zadania:**
- **Janusz Bossak:** Przetestowanie funkcji `GetAttachmentContent` i zgłoszenie problemu
- **Piotr Buczkowski:** Weryfikacja i poprawa funkcji `GetAttachmentContent` – zwracanie treści tekstowej zamiast metadanych

**Punkty otwarte:**
- Czy metadane powinny być dostępne w inny sposób, czy całkowicie usunięte z odpowiedzi funkcji?
- Jak obsłużyć przypadek, gdy plik nie jest tekstowy – czy zwracać pustą treść czy błąd?
