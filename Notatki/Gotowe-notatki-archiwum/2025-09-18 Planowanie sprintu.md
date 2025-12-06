# Planowanie Sprintu – 2025-09-18

> 🛡️ Zweryfikowano (Review) w dniu 2025-12-04

**Sprint:** [nie określono]
**Okres:** [nie określono]

**Powiązane projekty:**
- `Moduly/AMODIT Copilot` – tematy 1, 2, 3, 4

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| Baza wiedzy w Copilot | `Moduly/AMODIT Copilot` | ✅ Funkcjonalność dostępna | Wymaga dokumentacji i instrukcji |

---

## 2. Plany na sprint

### Baza wiedzy w Copilot – demo i wyjaśnienia

**Projekt:** `Moduly/AMODIT Copilot`

**Kontekst i cel:**
Spotkanie poświęcone demo i wyjaśnieniom funkcjonalności bazy wiedzy w Copilot. Omówiono:
- Jak działa prywatna baza wiedzy
- Jak dodawać dokumenty do bazy wiedzy
- Uprawnienia i bezpieczeństwo
- Funkcje w silniku reguł do zarządzania bazą wiedzy

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przygotowanie instrukcji zarządzania bazą wiedzy | **Janusz** | - | Na podstawie nagrania ze spotkania |

**Szczegóły techniczne:**
- Funkcja w silniku reguł: `Knowledge Base Document Insert`
- Parametry funkcji:
  - `Collection` – nazwa bazy wiedzy (np. "Dokumenty ze spraw")
  - `Content` – zawartość dokumentu do dodania
  - `Metadata` – obiekt JSON z metadanymi (opcjonalnie)
  - `Unique ID` – unikalny identyfikator dokumentu (opcjonalnie, domyślnie używa `case`)
- Inne funkcje związane z bazą wiedzy:
  - `Knowledge Base Search` – przeszukiwanie bazy wiedzy
  - `Ask AI` – wykorzystanie wyników wyszukiwania do generowania odpowiedzi
- Uprawnienia do bazy wiedzy:
  - Administratorzy mogą zarządzać bazami wiedzy
  - Dostęp do konkretnej bazy wiedzy można ustawić na: Administratorzy, Wszyscy, Właściciel, Custom (określone grupy)
  - W przypadku Custom, trzeba dodatkowo zaznaczyć dostęp w ustawieniach grup

**Decyzje podjęte przy planowaniu:**
- ✅ **Dokumenty do bazy wiedzy muszą być dodawane świadomie** – nie może być automatycznego dodawania wszystkich dokumentów ze spraw do bazy wiedzy
- ✅ **Zerwanie uprawnień do sprawy** – dodanie dokumentu do bazy wiedzy powoduje zerwanie uprawnień do sprawy i przejście na uprawnienia do bazy wiedzy
- ✅ **Prywatna baza wiedzy per instancja** – każda instancja AMODIT ma swoją prywatną bazę wiedzy, nie ma dostępu między instancjami (np. Neuca nie ma dostępu do bazy wiedzy PKF)

**Ryzyka:**
- Brak dokumentacji może prowadzić do nieprawidłowego użycia funkcjonalności
- Możliwość przypadkowego udostępnienia poufnych danych przez dodanie dokumentu do bazy wiedzy bez odpowiednich uprawnień

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Świadome dodawanie dokumentów do bazy wiedzy | `Moduly/AMODIT Copilot` | ✅ Zatwierdzone | Bezpieczeństwo danych – dokumenty nie mogą być automatycznie dodawane do bazy wiedzy |
| Zerwanie uprawnień do sprawy przy dodaniu do bazy wiedzy | `Moduly/AMODIT Copilot` | ✅ Zatwierdzone | Uprawnienia do bazy wiedzy są odrębne od uprawnień do sprawy |
| Prywatna baza wiedzy per instancja | `Moduly/AMODIT Copilot` | ✅ Zatwierdzone | Izolacja danych między klientami |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Brak dokumentacji funkcjonalności bazy wiedzy | `Moduly/AMODIT Copilot` | Średni | Przygotowanie instrukcji na podstawie nagrania ze spotkania | **Janusz** |
| Optymalizacja zużycia tokenów | `Moduly/AMODIT Copilot` | Średni | Do rozważenia – klient Neuca zgłosił problem z wysokim zużyciem tokenów (100000 tokenów na jedno zapytanie) | **Zespół** |
| Długi czas zapisywania dokumentów do bazy wiedzy | `Moduly/AMODIT Copilot` | Niski | Do zbadania – czy to kwestia funkcjonalności czy środowiska/połączenia | **Zespół** |

---

## 5. Pytania i potrzeby klientów

### Neuca i PKF – przeszukiwanie dokumentów

**Projekt:** `Moduly/AMODIT Copilot`

**Kontekst:**
Miłosz Śliwiński (Neuca) zgłosił potrzebę przeszukiwania dokumentów w Copilot. Obecnie funkcjonalność jest dostępna, ale wymaga świadomego dodania dokumentów do bazy wiedzy.

**Wyjaśnienie:**
- Przeszukiwanie dokumentów jest możliwe, ale dokumenty muszą być najpierw dodane do bazy wiedzy
- Dodawanie dokumentów odbywa się świadomie z poziomu reguł procesu za pomocą funkcji `Knowledge Base Document Insert`
- Nie ma automatycznego dodawania wszystkich dokumentów ze spraw do bazy wiedzy ze względów bezpieczeństwa

**Decyzja:**
- ✅ Funkcjonalność jest dostępna, ale wymaga świadomego zarządzania bazą wiedzy
- ✅ Nie obiecujemy automatycznego przeszukiwania wszystkich dokumentów ze spraw

### Neuca – optymalizacja zużycia tokenów

**Projekt:** `Moduly/AMODIT Copilot`

**Kontekst:**
Miłosz Śliwiński (Neuca) zgłosił problem z wysokim zużyciem tokenów podczas korzystania z Copilota. Przykład: jedno zapytanie zużyło 100000 tokenów przy niskich limitach.

**Problem:**
- Gdy użytkownik pyta o procesy, Copilot przeszukuje definicje procesów
- Jeśli definicja procesu jest bardzo duża, Copilot czyta całą definicję
- To prowadzi do wysokiego zużycia tokenów

**Decyzja:**
- ⏸️ **Do rozważenia** – zespół ma się zastanowić nad optymalizacją zużycia tokenów
- Nie określono konkretnego rozwiązania ani terminu

---

## 6. Organizacja pracy

- **Spotkania:** Spotkanie planowania sprintu połączone z demo funkcjonalności bazy wiedzy
- **Nagranie:** Spotkanie zostało nagrane w celu przygotowania instrukcji zarządzania bazą wiedzy
- **Uwagi:** Spotkanie zostało przerwane i wznowione jako osobne spotkanie (osobna transkrypcja)

---

## 7. Uwagi techniczne

### Funkcje silnika reguł związane z bazą wiedzy

1. **Knowledge Base Document Insert**
   - Dodaje zawartość dokumentu do bazy wiedzy
   - Parametry: Collection, Content, Metadata (opcjonalnie), Unique ID (opcjonalnie)
   - Przykład użycia: dodanie treści załącznika ze sprawy do bazy wiedzy

2. **Knowledge Base Search**
   - Przeszukiwanie bazy wiedzy z poziomu reguł procesu
   - Można użyć w połączeniu z `Ask AI` do generowania odpowiedzi

3. **Get To Do**
   - Funkcja pomocnicza do pracy z bazą wiedzy

### Uprawnienia i dostęp

- **Copilot Access** w ustawieniach systemowych:
  - Można ustawić: None, Wszyscy, Administratorzy, Grupy
  - W przypadku Grup, trzeba dodatkowo zaznaczyć dostęp w ustawieniach grup
- **Organization Key** – ustawia się automatycznie przy pierwszym korzystaniu z Copilota
- **Zarządzanie bazami wiedzy** – każdy administrator może zarządzać bazami wiedzy i ustawiać uprawnienia dostępu

### Problemy techniczne zgłoszone podczas demo

1. **Długi czas zapisywania dokumentów do bazy wiedzy**
   - Może wynikać z tworzenia dodatkowej bazy wiedzy
   - Do zbadania czy to kwestia funkcjonalności czy środowiska/połączenia

2. **Brak IntelliSense dla nazw baz wiedzy w AMODIT Script**
   - Możliwość dodania podpowiedzi dla istniejących baz wiedzy

3. **Brak tytułu przy dodawaniu dokumentu z reguły**
   - Dokument dodany z reguły nie ma tytułu (można dodać ręcznie)

4. **Metadata jako obiekt**
   - Metadata powinno być obiektem JSON, nie zwykłym tekstem
   - Przykład: `{"ptaszki": "informacja"}` zamiast `"ptaszki"`

