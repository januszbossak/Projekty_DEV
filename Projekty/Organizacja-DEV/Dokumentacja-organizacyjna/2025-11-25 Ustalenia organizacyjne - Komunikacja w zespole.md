# Ustalenia organizacyjne – 2025-11-25 (Komunikacja w zespole)

**Źródło:** Spotkanie "Komunikacja w zespole" (część Designu/Daily)
**Kategorie:** Procesy, Zespół

---

## 1. Proces konsultacji architektonicznych (Rola Piotra)

**Kategoria:** Procesy / Zespół

### Kontekst
Zidentyfikowano powtarzający się problem: deweloperzy (np. Adrian, Mateusz) realizują zadania według własnych pomysłów bez szerszej konsultacji architektonicznej. Prowadzi to do błędów projektowych, długu technologicznego i konieczności refactoringu (przykłady: Komunikator, e-Doręczenia, Moduł Raportowy). Brakuje etapu analizy systemowej przed kodowaniem.

### Ustalenie
Wprowadzamy obowiązkowy etap **analizy systemowej** i akceptacji architektonicznej przed rozpoczęciem prac deweloperskich nad nowymi funkcjonalnościami.

**Status:** ✅ Obowiązuje od 2025-11-25

### Szczegóły
- Każdy nowy pomysł techniczny lub projekt (niezależnie od autora - Marek, Adrian, Ania itd.) musi zostać **skonsultowany i zaakceptowany przez Piotra (Architekta)**.
- Deweloper musi przygotować opis systemowy (jak to ma działać "pod spodem", wpływ na system) przed rozpoczęciem prac.
- Piotr ma być odciążony od bieżących prac deweloperskich/poprawek, aby mieć czas na konsultacje i akceptacje.
- Piotr powinien być włączany w spotkania projektowe (Design) lub opiniować koncepcje asynchronicznie.
- Celem jest uniknięcie "cofania się do projektowania" po wdrożeniu oraz edukacja zespołu (nauka szerszego spojrzenia na system).

### Odpowiedzialny
**Damian Kamiński / Janusz Bossak** – egzekwowanie procesu, angażowanie Piotra.
**Piotr Buczkowski** – weryfikacja i akceptacja rozwiązań.

---

## 2. Podejście do rozwiązań dedykowanych vs ogólnych

**Kategoria:** Standardy / Architektura

### Kontekst
Przykład integracji z KSeF/DocuSign pokazał tendencję do tworzenia dedykowanych, wąskich rozwiązań (np. dedykowana funkcja `CallRest` dla KSeF), zamiast rozwiązań systemowych (np. obsługa OAuth w ogólnym `CallRest`).

### Ustalenie
Należy unikać tworzenia rozwiązań dedykowanych dla jednego klienta/przypadku, jeśli można rozwiązać problem systemowo (np. rozbudowa `CallRest` zamiast nowej funkcji). Nie implementujemy rozwiązań narzuconych przez klienta, jeśli są architektonicznie błędne lub niebezpieczne (np. przechowywanie tokena sesji dla Neuca).

**Status:** ✅ Obowiązuje

---

## 3. Dostęp do transkrypcji spotkań

**Kategoria:** Narzędzia

### Kontekst
Janusz ma problem z pobieraniem pełnych transkrypcji ze spotkań, których nie jest organizatorem (kopiowanie ręczne ucina treść). Blokuje to proces tworzenia notatek i aktualizacji dokumentacji.

### Ustalenie
Aby umożliwić pobieranie transkrypcji, Janusz (oraz inne osoby potrzebujące dostępu) będą dodawane jako **współorganizatorzy** w opcjach spotkania Teams.

**Status:** 🔍 Do weryfikacji (testowane na bieżącym spotkaniu)

### Odpowiedzialny
**Kamil Dubaniowski / Organizatorzy spotkań** – dodawanie Janusza jako współorganizatora.
