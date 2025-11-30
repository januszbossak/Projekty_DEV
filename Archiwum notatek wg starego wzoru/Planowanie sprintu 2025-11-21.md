## Tytuł: Podsumowanie "Planowania sprintu" – 21.11.2025

### 1. Status bieżący (Domykanie tematów)

- **Temat Ametystowy:** Piotrek kończy prace, deklarowane zamknięcie dzisiaj.
    
- **Komunikator:** Został uruchomiony, działa u klienta, oczekiwanie na uwagi.
    
- **Integracje kurierskie:** Łukasz Brocki posiada dane do UPS i GLS. Global Express ma szansę zostać zrealizowany w tym sprincie.
    
- **Wizualne poprawki edytora:** Kamil D. zamknął tematy związane z listą pól, zaokrągleniami (5px) i bugami wizualnymi.
    

---

### 2. Plany na kolejny sprint (Główne tematy)

#### Integracja JRWA (Jednolity Rzeczowy Wykaz Akt)

**Kontekst:** Implementacja struktury wzorowanej na rozwiązaniu GUS Teryt. Klient (LOT) wstępnie nie wymaga skomplikowanych uprawnień (widoczność wszystkich klas), więc pomijamy na tym etapie dedykowaną tabelę uprawnień. **Ustalenia techniczne:**

- **Mechanizm:** Podpięcie źródła jako `Odnośnik do źródła zewnętrznego` -> Wybór pozycji -> Zwrotka JSON.
    
- **Dostęp do danych:** Rezygnacja z parsowania JSON-a w regułach. Dane wybranej pozycji mają być dostępne przez notację kropkową, np. `[pole_jrwa.symbol]`, `[pole_jrwa.okres_przechowywania]`. Wymaga to obsługi po stronie backendu, by zwracał obiekt, a nie raw JSON string.
    
- **Wykonanie:** Piotrek buduje strukturę (start od poniedziałku). Potencjalnie temat może przejąć Mariusz w dalszej fazie.
    

#### Repozytorium Plików (Finder)

**Kontekst:** Budowa dedykowanego widoku zarządzania plikami. **Ustalenia i Zakres:**

- **Backend:** Ania przygotowuje pierwszy endpoint (tworzenie folderów) dzisiaj.
    
- **Frontend:** Filip podpina się pod gotowe endpointy w przyszłym tygodniu.
    
- **Instalacja (LOT):** Konieczność obejścia braku certyfikacji na Mac dla dyrektora (obejście przez "zgadzam się na instalację") w celu prezentacji demo.
    

#### Integracje LOT (SIEM & Logi)

**Kontekst:** Monitorowanie zdarzeń bezpieczeństwa. Spotkanie techniczne z LOT we wtorek. **Podejście:**

- Nie budujemy dedykowanej logiki integracyjnej w aplikacji.
    
- Wystawiamy logi systemowe w ustandaryzowanym formacie (np. CSV lub bezpośredni strumień sieciowy), które system SIEM klienta będzie "nasłuchiwał".
    

#### Edytor Formularza i Lista Pól (Fixy Grudniowe)

**Kontekst:** W nowej wersji listy pól (grudniowej) zniknęła możliwość edycji reguł tabeli (brak widocznej sekcji). **Ustalenia:**

- **Priorytet:** Przywrócenie widoczności sekcji "Reguły tabeli" w edytorze jest krytyczne dla wersji grudniowej (blocker).
    
- **Długofalowo:** Zmiana logiki backendowej – sekcje powinny mieć swoją reprezentację w bazie, zamiast być zapisywane redundantnie w definicji każdego pola.
    

---

### 3. Dług techniczny i Ryzyka

- **Ryzyko zasobowe (Backend):** Sytuacja Adriana jest niepewna, co jest ryzykiem dla tematu Repozytorium (możliwe opóźnienie prac backendowych).
    
- **Raporty / Operatory dat:** Przemek porządkuje logikę operatorów daty. Cel: Priorytetyzacja prostych filtrów ("Ostatnie 7 dni", "Ostatnie 30 dni") nad skomplikowanymi ("Nie wcześniej niż...").
    
- **Wydajność:** Mateusz pracuje nad indeksami w bazie danych, co jest kluczowe przed dalszymi pracami wizualnymi.
    

---

### 4. Organizacja pracy (Propozycja)

- **Zespoły zadaniowe:** Janusz proponuje powrót do trwałych zespołów (np. 3 zespoły: 2 BE + 1 FE + 1 QA) przypisanych do obszarów (np. Zespół OCR/AI, Zespół Trust Center).
    
- **Decyzja:** Temat do przemyślenia przez zespół, brak finalnej decyzji na spotkaniu.