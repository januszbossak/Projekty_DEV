# Cele Sprintu - 1 grudnia 2025

## Repozytorium WIM

**Cel:** Realizacja MVP 2 - zarządzanie strukturą repozytorium zainstalowane u klienta WIM

- zainstalowano repozytorium u klienta WIM
- działa tworzenie folderów
- działa edycja folderów
- działa usuwanie folderów
- działa wgrywanie plików
- działa pobieranie plików
- działa podgląd plików
- działa zarządzanie uprawnieniami
- (opcjonalnie) zaimplementowano historię zdarzeń (jeśli zdążymy)

**Zespół:**
- PDM: Damian Kaminski
- DEV1: Anna Skupinska
- DEV2: Filip Liwiński
- DEV3: Adrian Kotowski
- Tester: Oktawia

---

## JRWA dla LOT

**Cel:** Funkcjonalność JRWA dostarczona do konsultantów i zainstalowana u klienta LOT

- przygotowano strukturę po stronie bazy danych
- osadzono funkcjonalność w polu odnośnik do źródła zewnętrznego
- zaimplementowano możliwość wyboru kategorii JRWA
- przekazano paczkę do instalacji dla LOTu
- dane z wybranego JRWA przepisują się do pól typu tekstowego (na poziomie sprawy, bez raportów)

**Zespół:**
- PDM: Kamil Dubaniowski
- DEV: Marek Dziakowski
- Tester: (do przypisania przez testerki)

---

## Spójny styl tabel dla Design

**Cel:** Spójny wygląd tabel w module Design zgodny z wytycznymi

- spisano wytyczne co do wyglądu standardowego tabel w Design
- poprawiono obecne tabele zgodnie z wytycznymi
- ustalono odchylenia w widokach wymagających odstępstw od standardu

**Zespół:**
- PDM: Kamil Dubaniowski
- DEV: Marek Dziakowski

---

## Prawy panel - projekt i realizacja

**Cel:** Ulepszony prawy panel w edytorze graficznym i liście pól zgodny z projektem

- ustalono gotowy projekt prawego panelu (pierwszy tydzień)
- zrealizowano zmiany zgodnie z projektem (drugi tydzień)
- uporządkowano kolejność ustawień (najczęściej używane na górze)
- wyróżniono wygląd prawego panelu jako elementu konfiguracyjnego (nie formularza)
- zoptymalizowano lokalizację przycisków i akcji
- zmieniono sposób edycji parametrów GUID w polu (okno zamiast osadzenia)
- zlokalizowano akcje związane z regułami tabeli w prawym panelu

**Zespół:**
- PDM: Kamil Dubaniowski
- DEV: Przemysław Rogaś

---

## Porządki i bugi UI

**Cel:** Naprawione bugi UI i poprawiony wygląd pól tabeli

- naprawiono bugi UI-owe w polach tabeli
- poprawiono wygląd menu przy polach (odnośnik, dokument) - zmniejszono wysokość pozycji
- ujednolicono kolory menu (usunięto niespójności niebieskie/czarne)
- poprawiono wygląd pola tabela z zagnieżdżeniami (tabela w tabeli)
- naprawiono niespójności w wyświetlaniu kompaktowym (pola z wyborami)
- zweryfikowano mobilny interfejs (jeśli zdążymy)

**Zespół:**
- PDM: Kamil Dubaniowski
- DEV: Przemysław Rogaś

---

## Raporty systemowe dla WIM

**Cel:** Przygotowane 5 raportów systemowych dla WIM zgodnie z wymaganiami

- przygotowano 5 raportów systemowych
- opisano cele i funkcjonalności każdego raportu
- zweryfikowano zgodność z wymaganiami WIM
- dostosowano raporty do potrzeb klienta (jeśli wymagane)

**Zespół:**
- PDM: Łukasz Bott
- DEV: (do ustalenia - możliwe uproszczone źródła przygotowane przez zespół)
- Wsparcie: Damian Kaminski

---

## Indeksacja - raport tabelaryczny

**Cel:** Dokończona indeksacja zapewniająca 100% działanie raportu tabelarycznego bez błędów

- dokończono indeksację
- zapewniono 100% działanie raportu tabelarycznego
- wyeliminowano wszystkie błędy związane z raportem tabelarycznym

**Zespół:**
- PDM: Janusz Bossak
- DEV Backend: Mateusz Kisiel
- DEV Frontend: Przemysław Rogaś

---

## Certyfikacja SignApp

**Cel:** Zakończony proces certyfikacji aplikacji SignApp zgodnie z wymaganiami Apple

- przeprowadzono proces certyfikacji aplikacji SignApp zgodnie z wymaganiami Apple
- złożono dokumenty i wymagania do subskrypcji Apple
- przygotowano aplikację do wydawania poza App Store

**Zespół:**
- PDM: Kamil Dubaniowski
- DEV: Adrian Kotowski

---

## Integracja z SIEM dla LOT

**Cel:** Przygotowany dokument z zakresem integracji z systemami klasy SIEM

- przygotowano dokument z zakresem integracji z systemami klasy SIEM
- określono wytyczne do opracowania integracji na poziomie wymagań biznesowo-technicznych
- zdefiniowano zdarzenia do przekazywania do SIEM (np. zapomniane hasło, logowanie)

**Zespół:**
- PDM: Łukasz Bott

---

## Comarch Hub dla Lewiatan

**Cel:** Dokończona integracja z Comarch Hub uruchomiona u klienta Lewiatan

- dokończono integrację z Comarch Hub
- uruchomiono moduł u klienta Lewiatan
- przeprowadzono testy u klienta (brak środowiska testowego)
- przygotowano dokumentację konfiguracyjną

**Zespół:**
- PDM: Łukasz Bott
- DEV: Łukasz Brocki
- Tester: (do przypisania przez testerki)

---

## Integracja UPS

**Cel:** Zaimplementowana integracja z UPS analogiczna do Global Express

- zaimplementowano funkcje w regułach umożliwiające wysyłkę przesyłki
- zaimplementowano sprawdzanie statusu przesyłki
- zaimplementowano wydruk etykiety
- przeprowadzono testy u klienta (wymagane konto z umową handlową)
- przygotowano dokumentację

**Zespół:**
- PDM: Łukasz Bott
- DEV: Łukasz Brocki
- Tester: (do przypisania przez testerki)

---

## Trust Center - joby

**Cel:** Joby Trust Center wdrożone na produkcji

- przetestowano joby Trust Center
- wgrano joby na domówkę
- wdrożono joby na produkcję (po okresie testowym na domówce)
- (opcjonalnie) zaimplementowano job do przestawiania długo nieużywanych dokumentów na wygasłe

**Zespół:**
- PDM: (nie określono)
- DEV: Marek Dziakowski

---

## Bugi raportów

**Cel:** Naprawione bugi w raportach (ogólne ustawienia i raport tabelaryczny)

- naprawiono bugi z raportów dotyczące ogólnych ustawień
- naprawiono bugi z raportu tabelarycznego
- naprawiono bugi z filtrów (jeśli ogólne, nie specyficzne dla Ganta)

**Zespół:**
- PDM: Kamil Dubaniowski
- DEV: Przemysław Rogaś

---

## Obserwacja czatów serwisowych

**Cel:** Zapewnione pokrycie czatów serwisowych podczas nieobecności Piotra

- Adrian i Mariusz obserwują czaty konsultantów podczas nieobecności Piotra
- zapewniono pokrycie przez cały tydzień
- obsłużono bieżące zgłoszenia serwisowe

**Zespół:**
- PDM: Kamil Dubaniowski
- DEV: Adrian Kotowski, Mariusz Piotrzkowski

---

## Uwagi

- Niektóre zespoły mają nieokreślonych testerów - testerki mają się podzielić zadaniami między sobą
- Niektóre cele mogą wymagać doprecyzowania w trakcie sprintu
- Historia zdarzeń w repozytorium jest opcjonalna - jeśli nie zdążymy, przechodzi do następnego sprintu
- MCP i dokumentacja AI zostały zaparkowane jako proof of concept - wymagają dalszego planowania biznesowego


