# Historia Biznesowa - Panel Monitoringu Procesów Biznesowych

## Koncepcja
**Historia Biznesowa** to mechanizm monitorowania przebiegu sprawy biznesowej w systemie AMODIT, zaprojektowany w formie interaktywnego timeline`u wizualizującego chronologię kluczowych zdarzeń biznesowych.

## Cel i kontekst
System AMODIT posiada już szczegółową historię zdarzeń (*audit trail*) rejestrującą wszystkie operacje na formularzach. Historia Biznesowa stanowi warstwę analityczną nad tym mechanizmem, prezentując wyłącznie zdarzenia kluczowe dla przebiegu sprawy biznesowej, agregując informacje z wielu powiązanych formularzy AMODIT.

**Kluczowa różnica:**
- **Historia szczegółowa** dokumentuje wszystko na poziomie pojedynczego formularza.
- **Historia Biznesowa** pokazuje tylko to, co istotne biznesowo, w kontekście całej sprawy obejmującej wiele formularzy.

## Umiejscowienie w interfejsie
Panel dostępny jest w prawym menu bocznym (sidebar) - w tej samej pozycji co obecna historia szczegółowa. Obie historie dostępne są przez osobne zakładki:
*   **Historia szczegółowa** - pełny audit trail pojedynczego formularza.
*   **Historia Biznesowa** - kluczowe zdarzenia całej sprawy biznesowej.

## Wizualizacja i prezentacja danych

### Timeline procesów
Historia prezentowana jest jako chronologiczny timeline (od najstarszego do najnowszego zdarzenia) z wizualnym oznaczeniem sekwencji - kropkami połączonymi linią.

### Kolorowe kodowanie procesów
Procesy biznesowe są wizualnie rozróżniane poprzez sekcje w przypisanych kolorach systemowych, np.:
*   **Pobieranie korespondencji z eDoręczeń** - niebieski
*   **Korespondencja typu X** - pomarańczowy
*   **Korespondencja typu Y** - fioletowy

To umożliwia natychmiastową identyfikację typu operacji na pierwszy rzut oka.

### Kafelki zdarzeń
Każde zdarzenie prezentowane jest jako kafelek zawierający:
*   Nazwę zdarzenia
*   Datę i godzinę wykonania
*   Użytkownika, który wywołał zdarzenie
*   Przycisk **"Pokaż szczegóły"**

### Szczegóły zdarzenia
Po kliknięciu "Pokaż szczegóły" wyświetlana jest dowolna informacja merytoryczna skonfigurowana podczas wdrożenia, pozwalająca na głębszą analizę konkretnego zdarzenia.

## Funkcje wyszukiwania i filtrowania

### Wyszukiwarka pełnotekstowa
*   Przeszukuje nazwy procesów i zdarzeń.
*   Podświetla wyniki na żółto.
*   Umożliwia błyskawiczne odnalezienie konkretnych zdarzeń w długiej historii sprawy.

### System filtrowania
*   Zaawansowane opcje zawężania widoku po procesie lub zdarzeniu.
*   Działa łącznie z wyszukiwarką dla maksymalnej precyzji.

## Konfiguracja i wdrożenie

### Odpowiedzialność wdrożeniowa
Historia Biznesowa wymaga konfiguracji na poziomie procesu i nie jest budowana natywnie w systemie. Konfigurację wykonuje wdrożeniowiec we współpracy z biznesem, definiując:
1.  **Identyfikację sprawy biznesowej** - które formularze należą do tej samej sprawy (relacje, identyfikatory).
2.  **Zdarzenia kluczowe** - które zdarzenia z audit trail i kontekstu powiązanych formularzy mają być rejestrowane w Historii Biznesowej.
3.  **Treść szczegółów** - jakie informacje mają być zapisywane dla każdego typu zdarzenia.
4.  **Przypisanie do procesów** - do którego procesu biznesowego należy dane zdarzenie.

### Elementy systemowe
*   **Procesy biznesowe** - definiowane w systemie.
*   **Kolory procesów** - przypisane systemowo.
*   **Administrator** – konfiguruje przy pomocy *Amodit Script*, które zdarzenia są odnotowywane w Historii Biznesowej.

## Uprawnienia
Historia Biznesowa widoczna jest dla każdego użytkownika, który ma dostęp do sprawy (formularza). Brak dodatkowych ograniczeń widoczności na poziomie procesów czy zdarzeń.

## Korzyści biznesowe
*   Natychmiastowy wgląd w status sprawy z wyszczególnieniem kluczowych zdarzeń biznesowych.
*   Szybka identyfikacja problemów w przebiegu procesu.
*   Możliwość audytu pełnego przebiegu sprawy w kontekście biznesowym.
*   Eliminacja potrzeby przeszukiwania wielu formularzy i szczegółowej historii.
*   Centralne narzędzie kontrolne dla użytkowników i koordynatorów spraw.

## Materiały pomocnicze
Mockup demonstracyjny koncepcji dostępny pod adresem: [https://grow-silver-08622037.figma.site/](https://grow-silver-08622037.figma.site/)
