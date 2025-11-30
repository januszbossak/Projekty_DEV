# Notatka projektowa – 2025-11-19 – Przegląd wycen

**Data:** 2025-11-19
**Temat główny:** Przegląd wycen, interfejs SignApp oraz problemy z odświeżaniem raportów.

---

## 1. Interfejs SignApp - Certyfikaty



### Cel i problem
Ustalenie sposobu wyświetlania certyfikatów w aplikacji SignApp (Mac). Dylemat: czy pokazywać wszystkie certyfikaty (również nieaktywne), czy tylko aktywne/służące do podpisu.

### Rozważane alternatywy
| Opcja | Opis | Status |
|-------|------|--------|
| Tylko aktywne | Wyświetlanie tylko certyfikatów aktywnych i służących do podpisu. | ✅ Wybrana (jako domyślna) – upraszcza widok dla użytkownika. |
| Wszystkie (przełącznik) | Opcja pokazania wszystkich certyfikatów (w tym nieaktywnych) za pomocą przełącznika. | ✅ Wybrana (jako opcja) – pomaga w diagnostyce (użytkownik widzi, że certyfikat jest, ale nieaktywny). |

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- Domyślnie wyświetlane są tylko **aktywne certyfikaty służące do podpisu**.
- Opcja "Pokaż wszystkie certyfikaty" (lub podobna) zostanie umieszczona na dole ekranu (w stylu trybu deweloperskiego), a nie na górze.
- Komunikaty błędów mają być wzorowane na module raportowym: Opis sytuacji + Instrukcja co zrobić (np. "Podłącz urządzenie i kliknij Odśwież").
- Wyróżnianie certyfikatów z krótką datą ważności (na czerwono) – temat do rozwoju w przyszłości (nie w MVP).

---

## 2. Problem odświeżania raportów (Dashboard)



### Cel i problem
Po wykonaniu akcji na sprawie otwartej z raportu (np. zmiana statusu, która powinna usunąć sprawę z listy) i powrocie do raportu/zamknięciu pop-upa, raport na dashboardzie nie odświeża się automatycznie – sprawa nadal jest widoczna. Zgłoszono również problem z działaniem przycisku "Odśwież" na dashboardzie.

### Rozważane alternatywy
Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone (doraźnie) / 🔍 Do analizy (docelowo)

- **Doraźnie:** Należy naprawić działanie przycisku "Odśwież" na dashboardzie (musi skutecznie odświeżać zawartość).
- **Docelowo:** Należy przeanalizować i opisać przypadki użycia dla automatycznego odświeżania po powrocie do raportu:
    1. Rekord nadal spełnia kryteria: czy ma zostać w tym samym miejscu (nawet przy zmianie sortowania)?
    2. Rekord przestaje spełniać kryteria: czy ma zniknąć natychmiast, czy po ręcznym odświeżeniu?
    Decyzja: Nie wdrażać pochopnych zmian w automatyzacji, dopóki nie zostaną spisane spójne zasady UX.

---

## 3. Przegląd Wycen i Zleceń



### Statusy zleceń
- **Orlen:** Oferta wysłana w czerwcu, brak odpowiedzi, ale duża szansa na realizację.
- **Rejestrowanie pobierania PDF:** Zlecenie zrealizowane i rozliczone w ramach głównej umowy – do zamknięcia w systemie.
- **Rossmann (Powiadomienia):** Temat ważny ("ważne, ale nie pilne"), ale wisi od marca bez decyzji klienta.
- **LPP:** Wyceny pomysłów, na które klientowi skończył się budżet, należy anulować.

### Nowe tematy
- **Rossmann - Historia spraw powiązanych:** Klient oczekuje wyświetlania historii. Damian spotka się z klientem, aby ustalić, czy potrzebują pełnej historii technicznej (pomysł Kamila), czy dedykowanej historii biznesowej (sugerowane przez Łukasza B. i Damiana).
- **Dashboard "Wyceny":** Prośba o skopiowanie dashboardu i usunięcie filtra "aktywne", aby umożliwić przeszukiwanie wszystkich wycen (również archiwalnych) i filtrowanie po kliencie.

---

## 4. JRWA i Archiwizacja (LOT) - Wzmianka



### Kontekst
Kamil zwraca uwagę, że JRWA to tylko część zagadnienia – istotna jest również fizyczna archiwizacja (pudła, składy chronologiczne). Sugestia budowy dedykowanego rozwiązania zamiast opierania się na standardowych rejestrach i odnośnikach. Temat przekierowany na dedykowane spotkanie projektowe.

---

## Punkty otwarte

- Ustalenie wymagań biznesowych Rossmanna dot. historii spraw powiązanych (spotkanie Damiana).
- Opracowanie spójnych zasad zachowania raportu po powrocie ze szczegółów sprawy (odświeżanie, sortowanie, paginacja).
