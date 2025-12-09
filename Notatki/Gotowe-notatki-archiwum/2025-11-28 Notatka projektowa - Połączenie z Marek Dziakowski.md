> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-09

# Notatka projektowa – 2025-11-28 – JRWA i personalizacja TrustCenter

**Data:** 2025-11-28
**Temat główny:** Implementacja JRWA (LOT), obsługa podteczek, personalizacja wysyłki TrustCenter
**Powiązane projekty:**
- `Klienci/LOT/JRWA`
- `Moduly/Trust-Center`
- `Moduly/Modul-raportowy`

---

## 1. Personalizacja wysyłki e-maili z TrustCenter

**Komponent:** Trust Center / Integracje

### Cel i problem

Niektórzy klienci wyrażają potrzebę, aby e-maile wysyłane przez usługę TrustCenter (np. dokumenty do podpisu) wyglądały tak, jakby pochodziły z ich własnej domeny/serwera pocztowego, a nie z domeny AMODIT lub TrustCenter.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| **Fizyczne przekierowanie przez serwer klienta** | Konfiguracja TrustCenter do wysyłki e-maili przez serwery pocztowe klienta. | ❌ Odrzucona (propozycja Janusza i Marka) |
| **Wykorzystanie istniejącej funkcji personalizacji (aliasów)** | Użycie mechanizmów w AMODIT/TrustCenter, które pozwalają na ustawienie aliasów/personalizację adresu nadawcy e-mail, aby wyglądał na pochodzący od klienta, przy zachowaniu wysyłki z serwerów TrustCenter. | ✅ Wybrana – do weryfikacji |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (do weryfikacji)

- **Weryfikacja istniejącej funkcjonalności:** Należy sprawdzić dokumentację i konfigurację AMODIT (prawdopodobnie w ustawieniach organizacji) pod kątem możliwości personalizacji adresu nadawcy e-mail. Janusz Bossak potwierdza, że taka funkcjonalność istniała (np. dla Adecco, Rossmanna).
- **Odrzucenie fizycznego przekierowania:** Z punktu widzenia technicznego i biznesowego, fizyczne przekierowywanie e-maili przez serwery klienta jest nieopłacalne i ryzykowne:
    - Wysoka złożoność techniczna, konieczność reprogramowania.
    - Potencjalne ryzyko wysłania nieprawidłowych e-maili (spam, pomyłki).
    - Brak gwarancji dostarczenia e-maili (problemy z serwerem klienta, spam).
    - Obciąża klienta (serwer klienta wysyła dużą ilość e-maili).
    - Podważa kontrolę AMODIT nad własną usługą.

### Punkty otwarte

- Znalezienie i udokumentowanie istniejącej funkcjonalności personalizacji adresu nadawcy e-mail w TrustCenter.
- Weryfikacja, czy ta funkcjonalność spełnia wymagania klienta.

---

## 2. Implementacja Jednolitego Rzeczowego Wykazu Akt (JRWA) – LOT

**Komponent:** JRWA / Moduły

### Cel i problem

Wdrożenie systemu JRWA dla klienta LOT, w szczególności rozwiązania kwestii klasyfikacji dokumentów poza standardowym 4-poziomowym schematem, tzw. "podteczek" (5. poziom klasyfikacji) lub przyporządkowania do obiektów (np. nieruchomości).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| **Implementacja "podteczek" (5. poziomu) w strukturze JRWA** | Rozszerzenie struktury JRWA o dodatkowy poziom hierarchii, np. dla nieruchomości, jako podkatalogi klasy JRWA. (Propozycja Kamila, wzorowana na eZD RP) | ❌ Odrzucona |
| **Model elektroniczny: Klasyfikacja przez słownik i raportowanie** | Prowadzenie JRWA na standardowych 4 poziomach. Dodatkowe powiązanie (np. z nieruchomością) realizowane poprzez pole typu "słownik" w sprawie AMODIT. | ✅ Wybrana |
| **Procesy "Teczka JRWA" i "Podteczka JRWA"** | Dwa oddzielne procesy: jeden dla teczek (4-znakowy symbol), drugi dla podteczek (5-znakowy symbol). (Propozycja Janusza) | ⏸️ Odroczona (z uwagi na złożoność i preferencje rozwiązania ze słownikiem) |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (do realizacji)

- **JRWA jako struktura 4-poziomowa:** JRWA będzie implementowane jako struktura 4-poziomowa, zgodna z normatywnymi wymogami.
- **"Sprawa JRWA" (teczka JRWA):** W AMODIT będzie obiekt (proces) nazwany "Sprawą JRWA" (lub "Teczką JRWA"), który będzie reprezentował teczkę aktową i będzie przypisywany do odpowiedniej klasy JRWA.
- **Brak 5. poziomu w strukturze JRWA:** Nie będzie implementowany dodatkowy 5. poziom w strukturze JRWA (np. podteczki dla nieruchomości) jako element klasyfikacji JRWA. JRWA jest normatywne i nie ma pola na własne rozszerzenia strukturalne.
- **Klasyfikacja obiektów przez słownik:** Dodatkowe przyporządkowanie spraw do obiektów (np. konkretnych nieruchomości, komisji) będzie realizowane poprzez pole typu **"słownik" (np. słownik nieruchomości)** w samej sprawie AMODIT. To pole będzie obligatoryjne dla klas JRWA wymagających takiej dodatkowej klasyfikacji.
- **Raportowanie:** Umożliwi to elastyczne raportowanie i zestawianie wszystkich spraw dotyczących danego obiektu (np. nieruchomości), niezależnie od ich klasyfikacji w JRWA, wykorzystując możliwości systemu elektronicznego.
- **Widoki JRWA:** Marek ma zaimplementować JRWA jako pole typu `Odnośnik`, umożliwiające wybór klasy JRWA. W dalszym etapie rozważane jest dodanie widoku drzewa dla JRWA, aby ułatwić wybór użytkownikom niezaznajomionym ze strukturą.

**Szczegóły techniczne:**
- Pole typu `Odnośnik` dla wyboru klasy JRWA.
- Słownik nieruchomości (lub innych obiektów) jako dodatkowe pole w sprawach AMODIT.
- Konieczne zmiany w polu `Odnośnik` w raportach (patrz niżej).
- Numeracja spraw JRWA ma być spójna w ramach klasy.
- Koncepcja "teczka/podteczka" w rozporządzeniu odnosi się do 2 poziomów sprawy AMODIT w ramach JRWA, a nie 2 poziomów klas JRWA.

### Ograniczenia / Poza zakresem

- Nie będzie implementowany dynamiczny system podteczek, który jest przenoszony na każdy rok i jest niezależny od struktury JRWA (wzorem eZD RP).
- Nie będzie dwóch procesów (Teczka JRWA i Podteczka JRWA) na tym etapie.

### Punkty otwarte

- Potwierdzenie interpretacji z archiwistą (Janusz sugeruje).

---

## 3. Raportowanie z pól typu Odnośnik (Link)

**Komponent:** Moduł Raportowy

### Cel i problem

Umożliwienie generowania raportów, które mogą "drążyć" w głąb pól typu `Odnośnik`, podobnie jak to ma miejsce w przypadku pól typu `Tabela`. Obecnie, aby raportować dane z procesu, na który wskazuje pole `Odnośnik`, należy te dane kopiować do sprawy nadrzędnej.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (do realizacji w ramach projektu JRWA)

- **Rozszerzenie funkcjonalności raportowania:** Użytkownik powinien mieć możliwość wyboru pola typu `Odnośnik` w raporcie, a następnie wyboru pól z procesu, na który ten `Odnośnik` wskazuje.
- **Korzyści:** Znaczące uproszczenie tworzenia raportów, eliminacja potrzeby duplikowania danych, poprawa spójności.

**Szczegóły techniczne:**
- Funkcjonalność zostanie wdrożona w ramach prac nad projektem JRWA.

---

## Punkty do dalszej dyskusji (globalne)

- **Wycena Kushina (OAuth2 dla Coloristica):** Do ponownej analizy i aktualizacji estymacji z uwagi na dwie opcje (tylko OAuth2 dla Coloristica vs. pełna integracja z Envelope/Datacom).
- **Zasady prowadzenia Daily:** Janusz zaproponował zmianę formuły Daily na bardziej projektową.
- **Code Review z Copilotem:** Propozycja do dalszego rozwoju.
