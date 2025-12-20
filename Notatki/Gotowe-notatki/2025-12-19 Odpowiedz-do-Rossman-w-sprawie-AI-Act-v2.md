# Odpowiedź w sprawie compliance AI Act – Rossmann (v2)

**Data:** 2025-12-19  
**Dotyczy:** Zapytania AI Compliance Officera Rossmann w sprawie platformy AMODIT  
**Status:** Projekt do wewnętrznej weryfikacji przed wysłaniem

> **Zastrzeżenie:**  
> Niniejsze odpowiedzi mają charakter informacyjny i opisują aktualny model odpowiedzialności oraz interpretację wymogów AI Act w odniesieniu do funkcjonalności systemu AMODIT. Ostateczny zakres obowiązków stron może zostać doprecyzowany w umowie lub aneksie.

---

## Pytanie 1

**Czy Astrafox jednoznacznie deklaruje, że jest „providerem systemu AI" w rozumieniu AI Act?**

**Nie.**

Astrafox nie deklaruje, że platforma AMODIT jako całość stanowi „system AI" w rozumieniu art. 3 AI Act ani że Astrafox pełni rolę Provider systemu AI w tym znaczeniu.

**Platforma AMODIT jest systemem klasy BPM / DMS / low-code**, który umożliwia klientom korzystanie z funkcjonalności opartych o zewnętrzne modele AI (GPAI), dostarczane przez wyspecjalizowanych dostawców technologicznych (np. Microsoft Azure OpenAI).

Astrafox:
- nie tworzy modeli bazowych,
- nie trenuje modeli,
- nie wprowadza na rynek własnych modeli AI,
- nie udostępnia samodzielnego systemu AI niezależnie od platformy AMODIT.

**Zgodnie z publicznym dokumentem** [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„Platforma AMODIT jako system BPM/DMS/Low-code nie jest samodzielnym „systemem sztucznej inteligencji" w rozumieniu art. 3 AI Act."*

AMODIT umożliwia użytkownikom wykorzystanie zewnętrznych modeli AI (np. AMODIT Copilot, integracje z LLM), ale w takich sytuacjach:

→ **klient, a nie AMODIT, podlega obowiązkom AI Act jako „deployer"**  
→ i odpowiada za sposób wykorzystania AI w swoich procesach.

---

## Pytanie 2

**Czy Rossmann jest wyłącznie użytkownikiem / deployerem systemu AI?**

W kontekście AI Act, **Rossmann występuje w roli Deployer**, przy czym zakres obowiązków zależy od sposobu wykorzystania funkcjonalności AI w ramach platformy AMODIT.

### A) Gotowe funkcjonalności AI w AMODIT (np. Copilot, AI OCR)

Astrafox dostarcza standardowe funkcjonalności platformowe, które:
- integrują modele AI dostawców zewnętrznych,
- nie podejmują autonomicznych decyzji,
- mają charakter wspierający użytkownika.

**Rossmann decyduje:**
- czy i w jakich procesach te funkcjonalności są wykorzystywane,
- jakie dane są do nich przekazywane,
- jakie skutki biznesowe wywołują ich użycia.

### B) Funkcja AskAI (silnik reguł)

W przypadku funkcji AskAI:
- **Rossmann samodzielnie definiuje prompt**,
- decyduje o danych wejściowych,
- wybiera model z listy dostępnej w platformie.

**Odpowiedzialność za zgodność danego use case z AI Act (w tym klasyfikację ryzyka) spoczywa na Rossmann jako deployerze.**

---

## Pytanie 3

**Czy w dokumentacji i umowie system jest oferowany pod marką AMODIT?**

**Tak.**

Funkcjonalności AI są oferowane jako element platformy **AMODIT**.  
Astrafox jest producentem i właścicielem platformy AMODIT.

---

## Pytanie 4

**Kto odpowiada za klasyfikację ryzyka systemu AI?**

Zgodnie z AI Act, **klasyfikacja ryzyka zależy od konkretnego przypadku użycia (use case)**.

### Podział odpowiedzialności:

**Astrafox:**
- nie klasyfikuje procesów klienta, ponieważ:
  - nie zna kontekstu biznesowego,
  - nie decyduje o danych wejściowych,
  - nie decyduje o skutkach wykorzystania AI.

**Rossmann (jako deployer):**
- odpowiada za ocenę, czy dany sposób wykorzystania AI:
  - wchodzi w obszary wskazane w Załączniku III AI Act,
  - wymaga zastosowania dodatkowych środków organizacyjnych lub technicznych.

**Zgodnie z dokumentem publicznym** [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„Astrafox:*
> - *nie zna szczegółów procesów wdrażanych przez klienta,*
> - *nie klasyfikuje procesów klienta,*
> - *nie ponosi odpowiedzialności za ich zgodność z AI Act."*

---

## Pytanie 5

**Kto odpowiada za zgodność z art. 9–15 AI Act?**

Odpowiedzialność jest **rozproszona zgodnie z rolami**:

### Astrafox:

Zapewnia, że platforma AMODIT:
- **umożliwia nadzór ludzki** (art. 14),
- **informuje użytkownika o wykorzystaniu AI** (art. 13 – transparentność),
- **posiada dokumentację techniczną funkcjonalności** (art. 11),
- **integruje się z dostawcami modeli** na warunkach deklarowanych jako zgodne z prawem UE.

**Zgodnie z dokumentem publicznym** [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„W celu zapewnienia zgodności z AI Act wdrożyliśmy następujące środki:*
> - *Transparentność (art. 52 AI Act) – użytkownicy są informowani, że dana funkcja korzysta z AI,*
> - *Nadzór człowieka – AMODIT nie podejmuje decyzji autonomicznie,*
> - *Minimalizacja danych i bezpieczeństwo – zgodnie z RODO, ISO 27001,*
> - *Współpraca z dostawcami zgodnymi z AI Act."*

### Rossmann (Deployer):

Odpowiada za:
- **dane wykorzystywane w AI** (art. 10 – data governance),
- **konfigurację procesów**,
- **decyzje biznesowe** podejmowane w oparciu o wyniki AI,
- **ocenę ryzyka i obowiązki** wynikające z konkretnego use case.

**Zgodnie z dokumentem publicznym** [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„Klient, korzystając z funkcji AI w swoich procesach:*
> - *jest podmiotem stosującym system AI („deployer"),*
> - *sam klasyfikuje ryzyko zastosowania,*
> - *ponosi odpowiedzialność za zgodność takiego procesu z AI Act,*
> - *zapewnia nadzór człowieka, jeśli jest to wymagane,*
> - *weryfikuje i kontroluje treści generowane przez AI."*

### Dostawcy modeli GPAI:

Ponoszą obowiązki wynikające z AI Act w zakresie mającym do nich zastosowanie (w tym m.in. art. 53).

---

## Pytanie 6

**Czy Astrafox zapewnia dokumentację techniczną AI oraz opis ograniczeń i ryzyk?**

**Tak.**

Astrafox udostępnia dokumentację platformy AMODIT, obejmującą:
- opis funkcjonalności AI,
- ich przeznaczenie,
- ograniczenia (np. brak autonomicznego podejmowania decyzji),
- zalecenia dotyczące weryfikacji wyników przez użytkownika.

**Zgodnie z dokumentem publicznym** [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„Użytkownicy są informowani, że:*
> - *dana funkcja korzysta z AI,*
> - *generowane treści wymagają weryfikacji,*
> - *odpowiedzialność za wykorzystanie wyników AI spoczywa na użytkowniku."*

---

## Pytanie 7–8

**Relacja z dostawcami modeli AI**

Modele AI są dostarczane przez zewnętrznych dostawców technologicznych i wykorzystywane w AMODIT w ramach integracji platformowej.

**Rossmann nie posiada bezpośredniej relacji umownej z dostawcami modeli AI** w standardowym modelu świadczenia usługi.

**Architektura:**
- Rossmann ↔ AMODIT (Astrafox) ↔ Microsoft Azure OpenAI

Astrafox posiada własne umowy z dostawcami modeli i zapewnia, aby korzystanie z tych usług w ramach AMODIT odbywało się na warunkach zgodnych z wymaganiami prawnymi.

---

## Pytanie 9

**Wpływ Rossmann na modele i bezpieczeństwo**

Rossmann:
- **decyduje o tym, czy i gdzie AI jest używane**,
- **decyduje o danych wejściowych**,
- w przypadku **AskAI** — decyduje o promptach i wyborze modelu,
- **kontroluje uprawnienia dostępu** do funkcji AI (ustawienie `CopilotAccess`),
- **zarządza lokalnymi bazami wiedzy** – samodzielnie tworzy i zarządza własnymi bazami wiedzy tematycznymi, ustawia uprawnienia dostępu do każdej bazy,
- **decyduje o zawartości baz** – Astrafox nie ma wglądu ani wpływu na treści umieszczane przez Rossmann w ich lokalnych bazach wiedzy.

---

## Pytanie 10

**Czy dane są wykorzystywane do treningu?**

**Nie.**

Dane klientów:
- są wykorzystywane **wyłącznie do inferencji**,
- **nie są używane do treningu modeli bazowych**,
- są przetwarzane zgodnie z warunkami usług dostawców modeli.

**Gwarancje:**
- Zgodnie z polityką Microsoft Azure OpenAI, dane przesyłane przez klientów **nie są wykorzystywane** do trenowania, ulepszania ani dostrajania modeli bazowych.
- Baza Wiedzy (Knowledge Base) każdej organizacji jest **odseparowana** – dane jednego klienta nie są dostępne dla innych klientów AMODIT.

---

## Pytanie 11

**Klauzule umowne / indemnizacja**

Umowy AMODIT odzwierciedlają podział odpowiedzialności.

**Zgodnie z dokumentem publicznym** [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„Astrafox nie ponosi odpowiedzialności za:*
> - *automatyczne decyzje tworzone przez klienta,*
> - *klasyfikację ryzyka wdrożeń klienta,*
> - *skutki biznesowe procesów zaprojektowanych przez klienta."*

**Propozycja dla Rossmann:**

Rozumiemy, że jako duży klient enterprise Rossmann może wymagać bardziej szczegółowych zapisów umownych. Szczegółowe zapisy dotyczące:
- explicite sformułowanej odpowiedzialności za zgodność z AI Act,
- klauzuli indemnizacyjnej na wypadek naruszeń,
- procedur powiadamiania o incydentach,

**mogą być przedmiotem aneksu do umowy** dedykowanego kwestiom AI compliance. Jesteśmy otwarci na rozmowy w tym zakresie.

---

## Pytanie 12

**Aktualizacja systemu**

**Tak.**

Astrafox monitoruje zmiany regulacyjne i rozwija platformę AMODIT zgodnie z obowiązującymi przepisami, w zakresie mającym zastosowanie do oferowanych funkcjonalności.

**Zgodnie z dokumentem publicznym** [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/):

> *„Korzystamy wyłącznie z dostawców, którzy:*
> - *deklarują zgodność z AI Act,*
> - *zapewniają wymagane dokumentacje i mechanizmy bezpieczeństwa."*

AI Act wprowadza różne terminy stosowania poszczególnych przepisów. Astrafox planuje dostosowania zgodnie z harmonogramem regulacyjnym.

---

## Podsumowanie techniczne

| Aspekt | Szczegóły |
|--------|-----------|
| **Modele bazowe** | GPT-4o, GPT-4o mini via Microsoft Azure OpenAI |
| **Lokalizacja przetwarzania** | Regiony Microsoft Azure na terenie Unii Europejskiej |
| **Izolacja danych** | Odseparowana Baza Wiedzy (Knowledge Base) per instancja klienta |
| **Polityka treningu** | No Training – dane klientów nie są używane do treningu modeli |
| **Architektura** | RAG (Retrieval-Augmented Generation) – model bazowy + prywatna baza wiedzy organizacji |
| **Instalacja Rossmann** | On-premise – dane przechowywane na infrastrukturze Rossmann |

---

## Uwagi końcowe

Niniejszy dokument stanowi projekt odpowiedzi do wewnętrznej weryfikacji. Przed wysłaniem do Rossmann rekomendujemy:
1. Weryfikację przez dział prawny Astrafox
2. Ewentualne konsultacje z zespołem odpowiedzialnym za umowy z klientami
3. Przygotowanie propozycji aneksu AI compliance (w nawiązaniu do pytania 11)

---

## Źródła

- [Zgodność AMODIT z AI Act](https://amodit.pl/ai-act/) – dokument publiczny Astrafox
- Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2024/1689 (AI Act)
