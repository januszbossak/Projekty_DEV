
> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-07

## Cel projektu

Integracja systemu AMODIT z systemem CAS (Central Authentication Service) w celu zapewnienia centralnej autoryzacji, autentykacji oraz zarządzania uprawnieniami użytkowników.

---

## 1. PRZEPŁYW LOGOWANIA I AUTORYZACJI

### 1.1 Zakres funkcjonalny

- **Przekierowanie do CAS**: Wywołanie linku do systemu AMODIT automatycznie przekierowuje użytkownika do aplikacji CAS
- **Autoryzacja użytkownika**: Użytkownik autoryzuje się w systemie CAS swoim loginem i hasłem
- **Powrót do AMODIT**: Po poprawnej autoryzacji użytkownik jest przekierowywany z powrotem do systemu AMODIT

### 1.2 Proces działania

1. Użytkownik wchodzi na URL systemu AMODIT
2. System wykrywa brak aktywnej sesji i przekierowuje do CAS
3. CAS prezentuje formularz logowania
4. Po poprawnym zalogowaniu CAS zwraca token/bilet autoryzacyjny
5. AMODIT weryfikuje token i tworzy sesję użytkownika

---

## 2. ZARZĄDZANIE UŻYTKOWNIKAMI

### 2.1 Tworzenie nowych użytkowników

**Zakres:**

- System AMODIT automatycznie zakłada konto użytkownika, jeśli nie istnieje w bazie podczas pierwszego logowania
- Tworzenie konta następuje w oparciu o dane przekazane z CAS

**Warunki:**

- Użytkownik musi być poprawnie uwierzytelniony w CAS
- Dane użytkownika są pobierane z endpointu CAS (GetFull)

### 2.2 Aktualizacja istniejących użytkowników

**Zakres:**

- Przy każdym logowaniu system pobiera aktualne dane użytkownika z CAS (GetFull endpoint)
- Automatyczna aktualizacja danych personalnych (imię, nazwisko)
- Aktualizacja danych następuje tylko przy faktycznym zalogowaniu

**Ograniczenia:**

- Zmiany w systemie źródłowym (CAS) będą widoczne w AMODIT dopiero po ponownym zalogowaniu użytkownika
- Do momentu ponownego logowania w systemie pozostają stare dane

---

## 3. ZARZĄDZANIE GRUPAMI I UPRAWNIENIAMI

### 3.1 Synchronizacja grup z CAS

**Zakres:**

- System pobiera informacje o przynależności użytkownika do grup z systemu CAS (GetFull endpoint)
- Automatyczne przypisanie użytkownika do grup w AMODIT, jeśli nazwy grup są tożsame między systemami
- Automatyczne usunięcie użytkownika z grup, jeśli nie należy już do nich w systemie CAS

**Mechanizm działania:**

1. Przy logowaniu pobierana jest lista grup użytkownika z CAS
2. System porównuje grupy w CAS z grupami w AMODIT
3. Dodanie do grup, które istnieją w obu systemach
4. Usunięcie z grup, które nie są już przypisane w CAS

### 3.2 Zasada tożsamości grup

**WAŻNE:**

- Grupy w AMODIT muszą mieć dokładnie takie same nazwy jak grupy w CAS i musza być wcześniej utworzone w Amodit
- Mogą istnieć grupy tylko po stronie AMODIT, które nie mają odpowiednika w CAS, ale żaden użytkownik autoryzujący się przez CAS nie będzie skutecznie przypisany do takiej grupy  
- Każda grupa lokalna bez odpowiednika w CAS będzie automatycznie wypinana przy logowaniu - dotyczy punktu wyżej.

**Konsekwencje:**

- Ręczne przypisanie użytkownika do grupy nieistniejącej w CAS zostanie cofnięte przy kolejnym logowaniu
- Wszystkie grupy muszą być zarządzane centralnie w systemie CAS

### 3.3 Model uprawnień

**Wariant do ustalenia:**

#### OPCJA A: Pełna synchronizacja przez grupy

- **Wszystkie** uprawnienia dostępowe wynikają z przynależności do grup
- Grupy definiują kompletny zakres uprawnień (poza rolą Administrator)
- Uprawnienia: widoczność faktur, reguł, akceptacja reguł, etc.

#### OPCJA B: Model mieszany

- **Podział na role podstawowe**: Administrator vs. Zwykły użytkownik
- **Grupy definiują szczegółowe uprawnienia**:
    - Widoczność faktur
    - Widoczność reguł
    - Akceptacja reguł
    - Inne uprawnienia biznesowe
- Zarządzanie grupami(ich składem i przynależnością usera do groupy) pozostaje po stronie AMODIT 

**Zalecenie:** Opcja A ze względu na spójność i łatwiejsze zarządzanie

---

## 4. ROLA ADMINISTRATORA

### 4.1 Zakres

- Rola "Administrator" jest ustawiana sztywno w systemie AMODIT
- Nie wynika z przynależności do grup, lecz z bezpośredniego atrybutu użytkownika
- Administrator ma pełen dostęp do wszystkich funkcji systemu

### 4.2 Zasady przypisania

- Rola Administratora przypisywana jest ręcznie w systemie AMODIT
- Jest synchronizowana z systemem CAS - ale nazwa musi być ustawiona wspólnie na sztywno
- Pozostaje niezmienna podczas procesów logowania i synchronizacji

### 4.3 Model uprawnień

- **Administrator**: pełne uprawnienia
- **Pozostałe role/uprawnienia**: zarządzane przez grupy synchronizowane z CAS

---

## 5. MAPOWANIE PÓL UŻYTKOWNIKA

### 5.1 Pola podstawowe (obowiązkowe)

Następujące pola są mapowane standardowo z CAS do AMODIT:

|Pole w CAS|Pole w AMODIT|Opis|
|---|---|---|
|username / józef_name|Login|Nazwa użytkownika do logowania|
|first_name|Imię|Imię użytkownika|
|last_name|Nazwisko|Nazwisko użytkownika|
|email|E-mail|Adres e-mail użytkownika|

### 5.2 Pola dodatkowe (do ustalenia)

**Pytania wymagające odpowiedzi:**

- Czy system CAS udostępnia dodatkowe pola (np. stanowisko, dział, telefon)?
- Czy te dodatkowe pola powinny być mapowane na pola użytkownika w AMODIT? np. przełożony czy przynależność do działu

**Zalecenie:**

- Zdefiniować pełną listę dostępnych atrybutów w CAS
- Zmapować wszystkie przydatne pola dla celów biznesowych
- Przygotować konfigurację mapowania jako parametr systemu

---

## 6. BLOKOWANIE I DEZAKTYWACJA KONT

### 6.1 Blokowanie w systemie CAS

**Zakres:**

- Blokowanie/dezaktywacja konta użytkownika odbywa się w systemie CAS
- CAS jest providerem autoryzacji i decyduje o możliwości logowania
- Zablokowany w CAS użytkownik nie będzie mógł zalogować się do AMODIT

### 6.2 Blokowanie w systemie AMODIT

**Zakres:**

- System AMODIT **nie synchronizuje** automatycznie statusu blokady z CAS
- Blokada w AMODIT wymaga **ręcznego działania administratora**
- Możliwość niezależnej blokady konta w AMODIT (bez blokady w CAS)

**Przypadki użycia:**

- Tymczasowe zablokowanie dostępu do AMODIT bez wpływu na inne systemy
- Sytuacje wymagające natychmiastowej reakcji administratora

### 6.3 Scenariusze blokowania

|Scenariusz|Efekt w CAS|Efekt w AMODIT|
|---|---|---|
|Blokada w CAS|Brak możliwości logowania|Brak możliwości logowania (via CAS)|
|Blokada w AMODIT|Brak wpływu|Brak możliwości korzystania z AMODIT|
|Blokada w obu systemach|Brak możliwości logowania|Pełna blokada dostępu|

---

## 7. KWESTIE TECHNICZNE DO DOPRECYZOWANIA

### 7.1 Endpoint GetFull

**Wymagania:**

- Dokumentacja struktury odpowiedzi z endpointu GetFull
- Lista wszystkich dostępnych atrybutów użytkownika
- Lista wszystkich dostępnych grup
- Metoda uwierzytelniania do endpointu - **do potwierdzenia czy korzystamy z tych samych danych co Pit kalkualtor - wysłałem maila: Damian Kamiński**

### 7.2 Protokół CAS

**Do ustalenia:**

- Wersja protokołu CAS (2.0, 3.0?)
- Format biletów (Service Ticket, Proxy Ticket)
- Procedura walidacji biletów
- Obsługa Single Logout (SLO)
- Timeout sesji

### 7.3 Konfiguracja

**Parametry konfiguracyjne:**

- URL serwera CAS
- URL callback AMODIT (service URL)
- Certyfikaty SSL (jeśli wymagane)
- Mapowanie nazw atrybutów (konfiguracja pól)
- Mapowanie nazw grup (jeśli różne nazewnictwo)

---

## 8. PROBLEMY I RYZYKA

### 8.1 Problem synchronizacji grup

**Ryzyko:** Utrata ręcznie przypisanych uprawnień

**Opis problemu:**

- Jeśli grupy nie są w 100% synchronizowane między CAS a AMODIT
- Każde logowanie powoduje usunięcie użytkownika z grup nieistniejących w CAS
- Ręczne zmiany w AMODIT są anulowane przy kolejnym logowaniu

**Rozwiązanie:**

- Wszystkie grupy muszą być definiowane w CAS
- Brak lokalnych grup w AMODIT (poza systemowymi)
- Dokumentacja i procedura dodawania nowych grup

### 8.2 Opóźnienie aktualizacji danych

**Ryzyko:** Nieaktualne dane użytkownika

**Opis problemu:**

- Zmiana danych w CAS (np. nazwisko) nie jest natychmiast widoczna w AMODIT
- Wymagane jest ponowne zalogowanie użytkownika

**Rozwiązanie:**

- Komunikacja dla użytkowników o konieczności ponownego logowania po zmianie danych
- Opcjonalnie: mechanizm wymuszania ponownego logowania (logout)

### 8.3 Brak automatycznej blokady

**Ryzyko:** Konta zablokowane w CAS mogą pozostać aktywne w AMODIT

**Opis problemu:**

- Jeśli użytkownik został zablokowany w CAS, ale ma aktywną sesję w AMODIT
- Sesja pozostanie aktywna do czasu jej wygaśnięcia

**Rozwiązanie:**

- Implementacja Single Logout (SLO)
- Krótsze czasy życia sesji
- Procedura ręcznego blokowania w sytuacjach krytycznych

---

## 9. WYMAGANIA FUNKCJONALNE - PODSUMOWANIE

### 9.1 Must Have (Wymagane)

1. ✓ Przekierowanie do CAS przy próbie dostępu do AMODIT
2. ✓ Autoryzacja poprzez CAS
3. ✓ Automatyczne tworzenie użytkownika przy pierwszym logowaniu
4. ✓ Pobieranie danych użytkownika z CAS (GetFull)
5. ✓ Synchronizacja przynależności do grup
6. ✓ Mapowanie podstawowych pól (login, imię, nazwisko, email)
7. ✓ Obsługa roli Administrator (lokalna, sztywna)
8. ✓ Aktualizacja danych przy każdym logowaniu

### 9.2 Should Have (Zalecane)

1. ⚠ Single Logout (SLO) - wylogowanie ze wszystkich systemów
2. ⚠ Mapowanie dodatkowych pól użytkownika
3. ⚠ Mechanizm powiadamiania o zmianie uprawnień
4. ⚠ Logi synchronizacji (audyt zmian uprawnień)

### 9.3 Could Have (Opcjonalne)

1. ○ Dashboard do zarządzania mapowaniem grup ?
2. ○ Raportowanie o niezsynchronizowanych grupach ?
3. ○ Mechanizm wymuszania ponownego logowania ?

---

## 10. DECYZJE DO PODJĘCIA

### Priorytet WYSOKI

1. **Model uprawnień**: Opcja A (pełna synchronizacja) vs. Opcja B (model mieszany)?
2. **Mapowanie pól**: Jakie dodatkowe pola poza podstawowymi czterema?
3. **Mapowanie grup**: Czy nazwy grup będą identyczne, czy wymagane jest mapowanie?
4. **Timeout sesji**: Jaki maksymalny czas życia sesji w AMODIT?

### Priorytet ŚREDNI

5. **Single Logout**: Czy implementować SLO?
6. **Logi synchronizacji**: Jaki poziom szczegółowości logów?
7. **Obsługa błędów**: Co w przypadku niedostępności CAS?

### Priorytet NISKI

8. **Dashboard zarządzania**: Czy potrzebne narzędzie administracyjne?
9. **Migracja użytkowników**: Jak obsłużyć istniejących użytkowników?

##   

---

## ZAŁĄCZNIKI

### A. Słownik pojęć

- **CAS**: Central Authentication Service - system centralnej autoryzacji
- **GetFull**: Endpoint CAS zwracający pełne dane użytkownika
- **Service Ticket**: Bilet jednorazowy potwierdzający autentykację
- **SLO**: Single Logout - mechanizm jednokrotnego wylogowania
- **Provider**: System dostarczający usługi autoryzacji (w tym przypadku CAS)

## Powiązane projekty
- [[Projekty/Integracje/Integracja-CAS/Integracja-CAS.md|Integracje/Integracja-CAS]]