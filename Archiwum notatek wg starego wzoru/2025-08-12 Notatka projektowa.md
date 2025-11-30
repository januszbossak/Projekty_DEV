

Data: 12 sierpnia 2025 1

Temat: Architektura, uwierzytelnianie i model danych modułu Komunikator (AMODIT Talk)

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Architektura modułu Komunikator (Model wdrażania)**

- **Komponent:** Moduł Komunikator (Aplikacja Zewnętrzna / Mikroserwis)
    
- **Cel:** Zapewnienie działania komunikatora zarówno w środowisku On-Premises, jak i w chmurze (SaaS) bez konieczności utrzymywania dwóch osobnych wersji kodu2222.
    
- **Problem do rozwiązania:** Obecna konfiguracja opiera się na sztywnym łańcuchu połączeń (connection string), co jest problematyczne w środowisku chmurowym (wielu najemców/organizacji)3333. Dodatkowo, istniała obawa o sensowność utrzymywania komunikatora jako osobnej aplikacji4444.
    
- **Sposób realizacji / Decyzja:**
    
    - Utrzymanie Komunikatora jako osobnej aplikacji wykorzystującej SignalR, aby nie obciążać głównej instancji AMODIT5.
        
    - System ma automatycznie wykrywać tryb pracy (lokalny vs chmurowy)6.
        
    - W wersji chmurowej connection string oraz konfiguracja mają być pobierane dynamicznie z serwisu centralnego na podstawie identyfikatora organizacji, zamiast być wpisane na sztywno7777.
        
    - Projekt będzie kontynuowany w obecnej architekturze (osobna aplikacja), z naciskiem na dostosowanie do wymogów chmurowych8.
        

#### **Funkcjonalność: Mechanizm Uwierzytelniania (SSO / JWT)**

- **Komponent:** Moduł Komunikator / Integracja Systemowa
    
- **Cel:** Bezpieczne logowanie użytkowników do Komunikatora z wykorzystaniem tożsamości z systemu AMODIT (w tym obsługa Windows Auth w On-Premises)9999.
    
- **Problem do rozwiązania:** Komunikator działa jako osobny serwis (inna domena/port), co utrudnia współdzielenie ciasteczek sesyjnych oraz obsługę zintegrowanego logowania Windows10. Przekazywanie tokena bezpośrednio w URL jest niebezpieczne11.
    
- **Sposób realizacji / Decyzja:**
    
    - Wdrożenie mechanizmu opartego na kodzie jednorazowym (OTP) i tokenach JWT12.
        
    - Przepływ: AMODIT generuje kod jednorazowy -> Przekierowanie użytkownika do Komunikatora z kodem w query stringu -> Komunikator wymienia kod na token JWT poprzez API backendowe13.
        
    - Rezygnacja z przekazywania tokena bezpośrednio w URL na rzecz kodu jednorazowego14.
        

#### **Funkcjonalność: Przechowywanie kodów autoryzacyjnych (OTP)**

- **Komponent:** Backend / Baza Danych
    
- **Cel:** Obsługa środowisk z Load Balancingiem (wiele serwerów).
    
- **Problem do rozwiązania:** Obecnie kody jednorazowe przechowywane są w pamięci RAM (cache). W środowisku z wieloma serwerami (Load Balancing), zapytanie o weryfikację kodu może trafić na inny serwer niż ten, który go wygenerował, co spowoduje błąd autoryzacji1515151515151515.
    
- **Sposób realizacji / Decyzja:**
    
    - Konieczność przeniesienia przechowywania kodów jednorazowych z pamięci RAM do współdzielonej bazy danych lub rozproszonego cache'a16161616.
        
    - Zostanie rozważone wykorzystanie istniejących tabel logów (np. UserActivityLog) lub tabeli powiadomień do tymczasowego składowania kodów17171717.
        

#### **Funkcjonalność: Model Bazy Danych i Migracje**

- **Komponent:** Moduł Komunikator / Baza Danych
    
- **Cel:** Przechowywanie historii czatów i definicji użytkowników.
    
- **Problem do rozwiązania:** Spójność nazewnictwa tabel i kolumn z konwencją AMODIT oraz zarządzanie zmianami w schemacie bazy.
    
- **Sposób realizacji / Decyzja:**
    
    - Wykorzystanie osobnych tabel dla komunikatora (niezależnych od rdzenia AMODIT)18.
        
    - Zastosowanie mechanizmu migracji Entity Framework (`__EFMigrationsHistory`) do zarządzania wersjonowaniem bazy19.
        
    - Integracja listy użytkowników poprzez pobieranie ich z API AMODIT (User Controller), zamiast duplikowania tabeli użytkowników, choć lokalna kopia/cache w bazie komunikatora może być utrzymywana2020.
        

#### **Funkcjonalność: Szyfrowanie wiadomości**

- **Komponent:** Moduł Komunikator / Bezpieczeństwo
    
- **Cel:** Zapewnienie poufności korespondencji.
    
- **Problem do rozwiązania:** Zarządzanie kluczami szyfrującymi w środowisku wielodostępnym (chmura). Obecnie klucz jest w pliku konfiguracyjnym (jeden dla całej instancji)21.
    
- **Sposób realizacji / Decyzja:**
    
    - Wiadomości są szyfrowane w bazie danych22.
        
    - Docelowo (dla wersji chmurowej) klucze muszą być unikalne dla każdego klienta (tenanta) i przechowywane w bazie danych lub bezpiecznym magazynie (Vault), a nie w globalnym pliku konfiguracyjnym232323.
        

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Stabilizacja wersji On-Premises i Poprawa Bezpieczeństwa**

- **Cel:** Uruchomienie działającej, bezpiecznej wersji komunikatora w środowisku lokalnym klienta, eliminując błędy architektury uwierzytelniania.
    
- **Zakres:**
    
    - Implementacja wymiany kodu jednorazowego na token JWT (eliminacja tokena z URL)24.
        
    - Przeniesienie zapisu kodów jednorazowych z pamięci RAM do bazy danych (obsługa LoadBalancingu)25.
        
    - Integracja z kontrolerem użytkowników AMODIT (pobieranie listy użytkowników)26.
        
    - Szyfrowanie wiadomości z wykorzystaniem klucza z konfiguracji (model On-Premises)27.
        

#### **MVP 2: Dostosowanie do Chmury (SaaS)**

- **Cel:** Umożliwienie wdrażania komunikatora w środowisku wielodostępnym.
    
- **Zakres:**
    
    - Implementacja dynamicznego pobierania Connection Stringa i konfiguracji na podstawie identyfikatora organizacji28282828.
        
    - Mechanizm zarządzania kluczami szyfrowania per tenant (klient)29.
        
    - Pełna obsługa separacji danych dla różnych organizacji w ramach jednej instancji aplikacji.
        

---

### **Punkty do dalszej dyskusji i weryfikacji (Otwarte)**

1. **Szczegółowy przegląd kodu:** Architekt (Piotr) musi przejrzeć kod i repozytorium, aby zatwierdzić ostateczny kształt rozwiązań technicznych, ponieważ dyskusja opierała się na deklaracjach dewelopera30.
    
2. **Miejsce zapisu kodów OTP:** Należy ostatecznie wskazać konkretną tabelę w bazie danych do przechowywania kodów autoryzacyjnych (sugerowane `UserActivityLog` lub tabele powiadomień, ale brak ostatecznej decyzji)31313131.
    
3. **Integracja z Copilotem:** Wstępna koncepcja, aby Copilot był dostępny jako "użytkownik" w czacie, wymaga osobnego zaplanowania w przyszłości32.