# Notatka projektowa – 2025-12-15 – Błędy z ładowaniem formularza po aktualizacji

**Data:** 2025-12-15
**Typ:** Spotkanie projektowe
**Temat główny:** Błędy z ładowaniem formularza po aktualizacji
**Źródło:** [Transkrypcja](../Transkrypcje/oczyszczone-archiwum/2025-12-15%20Błędy%20z%20ładowaniem%20formularza%20po%20aktualizacji%20-%20transkrypcja%20-%20część%201.md)

---

## 1. Problem z ładowaniem formularza po aktualizacji u klienta AgroUbezpieczenia

**Komponent:** Deployment / Konfiguracja systemu

### Kontekst i cel

Klient onpremise (AgroUbezpieczenia) zgłosił problem z ładowaniem formularza po aktualizacji systemu AMODIT. Wersja przed aktualizacją: 250630.87 (lub 104), wersja po aktualizacji: 250630.132. Wersja obecna: 250331.136. Baza została odtworzona z backupu z 28.11 (zawiera dane z 27.11), więc wersja bazy jest zgodna z wersją przed aktualizacją. Aktualizacja była robiona zgodnie z przyjętym standardem, pliki nie miały atrybutu "blocked". Problem występuje również przy próbie załadowania zakładek systemowych.

### Zidentyfikowane ryzyka

- Problem może dotyczyć wielu klientów onpremise używających podobnej konfiguracji
- Windows Defender może blokować kompilację i ładowanie bibliotek DLL
- Dodanie dodatkowej witryny na serwer może powodować konflikty z bibliotekami w GAC
- Aktualizacja innych aplikacji (np. Symfonia F-K) może wpływać na działanie AMODIT

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Przywrócenie poprzedniej wersji aplikacji | Cofnięcie aktualizacji do działającej wersji | ❌ Odrzucona – nie rozwiązuje problemu, nawet starsza wersja nie działa po przywróceniu |
| Przywrócenie bazy z backupu | Powrót do stanu przed aktualizacją | ❌ Odrzucona – Piotr Buczkowski: "Nie ma sensu przywracać bazy, co najwyżej przywrócić starą wersję AMODIT" |
| Zmiana ustawień Windows Defender | Dodanie katalogu AMODIT do wyjątków | ⏸️ Odroczona – klient twierdzi, że defender został wyłączony, ale problem nadal występuje |
| Usunięcie plików Newtonsoft z GAC | Ręczne usunięcie przekompilowanych plików DLL z GAC | ✅ Wybrana – rozwiązanie problemu |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Problem został rozwiązany przez usunięcie przekompilowanych / zcachowanych plików DLL z GAC (Global Assembly Cache). Okazało się, że pliki Newtonsoft.JSON w GAC były corrupted i mechanizm .NET tego nie wykrył. Usunięto pliki Newtonsoft* z `C:\Windows\assembly\GAC_64`, po czym ponownie uruchomiono wszystko i system zaczął działać.

**Szczegóły techniczne:**
- Lokalizacja problemu: `C:\Windows\assembly\GAC_64\Newtonsoft.Json\` oraz `C:\Windows\assembly\gac_msil\newtonsoft.json\`
- Narzędzie diagnostyczne: `resmon.exe` (Resource Monitor) – użyto do znalezienia aktywnie używanych plików .dll
- Mechanizm: Windows kompiluje DLL z AMODITa i kopiuje skompilowaną wersję do GAC
- Problem: Przekompilowane pliki w GAC były corrupted, co powodowało błędy przy przypisaniu do property w JObject
- Błędy występowały w: `caselist` i `usercontroler` (pierwsze przypisanie do obiektu)

**Dodatkowe ustalenia:**
- Postawienie aktywnej dodatkowej witryny psuje ustawienia newtonsoftowe (do działającej produkcji dodano instancję test) i pojawia się ten sam błąd
- Mariusz Piotrzkowski i Tomasz Kalinowski będą sprawdzać zachowanie witryn po restarcie w trybie (1 lub 2), (1 i 2), przy wrzuceniu kolejnej witryny na serwer
- Problem wystąpił również u klienta PCBC w podobnych okolicznościach (aktualizacja konektora i Symfonii F-K do 2026)

### Ograniczenia / Poza zakresem

- Nie ma potrzeby wskazywania wersji Newtonsoft w web.config – aplikacja powinna korzystać z pliku newtonsoft.json.dll w swoim katalogu, a nie szukać podanej wersji w GAC
- Wartość z `<applicationSettings>` jest niepotrzebna i nie powinna być w pliku wzorcowym

### Zadania / Dalsze kroki

- **Mariusz Piotrzkowski:** Napisanie artykułu jak znajdować i wykrywać takie problemy (użycie resmon.exe)
- **Mariusz Piotrzkowski, Tomasz Kalinowski:** Sprawdzenie zachowania witryn po restarcie w trybie (1 lub 2), (1 i 2), przy wrzuceniu kolejnej witryny na serwer
- **Piotr Buczkowski:** Poprawa plików wzorcowych web.config – usunięcie błędnych wpisów `<dependentAssembly>` i `<applicationSettings>` dla Newtonsoft
- **Piotr Buczkowski:** Rozważenie dodania sprawdzania do check config w AMODITDatabaseAdmin (nie pomyślał, że ktoś z tego korzysta)

### Punkty otwarte

- Czy Windows Defender rzeczywiście był przyczyną problemu, czy tylko współwystępował? (klient twierdzi, że został wyłączony, ale problem nadal występował)
- Czy aktualizacja Symfonii F-K do 2026 może wpływać na działanie AMODIT? (Xape twierdzi, że może mieć wpływ, ale na razie to nic potwierdzonego)
- Czy można opracować repro steps do sprawdzenia problemu z i bez Windows Defendera?
- Czy problem występuje u innych klientów onpremise, którzy mają podobną konfigurację?

---

## 2. Poprawka w web.config – usunięcie błędnych wpisów dla Newtonsoft

**Komponent:** Deployment / Konfiguracja systemu

### Kontekst i cel

W pliku web.config u klienta AgroUbezpieczenia znajdowały się błędne wpisy dotyczące Newtonsoft.JSON, które powodowały problemy z ładowaniem biblioteki. Aktualnie Newtonsoft ma wersję 13.0.3.0, a w web.config był wpis wskazujący na wersję 12.0.0.0.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Usunięto z web.config:
- Wpis `<dependentAssembly>` z `<bindingRedirect>` dla Newtonsoft.Json wskazujący na wersję 12.0.0.0
- Wpis `<applicationSettings>` dla Newtonsoft (niepotrzebny)

**Szczegóły techniczne:**
- Format błędnego wpisu: `<dependentAssembly>` `<assemblyIdentity name="Newtonsoft.Json" publicKeyToken="30ad4fe6b2a6aeed" culture="neutral" />` `<bindingRedirect oldVersion="0.0.0.0-13.0.0.0" newVersion="13.0.0.0" />` `</dependentAssembly>`
- Problem: Aplikacja szukała podanej wersji w GAC zamiast korzystać z pliku newtonsoft.json.dll w swoim katalogu
- Rozwiązanie: Usunięcie wpisu – aplikacja automatycznie korzysta z DLL w swoim katalogu

### Ograniczenia / Poza zakresem

- Nie ma potrzeby wskazywania wersji Newtonsoft w web.config
- Ważne: W `<bindingRedirect>` w `newVersion` nie powinna być nowsza wersja niż faktycznie dostępna w aplikacji

### Zadania / Dalsze kroki

- **Piotr Buczkowski:** Poprawa plików wzorcowych web.config (web.config.safe.txt) – usunięcie błędnych wpisów, aby nie były wgrywane u innych klientów
- **Piotr Buczkowski:** Rozważenie dodania sprawdzania do check config w AMODITDatabaseAdmin (używane przy każdej aktualizacji na serwisie)
- **Zespół serwisowy:** Ręczna poprawa u innych klientów, gdzie były wgrywane pliki na podstawie web.config.safe.txt

### Punkty otwarte

- Czy przyszła aktualizacja automatycznie poprawi to u klientów (check config z DBAdmina), czy trzeba ręcznie wszędzie poprawiać?

