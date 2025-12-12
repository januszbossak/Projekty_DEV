# Rada developerów – 2025-12-04

**Data:** 2025-12-04  
**Typ:** Rada developerów  
**Temat główny:** Repozytorium plików - UX uploadu i lokalizacja w menu

---

## 1. Języki i wersje językowe w AMODIT - uporządkowanie

**Komponent:** AMODIT - konfiguracja języków

### Kontekst i cel

Nowy konsultant (Valdemar Modrak) zgłosił uwagi do artykułu na Wiki dotyczącego języków w AMODIT. Punktem wyjścia była niespójność między:
- Wyborem języka w profilu użytkownika (~10 języków)
- Formatami dat i liczb (tylko kilka)
- Wersjami językowymi w definicji procesu (zależne od parametru systemowego `DisplayLanguages`, nie od listy w profilu)

Łukasz Bott zaproponował uporządkowanie: aby lista języków w `DisplayLanguages` była spójna we wszystkich miejscach systemu (profil, logowanie, definicje procesów).

### Decyzja / Ustalenie

**Status:** ❌ Odrzucone

**Uzasadnienie (Janusz Bossak):**
- **Brak wpływu na sprzedaż** - "Dlaczego mam się tym zajmować? Jaki to ma wpływ na sprzedaż? Jaki to ma wpływ na zmniejszenie kosztów?"
- **Brak priorytetu** - "Po co się zajmujemy tym teraz? Komu to przeszkadza?"
- **Działa i będzie działać** - system funkcjonuje, niespójność nie blokuje pracy

**Co zostaje:**
- ✅ Aktualizacja artykułu na Wiki (Łukasz Bott) - opis obecnego stanu z poprawkami konsultanta
- ❌ Żadnych zmian w kodzie AMODIT

### Feedback / Uwagi uczestników

- **Janusz Bossak:** "Mamy ciągle ogon straszny w aktualizacji rzeczy na Wiki. Zaległości jest ogrom, po prostu nie ma co dywagować, poprawić Wiki, niczego w AMODIT dzisiaj nie zmieniamy na ten moment."
- **Damian Kamiński:** "Może trzeba powiedzieć, że człowiek się nudzi. Ja nie mam w co rąk włożyć. Jak ktoś przeszukuje Wiki, to mogę go zatrudnić do wdrożeń."
- **Janusz Bossak (o konsultancie):** "To, że kolega Wiki i daje feedback to jest bardzo dobrze. Niech to robi. Przy okazji się uczy, jeżeli znajduje różnicę to tym lepiej, bo znaczy, że zaczyna rozumieć."

---

## 2. Repozytorium plików - status uploadu i progress bar

**Komponent:** Repozytorium plików (DMS) - upload plików

### Kontekst i cel

Damian Kamiński przedstawił Proof of Concept statusu uploadu plików do repozytorium. Problem: przy wgrywaniu dużych plików (2 GB) użytkownik nie widzi postępu. Filip zaproponował wyświetlanie statusu ładowania.

**Obecne rozwiązanie (PoC):**
- Status wyświetlany po lewej stronie ekranu (kafelek z progress barem)
- Wygląda "jak zrobione przez dewelopera", nieestetycznie
- Komunikaty toastowe (chmurki) w prawym dolnym rogu - przysłaniają się wzajemnie

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Status po lewej stronie | Kafelek z progress barem po lewej (PoC Filipa) | ❌ Odrzucona - "brzydko wygląda" |
| Komunikaty toastowe | Chmurki w prawym dolnym rogu | ❌ Odrzucona - przysłaniają się, znikają za szybko |
| Prawy sidebar z kolejką | Otwarcie prawego panelu z listą uploadowanych plików + progress bary | ✅ Wybrana - wzorowane na sprawie |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

**Rozwiązanie - prawy sidebar z kolejką uploadów:**

1. **Otwarcie sidebara:**
   - Automatyczne otwarcie prawego sidebara w momencie rozpoczęcia uploadu
   - Sidebar wyświetla kolejkę plików do wgrania

2. **Progress bary:**
   - Każdy plik ma własny progress bar (jak na sprawie)
   - Progress bar na szerokości kolumny "Nazwa" - zakolorowywanie na zielono w miarę postępu
   - Po zakończeniu: 100% zielony lub czerwony (błąd)

3. **Zachowanie po zakończeniu - Wersja 1 (preferowana):**
   - Sidebar **pozostaje otwarty** po zakończeniu uploadu
   - Użytkownik widzi podsumowanie: co się załadowało (zielone), co nie (czerwone)
   - Użytkownik **ręcznie zamyka** sidebar (X)
   - Pozwala zweryfikować czy wszystkie pliki wrzucił

4. **Alternatywna Wersja 2 (do rozważenia):**
   - Pliki znikają z sidebara po pomyślnym załadowaniu
   - Sidebar działa jak kolejka - pokazuje tylko to, co jeszcze trwa
   - Zostają tylko błędy (czerwone)
   - Dla pojedynczego pliku (upload < 1s): tylko toast, bez sidebara

5. **Obsługa błędów:**
   - Plik z błędem: czerwony, komunikat przyczyny (za duży, za mały, zerowy rozmiar, niedozwolony typ, przekroczenie limitu z ustawień systemowych)
   - Błędy pozostają w sidebarze nawet po zakończeniu sesji

6. **Sesje uploadów:**
   - Każde wrzucenie plików = osobna sesja
   - Nowa sesja zastępuje poprzednią (nie można wrócić do historii)
   - Podczas uploadu: **zablokowanie** przycisku "Dodaj plik" i drag & drop (wyszarzenie ekranu)

7. **Komunikaty toastowe:**
   - **NIE wyświetlać** podczas gdy sidebar jest otwarty (wzajemnie się przysłaniają)

**Szczegóły techniczne:**
- Mechanizm uploadu: ten sam co na sprawie
- Kolejkowanie: pliki uploadowane w osobnych sesjach, ale wszystkie lecą równolegle
- Limity: uwzględnienie ustawień systemowych + limitów IIS

**Wzorowanie:**
- Progress bary jak na sprawie (pod każdym plikiem)
- Logika znikania plików jak w OneDrive (po pomyślnym zakończeniu znikają, błędy zostają)

### Zadania / Dalsze kroki

- **Filip / Damian Kamiński:** Implementacja prawego sidebara z kolejką uploadów → brak terminu
- **Backend:** Weryfikacja czy błędy z IIS są dostępne do wyświetlenia użytkownikowi → do sprawdzenia

---

## 3. Repozytorium plików - obszar drag & drop

**Komponent:** Repozytorium plików - drag & drop

### Kontekst i cel

Obecne rozwiązanie: pomarańczowy prostokąt na środku ekranu jako obszar do upuszczania plików. Problem: sugeruje użytkownikowi, że musi trafić dokładnie w ten prostokąt, podczas gdy faktycznie można upuścić plik w całym szarym obszarze.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

**Rozwiązanie:**
- **Usunięcie** pomarańczowego prostokąta na środku
- **Obramowanie** całego szarego obszaru roboczego pomarańczową ramką (jak w Claude, Teams, ChatGPT, Gemini)
- **Ikona + napis** na środku: "Upuść pliki tutaj" lub "Upuść pliki aby je przesłać" (jak na sprawie)
- **Animacja:** Opcjonalnie dodać "bounce" (powiększenie) jak na sprawie - dla spójności wizualnej

**Uzasadnienie:**
- Nowoczesne aplikacje (Teams, ChatGPT, Gemini, OneDrive) podświetlają całą przestrzeń, nie tylko fragment
- Użytkownik nie musi celować w środek ekranu
- Spójność z wzorcami UX

---

## 4. Repozytorium plików - usuwanie plików (masowe)

**Komponent:** Repozytorium plików - usuwanie

### Kontekst i cel

Obecne rozwiązanie: można usunąć tylko pojedynczy plik (ikona X). Problem: przy wrzuceniu wielu plików przez pomyłkę, użytkownik musi klikać X na każdym pliku osobno. Nie można usunąć folderu, jeśli zawiera pliki.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Tylko pojedyncze usuwanie | Obecny stan - X na każdym pliku | ❌ Niewystarczające |
| Checkboxy + akcje masowe | Zaznaczanie wielu plików + przycisk "Usuń" | ✅ Wybrana (MVP 2 lub 3) |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja - MVP 2/3

**Rozwiązanie (do implementacji w MVP 2 lub 3):**
- **Checkboxy** przy każdym pliku/folderze (jak w raportach, OneDrive)
- **Checkbox "Zaznacz wszystko"** na górze listy
- **Obsługa klawiatury:**
  - `Ctrl + Click` - zaznaczanie pojedynczych elementów
  - `Shift + Click` - zaznaczanie zakresu (pierwszy + Shift + ostatni)
- **Akcje masowe:** Przycisk "Usuń" pojawia się po zaznaczeniu elementów
- **Checkboxy na hover:** Checkbox pojawia się dopiero po najechaniu na wiersz (jak w OneDrive) - czystszy widok

**Szczegóły techniczne:**
- Wzorowanie na raportach (już mamy checkboxy i "zaznacz wszystko")
- Możliwość rozszerzenia o inne akcje masowe w przyszłości (przenoszenie, kopiowanie)

**Priorytet:**
- MVP 1: Tylko pojedyncze usuwanie
- MVP 2/3: Akcje masowe (jeśli będzie przestrzeń i Filip ma czas)

### Zadania / Dalsze kroki

- **Damian Kamiński / Filip:** Ocena czy jest przestrzeń w MVP 1 na akcje masowe → do decyzji
- **Kamil Dubaniowski:** Konsultacja wzorców UX (checkboxy, Shift+Click) → w trakcie

---

## 5. Lokalizacja Repozytorium w menu - gdzie umieścić?

**Komponent:** AMODIT UI - nawigacja główna

### Kontekst i cel

Pytanie: gdzie umieścić Repozytorium plików w menu AMODIT?
- **Opcja A:** W górnym menu (obok "Do wykonania", "Powiadomienia", "Komunikator")
- **Opcja B:** W obszarach → Moduły (na samym dole)

**Kontekst:**
- Repozytorium spraw jest w "Listy spraw" (sterowane w ustawieniach systemowych)
- Repozytorium plików to nie jest lista spraw, to osobna aplikacja (DMS)

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Górne menu (obok Komunikatora) | Szybki dostęp, zawsze widoczne | ⏸️ Odroczona - obawa przed rozrostem listy |
| Obszary → Moduły (dół) | Ukryte w obszarach, trzeba przewinąć | ❌ Odrzucona - mało wygodne dla kluczowej funkcjonalności |
| Folder "Aplikacje" (nowy) | Pseudo-obszar z aplikacjami: Komunikator, Repozytorium, Timesheet, e-Nadawca, moduł bankowy | 💡 Propozycja Janusza - do rozważenia |
| Przypinanie przez użytkownika | Użytkownik sam decyduje co przypina do górnego menu | 💡 Propozycja Janusza - do rozważenia |

### Decyzja / Ustalenie

**Status:** ⏸️ Odroczona - do przemyślenia w przyszłym tygodniu

**Argumenty za górnym menu:**
- Kluczowa funkcjonalność dla klientów
- Szybki dostęp bez klikania i przewijania
- Spójność z Komunikatorem (też aplikacja)

**Argumenty przeciw górnemu menu:**
- Obawa przed rozrostem listy (kolejne aplikacje: Timesheet, e-Nadawca, moduł bankowy)
- Górne menu miało być przestrzenią dla **zadań i powiadomień** (rzeczy wymagające uwagi), nie dla aplikacji

**Koncepcja "Aplikacje" (Janusz Bossak):**
- Folder "Aplikacje" w menu (jak "Wszystkie procesy")
- Zawiera: Komunikator, Repozytorium, Timesheet, e-Nadawca, moduł bankowy
- To są aplikacje "wmontowane w AMODIT", nie typowe procesy
- Alternatywnie: przypinanie przez użytkownika (każdy przypina co chce)

**Koncepcja przypinania (Janusz Bossak):**
- Górne menu = lista szybkich dostępów konfigurowana przez użytkownika
- Użytkownik przypina co chce (np. Timesheet, Repozytorium)
- Ryzyko: bałagan u użytkownika (długa lista jak wcześniej)

**Obecny stan:**
- Repozytorium jest w górnym menu (obok Komunikatora)
- Sterowane w ustawieniach systemowych (włącz/wyłącz)
- Klient (firma) widział mock-up z Repozytorium w górnym menu

**Obawa (Damian Kamiński):**
- "Jak pokażemy klientowi tutaj, to potem nie pozwolą żeby to schować"
- Raz pokazane w górnym menu = trudno będzie przenieść do obszarów

### Punkty otwarte

- Czy górne menu ma być przestrzenią dla zadań/powiadomień czy dla aplikacji?
- Czy wprowadzić folder "Aplikacje"?
- Czy pozwolić użytkownikom na przypinanie?
- Jak nie dopuścić do rozrostu górnego menu?

### Zadania / Dalsze kroki

- **Zespół:** Przemyślenie koncepcji w przyszłym tygodniu → do decyzji
- **Damian Kamiński:** Przygotowanie argumentów za/przeciw dla każdej opcji → przyszły tydzień

---

## 6. Raporty systemowe - priorytet

**Komponent:** Raporty systemowe

### Kontekst i cel

Łukasz Bott zapytał o status raportów systemowych. Damian Kamiński wyjaśnił priorytety.

### Decyzja / Ustalenie

**Status:** ⏸️ Niższy priorytet

**Uzasadnienie (Damian Kamiński):**
- **Priorytet 1:** Proces faktur dla klienta (firma) - musi działać w lutym
- **Priorytet 2:** Raporty systemowe - analityczne, mogą poczekać
- "Skupiamy się na tym pod kątem [firmy], ale to są tylko i wyłącznie raporty analityczne. To dla mnie ma dużo niższy priorytet niż proces, który oni muszą mieć w lutym gotowy."
- "Nawet jak się go dowiezie za miesiąc czy dwa później, to tutaj to będzie już wynik tego, co jest w systemie. Analiza prezentacja tego, co jest w systemie, a nie czegoś co trzeba zbierać."

**Proces faktur (kontekst):**
- Setki faktur miesięcznie
- Musi być automatyczne pobieranie (nie ręczne drukowanie)
- "Taka kobyła i to leży" - duże ryzyko projektu
- Mateusz i Damian nie mają przestrzeni na inne tematy

**Następne kroki:**
- **Łukasz Bott:** Przygotowanie artykułu na Wiki devowej z opisem raportów systemowych i linkami → w trakcie
- **Damian Kamiński:** Przegląd w wolnej chwili, prawdopodobnie w przyszłym tygodniu → do zaplanowania

---

## Podsumowanie spotkania

**Główne ustalenia:**

1. ❌ **Języki w AMODIT:** Odrzucone - tylko aktualizacja Wiki, bez zmian w kodzie
2. ✅ **Status uploadu:** Prawy sidebar z kolejką, progress bary, obsługa błędów
3. ✅ **Drag & drop:** Obramowanie całego obszaru, usunięcie prostokąta na środku
4. 💡 **Usuwanie masowe:** Checkboxy + akcje masowe w MVP 2/3
5. ⏸️ **Lokalizacja Repozytorium:** Do przemyślenia (górne menu vs obszary vs folder "Aplikacje")
6. ⏸️ **Raporty systemowe:** Niższy priorytet, skupienie na procesie faktur

**Ton spotkania:** Praktyczny, skupiony na UX i priorytetach biznesowych. Janusz Bossak konsekwentnie pytał o wpływ na sprzedaż i koszty. Damian Kamiński prezentował PoC i zbierał feedback.

**Kontekst organizacyjny:**
- Janusz Bossak pracuje nad dokumentacją projektową (do końca tygodnia gotowa)
- Damian Kamiński: "Jestem wrakiem przez ostatnie dni" - duże obciążenie projektem faktur
- Spotkanie z Neuca zaplanowane na później tego samego dnia (uwagi do zmian w AMODIT)
