
**Data:** 2025-12-22  
**Dotyczy:** Zapytania AI Compliance Officera Rossmann w sprawie platformy AMODIT  


> **Zastrzeżenie:**  
> Niniejsze odpowiedzi mają charakter informacyjny i opisują aktualny model odpowiedzialności oraz interpretację wymogów AI Act w odniesieniu do funkcjonalności systemu AMODIT. Ostateczny zakres obowiązków stron może zostać doprecyzowany w umowie lub aneksie.

---

## Pytanie 1

**Czy Astrafox jednoznacznie deklaruje, że jest „providerem systemu AI" w rozumieniu AI Act?**

**Nie.**

Astrafox nie deklaruje, że platforma AMODIT jako całość stanowi „system AI" w rozumieniu art. 3 AI Act ani że Astrafox pełni rolę Provider systemu AI w tym znaczeniu.

**Charakter platformy AMODIT:**

Platforma AMODIT jest systemem klasy **BPM / DMS / low-code**, który umożliwia klientom korzystanie z funkcjonalności opartych o zewnętrzne modele AI (GPAI), dostarczane przez wyspecjalizowanych dostawców technologicznych (np. Microsoft Azure OpenAI).

Astrafox:
- nie tworzy modeli bazowych,
- nie trenuje modeli,
- nie wprowadza na rynek własnych modeli AI,
- nie udostępnia samodzielnego systemu AI niezależnie od platformy AMODIT.

**Stanowisko publiczne Astrafox:**

Zgodnie z oficjalnym dokumentem [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„Platforma AMODIT jako system BPM/DMS/Low-code nie jest samodzielnym „systemem sztucznej inteligencji" w rozumieniu art. 3 AI Act. AMODIT nie trenuje modeli AI, nie tworzy algorytmów predykcyjnych, nie podejmuje decyzji bez inicjacji użytkownika, nie ocenia ani nie klasyfikuje użytkowników, nie jest usługą wysokiego ryzyka."*

AMODIT umożliwia użytkownikom wykorzystanie zewnętrznych modeli AI (np. AMODIT Copilot, integracje z LLM, wywołania API AI w procesach), ale w takich sytuacjach:

→ **klient, a nie AMODIT, podlega obowiązkom AI Act jako „deployer"**  
→ i odpowiada za sposób wykorzystania AI w swoich procesach.

---

## Pytanie 2

**Czy Rossmann jest wyłącznie użytkownikiem / deployerem systemu AI?**

W kontekście AI Act, **Rossmann występuje w roli Deployer (Wdrażającego)**, przy czym zakres obowiązków zależy od sposobu wykorzystania funkcjonalności AI w ramach platformy AMODIT.

Odpowiedź wymaga rozróżnienia w zależności od wykorzystywanej funkcjonalności AI:

### A) Moduły zarządzane przez Astrafox (AMODIT Copilot, AMODIT AI OCR)

W przypadku tych modułów Rossmann występuje w roli **Wdrażającego (Deployer)**. Astrafox dostarcza standardowe funkcjonalności platformowe, które:
- integrują modele AI dostawców zewnętrznych,
- nie podejmują autonomicznych decyzji,
- mają charakter wspierający użytkownika (assistive AI).

**Rossmann jako Deployer decyduje:**
- czy i w jakich procesach biznesowych te funkcjonalności są wykorzystywane,
- jakie dane są do nich przekazywane,
- jakie skutki biznesowe wywołują ich użycia,
- kto w organizacji ma dostęp do funkcji AI (kontrola uprawnień).

Astrafox w całości projektuje i kontroluje architekturę promptów, logikę przetwarzania oraz sposób wykorzystania modeli w tych modułach. Rossmann korzysta z gotowej funkcjonalności bez możliwości modyfikacji warstwy AI.

### B) Funkcje AI w silniku reguł

W przypadku funkcji bezpośrednio wykorzystujących AI w silniku reguł sytuacja jest bardziej złożona i wymaga szczególnej uwagi.

**Funkcje AI w silniku reguł obejmują:**
- `AskAI` – bezpośrednie wywołanie modeli LLM z promptem definiowanym przez użytkownika
- `KnowledgeBaseSearch` – semantic search (wyszukiwanie semantyczne z wykorzystaniem embeddingów AI)
- `KnowledgeBaseDocumentUpsert` – indeksowanie dokumentów z wykorzystaniem embeddingów AI

**Charakterystyka tych funkcji:**

- **Twórca procesu** (np. zespół Rossmann) samodzielnie konstruuje prompt o dowolnej treści
- **Wybór modelu** – Rossmann wybiera model z listy udostępnionej przez Astrafox
- **Dane wejściowe** – to twórca procesu decyduje, jakie dane trafiają do promptu (w tym potencjalnie dane osobowe, dane objęte tajemnicą przedsiębiorstwa)
- **Rola Astrafox** – przekazujemy prompt *as is* do modelu LLM (np. Azure OpenAI) bez analizy ani ingerencji w jego treść

W kontekście tych funkcji AI Rossmann bierze na siebie większą odpowiedzialność za:
- Treść konstruowanych promptów (w przypadku `AskAI`)
- Rodzaj danych przekazywanych do modelu AI (zarówno do LLM, jak i do procesu tworzenia embeddingów)
- Zgodność z wewnętrznymi politykami ochrony danych
- Klasyfikację ryzyka konkretnego przypadku użycia

**Podsumowanie:** Rossmann jest Deployerem w przypadku gotowych modułów (Copilot, AI OCR). W przypadku funkcji AI w silniku reguł (`AskAI`, `KnowledgeBaseSearch`, `KnowledgeBaseDocumentUpsert`) rola Rossmann zbliża się do podmiotu definiującego konkretny przypadek użycia (use case) systemu AI, co może generować dodatkowe obowiązki po stronie Rossmann w kontekście AI Act.

**Odpowiedzialność za zgodność danego use case z AI Act (w tym klasyfikację ryzyka) spoczywa na Rossmann jako deployerze.**

---

## Pytanie 3

**Czy w dokumentacji i umowie system jest oferowany pod marką AMODIT?**

**Tak.**

Funkcjonalności AI są integralną częścią platformy **AMODIT** i są oferowane pod tą marką (np. moduły AMODIT Copilot, AMODIT AI OCR). W dokumentacji produktowej i materiałach umownych występuje nazwa AMODIT jako główna marka produktu. 

Astrafox jest producentem i właścicielem marki AMODIT.

---

## Pytanie 4

**Kto odpowiada za klasyfikację ryzyka systemu AI?**

Odpowiedzialność za klasyfikację ryzyka zależy od wykorzystywanej funkcjonalności oraz konkretnego przypadku użycia.

Zgodnie z AI Act, **klasyfikacja ryzyka zależy od konkretnego przypadku użycia (use case)**, a nie od samej technologii jako takiej.

### A) Moduły zarządzane przez Astrafox (Copilot, AI OCR)

Astrafox, jako dostawca funkcjonalności, dokonuje wstępnej oceny klasyfikacji ryzyka projektowanych funkcjonalności AI, przy założeniu standardowych i przewidywalnych scenariuszy użycia. 

Zgodnie z naszą oceną, standardowe zastosowania tych modułów:
- automatyzacja workflow,
- wsparcie analizy dokumentów,
- asystent konwersacyjny,

**nie kwalifikują systemu jako systemu wysokiego ryzyka** w rozumieniu Załącznika III do AI Act.

**Zastrzeżenie:** Ostateczna klasyfikacja ryzyka może ulec zmianie w zależności od konkretnego sposobu wykorzystania systemu przez klienta.

### B) Funkcje AI w silniku reguł

W przypadku funkcji AI w silniku reguł (`AskAI`, `KnowledgeBaseSearch`, `KnowledgeBaseDocumentUpsert`) to **Rossmann** jako twórca procesu decyduje o sposobie wykorzystania AI i ponosi odpowiedzialność za klasyfikację ryzyka konkretnego przypadku użycia (use case).

**Przykład praktyczny:** 

Jeżeli Rossmann zdecyduje się użyć `AskAI` do wstępnej analizy CV kandydatów, może to wchodzić w obszar **zatrudnienia** (Załącznik III, punkt 4 AI Act). W takim przypadku:
- Rossmann odpowiada za ocenę, czy dany use case wymaga traktowania jako High-Risk
- Rossmann może zastosować środki minimalizujące ryzyko, np. **anonimizację danych** (imię, nazwisko, telefon) przed wysłaniem do modelu AI.
- Alternatywnie, Rossmann może dostarczać do systemu już zanonimizowane dokumenty

**Rekomendacja:** Jeżeli Rossmann zamierza wykorzystać funkcje AI w silniku reguł w obszarach szczególnie wrażliwych (zatrudnienie, ocena zdolności kredytowej, dostęp do usług), rekomendujemy wspólną analizę przypadku użycia.


---

## Pytanie 5

**Kto odpowiada za zgodność z art. 9–15 AI Act (risk management, data governance)?**

Odpowiedzialność za zgodność z art. 9–15 AI Act jest **rozłożona pomiędzy strony** w zależności od warstwy systemu i charakteru obowiązków.

### A) Astrafox (jako dostawca funkcjonalności AI) realizuje swoje obowiązki w szczególności w zakresie:

**Elementy systemu zarządzania ryzykiem (art. 9)** odnoszące się do warstwy aplikacyjnej AI:
- Moduły Copilot, AI OCR oraz elementy integracyjne funkcji AskAI po stronie platformy AMODIT
- Identyfikacja i analiza znanych i przewidywalnych ryzyk związanych z funkcjonalnościami AI
- Projektowanie z uwzględnieniem minimalizacji ryzyk

**Dokumentacja techniczna (art. 11):**
- Opis działania funkcji AI
- Ograniczenia systemowe (np. zjawisko halucynacji charakterystyczne dla modeli LLM)
- Instrukcje użytkowania i bezpiecznego wykorzystania

**Przejrzystość i informowanie użytkowników (art. 13):**
- Informacja, że użytkownik komunikuje się z AI
- Informacja o charakterze generowanych treści
- Zalecenia dotyczące weryfikacji wyników

**Nadzór ludzki (art. 14):**
- Projektowanie z zasadą *human-in-the-loop* (wyniki AI wymagają weryfikacji)
- Zapewnienie, że system nie podejmuje decyzji autonomicznie
- Możliwość interwencji użytkownika

**Zapewnienie odpowiednich parametrów dokładności i odporności (art. 15):**
- Warstwy aplikacyjnej AI po stronie platformy AMODIT
- Z wyłączeniem treści promptów i danych wejściowych definiowanych przez klienta

### B) Rossmann (Deployer / operator instalacji on-premise) odpowiada za:

**Zarządzanie danymi (art. 10 – data governance):**
- Rossmann posiada instalację AMODIT **on-premise**, co oznacza, że dane są przechowywane na infrastrukturze Rossmann
- Rossmann zarządza dostępem, backupami, retencją i bezpieczeństwem danych w systemie AMODIT
- Decyzje o danych wejściowych – w przypadku funkcji `AskAI` to Rossmann decyduje, jakie dane trafiają do promptu

**Prowadzenie rejestrów (art. 12):**
- Logi systemowe AMODIT są przechowywane na serwerach Rossmann
- Rossmann zarządza retencją i dostępem do logów

**Konfigurację procesów biznesowych:**
- Sposób wykorzystania funkcjonalności AI w konkretnych procesach
- Decyzje biznesowe podejmowane w oparciu o wyniki AI
- Ocenę ryzyka i obowiązki wynikające z konkretnego use case

### C) Dane przekazywane do warstwy AI (chmura):

Gdy zapytanie trafia do modeli AI, dane są przetwarzane w chmurze zgodnie z gwarancjami dostawców:

| Dostawca | Lokalizacja | Gwarancje |
|----------|-------------|-----------|
| Microsoft Azure OpenAI | Regiony EU | Przetwarzanie na terenie UE, brak treningu na danych klientów |
| Google Vertex AI *(planowane)* | Regiony EU | Przetwarzanie na terenie UE, brak treningu na danych klientów |

Astrafox dobiera i utrzymuje integracje z dostawcami modeli w oparciu o usługi oraz warunki świadczenia usług deklarowane jako zgodne z wymogami prawa UE i mające zastosowanie do tego typu przetwarzania. 

W zakresie parametrów samego silnika LLM, Astrafox, zgodnie z praktyką rynkową, opiera się na publicznych oraz umownych deklaracjach zgodności dostawców modeli (Microsoft, Google). 

### D) Dostawcy modeli GPAI:

Ponoszą obowiązki wynikające z AI Act w zakresie mającym do nich zastosowanie, w tym – w zakresie mającym zastosowanie – obowiązkom przewidzianym m.in. w art. 53 AI Act (obowiązki dostawców modeli AI ogólnego przeznaczenia).

---

## Pytanie 6

**Czy Astrafox zapewnia dokumentację techniczną AI oraz opis ograniczeń i ryzyk?**

**Tak.**

Astrafox udostępnia dokumentację techniczną obejmującą:

**Zasady działania modułów AI:**
- AMODIT Copilot – asystent konwersacyjny z dostępem do baz wiedzy organizacji
- AMODIT AI OCR – rozpoznawanie i ekstrakcja danych z dokumentów
- Funkcje AI w silniku reguł:
  - `AskAI` – bezpośrednie wywołanie modeli LLM
  - `KnowledgeBaseSearch` – semantic search (wyszukiwanie z wykorzystaniem embeddingów AI)
  - `KnowledgeBaseDocumentUpsert` – indeksowanie dokumentów z wykorzystaniem embeddingów AI

**Opis ograniczeń systemowych:**
- Zjawisko halucynacji charakterystyczne dla modeli LLM (model może generować treści, które brzmią wiarygodnie, ale są nieprawdziwe)
- Ograniczenia w rozpoznawaniu specyficznych formatów dokumentów
- Zależność jakości wyników od jakości danych wejściowych

**Zalecane środki kontroli i weryfikacji:**
- Zasada *human-in-the-loop* – wyniki AI powinny być weryfikowane przez człowieka przed podjęciem krytycznych decyzji biznesowych
- Procedury walidacji wyników w procesach krytycznych
- Mechanizmy eskalacji w przypadku wątpliwości co do jakości wyników

**Instrukcje bezpiecznego użytkowania:**
- Najlepsze praktyki konstruowania promptów (w przypadku AskAI)
- Zalecenia dotyczące zarządzania bazami wiedzy
- Wytyczne dotyczące kontroli dostępu do funkcji AI

Dokumentacja jest dostępna w ramach Wiki AMODIT oraz materiałów onboardingowych dla administratorów.


---

## Pytanie 7

**Czy wykorzystywany model AI jest używany jako podwykonawca technologiczny Astrafox, czy bezpośredni dostawca Rossmanna?**

Modele bazowe są wykorzystywane jako **podwykonawca technologiczny Astrafox**. 

**Obecna architektura:**
- Rossmann ↔ AMODIT (Astrafox) ↔ Microsoft Azure OpenAI

**Planowany rozwój:**
- W planach jest integracja z **Google Vertex AI / Gemini** jako alternatywnym dostawcą modeli. Pozwoli to na większą elastyczność i potencjalnie możliwość wyboru dostawcy przez klienta.

Rossmann korzysta z modeli AI wyłącznie za pośrednictwem platformy AMODIT. W standardowym modelu świadczenia usługi w ramach AMODIT nie ma bezpośredniej relacji technicznej ani umownej pomiędzy Rossmann a Microsoft/OpenAI/Google w zakresie usług AI wykorzystywanych w AMODIT.

---

## Pytanie 8

**Czy jako Rossmann podpisujemy jakiekolwiek dodatkowe umowy bezpośrednio z dostawcą modelu/technologii AI wykorzystywanej przez AMODIT/Astrafox?**

**Nie.** 

Cała relacja prawna w zakresie dostarczania funkcjonalności AI jest zawarta w ramach umowy pomiędzy Rossmann a Astrafox. 

Astrafox posiada własne umowy z Microsoft Azure obejmujące usługi Azure OpenAI i zapewnia w zakresie pozostającym pod kontrolą Astrafox, aby korzystanie z tych usług w ramach AMODIT odbywało się na warunkach zgodnych z wymaganiami prawnymi oraz z umowami zawartymi z dostawcą. 

W standardowym modelu świadczenia usługi Rossmann nie musi zawierać odrębnych umów z dostawcami infrastruktury AI.

---

## Pytanie 9

**Czy mamy jako Rossmann wpływ na wybór modelu lub parametrów bezpieczeństwa?**

Odpowiedź zależy od modułu AI oraz poziomu kontroli, jakiego wymaga Rossmann:

### A) AMODIT Copilot

**Wybór modeli:**
- Wybór modeli należy do Astrafox
- Astrafox może dokonywać aktualizacji modeli w ramach rozwoju produktu, kierując się jakością i stabilnością usługi
- Rossmann nie ma bezpośredniego wpływu na wybór modelu konwersacyjnego

**Kontrola bezpieczeństwa po stronie Rossmann:**

Rossmann ma pełną kontrolę nad tym, kto i w jaki sposób korzysta z AMODIT Copilot:

1. **Uprawnienie `CopilotAccess`** (Ustawienia systemowe) – Rossmann decyduje, kto ma dostęp do AMODIT Copilot:
   - `All` – wszyscy użytkownicy
   - `Admins` – tylko administratorzy
   - `Groups` – wybrane grupy użytkowników
   - `None` – funkcja wyłączona

2. **Lokalne Bazy Wiedzy** – Rossmann samodzielnie tworzy i zarządza własnymi bazami wiedzy tematycznymi, np.:
   - *„Wiedza o otwieraniu nowych sklepów"*
   - *„Postępowanie w razie kradzieży w sklepie"* (dostępna tylko dla kierowników)
   - inne bazy dedykowane różnym obszarom działalności
   
   Dla każdej bazy wiedzy Rossmann ustawia **uprawnienia dostępu**:
   - `None` – baza niedostępna w Copilocie
   - `Admins` – tylko administratorzy
   - `AllUsers` – wszyscy użytkownicy
   - `Owner` – tylko właściciel bazy
   - `Custom` – wybrane grupy/osoby

3. **Decyzja o zawartości baz** – Rossmann decyduje, które dokumenty są dodawane do każdej bazy wiedzy. Astrafox nie ma wglądu ani wpływu na treści umieszczane przez Rossmann w ich lokalnych bazach wiedzy.

### B) AMODIT AI OCR

**Stan obecny:**
- Astrafox decyduje, które modele są wykorzystywane do rozpoznawania dokumentów
- Astrafox zastrzega sobie prawo do zmiany modelu, jeśli inny okaże się skuteczniejszy

**Planowane zmiany (Q1 2026):**
- Rozważamy wprowadzenie możliwości wyboru przez Klienta pomiędzy OCR opartym o rozwiązania Microsoft Azure a OCR opartym o Google
- *(Uwaga: ta funkcjonalność jest w fazie planowania i nie jest jeszcze architektonicznie zatwierdzona.)*

### C) Funkcja AskAI (silnik reguł)

**Pełna kontrola Rossmann:**

Rossmann ma pełną kontrolę nad wykorzystaniem funkcji `AskAI`, w tym:

- **Wybór modelu** – z listy udostępnionej przez Astrafox (np. GPT-4o, GPT-4o mini)
- **Konstrukcja promptu** – pełna swoboda w definiowaniu treści zapytania
- **System Message** – możliwość zdefiniowania instrukcji systemowej dla modelu (np. rola, kontekst, ograniczenia)
- **Parametry modelu:**
  - `Temperature` – kontrola kreatywności/deterministyczności odpowiedzi (domyślnie 0.3)
  - `MaxTokens` – limit długości odpowiedzi (domyślnie 2000)
  - `IsJSONResponse` – wymuszenie odpowiedzi w formacie JSON
- **Few-shot learning** – możliwość dostarczenia przykładowych pytań i odpowiedzi dla modelu
- **Dane wejściowe** – pełna kontrola nad tym, jakie dane trafiają do promptu

Astrafox kontroluje jedynie listę dostępnych modeli oraz infrastrukturę integracyjną.

### D) Dodatkowe mechanizmy kontroli

- **Polityki wewnętrzne** – Rossmann ustala własne procedury dotyczące sposobu wykorzystania wyników generowanych przez AI

- **Anonimizacja danych** – AMODIT udostępnia funkcje w silniku reguł umożliwiające anonimizację danych przed przekazaniem do modelu AI

---

## Pytanie 10

**Czy dane Rossmanna są wykorzystywane wyłącznie do inferencji i czy nie są używane do treningu lub fine-tuningu modelu bazowego?**

**Tak.** Dane Rossmann są wykorzystywane wyłącznie do bieżącego przetwarzania (inferencji).

**Gwarancje w tym zakresie:**

1. **Polityka Microsoft Azure OpenAI:** 
   - Zgodnie z warunkami usługi Azure OpenAI, dane przesyłane przez klientów **nie są wykorzystywane** do trenowania, ulepszania ani dostrajania modeli bazowych Microsoft ani OpenAI.

2. **Brak fine-tuningu:** 
   - Astrafox nie wykonuje fine-tuningu modeli bazowych na danych klientów.

3. **Izolacja danych:** 
   - Baza Wiedzy (Knowledge Base) każdej organizacji jest odseparowana – dane jednego klienta nie są dostępne dla innych klientów AMODIT.

4. **Retencja:** 
   - Zgodnie z warunkami usługi Azure OpenAI oraz przy założonej konfiguracji usługi dla AMODIT, dane wejściowe i wyjściowe nie są wykorzystywane do treningu modeli, a ich przechowywanie (jeśli występuje) ma charakter ograniczony i wynika z wymogów technicznych/bezpieczeństwa usługi.

**Kontrola po stronie Rossmann:**

Niezależnie od powyższego, retencja logów oraz danych po stronie infrastruktury Rossmann (instalacja on-premise) jest zarządzana zgodnie z konfiguracją i politykami Rossmann.

---

## Pytanie 11

**Czy w umowie jest: klauzula o odpowiedzialności za AI Act compliance oraz indemnizacja na wypadek naruszeń AI Act?**

**Oficjalne stanowisko Astrafox:**

Publiczny dokument [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/) określa ogólne zasady odpowiedzialności:

> *„Astrafox nie ponosi odpowiedzialności za automatyczne decyzje tworzone przez klienta, klasyfikację ryzyka wdrożeń klienta, skutki biznesowe procesów zaprojektowanych przez klienta."*

Stanowisko to odnosi się przede wszystkim do **procesów projektowanych przez klienta** (np. z wykorzystaniem funkcji `AskAI`), gdzie to klient samodzielnie definiuje logikę i ponosi odpowiedzialność za sposób wykorzystania AI.

**W kontekście modułów zarządzanych przez Astrafox (Copilot, AI OCR):**

Astrafox jako profesjonalny dostawca oprogramowania realizuje swoje obowiązki wynikające z obowiązujących przepisów prawa, w tym rozporządzenia AI Act, w zakresie swoich obowiązków jako dostawcy tych funkcjonalności.

**Propozycja dla Rossmann:**

Rozumiemy, że jako duży klient enterprise Rossmann może wymagać bardziej szczegółowych zapisów umownych. Szczegółowe zapisy dotyczące:
- explicite sformułowanej odpowiedzialności za zgodność z AI Act (z rozróżnieniem modułów Astrafox vs. procesów klienta)
- klauzuli indemnizacyjnej na wypadek naruszeń
- procedur powiadamiania o incydentach
- mechanizmów współpracy w przypadku audytów regulatorów

mogą być przedmiotem **aneksu do umowy** dedykowanego kwestiom AI compliance. Jesteśmy otwarci na rozmowy w tym zakresie i przygotowanie stosownych zapisów umownych uwzględniających specyfikę współpracy z Rossmann.

---

## Pytanie 12

**Czy Astrafox zobowiązuje się do aktualizacji systemu zgodnie z nowymi wytycznymi regulatorów?**

**Tak.** 

W ramach obowiązujących umów i usług utrzymania (maintenance / SaaS) Astrafox:

**Monitoruje zmiany legislacyjne:**
- Śledzi zmiany dotyczące AI Act oraz powiązanych regulacji (RODO, NIS2, Data Act)
- Analizuje wytyczne organów nadzorczych i interpretacje prawne
- Uczestniczy w branżowych inicjatywach dotyczących compliance

**Planuje i realizuje dostosowania:**
- Dostosowywanie systemu AMODIT do ewoluujących wymagań prawnych i technicznych w zakresie mającym zastosowanie do oferowanych funkcjonalności
- Aktualizacje dokumentacji technicznej
- Rozwój mechanizmów zgodności

**Informuje klientów:**
- O istotnych zmianach wpływających na sposób korzystania z funkcji AI
- O nowych funkcjonalnościach wspierających compliance
- O zalecanych działaniach po stronie klienta

**Harmonogram AI Act:**

AI Act wprowadza różne terminy stosowania poszczególnych przepisów (6, 12, 24, 36 miesięcy od wejścia w życie). Astrafox planuje dostosowania zgodnie z harmonogramem regulacyjnym.

**Zgodnie z oficjalnym dokumentem** [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„Korzystamy wyłącznie z dostawców, którzy:*
> - *deklarują zgodność z AI Act,*
> - *zapewniają wymagane dokumentacje i mechanizmy bezpieczeństwa."*

---

## Podsumowanie techniczne (dla kontekstu)

| Aspekt | Szczegóły |
|--------|-----------|
| **Modele bazowe** | GPT-4o, GPT-4o mini via Microsoft Azure OpenAI |
| **Lokalizacja przetwarzania** | Regiony Microsoft Azure na terenie Unii Europejskiej |
| **Instalacja Rossmann** | On-premise – dane przechowywane na infrastrukturze Rossmann |
| **Izolacja danych** | Odseparowana Baza Wiedzy (Knowledge Base) per instancja klienta |
| **Polityka treningu** | No Training – dane klientów nie są używane do treningu modeli; retencja danych po stronie dostawcy jest zgodna z warunkami usługi i konfiguracją przyjętą dla AMODIT |
| **Architektura** | RAG (Retrieval-Augmented Generation) – model bazowy + prywatna baza wiedzy organizacji |
| **Bezpieczeństwo** | ISO 27001, RODO, polityka bezpieczeństwa informacji Astrafox |

---


## Źródła i dokumenty referencyjne

- [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/) – oficjalny dokument publiczny Astrafox
- Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2024/1689 z dnia 13 czerwca 2024 r. ustanawiające zharmonizowane przepisy dotyczące sztucznej inteligencji (AI Act)
- [Polityka Prywatności AMODIT](https://amodit.pl/polityka-prywatnosci-amodit/)
- [Przetwarzanie danych osobowych na platformie AMODIT](https://amodit.pl/przetwarzanie-danych-osobowych-na-platformie-amodit-trust-center/)
- Microsoft Azure OpenAI Service – Terms of Service
