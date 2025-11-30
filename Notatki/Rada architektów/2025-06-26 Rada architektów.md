

**Powiązane projekty:**
- [[Projekty/Klienci/WIM/News-Feed-Anonse/README|News-Feed-Anonse]] – tematy 1
- [[Projekty/Klienci/WIM/Komunikator/README|Komunikator]] – temat 2
- [[Projekty/Klienci/WIM/Repozytorium/README|Repozytorium]] – temat 3
- [[Projekty/Klienci/WIM/Call-Snippet/README|Call-Snippet]] – temat 4
- [[Projekty/Klienci/WIM/Zmienne-globalne/README|Zmienne-globalne]] – temat 5
- [[Projekty/Moduly/Modul-raportowy/README|Modul-raportowy]] – temat 6
- [[Projekty/cross-cutting/WCAG/README|WCAG]] – temat 7

---

## 1. News Feed i Anonse (dawniej Baza Wiedzy)

**Projekt:** `moduly/Copilot-Baza-wiedzy-AI` (ewolucja koncepcji)

### Kontekst i Problem
Dyskusja nad funkcjonalnością "News Feed" oraz "Anonsów/Ogłoszeń". Pierwotnie łączono to z "Bazą wiedzy", ale zdecydowano o rozdzieleniu pojęć. Celem jest mechanizm wyświetlania ogłoszeń (np. o awariach, zmianach) oraz newsów (np. z bloga amodit.pl) w interfejsie systemu.

### Zidentyfikowane Ryzyka
- Klient (Piotr) może negować podejście oparte na procesach dla funkcjonalności, które uważa za natywne (np. anonse).

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dedykowany moduł "Baza Wiedzy/Newsy" | Budowa osobnego, dedykowanego mechanizmu w kodzie. | ❌ Odrzucona – zbyt duży narzut pracy deweloperskiej na ten moment. |
| Wykorzystanie Bazy Wiedzy (ChromaDB) | Zapisywanie newsów w bazie wektorowej (mikroserwis). | ❌ Odrzucona – brak dostępu "od ręki", konieczność integracji, overkill dla prostych ogłoszeń. |
| Realizacja na procesach (Low-code) | Ogłoszenia to sprawy w procesie "Anonse". News feed wyświetla te sprawy (z odpowiednimi uprawnieniami). | ✅ Wybrana – najszybsza implementacja (konfiguracja, nie kod), elastyczność uprawnień. |

### Decyzja
**Status:** ✅ Zatwierdzone

Funkcjonalność Anonsów i News Feedu zostanie zrealizowana w oparciu o **procesy AMODIT**.
1. "Anonse" to proces, w którym sprawy to poszczególne ogłoszenia.
2. Mechanizm wyświetlania (News Feed) będzie pobierał dane z tego procesu (lub zewnętrznego źródła jak blog) i prezentował je użytkownikowi.
3. Zastosowanie: "obdarcie" sprawy ze zbędnych elementów (formularza, historii), wyświetlanie tylko treści ogłoszenia.

### Zadania
- **Wiktor / Damian Kamiński:** Konfiguracja procesu "Anonse" i mechanizmu wyświetlania (News Feed).

---

## 2. Komunikator systemowy (Czat)

**Projekt:** `klienci/WIM/Komunikator`

### Kontekst i Problem
Potrzeba komunikacji w czasie rzeczywistym w kontekście sprawy (wątki, wzmiankowanie osób). Obecny mechanizm komentarzy wymaga odświeżania strony, co nie spełnia oczekiwań "czatu".

### Zidentyfikowane Ryzyka
- **Wydajnosc:** Ciągły polling (odpytywanie serwera) przez wiele otwartych kart "zabije" serwery.
- **Licencje:** Biblioteki Open Source (np. Matrix) często są na licencji GPL v3, co wymuszałoby udostępnienie kodu AMODIT.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Własna implementacja w AMODIT | Rozbudowa komentarzy o mechanizmy real-time. | ⏸️ Odroczona – ryzyko wydajnościowe, duży nakład pracy. |
| Integracja z gotowym rozwiązaniem (Open Source) | Postawienie osobnego serwera czatu (np. Matrix) i integracja w UI (iframe/api). | 💡 Propozycja wiodąca – pod warunkiem znalezienia licencji MIT. |

### Decyzja
**Status:** ⏸️ Odroczone

Temat "zaparkowany" do czasu zebrania wymagań i znalezienia odpowiedniej technologii (bezpiecznej licencyjnie i wydajnościowo).

### Zadania
- **Zespół:** Research rozwiązań Open Source (licencja MIT) do integracji.
- **Zespół:** Zgłaszanie pomysłów na kanale "Wymagania".

---

## 3. Repozytorium - definicja

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`

### Kontekst i Problem
Rozbieżność w rozumieniu pojęcia "Repozytorium" między zespołem R&D a klientem (Piotr Murawski).

### Decyzja
**Status:** ⏸️ Odroczone

Wstrzymanie prac koncepcyjnych do czasu otrzymania jasnej definicji i wymagań od klienta.

---

## 4. Call Snippet (zmiana nazwy Call Function)

**Projekt:** `koncepcje/CallFunctionEx`

### Kontekst i Problem
Funkcja `CallFunction` w rzeczywistości wstawia kod (snippet) w miejsce wywołania, a nie działa jak klasyczna funkcja programistyczna. Nazwa jest myląca. Dodatkowo rozważano dodanie parametrów (zmiennych).

### Decyzja
**Status:** ✅ Zatwierdzone (koncepcyjnie)

1. Zmiana nazwy z `Call Function` na **`Call Snippet`** (z zachowaniem kompatybilności wstecznej/aliasu).
2. Rezygnacja z dodawania jawnych parametrów na tym etapie (używanie zmiennych wewnątrz snippetu).

---

## 5. Zmienne globalne / Źródła danych "Static"

**Projekt:** `moduly/Zrodla-danych`

### Kontekst i Problem
Brak w AMODIT odpowiednika "zmiennych procesowych" (globalnych dla procesu, np. pula dni urlopowych, budżet, lista sprzętu), które można łatwo edytować z poziomu reguł, a które nie są sprawami (rejestrami).

### Rozważane alternatywy
- Użycie rejestrów (spraw) – odrzucone przez klienta (negatywne skojarzenia, "ciężkie").
- Źródła danych typu "Static" z możliwością edycji (`Set`).

### Decyzja
**Status:** ✅ Zatwierdzone

Rozbudowa **Zewnętrznych Źródeł Danych** (typ "Static" / "Local"):
1. Źródło inicjowane z Excela lub puste (tworzy tabelę w DB).
2. Zablokowanie możliwości usunięcia takiego źródła (ochrona integralności).
3. Implementacja funkcji **`SetEx`** (lub `SetExternal`) oraz `Add`:
   - Jeśli klucz istnieje → `Update`.
   - Jeśli klucz nie istnieje → `Insert` (Add).
4. Umożliwi to budowanie prostej logiki "zmiennych globalnych" (np. zdejmowanie ze stanu magazynowego, aktualizacja budżetu) bez tworzenia tysięcy spraw.

### Zadania
- **[Do ustalenia]:** Implementacja funkcji `SetEx`/`Add` dla źródeł statycznych.
- **[Do ustalenia]:** Zabezpieczenie źródeł statycznych przed usunięciem.

---

## 6. Raportowanie: Heatmapa i Pivot

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem
Dwie potrzeby raportowe:
1. Kolorowanie warunkowe w tabelach przestawnych (Pivot) – gradienty (min/max), własne kolory.
2. Nowy typ wizualizacji – Heatmapa.

### Decyzja
**Status:** ✅ Zatwierdzone

Realizujemy oba tematy:
1. **Rozbudowa Pivota:** Dodanie edycji kolorów w gradientach (użytkownik wybiera kolor dla min/max).
2. **Heatmapa:** Dodanie nowego typu wykresu (bazując na bibliotece AmCharts).

### Zadania
- **Anna Skupińska:** Implementacja rozszerzonego kolorowania w Pivocie i typu Heatmapa.

---

## 7. Tryb ciemny (Dark Mode) - eksperyment

**Projekt:** `cross-cutting/WCAG`

### Kontekst i Problem
Eksperyment z szybkim wdrożeniem trybu ciemnego przy użyciu filtrów CSS.

### Rozwiązanie
Zastosowanie sekwencji filtrów CSS: `contrast(0.8) invert(1) hue-rotate(180deg)`.
- `invert(1)` – odwraca jasność (biały->czarny).
- `hue-rotate(180deg)` – przywraca oryginalne odcienie kolorów (żeby zielony nie stał się fioletowy).

### Punkty otwarte
- Wymaga dopracowania dla obrazków i specyficznych elementów (np. pasek nawigacji), które nie powinny być odwracane (lub odwracane podwójnie).
- Temat do dalszego "pociągnięcia" jako `cross-cutting`.
