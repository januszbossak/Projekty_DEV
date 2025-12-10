# Planowanie Sprintu – 2025-12-01

> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-09

**Sprint:** (do ustalenia)
**Okres:** (do ustalenia)

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Status | Uwagi |
|-------|--------|-------|
| Indeksacja (raporty tabelaryczne) | 🔄 W trakcie | Mateusz kontynuuje, pilny temat. |
| Joby (job monitoring/document expiration) | ✅ Ukończone (testy) | Marek przetestował, wdrożenie na domówkę jutro, produkcja w przyszłym tygodniu. |
| Comarch Hub | 🔄 W trakcie | Bloker zszedł w piątek, Łukasz Brocki kontynuuje. |
| Dokumentacja powdrożeniowa AI | ✅ Ukończone (PoC) | Proof of Concept, że "da się". |
| MCP (AI for client services) | ⏸️ Odroczone | Brak klienta, niższy priorytet. |
| Audyt baz danych (Azure) | 🔄 W trakcie | Łukasz Brocki ma zająć się rozwojem/poprawkami do Azure (onboarding/dezaktywacja baz danych). |

---

## 2. Plany na sprint

### Repozytorium plików (Projekt WIM)

**Kontekst i cel:**
Dowiezienie funkcjonalnego Repozytorium plików dla klienta WIM w ramach MVP, z planem dalszego rozwoju.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Realizacja MVP 2 (zarządzanie strukturą, upload, download, podgląd, uprawnienia, instalacja u klienta). | **Filip**, **Ania**, **Adrian** | | |
| (Opcjonalnie) Historia zdarzeń (audyt trail) | (do ustalenia) | | |

**Szczegóły techniczne** (jeśli istotne):
- Aplikacja będzie odrębna, wpięta w **AMODIT** (podobnie jak Komunikator).
- Wykorzystanie AI do wytwarzania.
- Oddzielna baza danych (dyskusja na temat tego, czy w tej samej instancji co **AMODIT**, czy oddzielna dla każdego klienta).
- Metadane (MVP): nazwa pliku (techniczna i wyświetlana), opis, tagi.
- Uprawnienia (MVP): dziedziczone z najwyższego poziomu (przestrzeń repozytorium), bez zrywania dziedziczenia.

**Decyzje podjęte przy planowaniu:**
- Cel sprintu ustalony jako tryb dokonany: Repozytorium będzie zrobione i zainstalowane u klienta, realizujące zdefiniowane funkcjonalności.

**Ryzyka:**
- Akceptacja uproszczonego modelu uprawnień przez WIM.

---

### JRWA (Jednolity Rzeczowy Wykaz Akt)

**Kontekst i cel:**
Dostarczenie funkcjonalności JRWA dla klienta LOT.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przygotowanie struktury po stronie bazy danych. | **Marek** | | |
| Osadzenie w polu `Odnośnik` (zewnętrzne źródło) i możliwość wyboru kategorii JRWA. | **Marek** | | |
| Przekazanie paczki do instalacji dla LOTu. | **Marek** | | |

**Szczegóły techniczne:**
- JRWA będzie implementowane jako struktura 4-poziomowa.
- Klasyfikacja obiektów (np. nieruchomości) poprzez pole typu "słownik" w sprawie **AMODIT**.
- Marek będzie realizował część frontendową.
- Tylko na poziomie sprawy, nie dla raportów w obecnym etapie.

---

### Standardy tabel i UI/UX Edytora Procesów

**Kontekst i cel:**
Ujednolicenie wyglądu i zachowania tabel, oraz poprawa użyteczności panelu prawego w Edytorze Procesów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Spisanie wytycznych dla standardowego wyglądu tabel w Design. | **Kamil** | | |
| Poprawa istniejących tabel zgodnie z wytycznymi. | **Kamil** | | |
| Przegląd i optymalizacja panelu prawego ustawień pól. | **Kamil**, **Przemek Rogaś** | | Przemek Rogaś ma zająć się ogólnymi bugami w raportach. |
| Naprawa bugów UI/UX (kolory, menu, widoki kompaktowe, mobilne). | **Kamil** | | |
| Ujednolicenie wyglądu pola `Tabela` (zagnieżdżenia). | **Kamil** | | |

**Decyzje podjęte przy planowaniu:**
- Celem jest ustalenie gotowego projektu w pierwszym tygodniu, a realizacja w drugim.

---

### Moduł raportowy – System Reports (WIM)

**Kontekst i cel:**
Dostarczenie kluczowych raportów systemowych dla WIM.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Definicja 5 raportów dla WIM i opis ich celu/funkcjonalności. | **Lukasz Bott**, **Damian** | | |
| Implementacja z wykorzystaniem istniejących danych (ew. przygotowanych źródeł). | | | |

**Szczegóły techniczne:**
- Nowe podejście do raportów systemowych.

---

### Moduł raportowy – Rozszerzenie okna dialogowego dla akcji masowych (Execute before rule)

**Kontekst i cel:**
Umożliwienie interaktywnego zbierania danych od użytkownika podczas masowego uruchamiania reguł z poziomu raportu.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Uruchomienie istniejącej funkcjonalności `Wykonaj przed wykonaniem reguły` w akcjach masowych z raportu. | **Kamil** | | |
| Obsługa zbierania danych z okna dialogowego dla wszystkich zaznaczonych spraw (z pamięci z pierwszej sprawy). | **Kamil** | | |
| Weryfikacja, czy reguły z warunkiem wstępnym nie są podpowiadane w akcjach masowych, jeśli nie są kompatybilne. | **Kamil** | | |

**Szczegóły techniczne:**
- Na początek priorytetem jest poprawne działanie istniejącej funkcji w kontekście masowym.

---

### Integracja z SIEM

**Kontekst i cel:**
Opracowanie wytycznych i implementacja integracji **AMODIT** z systemami klasy SIEM (dla LOTu).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Opracowanie dokumentu z zakresem integracji i wytycznymi. | **Lukasz Bott** | | |

**Szczegóły techniczne:**
- Standardowe rozwiązania dla integracji z systemami SIEM.

---

### Comarch Hub Integration

**Kontekst i cel:**
Uruchomienie integracji Comarch Hub u klienta.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Dokończenie integracji Comarch Hub. | **Lukasz Brocki** | | |
| Testy u klienta (brak środowiska testowego). | **Lukasz Brocki** | | |
| Dokumentacja konfiguracji. | **Lukasz Brocki** | | |

---

### Integracja UPS

**Kontekst i cel:**
Opracowanie i implementacja integracji z UPS.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja funkcji w regułach (wysyłka, status, anulowanie przesyłki). | **Lukasz Brocki** | | |
| Wydruk etykiety. | **Lukasz Brocki** | | |
| Testy u klienta (brak konta testowego). | **Lukasz Brocki** | | |

**Szczegóły techniczne:**
- Brak potrzeby certyfikatów, wszystko przez API.

---

### SignApp Certification

**Kontekst i cel:**
Zakończenie procesu certyfikacji aplikacji SignApp.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przeprowadzenie procesu certyfikacji aplikacji SignApp zgodnie z wymaganiami Apple (poza App Store). | **Adrian** | | |

---

### Dokumentacja powdrożeniowa AI

**Kontekst i cel:**
Opracowanie narzędzia do generowania kompleksowej dokumentacji powdrożeniowej przy użyciu AI.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Określenie zakresu dokumentacji, źródeł informacji, workflow. | **Janusz**, **Mateusz** (wsparcie) | | Wdrożeniowcy (Mateusz Kołakowski) do konsultacji. |
| Ustalenie ostatecznego formatu i szablonu dokumentu. | **Janusz**, **Mateusz** (wsparcie) | | Konsultacje z wdrożeniowcami i klientami. |
| Rozwój narzędzia (na podstawie PoC). | **Mateusz** | | Po zakończeniu indeksacji. |

**Szczegóły techniczne:**
- Konieczność uwzględnienia procesów, ustawień systemowych, integracji, jobów.
- Prawdopodobnie dedykowany tryb **Copilota** do generowania dokumentacji.

---

## 3. Decyzje architektoniczne (ad-hoc)

- **AI Development (Repozytorium):** Budowa jako oddzielna aplikacja wpięta w **AMODIT**, rozwijana z użyciem AI, z oddzielną bazą danych (docelowo być może integracja z główną bazą **AMODIT**).
- **Strategia rozwoju:** Przejście na bardziej skoncentrowane cele sprintu (np. "dokończyć edytor formularza"). Dostarczanie "domkniętych" funkcjonalności (MVP).
- **Zarządzanie poprzez cele:** Wdrożenie metodyki, gdzie cele sprintu są jasno sformułowane w trybie dokonanym.

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Kontekst | Wpływ | Mitygacja | Właściciel |
|---------------|----------|-------|-----------|------------|
| Brak środowiska testowego | Comarch Hub, UPS | Wydłużenie czasu testów, konieczność testowania u klienta. | Testowanie bezpośrednio u klienta. | **Łukasz Brocki** |
| Niespójność wyświetlania kompaktowego | Edytor Procesów | UI/UX błędy w niektórych polach. | Zweryfikować, czy można zweryfikować i poprawić w tym sprincie. | **Kamil** |
| Konflikty w zespole Repozytorium | Integracja Adriana | Potencjalne konflikty między Adrianem a Anią. | Ustalenia wewnętrzne. | **Damian** |
| Brak zadań dla Przemka Rogaś | Edytor Procesów (bugi) | Opóźnienie w naprawie bugów. | Przemek zajmie się bugami z raportów, skupiając się na raportach tabelarycznych. | **Damian** |
| Brak jasności co do obciążenia deweloperów | Ogólne | Ryzyko niedowiezienia celów sprintu. | Ustalenie obciążenia i zobowiązań każdego dewelopera na koniec planowania. | **Janusz**, **Damian** |
| Brak feedbacku od WIM | Komunikator | Opóźnienie w wdrożeniu produkcyjnym. | Damian skontaktuje się offline. | **Damian** |

---

## 5. Organizacja pracy

- **Cel:** Praca w zespołach, każdy zespół ma jasny cel sprintu.
- **Zastępstwo za Piotra (nieobecność):** **Adrian** i **Mariusz** mają obserwować czaty konsultantów i pełnić rolę wsparcia. Janusz ma ich dodać do grupy `duty team`.
- **Zespoły:**
    - Repozytorium: **Filip**, **Ania**, **Adrian**, **Oktawia** (QA).
    - JRWA: **Marek**, **testerki** (do przypisania).
- **Planowanie Sprintu:** W przyszłości przygotowanie do planowania powinno być dokładniejsze, z precyzyjnie zdefiniowanymi celami.
- **Roadmapa:** Janusz chce, aby roadmapa zawierała mniej rzeczy, ale były one dowiezione.
- **Comarch Resto do Kirin:** Planowanie na następny lub kolejny sprint, w zależności od decyzji Neuca.
- **Wyceny:** Wyceny "Kushina" i "rozszerzenie okna dialogowego" do ponownej analizy i aktualizacji estymacji.

---

## Powiązane projekty
- `Klienci/WIM/Repozytorium-plikow-DMS`
- `Klienci/LOT/JRWA`
- `cross-cutting/Design-System`
- `Moduly/Edytor-procesow`
- `Klienci/WIM/Raporty-systemowe`
- `Moduly/Modul-raportowy/Masowe-akcje`
- `Klienci/LOT/Integracjai-SIEM`
- `klienci/Lewiatan/Comarch-HUB`
- `Klienci/LOT/Integracja-UPS`
- `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`
- `Organizacja-DEV/Automatyzacja-dokumentacji-AI`
- `Organizacja-DEV/Dokumentacja-organizacyjna/Narzędzia`
- `Moduly/Ustawienia-systemowe/Zadania-jobs`
- `Moduly/Modul-raportowy/Wydajnosc`
