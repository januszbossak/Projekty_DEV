# Odpowiedź w sprawie compliance AI Act – Rossmann

**Data:** 2025-12-19  
**Dotyczy:** Zapytania AI Compliance Officera Rossmann w sprawie platformy AMODIT  

---

## ⚠️ WEWNĘTRZNE: Analiza rozbieżności z oficjalną stroną

**Źródło:** [https://amodit.pl/ai-act/](https://amodit.pl/ai-act/)

Poniższa analiza wskazuje różnice między niniejszym dokumentem a oficjalnym stanowiskiem opublikowanym na stronie Astrafox. Służy jako materiał do wewnętrznej dyskusji.

### Rozbieżność 1: Rola Astrafox (Provider vs. Platforma)

| **Oficjalna strona** | **Ten dokument** |
|---------------------|------------------|
| *"Platforma AMODIT jako system BPM/DMS/Low-code nie jest samodzielnym „systemem sztucznej inteligencji" w rozumieniu art. 3 AI Act. AMODIT umożliwia użytkownikom wykorzystanie zewnętrznych modeli AI."* | Astrafox występuje jako **Dostawca Systemu AI (Provider)** dla modułów Copilot i AI OCR. |

**Pytanie do dyskusji:** Czy pozycjonowanie jako "platforma umożliwiająca" jest wystarczająco precyzyjne? W przypadku modułów Copilot i AI OCR, Astrafox de facto projektuje prompty, integruje modele i kontroluje architekturę – co może kwalifikować nas jako Provider w rozumieniu AI Act.

---

### Rozbieżność 2: Odpowiedzialność za klasyfikację ryzyka

| **Oficjalna strona** | **Ten dokument** |
|---------------------|------------------|
| *"Astrafox nie klasyfikuje procesów klienta, nie ponosi odpowiedzialności za ich zgodność z AI Act."* | Dla Copilot/AI OCR Astrafox odpowiada za klasyfikację. Dla AskAI odpowiada klient. |

**Pytanie do dyskusji:** Oficjalna strona całkowicie przenosi odpowiedzialność na klienta. Czy to jest bezpieczne prawnie, skoro w przypadku Copilot/AI OCR to my projektujemy logikę AI?

---

### Rozbieżność 3: Podział obowiązków art. 9-15 AI Act

| **Oficjalna strona** | **Ten dokument** |
|---------------------|------------------|
| *"Klient sam klasyfikuje ryzyko zastosowania, ponosi odpowiedzialność za zgodność z AI Act"* | Rozdzielamy: Astrafox (art. 9, 11, 13-15), Rossmann/klient (art. 10, 12) |

**Pytanie do dyskusji:** Oficjalna strona umieszcza całą odpowiedzialność po stronie klienta. Nasz dokument jest bardziej precyzyjny i uznaje, że przy modułach zarządzanych przez Astrafox część odpowiedzialności leży po naszej stronie.

---

### Rozbieżność 4: Klauzule odpowiedzialności i indemnizacji

| **Oficjalna strona** | **Ten dokument** |
|---------------------|------------------|
| *"Astrafox nie ponosi odpowiedzialności za automatyczne decyzje tworzone przez klienta, klasyfikację ryzyka wdrożeń klienta, skutki biznesowe procesów zaprojektowanych przez klienta"* | Sugerujemy możliwość przygotowania aneksu z klauzulą odpowiedzialności i indemnizacją |

**Pytanie do dyskusji:** Oficjalna strona wyłącza odpowiedzialność. Czy przy dużych klientach (jak Rossmann) nie powinniśmy mieć bardziej proaktywnego stanowiska?

---

### Rekomendacja

Oficjalna strona amodit.pl/ai-act/ przyjmuje stanowisko maksymalnie chroniące Astrafox (całkowite przeniesienie odpowiedzialności na klienta). Jest to zrozumiałe jako ogólny komunikat.

Jednak w przypadku **konkretnych klientów enterprise** (Rossmann, Vasco, etc.) może być konieczne:
1. Bardziej precyzyjne rozróżnienie między modułami zarządzanymi przez Astrafox a funkcją AskAI
2. Doprecyzowanie roli Astrafox jako Provider (przynajmniej dla Copilot/AI OCR)
3. Przygotowanie wzoru aneksu AI compliance dla klientów wymagających formalnych deklaracji

**Sugestia:** Rozważyć aktualizację oficjalnej strony o rozróżnienie między różnymi funkcjonalnościami AI (moduły Astrafox vs. procesy budowane przez klienta).
