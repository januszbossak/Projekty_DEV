# Project Canvas: Silnik reguł

**Status:** 🟢 W realizacji (ciągły rozwój)
**Ostatnia aktualizacja:** 2025-09-08
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** [historyczna]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | Piotr Buczkowski | Architektura, rozwój |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Złożone procesy biznesowe często wymagają niestandardowej logiki, której nie da się zamodelować za pomocą standardowych akcji i konfiguracji w AMODIT. Konsultanci i wdrożeniowcy potrzebują potężnego, elastycznego narzędzia do automatyzacji skomplikowanych operacji, walidacji i integracji bez konieczności modyfikacji kodu źródłowego aplikacji.

### Cel biznesowy
Umożliwienie modelowania i automatyzacji nawet najbardziej złożonych i nietypowych scenariuszy biznesowych bezpośrednio w procesach AMODIT. Silnik reguł jest kluczowym narzędziem, które daje AMODIT przewagę konkurencyjną, pozwalając na głęboką personalizację i adaptację do unikalnych potrzeb klientów.

### Cel techniczny
Ciągły rozwój i optymalizacja języka skryptowego silnika reguł. Wprowadzanie nowych funkcji, pętli i konstrukcji językowych, które rozszerzają jego możliwości, a jednocześnie dbanie o wydajność i bezpieczeństwo wykonywanego kodu.

### Metryka sukcesu
- 95% niestandardowych wymagań logiki biznesowej klientów jest możliwych do zrealizowania za pomocą silnika reguł.
- Nowe funkcje silnika reguł są regularnie dodawane w odpowiedzi na zgłaszane potrzeby z wdrożeń.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-08-25]] | Wprowadzenie nowej funkcji `foreach attachment` do iterowania po załącznikach swobodnie dodanych do sprawy. | Upraszcza to pracę konsultantów, którzy do tej pory musieli tworzyć obejścia (np. tabele plików), aby operować na takich załącznikach. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-09-08]] | W `ForEachAttachment` parametr `Value` (zawartość pliku) jest pobierany dopiero na żądanie (`lazy loading`). | Jest to krytyczna optymalizacja. Pobieranie zawartości wszystkich plików w pętli mogłoby drastycznie obniżyć wydajność, zwłaszcza przy dużych załącznikach. | - |
| ADR-003 | 💡 Propozycja | [[2025-09-08]] | Należy rozważyć w przyszłości umożliwienie odwołania się do całego obiektu załącznika przez `this`, a nie tylko do jego właściwości (`this.Id`, `this.Name`). | Uprościłoby to składnię w niektórych przypadkach (np. `AddToList(this)`), ale wymaga starannej implementacji, aby nie stracić korzyści z `lazy-loading`. | - |

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-08-25]] | Zaplanowano reset dokumentacji do formatu v2 Project Canvas. | [[2025-08-25 Sprint review]] |
| [[2025-09-08]] | Demo nowej funkcji `ForEachAttachment`. Zebrano feedback dotyczący optymalizacji (`lazy loading` dla `Value`) i potrzeby uzupełnienia dokumentacji o przykłady użycia `this.Id`. | [[2025-09-08 Sprint review]] |
