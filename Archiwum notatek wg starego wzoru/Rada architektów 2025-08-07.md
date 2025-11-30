[[Rada architektów 2025-10-14]] [[2025-08-07 czwartek]]
### Spotkanie rady architektów z dnia 7 sierpnia 2025

---

#### 1. Przebudowa panelu konfiguracji integracji w ustawieniach systemowych [[Integracje definiowane]]


- **Ryzyko:**
    - Obecny interfejs konfiguracji integracji jest nieintuicyjny; wyświetla wszystkie możliwe integracje, nawet te nieużywane, co wprowadza chaos.
    - Konfiguracje dla różnych usług (poczta, Active Directory, bazy danych) są rozproszone po całym module ustawień, zamiast być w jednym, dedykowanym miejscu.
    - Nieuporządkowany wygląd panelu negatywnie wpływa na prezentację możliwości systemu potencjalnym klientom.
    - Ukończenie prac nad tym panelem blokuje wdrożenie całego nowego modułu ustawień systemowych.

- **Proponowane rozwiązanie:**
    - Zastosowanie strategii MVP (Minimum Viable Product), aby jak najszybciej dostarczyć funkcjonalną wersję i odblokować dalsze prace.
    - **Interfejs użytkownika (UI):**
        - Główna lista (lewy panel) będzie pokazywać wyłącznie aktywne, skonfigurowane przez użytkownika integracje.
        - Zostanie dodany przycisk "Dodaj nową integrację", który otworzy okno modalne w formie "marketplace". Będą tam przedstawione w sposób graficzny wszystkie dostępne standardowe integracje wraz z krótkim opisem.
        - Integracje wbudowane, które nie wymagają żadnej konfiguracji (np. kursy walut NBP, VIES), zostaną zgrupowane w osobnej, stałej pozycji na liście, np. "Integracje wbudowane".
        - Użytkownik będzie miał możliwość zdefiniowania "integracji własnej" poprzez interfejs, bez konieczności dostępu do bazy danych.
    - **Dalszy rozwój (po MVP):**
        - Przeprowadzenie kompleksowej reorganizacji wszystkich ustawień systemowych.
        - Wprowadzenie logicznego podziału integracji na kategorie biznesowe (np. podpisy elektroniczne, systemy DMS, uwierzytelnianie).
        - Zbadanie możliwości wykorzystania AI do automatyzacji tworzenia konfiguracji dla nowych, niestandardowych integracji na podstawie dostarczonego linku do dokumentacji API (np. Swagger).

- **Decyzja:**
    - Realizujemy projekt w wersji MVP, aby przyspieszyć wdrożenie. Lista integracji zostanie uproszczona, a dodawanie nowych będzie odbywać się przez graficzny "marketplace". Backend na tym etapie pozostaje bez zmian (korzysta z tabeli `parameters`). Pełna reorganizacja ustawień i grupowanie po kategoriach zostaje odłożona na przyszłość jako osobny, większy projekt.

- **Zadania:**
    - **Przemek i Kamil:** Kontynuacja prac nad front-endem zgodnie z ustaleniami dla wersji MVP – czysta lista aktywnych integracji oraz okno "marketplace" do dodawania nowych.

---

#### 2. Ujednolicenie konfiguracji uwierzytelniania (OAuth)

- **Ryzyko:**
    - Obecne konfiguracje metod uwierzytelniania (np. dla poczty Microsoft 365) są często zaszyte w kodzie lub wymagają skomplikowanych wpisów w parametrach systemowych, co utrudnia zarządzanie i skalowanie.

- **Proponowane rozwiązanie:**
    - Stworzenie centralnego repozytorium do zarządzania "Aplikacjami OAuth", działającego podobnie do obecnego mechanizmu nazwanych połączeń do baz danych.
    - W nowym panelu użytkownik definiowałby aplikację (np. "Microsoft Graph API"), podając jej kluczowe parametry (Client ID, Secret, Tenant ID).
    - Następnie, dla tak zdefiniowanej aplikacji, można by generować wiele tokenów dostępowych dla różnych kont i celów.
    - W miejscach konfiguracji poszczególnych integracji (np. poczta przychodząca) użytkownik zamiast wpisywać wszystkie dane, wybierałby z listy wcześniej zdefiniowany token.

- **Decyzja:**
    - Koncepcja jest słuszna, jednak jej wdrożenie nie jest częścią bieżącego zakresu MVP. Zostanie uwzględniona w ramach przyszłej, kompleksowej reorganizacji ustawień systemowych.

- **Zadania:**
    -

---

#### 3. Prośba klienta o eksport dokumentacji pomocniczej

- **Ryzyko:**
    - Klient (VIM) poprosił o możliwość wyeksportowania całej zawartości systemu pomocy do pojedynczego pliku.
    - Spełnienie tej prośby jest problematyczne, ponieważ zawartość pomocy jest generowana dynamicznie i często aktualizowana, przez co statyczny eksport szybko stałby się nieaktualny.

- **Proponowane rozwiązanie:**
    - Odmówić prośbie, tłumacząc, że funkcja nie jest dostępna, a dynamiczna natura treści uniemożliwia prosty eksport.
    - Jeśli klient będzie nalegał, potraktować zlecenie jako pracę niestandardową i przygotować osobną wycenę.

- **Decyzja:**
    - Prośba klienta zostaje odrzucona. Nie ma technicznej możliwości prostego wygenerowania takiego pliku.

- **Zadania:**
    - **Damian:** Poinformuje klienta o braku możliwości eksportu dokumentacji do jednego pliku.