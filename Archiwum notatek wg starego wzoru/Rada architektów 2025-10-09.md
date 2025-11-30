[[2025-10-09 czwartek]] [[Rada architektów 2025-10-14]]

### Spotkanie rady architektów z dnia 9 października 2025

---

#### 1. Licencjonowanie i utrzymanie biblioteki DevExtreme

- **Ryzyko:**
    
    - Nowsze wersje biblioteki DevExtreme (od v23) wymagają klucza licencyjnego do poprawnego działania. 1Istniały obawy dotyczące bezpieczeństwa umieszczania tego klucza w kodzie front-endowym, który jest publicznie dostępny. 
        
- **Proponowane rozwiązanie:**
    
    - Zgodnie z oficjalną dokumentacją DevExtreme, klucze licencyjne dla aplikacji JavaScript mają charakter publiczny. Należy postępować zgodnie z instrukcją dostawcy i umieścić klucz w kodzie. 
        
    - Należy wyznaczyć osobę odpowiedzialną za utrzymanie biblioteki, śledzenie nowych wersji i kontakt ze wsparciem technicznym w razie problemów. 
        
- **Decyzja:**
    
    - Sposób implementacji licencji jest prawidłowy. 
        
    - Należy zakupić i wdrożyć najnowszą wersję biblioteki, aby korzystać z poprawek błędów i nowych funkcji (np. w zakresie dostępności WCAG). 
        
    - **Ania** zostaje oficjalnie wyznaczona jako opiekun biblioteki DevExtreme. 
        
- **Zadania:**
    
    - **Ania:** Będzie odpowiedzialna za monitorowanie zmian w bibliotece, zgłaszanie błędów do dostawcy i dbanie o jej aktualizacje. 
        
    - **Janusz:** Zainicjuje proces zakupu najnowszej wersji licencji.
        

---

#### 2. Krytyczny problem z e-Doręczeniami na środowisku chmurowym

- **Ryzyko:**
    
    - Integracja z e-Doręczeniami nie działa na środowisku chmurowym dla klientów produkcyjnych od ponad trzech miesięcy, mimo że działa na środowiskach on-premise. 11 Blokuje to kluczową funkcjonalność, za którą klienci płacą.
        
    - Brak odpowiedzi ze strony wsparcia Poczty Polskiej utrudnia diagnozę. 
        
- **Proponowane rozwiązanie:**
    
    - Należy pilnie zdiagnozować problem po stronie AMODIT, ponieważ wszystko wskazuje na to, że błąd leży w konfiguracji środowiska chmurowego (np. Azure Key Vault, ustawienia sieciowe, lokalizacja serwerów), a nie po stronie dostawcy usługi. 
        
    - Konieczne jest stworzenie prostego, niezależnego programu testującego połączenie, aby uruchomić go z różnych serwerów i zidentyfikować miejsce występowania problemu. 
        
- **Decyzja:**
    
    - Problem ma najwyższy priorytet. **Adrian** ma odłożyć inne zadania i skupić się wyłącznie na rozwiązaniu tej kwestii. 
        
- **Zadania:**
    
    - **Adrian:** Stworzy i uruchomi program diagnostyczny na różnych środowiskach w celu zlokalizowania źródła błędu. 
        
    - **Piotr:** Wesprze Adriana w procesie diagnostycznym. 
        

---

#### 3. Zarządzanie procesami w stanach "nieaktywny" i "usunięty"

- **Ryzyko:**
    
    - Brak jest jasności co do faktycznego zachowania systemu, gdy proces jest oznaczony jako "nieaktywny" lub "usunięty". W praktyce jedynym efektem jest ukrycie procesu na liście, natomiast wszystkie powiązane z nim mechanizmy (np. reguły okresowe) nadal działają w tle. 
        
- **Proponowane rozwiązanie:**
    
    - Nie można zmieniać obecnego zachowania ze względu na kompatybilność wsteczną. 
        
    - Należy w pierwszej kolejności precyzyjnie opisać działanie każdego ze statusów w interfejsie aplikacji oraz w dokumentacji (wiki). 
        
    - W przyszłości należy rozważyć dodanie nowego, czwartego stanu (np. "Zatrzymany", "Archiwalny"), który faktycznie "zamrozi" proces i wszystkie jego automatyzacje. 
        
- **Decyzja:**
    
    - W ramach MVP należy przygotować szczegółowe opisy wyjaśniające działanie każdego statusu. Wprowadzenie nowego, w pełni blokującego stanu, jest dobrym pomysłem na dalszy rozwój.
        
- **Zadania:**
    
    - Zespół (w domyśle Damian) przygotuje opisy do UI i dokumentacji. 
        

---

#### 4. Zapobieganie błędom przy imporcie procesów (problem Polpharmy)

- **Ryzyko:**
    
    - Wprowadzanie zmian w strukturze formularza (dodawanie pól) bezpośrednio na produkcji prowadzi do rozjechania się schematów bazy danych między środowiskami. Powoduje to krytyczne błędy i potencjalne uszkodzenie danych podczas importu nowszej wersji procesu. 
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzić w ustawieniach systemowych parametr określający typ środowiska ("produkcyjne", "testowe"). 
        
    - Na środowisku oznaczonym jako produkcyjne, utrudnić modyfikację struktury formularza poprzez wprowadzenie dodatkowych ostrzeżeń i kroków potwierdzających.
        
    - Podczas importu procesu, jeśli system wykryje konflikt w mapowaniu pól (jak w przypadku Polpharmy), opcja "nadpisz" powinna zostać zablokowana. Użytkownik powinien otrzymać jasny komunikat o konieczności naprawy procesu na środowisku źródłowym. 
        
- **Decyzja:**
    
    - Oba kierunki rozwoju są słuszne. Wdrożenie mechanizmu oznaczania środowisk oraz blokada importu w przypadku krytycznych konfliktów znacząco podniesie bezpieczeństwo i stabilność systemu.
        
- **Zadania:**
    
    - **Piotr:** Zaproponuje szczegółowy komunikat błędu i logikę blokowania importu. 