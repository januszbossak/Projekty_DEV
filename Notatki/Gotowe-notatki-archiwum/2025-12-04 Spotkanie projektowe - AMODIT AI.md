# Spotkanie projektowe – 2025-12-04 – AMODIT AI

**Data:** 2025-12-04
**Typ:** Spotkanie projektowe
**Temat główny:** Funkcje AI (Generowanie dokumentacji procesu, OCR dla WASKO)

---

## 1. Generowanie dokumentacji procesu (AMODIT AI / Copilot)

**Komponent:** Copilot / AI

### Kontekst i cel

Mateusz Kisiel rozwijał funkcję automatycznego generowania dokumentacji procesów. Funkcja ma pomóc konsultantom wdrożeniowym w tworzeniu dokumentacji procesów dla klientów. Według szacunków może zaoszczędzić około 60 dni pracy działu wdrożeń rocznie. Funkcja generuje opis procesu na podstawie jego konfiguracji: nazwy, pola formularza, diagram przebiegu etapów, sposób powstawania sprawy (z maila, z pliku), reguły biznesowe dla każdego etapu.

Funkcja działa w trybie czatu (AMODIT Copilot) - użytkownik może zapytać o generowanie dokumentacji dla bieżącego procesu, na którym się znajduje (Copilot ma świadomość URL, np. procedury numer 821).

### Szczegóły techniczne implementacji

**Elementy generowanej dokumentacji:**
- Nazwa systemowa i nazwa wyświetlana procesu
- Diagram przebiegu etapów (generowany w backendzie - obrazek)
- Sposób powstawania sprawy (mail, plik, inne)
- Dla każdego etapu: opis etapu, lista reguł biznesowych
- Restrykcje pól na poszczególnych etapach (jeśli są różne - osobne tabelki)

**Kwestie otwarte dotyczące diagramu:**
- Diagram generowany w backendzie ma problemy z proporcjami (rozjechane)
- Frontend generuje obrazki przez przeglądarkę, backend nie ma do tego dostępu
- Rozważano mermaid (markdown), ale Word tego nie wyświetli
- Przemysław Sołdacki zasugerował zachowanie proporcji obrazka (żeby nie był zniekształcony)

**Struktura dokumentacji:**
- Najpierw wymienione są reguły biznesowe (z numeracją globalną, niezależnie od etapu)
- Potem opis etapu z odwołaniami do reguł
- Damian Kamiński zauważył, że kolejność mogłaby być zamieniona (opis przed regułami), ale ostatecznie uznano, że obecna kolejność ma sens logiczny

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Obrazek z frontendu | Wziąć obrazek diagramu generowany przez przeglądarkę | ❌ Odrzucona – backend nie ma dostępu do obrazków z frontendu |
| Mermaid (markdown) | Zapis diagramu w formacie mermaid | ❌ Odrzucona – Word nie wyświetla mermaid |
| Poprawienie proporcji w backendzie | Zachowanie proporcji przy generowaniu obrazka | ✅ Wybrana – Mateusz Kisiel zmienił proporcje |
| Diagram przedstawia... | Tekst zastępczy bez obrazka, który użytkownik może uzupełnić | 💡 Propozycja Damiana – uznano za możliwy fallback (minuta pracy) |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

**Zakres MVP - Proof of Concept:**
- Funkcja generowania dokumentacji procesu będzie wydana jako PoC w grudniowej wersji (wydanie na początku stycznia 2026)
- Konsultanci wdrożeniowi będą mogli testować funkcję i zgłaszać feedback w styczniu
- Obrazek diagramu zostanie zachowany z poprawionymi proporcjami

**Wersjonowanie:**
- Funkcja będzie oznaczona w PBI jako "AMODIT AI" (w nazwie zgłoszenia)
- Release Version: grudniowa (suggest version)
- Zmiany traktowane jak każde inne zgłoszenie (Waiting for Release → automatyczne przypisanie wersji)

### Feedback / Uwagi uczestników

**💭 Pomysł Przemka (Przemysław Sołdacki):**
- Dodać zakładkę "Dokumentacja" w lewej zakładce procesu (zamiast tylko czatu)
- Tam możliwość generowania dokumentacji + wgrywania własnych plików dokumentacji
- Fajnie żeby dokumentacja była załączana do szablonu procesu i przenosiła się razem z nim między środowiskami (wgrywanie ze środowiska na środowisko)
- Gadał o tym z Mateuszem Kołakowskim

**Status tego pomysłu:** 💡 Propozycja - nie ma potwierdzenia, że zostanie zaimplementowane w MVP

### Zadania / Dalsze kroki

- **Mateusz Kisiel:** Wysłać przykładową wygenerowaną dokumentację do konsultantów (Mateusz Kołakowski, Daniel Reszka) na feedback
- **Mateusz Kisiel:** Wybrać dobry proces do pokazania (z różnymi restrykcjami pól na etapach)
- **Damian Kamiński:** Wymusić na konsultantach, żeby zaczynali robić specyfikacje od tego narzędzia i zgłaszali, co musieli dopisać

### Punkty otwarte

- Jak konsultanci dostaną to na produkcji? Kiedy będą mogli u klienta odpalać? (grudniowa wersja → wydanie na początku stycznia)
- Czy tworzyć osobne środowisko typu "dokumentacja AI" (robocze)?
- Jak oznaczyć funkcje AI w changelogu? (automatyczny changelog z PBI)

---

## 2. OCR dla WASKO - integracja z Google Gemini

**Komponent:** Copilot / AI (OCR)

### Kontekst i cel

WASKO to klient generujący około 80 000 zł przychodów rocznie. Klient jest niezadowolony z jakości OCR (Azure Document Intelligence) i rozważa odejście do konkurencji. Około miesiąc temu (25 października) odbyło się spotkanie, na którym ustalono, że WASKO może zostać, jeśli zostanie wdrożone OCR na Google Cloud (Gemini).

WASKO jest "klientem googlowym" - wszystko ma na Google. Klient zrobił testy z Google Gemini i stwierdził, że działa lepiej niż Azure. Według klienta: faktury, z których obecny OCR nie rozszyfrował żadnej poprawnie, Gemini rozczytał 90% poprawnie. Klient dostarczył gotowy prompt do testów. Google jest również gotowe do wsparcia technicznego (odbyło się spotkanie z przedstawicielami Google).

### Zidentyfikowane ryzyka

- **Utrata klienta WASKO** (około 80k zł ARR) - jeśli nie zostanie wdrożone Google OCR
- **Opóźnienie wdrożenia** - minął już ponad miesiąc od spotkania (25.10), klient może stracić cierpliwość
- **Wyższe koszty Google** - wysyłanie całego PDF-a do LLM może być droższe niż Azure Document Intelligence
- **Niedziałające rozwiązanie** - może się okazać, że Google dalej źle odczytuje (wtedy klient odejdzie z zarzutem "nie umiecie tego robić")

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Azure Document Intelligence (obecny) | Obecne rozwiązanie na Azure | ❌ Odrzucona – klient niezadowolony, nie działa dla jego faktur |
| Google Document AI | Dedykowane narzędzie Google do OCR | ⏸️ Odroczona – Gemini jest bardziej uniwersalny i tańszy |
| Google Gemini 1.5 / Flash | Model LLM Google z wysyłaniem całego PDF-a + prompt | ✅ Wybrana – według klienta działa lepiej, Gemini ma dostęp do struktury dokumentu i układu graficznego |
| Eksperyment z GPT (OpenAI) | Przed integracją z Google - test z modelem OpenAI | ❌ Odrzucona – Przemek chce najpierw Google, żeby nie tracić czasu |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone - priorytet najwyższy

**Zakres wdrożenia:**

1. **Minimalna integracja z Google Gemini:**
   - Osobna integracja w mikroserwisie OCR (wybór modelu: OCR google'owy)
   - Wysyłanie całego PDF-a do Gemini (zamiast tylko wyników z Document Intelligence)
   - Użycie prompta dostarczonego przez klienta WASKO
   - Zwracanie surowych wyników w postaci tekstu (bez mapowania na pola AMODIT)

2. **Cel etapu 1:**
   - Pokazać klientowi wynik: "działa na Google Gemini z waszym promptem"
   - Porównać faktury, które według klienta źle się odczytują: Azure vs Google
   - Sprawdzić czy Google rzeczywiście odczytuje lepiej

3. **Dalsze prace (jeśli test się uda):**
   - Mapowanie wyników na pola AMODIT (schemat jak obecnie)
   - Wdrożenie heurystyk (jak są obecnie w Azure)
   - Przerobienie prompta klienta na format zgodny z AMODIT (ręcznie lub przez AI)

**Szczegóły techniczne:**
- Model: Google Gemini 1.5 lub Flash
- Prompt: dostarczony przez WASKO (Mateusz Kisiel ma)
- Integracja: przez proxy w mikroserwisie (jak obecnie Azure)
- Konto Google: Mateusz utworzy nowe konto i będzie korzystał z triala

**Priorytetyzacja:**
- **WASKO OCR** - najwyższy priorytet (ryzyko utraty klienta)
- **Generowanie dokumentacji** - dalsze dopracowanie (już jest PoC)
- **MCP** - później (Rossmann i inni pytają o to)

**Koszt:**
- Klient bierze koszty na siebie (klient stwierdził, że nie będą wyższe niż Azure)
- Wysyłanie całego PDF-a może być droższe, ale Gemini ma dostęp do pełnej struktury dokumentu

### Ograniczenia / Poza zakresem

**W pierwszej fazie (PoC):**
- Brak mapowania na pola AMODIT (surowe dane z prompta)
- Brak heurystyk
- Brak produkcyjnej integracji (najpierw środowisko testowe)

### Zadania / Dalsze kroki

- **Mateusz Kisiel:** Zająć się integracją z Google Gemini dzisiaj (4.12) - priorytet
- **Mateusz Kisiel:** Utworzyć konto Google (trial) do testów
- **Przemysław Sołdacki:** W razie potrzeby zadzwonić do Google (opiekun) i założyć konto firmowe
- **Przemysław Sołdacki:** Po sukcesie podpisać umowę partnerską z Google
- **Janusz Bossak:** W razie niejasności Mateusz może pisać do osoby z WASKO odpowiedzialnej za rozwój (mocno technologiczny człowiek)

**Termin:** Jak najszybciej (minął już miesiąc od spotkania z klientem)

### Punkty otwarte

- Czy Gemini rzeczywiście działa lepiej? (według klienta tak, ale trzeba zweryfikować na produkcyjnych fakturach)
- Jaki będzie finalny koszt dla klientów? (klient stwierdzi, czy akceptuje)
- Czy przejdziemy na Google z Azure globalnie, jeśli się okaże, że jest dużo lepszy?

---

## 3. Priorytetyzacja zadań AI

**Komponent:** Organizacja pracy

### Kontekst i cel

Podczas spotkania pojawiła się kwestia priorytetów w ramach AMODIT AI. Mateusz Kisiel wspomniał, że obecnie pracuje nad filtrami użytkownika i indeksowaniem dla modułu raportowego. Przemysław Sołdacki przerwał i zapytał o WASKO, które jest na roadmapie na kwiecień. Powstała dyskusja o tym, dlaczego robione są filtry do modułu raportowego (z powodu problemów wydajnościowych bazy danych), a nie WASKO, gdzie ryzykujemy utratę klienta (kilkadziesiąt tysięcy zł rocznie).

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

**Kolejność priorytetów:**
1. **WASKO OCR (Google Gemini)** - najwyższy priorytet (ryzyko utraty klienta)
2. **Generowanie dokumentacji** - dopracowanie funkcji (feedback od konsultantów)
3. **MCP** - dalsze prace (Rossmann i inni pytają)

**Filtry modułu raportowego:**
- Odłożone (Janusz: "te indeksowania i tak nie mamy już od dłuższego czasu")
- Przemek: "Zamykamy rok, i się zastanawiamy co dalej"

### Punkty otwarte

- Kiedy wrócą filtry modułu raportowego? (po zamknięciu roku)

---

## 4. Edytor procesów

**Komponent:** Edytor Procesów

### Kontekst i cel

Krótka wzmianka o edytorze procesów na końcu spotkania. Damian Kamiński wspomniał, że "Przemka nie było ostatnio 2 dni, wcześniej poprawiał błędy związane z raportami". Janusz Bossak zaproponował zrobienie krótkiego statusu (5 minut).

### Decyzja / Ustalenie

**Status:** ⏸️ Odroczone - osobne spotkanie

Uczestnicy przełączyli się na osobne spotkanie, żeby nagranie było osobno.

