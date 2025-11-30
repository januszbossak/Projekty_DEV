# Azure DevOps

**Status:** ✅ Obowiązuje
**Ostatnia aktualizacja:** 2025-09-09

---

## 1. Ogólne zasady korzystania

| Zasada | Opis |
|---|---|
| **Wszystko jest w ADO** | Azure DevOps jest jedynym i ostatecznym źródłem prawdy o zadaniach. Jeśli czegoś nie ma w ADO, to nie istnieje z perspektywy deweloperskiej. |
| **Hierarchia pracy** | Obowiązuje struktura: `Epic -> Feature -> Product Backlog Item (PBI)`. Historyjki użytkownika (User Story) nie są używane. |
| **Wiki vs Backlog** | **Wiki** służy do dokumentacji projektowej i analitycznej (CO i DLACZEGO robimy). **Backlog** służy do zarządzania zadaniami deweloperskimi (JAK robimy). |

## 2. Zgłaszanie pytań i pomysłów rozwojowych

### Problem
Backlog bywa zaśmiecany pytaniami i luźnymi pomysłami, które nie są jeszcze formalnymi zadaniami do realizacji. Miesza to zadania z finansowaniem z koncepcjami, które wymagają dopiero analizy.

### Ustalona ścieżka postępowania

#### A. Pytania ("czy coś się da zrobić?", "jak to działa?")
1.  **Zgłoszenie:** Przez proces wycen w AMODIT z oznaczeniem "pytanie" lub bezpośrednio do jednego z Product Ownerów (Damian, Kamil, Łukasz, Janusz, Piotr B.).
2.  **Analiza:** Product Ownerzy przetwarzają pytanie, w razie potrzeby konsultując je na Radzie Architektów.
3.  **Dokumentacja:** Jeśli pomysł jest wartościowy, powstaje dla niego dedykowany projekt w dokumentacji (w folderze `Projekty/`).
4.  **Backlog:** Dopiero na podstawie udokumentowanego projektu tworzone są konkretne, zdefiniowane zadania (PBI) w backlogu ADO.

#### B. Pomysły rozwojowe (brak finansowania)
1.  **Zgłoszenie:** Przez proces wycen w AMODIT z użyciem kategorii "pomysł rozwojowy".

### Podsumowanie
**Backlog w Azure DevOps służy wyłącznie do zadań gotowych do realizacji.** Nie jest miejscem na luźne pytania czy pomysły. Te powinny trafiać do Product Ownerów przez dedykowane kanały (proces wycen lub bezpośrednia komunikacja), aby mogły zostać poddane analizie i ewentualnie przekształcone w udokumentowane projekty, a dopiero potem w zadania.
