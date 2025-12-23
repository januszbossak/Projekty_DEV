# Analiza spotkań farmingowych dla działu R&D
**Data analizy:** 2025-12-20  
**Zakres:** 17 spotkań farmingowych (październik-grudzień 2025)  
**Autor:** Analiza AI na podstawie notatek ze spotkań

---

## Executive Summary

Analiza 17 spotkań farmingowych ujawnia **kluczowe obszary wymagające uwagi działu R&D**. Klienci wyrażają wysokie zadowolenie z kierunku rozwoju produktu (AI, stabilizacja), ale zgłaszają **powtarzające się problemy** dotyczące modułu raportowego, dokumentacji, zarządzania dostępami oraz potrzeby większej otwartości systemu. 

**Najważniejsze wnioski:**
- **Moduł raportowy** to największy ból klientów - zbyt skomplikowany, brakuje funkcji ad-hoc
- **AI/MCP** to kierunek bardzo oczekiwany przez klientów enterprise
- **OCR** wymaga ciągłego doskonalenia (faktury zagraniczne, nietypowe formaty)
- **Dokumentacja i Help** są niewystarczające dla użytkowników końcowych
- **Portal pracowniczy/licencje okazjonalne** to powtarzająca się potrzeba biznesowa

---

## I. KWESTIE BEZPOŚREDNIO WSKAZANE PRZEZ KLIENTÓW

### 1. Moduł Raportowy - KRYTYCZNY PRIORYTET

**Klienci zgłaszający:** AmRest, HAWE Telekom, NIDEN, Horn Distribution

#### Problemy:
- **Zbyt skomplikowany dla użytkowników końcowych** (AmRest, NIDEN)
- **Konieczność zapisywania raportów** postrzegana jako poważne ograniczenie (AmRest)
- **Brak prostych filtrów "ad hoc"** - użytkownicy chcą szybko przejrzeć dane bez tworzenia raportu (AmRest)
- **Brak możliwości przyznania dostępu do edycji raportu** osobom niebędącym twórcami/administratorami (NIDEN)
- **Personalizacja kolumn** - użytkownicy nie mogą układać własnych kolumn, tylko twórca raportu (HAWE Telekom)
- **Szerokość kolumn** - potrzeba łatwej i trwałej zmiany (HAWE Telekom)
- **Brak funkcji cyklicznego wysyłania raportów** (AmRest)

#### Kontekst biznesowy:
- AmRest **nie przeszedł na nowy moduł** mimo 5 lat od jego powstania - wciąż używa "wyszukiwania zaawansowanego"
- Powód: nowy moduł wymaga zapisywania raportu (blokuje masowe uruchamianie reguł), przepisanie setek raportów
- **Ryzyko:** AmRest może stać się "drugim Orlenem" - osobna linia produktu z poprawkami do starych funkcji

#### Rekomendacje R&D:
1. **PILNE:** Stworzyć uproszczony widok raportowy / tryb "ad hoc" bez konieczności zapisywania
2. **PILNE:** Dodać możliwość udostępniania uprawnień do edycji raportów
3. Rozważyć konwerter raportów ze starego modułu (już istnieje, ale promować)
4. Dodać funkcję cyklicznego wysyłania raportów
5. Personalizacja widoków użytkowników (kolumny, szerokości)

---

### 2. AI i Integracje - STRATEGICZNY PRIORYTET

**Klienci zgłaszający:** Rossmann, AmRest, Holcim, Grupa Pracuj.pl, RESINVEST, Coral Travel, NIDEN, PGE Obrót

#### Oczekiwania:
- **Protokół MCP (Agent Protocol)** - absolutny must-have (Rossmann, RESINVEST)
- **Integracja własnych agentów AI** klientów z AMODIT (Rossmann, Grupa Pracuj.pl, Polpharma)
- **Open Data Protocol** dla systemów BI (Rossmann, NIDEN)
- **Copilot** - dostęp do danych procesów, baza wiedzy (wszystkie duże firmy)
- **AI w Teams** - możliwość zadawania pytań o urlopy, faktury bez logowania do AMODIT (RESINVEST, Rossmann)

#### Konkretne use case:
- **Automatyczne opisywanie faktur kosztowych** na podstawie historii (Lewiatan, AmRest)
- **Weryfikacja faktur z umowami** (Rossmann, NIDEN)
- **Analiza CV** (NIDEN, Grupa Pracuj.pl)
- **Klasyfikacja i kategoryzacja dokumentów** (Rossmann, ORA Warszawa)
- **Podpowiedzi w dekretacji** (Coral Travel, Horn Distribution)

#### Obawy klientów:
- **Bezpieczeństwo danych** - wymóg serwerów w Europie, zgodność z RODO (Rossmann, HAWE, NIDEN)
- **Transparentność** - klienci chcą wiedzieć, gdzie są dane i jak AI działa (HAWE, Lewiatan)
- **Kontrola** - możliwość włączania/wyłączania AI przez administratora (NIDEN)

#### Rekomendacje R&D:
1. **NAJWYŻSZY PRIORYTET:** Dokończyć i wdrożyć protokół MCP (klienci pytają o to na każdym spotkaniu!)
2. Rozbudować Copilota o dostęp do danych procesów (z kontrolą uprawnień)
3. Stworzyć dokumentację bezpieczeństwa AI dla działów RODO klientów
4. Rozważyć integrację z Gemini (oprócz Azure) - Holcim, Vasco
5. Panel monitorowania zużycia AI/tokenów z limitami (Lewiatan)

---

### 3. OCR - CIĄGŁE DOSKONALENIE

**Klienci zgłaszający:** Vasco, Lewiatan, AGRO TUW, Grupa Żywiec, Coral Travel, Horn Distribution

#### Problemy:
- **Faktury zagraniczne** (chińskie, AWS) - słaba jakość rozpoznawania (Vasco, AmRest)
- **Dokumenty od pośredników** zwolnionych z VAT (AGRO TUW)
- **Nietypowe formaty** - faktury lotnicze (Coral Travel)
- **Dokumenty HR** - badania PHP, zaświadczenia lekarskie (Rossmann)

#### Sukcesy:
- **Vasco:** Google Gemini rozpoznał 90% faktur, które Azure nie rozpoznał żadnej ✅
- **Grupa Żywiec:** Migracja z Skanuj.to na AMODIT AI OCR w trakcie, pozytywne oceny ✅
- **Coral Travel:** Nowy OCR "o niebo lepszy niż poprzedni" ✅

#### Rekomendacje R&D:
1. Kontynuować rozwój integracji z Google Gemini (alternatywa dla Azure)
2. Rozszerzyć wsparcie dla dokumentów HR (badania, zaświadczenia)
3. **Raportowanie jakości OCR** - accuracy, wyjątki (Grupa Żywiec)
4. Lepsze wsparcie dla faktur zagranicznych i nietypowych formatów

---

### 4. Dokumentacja i Help - POWAŻNA LUKA

**Klienci zgłaszający:** Lewiatan, AmRest, NIDEN, AGRO TUW

#### Problemy:
- **Opisy funkcji w Wiki/Help zbyt lakoniczne** (Lewiatan, NIDEN)
- **Brak oznaczenia modułów płatnych** (Lewiatan, NIDEN)
- **Brak wymagań systemowych** dla kolejnych wersji (Lewiatan)
  - Przykład: Klient musiał awaryjnie aktualizować Windows Server 2019, bo nie wiedział o wymaganiach wersji 2025
- **Brak dostępu do archiwalnych wersji** instalatorów (Lewiatan)
- **Brak przykładów użycia** - dokumentacja opisuje składnię, ale nie kontekst (AmRest)

#### Kontekst:
- Klienci on-premises (Lewiatan, AGRO TUW) szczególnie dotknięci brakiem dokumentacji instalacyjnej
- Konsultanci muszą powtarzać te same wyjaśnienia (nieefektywne)

#### Rekomendacje R&D:
1. **PILNE:** Opublikować tabelę wymagań systemowych dla każdej wersji AMODIT
2. Rozbudować opisy funkcji w Help - dodać przykłady użycia, kontekst biznesowy
3. Oznaczyć funkcje płatne (pogrubienie, kolor, ikona)
4. Udostępnić archiwalne wersje instalatorów dla instalatorów
5. Stworzyć sekcję "Best Practices" i "Use Cases" w dokumentacji

---

### 5. Portal Pracowniczy / Licencje Okazjonalne - POTRZEBA BIZNESOWA

**Klienci zgłaszający:** NIDEN, Horn Distribution, Grupa Pracuj.pl

#### Potrzeba:
- **Dostęp dla użytkowników zewnętrznych** (pracownicy tymczasowi, klienci) z ograniczonym zakresem
- **Licencje okazjonalne** - użytkownicy logujący się 1-2 razy w roku (wnioski urlopowe, delegacje)
- **Atrakcyjny model cenowy** - kluczowy czynnik decyzyjny dla rozszerzenia na HR

#### Konkretne scenariusze:
- **NIDEN:** Portal dla pracowników tymczasowych z możliwością składania wniosków urlopowych
- **Horn Distribution:** ~200 pracowników minus 75 obecnych licencji - potrzeba modelu okazjonalnego
- **Grupa Pracuj.pl:** Portal pracowniczy z wnioskami kadrowymi

#### Rekomendacje R&D:
1. Stworzyć nowy typ licencji: "Użytkownik okazjonalny" / "Portal pracowniczy"
2. Model cenowy: limit dokumentów/miesiąc lub roczny abonament
3. Funkcjonalność: okrojony widok danych, możliwość składania wniosków, brak pełnego dostępu
4. Priorytet: Q1-Q2 2026 (duży potencjał sprzedażowy)

---

### 6. Zarządzanie Dostępami i Uprawnieniami

**Klienci zgłaszający:** NIDEN, AmRest

#### Problemy:
- **Brak raportów kontrolnych uprawnień** (NIDEN)
- **Brak reguły na przyznawanie dostępu do raportów** (NIDEN)
- **Automatyczne czyszczenie uprawnień** - potrzeba narzędzi do wykrywania nieaktywnych użytkowników (AmRest)
- **Trudności w zarządzaniu dostępami** - ryzyko cyberbezpieczeństwa (NIDEN)

#### Rekomendacje R&D:
1. Stworzyć gotowe raporty kontrolne uprawnień (dla dużych klientów)
2. Dodać regułę na przyznawanie dostępu do raportów
3. Narzędzie do automatycznego wykrywania i czyszczenia nieaktywnych użytkowników
4. Panel audytu dostępów (kto, kiedy, do czego miał dostęp)

---

### 7. KSeF i Integracje

**Klienci zgłaszający:** Lewiatan, HAWE, AGRO TUW, Horn Distribution, Infor

#### Problemy zgłaszane przez klientów:
- **Problem mapowania pól KSeF z API Comarch** - oczekiwanie na odpowiedź deweloperów (Lewiatan)
- **Certyfikaty zamiast tokenów** - pytanie czy obsługiwane? (NIDEN)
- **Zmiany formatu faktury w 2026** - potrzeba utrzymania zgodności (NIDEN)
- **Model pobierania faktur z KSeF** - SAP → AMODIT → SAP vs KSeF → AMODIT → SAP (Horn Distribution)

#### Rekomendacje R&D:
1. Priorytet: odpowiedź na pytanie Lewiatana o mapowanie pól KSeF z Comarch
2. Potwierdzić obsługę certyfikatów (nie tylko tokenów)
3. Monitorować zmiany formatu KSeF i zapewnić zgodność

---

### 8. Podpis Kwalifikowany na macOS

**Klienci zgłaszający:** Holcim

#### Potrzeba:
- Holcim oczekuje możliwości obsługi podpisów kwalifikowanych na Mac

#### Rekomendacje R&D:
1. Zapewnić wsparcie dla podpisów na macOS

---

### 9. Monitoring i Wydajność

**Klienci zgłaszający:** RESINVEST, Polpharma

#### Problemy:
- **Dekretowanie faktur "strasznie długo trwa"** (RESINVEST)
- **Brak monitoringu integracji** z Signius (Polpharma)
- **Wydajność jako bloker rozwoju** (RESINVEST)

#### Rekomendacje R&D:
1. Priorytet: analiza wydajności dla RESINVEST (już zlecona)
2. Rozważyć narzędzie do monitoringu integracji z partnerami zewnętrznymi
3. Panel diagnostyczny dla administratorów (planowany w roadmapie 2026)

---

## II. KWESTIE WYNIKAJĄCE Z KONTEKSTU (nie wprost wskazane)

### 1. Problem Adopcji Nowych Funkcji

**Obserwacja:**
- Klienci używają AMODIT w **bardzo ograniczonym zakresie** (PGE Obrót - tylko podpisy, Horn Distribution - tylko faktury)
- **AmRest nie przeszedł na nowy moduł raportowy** mimo 5 lat
- **Brak wiedzy o możliwościach** produktu (PGE, Horn, Coral Travel)

#### Przyczyny:
- Brak czasu i zasobów po stronie klienta
- Niewystarczający onboarding
- Brak przykładów use case i best practices
- Komunikacja skupiona na nowych funkcjach, nie na edukacji

#### Rekomendacje R&D:
1. **Onboarding użytkowników** - interaktywne tutoriale, guided tours
2. **Biblioteka use cases** - przykłady zastosowań dla różnych branż
3. **In-app suggestions** - podpowiedzi "Czy wiesz, że możesz...?"
4. **Webinary i szkolenia** - regularne sesje edukacyjne
5. **Copilot jako przewodnik** - AI sugerujące optymalizacje procesów

---

### 2. Nowe GUI (2025) - Opór Użytkowników

**Obserwacja:**
- **Lewiatan:** Silna dezaprobata kluczowego administratora, obawa przed "szokiem" użytkowników
- **AmRest:** Klienci zgłaszają drobne bugi wizualne (kolory menu, full czarny kolor)

#### Przyczyny:
- Zbyt rewolucyjna zmiana (nie ewolucyjna)
- Brak przygotowania użytkowników
- Brak opcji stopniowego przejścia

#### Rekomendacje R&D:
1. **Tryb kompatybilności** - opcja "klasycznego" widoku dla konserwatywnych klientów
2. **Stopniowe wprowadzanie** - możliwość włączania nowego GUI per moduł
3. **Szkolenia i materiały** - dedykowane dla administratorów przed wdrożeniem
4. **Feedback loop** - szybkie reagowanie na zgłoszenia wizualne

---

### 3. Statystyki i Analityka Systemowa

**Obserwacja:**
- **AmRest:** Brakuje rozbudowanych statystyk adopcji, które były w starszych wersjach
- **NIDEN:** W niektórych wersjach interfejsu brakuje zakładki statystyki

#### Potrzeba biznesowa:
- Klienci chcą mierzyć adopcję systemu
- Analiza wykorzystania procesów
- Identyfikacja wąskich gardeł

#### Rekomendacje R&D:
1. Przywrócić i rozbudować moduł statystyk
2. Dashboard adopcji dla administratorów
3. Raporty wykorzystania procesów, użytkowników, dokumentów
4. Integracja z Power BI (Open Data Protocol)

---

### 4. Komunikacja i Powiadomienia

**Obserwacja:**
- **Lewiatan:** Pomysł powiadomień mobilnych (push notifications) dla krytycznych spraw
- **PGE Obrót:** Brak widoczności powiadomień/przypomnień w diagramie obiegu

#### Rekomendacje R&D:
1. Powiadomienia mobilne (push) dla krytycznych spraw (opóźnienia, eskalacje)
2. Widoczność powiadomień w historii procesu i na diagramie
3. Komunikator wewnętrzny (już w roadmapie)

---

### 5. Globalne Wyszukiwanie Pełnotekstowe

**Obserwacja:**
- **Lewiatan:** Potrzeba globalnego, pełnotekstowego wyszukiwania (jak Google Drive) obejmującego zawartość OCR

#### Rekomendacja R&D:
1. Rozważyć wdrożenie globalnego wyszukiwania w ramach refactoringu
2. Indeksacja treści dokumentów OCR
3. Wyszukiwanie cross-process

---

### 6. Generowanie Dokumentacji Umownej

**Obserwacja:**
- **PGE Obrót:** Konkretne zapytanie o generowanie dokumentacji umownej z szablonów
- **Wartość biznesowa:** Skrócenie procesu o 1-2 kroki

#### Kontekst:
- Funkcjonalność **już istnieje** w AMODIT (mergefields, szablony Word)
- Klient **nie wie**, że może to robić
- **Łatwy quick win** - edukacja, nie development

#### Rekomendacje R&D:
1. Lepsze promowanie istniejących funkcji (dokumentacja, szkolenia)
2. Uproszczenie procesu tworzenia szablonów
3. Biblioteka gotowych szablonów (umowy, wnioski, porozumienia)

---

### 7. Informacja o Wyświetleniu Dokumentu

**Obserwacja:**
- **PGE Obrót:** Potrzeba weryfikacji, czy dokument został faktycznie odebrany i obejrzany (nie tylko dostarczony)
- Informacja jest w TrustCenter, ale **nie wraca do AMODIT**

#### Use case:
- Dowód doręczenia (PIT pracownikom, umowy z klientami)
- Weryfikacja procesów biznesowych

#### Rekomendacje R&D:
1. **Feature request:** Przekazywanie informacji o wyświetleniu z DocuCenter do AMODIT
2. Widoczność w historii procesu
3. Możliwość eskalacji jeśli dokument nie został wyświetlony w X dni

---

### 8. Repozytorium Dokumentów

**Obserwacja:**
- **ORA Warszawa:** Potrzeba digitalizacji akt osobowych adwokatów i aplikantów, akt dyscyplinarnych
- **Horn Distribution:** Archiwizacja umów zamiast dysku sieciowego z OSD
- **Lewiatan:** Potrzeba globalnego wyszukiwania pełnotekstowego

#### Rekomendacje R&D:
1. Rozważyć rozwój funkcjonalności repozytorium dokumentów
2. Priorytet: indeksacja i wyszukiwanie pełnotekstowe
3. Zaawansowane uprawnienia (granularne, dziedziczenie)
4. Integracja z OCR dla automatycznej klasyfikacji

---

### 9. e-Doręczenia - Stabilizacja

**Obserwacja:**
- **Holcim:** Wiele reguł powoduje błędy podczas testów
- **Horn Distribution:** Klient odkrył pismo po 3 miesiącach (problem!)

#### Rekomendacje R&D:
1. Priorytet: stabilizacja e-Doręczeń (zgodnie z umową - miesiąc stabilizacji)
2. Automatyczne powiadomienia o nowych doręczeniach
3. Eskalacje dla nieodebranych doręczeń

---

### 10. Błąd Kopiowania Dokumentów

**Obserwacja:**
- **Horn Distribution:** Powtarzający się błąd podczas wysyłania dokumentów utworzonych na podstawie kopii
- Błąd na różnych obiegach i przeglądarkach (Chrome, Safari)
- **Nie zgłoszony wcześniej** - klient znalazł workaround

#### Rekomendacje R&D:
1. **PILNE:** Zdiagnozować i naprawić błąd kopiowania dokumentów
2. Może dotyczyć również innych klientów (nie zgłaszają, bo mają workaround)
3. Priorytet: wysoki (wpływa na UX)

---

## III. PRIORYTETY DLA R&D (Ranking)

### 🔴 KRYTYCZNE (Q1 2026)

1. **Moduł raportowy - tryb ad-hoc** (AmRest, NIDEN, HAWE)
2. **Protokół MCP** (Rossmann, RESINVEST, Holcim, Grupa Pracuj.pl)
3. **Błąd kopiowania dokumentów** (Horn Distribution)
4. **Dokumentacja - wymagania systemowe** (Lewiatan)
5. **Stabilizacja e-Doręczeń** (Holcim)

### 🟠 WYSOKIE (Q1-Q2 2026)

6. **Portal pracowniczy / licencje okazjonalne** (NIDEN, Horn Distribution)
7. **Uprawnienia do edycji raportów** (NIDEN)
8. **Raportowanie jakości OCR** (Grupa Żywiec)
9. **Raporty kontrolne uprawnień** (NIDEN, AmRest)
10. **Informacja o wyświetleniu dokumentu** (PGE Obrót)

### 🟡 ŚREDNIE (Q2-Q3 2026)

11. **Cykliczne wysyłanie raportów** (AmRest)
12. **Personalizacja widoków raportowych** (HAWE, AmRest)
13. **Globalne wyszukiwanie pełnotekstowe** (Lewiatan)
14. **Monitoring integracji** (Polpharma)
15. **Statystyki adopcji** (AmRest, NIDEN)

### 🟢 NISKIE (Q3-Q4 2026)

16. **Powiadomienia mobilne** (Lewiatan)
17. **Tryb kompatybilności GUI** (Lewiatan)
18. **Biblioteka use cases** (PGE, Horn, Coral)
19. **Onboarding interaktywny** (wszyscy klienci)
20. **Automatyczne czyszczenie uprawnień** (AmRest)

---

## IV. POZYTYWNE SYGNAŁY (Co robimy dobrze)

### ✅ Kierunek AI i Otwartość
- **Wszyscy duzi klienci** pozytywnie oceniają kierunek AI, MCP, Open Data
- Rossmann, Holcim, Grupa Pracuj.pl gotowi jako beta-testerzy

### ✅ OCR - Postęp Widoczny
- Vasco uratowany dzięki Google Gemini
- Grupa Żywiec, Coral Travel chwalą nowy OCR
- Migracje z Skanuj.to przebiegają pomyślnie

### ✅ Stabilność i Wydajność
- Większość klientów nie zgłasza problemów operacyjnych
- System działa stabilnie (Polpharma, Horn, HAWE, Coral)

### ✅ Współpraca i Support
- Klienci chwalą szybkość reakcji (Holcim, Coral, PGE, Grupa Żywiec)
- Dedykowani konsultanci wysoko oceniani (Mateusz Kolakowski, Daniel Reszka)

---

## V. RYZYKA I ZAGROŻENIA

### ⚠️ Ryzyko "Drugiego Orlena"
- **AmRest** może wymagać osobnej linii produktu jeśli nie przejdzie na nowy moduł raportowy
- Koszt utrzymania starych funkcji rośnie

### ⚠️ Opór przed Nowym GUI
- **Lewiatan** - silna dezaprobata kluczowego administratora
- Ryzyko: negatywny wpływ na morale i efektywność zespołu klienta

### ⚠️ Luki w Dokumentacji
- Klienci on-premises (Lewiatan, AGRO TUW) szczególnie dotknięci
- Ryzyko: frustracja, problemy wdrożeniowe, utrata klientów

### ⚠️ Brak Adopcji Funkcji
- Klienci używają 20-30% możliwości produktu
- Ryzyko: postrzeganie AMODIT jako "narzędzia do podpisów" zamiast platformy

### ⚠️ Konkurencja w AI
- Klienci rozwijają własne rozwiązania AI (Rossmann, Grupa Pracuj.pl, Polpharma)
- Ryzyko: jeśli nie będziemy otwarci (MCP), klienci zbudują alternatywy

---

## VI. REKOMENDACJE STRATEGICZNE

### 1. Priorytet: Moduł Raportowy
- **Dedykowany zespół** do przeprojektowania UX modułu raportowego
- **Cel:** Uproszczenie, tryb ad-hoc, personalizacja
- **Deadline:** Q1 2026 (przed utratą AmRest)

### 2. Przyspieszenie MCP
- **Najwyższy priorytet** - klienci pytają o to na każdym spotkaniu
- **Beta-testerzy gotowi:** Rossmann, Holcim, RESINVEST
- **Deadline:** "Tygodnie, nie miesiące" (Rossmann)

### 3. Dokumentacja i Edukacja
- **Dedykowany technical writer** do rozbudowy dokumentacji
- **Biblioteka use cases** dla różnych branż
- **Webinary i szkolenia** - regularne sesje

### 4. Portal Pracowniczy
- **Nowy typ licencji** - duży potencjał sprzedażowy
- **Pilot:** NIDEN lub Horn Distribution
- **Deadline:** Q2 2026

### 5. Stabilizacja przed Innowacją
- **Naprawić błędy** (kopiowanie dokumentów, e-Doręczenia)
- **Dopracować istniejące funkcje** (raporty, uprawnienia)
- **Potem:** Nowe funkcje

---

## VII. PODSUMOWANIE

Analiza 17 spotkań farmingowych pokazuje, że **kierunek rozwoju AMODIT jest właściwy** (AI, otwartość, stabilizacja), ale **wykonanie kuleje w kluczowych obszarach**:

1. **Moduł raportowy** wymaga pilnej interwencji - ryzyko utraty klientów
2. **MCP** to must-have dla klientów enterprise - przyspieszenie niezbędne
3. **Dokumentacja** to poważna luka - wpływa na adopcję i satysfakcję
4. **Portal pracowniczy** to powtarzająca się potrzeba - duży potencjał biznesowy
5. **OCR** rozwija się dobrze - kontynuować

**Kluczowe przesłanie:** Klienci są zadowoleni z produktu, ale **nie wykorzystują jego pełnego potencjału**. Priorytetem powinno być **uproszczenie, edukacja i stabilizacja**, a dopiero potem nowe funkcje.

---

**Następne kroki:**
1. Priorytetyzacja zadań w backlogu R&D zgodnie z tym raportem
2. Dedykowane zespoły dla: moduł raportowy, MCP, dokumentacja
3. Spotkanie z klientami beta-testerami (Rossmann, Holcim) - MCP
4. Plan migracji AmRest na nowy moduł raportowy (Q1 2026)
5. Audyt dokumentacji i plan rozbudowy (Q1 2026)

---

**Koniec raportu**
