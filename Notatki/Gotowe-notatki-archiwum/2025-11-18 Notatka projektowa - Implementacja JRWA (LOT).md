# Notatka projektowa – 2025-11-18 – Implementacja JRWA (LOT)

**Data:** 2025-11-18
**Temat główny:** Implementacja Jednolitego Rzeczowego Wykazu Akt (JRWA) w AMODIT dla klienta LOT.

> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-08

---

## 1. Struktura i Zarządzanie JRWA

**Komponent:** JRWA (nowa funkcjonalność)

### Cel i problem
Zaimplementowanie hierarchicznej struktury Jednolitego Rzeczowego Wykazu Akt (JRWA) w AMODIT, która pozwoli na kategoryzowanie spraw (zbiorów pism) i ich efektywne zarządzanie.

### Rozważane alternatywy
| Opcja | Opis | Status |
|-------|------|--------|
| Dedykowana tabela | Przechowywanie struktury JRWA w oddzielnej tabeli w bazie danych. | ✅ Wybrana – zapewnia wydajność i oddzielenie logiki od spraw. |
| Oparcie na procesach | Użycie istniejących mechanizmów procesów AMODIT (np. dynamicznych źródeł danych) do zarządzania JRWA. | ❌ Odrzucona – obawa o wydajność i "pajęczyny zależności". |

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- Struktura JRWA będzie przechowywana w **dedykowanej tabeli** w bazie danych (`JRWA_Schema`).
- Tabela ta będzie zawierać: symbol, hasło klasyfikacyjne, kategorię archiwalną, opis, daty obowiązywania (`data_obowiazywania_od`, `data_obowiazywania_do`).
- Schemat JRWA jest faktycznie strukturą płaską (np. 4-cyfrowe symbole), mimo wizualnej prezentacji jako drzewo.
- Zarządzanie schematem JRWA (dodawanie/usuwanie/modyfikacja węzłów) w pierwszej fazie będzie możliwe **tylko z poziomu bazy danych**, wymaga formalnej uchwały klienta.
- W przyszłości rozważany dedykowany interfejs do zarządzania schematem, podobny do repozytorium.

### Szczegóły techniczne:
- Tabela `JRWA_Schema` (płaska struktura symboli).
- Tabela `JRWA_Permissions` (uprawnienia).
- Tabela `JRWA_CaseMapping` (połączenie struktury ze sprawą).
- Indeksowanie kluczowych pól (rok, numer teczki, nazwa) w tabeli `case definition` lub dedykowana tabela indeksująca JRWA.
- Użycie zwykłych ID dla relacji, GUID opcjonalnie jako dodatkowy element.

### Punkty otwarte
- Konieczność doszukania się w instrukcji kancelaryjnej sposobu numerowania teczek (przez Kamila).
- Weryfikacja, czy faktycznie nie ma potrzeby kopiowania schematu JRWA co roku (Janusz sugeruje daty obowiązywania na węzłach).

---

## 2. Definicja i Wpinanie Spraw do JRWA

**Komponent:** JRWA (funkcjonalność wpinania)

### Cel i problem
Umożliwienie użytkowników podpinania spraw AMODIT (pojedynczych pism) do "teczek spraw" (zbiorów pism w nomenklaturze SZD), które są sklasyfikowane w strukturze JRWA.

### Rozważane alternatywy
| Opcja | Opis | Status |
|-------|------|--------|
| Pole Odnośnik | Wykorzystanie istniejącego pola `Odnośnik` na formularzu sprawy do wskazania teczki sprawy JRWA. | ❌ Odrzucona – mała optymalizacja pod konkretne działanie, nieobsługa uprawnień, słabe UX. |
| Dedykowany panel | Nowy, dedykowany panel na formularzu sprawy (np. prawy panel, jak repozytorium), zawierający dedykowane okienko lub 2 zakładki do wyboru katalogu JRWA. | ✅ Wybrana – lepsze UX, możliwość implementacji uprawnień, wydajność. |

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- Na formularzu sprawy zostanie dodany **dedykowany panel** (lub okienko) do wyboru katalogu JRWA.
- Panel będzie miał dwie zakładki:
    1. Wpisywanie symbolu/nazwy katalogu JRWA (z autouzupełnianiem).
    2. Widok drzewka struktury JRWA do przeklikania (jak w repozytorium).
- Użytkownik wpina amoditową sprawę (pojedyncze pismo) do istniejącej "teczki sprawy".
- "Teczka sprawy" (w rozumieniu JRWA) będzie procesem w AMODIT (podobnie do e-teczek pracowniczych).
- Jedna amoditowa sprawa może być wpięta **tylko do jednego miejsca** w JRWA. W przypadku wielu kontekstów (np. pismo dotyczy 2 tematów) należy utworzyć **kopię amoditowej sprawy**.

### Szczegóły techniczne:
- W teczce sprawy (procesie) będzie pole do przypisania ID pozycji z `JRWA_Schema`.
- Linkowanie amoditowych spraw do teczek sprawy JRWA (np. `Connected to case ID`).

### Ograniczenia / Poza zakresem
- Na początek, widok JRWA dla zwykłego pracownika będzie tabelaryczny (lista spraw), bez możliwości przeglądania struktury drzewa. Widok struktury będzie potrzebny dla archiwistów na późniejszym etapie.

---

## 3. Uprawnienia do JRWA

**Komponent:** JRWA (mechanizm uprawnień)

### Cel i problem
Zapewnienie, że użytkownicy mają prawo zakładać "teczki spraw" tylko w określonych węzłach JRWA, zgodnie z przynależnością działową i z uwzględnieniem dziedziczenia uprawnień.

### Rozważane alternatywy
Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- Uprawnienia będą zarządzane na poziomie **działów**, z możliwością definiowania wyjątków.
- Struktura uprawnień będzie **dziedziczona** w dół drzewa JRWA (jeśli dział ma dostęp do węzła nadrzędnego, ma też dostęp do podrzędnych, chyba że zdefiniowano wyjątek).
- Dla zalogowanego użytkownika system będzie wyświetlał **tylko te katalogi JRWA, do których ma on uprawnienia** do tworzenia teczek.
- Mechanizm uprawnień będzie działał na dedykowanej tabeli (`JRWA_Permissions`).

### Szczegóły techniczne:
- Tabela `JRWA_Permissions` (zestaw uprawnień przypięty do folderów/węzłów JRWA, z dziedziczeniem).
- Indeksowane uprawnienia dla szybkiego wyszukiwania.

---

## 4. Wydajność i Raportowanie JRWA

**Komponent:** JRWA (wydajność i raportowanie)

### Cel i problem
Zapewnienie wydajnego wyszukiwania i raportowania spraw w kontekście JRWA, szczególnie dla archiwistów, oraz uniknięcie problemów wydajnościowych przy dużej liczbie spraw.

### Rozważane alternatywy
Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- **Wydajność:** Wyszukiwanie spraw w JRWA będzie realizowane na podstawie dedykowanej tabeli indeksującej (`JRWA_CaseMapping`) lub poprzez indeksy na polach w tabeli `case definition` (np. rok, numer teczki, nazwa).
- **Raportowanie:** Docelowo potrzebne będą dedykowane endpointy dla modułu raportowego, aby umożliwić archiwistom wyciąganie danych i generowanie raportów (np. spisy spraw, sprawy do brakowania).
- **Eksport do Archiwum Państwowego:** Należy uwzględnić konieczność eksportu danych (np. plik o odpowiedniej strukturze, jak w e-teczce, XML opisujący skany).

### Punkty otwarte
- Brak wiedzy biznesowej o tym, jak pracują archiwiści (czy preferują widok tabelaryczny, czy struktury drzewa) – Kamil skontaktuje się z partnerem AMODIT (Artur, specjalista ds. archiwów) w celu pozyskania wiedzy.

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: Podstawowa implementacja JRWA

**Cel:** Prezentacja szkieletu rozwiązania do końca roku (28 listopada).
**Zakres:**
- Struktura JRWA w dedykowanej tabeli (edycja z poziomu bazy danych).
- Mechanizm uprawnień (dziedziczenie, wyświetlanie tylko dostępnych katalogów).
- Dedykowany panel na formularzu sprawy do wpinania spraw do JRWA (z wpisywaniem symbolu/nazwy lub drzewkiem).
- Podstawowe raportowanie (płaski widok spraw).

### MVP 2: Rozszerzone zarządzanie i raportowanie

**Cel:** Uzupełnienie funkcjonalności o bardziej zaawansowane mechanizmy.
**Zakres:**
- Interfejs do zarządzania strukturą JRWA (dodawanie/edycja węzłów).
- Rozbudowane raportowanie dla archiwistów (widok struktury drzewa).
- Obsługa "teczek nie tworzących akt sprawy" (śmietnik).

---

## Powiązane projekty:
- `Klienci/LOT/JRWA`

---

## Punkty do dalszej dyskusji (globalne)

- Ostateczny kształt i UX panelu do wpinania spraw w JRWA (Mariusz ma przygotować mockup).
- Weryfikacja kierunku technologicznego dla frontu aplikacji (Mariusz/Kamil/Adrian - konsultacja z Januszem/Piotrem).
- Możliwość automatyzacji częściowej aktualizacji TrustCenter.
- Brak wiedzy biznesowej o pracy archiwistów.