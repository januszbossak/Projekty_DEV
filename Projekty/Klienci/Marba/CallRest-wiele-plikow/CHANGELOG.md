# CHANGELOG – CallRest-wiele-plikow (Marba)

---

## 2025-09-11 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-11 Rada architektów - Multipart REST checkboxy edytor.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-11%20Rada%20architektów%20-%20Multipart%20REST%20checkboxy%20edytor.md)
**Kategoria:** #Architektura #Funkcjonalność #Decyzja

**CallRest – obsługa multipart form data dla wielu plików** ✅

Implementacja dedykowana dla Marba - wysyłanie wielu plików (dynamiczna ilość, do 100) do zewnętrznego Web Service'u za pomocą CallRest w formacie multipart form data.

**Kontekst biznesowy:**
- Marba potrzebuje wysyłania wielu plików (do 100) do zewnętrznego Web Service'u
- Obecny mechanizm CallRest wymaga definiowania wielu parametrów systemowych (parametr 1, 2, 3...) - niepraktyczne przy dużej liczbie plików
- Problem może pojawić się u innych klientów (KSeF - faktury z załącznikami)

**Rozwiązanie:**
- Format: multipart form data (optymalny dla plików binarnych, nie JSON)
- Mechanizm: jeden parametr z listą plików + separatory (analogicznie do headers 10.2)
- Separator: pojedynczy dwukropek (`:`) - spójność z istniejącym mechanizmem headers
- Budowanie: Handlebars (`each`, `if`) do dynamicznego budowania listy plików w regule
- Format parametru: `file:FieldByName:nazwa_pola:nazwa_pliku`
- 3 sposoby wskazania pliku: ID pliku, nazwa pola, nazwa załącznika
- Możliwość zmiany nazwy pliku przy wysyłaniu
- Nowa linia = nowa para klucz-wartość w multipart form data
- Dokumentacja: przykład na Wiki Wewnętrzne (CallRest, sekcja 10.2 - Headers)

**Rozważane alternatywy:**
- ❌ Budowanie JSON-a dynamicznie w regule - zasobochłonne, niewydajne przy dużych stringach
- ✅ Multipart form data w jednym parametrze - wybrana, spójność z mechanizmem headers (10.2)
- ⏸️ JSON z Base64 dla wielu plików - odroczona, może być w przyszłości, ale multipart bardziej optymalny

**Uwaga:** Rozważano podwójny dwukropek (`::`) jako separator dla większej niezawodności, ale zachowano pojedynczy dwukropek dla spójności z headers. Zmiana separatora wymagałaby aktualizacji istniejących integracji.

**Technologia:**
- Rozwiązanie ogólnosystemowe - zobacz [Integracje/Integracje-REST-multipart](../../../Integracje/Integracje-REST-multipart/)

**Zadania:**
- Adrian Kotowski - implementacja obsługi multipart form data w CallRest (zlecenie Marba)
- Piotr Buczkowski - weryfikacja i uwagi do propozycji Adriana

**Punkty otwarte:**
- Czy w przyszłości potrzeba JSON z wieloma plikami (zamiast multipart)?
- Jak obsłużyć różne formaty (multipart vs JSON) dla różnych systemów?
- Czy separator jest wystarczająco niezawodny przy specjalnych nazwach plików?

---
