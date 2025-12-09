> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-08

# Planowanie Sprintu – 2025-11-21

**Sprint:** Bieżący (Listopad 2025)
**Data:** 2025-11-21

**Powiązane projekty:**
- `Klienci/LOT/JRWA`
- `Klienci/WIM/Repozytorium-plikow-DMS`
- `Klienci/WIM/Komunikator`
- `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`
- `Klienci/LOT/Integracja-UPS`
- `Klienci/LOT/Integracja-Global-Express`
- `Klienci/LOT/Integracjai-SIEM`
- `Moduly/Edytor-procesow/Edytor-formularzy`
- `Moduly/Modul-raportowy`
- `Moduly/Modul-raportowy/Filtry-uzytkownika`
- `Organizacja-DEV/Dokumentacja-organizacyjna`

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Status | Uwagi |
|-------|--------|-------|
| **Komunikator (WIM)** | ✅ Ukończone | Potwierdzone działanie u klienta. Oczekuje na ewentualne uwagi. |
| **Ametystowy** | 🔄 W trakcie | Piotr deklaruje zakończenie dzisiaj. |

---

## 2. Plany na sprint

### JRWA (Jednolity Rzeczowy Wykaz Akt) dla LOT

**Projekt:** `Klienci/LOT/JRWA`

**Kontekst i cel:**
Budowa struktury danych dla JRWA na wzór rozwiązania GUS TERYT. Umożliwienie wyboru klasy z wykazu i dostępu do jej atrybutów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Budowa struktury JRWA (tabela, źródło danych) | **Piotr** | Start przyszły tydzień | - |
| Ewentualne wsparcie/przejęcie tematu | **Mariusz** | - | Jeśli Piotr nie zdąży |

**Szczegóły techniczne:**
- Dedykowana tabela w bazie.
- Mechanizm źródła danych zwracający obiekt/JSON.
- Dostęp w regułach przez notację kropki: `[PoleJRWA].KlasaArchiwalna`, `[PoleJRWA].Nazwa`.

**Decyzje podjęte przy planowaniu:**
- **Brak logiki uprawnień:** Klient (LOT) zadeklarował, że nie chce przypisywać klas do działów (odpowiedzialność), więc prawdopodobnie wszyscy będą widzieć wszystko. Rezygnujemy z implementacji uprawnień w tym etapie.
- **Zarządzanie:** Panel do zarządzania strukturą przesunięty na kolejne sprinty.

---

### Repozytorium Plików (WIM)

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`

**Kontekst i cel:**
Uruchomienie tworzenia folderów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przygotowanie pierwszego endpointu (tworzenie folderów) | **Ania** | 1d (dziś) | - |
| Podpięcie pod endpoint (tworzenie folderów) | **Filip** | - | Czeka na API od Ani |

---

### SignApp (MacOS)

**Projekt:** `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`

**Status:**
Aplikacja gotowa (UI poprawione), ale **niecertyfikowana**.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przekazanie wersji niecertyfikowanej do testów IT | **Filip** | Pon/Wt | - |

**Ryzyka:**
- **Nieobecność Adriana:** Może spowolnić prace backendowe/wsparcie.
- Certyfikacja: Konieczność obejścia zabezpieczeń przy instalacji wersji testowej (akceptowalne dla IT, nie dla dyrektorów).

---

### Integracje (LOT)

**Projekt:** `Klienci/LOT/Integracja-UPS`, `Klienci/LOT/Integracja-Global-Express`, `klienci/Lewiatan/Comarch-HUB`

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja UPS i Global Express | **Łukasz Brocki** | Global Express w tym sprincie | Dane pozyskane |
| Prace przy Comarch Hub | **Łukasz Brocki** | - | - |

---

### Integracja SIEM (LOT)

**Projekt:** `Klienci/LOT/Integracjai-SIEM`

**Kontekst:**
Monitorowanie zdarzeń systemu.

**Plan:**
- Spotkanie techniczne we wtorek (**Łukasz Bott**).
- **Koncepcja:** Zamiast dedykowanej integracji, wystawienie logów systemowych w ustandaryzowanym formacie na porcie sieciowym (SIEM nasłuchuje).

---

### Edytor Formularza i Lista Pól

**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`

**Kontekst:**
Porządkowanie błędów wizualnych i funkcjonalnych (tabela, ikonki).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Porządkowanie pola typu Tabela (rozjechany import, ikonki) | **Mariusz** | - | Warunkowe: Jeśli Piotr weźmie JRWA w całości |

**Dyskusja / Pomysły:**
- **Podgląd reguł:** Potrzeba widoku "Gdzie to pole jest używane?" (lista reguł) w prawym panelu.
- **Reguły tabeli:** Obecnie niedostępne z nowej listy pól - do naprawy.
- **Dodawanie sekcji:** Problem z dodawaniem nowej sekcji z poziomu listy pól (ograniczenia tabeli Ant Design).

---

### Moduł Raportowy

**Projekt:** `Moduly/Modul-raportowy`

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Prace nad indeksami (wydajność) | **Mateusz** | - | - |
| Porządkowanie operatorów daty w filtrach | **Szymek/Przemek** | - | Uporządkowanie logiki ("ostatnie 7 dni" vs "tydzień temu") |

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| **Reprezentacja sekcji w DB** | Edytor formularza | 💡 Do analizy | Postulat zmiany backendu, aby sekcje miały swoją reprezentację w bazie (obecnie redundantny zapis w definicji pola). Ułatwiłoby to zarządzanie pustymi sekcjami. |

---

## 4. Organizacja pracy

- **Zespoły Zadaniowe:** Powrót do koncepcji stałych zespołów celowych.
    - Struktura: 2 zespoły backendowe, 1 frontendowy, testerki przypisane do zespołów.
    - Przykłady: Marek (Trust Center), Mateusz (AI/OCR).