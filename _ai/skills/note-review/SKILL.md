---
name: note-review
description: Audyt jakości wygenerowanych notatek - weryfikacja zgodności z transkrypcją, wykrywanie przekłamań i nadinterpretacji, kontrola statusów decyzji
---

# SKILL: Review Notatki (Codex)

## Cel
Pełnisz rolę **Audytora Dokumentacji (QA)**. Twoim zadaniem jest weryfikacja zgodności wygenerowanej notatki z oryginalną transkrypcją spotkania. Szukasz przekłamań, pominięć i błędnych interpretacji statusu decyzji.

Tworzysz raport "Codex", który służy do podjęcia ostatecznej decyzji o akceptacji lub poprawie notatki.

---

## Dane wejściowe
1.  **Notatka projektowa** (plik `.md`) - dokument do sprawdzenia.
2.  **Transkrypcja** (plik(i) `.md`) - źródło prawdy (może być podzielone na części).
3.  **Słownik domenowy** - do weryfikacji terminologii.

---

## Kluczowe obszary weryfikacji

### 1. Statusy decyzji (NAJWAŻNIEJSZE)
AI często ma tendencję do "utwardzania" rzeczywistości. Sprawdź czy:
*   **Luźna propozycja** nie stała się **Zatwierdzoną decyzją (✅)**.
*   **Pomysł do rozważenia** nie stał się **Planem wdrożenia**.
*   **Wątpliwości** ("chyba", "może", "zobaczymy") nie zostały wycięte.

> **Przykład błędu:**
> Transkrypcja: "Damian: *No musimy to jeszcze przegadać z Kamilem, ale wstępnie myślę, że XSLT to dobra droga.*"
> Notatka: "**Decyzja:** ✅ Wdrażamy XSLT. Zatwierdzone przez Damiana."
>
> **W raporcie:** "Statusy decyzji nadmiernie stanowcze – w transkrypcji Damian chce najpierw omówić z Kamilem; w notatce oznaczono jako ✅ Zatwierdzone."

### 2. Kompletność techniczna
Czy notatka zawiera kluczowe szczegóły, które padły w rozmowie?
*   Nazwy tabel, API, parametry, limity.
*   Ograniczenia techniczne (np. "działa tylko na Windows 11", "limit ścieżki 260 znaków").
*   Warunki brzegowe ("działa, ale tylko dla...").

### 4. Weryfikacja nazw projektów (Słownik Projektów)
Sprawdź każdą nazwę projektu użytą w notatce (np. w sekcji "Powiązane projekty" lub przy konkretnych tematach) pod kątem zgodności z plikiem `_SLOWNIK_PROJEKTOW.md`.

*   **Zasada:** Nazwa musi być **identyczna** (ścieżka/wielkość liter) jak w słowniku.
*   **Błąd:** Jeśli nazwa nie istnieje w słowniku (np. `moduly/Raporty` zamiast `Moduly/Modul-raportowy`), zgłoś to.
*   **Sugestia:** W raporcie zaproponuj poprawną nazwę ze słownika lub oznacz jako "Do sklasyfikowania".

---

## Format raportu (Codex) - INSTRUKCJA DLA AGENTA

**Twoim celem jest ułatwienie użytkownikowi szybkiego zatwierdzania poprawek.**

Zamiast prosić o ogólną zgodę, przedstaw **numerowaną listę konkretnych działań**, na którą użytkownik może odpowiedzieć np. "1. Tak, 2. Zmień na X, 3. Tak".

### Struktura Raportu:

1.  **Nagłówek:**
    ```markdown
    # Raport Review (Codex)
    **Notatka:** [Nazwa pliku]
    **Transkrypcja:** [Nazwa pliku(ów)]
    **Data:** [RRRR-MM-DD]
    ```

2.  **Numerowana Lista Problemów i Sugestii (Actionable Items):**
    Każdy punkt musi być konkretny i zawierać propozycję zmiany. Grupuj logicznie.
    W sekcji **Kontekst** podawaj szczegóły z transkrypcji aby uzytkownik mógł oceniec twoje **uzasadnienie**

    *Przykład:*
    > 1. **Błędna nazwa projektu:** "WIM/KAS" -> Zmienić na `Klienci/Allianz/Integracja-CAS`.
    > 2. **Status Repozytorium:** "W trakcie" -> Zmienić na "⚠️ Ekstremalny Priorytet (2-3 dni)". (Transkrypcja: "Absolutny must have...").
    > 3. **Brakujący kontekst (PKF):** Dodać cytat Janusza "Po co?" w kontekście folderów per proces.
    > 4. **Literówka nazwiska:** "Łukasz Borowski" -> Ujednolicić na "Łukasz Brocki".

3.  **Pytanie końcowe:**
    "Proszę o decyzje dla powyższych punktów (np. 'Wszystkie Tak' lub '1. Tak, 2. Nie...')."

---

## Zasady edycji notatki (po zatwierdzeniu)
1.  **Zachowaj oryginalną strukturę** (nagłówki, sekcje).
2.  **Zmieniaj statusy** tam, gdzie wykryłeś nadinterpretację (np. `✅ Zatwierdzone` -> `💡 Propozycja (do weryfikacji)`).
3.  **Dopisuj brakujące szczegóły** w treści sekcji lub jako nowe punkty list.
4.  **Dodaj nagłówek Codex:**
    Na samym początku pliku dodaj blok:
    ```markdown
    > 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu RRRR-MM-DD.
    > **Korekty:** [Krótka lista głównych zmian, np. "Zmieniono status decyzji o XSLT, dodano szczegóły limitów API"]
    ```

## ⚠️ Uwagi do terminologii / Słownik

- [Błędnie użyty termin lub nazwa własna] (jeśli występuje)

## 📂 Weryfikacja Projektów

- [ ] **[Błędna Nazwa Projektu]** → Sugerowana: **[Poprawna Nazwa ze Słownika]** (lub "Brak w słowniku")
- [ ] Wszystkie projekty zgodne ze słownikiem (jeśli brak uwag)

## 💡 Sugestia działań

## Algorytm działania

1.  **Wczytaj Notatkę**.
2.  **Wczytaj Transkrypcję** (wszystkie części).
3.  **Przeczytaj Słownik**.
4.  **Analiza porównawcza:** Czytaj sekcja po sekcji notatki i szukaj pokrycia w transkrypcji.
5.  **Wykrywanie "nadinterpretacji":** Szukaj w transkrypcji słów łagodzących ("może", "chyba", "sprawdźmy", "zastanówmy się") i sprawdzaj, czy nie zniknęły w notatce.
6.  **Generuj Raport.**

---

## Przykład dobrego wpisu w raporcie

> **Repozytorium plików – pominięte wątpliwości (części 5–6):**
> *   Dyskusja czy per-plik można dać tylko zawężenie uprawnień vs. pełne nadawanie niezależne od folderu; Piotr ma wątpliwość co do sensu pełnego oderwania od dziedziczenia – w notatce brak tego śladu.
> *   Struktura folderów: Piotr sugerował, że skracanie nazw (pierwsze znaki) może być mylące; w notatce opisano to jako ustalony fakt.
