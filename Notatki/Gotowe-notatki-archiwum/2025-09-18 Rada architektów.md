> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

# Rada Architektów – 2025-09-18

**Powiązane projekty:**
- `Moduly/Silnik-regul` – tematy 1, 3
- `Moduly/Edytor-procesow/Edytor-formularzy` – tematy 1, 2, 3
- `Moduly/Modul-raportowy` – temat 4
- `cross-cutting/Logowanie-do-amodit` – temat 5
- `Organizacja-DEV/Automatyzacja-dokumentacji-AI` – tematy 6, 8
- `Moduly/Modul-raportowy/Gantt` – temat 7

---

## 1. Funkcja Create Callout do komunikatów w regułach

**Projekt:** `moduly/Silnik-regul`, `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

Zespół wdrożeniowy potrzebuje funkcji do generowania komunikatów (callout) w regułach, zamiast ręcznego tworzenia HTML-a. Obecnie muszą tworzyć statyczne pola z ręczną rzeźbą HTML-a, co jest nieefektywne. Potrzebny jest zestaw funkcji do tego celu, podobny do istniejących funkcji jak `setFieldAliasDanger`.

### Zidentyfikowane Ryzyka

- Brak standaryzacji komunikatów może prowadzić do niespójnego wyglądu w różnych miejscach systemu
- Ręczne tworzenie HTML-a jest podatne na błędy i trudne w utrzymaniu

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Funkcja `Create Callout` | Funkcja zwracająca HTML callout z parametrami tekst i styl | ✅ Wybrana – zgodna z propozycją zespołu wdrożeniowego |
| Funkcja typu `setStatic` lub podobna | Analogiczna do `setFieldAliasDanger` | ❌ Odrzucona – zespół zasugerował `Create Callout` |
| Funkcja w ustawieniach pola static | Możliwość ustawienia pola static jako callout bezpośrednio w edytorze | ⏸️ Odroczona – trzecie zagadnienie, na rozwój |

### Decyzja

**Status:** ✅ Zatwierdzone

Funkcja `Create Callout` zostanie dodana do silnika reguł. Funkcja zwraca HTML callout, który można przypisać do pola typu static tekst. Funkcja przyjmuje 2 parametry: tekst komunikatu i styl (info, danger, warning). Styl jest narzucany jako szablonowy przez system, aby zapewnić spójność wyglądu.

**Szczegóły techniczne:**
- Funkcja: `Create Callout(tekst, styl)`
- Zwraca: HTML callout (sprawdzalny)
- Można przypisać do: pola typu static tekst
- Działa w: regułach automatycznych i ręcznych
- Przykład użycia: `infoTest = Create Callout("komunikat", "info")`

### Zadania

- **[Damian Kaminski]:** Stworzenie funkcji `Create Callout` do komunikatów w regułach → termin: następny sprint
- **[Łukasz Bott]:** Aktualizacja opisu zadania z przykładem użycia funkcji `Create Callout`
- **[Ania / Kamil]:** Implementacja wyświetlania komunikatów na stronie (przejęcie od Ani przez Mariusza, następnie przez Kamila)

### Punkty otwarte

- Czy komunikaty będą mogły być pobierane z bazy danych, czy tylko generowane dynamicznie w regułach?

---

## 2. Pole static na szerokość kolumny

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

Obecnie pole static jest zawsze wyświetlane na całą szerokość formularza. W kontekście komunikatów callout z poprzedniego tematu, potrzebna jest możliwość wyświetlania pola static w ramach jednej kolumny, podobnie jak tabelki mogą być wyświetlane w jednej kolumnie. To ułatwiłoby wdrożeniowo lepsze układanie komunikatów w formularzach.

### Zidentyfikowane Ryzyka

- Brak tej funkcjonalności może prowadzić do błędów wyrównywania, które zespół chciał usuwać
- Komunikaty callout mogą wyglądać jak przyciski, jeśli nie będą na szerokość kolumny

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Opcja wyświetlania pola static w jednej kolumnie | Dodanie właściwości pola static do wyświetlania w jednej kolumnie | ✅ Wybrana – bardzo przydatne wdrożeniowo |
| Tylko na szerokość pola static (jak obecnie) | Zachowanie obecnego zachowania | ❌ Odrzucona – nie rozwiązuje problemu wyrównywania |

### Decyzja

**Status:** ✅ Zatwierdzone

Pole static będzie mogło być wyświetlane w jednej kolumnie, podobnie jak tabelki. To będzie opcja konfigurowalna dla pola static. Najpierw zostanie zaimplementowane wyświetlanie na szerokość pola static (jak obecnie działa żółty komunikat), a następnie dodana zostanie opcja wyświetlania w jednej kolumnie.

**Szczegóły techniczne:**
- Właściwość pola static: możliwość wyboru szerokości (cała szerokość formularza / jedna kolumna)
- Paddingi muszą być zachowane dla poprawnego wyglądu

### Zadania

- **[Piotr Buczkowski]:** Zaprojektowanie i implementacja opcji wyświetlania pola static w jednej kolumnie → termin: po implementacji funkcji Create Callout

---

## 3. Właściwość pola static jako callout w ustawieniach pola

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

W nowym edytorze formularza dla pola static nie można wpisać ładnego tekstu bezpośrednio w edytorze. Obecnie trzeba pisać całą rzeźbę HTML-a (`<div class="colour">` itd.), zamiast po prostu wpisać tekst i wybrać styl callout. To utrudnia tworzenie statycznych komunikatów/instrukcji w formularzach.

### Zidentyfikowane Ryzyka

- Brak tej funkcjonalności utrudnia szybkie tworzenie komunikatów/instrukcji w formularzach
- Wymusza użycie reguł nawet dla prostych, statycznych komunikatów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Właściwość "display jako callout" dla pola static | Opcja w ustawieniach pola static do wyboru stylu callout (info, danger, warning) | ✅ Wybrana – pozwala na szybkie tworzenie statycznych komunikatów |
| Tylko dynamicznie przez reguły | Wszystkie callouty przez funkcję Create Callout w regułach | ❌ Odrzucona – nie rozwiązuje problemu statycznych komunikatów/instrukcji |

### Decyzja

**Status:** 💡 Propozycja

Możliwość dodania do pola static właściwości "display jako callout", gdzie można wpisać tekst i wybrać styl (info, danger, warning). To pozwoli na szybkie tworzenie statycznych komunikatów/instrukcji bez konieczności użycia reguł. Można też nadal używać reguł do dynamicznego generowania komunikatów z różnymi stylami.

**Szczegóły techniczne:**
- Właściwość pola static: "Display jako callout" (checkbox lub dropdown)
- Opcje stylu: info, danger, warning (możliwe inne style)
- Tekst wpisywany bezpośrednio w edytorze pola

### Zadania

- **[Piotr Buczkowski]:** Zaprojektowanie i implementacja właściwości "display jako callout" dla pola static → termin: na rozwój (trzecie zagadnienie)

---

## 4. Kontrola dostępu do reguł wywoływanych z poziomu raportów

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

Temat dotyczący kontroli dostępu do reguł wywoływanych z poziomu raportów. Został już wcześniej omawiany, ale nie został jeszcze zaopiekowany. Obecnie reguły są dostępne w raportach, ale kontrola dostępu jest weryfikowana na poziomie wywołania reguły.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zostawić jak jest | Kontrola dostępu na poziomie wywołania reguły | ✅ Wybrana – nie jest to luka bezpieczeństwa, obecne rozwiązanie jest wystarczające |
| Usprawnienie wizualne | Checkbox domyślnie niezaznaczony dla nowych reguł, zaznaczony dla starych (wsteczna kompatybilność) | ⏸️ Odroczona – do elementu modyfikacji całego wyglądu reguł |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostaje jak jest. Obecne rozwiązanie jest wystarczające – kontrola dostępu jest weryfikowana na poziomie wywołania reguły, więc nawet jeśli ktoś wybierze regułę, która nie powinna być wykonana, i tak się ona nie wykona w kontekście użytkownika, który z niej skorzysta. Usprawnienie wizualne (checkbox domyślnie niezaznaczony dla nowych reguł) zostanie zrealizowane przy okazji modyfikacji całego wyglądu reguł.

### Zadania

- **[Damian Kaminski]:** Przeniesienie tematu do komentarza zadania (już omówione, nie krytyczne)

---

## 5. Wsparcie dla Google w logowaniu (ACS - Application Apollo)

**Projekt:** `integracje/SharePoint-OAuth`

### Kontekst i Problem

Obecnie system obsługuje logowanie przez Azure (Application Apollo). Microsoft kończy wsparcie dla Azure AD w kwietniu 2026, więc potrzebne jest dodanie wsparcia dla Google i innych providerów OAuth. Obecnie konfiguracja jest w ustawieniach systemowych jako "Aplikacja Azure", ale potrzebny jest interfejs do zarządzania konfiguracją różnych providerów (Google, SharePoint, inne).

### Zidentyfikowane Ryzyka

- Termin 2 kwietnia 2026 jest blisko – nie można odkładać implementacji na pierwszy kwartał 2026
- Brak wsparcia dla Google może uniemożliwić logowanie po zakończeniu wsparcia dla Azure AD

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zrobić dobrze | Stworzenie interfejsu do zarządzania konfiguracją różnych providerów OAuth w ustawieniach systemowych | ✅ Wybrana – długoterminowe rozwiązanie |
| Zrobić na szybko | Tymczasowe rozwiązanie jak dotychczas | ❌ Odrzucona – zdecydowanie zrobić dobrze |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostanie stworzony interfejs do zarządzania konfiguracją różnych providerów OAuth (Google, SharePoint, inne) w ustawieniach systemowych. Każdy provider będzie miał swoją konfigurację (podobnie jak obecnie "Aplikacja Azure"). Implementacja powinna być zaplanowana już na najbliższe sprinty (nie za tydzień, ale już w takim tempie), aby mieć czas na testy przed terminem 2 kwietnia 2026.

**Szczegóły techniczne:**
- Interfejs w ustawieniach systemowych do zarządzania konfiguracją providerów OAuth
- Każdy provider: Google, SharePoint, inne – osobna konfiguracja
- Dodanie nowego parametru i obsłużenie go przy logowaniu
- SharePoint będzie prosty do dodania

### Zadania

- **[Piotr Buczkowski]:** Zaprojektowanie i implementacja interfejsu do zarządzania konfiguracją providerów OAuth → termin: najbliższe sprinty (nie za tydzień, ale już w takim tempie)

---

## 6. Azure DevOps AI Generator – problem z konfiguracją

**Projekt:** Nowy temat / do sklasyfikowania

### Kontekst i Problem

Azure DevOps AI Generator (Feature 21841) został skonfigurowany, ale nie działa poprawnie. Po wejściu w zakładkę AI generator wyświetlają się childy podpięte pod Feature, ale funkcja "regenerator work items" się wywala i nie można zdiagnozować problemu. To narzędzie Microsoftu do pomocy w rozbijaniu Feature na zadania (PBI) i poprawianiu opisu Feature.

### Zidentyfikowane Ryzyka

- Brak działającego narzędzia utrudnia efektywne planowanie i opisywanie zadań w backlogu

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Problem wymaga diagnozy i naprawy konfiguracji. Narzędzie powinno działać poprawnie, ponieważ jest stworzone przez Microsoft do pracy z Azure backlog. Prawdopodobnie problem jest w konfiguracji lub w sposobie, w jaki został skonfigurowany.

### Zadania

- **[Janusz Bossak / Michał / Łukasz Poskrobko]:** Diagnoza i naprawa problemu z Azure DevOps AI Generator → termin: do ustalenia (wymaga czasu na spokojne podejście)

### Punkty otwarte

- Jaka jest przyczyna wywalania się funkcji "regenerator work items"?
- Czy problem jest w konfiguracji, czy w samym narzędziu?

---

## 7. Gantt – temat o grupowaniu

**Projekt:** Nowy temat / do sklasyfikowania

### Kontekst i Problem

Temat dotyczący Gantta został poruszony, ale nie jest konfliktem. Marek świetnie opanował Gantta i powinien takie rzeczy robić.

### Decyzja

**Status:** ⏸️ Odroczone

Temat nie jest krytyczny i został odroczony. Nie zajmujemy się tym na razie, mówimy o grupowaniu w pierwszym rzędzie.

---

## 8. Podsumowanie notatek z Rad Architektów

**Projekt:** `cross-cutting/Automatyzacja-dokumentacji-AI`

### Kontekst i Problem

Janusz Bossak wygenerował podsumowanie z poprzedniej Rady Architektów na podstawie transkrypcji. Podsumowanie zawiera strukturę: Edytor formularza, problem z obsługą pól pustych, ryzyka, proponowane rozwiązania, decyzje, zadania, bezpieczeństwo, dane poufne w nazwach plików. To podsumowanie jest dużo lepsze niż standardowe podsumowanie Microsoft Copilot, które jest zbyt uproszczone.

### Decyzja

**Status:** ✅ Zatwierdzone

Będą generowane takie podsumowania po każdej Radzie Architektów. Ważne jest, aby na Radzie mówić na głos o zagadnieniach, nad którymi pracujemy, ponieważ AI widzi transkrypcję i będzie się koncentrował na tych zagadnieniach.

### Zadania

- **[Janusz Bossak]:** Generowanie podsumowań po każdej Radzie Architektów w strukturze: kontekst, ryzyka, proponowane rozwiązania, decyzje, zadania

