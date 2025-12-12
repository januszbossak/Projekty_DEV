# CHANGELOG - Dokumentacja organizacyjna

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-03 Spotkanie projektowe - Błędy formularzy i procedury aktualizacji.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-03%20Spotkanie%20projektowe%20-%20Błędy%20formularzy%20i%20procedury%20aktualizacji.md)  
**Kategoria:** #Procedury #Organizacja #Decyzja

**Procedury aktualizacji dla klientów chmurowych:**
- **Problem:** Brak procedur testowania przed aktualizacją produkcji - Adecco dev i prod zaktualizowane jednocześnie, co doprowadziło do krytycznego błędu
- **Decyzja:** Nowa procedura dla dużych klientów chmurowych z dev/test: dev → testy przez klienta (checklist) → prod (tylko po zatwierdzeniu) → support/hotline następnego dnia → rollback jeśli problemy
- **Klienci do objęcia:** Adecco (traktować jak on-premise, ma 3 witryny), MSIT (już ma procedurę - wzorcowy), wszyscy duzi klienci z środowiskiem testowym
- **Wzór:** Deutsche Bank (Łukasz Bott) - checklist po aktualizacji testowej, zielone światło na prod, support następnego dnia, rollback dopóki nie naprawione
- **Ograniczenia:** Mniejsi klienci bez środowiska testowego pozostają w standardowym modelu chmurowym

**Testy end-to-end - potrzeba automatyzacji:**
- **Kontekst:** Przypadek Adecco pokazał, że testy funkcjonalne nie wystarczą - potrzebne testy na konkretnych przypadkach biznesowych
- **Dwa rodzaje testów:** (1) funkcjonalne - czy działa, (2) przypadki biznesowe - czy działa w pokręconych scenariuszach klientów
- **Narzędzia rozważane:** Playwright, Cypress (wymaga full-time job, nawet z AI)
- **Kursy:** Dostępne (część darmowa, część płatna z pomocą - kilkadziesiąt tys. zł)
- **Status:** Michał Zwierzchowski zaczął przeglądać materiały, Janusz Bossak próbował ale utknął
- **Decyzja Przemka:** Nie zgodził się na zatrudnienie osoby do testów e2e
- **Problem:** Trudno przewidzieć wszystkie przypadki biznesowe bez testów na żywych procesach klientów

---


## 2025-12-02 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-02 Spotkanie projektowe - AMODIT UI.md]
**Kategoria:** #Metodyka #Organizacja #Automatyzacja #Strategia

- **Planowanie sprintów - metodyka 2 sprintów do przodu**:
  - Propozycja: planowanie bieżącego + kolejnego sprintu szczegółowo
  - Cel: weryfikacja zgodności z roadmapą, lepsza komunikacja priorytetów do zespołu
  - Roadmapa roczna z szczegółowym pierwszym kwartałem
  - Planowanie kolejnego sprintu na początku tygodnia (poniedziałek-wtorek)
  - Programiści wiedzą co jest najważniejsze (nie muszą zgadywać)
  
- **Bieżący sprint - cele i projekty klienckie**:
  - Główne cele: MVP edytora procesów + repozytorium WIM
  - Projekty klienckie (poza celami): LOT (JRWA, ADE, integracje UPS/Global Express), Lewiatan (Comarch Hub - 18k zł), Vasco (Google Gemini OCR)
  - Część mocy zespołu zarezerwowana na nieprzewidywalne zlecenia klientów
  - Nie rozpoczynać nowych rzeczy rozwojowych poza celami (chyba że zlecenie klienta)
  
- **Zarządzanie projektami i automatyzacja przez AI** (Janusz):
  - Automatyczne generowanie celów sprintów z transkrypcji spotkań (AI zna kontekst, roadmapę)
  - Klasyfikacja zgłoszeń na backlogu (inicjatywa, PBI, epic) + przeformułowanie opisów
  - Pilnowanie roadmapy - weryfikacja czy cele sprintów są zgodne z planem
  - Cele do mierzenia (KPI): mniejsza liczba błędów (cel: zero błędów przy przekazaniu), mniej powracania do tych samych tematów
  - Uzasadnienie biznesowe celów sprintów (przeliczenie na pieniądze)
  
- **Filozofia planowania i projektowania - "więcej planowania, mniej poprawek"**:
  - Zasada: "5 godzin rozmowy oszczędza 5 dni pracy programisty"
  - Więcej czasu na planowanie, projektowanie, uzgodnienia = szybsza implementacja
  - Prototypowanie po 2 godzinach pracy (szybka weryfikacja) zamiast tygodnia implementacji
  - Filtrowanie błędów w projektowaniu zanim trafią do wytworzenia
  - Przykład: JRWA - uproszczona koncepcja, Marek zrobi w 1-2 dni
  
- **Standaryzacja procesów przez AI**:
  - Ocena zgłoszeń od klientów przez LLM (budżet, koszt, priorytet) - klasyfikacja: robimy/zastanówmy się/nie robimy
  - Ocena leadów (marketing) - już wdrożone w marketingu (Google Drive + LLM)
  - Wyceny dla klientów - klient ma dostęp do procesu w AMODIT, LLM ocenia kompletność wymagań
  - Korzyści: standaryzacja (niezależnie kto ocenia, proces ten sam), nie trzeba szkolić nowych pracowników, LLM wykrywa badanie konkurencji
  
- **Sprzęt - MacBook Pro vs Air dla Janusza**:
  - Rozważane: Pro (32 GB RAM, 1 TB dysk, mocniejszy GPU) vs Air (lżejszy, dłuższa bateria, cichszy)
  - Główny cel: więcej pamięci (obecnie 16 GB, swap używany) i większy dysk (obecnie 256 GB)
  - Decyzja: Janusz sprawdzi w iSpot jak Pro hałasuje, potem finalna decyzja
  - Filozofia: kupować najlepszego Macka w danym momencie (służy 10 lat)

---

## 2025-11-30 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-30 Spotkanie projektowe - Edytor procesow.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-30%20Spotkanie%20projektowe%20-%20Edytor%20procesow.md)
**Kategoria:** #Organizacja #Metodyka #Decyzja

- Zmiana formuły Daily: fokus na postępach w kluczowych projektach i celach sprintu.
- Backlog: redukcja roadmapy ("połowę wyrzucić") na rzecz dowiezienia domkniętych funkcjonalności.
- Zespoły projektowe: podział na mniejsze, skoncentrowane zespoły (np. osobno edytor, osobno repozytorium).
- Koncepcja publicznego demo (reset co godzinę) dla zewnętrznych funkcjonalności (Repozytorium, Komunikator).



---

## 2025-11-28 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-28 Planowanie sprintu.md]
**Kategoria:** #Organizacja #Decyzja #Urlopy

- Zmiana struktury Daily: skupienie na postępach w kluczowych projektach (np. Repozytorium, Moduł raportowy) zamiast indywidualnych zadań.
- Urlopy: Piotr Buczkowski nieobecny przez następny tydzień.
- Zakaz instalacji/aktualizacji: Przez tydzień brak instalacji AMODIT, aby uniknąć problemów bez monitoringu Piotra.
- Zastępstwo w nagłych wypadkach: Adrian lub Mateusz.

---

## 2025-11-21 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-21 Planowanie sprintu.md]
**Kategoria:** #Organizacja #Decyzja

- Powrót do koncepcji stałych zespołów zadaniowych w dziale rozwoju.
- Struktura zespołów: 2 backendowe, 1 frontendowy, testerki przypisane do zespołów.
- Przykłady zespołów celowych: Marek (Trust Center), Mateusz (AI/OCR).

---

## 2025-11-17 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-17 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-17%20Planowanie%20sprintu.md)
**Kategoria:** #Metodyka #Zadanie #Decyzja

- Wdrożenie planowania opartego o tablice w Teams (podział na projekty/osoby).
- Zasada "Brak wrzutek": zadania spoza sprintu tylko jako hotfixy lub po decyzji PM.
- Ścieżka zgłoszeń: deweloperzy nie przyjmują zadań bezpośrednio od konsultantów (samoobsługa tylko na bieżący sprint po uzgodnieniu).
- Daily: przegląd zgłoszeń z dnia poprzedniego i decyzja o podjęciu (20 min).

---

## 2025-11-14 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-14 Spotkanie projektowe - Repozytorium.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-14%20Spotkanie%20projektowe%20-%20Repozytorium.md)
**Kategoria:** #Backlog #Metodyka

- **Struktura backlogu:** Zdefiniowano hierarchię: Inicjatywa (cel biznesowy) → Epik → MVP (wartość) → Ficzer → Use Case → PBI.
- **Definicja MVP:** MVP to dostarczane wartości ("Value"), a nie zbiór funkcjonalności.
- **Inicjatywa:** Traktowana jako wytyczna/cel biznesowy (np. "skrócenie czasu wdrożeń"), nie jako element rozliczalny statusami.

---

## 2025-11-13 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-13 Notatka projektowa - Edytor procesów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-13%20Notatka%20projektowa%20-%20Edytor%20procesów.md)
**Kategoria:** #Zadanie #Wydanie

- Priorytet do końca roku: Odbiór WIM (Komunikator, Repozytorium).
- Priorytet do końca roku: Grudniowa paczka stabilna (Edytor formularzy, MVP Diagramu).
- Zaplanowano testy stabilności grudniowej paczki na środowisku Astrafox.

---

## 2025-11-12 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-12 Spotkanie projektowe - Przegląd wycen.md]
**Kategoria:** #Decyzja #Dokumentacja

- Dyskusja na temat właściciela na poziomie feature'a i epica.
- Obecnie Delivery Manager jest właścicielem, docelowo powinien być deweloper.
- Propozycja pracy na branchach per paczka w celu uproszczenia pracy.

---

## 2025-10-31 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-31 Planowanie sprintu.md]
**Kategoria:** #Dokumentacja #Decyzja

- Zaproponowano rozwiązanie na kanałach w Teams dla przestrzeni dokumentacji projektowej.
- Projekt minimalnie składa się z trzech plików: uzasadnienie biznesowe, rozbicie na MVP, plik architektoniczno-techniczny.
- Brakuje jednego miejsca do przechowywania i edycji dokumentacji projektowej dla wszystkich.

---

## 2025-10-23 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-23 Notatka projektowa - Edytor procesów.md]
**Kategoria:** #Organizacja #Decyzja #Roadmapa

- Konieczność rewizji roadmapy na końcówkę roku 2025 i 2026.
- Priorytet absolutny: Domykanie wdrożeń (WIM, Lot) w celu wystawienia faktur i zamknięcia projektów.
- Strategia rozwoju: Skupienie na wsparciu sprzedaży (atrakcyjność systemu) i wdrożeń/serwisu (skrócenie czasu wdrożeń o 30%).
- Termin: Propozycja nowej roadmapy (uzgodnionej z Działem Wdrożeń i Serwisu) ma zostać przedstawiona Zarządowi do 3 listopada 2025.

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Zadanie #Zespół

- Statystyki sprintu: 113 zgłoszeń zamkniętych, 180 pozycji zakończonych dewelopersko
- Uwagi: Dużo pracy nad stabilizacją wersji i błędami
- Planowanie pracy: Pozostały fizycznie 2 miesiące do końca roku (presja czasu)

---

## 2025-10-06 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Planowanie sprintu.md]
**Kategoria:** #Proces #Organizacja #Ryzyko

- Zidentyfikowano ryzyka: zaległości w testach, brak procesu planowania, brak zgłoszeń na prace, niejasny status zadań
- Wdrożenie nowego modelu planowania sprintu (indywidualne sesje, szacowanie `effortu`)
- Wprowadzenie miary `effort` (5=8h) i wymóg uzupełniania jej dla zadań sprintu
- Dyskusja nad zmianą formuły Daily i zasad przepinania zadań na kolejny sprint

---

## 2025-10-09 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-09 Rada architektów.md]
**Kategoria:** #Organizacja #Proces #HR #Ryzyko

- Ustalenie procesu pracy z backlogiem i zgłoszeniami na Radę (porządkowanie tagów, statusów)
- Dyskusja o podejściu biznesowym deweloperów, pomysł delegowania na wdrożenia wewnętrzne w celu zrozumienia potrzeb klienta

---

## 2025-09-16 - Rada architektów (część organizacyjna)

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-09-16 Organizacja pracy - Zgłaszanie błędów|2025-09-16 Zgłaszanie błędów]]

**Kategoria:** #Organizacja #Procesy

**Decyzja: Zgłaszanie błędów – kanały komunikacji**

*   **Problem:** Brak jasności gdzie zgłaszać błędy (Teams vs Backlog), duplikacja zgłoszeń, brak weryfikacji.
*   **Decyzja:** ✅ Zatwierdzone - zgłoszenia na dedykowane kanały Teams projektu (np. "Edytor procesów", "Moduł raportowy").
*   **Proces:** Kanały przeglądane przez "Trójkę Amigos" (DM + Dev + Tester), którzy weryfikują zgłoszenie przed wrzuceniem na Backlog.
*   **Szczegóły:** Zobacz [[Procesy/Zglaszanie-bledow|Procedura zgłaszania błędów]]

---

## 2025-09-09 - Rada architektów

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-09-09 Rada architektów|2025-09-09 Rada architektów]]

**Kategoria:** #Organizacja #Procesy

**Kontekst:**
Pojawiło się pytanie, gdzie powinny być przestrzeń do wrzucania pytań i pomysłów rozwojowych od konsultantów i wdrożeniowców (szczególnie od starszych wdrożeniowców i Mateusza). Obecnie takie pytania trafiają do backlogu, co zaśmieca go i miesza zadania do realizacji z pytaniami do rozważenia.

### Problem

- Zaśmiecanie backlogu pytaniami i pomysłami, które nie są jeszcze zadaniami do realizacji
- Brak jasnej ścieżki dla pytań i pomysłów rozwojowych
- Mieszanie zadań (które mają finansowanie) z pytaniami (które wymagają najpierw decyzji, czy w ogóle warto się nad tym pochylać)

### Decyzja

**Status:** 🔍 Do weryfikacji

**Ścieżka dla pytań i pomysłów:**

1. **Pytania (czy coś da się zrobić, jak to działa):**
   - Zgłaszanie przez proces wycen z oznaczeniem **"pytanie"** (nie wycena)
   - Alternatywnie: zgłaszanie bezpośrednio do Product Ownerów (Damian, Kamil, Łukasz, Janusz, Piotr Buczkowski)
   - Product Ownerzy przetwarzają pytania, analizują na radzie architektów
   - Na podstawie analizy powstaje projekt zapisany na wiki (jeśli pomysł jest wartościowy)
   - Dopiero na podstawie projektu powstają wpisy na backlogu (zadania do zrobienia)

2. **Pomysły rozwojowe (chcą, żeby było zrealizowane, ale nie ma chętnych do zapłacenia):**
   - Zgłaszanie przez proces wycen z kategorią **"pomysł rozwojowy"**
   - Proces wycen ma już taką kategorię

3. **Backlog:**
   - Backlog powinien zawierać **zadania do realizacji**, nie pytania i pomysły
   - Jeśli pytania/pomysły trafiają do backlogu, powinny być szybko przetworzone i przeniesione do odpowiedniej ścieżki
   - Możliwość ustawienia statusu "pytanie" lub "pomysł" dla szybkiej identyfikacji

### Szczegóły

- Proces wycen ma opcję oznaczenia jako "pomysł rozwojowy" lub "pytanie"
- Konsultanci mogą zgłaszać pytania bezpośrednio do Product Ownerów (zamiast przez backlog)
- Product Ownerzy przetwarzają pytania na radzie architektów
- Jeśli pomysł jest wartościowy, powstaje projekt na wiki, a następnie zadania na backlogu

**Uwaga:** Rozważano również wznowienie tablicy analitycznej (jak kiedyś), ale uznano, że lepiej użyć istniejących procesów (wyceny) z odpowiednimi oznaczeniami.

### Zadania

- **Damian Kamiński:** Weryfikacja procesu wycen – czy można oznaczać jako "pytanie"
- **Damian Kamiński:** Komunikacja do konsultantów dotycząca ścieżki zgłaszania pytań i pomysłów
- **Product Ownerzy:** Przetwarzanie pytań i pomysłów z backlogu (przeniesienie do odpowiedniej ścieżki)

### Punkty otwarte

- Czy wznowić dedykowaną tablicę analityczną dla pytań i pomysłów?
- Czy ograniczyć dostęp konsultantów do backlogu tylko do bugów i hotfixów?
- Jak często przeglądać pytania i pomysły rozwojowe (dedykowane spotkanie czy w ramach istniejących spotkań)?

---

## 2025-08-29 - Planowanie sprintu (przerwane)

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-29 Planowanie sprintu-codex|2025-08-29 Planowanie sprintu-codex]]

**Kategoria:** #Organizacja #Metodologia

**Kontekst:**
Spotkanie planowania sprintu zostało przerwane z powodu pilnych zadań związanych z wdrożeniem dla klienta WIM. Główna część spotkania dotyczyła problemów organizacyjnych działu i metodologii pracy, co doprowadziło do zaplanowania natychmiastowej retrospekcji.

### Decyzje architektoniczne i standardy

**1. Wszystkie zadania i bugi muszą być w Azure DevOps:**
- ✅ Zatwierdzone - brak odstępstw od standardu
- Wszystko w Azure, bez Exceli/Wordów (nacisk Janusza i Basi)
- Uzasadnienie: możliwość wyszukiwania, śledzenia historii, przejęcia przez innych

**2. Projekty opisujemy na Wiki, zadania na backlogu:**
- ✅ Zatwierdzone
- Backlog to zadania do zrobienia, nie miejsce na opis projektu

**3. Feature'y muszą mieć początek i koniec:**
- ✅ Zatwierdzone
- Feature to funkcjonalność do dostarczenia, nie nieskończony opis
- Przykład zły: "Raport Gantta"
- Przykład dobry: "Wprowadzić funkcjonalność X"

### Ryzyka i blokery zidentyfikowane

**1. Chaos w organizacji pracy:**
- **Wpływ:** Wysoki
- **Mitygacja:** Retrospekcja w poniedziałek 9:00-12:00, reorganizacja działu
- **Kontekst:** Odejście Krystyny, brak projektów

**2. Brak zaangażowania testerek w projekty:**
- **Wpływ:** Wysoki
- **Mitygacja:** Wprowadzenie modelu "Trójki Amigos" (projektant, deweloper, tester)
- **Kontekst:** Powrót do sprawdzonego modelu z modułu raportowego

**3. Brak dokumentacji projektowej:**
- **Wpływ:** Średni
- **Mitygacja:** Wykorzystanie AI do generowania dokumentacji z transkrypcji
- **Szczegóły:** Zobacz [[../Automatyzacja-dokumentacji-AI/CHANGELOG|Automatyzacja-dokumentacji-AI]]

**4. Zbyt duża ilość zadań, brak czasu:**
- **Wpływ:** Wysoki
- **Mitygacja:** Ustawienie priorytetów, obrona przed strumieniem zadań

### Metodologia pracy – Model "Trójki Amigos" (Three Amigos)

**Opis:** Dla każdego większego projektu tworzony jest zespół składający się z:
- **Projektant** (od strony biznesowej): Łukasz, Damian, Kamil, Janusz
- **Deweloper** (od strony technicznej)
- **Tester** (od strony UX i funkcjonalnej): Barbara, Oktawia, Patrycja

**Zasady:**
- Zespół jest formalnie ogłaszany
- Odpowiedzialny za dowiezienie projektu jest lider (np. Damian)
- Zespół ma za zadanie najpierw zrobić projekt (koncepcję), potem wytworzenie
- Wszyscy członkowie zespołu wiedzą o zmianach w trakcie wytwarzania
- Testerki będą angażowane w spotkania projektowe przed rozpoczęciem prac

**Przykłady projektów:**
- Komunikator (AMODIT Talk)
- Repozytorium dla WIM
- Process Builder (Edytor procesów)
- Edytor diagramów
- Edytor reguł
- WCAG

### Specjalizacja testerek

- **Barbara** – specjalistka od modułu raportowego
- **Oktawia** – specjalistka od e-Doręczeń
- **Patrycja** – specjalistka od e-podpisów

**Uwaga:** Specjalizacja nie wyklucza innych testerek z danego tematu, ale zapewnia eksperta w danej dziedzinie.

### Standardy pracy w Azure DevOps

**Zasady bezwzględne:**

1. **Wszystko w Azure DevOps:**
   - ✅ Wszystkie zadania, bugi, feature'y w Azure DevOps
   - ❌ Brak odstępstw: Excel, Word, czat, inne narzędzia

2. **Struktura w Azure DevOps:**
   - **Epic** – duży projekt (np. "Komunikator")
   - **Feature** – funkcjonalność do dostarczenia (musi mieć początek i koniec, Definition of Done)
   - **PBI** – zadanie do zrobienia (oszacowane czasowo)
   - **Bug** – błąd powiązany z Feature/PBI

3. **Wiki vs Backlog:**
   - **Wiki** – miejsce na opis projektu, koncepcję, dokumentację
   - **Backlog** – miejsce na zadania do zrobienia (z oszacowaniem, kryteriami akceptacji)

### Problemy zidentyfikowane

**1. Chaos w organizacji:**
- Testerki nie są brane do pracy nad projektami tak jak do modułu raportowego (poczucie wykluczenia)
- Testerki są na końcu procesu, nie wiedzą co ma robić
- Zadania przychodzą w Excelu zamiast w Azure DevOps
- Brak zaangażowania w projektowanie

**2. Przeciążenie pracą:**
- Zbyt duża ilość zadań
- Brak czasu na przygotowanie ofert/projektów
- Pilne zadania przerywają planowanie
- Trudność w obronie przed strumieniem zadań

**3. Brak dokumentacji:**
- Brak podstawowej dokumentacji funkcjonalnej
- Trudność w przekazywaniu wiedzy
- Brak standardów tworzenia dokumentacji

### Planowane działania

**1. Retrospekcja w poniedziałek 9:00-12:00:**
- Dyskusja o reorganizacji działu
- Organizacja projektów
- Tworzenie dokumentacji projektowej
- Zarządzanie

**2. Wprowadzenie modelu "Trójki Amigos":**
- Formalne ogłaszanie zespołów projektowych
- Zaangażowanie testerek od początku projektu

**3. Wykorzystanie AI do dokumentacji:**
- Każdy członek zespołu może tworzyć dokumentację metodą nagrania + AI
- Publikacja na Wiki

**4. Utrzymanie standardów Azure DevOps:**
- Bezwzględne trzymanie się Azure DevOps
- Brak odstępstw na Excel/Word/czat

