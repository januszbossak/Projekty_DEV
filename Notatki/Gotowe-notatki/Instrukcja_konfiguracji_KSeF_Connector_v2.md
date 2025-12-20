Instrukcja konfiguracji integracji Amodit z KSeF Connector v2

_Wersja dokumentu: 2.0 Data: 2025-12-08  
  

# Wprowadzenie — co to w ogóle jest?

Zanim zaczniemy konfigurować, wyjaśnijmy sobie **o co tu chodzi**.  

## Co to jest KSeF?  


**Krajowy System e-Faktur** to rządowy system, do którego firmy muszą wysyłać i z którego pobierają faktury w formie elektronicznej (format XML). To wymóg ustawowy.  

## Co to jest KSeF Connector?  

To **pośrednik** między KSeF a systemami biznesowymi (jak AMODIT). KSeF Connector:

Pobiera faktury zakupowe z KSeF

Wysyła faktury sprzedażowe do KSeF

Przekazuje dane faktur do AMODIT, gdzie uruchamiają się procesy biznesowe (akceptacja, księgowanie itd.)  

## Jak to działa w praktyce?  

Kontrahent wystawia fakturę
↓
System KSeF (rząd)
↓
KSeF Connector (pobiera fakturę)
↓
AMODIT (tworzy sprawę w obiegu faktur)
↓
Proces biznesowy (weryfikacja, akceptacja, księgowanie)

# 1. Wymagania wstępne

## 1.1. Minimalna wersja Amodit

**WAŻNE: Wymagana minimalna wersja Amodit: 250630.133**

Ta wersja wprowadza kluczowe zmiany w integracji z KSeF Connector, które zapewniają stabilność i funkcjonalność opisaną w niniejszej instrukcji.

## 1.2. Kluczowe zmiany wprowadzone w wersji 250630.133

*> *Uwaga: Te funkcjonalności nie są dostępne w konfiguracji z Jobem (Amodit jako inicjator).**

### Zwrotne CaseId po rejestracji faktury

W trybie synchronicznym KSeF Connector otrzymuje CaseId bezpośrednio po rejestracji faktury w systemie Amodit, analogicznie jak w AMODIT REST API przy użyciu metody POST.

- Działa zarówno dla faktur zakupowych jak i sprzedażowych
- Zapewnia natychmiastowe potwierdzenie utworzenia sprawy

### Nowa ścieżka API

Wprowadzono nowy endpoint dla integracji. Zmiana nie wpływa na zakres konfiguracji a jedynie standaryzuje zarządzanie enpointami AMODITA.

### Nowy mechanizm uwierzytelnienia

Uwierzytelnienie odbywa się poprzez przekazanie niewygasającego tokenu w nagłówku żądania:

- **Nagłówek:** Authorization
- **Wartość:** Bearer <token>

Token konfiguruje się w ustawieniu systemowym: **KSeFConnector.AmoditAPI.AccessToken**

### Mapowanie dodatkowych elementów JSON

Rozbudowano mechanizm mapowania o możliwość przekazywania dodatkowych elementów JSON poza strukturą XML faktury. Szczegóły w sekcji 5.2.

# 2. Scenariusze konfiguracji

Sposób konfiguracji integracji zależy od lokalizacji systemów Amodit i KSeF Connector oraz polityk bezpieczeństwa organizacji.

|**Amodit**|**KSeF Connector**|**Konfiguracja**|
|---|---|---|
|**CHMURA**|**CHMURA**|**Jedyna możliwa opcja:** Konfiguracja zalecana|
|**ON-PREMISE**|**ON-PREMISE**|**Wariant A (domyślny):** Konfiguracja zalecana<br><br>**Wariant B (wyjątek):  <br>**Konfiguracja z Jobem – przy występowaniu 2 warunków:  <br>1) gdy Amodit i KSeF Connector działają na różnych serwerach  <br>2) gdy serwer Amodit nie przyjmuje połączeń przychodzących|
|**ON-PREMISE**|**CHMURA**|**Wariant A (domyślny):** Konfiguracja zalecana<br><br>**Wariant B (wyjątek):  <br>**Konfiguracja z Jobem - gdy firewall blokuje ruch przychodzący do Amodit i polityka bezpieczeństwa firmy nie pozwala na otwarcie ruchu przychodzącego do serwera Amodit z naszej chmury.  <br>Przed rozpoczęciem konfiguracji zalecane konsultacje z działem bezpieczeństwa klienta czy na pewno nie można skorzystać z wariantu A|

# 3. Konfiguracja zalecana (domyślna)

**To jest rekomendowana konfiguracja dla większości wdrożeń.**

## 3.1. Charakterystyka

- **Inicjator połączenia:** KSeF Connector (łączy się do Amodit)
- **Uwierzytelnienie:** Token Bearer
- **Job w Amodicie:** NIE jest wymagany

## 3.2. Kroki konfiguracji

### Krok 1: Generowanie tokenu

Wygeneruj losowy token składający się z 24 znaków:

- Małe litery (a-z)
- Wielkie litery (A-Z)
- Cyfry (0-9)

_Na Przykład tutaj: https://it-tools.tech/token-generator?length=24_

### Krok 2: Konfiguracja w Amodicie

Przejdź do ustawień systemowych:

Ustawienia systemowe → Integracje systemowe → Krajowy System e-Faktur (KSeF)

  
  
Uzupełnij następujące pole:

- **KSeFConnector.AmoditAPI.AccessToken** - wklej wygenerowany token z Kroku 1

WAŻNE: Pole KSeFIntegrationAccessToken jest przestarzałe i nie powinno być używane. Na starych instalacjach mogą występować oba pola - używaj wyłącznie KSeFConnector.AmoditAPI.AccessToken.

**Pola, które MUSZĄ pozostać PUSTE:**

- KSeFConnector.ConnectorAPI.BaseUrl
- KSeFConnector.ConnectorAPI.UserLogin
- KSeFConnector.ConnectorAPI.UserPassword
- KSeFConnector.Job.RequestInvoiceMaxLimit
- KSeFConnector.Job.CompanyInvoiceMaxLimit
- KSeFConnector.Job.ExecutionInvoiceMaxLimit

### Krok 3: Przekazanie danych do Zespołu KSeF

Przekaż Zespołowi Administracyjnemu KSeF następujące informacje:

1. **Token** - wygenerowany w Kroku 1
2. **Adres instancji Amodit** - pełny URL do systemu Amodit

**✓ Konfiguracja zakończona**

# 4. Konfiguracja z Jobem (wyjątek)

UWAGA: Ta konfiguracja powinna być stosowana TYLKO w przypadkach opisanych w sekcji 4.1. W większości przypadków należy używać Konfiguracji zalecanej (Rozdział 3).

## 4.1. Kiedy stosować tę konfigurację

Konfiguracja z Jobem jest wymagana TYLKO gdy serwer Amodit nie może przyjmować połączeń przychodzących. Dotyczy to następujących scenariuszy:

- **Scenariusz 1:** Amodit ON-PREMISE + KSeF Connector ON-PREMISE  
    - gdy Amodit i KSeF Connector działają na różnych serwerach
    - gdy serwer Amodit nie przyjmuje połączeń przychodzących  
        
- **Scenariusz 2:** Amodit ON-PREMISE + KSeF Connector CHMURA, gdzie firewall blokuje dostęp z Internetu do Amodit / taka jest polityka bezpieczeństwa Klienta

## 4.2. Charakterystyka

- **Inicjator połączenia:** Amodit (odpytuje KSeF Connector)
- **Uwierzytelnienie:** Login i hasło (w KSeF Connectorze)
- **Job w Amodicie:** WYMAGANY (SynchronizeInvoicesFromKSeF)

## 4.3. Kroki konfiguracji

### Krok 1: Otrzymanie danych od Zespołu KSeF Connector

Skontaktuj się z Zespołem Administracyjnym KSeF Connector i otrzymaj:

- Adres URL KSeF Connector (BaseUrl)
- Login do KSeF Connector
- Hasło do KSeF Connector

###   
  
Krok 2: Konfiguracja w Amodicie

Przejdź do ustawień systemowych:

Ustawienia systemowe → Integracje systemowe → Krajowy System e-Faktur (KSeF)

Uzupełnij następujące pola:

- **KSeFConnector.ConnectorAPI.BaseUrl** - adres serwera KSeF Connector
- **KSeFConnector.ConnectorAPI.UserLogin** - login otrzymany od Zespołu KSeF Connector
- **KSeFConnector.ConnectorAPI.UserPassword** - hasło otrzymane od Zespołu KSeF Connector

_Opcjonalnie_ - można skonfigurować limity:

- **KSeFConnector.Job.RequestInvoiceMaxLimit** - maksymalna liczba faktur przetwarzanych w pojedynczym żądaniu (domyślnie: 10)
- **KSeFConnector.Job.CompanyInvoiceMaxLimit** - maksymalna liczba faktur przetwarzanych dla pojedynczej firmy (domyślnie: 50)
- **KSeFConnector.Job.ExecutionInvoiceMaxLimit** - maksymalna liczba faktur przetwarzanych podczas wykonania Joba

### Krok 3: Utworzenie Joba

Przejdź do ustawień zadań:

Ustawienia systemowe → Zadania

Utwórz nowe zadanie z następującymi parametrami:

- **Nazwa:** SynchronizeInvoicesFromKSeF
- **Biblioteka:** Inne, AMODITKSeFConnector
- **Klasa:** AMODITKSeFConnector.Jobs.SynchronizeInvoicesFromKSeFJob
- **Harmonogram:** Ustaw częstotliwość odpytywania KSeF Connector (np. co 5 minut)

### Krok 4: Restart usługi

KRYTYCZNE: Po zmianie ustawień systemowych ZAWSZE należy zrestartować usługę AMODAsynchronousService!

**✓ Konfiguracja zakończona**

# 5. Utworzenie/modyfikacja rejestru "Companies"

W środowisku Amodit należy **zaimportować, jeśli nie ma lub zaimportować, aby zaktualizować** (NIE TWORZYĆ RĘCZNIE!) rejestr "Companies" (Spółki). Rejestr powinien zawierać następujące pola:  

|**Nazwa pola**|**Typ pola**|**Opis**|
|---|---|---|
|ksef_company_guid|Tekstowe|GUID firmy podawany przez Zespołu KSeF Connector|
|ksef_purchase_invoice_procedure|Numeryczne|Identyfikator procesu obsługującego faktury zakupowe z KSeF|
|ksef_sales_invoice_procedure|Numeryczne|Identyfikator procesu obsługującego faktury sprzedażowe z KSeF|
|ksef_company_id|Numeryczne|ID firmy podawane przez Zespołu KSeF Connector|
|Tax Number|Tekstowe|NIP firmy **wprowadzany z prefixem państwa  <br>np.: PL123456789**|

#   
  

# 6. Wymagane pola w obiegach faktur

UWAGA: Bez tych pól integracja z KSeF Connector NIE zadziała!

## 6.1. Obieg faktur zakupowych

W obiegu faktur zakupowych należy utworzyć następujące pola wymagane:

|**Nazwa pola**|**Typ pola**|**Opis**|
|---|---|---|
|ksef_invoice_file|Dokument z szablonem ksef|Miejsce, gdzie trafia wizualizacja faktury|
|ksef_invoice_id|Tekstowe|ID faktury w systemie KSeF|
|ksef_invoice_correctness_flag|Tak/Nie|Pole techniczne - oznacza czy wiersze faktury zostały już zaimportowane|
|ksef_temporary_invoice_id|Tekstowe|Tymczasowe ID faktury w KSeF Connectorze przed nadaniem numeru KSeF|

## 6.2. Obieg faktur sprzedażowych

W obiegu faktur sprzedażowych wymagane są wszystkie pola z obiegu faktur zakupowych (sekcja 6.1) oraz dodatkowo:

|**Nazwa pola**|**Typ pola**|**Opis**|
|---|---|---|
|ksef_invoice_status_code|Tekstowe|Kod statusu faktury w systemie KSeF|
|ksef_invoice_receipt_confirmation|Dokument|Miejsce, gdzie trafia UPO (Urzędowe Potwierdzenie Odbioru) w formacie XML|
|ksef_invoice_status_desc|Tekstowe|Opis statusu faktury w systemie KSeF|

## 6.3. Dodatkowe uwagi i zalecenia

### Mapowanie wartości słownikowych

Jeśli chcesz mapować wartości z KSeF do pól słownikowych w Amodicie, zaleca się utworzenie pól technicznych pośredniczących.

**Przykład:**

Aby umieścić walutę z KSeF w polu słownikowym "Waluta":

- Utwórz pole tekstowe ksef_waluta
- Zmapuj wartość z XML KSeF do pola ksef_waluta
- Użyj reguł automatycznych lub ręcznych do przeniesienia wartości z ksef_waluta do pola słownikowego "Waluta"

WAŻNE: Mapowanie wartości bezpośrednio do pola słownikowego spowoduje błąd i sprawa nie zostanie utworzona. Błąd będzie widoczny w logach systemowych.  
  

### Obsługa dokumentu faktury

Jeśli chcesz zachować aktualne pole do obsługi dokumentu faktury, możesz użyć następującej reguły automatycznej lub ręcznej:

if([Faktura] == "" && [ksef_invoice_file] == "")  
{

MoveAttachmentToCase ("ksef_invoice_file", [CaseId], "Faktura")

}

### Automatyczne przenoszenie na dalsze etapy

Zaleca się utworzenie reguły cyklicznej, która w przypadku faktur zakupowych będzie automatycznie przenosić sprawy na etap weryfikacji (lub późniejszy) z pominięciem OCR.

Do wykrycia faktur z KSeF można wykorzystać następujące warunki:

- ksef_invoice_id - pole nie jest puste
- ksef_invoice_correctness_flag - wartość true

# 7. Mapowanie pól z KSeF do Amodit

## 7.1. Konfiguracja mapowania podstawowego

W zakładce "Tworzenie sprawy" w definicji procesu należy:

1. Wskazać użytkownika, do którego mają być przypisane sprawy na pierwszym etapie procesu
2. Utworzyć mapowanie pól

**Zasady mapowania:**

- W wartościach **"ksef"** należy podać pełną ścieżkę wartości z pliku XML faktury KSeF
- W wartościach **"amodit"** należy podać nazwę techniczną pola na formularzu  
      
    

Przykładowe proste mapowanie dostępne tutaj: [**link**](https://dev.azure.com/astrafox/d9d438fd-e067-4fd9-917d-b326deafabfa/_apis/git/repositories/d9cc9cd1-8dc6-4b29-aaed-9826c7fe481a/Items?path=/.attachments/ksef_amodit_mapowanie-46d75ee3-a38a-4ca5-9e0b-768aee1df649.txt&download=false&resolveLfs=true&%24format=octetStream&api-version=5.0-preview.1&sanitize=true&includeContentMetadata=true&versionDescriptor.version=wikiMaster)Listy pól zwracanych z KSeF, dostępnych do mapowania w AMODIT: [**Pola z KSeF wraz z opisem (FA3) 2.xlsx**](https://dev.azure.com/astrafox/d9d438fd-e067-4fd9-917d-b326deafabfa/_apis/git/repositories/d9cc9cd1-8dc6-4b29-aaed-9826c7fe481a/Items?path=/.attachments/Pola%20z%20KSeF%20wraz%20z%20opisem%20\(FA3\)%202-e6f3d705-4886-4b34-9be4-f5e9ad4d91a4.xlsx&download=false&resolveLfs=true&%24format=octetStream&api-version=5.0-preview.1&sanitize=true&includeContentMetadata=true&versionDescriptor.version=wikiMaster)**.  
**

## 7.2. Mapowanie dodatkowych elementów JSON (opcjonalne)

Od wersji 250630.133 możliwe jest mapowanie dodatkowych elementów JSON znajdujących się poza strukturą XML faktury. Ta funkcjonalność jest szczególnie przydatna dla faktur sprzedażowych.

**Zastosowanie:**

- Przekazywanie informacji o systemie wystawiającym fakturę (np. SystemDziedzinowy)
- Informacje o użytkowniku, który wystawił fakturę
- Inne metadane potrzebne do wewnętrznych procesów biznesowych

**Konfiguracja:**

Mechanizm mapowania dodatkowych elementów JSON jest elastyczny i działa analogicznie do mapowania pól z XML KSeF. Nazwy węzłów JSON można ustalić w porozumieniu z zespołem KSeF Connector.

_  
Przykładowe nazwy węzłów:_

- "SystemDziedzinowy" - nazwa systemu wystawiającego
- "UzytkownikWystawiajacy" - dane użytkownika

  
dla konfiguracji docelowej wyglądałoby to tak:

(…),

{

„ksef”: „CustomAttributes__SystemDziedzinowy”  
„amodit”: „Wystawiono_w_systemie_X”

},  
(…)

WAŻNE: CustomAttributes__ z dwoma podkreśleniami musi być prefixem, aby poprawnie zmapować wartość customową spoza xmla Faktury.

  

## 7.3. Mapowanie tabel

Aby zmapować tabelę (np. pozycje faktury):

1. W wartościach **"ksef"** wskaż tabelę w pliku XML
2. W wartościach **"amodit"** podaj nazwę techniczną tabeli na formularzu
3. Wewnątrz mapowania tabeli utwórz mapowanie poszczególnych kolumn
4. W wartościach **"ksef"** dla kolumn wskaż pełną ścieżkę do pól w XML, a **"amodit"** nazwę techniczną kolumny w Amodit  
    Przykład:  
      
    

# 8. Gotowe procesy demonstracyjne

Na środowisku demonstracyjnym dostępne są gotowe procesy przygotowane przez zespół wdrożeniowy:

**Środowisko:** https://ksefdemo.amodit.com/

**Dostępne procesy:**

- Rejestr Companies
- Obieg faktur zakupowych
- Obieg faktur sprzedażowych

Procesy te można wykorzystać jako wzór do konfiguracji własnych wdrożeń.

# 9. Podsumowanie i najważniejsze wskazówki

- **Zawsze używaj wersji Amodit 250630.133 lub nowszej**
- **Domyślnie stosuj Konfigurację zalecaną** (KSeF Connector → Amodit)
- **Konfigurację z Jobem używaj tylko w wyjątkowych przypadkach** (firewall, brak dostępu)
- Token w polu KSeFConnector.AmoditAPI.AccessToken to 24 znaki (małe, wielkie litery, cyfry)
- Pole KSeFIntegrationAccessToken jest przestarzałe - nie używaj!
- Po zmianach w ustawieniach systemowych ZAWSZE restartuj usługę AMODAsynchronousService
- Wszystkie wymagane pola w obiegach MUSZĄ być utworzone - bez nich pełna integracja nie zadziała
- Mapuj wartości słownikowe przez pola pośrednie (techniczne)
- Wykorzystaj dodatkowe elementy JSON dla zaawansowanych scenariuszy biznesowych