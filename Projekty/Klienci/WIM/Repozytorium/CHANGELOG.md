# CHANGELOG – Repozytorium

---

## 2025-07-30 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-07-30 Notatka projektowa 2025-07-30 Repozytorium - nowy wzor.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-07-30%20Notatka%20projektowa%202025-07-30%20Repozytorium%20-%20nowy%20wzor.md)

**Kategoria:** #Architektura

**1. Definicja i Filozofia Repozytorium**
- ✅ **Zatwierdzone:** Utrzymujemy koncepcję **dokument = sprawa**
  - Repozytorium to nakładka (widok) organizująca sprawy w strukturę drzewiastą
  - Sprawa może być podpięta do wielu węzłów jednocześnie
  - Fizyczny plik w sprawie, w repozytorium "link"
- ❌ **Odrzucone:** Repozytorium plików ("worek na dokumenty") niezależny od spraw
- ⏸️ **Punkt otwarty:** Oczekiwanie na formalne wymagania od Piotra Murawskiego

**Kategoria:** #Funkcjonalność

**2. Struktura i Uprawnienia**
- 💡 **Propozycja:** Model hybrydowy struktur
  - Struktura Działowa (domyślne foldery działów)
  - Struktura Udostępniona (foldery explicite udostępniane użytkownikom/grupom)
  - Struktura Specjalna (np. JRWA)
- 💡 **Propozycja:** Rozdzielenie uprawnień
  - Dostęp do folderu (węzła) ≠ dostęp do spraw w nim
  - Użytkownik widzi tylko sprawy, do których ma uprawnienia z procesu
  - Wyjątek: Administratorzy repozytorium/JRWA

**3. Obsługa JRWA (Jednolity Rzeczowy Wykaz Akt)**
- 💡 **Propozycja:** JRWA jako osobny typ repozytorium/węzła (włączany w konfiguracji)
- **Funkcjonalności:**
  - Struktura Roczna (główny węzeł = Rok)
  - Import/Eksport struktury klasyfikacji (XML)
  - Wygaszanie starych roczników (read-only)
  - Dziedziczenie parametrów (symbol, kategoria A/B5/B10) z folderu na sprawy
- **Techniczne:** Mechanizm "Formularza Folderu", funkcje reguł `GetRepositoryParams`
- ⏸️ **Punkty otwarte:**
  - Widoczność JRWA (dla wszystkich vs tylko kancelaria/archiwum)
  - Integracja z e-Archiwum (na razie MVP: eksport offline)
- ⚠️ **Uwaga:** JRWA NIE jest rozważane w kontekście klienta WIM (admin. publiczna)

**4. Parametryzacja folderów**
- 💡 **Propozycja:** Definicje atrybutów dla węzłów repozytorium
  - Opisywanie folderów (np. "Kategoria archiwalna: A")
  - Reguły na sprawach mogą odczytywać wartości z węzła nadrzędnego

**Kategoria:** #Roadmap

**Propozycja podziału na pakiety:**
- **MVP 1: WIM - Repozytorium Podstawowe**
  - Uelastycznienie struktury folderów (poza sztywne działy)
  - Mechanizm udostępniania folderów (Wybierz osoby/grupy)
  - Rozdzielenie uprawnień (Folder vs Sprawa)
- **MVP 2: Obsługa JRWA**
  - Węzeł typu JRWA (struktura roczna)
  - Parametryzacja folderów (kategorie archiwalne)
  - Dziedziczenie parametrów na sprawy
  - Eksport/Import struktury

**Do dalszej dyskusji:**
- Wymagania klienta (WIM) na piśmie przed deweloperką
- Warsztaty archiwizacyjne z partnerem zewnętrznym (specjaliści EZD)

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)
**Kategoria:** #Decyzja

- **Rozbieżność w rozumieniu pojęcia "Repozytorium"** między zespołem R&D a klientem (Piotr Murawski)
- **Decyzja:** ⏸️ Odroczone - wstrzymanie prac koncepcyjnych do czasu otrzymania jasnej definicji i wymagań od klienta

---

