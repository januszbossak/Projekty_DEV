> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-07

# Planowanie Sprintu – 2025-11-13

**Sprint:** 47
**Okres:** [do uzupełnienia]

**Powiązane projekty:**
- `Klienci/WIM/Repozytorium-plikow-DMS` – tematy 1, 2
- `Klienci/LOT/JRWA` – temat 2
- `cross-cutting/Wydajnosc` – temat 3

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| Repozytorium | `klienci/WIM/Repozytorium` | 🔄 W analizie | Specyfikacja w trakcie |
| JRWA dla LOT-u | `Klienci/LOT/JRWA` | 🔍 Do rozpracowania | Ogrom roboty, wymaga szczegółowego planowania |
| ADE | `Klienci/LOT/ADE` | 🔄 W trakcie | - |

---

## 2. Plany na sprint

### Repozytorium Plików (DMS)

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`

**Kontekst i cel:**
Dostarczenie funkcjonalności repozytorium, aby można było odebrać wdrożenie w WIM. Klient potrzebuje centralnego miejsca do przechowywania plików niezwiązanych ze sprawami (dokumenty korporacyjne, szablony, materiały referencyjne).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Backend do repozytorium | **Piotr** | [DO USTALENIA] | Spotkanie 13 listopada |
| Przygotowanie wzoru importu/eksportu dla klienta | **Kamil** | [DO USTALENIA] | Każdy klient ma swój wzór, ERP też ma swoją strukturę |
| Dodanie pozycji w repozytorium | [DO USTALENIA] | [DO USTALENIA] | - |
| Wyświetlenie drzewka | [DO USTALENIA] | [DO USTALENIA] | Wymaga układu hierarchicznego w raporcie typu tabela |
| Usunięcie pozycji | [DO USTALENIA] | [DO USTALENIA] | - |

**Szczegóły techniczne:**
- Rejestr jako struktura repozytorium (dla każdego węzła przechowywanie: daty obowiązywania, kategoria archiwalna, uprawnienia)
- Węzły jako sprawy w rejestrze z relacją nadrzędny-podrzędny
- Potrzebny układ hierarchiczny w raporcie typu tabela (jak w Gancie) do wyświetlenia drzewka
- Opis architektury od Piotra może być podpięty jako pierwszy ficzer w ramach MVP1

**Decyzje podjęte przy planowaniu:**
- Opis architektury technicznej może być podpięty jako osobny ficzer "Architektura" w ramach MVP1 (jeśli nie jest w pełni zrealizowany w pierwszym MVP)
- Ogólny opis architektury może być tylko opisem technicznym, z którego nie będą tworzone PBI (PBI będą wynikać z konkretnych ficzerów funkcjonalnych)
- Jeśli trzeba coś konkretnego zrobić w bazie (np. dodać kolumnę), to może być normalny ficzer w ramach MVP1

**Ryzyka:**
- [DO USTALENIA]

---

### JRWA dla LOT-u

**Projekt:** `klienci/LOT/JRWA`

**Kontekst i cel:**
JRWA (Jednolity Rzeczowy Wykaz Akt) jest krwiobiegiem każdej sprawy. LOT będzie miał hybrydę – 90% dokumentów w papierze, a w AMODIT rejestrowane będzie ich istnienie. Pozostałe 10-15% (korespondencja, wnioski) będą w pełni w AMODIT. Każda sprawa musi być ujęta w JRWA, czyli musi być dla niej założona odpowiednia teczka. Kluczowy jest mechanizm, który pozwala szybko, łatwo i zgodnie z uprawnieniami wyszukać i przypiąć dany dokument do odpowiedniej kategorii JRWA.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Rozpracowanie JRWA | **Kamil** | [DO USTALENIA] | Ostatni dzień na zaplanowanie i przedstawienie do akceptacji (13 listopada) |
| Analiza dokumentów przygotowanych przez Janusza | **Zespół** | [DO USTALENIA] | Dokumenty zawierają głęboką analizę i dziesiątki przypadków użycia |

**Szczegóły techniczne:**
- JRWA realizowane jako rejestr
- Węzły jako sprawy w rejestrze z relacją nadrzędny-podrzędny
- Potrzebny układ hierarchiczny w raporcie typu tabela (jak w Gancie) do wyświetlenia drzewka
- Dla każdego węzła JRWA przechowywanie: daty obowiązywania, kategoria archiwalna, uprawnienia
- JRWA jest definiowane co roku na nowo (zmiany w kategoryzacji są uchwalane rzadko przez wysoko postawione gremium)
- Nie ma potrzeby eksportowania i importowania struktury co roku – raczej jednorazowy import, a potem zarządzanie tym w AMODIT (ustawianie dat obowiązywania, tworzenie nowych węzłów)

**Decyzje podjęte przy planowaniu:**
- [DO USTALENIA]

**Ryzyka:**
- Ogrom roboty – wymaga szczegółowego rozpracowania
- Wpływ na proces u klienta – harmonogramy z Michałem Wierzbickim (PM), deadline'y z LOT-em

---

### Bugi i zgłoszenia

**Projekt:** [DO USTALENIA]

**Kontekst i cel:**
Przegląd bugów, które wpadły w ciągu ostatnich dwóch tygodni i decyzja, czy bierzemy je do następnego sprintu. Nowe bugi powinny być od razu planowane na najbliższe sprinty, a nieistotne od razu zamykane.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przegląd bugów z ostatnich dwóch tygodni | **Zespół** | [DO USTALENIA] | - |
| Zgłoszenie z City Handlowego (mechanizm przelewów przestał działać po aktualizacji) | **Łukasz** | [DO USTALENIA] | Przypisane do Łukasza |
| Zgłoszenie z PCBC | **Ania** | [DO USTALENIA] | Ania się tym zajmowała, coś o podsumowaniach – do dopytań |

**Decyzje podjęte przy planowaniu:**
- [DO USTALENIA]

**Ryzyka:**
- [DO USTALENIA]

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Metodologia planowania sprintu: "przestań zaczynać, zacznij kończyć" | `cross-cutting/Wydajnosc` | ✅ Zatwierdzone | Lepsze dowożenie przez paczki (prezenty/epiki) |
| Limit WIP na poziomie prezentu (epica) | `cross-cutting/Wydajnosc` | ✅ Zatwierdzone | Mamy 9 deweloperów, ale 3 testerki – prawdziwy systemowy limit WIP dla całego działu wynosi 3, a nie 9 |
| Prezent (epic) powinien być dowieziony maksymalnie w 1-3 sprinty | `cross-cutting/Wydajnosc` | ✅ Zatwierdzone | Coś wartościowego dla klienta |
| Dany zespół nie ma innego celu niż dowiezienie paczki | `cross-cutting/Wydajnosc` | ✅ Zatwierdzone | Nie powinno być wrzutek w trakcie sprintu |
| Strategia: stabilizacja, ściskamy hamulec, nie dorzucamy nowych funkcjonalności | `cross-cutting/Wydajnosc` | ✅ Zatwierdzone | Kończymy to, co zaczęliśmy: repozytorium, JRWA, ADE |
| Edytor formularza, diagramu i matrycę uprawnień zostawiamy na razie | `Moduly/Edytor-procesow` | ✅ Zatwierdzone | To nasze wewnętrzne narzędzia, żaden klient na to nie czeka |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Ogrom roboty w JRWA | `klienci/LOT/JRWA` | Wysoki | Szczegółowe rozpracowanie, analiza dokumentów | **Kamil** |
| Deadline'y z LOT-em | `klienci/LOT/JRWA` | Wysoki | Kontakt z Michałem Wierzbickim (PM), ustalenie harmonogramów | **Kamil** |
| Brak zastępstwa dla Mateusza Kisiela | [DO USTALENIA] | Średni | Wiedza o serwerach musi zostać upubliczniona, żeby w razie nieobecności inni wiedzieli, co robić | **Janusz** |
| Ograniczona ilość testerek jako wąskie gardło | `cross-cutting/Wydajnosc` | Wysoki | Dawać na sprint tyle MVP, ile mamy testerek (limit WIP = 3) | **Janusz** |

---

## 5. Organizacja pracy

- **Urlopy:** [DO USTALENIA]
- **Spotkania:** 
  - Spotkanie backendu do repozytorium – 13 listopada (wrzucone w kalendarz)
- **Przesunięcia:** [DO USTALENIA]

---

## 6. Metodologia planowania sprintu (decyzje)

### Zasady planowania

**Główna zasada:** "Przestań zaczynać, zacznij kończyć"

**Struktura hierarchiczna:**
1. **Inicjatywa** – np. "dostarczenie funkcjonalności repozytorium, aby można było odebrać wdrożenie w WIM"
   - Musi dawać mierzalną wartość
2. **Prezent (epic)** – nasze MVP
   - Powinien być dowieziony maksymalnie w 1-3 sprinty
   - Coś wartościowego dla klienta
3. **Ficzery** – pod prezenty
4. **PBI** – pod ficzery z najbliższego sprintu

**Proces planowania:**
1. Burza mózgów i tworzenie listy wszystkich funkcjonalności w ramach MVP
2. Wybór tego, co jest absolutnie niezbędne dla pierwszej paczki (najszybszy feedback od użytkownika)
3. Szacowanie, ile sprintów to zajmie
4. Jeśli za duże – dzielenie
5. Dopiero wtedy, dla ficzerów z najbliższego sprintu, rozpisujemy PBI

**Limit WIP:**
- Mamy 9 deweloperów, ale 3 testerki
- Prawdziwy systemowy limit WIP dla całego działu wynosi 3, a nie 9
- Powinniśmy dawać na sprint tyle MVP, ile mamy testerek

**Cel sprintu:**
- Nie "zespół coś robi", tylko "zespół kończy prezent", który był np. w testach
- Jeśli coś nie przeszło testów, zespół nie bierze się za nic nowego, dopóki tego nie dokończy
- Jednocześnie inny zespół, który swój prezent skończył, może wziąć następny

**Przykład struktury:**
- Cel: "wprowadzenie podglądu treści szablonów PDF i DOCX z poziomu sprawy" (prezent)
- Pod tym rozpisane są ficzery
- Przed daniem do zrobienia musimy zdecydować, czy wszystkie ficzery są do zrobienia w ramach jednej paczki
- Jeśli za duża, musimy coś jawnie wywalić albo zaplanować na dwa sprinty

**Uwagi:**
- Przez to, że mamy teraz trochę bałaganu, deweloperzy nie patrzą na ficzery, tylko na PBI
- Ta metoda trochę zmusi, żeby robiąc PBI, zajrzeli wyżej i zobaczyli, że to jest kawałek czegoś większego
- "Skończone kodowanie" to nie znaczy "skończone zadanie"
- "Skończone" powinno oznaczać: przetestowane, zweryfikowane i gotowe do wydania

