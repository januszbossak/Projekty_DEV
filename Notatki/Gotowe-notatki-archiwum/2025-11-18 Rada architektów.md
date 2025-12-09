# Rada Architektów – 2025-11-18

**Tematy:**
- Licencjonowanie - hurtowe blokowanie użytkowników
- Moduł raportowy - filtry i wydajność

---

## 1. Licencjonowanie - hurtowe blokowanie użytkowników

### Kontekst i Problem
Klient Dentsu (ok. 500 kont zsynchronizowanych z AD) zgłosił zapotrzebowanie na mechanizm hurtowego blokowania użytkowników (ok. 300 osób), którzy korzystają z systemu sporadycznie (np. raz w roku do akceptacji faktury). Celem jest oszczędność na licencjach poprzez dynamiczne przełączanie aktywnych kont.

### Rozważane alternatywy
| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dynamiczne blokowanie | Automatyzacja blokowania/odblokowywania kont w celu rotacji licencji. | ❌ Odrzucona – niezgodna z modelem biznesowym i intencją licencji imiennych. |
| Licencje concurrent | Model licencji jednoczesnych. | ⏸️ Odroczona – są wielokrotnie droższe, klient ma już preferencyjne warunki. |
| Licencje per proces | Licencje ograniczone do jednego procesu (np. urlopy). | 💡 Propozycja – stosowane biznesowo (np. Orlen), ale brak systemowego rozwiązania technicznego. |

### Decyzja
**Status:** ❌ Odrzucone

Nie wspieramy mechanizmów dynamicznego przełączania kont w celu omijania opłat licencyjnych. Zgodnie z umową każdy użytkownik systemu musi posiadać licencję. Przenoszenie licencji jest dozwolone tylko w przypadku rotacji pracowników (odejście/zatrudnienie), a nie bieżącej optymalizacji kosztów.

### Zadania
- **[Łukasz Bott]:** Przekazanie klientowi (Dentsu) stanowiska firmy – brak zgody na hurtowe blokowanie w tym celu.

---

## 2. Filtry w raportach i wydajność

### Kontekst i Problem
W raportach, które nie pilnują uprawnień do spraw, filtry nie podpowiadają wartości ze spraw, do których użytkownik nie ma dostępu (mimo że raport pokazuje dane). Dodatkowo, lista podpowiedzi w filtrze jest budowana na podstawie pierwszych 20 rekordów wyniku raportu, co powoduje, że nie wszystkie dostępne wartości są widoczne (np. widać tylko klienta A, mimo że w bazie są też B, C, D).
Obecna implementacja podpowiedzi (nowe zapytanie, `SELECT DISTINCT`, `LIKE %...%` na nieindeksowanej kolumnie `CaseDefinition`) jest nieoptymalna wydajnościowo.

### Zidentyfikowane Ryzyka
- Spadek wydajności przy wyszukiwaniu wartości filtrów na dużych zbiorach danych (brak indeksów, `LIKE %%`).
- Mylące działanie filtrów (brak podpowiedzi wartości, które faktycznie istnieją w danych).

### Rozważane alternatywy
| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Indeksowanie w definicji procesu | Konfiguracja indeksów w ustawieniach procesu (pomysł Piotra). | ⏸️ Odroczona – wymaga prac deweloperskich (nieukończony mechanizm). |
| Indeksowanie z poziomu raportu | Użytkownik w konfiguracji filtra klika "Zaindeksuj" (pomysł Janusza/Damiana). | 💡 Propozycja – bardziej naturalne dla użytkownika końcowego (twórcy raportu). |

### Decyzja
**Status:** ✅ Zatwierdzone (doraźnie) / 💡 Propozycja (docelowo)

1. **Doraźnie (Hotfix):** Należy poprawić mechanizm pobierania listy wartości do filtrów. Zapytanie powinno używać `DISTINCT` na całym zbiorze wyników (a nie tylko pierwszych 20 rekordach), aby wyświetlić wszystkie dostępne opcje.
2. **Docelowo:** Należy wdrożyć mechanizm indeksowania pól. Raporty powinny pozwalać na filtrowanie/podpowiadanie tylko po polach, które zostały zaindeksowane (np. w tabeli `Case` jako JSON lub Lucene). Indeksowanie powinno być "włączane" przez użytkownika (np. w konfiguracji raportu).

**Szczegóły techniczne:**
- Indeksowanie powinno obsługiwać wyszukiwanie od początku frazy (jak pole Odnośnik), ewentualnie w środku frazy (jeśli świadoma decyzja).
- Należy ograniczyć liczbę indeksowanych kolumn na proces (np. do kilku kluczowych: NIP, PESEL, Kontrahent).

### Zadania
- **[Anna Skupińska] / [Mateusz]:** Poprawa pobierania wartości do filtrów (usunięcie limitu 20 rekordów, zastosowanie DISTINCT na pełnym zbiorze).
- **[Janusz Bossak]:** Opracowanie przypadków użycia (Use Cases) dla nowego mechanizmu indeksowania i filtrów.

### Punkty otwarte
- Szczegóły implementacji mechanizmu indeksowania (dokończenie pomysłu Piotra vs nowe podejście od strony raportu).

> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-08

## Powiązane projekty
- `Moduly/Modul-raportowy/Filtry-uzytkownika`
- `Moduly/Modul-raportowy/Wydajnosc`
- `cross-cutting/Logowanie-do-amodit`

