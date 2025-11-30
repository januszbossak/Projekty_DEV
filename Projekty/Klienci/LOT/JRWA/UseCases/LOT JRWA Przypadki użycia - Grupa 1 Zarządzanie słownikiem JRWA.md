---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) koncentruje się na administracyjnym i technicznym zarządzaniu "słownikiem" JRWA w systemie AMODIT. Celem jest zapewnienie, że system posiada poprawną, aktualną i zgodną z przepisami (dla LOT – **JRWA 1997**) strukturę klasyfikacyjną.

Obejmuje to procesy wykonywane przez **Administratora JRWA** – od początkowego importu i walidacji, przez edycję klas, aż po zarządzanie uprawnieniami i regułami (np. które klasy są "końcowe"). Te przypadki użycia są fundamentem technicznym, który umożliwia użytkownikom merytorycznym (opisanym w Grupie 2) prawidłowe zakładanie `Teczka_sprawy` i klasyfikowanie dokumentów.

### **UC-JRWA-ADM-001 – Import słownika JRWA z pliku (CSV/XLSX)**

**Rola:** Administrator JRWA / Archiwista systemowy

**Cel:** Wczytanie pełnej struktury JRWA z pliku zewnętrznego w celu zainicjowania lub zaktualizowania drzewa klas w systemie AMODIT.

**Opis:** Pozwala zaimportować kompletny Jednolity Rzeczowy Wykaz Akt z pliku dostarczonego przez klienta.

Dla wdrożenia w LOT S.A. plikiem źródłowym jest **"Jednolity rzeczowy wykaz akt PLL LOT SA" stanowiący Załącznik Nr 2 do Zarządzenia Prezesa Zarządu D/30/97/TA z dnia 12 grudnia 1997 r.** (zgodnie z ustaleniami z Kompendium, Rozdział 6).

System waliduje strukturę — sprawdza poprawność symboli, unikalność i hierarchię klas.

Dzięki temu administrator unika ręcznego wprowadzania setek pozycji i zapewnia zgodność z oficjalnym, obowiązującym w LOT źródłem JRWA.

To pierwszy krok przy wdrażaniu modułu JRWA.

### **UC-JRWA-ADM-002 – Przeglądanie i wyszukiwanie klas JRWA (z filtrami uprawnień)**

**Rola:** Każdy użytkownik (pracownik merytoryczny, sekretariat, koordynator kancelaryjny)

**Cel:** Wyszukiwanie i przeglądanie dostępnych klas JRWA w zakresie określonym uprawnieniami użytkownika.

**Opis:** System udostępnia przeglądarkę drzewa JRWA z możliwością wyszukiwania po symbolu, nazwie lub fragmencie opisu.

Zgodnie z logiką opisaną w Kompendium (Rozdział 10), dla zwykłego użytkownika widoczne są **jedynie klasy, w których jego komórka może zakładać `Teczka_sprawy`** lub rejestrować sprawy.

Administrator i archiwista mają wgląd w całe drzewo.

Widok drzewa pozwala poznać kategorię archiwalną, status obowiązywania i hierarchię klas, ale samo przeglądanie nie daje prawa do rejestracji spraw.

### **UC-JRWA-ADM-003 – Zarządzanie klasą JRWA (dodawanie, edycja, wycofanie z datą)**

**Rola:** Administrator JRWA / Koordynator kancelaryjny

**Cel:** Utrzymanie aktualności i poprawności struktury JRWA poprzez możliwość dodawania, modyfikacji lub wyłączania klas z określeniem dat obowiązywania.

**Opis:** Administrator może wprowadzić nową klasę (np. gdy pojawia się nowe zadanie w działalności jednostki), zmienić nazwę istniejącej klasy lub wyłączyć ją z użycia od wskazanej daty.

System przechowuje historię zmian (wersjonuje słownik), dzięki czemu sprawy utworzone wcześniej pozostają przypisane do właściwej wersji klasy.

To zapewnia ciągłość klasyfikacji akt i zgodność z praktykami archiwalnymi.

### **UC-JRWA-ADM-004 – Walidacja struktury drzewa JRWA**

**Rola:** Administrator JRWA / Archiwista

**Cel:** Zapewnienie spójności i poprawności struktury JRWA w systemie.

**Opis:** System automatycznie sprawdza hierarchię i powiązania między klasami — np. czy każda klasa ma istniejącego rodzica, czy nie występują duplikaty symboli lub błędne poziomy.

Walidacja wykonywana jest po imporcie, po edycjach oraz cyklicznie w tle.

Błędy (np. osierocone klasy) są raportowane administratorowi do korekty.

Ta funkcja gwarantuje, że drzewo JRWA w AMODIT pozostaje zgodne z zasadami klasyfikacji dziesiętnej.

### **UC-JRWA-ADM-005 – Definiowanie zakresów operacyjnych JRWA (gdzie wolno zakładać Teczka_sprawy)**

**Rola:** Administrator JRWA

**Cel:** Określenie, w których klasach JRWA i przez które komórki organizacyjne można zakładać **`Teczka_sprawy`** lub przypisywać sprawy AMODIT.

**Opis:** Administrator przypisuje do wybranych klas JRWA tzw. „zakres operacyjny” – czyli informację, że dana klasa jest aktywna dla określonych ról, użytkowników lub działów.

Dzięki temu można kontrolować, że np. dział kadr zakłada `Teczka_sprawy` tylko w klasach `1...`, a dział finansowy – tylko w `3...`.

Funkcja ta pozwala również na odzwierciedlenie reguł biznesowych z **kolumny "Uwagi" JRWA** (np. oznaczenie klasy `120` jako wymagającej tworzenia podteczek dla każdego pracownika, zgodnie z logiką Kompendium, Rozdział 5 i 6).

System blokuje możliwość utworzenia teczki w klasach spoza uprawnionego zakresu.

To kluczowy mechanizm porządkujący i zabezpieczający logikę JRWA w dużych organizacjach.

### **UC-JRWA-ADM-006 – Oznaczanie klas jako końcowe lub agregujące**

**Rola:** Administrator JRWA

**Cel:** Wyznaczenie, w których klasach JRWA można zakładać `Teczka_sprawy` lub rejestrować sprawy, a które pełnią jedynie funkcję grupującą (nadrzędną).

**Opis:** Administrator oznacza węzły drzewa JRWA jako **końcowe** (np. `0130` – do rejestracji) lub **agregujące** (np. `01` – Organizacja, bez rejestracji).

System wymusza, aby `Teczka_sprawy` mogła powstać **tylko w klasach końcowych**, co jest zgodne z Instrukcją Kancelaryjną LOT (§24 ust. 2).

Zapobiega to tworzeniu teczek w miejscach przeznaczonych jedynie do porządkowania struktury wykazu.

To proste, ale bardzo ważne zabezpieczenie zgodności z logiką klasyfikacji dziesiętnej.

### **UC-JRWA-ADM-007 – Eksport słownika JRWA do pliku (raport / integracja)**

**Rola:** Administrator JRWA / Archiwista

**Cel:** Udostępnienie struktury JRWA w postaci pliku zewnętrznego dla raportowania lub integracji z innymi systemami.

**Opis:** System umożliwia eksport aktualnej struktury JRWA (lub jej fragmentu) do pliku CSV, XLSX lub XML.

Raport zawiera symbole, nazwy, kategorie archiwalne, status obowiązywania i zakresy operacyjne.

Eksport może być wykorzystany do kontroli archiwalnej, porównania wersji między jednostkami lub synchronizacji z systemami finansowo-kadrowymi.

## **Podsumowanie grupy 1**

> **Najważniejsze do zapamiętania:**

> Ten zestaw siedmiu UC obejmuje pełny cykl życia słownika JRWA – od importu i walidacji, przez utrzymanie i kontrolę, po eksport i dostęp użytkowników.

> Dla wdrożeniowców AMODIT to fundament: zapewnia poprawne drzewo (zgodne z JRWA LOT 1997), kontrolę uprawnień (zgodną z Kompendium, Rozdział 10) i prostą, zgodną z przepisami obsługę klasyfikacji spraw.