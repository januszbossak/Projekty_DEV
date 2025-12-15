# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-12-15 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-15 Notatka projektowa - Błędy z ładowaniem formularza po aktualizacji.md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-15%20Notatka%20projektowa%20-%20Błędy%20z%20ładowaniem%20formularza%20po%20aktualizacji.md)
**Kategoria:** #Problem #Decyzja #Architektura

- Problem z ładowaniem formularza po aktualizacji u klienta AgroUbezpieczenia - corrupted pliki Newtonsoft.JSON w GAC powodowały błędy przy przypisaniu do property w JObject
- Rozwiązanie: usunięcie przekompilowanych plików DLL z GAC (`C:\Windows\assembly\GAC_64\Newtonsoft.Json\` oraz `C:\Windows\assembly\gac_msil\newtonsoft.json\`)
- Problem wystąpił również u klienta PCBC - postawienie dodatkowej witryny psuje ustawienia newtonsoftowe
- Poprawka w web.config: usunięcie błędnych wpisów `<dependentAssembly>` i `<applicationSettings>` dla Newtonsoft - aplikacja powinna korzystać z DLL w swoim katalogu, nie z GAC
- Poprawa plików wzorcowych web.config (web.config.safe.txt) - usunięcie błędnych wpisów aby nie były wgrywane u innych klientów
- Rozważenie dodania sprawdzania do check config w AMODITDatabaseAdmin dla błędnych wpisów Newtonsoft
- Mariusz Piotrzkowski napisze artykuł jak znajdować i wykrywać takie problemy (użycie resmon.exe)


