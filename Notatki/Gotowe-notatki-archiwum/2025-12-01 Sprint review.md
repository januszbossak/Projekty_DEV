> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-10

# Sprint Review – 2025-12-01

**Sprint:** (do ustalenia)
**Okres:** (do ustalenia)

---

## 1. Klienci/WIM/Repozytorium-plikow-DMS

### Cel biznesowy

Zapewnienie funkcjonalnego systemu do zarządzania plikami dla klienta WIM, z możliwością zarządzania strukturą folderów, wgrywania, pobierania i podglądu plików.

### Co zaimplementowano

- Możliwość tworzenia nowych przestrzeni (węzłów najwyższego rzędu) i podwęzłów.
- Renaming i usuwanie folderów/węzłów.
- Wgrywanie pojedynczych plików (docelowo drag & drop).
- Podgląd plików.
- Podstawowe wyszukiwanie (filtrowanie po widocznych elementach).
- Spina frontend z backendem.

### Ograniczenia / Known issues

- Pliki wyświetlają się wielokrotnie (bug, prototyp).
- Wyszukiwanie działa tylko po widocznych elementach.
- MVP upraszcza uprawnienia do dziedziczenia z najwyższego poziomu (bez zrywania).

### Feedback z demo

- WIM (Murawski) pozytywnie ocenił prototyp, nie zgłosił zastrzeżeń do uproszczonego modelu metadanych i uprawnień.
- Przemysław Sołdacki: MVP jest okej, ale należy liczyć się z tym, że klient może wymagać bardziej granularnych uprawnień w przyszłości.

### Dalsze kroki

- Dalszy rozwój i eliminacja błędów.
- Zaangażowanie testerek.
- Instalacja u klienta WIM i zebranie feedbacku do końca sprintu.

---

## 2. Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS

### Cel biznesowy

Dostarczenie aplikacji do podpisywania dokumentów na systemie macOS, rozszerzającej możliwości podpisywania.

### Co zaimplementowano

- Wszelkie elementy ustalone w MVP.
- **Nowa funkcjonalność:** Masowe podpisywanie z poziomu raportu (wielokrotne zaznaczenie, opcja "Uruchom aplikację SignApp").
- Podpisywanie jednorazowym kodem/hasłem (wcześniej dwa razy).
- Wizualne informacje zwrotne podczas procesu podpisywania (SignalR).
- Zerowanie certyfikatów.
- Wsparcie dla Szafira.

### Ograniczenia / Known issues

- Brak 100% zgodności funkcjonalnej z wersją SignApp 2 (Windows) – brak wyboru języka, dark mode.

### Feedback z demo

- Przemysław Sołdacki: Pytanie o nazwę aplikacji ("AMODIT SignApp 3") i nazwy przycisków ("Podpisz SignApp") – sugeruje bardziej opisowe nazewnictwo (np. "Podpisz własnym certyfikatem", "Podpisz innym certyfikatem"), aby było bardziej zrozumiałe dla nowych użytkowników.
- Janusz Bossak: Brak zgłoszeń od klientów o niezrozumieniu nazewnictwa.

### Dalsze kroki

- Dalsze udoskonalenia i rozwijanie o brakujące funkcjonalności.
- Bloker: Oczekiwanie na weryfikację konta i subskrypcję Apple Developer ID.
- Temat MVP1 zamknięty.

---

## 3. Moduly/Edytor-procesow

### Cel biznesowy

Poprawa użyteczności i spójności wizualnej Edytora Procesów, w tym wyglądu tabel i panelu prawego, oraz optymalizacja interakcji z użytkownikiem.

### Co zaimplementowano

- **Pole Tabela (Mariusz):**
    - Drobne zmiany w przyciskach w tabeli (np. "Dodaj").
    - Rozwiązano problem z zachodzącym scrollem poziomym.
    - Poprawki CSS Marka.
    - Ikony sortowania bliżej nazw.
    - Mniej agresywny kolor przycisku drag & drop.
    - Zwiększone odstępy między wierszami i kolumnami.
    - Wyróżnienie identyfikatora wiersza jako technicznego (mniej widoczny).
    - Poprawki wyglądu tabeli w tabeli.
- **Edytor Graficzny (Przemysław Rogaś):**
    - Kontekstowe dodawanie sekcji (w miejscu, gdzie są potrzebne).
    - Zmiana nawigacji na `TriSelect` (zamiast powtarzania całej ścieżki).
    - Przeniesienie prawego panelu niżej (nie skacze).
    - Nagłówek prawego panelu (nazwa pola, ikona) zamrożony.
    - Wyszukiwanie przeniesione na prawo, z ikonami, wyszukiwanie po GUID.
- **Edytor listy (Filip):**
    - Kontekstowe dodawanie pól i sekcji.
    - Ikony dla czytelności.
    - Sposób wyboru typu kolumn spójny z edytorem graficznym.
    - Ramki na hover dla edytowalnych pól.
    - Wspólny komponent wyszukiwania.
    - Obsługa wersji językowych (przycisk do włączania/wyłączania kolumn językowych).
- **Reguły tabeli:** Dostępne jako akcja na tabeli (wcześniej w górnej belce). Planowane: kontekstowe wywołanie reguł dla danego pola.
- **Kompilacja/Wersjonowanie:** Niektóre zmiany Przemka Rogaś (Edytor graficzny) nie są jeszcze widoczne w wersji Filipa (Lista pól) z powodu pracy na osobnych gałęziach.

### Feedback z demo

- Janusz Bossak: Pozytywny odbiór, widać poprawę, oczekuje, że wdrożeniowcy polubią nową wersję.
- Klienci zgłaszali drobne bugi wizualne (np. kolory menu, full czarny kolor).

### Dalsze kroki

- Ujednolicenie przycisków (plus/minus, strzałki) w tabelach.
- Zmiany w prawym panelu Edytora graficznego (do potwierdzenia z Kamilem na projekcie).
- Rozwinięcie funkcjonalności reguł tabeli o kontekstowe wywoływanie dla danego pola.
- Poprawki UI/UX dotyczące widoku kompaktowego i mobilnego (rozjeżdżające się pola, brak scrolla poziomego).
- Przemek Rogaś do zajęcia się bugami w module raportowym (skupienie na raportach tabelarycznych).

---

## 4. Moduly/AMODIT Copilot

### Cel biznesowy

Wykorzystanie AI do automatyzacji zadań, takich jak generowanie dokumentacji i integracja z zewnętrznymi systemami.

### Co zaimplementowano

- **Generowanie dokumentacji procesów:**
    - Nowa funkcja w Copilocie, generująca dokumentację dla procesu (np. "OCR v3").
    - Opis procesu, etapy, pola, reguły.
    - Potrafi "wykoncypować" opis nawet bez jawnego opisu procesu.
    - Na razie prototyp.
- **Serwer MCP (Management Control Plane):**
    - **AMODIT** może łączyć się z zewnętrznymi serwerami MCP (np. Comarch).
    - Zewnętrzne aplikacje (Cursor, GPT desktop) mogą łączyć się z serwerem MCP w **AMODIT**.
    - Umożliwia wywoływanie funkcji **AMODIT** (np. pobieranie listy procesów, wyszukiwanie w Wiki) z narzędzi zewnętrznych.
    - Uwierzytelnianie przez token (30-90 dni), powiązany z uprawnieniami użytkownika.

### Ograniczenia / Known issues

- **Generowanie dokumentacji:** Prototyp, wymaga dalszego dopracowania (zakres, kontekst, wygląd dokumentu).
- **MCP:** Użytkownik musi wiedzieć, o co pytać Copilota. Generowanie tokena jest manualne. Nie w pełni zintegrowany z protokołami takimi jak OAuth.

### Feedback z demo

- Przemysław Sołdacki:
    - Brak roadmapy dla generowania dokumentacji, budzi wątpliwości.
    - Problem z User Experience dla Copilota – użytkownicy nie wiedzą, o co mogą pytać (brak sugestii, helpa).
    - Integracja z zewnętrznymi narzędziami AI (np. ChatGPT desktop) przez MCP jest kluczowa dla dużych klientów, którzy mają własne narzędzia.
- Mateusz Kisiel: Potrzeba połączenia z zewnętrznym serwerem MCP klienta (np. Comarch), aby wykorzystywać jego funkcje.

### Dalsze kroki

- **Generowanie dokumentacji:**
    - Definicja zakresu (procesy, ustawienia systemowe, integracje, joby).
    - Definicja źródeł informacji dla AI.
    - Definicja workflow (np. sekwencyjne kroki, a nie jedno kliknięcie).
    - Konsultacje z wdrożeniowcami w celu ustalenia finalnego kształtu.
    - Umieszczenie na roadmapie (Q1 2026).
- **MCP:**
    - Usprawnienie UX/UI dla Copilota (sugestie, help, pokazanie dostępnych funkcji).
    - Dopracowanie uwierzytelniania (np. integracja z OAuth).
    - Spotkanie w szerszym gronie w celu przedyskutowania rozwoju MCP (Mateusz Kisiel, Przemysław Sołdacki, Janusz Bossak, Damian Kaminski).

---

## 5. Moduly/Trust-Center

### Cel biznesowy

Zapewnienie stabilnego działania usług Trust Center i szybkie reagowanie na ewentualne problemy.

### Co zaimplementowano

- Joby zostały przetestowane.
- Wdrożenie na środowisko deweloperskie ("domówka") jutro, na produkcję w przyszłym tygodniu.

### Dalsze kroki

- Hotfixy (jeśli będą) dla dokumentów długo nieużywanych (job przestawiający na wygasłe).

---

## 6. klienci/Lewiatan/Comarch-HUB

### Cel biznesowy

Dokończenie i uruchomienie integracji z Comarch Hub u klienta.

### Co zaimplementowano

- Dokończono integrację.

### Ograniczenia / Known issues

- Brak środowiska testowego, testy bezpośrednio u klienta (Lewiatan).

### Dalsze kroki

- Uruchomienie modułu u klienta.
- Dokumentacja konfiguracji.

---

## 7. Klienci/LOT/Integracja-Global-Express

### Cel biznesowy

Umożliwienie wysyłki przesyłek, śledzenia statusu i innych operacji kurierskich z poziomu **AMODIT**.

### Co zaimplementowano

- Funkcje w regułach dla: otworzenia przesyłki, wezwania kuriera, śledzenia, anulowania przesyłki.
- Dokumentacja (w trakcie).

### Ograniczenia / Known issues

- Brak implementacji opcjonalnych parametrów (MVP).
- Brak wewnętrznego środowiska testowego, testy u klienta (PGL LOT).

### Dalsze kroki

- Testy u klienta.
- Dodanie obsługi licencji.
- Dodanie obsługi UPS.

---

## 8. Organizacja-DEV/Automatyzacja-dokumentacji-AI

### Cel biznesowy

Automatyzacja tworzenia Changeloga i dokumentacji zmian na podstawie zgłoszeń w Azure DevOps.

### Co zaimplementowano

- Automatyczne generowanie Changeloga na Wiki (wewnętrzne i zewnętrzne).
- Mechanizm zbierania danych z Azure DevOps (Backlog) i przetwarzania przez LLM.
- Generowanie dwóch typów artykułów: podsumowanie kluczowych zmian oraz pełna lista zmian.
- Uwzględnienie sekcji bezpieczeństwa w generowanych raportach.

### Dalsze kroki

- Dalsze usprawnienia w promptach (generowanie i weryfikacja).

---

## 9. Klienci/LOT/Integracjai-SIEM

### Cel biznesowy

Integracja **AMODIT** z systemami klasy SIEM (dla LOTu) w celu monitorowania zdarzeń (np. nieudane logowania).

### Co zaimplementowano

- Wytyczne do opracowania.

### Dalsze kroki

- Opracowanie dokumentu z zakresem integracji i wytycznymi.

---

## 10. Organizacja pracy

- **Formuła Sprint Review:** Janusz Bossak zaproponował przejście na review skupione na projektach, a nie na indywidualnych osobach.
- **Testowanie:** Testerki (Oktawia dla Repozytorium) będą zaangażowane we wczesnych etapach developmentu. Barbara i pozostałe testerki spotkają się, aby przypisać zadania testowe.
- **Wsparcie dla konsultantów:** Adrian i Mariusz mają obserwować czaty konsultantów i pełnić rolę wsparcia podczas nieobecności Piotra Buczkowskiego.
- **Roadmapa:** Przemysław Sołdacki podkreśla potrzebę ujęcia wszystkich kluczowych projektów (np. generowanie dokumentacji AI) na roadmapie.
- **Comarch Resto do Kirin:** Planowane na następny lub kolejny sprint, w zależności od decyzji Neuca.
- **Roadmapa:** Janusz Bossak chce, aby roadmapa zawierała mniej rzeczy, ale aby były one dowożone.
- **Główne cele:** Repozytorium, JRWA, raporty systemowe (szczególnie dla WIM).
