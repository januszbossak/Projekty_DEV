# Odpowiedź w sprawie compliance AI Act – Rossmann

**Data:** 2025-12-19  
**Dotyczy:** Zapytania AI Compliance Officera Rossmann w sprawie platformy AMODIT  
**Status:** Projekt do wewnętrznej weryfikacji przed wysłaniem

> **Zastrzeżenie:**  
> Niniejsze odpowiedzi mają charakter informacyjny i opisują aktualny model odpowiedzialności oraz interpretację wymogów AI Act w odniesieniu do funkcjonalności systemu AMODIT. Ostateczny zakres obowiązków stron może zostać doprecyzowany w umowie lub aneksie.

---

## Pytanie 1

**Czy Astrafox jednoznacznie deklaruje, że jest „providerem systemu AI" w rozumieniu AI Act?**

W odniesieniu do wybranych funkcjonalności AI (w szczególności **AMODIT Copilot** oraz **AMODIT AI OCR**), Astrafox pełni rolę **Dostawcy Systemu AI (Provider)** w rozumieniu AI Act. Jednocześnie wykorzystujemy w architekturze gotowe modele ogólnego przeznaczenia (GPAI) od uznanych dostawców technologicznych. Oznacza to, że Astrafox realizuje swoje obowiązki jako dostawca w zakresie warstwy aplikacyjnej, integracji danych (RAG) oraz bezpiecznego udostępniania funkcjonalności, natomiast opiera się na publicznych oraz umownych deklaracjach zgodności dostawcy modelu w zakresie parametrów samego silnika LLM.

---

## Pytanie 2

**Czy Rossmann jest wyłącznie użytkownikiem / deployerem systemu AI?**

Odpowiedź wymaga rozróżnienia w zależności od wykorzystywanej funkcjonalności AI:

**A) Moduły zarządzane przez Astrafox (AMODIT Copilot, AMODIT AI OCR)**

W przypadku tych modułów Rossmann występuje w roli **Wdrażającego (Deployer)**. Astrafox w całości projektuje i kontroluje architekturę promptów, logikę przetwarzania oraz sposób wykorzystania modeli. Rossmann korzysta z gotowej funkcjonalności bez możliwości modyfikacji warstwy AI.

**B) Funkcja AskAI (silnik reguł AMODIT)**

W przypadku funkcji `AskAI` dostępnej w silniku reguł sytuacja jest bardziej złożona:
- **Twórca procesu** (np. zespół Rossmann) samodzielnie konstruuje prompt o dowolnej treści
- **Wybór modelu** – Rossmann wybiera model z listy udostępnionej przez Astrafox
- **Dane wejściowe** – to twórca procesu decyduje, jakie dane trafiają do promptu (w tym potencjalnie dane osobowe, dane objęte tajemnicą przedsiębiorstwa)
- **Rola Astrafox** – przekazujemy prompt *as is* do modelu LLM (np. Azure OpenAI) bez analizy ani ingerencji w jego treść

W kontekście funkcji `AskAI` Rossmann bierze na siebie większą odpowiedzialność za:
- Treść konstruowanych promptów
- Rodzaj danych przekazywanych do modelu AI
- Zgodność z wewnętrznymi politykami ochrony danych

**Podsumowanie:** Rossmann jest Deployerem w przypadku gotowych modułów (Copilot, AI OCR). W przypadku funkcji `AskAI` rola Rossmann zbliża się do podmiotu definiującego konkretny przypadek użycia (use case) systemu AI, co może generować dodatkowe obowiązki po stronie Rossmann w kontekście AI Act.

---

## Pytanie 3

**Czy w dokumentacji i umowie system jest oferowany pod marką Amodit?**

Tak, funkcjonalności AI są integralną częścią platformy **AMODIT** i są oferowane pod tą marką (np. moduły AMODIT Copilot, AMODIT AI OCR). W dokumentacji produktowej i materiałach umownych występuje nazwa AMODIT jako główna marka produktu. Astrafox jest producentem i właścicielem marki AMODIT.

---

## Pytanie 4

**Kto odpowiada za klasyfikację ryzyka systemu AI?**

Odpowiedzialność za klasyfikację ryzyka zależy od wykorzystywanej funkcjonalności:

**A) Moduły zarządzane przez Astrafox (Copilot, AI OCR)**

Astrafox, jako dostawca (Provider), dokonuje wstępnej oceny klasyfikacji ryzyka projektowanych funkcjonalności AI, przy założeniu standardowych i przewidywalnych scenariuszy użycia. Zgodnie z naszą oceną, standardowe zastosowania tych modułów (automatyzacja workflow, wsparcie analizy dokumentów, asystent konwersacyjny) nie kwalifikują systemu jako **systemu wysokiego ryzyka** w rozumieniu Załącznika III do AI Act.

**Zastrzeżenie:** Ostateczna klasyfikacja ryzyka może ulec zmianie w zależności od konkretnego sposobu wykorzystania systemu przez klienta.

**B) Funkcja AskAI (silnik reguł)**

W przypadku funkcji `AskAI` to **Rossmann** jako twórca procesu decyduje o sposobie wykorzystania AI i ponosi odpowiedzialność za klasyfikację ryzyka konkretnego przypadku użycia (use case).

**Przykład:** Jeżeli Rossmann zdecyduje się użyć `AskAI` do wstępnej analizy CV kandydatów, może to wchodzić w obszar **zatrudnienia** (Załącznik III, punkt 4 AI Act). W takim przypadku:
- Rossmann odpowiada za ocenę, czy dany use case wymaga traktowania jako High-Risk
- Rossmann może zastosować środki minimalizujące ryzyko, np. **anonimizację danych** (imię, nazwisko, telefon) przed wysłaniem do modelu AI – AMODIT udostępnia funkcje w silniku reguł umożliwiające taką anonimizację
- Alternatywnie, Rossmann może dostarczać do systemu już zanonimizowane dokumenty

**Rekomendacja:** Jeżeli Rossmann zamierza wykorzystać `AskAI` w obszarach szczególnie wrażliwych (zatrudnienie, ocena zdolności kredytowej, dostęp do usług), rekomendujemy wspólną analizę przypadku użycia.

---

## Pytanie 5

**Kto odpowiada za zgodność z art. 9–15 AI Act (risk management, data governance)?**

Odpowiedzialność za zgodność z art. 9–15 AI Act jest **rozłożona pomiędzy strony** w zależności od warstwy systemu:

**A) Astrafox (Provider) realizuje swoje obowiązki wynikające z AI Act w szczególności w zakresie:**
- **Elementy systemu zarządzania ryzykiem (art. 9)** odnoszące się do warstwy aplikacyjnej AI (moduły Copilot, AI OCR oraz elementy integracyjne funkcji AskAI po stronie platformy AMODIT)
- **Dokumentację techniczną (art. 11)** – opis działania funkcji AI, ograniczenia, instrukcje użytkowania
- **Przejrzystość i informowanie użytkowników (art. 13)** – informacja, że użytkownik komunikuje się z AI
- **Nadzór ludzki (art. 14)** – projektowanie z zasadą *human-in-the-loop* (wyniki AI wymagają weryfikacji)
- **Zapewnienie odpowiednich parametrów dokładności i odporności (art. 15)** warstwy aplikacyjnej AI po stronie platformy AMODIT (z wyłączeniem treści promptów i danych wejściowych definiowanych przez klienta)

**B) Rossmann (Deployer / operator instalacji on-premise) odpowiada za:**
- **Zarządzanie danymi (art. 10)** – Rossmann posiada instalację AMODIT **on-premise**, co oznacza, że dane są przechowywane na infrastrukturze Rossmann. Rossmann zarządza dostępem, backupami, retencją i bezpieczeństwem danych w systemie AMODIT.
- **Prowadzenie rejestrów (art. 12)** – logi systemowe AMODIT są przechowywane na serwerach Rossmann
- **Decyzje o danych wejściowych** – w przypadku funkcji `AskAI` to Rossmann decyduje, jakie dane trafiają do promptu

**C) Dane przekazywane do warstwy AI (chmura):**

Gdy zapytanie trafia do modeli AI, dane są przetwarzane w chmurze zgodnie z gwarancjami dostawców:

| Dostawca | Lokalizacja | Gwarancje |
|----------|-------------|-----------|
| Microsoft Azure OpenAI | Regiony EU | Przetwarzanie na terenie UE, brak treningu na danych klientów |
| Google Vertex AI *(planowane)* | Regiony EU | Przetwarzanie na terenie UE, brak treningu na danych klientów |

Astrafox dobiera i utrzymuje integracje z dostawcami modeli w oparciu o usługi oraz warunki świadczenia usług deklarowane jako zgodne z wymogami prawa UE i mające zastosowanie do tego typu przetwarzania. W zakresie parametrów samego silnika LLM, Astrafox, zgodnie z praktyką rynkową, opiera się na publicznych oraz umownych deklaracjach zgodności dostawców modeli (Microsoft, Google). Dostawcy modeli GPAI podlegają obowiązkom wynikającym z AI Act, w tym – w zakresie mającym zastosowanie – obowiązkom przewidzianym m.in. w art. 53 AI Act.

---

## Pytanie 6

**Czy Astrafox zapewnia dokumentację techniczną AI oraz opis ograniczeń i ryzyk?**

Tak, Astrafox udostępnia dokumentację techniczną obejmującą:
- Zasady działania modułów AI (AMODIT Copilot, AMODIT AI OCR)
- Opis ograniczeń systemowych (np. zjawisko halucynacji charakterystyczne dla modeli LLM)
- Zalecane środki kontroli i weryfikacji (zasada *human-in-the-loop* – wyniki AI powinny być weryfikowane przez człowieka przed podjęciem krytycznych decyzji biznesowych)
- Instrukcje bezpiecznego użytkowania

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

**Czy jako Rossmann podpisujemy jakiekolwiek dodatkowe umowy bezpośrednio z dostawcą modelu/technologii AI wykorzystywanej przez Amodit/Astrafox?**

Nie. Cała relacja prawna w zakresie dostarczania funkcjonalności AI jest zawarta w ramach umowy pomiędzy Rossmann a Astrafox. 

Astrafox posiada własne umowy z Microsoft Azure obejmujące usługi Azure OpenAI i zapewnia w zakresie pozostającym pod kontrolą Astrafox, aby korzystanie z tych usług w ramach AMODIT odbywało się na warunkach zgodnych z wymaganiami prawnymi oraz z umowami zawartymi z dostawcą. W standardowym modelu świadczenia usługi Rossmann nie musi zawierać odrębnych umów z dostawcami infrastruktury AI.

---

## Pytanie 9

**Czy mamy jako Rossmann wpływ na wybór modelu lub parametrów bezpieczeństwa?**

Odpowiedź zależy od modułu AI:

**A) AMODIT Copilot**
- Wybór modeli  należy do Astrafox
- Astrafox może dokonywać aktualizacji modeli w ramach rozwoju produktu, kierując się jakością i stabilnością usługi
- Rossmann nie ma bezpośredniego wpływu na wybór modelu konwersacyjnego

**B) AMODIT AI OCR**
- **Stan obecny:** Astrafox decyduje, które modele są wykorzystywane do rozpoznawania dokumentów. Astrafox zastrzega sobie prawo do zmiany modelu, jeśli inny okaże się skuteczniejszy.
- **Planowane zmiany (Q1 2026):** Rozważamy wprowadzenie możliwości wyboru przez Klienta pomiędzy OCR opartym o rozwiązania Microsoft Azure a OCR opartym o Google. *(Uwaga: ta funkcjonalność jest w fazie planowania i nie jest jeszcze architektonicznie zatwierdzona.)*

**C) Funkcja AskAI (silnik reguł)**
- Rossmann **wybiera model** z listy udostępnionej przez Astrafox
- Rossmann **konstruuje prompt** i decyduje o danych wejściowych
- Astrafox kontroluje jedynie listę dostępnych modeli

**Kontrola bezpieczeństwa po stronie Rossmann:**

1. **Uprawnienie `CopilotAccess`** (Ustawienia systemowe) – Rossmann decyduje, kto ma dostęp do AMODIT Copilot:
   - `All` – wszyscy użytkownicy
   - `Admins` – tylko administratorzy
   - `Groups` – wybrane grupy użytkowników
   - `None` – funkcja wyłączona

2. **Lokalne Bazy Wiedzy** – Rossmann samodzielnie tworzy i zarządza własnymi bazami wiedzy tematycznymi, np.:
   - *"Wiedza o otwieraniu nowych sklepów"*
   - *"Postępowanie w razie kradzieży w sklepie"* (dostępna tylko dla kierowników)
   - inne bazy dedykowane różnym obszarom działalności
   
   Dla każdej bazy wiedzy Rossmann ustawia **uprawnienia dostępu**:
   - `None` – baza niedostępna w Copilocie
   - `Admins` – tylko administratorzy
   - `AllUsers` – wszyscy użytkownicy
   - `Owner` – tylko właściciel bazy
   - `Custom` – wybrane grupy/osoby

3. **Decyzja o zawartości baz** – Rossmann decyduje, które dokumenty są dodawane do każdej bazy wiedzy. Astrafox nie ma wglądu ani wpływu na treści umieszczane przez Rossmann w ich lokalnych bazach wiedzy.

4. **Polityki wewnętrzne** – Rossmann ustala własne procedury dotyczące sposobu wykorzystania wyników generowanych przez AI

5. **Funkcja `AskAI`** – pełna kontrola nad treścią promptu i danymi wejściowymi

Jeżeli Rossmann ma szczególne wymagania dotyczące parametrów modelu (np. temperatura, limity tokenów) lub wyłączenia określonych funkcji, możemy omówić to w ramach indywidualnych ustaleń.

---

## Pytanie 10

**Czy dane Rossmanna są wykorzystywane wyłącznie do inferencji i czy nie są używane do treningu lub fine-tuningu modelu bazowego?**

**Tak.** Dane Rossmann są wykorzystywane wyłącznie do bieżącego przetwarzania (inferencji).

Gwarancje w tym zakresie:
1. **Polityka Microsoft Azure OpenAI:** Zgodnie z warunkami usługi Azure OpenAI, dane przesyłane przez klientów **nie są wykorzystywane** do trenowania, ulepszania ani dostrajania modeli bazowych Microsoft ani OpenAI.
2. **Brak fine-tuningu:** Astrafox nie wykonuje fine-tuningu modeli bazowych na danych klientów.
3. **Izolacja danych:** Baza Wiedzy (Knowledge Base) każdej organizacji jest odseparowana – dane jednego klienta nie są dostępne dla innych klientów AMODIT.
4. **Retencja:** Zgodnie z warunkami usługi Azure OpenAI oraz przy założonej konfiguracji usługi dla AMODIT, dane wejściowe i wyjściowe nie są wykorzystywane do treningu modeli, a ich przechowywanie (jeśli występuje) ma charakter ograniczony i wynika z wymogów technicznych/bezpieczeństwa usługi.

Niezależnie od powyższego, retencja logów oraz danych po stronie infrastruktury Rossmann (instalacja on-premise) jest zarządzana zgodnie z konfiguracją i politykami Rossmann.

---

## Pytanie 11

**Czy w umowie jest: klauzula o odpowiedzialności za AI Act compliance oraz indemnizacja na wypadek naruszeń AI Act?**

**Oficjalne stanowisko Astrafox:**

Publiczny dokument [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/) określa ogólne zasady odpowiedzialności:

> *„Astrafox nie ponosi odpowiedzialności za automatyczne decyzje tworzone przez klienta, klasyfikację ryzyka wdrożeń klienta, skutki biznesowe procesów zaprojektowanych przez klienta."*

Stanowisko to odnosi się przede wszystkim do **procesów projektowanych przez klienta** (np. z wykorzystaniem funkcji `AskAI`), gdzie to klient samodzielnie definiuje logikę i ponosi odpowiedzialność za sposób wykorzystania AI.

**W kontekście modułów zarządzanych przez Astrafox (Copilot, AI OCR):**

Astrafox jako profesjonalny dostawca oprogramowania realizuje swoje obowiązki wynikające z obowiązujących przepisów prawa, w tym rozporządzenia AI Act, w zakresie swoich obowiązków jako Provider tych modułów.

**Propozycja dla Rossmann:**

Rozumiemy, że jako duży klient enterprise Rossmann może wymagać bardziej szczegółowych zapisów umownych. Szczegółowe zapisy dotyczące:
- explicite sformułowanej odpowiedzialności za zgodność z AI Act (z rozróżnieniem modułów Astrafox vs. procesów klienta)
- klauzuli indemnizacyjnej na wypadek naruszeń
- procedur powiadamiania o incydentach

mogą być przedmiotem **aneksu do umowy** dedykowanego kwestiom AI compliance. Jesteśmy otwarci na rozmowy w tym zakresie i przygotowanie stosownych zapisów umownych uwzględniających specyfikę współpracy z Rossmann.

---

## Pytanie 12

**Czy Astrafox zobowiązuje się do aktualizacji systemu zgodnie z nowymi wytycznymi regulatorów?**

Tak. W ramach obowiązujących umów i usług utrzymania (maintenance / SaaS) Astrafox:
- Monitoruje zmiany legislacyjne dotyczące AI Act oraz powiązanych regulacji
- Planuje i realizuje dostosowywanie systemu AMODIT do ewoluujących wymagań prawnych i technicznych w zakresie mającym zastosowanie do oferowanych funkcjonalności
- Informuje klientów o istotnych zmianach wpływających na sposób korzystania z funkcji AI

AI Act wprowadza różne terminy stosowania poszczególnych przepisów (6, 12, 24, 36 miesięcy od wejścia w życie). Astrafox planuje dostosowania zgodnie z harmonogramem regulacyjnym.

---

## Podsumowanie techniczne (dla kontekstu)

| Aspekt | Szczegóły |
|--------|-----------|
| **Modele bazowe** | GPT-4o, GPT-4o mini via Microsoft Azure OpenAI |
| **Lokalizacja przetwarzania** | Regiony Microsoft Azure na terenie Unii Europejskiej |
| **Izolacja danych** | Odseparowana Baza Wiedzy (Knowledge Base) per instancja klienta |
| **Polityka treningu** | No Training – dane klientów nie są używane do treningu modeli; retencja danych po stronie dostawcy jest zgodna z warunkami usługi i konfiguracją przyjętą dla AMODIT |
| **Architektura** | RAG (Retrieval-Augmented Generation) – model bazowy + prywatna baza wiedzy organizacji |

---

## Uwagi końcowe

Niniejszy dokument stanowi projekt odpowiedzi do wewnętrznej weryfikacji. Przed wysłaniem do Rossmann rekomendujemy:
1. Weryfikację przez dział prawny Astrafox
2. Ewentualne konsultacje z zespołem odpowiedzialnym za umowy z klientami
3. Przygotowanie propozycji aneksu AI compliance (w nawiązaniu do pytania 11)

---


