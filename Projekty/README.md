# Indeks Projektów

Ten plik stanowi centralny spis treści i indeks dla wszystkich projektów zarządzanych w tym repozytorium. Każdy wpis odpowiada katalogowi projektu i zawiera krótki opis jego celu.

**Standardy dokumentacji:** Zobacz `ZASADY.md`, `STYL.md`, `SZABLON.md` - jak strukturyzować i aktualizować dokumentację projektów.

---

## Moduły Główne (`moduly`)
*   `Copilot-Baza-wiedzy-AI`
*   `e-Doreczenia`
*   `e-Nadawca` - Integracja z systemem e-Nadawca (Poczta Polska)
*   `Edytor-procesow` - Zintegrowany edytor procesów (podprojekty: Edytor-formularzy, Edytor-diagramu, Matryca-uprawnien, Edytor-szablonow)
*   `Eksport-import-definicji-procesow` - Eksport/import procesów XML, walidacja, konflikty GUID
*   `Modul-raportowy`
*   `Raporty-systemowe` - Zarządzanie raportami systemowymi (dashboardy, prezentacja, "Zapisz jako")
*   `Repozytorium-plikow-DMS` - Moduł repozytorium plików (DMS) - przechowywanie dokumentów w strukturze przestrzeni i folderów
*   `Silnik-regul` - Rozszerzenia silnika reguł (for each...in attachments)
*   `Slowniki` - Obsługa słowników (wewnętrzne, zewnętrzne, hierarchiczne, zagnieżdżone)
*   `Trust-Center`
*   `Ustawienia-systemowe` - Nowy moduł ustawień systemowych (Widok Jobów, konfiguracja integracji)
*   `Wspolna-praca-na-dokumentach-office` - Wspólna praca na dokumentach Office (SharePoint) - zarządzanie sesjami edycji, synchronizacja dokumentów
*   `Zrodla-danych` - Operacje na źródłach danych (Source get/set), nowy typ dynamic

## Projekty Cross-Cutting (`cross-cutting`)
*   `Bezpieczenstwo-pentesty` - Bezpieczeństwo systemu: pentesty, hardening, usuwanie luk, security compliance
*   `Interfejs-sprawy` - UI sprawy, ikonki, pola, podgląd dokumentu (podprojekty: Formularz-sprawy, Historia-sprawy, Historia-aktywnosci-uprawnien, Podglad-dokumentow)
*   `Dostep-bylych-wspolpracownikow` - Zachowanie dostępu do odczytu dla byłych współpracowników sprawy
*   `GTA` (Grant Temporary Access)
*   `Logowanie-delete-case` - Rejestrowanie operacji trwałego usuwania spraw
*   `Logowanie-powiadomien` - Ślad audytowy dla powiadomień e-mail z procesów
*   `Szablony-maili-systemowych` - Zarządzanie szablonami maili, ochrona przed nadpisaniem
*   `Testy-kompatybilnosci-API` - Test snapshotowy do wykrywania zmian w publicznym API kluczowych bibliotek
*   `WCAG` - Dostępność (WCAG), eksperyment z trybem ciemnym (Dark Mode)
*   `Wielospolkowosc` (Multi-tenancy)
*   `Wydajnosc` (Performance)
*   `Wzmiankowanie-w-komentarzach` - Przebudowa logiki @mention (rola reader, dedykowany email)
*   `Zakladka-Do-wykonania` - Konfiguracja wyświetlania zadań dla współpracowników
*   `Zastepstwa-grupy`

## Integracje (`integracje`)
*   `Integracje-REST-multipart`
*   `Podpisy-jednorazowe` - Integracja z systemem podpisów jednorazowych (SIGNIUS / EuroCert)
*   `SharePoint-OAuth`
*   `System-mailowy`

## Projekty dla Klientów (`klienci`)
*   `LOT`
*   `Marba`
*   `PKF`
*   `Polpharma`
*   `Rossmann`
*   `WIM`
  *   `Call-Snippet` - Zmiana nazwy z Call Function na Call Snippet
  *   `Komunikator` - Komunikator wewnętrzny (AMODIT Talk)
  *   `News-Feed-Anonse` - Mechanizm wyświetlania ogłoszeń i newsów na procesach
  *   `Repozytorium` - Repozytorium Plików (DMS)
  *   `Zmienne-globalne` - Źródła danych Static z funkcjami SetEx i Add

## Koncepcje i Pomysły (`koncepcje`)
*   `AI-driven-workflow` - Koncepcja strategiczna: ewolucja AMODIT w kierunku agentów AI
*   `CallFunctionEx`
*   `Okna-dialogowe`
*   `RunAsUser`
*   `Tablica-ogloszen`

## Dokumentacja AMODIT (`dokumentacja`)
*   `Standardy-dokumentacji-Wiki` - Standaryzacja dokumentacji projektowej w Azure DevOps Wiki

## Organizacja Działu DEV (`Organizacja-DEV`)
*   `Automatyzacja-dokumentacji-AI` - Automatyzacja przepływów pracy dokumentacyjnej przy użyciu AI (agenci Claude Code, generowanie notatek, przetwarzanie transkrypcji)

## Inne Projekty
*   `backlog` - Projekt wsparcia i analizy backlogu projektu AMODIT w Azure DevOps.
*   `UC moduł raportowy` - Baza wiedzy dla przypadków użycia (Use Cases) modułu raportowego.
