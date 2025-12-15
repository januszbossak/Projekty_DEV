# Planowanie Sprintu – 2025-12-05

**Data:** 2025-12-05  
**Typ:** Planowanie Sprintu  
**Temat główny:** JRWA - pole Odnośnik do źródła zewnętrznego

---

## 1. JRWA - Wyświetlanie wartości po wyborze kategorii

**Komponent:** Edytor Formularza (pole Odnośnik do źródła zewnętrznego)

### Kontekst i cel

Po wybraniu kategorii JRWA w polu Odnośnik do źródła zewnętrznego, użytkownik widzi tylko placeholder "Znajdź kategorię archiwalną". Konieczne jest ustalenie, jakie dane powinny być wyświetlane po dokonaniu wyboru, aby użytkownik miał pełny kontekst wybranej kategorii (symbol, nazwa, opis, kategoria archiwalna).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Symbol + Nazwa | Wyświetlanie symbolu (np. "001") i nazwy kategorii (np. "Rada nadzorcza") | ✅ Wybrana – najbardziej przejrzyste dla użytkownika |
| Symbol + Nazwa + Kategoria | Dodatkowo kategoria archiwalna | ⏸️ Odroczona – kategoria jest mniej istotna dla użytkowników końcowych, bardziej dla archiwistów |
| Tylko nazwa | Wyświetlanie samej nazwy bez symbolu | ❌ Odrzucona – użytkownicy szukają po symbolach |
| Opis | Wyświetlanie opisu kategorii | ❌ Odrzucona – opis może być bardzo długi, wymaga zmiany pola na długi tekst |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Po wyborze kategorii JRWA w polu powinien wyświetlać się **symbol + nazwa** (np. "001 Rada nadzorcza").

**Szczegóły techniczne:**
- Pole: Odnośnik do źródła zewnętrznego (JRWA)
- Format wyświetlania: `{symbol} {nazwa}`
- Rozszerzenie funkcjonalności: możliwość wyboru wielu kolumn do wyświetlania (analogicznie do standardowego pola Odnośnik)

### Ograniczenia / Poza zakresem

- Kategoria archiwalna nie będzie wyświetlana w głównym polu (jest mniej istotna dla użytkowników końcowych)
- Opis nie będzie wyświetlany ze względu na potencjalną długość

### Zadania / Dalsze kroki

- **Marek:** Rozbudować pole Odnośnik do źródła zewnętrznego o możliwość wyboru wielu kolumn do wyświetlania (symbol + nazwa) – analogicznie do standardowego pola Odnośnik

---

## 2. JRWA - Wyświetlanie ścieżki hierarchicznej w wynikach wyszukiwania

**Komponent:** Edytor Formularza (pole Odnośnik do źródła zewnętrznego)

### Kontekst i cel

Podczas wyszukiwania kategorii JRWA użytkownik widzi tylko nazwę znalezionej pozycji (np. "Walne zgromadzenie"), bez kontekstu hierarchicznego (skąd pochodzi w strukturze drzewa). Utrudnia to identyfikację właściwej kategorii, szczególnie gdy istnieją podobne nazwy w różnych gałęziach.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

W wynikach wyszukiwania należy wyświetlać pełną ścieżkę hierarchiczną z zaznaczeniem pozycji nadrzędnych na szaro.

**Przykład:**
- Wyszukiwanie: "Walne zgromadzenie"
- Wyświetlanie:
  - **Zarządzanie** (szary)
  - **Gremia kolegialne** (szary)
  - **Walne zgromadzenie** (czarny/aktywny)

**Szczegóły techniczne:**
- Mechanizm: pobranie `parent` dla znalezionej pozycji i wyświetlenie całej ścieżki
- Wizualizacja: pozycje nadrzędne na szaro, wybierana pozycja normalnym kolorem

### Zadania / Dalsze kroki

- **Marek:** Dodać wyświetlanie ścieżki hierarchicznej (parent) w wynikach wyszukiwania JRWA

---

## 3. JRWA - Brakujące pole "Elektroniczne/Papierowe"

**Komponent:** Edytor Formularza (pole Odnośnik do źródła zewnętrznego)

### Kontekst i cel

W oryginalnym zgłoszeniu JRWA było wymagane pole określające sposób prowadzenia dokumentacji (elektroniczne vs papierowe). To pole zostało pominięte w implementacji, a jest istotne dla archiwistów i może być kluczowe przy wyszukiwaniu (mogą istnieć 2 podobne węzły – jeden dla dokumentacji elektronicznej, drugi dla papierowej).

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Dodać pole "Elektroniczne/Papierowe" do:
1. Struktury danych źródła JRWA
2. Wyników wyszukiwania (jako dodatkowa kolumna/oznaczenie)
3. Drzewa hierarchicznego (jako oznaczenie przy pozycjach)

**Szczegóły techniczne:**
- Pole powinno być widoczne już na poziomie wyszukiwania i drzewa
- Pomaga rozróżnić podobne węzły dotyczące różnych form prowadzenia dokumentacji

### Zadania / Dalsze kroki

- **Marek:** Dodać pole "Elektroniczne/Papierowe" do źródła JRWA (struktura danych, wyszukiwanie, drzewo)

---

## 4. JRWA - Wyszukiwanie zaawansowane (okno modalne z drzewem)

**Komponent:** Edytor Formularza (pole Odnośnik do źródła zewnętrznego)

### Kontekst i cel

Obecny mechanizm wyboru JRWA jest hybrydą wyszukiwarki i drzewa, co powoduje problemy:
- Nie jest dobrą wyszukiwarką (ograniczone wyniki, brak filtrów)
- Nie jest dobrym drzewem (brak wizualizacji hierarchii, wcięć)
- Użytkownicy początkujący nie znają struktury JRWA i potrzebują pełnego drzewa do nauki
- Użytkownicy zaawansowani potrzebują szybkiego wyszukiwania po symbolach

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Drzewo z wcięciami w głównym polu | Wyświetlanie hierarchii bezpośrednio w rozwijanej liście | ❌ Odrzucona – nie załaduje się 900+ pozycji, problemy z wydajnością |
| Czysta wyszukiwarka (bez drzewa) | Tylko pole tekstowe do wpisywania | ❌ Odrzucona – użytkownicy początkujący nie wiedzą, co wpisać |
| Okno modalne z drzewem + wyszukiwarka | Przycisk otwierający osobne okno z pełnym drzewem i wyszukiwarką | ✅ Wybrana – łączy zalety obu podejść |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Dodać przycisk (analogiczny do pola Odnośnik do procesu) otwierający okno modalne z:
1. **Wyszukiwarką** na górze (dla użytkowników znających symbole/nazwy)
2. **Drzewem hierarchicznym** poniżej (dla użytkowników uczących się struktury)
   - Domyślnie zwinięte (aby nie ładować wszystkich 900+ pozycji)
   - Możliwość rozwijania gałęzi
   - Radio button na najniższym poziomie (wybór liścia)
3. **Kolumnami** z dodatkowymi danymi (symbol, nazwa, opis, kategoria archiwalna, elektroniczne/papierowe)

**Szczegóły techniczne:**
- Wzorowane na mechanizmie wyboru dla pola Odnośnik do procesu (okno modalne z filtrami)
- Drzewo domyślnie zwinięte – użytkownik rozwija tylko interesujące go gałęzie
- Wyszukiwarka nad drzewem – filtruje wyniki w drzewie

### Ograniczenia / Poza zakresem

- Mechanizm dedykowany dla JRWA (nie uniwersalny dla wszystkich źródeł drzewiastych – to przyszłościowy rozwój)

### Zadania / Dalsze kroki

- **Marek:** Zaimplementować okno modalne z drzewem JRWA + wyszukiwarką (wzorowane na polu Odnośnik do procesu)
- **Zespół:** Rozważyć podpowiadanie 5 ostatnio używanych kategorii JRWA (przyszły sprint)

---

## 5. JRWA - Dostęp do danych z pola Odnośnik do źródła zewnętrznego

**Komponent:** Silnik reguł (funkcje dostępu do danych)

### Kontekst i cel

Po wybraniu kategorii JRWA w polu Odnośnik do źródła zewnętrznego, dane są zapisywane w formacie JSON. Użytkownicy chcą mieć możliwość automatycznego uzupełniania innych pól formularza na podstawie wybranych danych (np. symbol, nazwa, kategoria archiwalna) bez konieczności ręcznego parsowania JSON.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Składnia `[NazwaPola.Źródło.Kolumna]` | Analogiczna do pola Odnośnik do procesu | 🔍 Do weryfikacji – wymaga sprawdzenia, czy działa dla źródeł zewnętrznych (GUST, TERYT, JRWA) |
| Parsowanie JSON ręcznie | Użycie funkcji `ParseJSON` w regułach | ✅ Działa obecnie (wzorowane na GUST) – ale jest mniej wygodne |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja

Rozszerzyć składnię `[NazwaPola.Źródło.Kolumna]` o obsługę źródeł zewnętrznych (GUST, TERYT, JRWA), aby umożliwić automatyczne uzupełnianie pól bez ręcznego parsowania JSON.

**Przykład:**
```
[KategoriaJRWA.Źródło.Symbol]  → "001"
[KategoriaJRWA.Źródło.Nazwa]   → "Rada nadzorcza"
```

**Szczegóły techniczne:**
- Obecnie działa dla pola Odnośnik do procesu
- Wymaga weryfikacji, czy walidator obsługuje tę składnię dla źródeł zewnętrznych
- Jeśli nie – dodać obsługę w walidatorze/silniku reguł

### Punkty otwarte

- Czy składnia `[NazwaPola.Źródło.Kolumna]` jest obsługiwana dla źródeł zewnętrznych (GUST, TERYT, JRWA)?
- Jeśli nie – czy walidator poprawnie interpretuje tę składnię?

### Zadania / Dalsze kroki

- **Marek:** Sprawdzić, czy składnia `[NazwaPola.Źródło.Kolumna]` działa dla źródeł zewnętrznych (JRWA, GUST, TERYT)
- **Marek:** Jeśli nie działa – dodać obsługę w walidatorze/silniku reguł (jedna linia kodu)

---

## 6. JRWA - Uniwersalizacja mechanizmu dla innych źródeł drzewiastych

**Komponent:** Edytor Formularza (pole Odnośnik do źródła zewnętrznego)

### Kontekst i cel

Mechanizm wyboru z drzewa hierarchicznego (okno modalne + wyszukiwarka) może być przydatny dla innych źródeł danych o strukturze drzewiastej (np. wybór działu, wybór kategorii). Obecnie JRWA ma dedykowaną tabelę i specyficzne kolumny, ale w przyszłości warto rozważyć uniwersalizację.

### Decyzja / Ustalenie

**Status:** ⏸️ Odroczona

Na razie mechanizm jest dedykowany dla JRWA (dedykowana tabela, konkretne kolumny: symbol, nazwa, opis, kategoria archiwalna, elektroniczne/papierowe).

W przyszłości rozważyć uniwersalizację:
- Mechanizm wyboru z drzewa jako osobny komponent
- Możliwość podpięcia różnych źródeł danych (nie tylko JRWA)
- Ustawienia: wskazanie kolumny z `parent`, kolumny do wyświetlania, etc.

**Przykład zastosowania:**
- Wybór działu (struktura organizacyjna)
- Wybór kategorii produktów
- Inne hierarchiczne słowniki

### Ograniczenia / Poza zakresem

- Obecnie JRWA ma dedykowaną implementację – uniwersalizacja to przyszłościowy rozwój
- Wymaga dodatkowych ustawień (wskazanie kolumny z parent, kolumny do wyświetlania)

---

## Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Status | Uwagi |
|-------|--------|-------|
| Repozytorium plików | 🔄 W testach | Testowanie przez Janusza i Kamila, feedback dla Marka |
| JRWA - pole Odnośnik | 🔄 W trakcie | Technicznie działa, teraz faza UX-owa |

---

## Cele na bieżący sprint

**Cel 1:** Oddanie do użytku repozytorium plików (zainstalowane u klienta)

**Cel 2:** Dokończenie JRWA – pole Odnośnik do źródła zewnętrznego (UX + funkcjonalności)

---

## Ustalenia organizacyjne

### Wyznaczanie celów sprintu

**Status:** 💡 Propozycja

Janusz i Przemek powinni wyznaczać cele sprintu dla zespołu, a zespół następnie organizuje się, rozpisuje zadania i realizuje te cele. Ma to zapobiec sytuacjom, gdy zespół wybiera cele, które później są kwestionowane przez management.

**Kontekst:**
- Roadmapa jest kluczowa – cele muszą być zgodne z roadmapą
- Typowa sytuacja: 2 cele na sprint (np. repozytorium + JRWA)
- Management (Janusz, Przemek) ma przegląd całości i może lepiej określić priorytety

**Szczegóły:**
- Janusz i Przemek wyznaczają cele
- Zespół organizuje się i rozpisuje zadania
- Realizacja zgodna z roadmapą
