# Kompendium Wiedzy o JRWA

## Podstawy dla firmy wdrażającej system AMODIT w PLL LOT S.A.

## 1. Wprowadzenie – po co w ogóle istnieje JRWA?

Zanim zaczniemy myśleć o konfiguracji procesów czy projektowaniu rejestrów w AMODIT, warto zrozumieć, **dlaczego w ogóle istnieje Jednolity Rzeczowy Wykaz Akt (JRWA)** i jaką pełni rolę w organizacji.

JRWA to nie jest biurokratyczny obowiązek, tylko **narzędzie porządkujące informację** — mapa całej działalności instytucji, która pozwala logicznie i konsekwentnie klasyfikować wszystkie dokumenty.

Każda instytucja publiczna, a coraz częściej także spółki z udziałem Skarbu Państwa czy organizacje z rozbudowaną strukturą, muszą działać zgodnie z zasadami określonymi w **Rozporządzeniu Prezesa Rady Ministrów z 18 stycznia 2011 roku**.

Rozporządzenie to definiuje, jak mają wyglądać trzy podstawowe elementy systemu kancelaryjnego:

1. **Instrukcja kancelaryjna** – czyli zasady obiegu dokumentów,
    
2. **Jednolity Rzeczowy Wykaz Akt (JRWA)** – czyli system klasyfikacji spraw,
    
3. **Instrukcja archiwalna** – określająca sposób przekazywania i brakowania dokumentacji.
    

Dzięki temu każda sprawa, niezależnie od tego, w której jednostce powstała, ma swój określony **symbol, kategorię archiwalną i sposób postępowania**.

JRWA klasyfikuje dokumenty **rzeczowo**, a nie według struktury organizacyjnej.

Oznacza to, że np. dział prawny i dział handlowy, jeśli oba zajmują się reklamacjami, powinny używać tego samego symbolu klasy (zgodnie z obowiązującym w LOT wykazem akt).

Dla nas, **jako firmy wdrażającej system AMODIT**, JRWA jest nie tylko punktem odniesienia, ale **fundamentem architektury systemu**.

To właśnie ono mówi nam, jakie typy spraw występują w organizacji, jak je grupować i w jaki sposób oznaczać.

Każdy rejestr, proces czy moduł raportowy powinien mieć swoje odzwierciedlenie w strukturze JRWA — tylko wtedy możemy powiedzieć, że system „rozumie” logikę kancelaryjną i wspiera ją technicznie.

**Najważniejsze do zapamiętania:**

- JRWA to nie zbiór folderów, lecz logiczny model organizacji dokumentacji.
    
- Wdrożenie AMODIT bez zrozumienia JRWA prowadzi do chaosu klasyfikacyjnego.
    

## 2. System kancelaryjny – środowisko, w którym JRWA żyje

JRWA nie istnieje w próżni. Jest częścią większego mechanizmu zwanego **systemem kancelaryjnym**, czyli zestawu zasad, według których w jednostce powstają, krążą i są archiwizowane dokumenty.

W zależności od poziomu cyfryzacji organizacji, system kancelaryjny może działać w jednym z trzech wariantów: **tradycyjnym (papierowym)**, **elektronicznym (EZD)** lub **hybrydowym**.

### 2.1 System hybrydowy (Papierowy oryginał, elektroniczny obieg) – Model docelowy "TO BE" w LOT

Dla naszego wdrożenia w LOT jest to **kluczowy i obowiązujący model docelowy**.

Choć Instrukcja Kancelaryjna LOT (§ 6 ust. 1) stwierdza, że czynności wykonuje się "w postaci nieelektronicznej", co wskazuje na system tradycyjny, to dostarczona mapa procesu "TO BE" (KORESPONDENCJA ZEWNĘTRZNA PRZYCHODZĄCA... TRADYCYJNA) oraz ustalenia ze spotkań precyzują ten model.

Docelowy system w LOT jest **systemem hybrydowym**, w którym:

1. **Oryginałem pozostaje dokument papierowy** (zgodnie z § 6 ust. 1 Instrukcji).
    
2. Po wpłynięciu do organizacji jest on **natychmiast skanowany** (zgodnie z mapą procesu "Skanowanie przesyłki do systemu").
    
3. Oryginał papierowy jest odkładany do **składnicy/archiwum** (zgodnie z mapą procesu "Składnica").
    
4. **Cały dalszy obieg** – rejestracja, dekretacja, weryfikacja, akceptacja, aż po zarządzanie sprawą – **odbywa się elektronicznie** w systemie AMODIT, w oparciu o odwzorowanie cyfrowe (skan).
    

Ten model w pełni realizuje zapisy § 6 ust. 2 Instrukcji Kancelaryjnej (wykorzystanie "narzędzi informatycznych" do m.in. dekretacji, prowadzenia spisów i przesyłania pism). AMODIT staje się więc centralnym systemem obiegu i rejestracji, a nie tylko "elektronicznym lustrem".

### 2.2 System EZD – dokument elektroniczny jako oryginał

W modelu EZD sytuacja jest odwrotna. Tu **dokument elektroniczny jest oryginałem**, a papier jest tylko jego odwzorowaniem. Cały obieg dokumentacji odbywa się w systemie teleinformatycznym.

Wdrażając AMODIT w takim środowisku, musimy zapewnić pełne wsparcie dla czynności kancelaryjnych. _Na obecnym etapie ten model nie jest modelem podstawowym dla LOT, choć system musi być gotowy na obsługę dokumentów czysto elektronicznych (np. z e-Doręczeń)._

### 2.3 Hybryda w praktyce – Potwierdzenie odbioru

Zgodnie z wymaganiami (transkrypcja z 5.11.2025), model hybrydowy obejmuje również interakcje z dokumentem papierowym. Przykładem jest proces odbioru korespondencji przychodzącej przez pracownika:

1. Dokument wpłynął w papierze i został zeskanowany do AMODIT.
    
2. Pracownik merytoryczny otrzymuje awizację w systemie.
    
3. Gdy pracownik fizycznie odbiera oryginał papierowy z Kancelarii, **potwierdza ten odbiór na tablecie** (składając podpis w systemie AMODIT).
    

To pokazuje ścisłe powiązanie obiegu elektronicznego (wiedza o dokumencie) z obiegiem fizycznym (zarządzanie oryginałem).

**Najważniejsze do zapamiętania (dla LOT):**

- Docelowym systemem "TO BE" w LOT jest **system hybrydowy** (oryginał papierowy, obieg elektroniczny), co precyzuje mapa procesu.
    
- AMODIT pełni rolę centralnego **systemu obiegu (workflow) i rejestracji** dla odwzorowań cyfrowych (skanów) oraz dokumentów elektronicznych.
    
- System musi wspierać interakcje cyfrowo-fizyczne (np. potwierdzenie odbioru papieru na tablecie).
    

## 3. Dwa rodzaje dokumentacji – sedno klasyfikacji

Jednym z pierwszych zadań, jakie wykonuje pracownik kancelarii przy każdym dokumencie, jest decyzja, **czy dany dokument tworzy akta sprawy, czy nie**.

To rozróżnienie jest kluczowe i zostało precyzyjnie zdefiniowane w **§ 20** i **§ 22** Instrukcji Kancelaryjnej LOT.

### 3.1 Dokumentacja tworząca “akta sprawy”

Do tej grupy należą wszystkie dokumenty, które dotyczą konkretnego zagadnienia – „akt sprawy” lub inaczej “teczka sprawy” mającej swój początek, przebieg i zakończenie.

To mogą być np.:

- wniosek o dofinansowanie projektu,
    
- procedura zatrudnienia pracownika,
    
- skarga pasażera,
    
- umowa i jej aneksy,
    
- kontrola techniczna budynku.
    

Zgodnie z **§ 20 ust. 2** Instrukcji LOT, jest to "dokumentacja, która została przyporządkowana do sprawy i otrzymała znak sprawy". Wymaga ona rejestracji w **spisie spraw** (§ 24).

W systemie AMODIT odpowiada to sytuacji, w której powstaje konkretna „teczka sprawy” – czyli instancja specjalnego procesu np. o nazwie `Teczka sprawy`, do której będziemy przypinali już sprawy atomowe z AMODIT’a. Ten proces `Teczka sprawy` zawiera tylko ogólne pola pozwalające na identyfikację oraz raport osadzony zawierający podpięte sprawy AMODIT.

### 3.2 Dokumentacja nietworząca akt sprawy

To dokumenty, które nie odnoszą się do konkretnej sprawy, lecz mają charakter ogólny, informacyjny lub ewidencyjny.

Zgodnie z **§ 20 ust. 3** Instrukcji LOT, jest to "dokumentacja, która nie została przyporządkowana do sprawy, a jedynie do klasy z wykazu akt". Nie jest rejestrowana w spisie spraw i nie otrzymuje pełnego znaku sprawy.

Instrukcja LOT w **§ 22** podaje konkretne przykłady:

- listy obecności,
    
- faktury, rachunki, inne dokumenty księgowe,
    
- karty urlopowe,
    
- zaproszenia, życzenia, podziękowania,
    
- niezamawiane oferty.
    

Takie dokumenty również klasyfikuje się w JRWA, ale tylko na poziomie klasy (np. `3114` – Rozliczenia z kontrahentami krajowymi), bez numeru sprawy. W AMODIT mogą być odwzorowane np. jako dokumenty zbiorcze lub rejestry.

**Najważniejsze do zapamiętania:**

- W JRWA każdy dokument musi zostać sklasyfikowany, ale nie każdy tworzy sprawę.
    
- Instrukcja LOT w § 20 i § 22 precyzyjnie definiuje ten podział.
    

## 4. Znak sprawy – „PESEL” dokumentacji

W każdej organizacji korzystającej z JRWA kluczowym elementem porządkującego systemu kancelaryjnego jest **znak sprawy**. To swoisty „PESEL” dokumentacji – unikalny identyfikator, który pozwala jednoznacznie rozpoznać sprawę.

Znak sprawy jest obowiązkowy dla każdej dokumentacji **tworzącej akta sprawy**.

Instrukcja Kancelaryjna LOT w **§ 21** definiuje dwa warianty znaku sprawy, oba opisane w Kompendium:

### 1. Znak 4-członowy (standardowy)

Składa się z czterech części (zgodnie z § 21 ust. 2 i 3 Instrukcji LOT):

[komórka].[symbol JRWA].[nr sprawy].[rok]

Przykład: **BA.010.15.2025**

- **BA** – skrót komórki (np. Biuro Administracji)
    
- **010** – symbol klasy z JRWA (np. Organizacja)
    
- **15** – numer kolejnej sprawy w danym roku w tej klasie
    
- **2025** – rok założenia sprawy
    

### 2. Znak 5-członowy (dla wydzielonych grup spraw / podteczek)

Występuje, gdy w obrębie danej klasy tworzy się wydzieloną grupę spraw (tzw. podteczkę), np. dla jednej nieruchomości, pracownika czy projektu. Zgodnie z § 21 ust. 5 i 6 Instrukcji LOT, znak ma postać:

[komórka].[symbol JRWA].[nr sprawy-matki].[nr sprawy w podserii].[rok]

Przykład: **BK.120.7.3.2025**

- **BK** – Biuro Kadr
    
- **120** – symbol JRWA (np. Akta osobowe)
    
- **7** – numer sprawy w głównym spisie klasy, na podstawie której utworzono podteczkę (sprawa‑matka, np. „Akta osobowe: Jan Kowalski”)
    
- **3** – kolejny numer sprawy w oddzielnym spisie tej podserii (np. "Wniosek urlopowy")
    
- **2025** – rok założenia sprawy
    

Dla nas, jako firmy wdrażającej AMODIT, zrozumienie logiki obu wariantów znaku sprawy ma kluczowe znaczenie. To na jego podstawie buduje się **spójność danych**. System musi umożliwiać generowanie obu typów znaków, zgodnie z § 21 Instrukcji LOT.

**Najważniejsze do zapamiętania:**

- Znak sprawy to kluczowy identyfikator; jego struktura w LOT jest precyzyjnie zdefiniowana w § 21 Instrukcji Kancelaryjnej z 2025 r.
    
- AMODIT musi wspierać generowanie zarówno 4- jak i 5-członowych znaków.
    

## 5. Teczki przedmiotowe (wydzielone grupy spraw) i widoki przekrojowe

To rozróżnienie jest kluczowe dla prawidłowej architektury systemu AMODIT.

### 5.1 Podteczka (Wydzielona grupa spraw)

W praktyce wiele klas w JRWA obejmuje zagadnienia powtarzające się na różnych obiektach — np. nieruchomościach, pracownikach, projektach.

Jeżeli kolumna „Uwagi” w JRWA nakazuje prowadzenie osobnych teczek dla tych obiektów, tworzy się w obrębie danej klasy tak zwane **wydzielone grupy spraw** (zwane też potocznie _teczkami przedmiotowymi_).

Jest to **formalna jednostka archiwalna** w ramach **jednej klasy JRWA**. Jak opisano w poprzednim rozdziale, taka podteczka:

- Ma **własny roczny spis spraw**.
    
- Używa **pięcioelementowego znaku sprawy** (§ 21 ust. 5 Instrukcji LOT).
    
- Jest zakładana na podstawie "sprawy-matki" z rejestru głównego.
    

Wszystkie sprawy z podteczki mają tę samą kategorię archiwalną co klasa macierzysta.

### 5.2 Widok przekrojowy (Logika systemowa AMODIT)

W praktyce biznesowej użytkownik często chce widzieć sprawy pogrupowane inaczej niż wynika to z JRWA – np. "wszystkie sprawy dla Kontrahenta X" albo "wszystko co dotyczy Nieruchomości Y".

Taki zbiór będzie zawierał dokumenty z **wielu różnych klas JRWA** (np. umowy z klasy `0320`, faktury z `340`, reklamacje z `380`).

Tworzenie dla takiego zbioru formalnej "teczki" byłoby **krytycznym błędem archiwalnym**, ponieważ mieszałoby dokumenty o różnych kategoriach (np. A, B5, BE10).

Dlatego w AMODIT stosujemy **widoki przekrojowe** (pulpity, dashboardy, raporty). Taki widok:

- Jest wyłącznie **narzędziem systemowym** ułatwiającym pracę.
    
- **Nie jest jednostką archiwalną.**
    
- Nie prowadzi się w nim spisu spraw ani nie nadaje znaku sprawy.
    
- Prezentuje jedynie logiczny zbiór linków/odwołań do spraw, które fizycznie (lub w systemie tradycyjnym – papierowo) pozostają w swoich właściwych teczkach macierzystych JRWA.
    

**Najważniejsze do zapamiętania (Krytyczne dla wdrożenia):**

- **Podteczka** (formalna, § 21 ust. 5 Instrukcji LOT): grupuje sprawy _w ramach tej samej klasy JRWA_ (np. Akta osobowe Jana Kowalskiego, klasa `120`). Ma 5-członowy znak.
    
- **Widok przekrojowy** (systemowy AMODIT): grupuje sprawy _z różnych klas JRWA_ (np. wszystko o Janie Kowalskim: akta z `120`, płace z `333`, szkolenia z `130`). Nie ma znaku sprawy.
    
- **Nie wolno** mieszać tych dwóch pojęć.
    

## 6. Słownik JRWA – żywy dokument i źródło logiki biznesowej

Jednolity Rzeczowy Wykaz Akt nie jest dokumentem zamkniętym raz na zawsze. To **żywy słownik**, który musi się rozwijać wraz ze zmianami w strukturze organizacyjnej, zadaniach i przepisach prawa.

### Krytyczne ustalenie dla wdrożenia w LOT S.A.

Analiza **Uchwały Zarządu Nr 3-2025-BA z 8.01.2025 r.** przynosi kluczowe ustalenie:

W **§ 4** tej uchwały Zarząd LOT S.A. uchyla punkty 1 i 3 Zarządzenia Prezesa Zarządu D/30/97/TA z 1997 roku (czyli starą Instrukcję Kancelaryjną i starą Instrukcję Archiwalną).

Oznacza to, że **§ 1 pkt 2 Zarządzenia D/30/97/TA – czyli "Jednolity rzeczowy wykaz akt PLL LOT SA" –** _**pozostał w mocy prawnej**_**.**

Dla wdrożenia AMODIT oznacza to, że:

1. Pracujemy w oparciu o **nowe zasady** (Instrukcja Kancelaryjna i Archiwalna z 2025 r.).
    
2. Ale korzystamy ze **"starego" słownika klas** (JRWA z 1997 r., dokument `D-30-97-TA...pdf`).
    
3. Wykaz akt PGL S.A. (`Jednolity Rzeczowy Wykaz Akt - PGL.pdf` z 2024 r.) jest dokumentem spółki matki i **nie jest** (jeszcze) formalnie wprowadzony do stosowania w LOT S.A.
    

Dlatego implementując słownik klas w AMODIT, musimy bazować **wyłącznie na JRWA z 1997 roku**.

### Rola kolumny "Uwagi"

Niezależnie od wersji JRWA, kluczowa pozostaje kolumna **"Uwagi"**. To tam zapisane są reguły, które bezpośrednio przekładają się na działanie systemu AMODIT.

Przykłady z JRWA LOT (1997):

- Dla klasy `006` (Komisje): "Dla każdej komisji... prowadzi się odrębną teczkę". To jest reguła biznesowa nakazująca stosowanie mechanizmu podteczek (znak 5-członowy).
    
- Dla klasy `0130` (Prokurenci): "Wnioski, opinie, decyzje przechowuje się w aktach osobowych - klasa 120". To jest reguła biznesowa wskazująca na powiązanie międzyklasowe (które zrealizujemy jako "widok przekrojowy" lub relację).
    

Słownik JRWA powinien być w AMODIT **wersjonowany**. Wersjonowanie oznacza, że każda zmiana – dodanie, modyfikacja lub usunięcie klasy – ma przypisaną datę obowiązywania.

**Najważniejsze do zapamiętania:**

- **Obowiązującym słownikiem klas w LOT jest JRWA z 1997 roku (zał. 2 do D/30/97/TA).**
    
- JRWA PGL S.A. z 2024 r. **nie ma** zastosowania w naszym wdrożeniu.
    
- Kolumna "Uwagi" z JRWA 1997 jest kluczem do automatyzacji i musi być czytelnie prezentowana w systemie.
    

## 7. Kategorie archiwalne – czas życia dokumentu

Każda klasa JRWA kończy się przypisaną **kategorią archiwalną**, która określa, jak długo dokumentacja powinna być przechowywana. To swoisty „termin ważności” akt, mający znaczenie prawne.

Najczęściej spotykane symbole:

|

| Symbol | Znaczenie | Przykłady (z JRWA LOT 1997) |

| A | Materiały archiwalne – przechowywać wieczyście | 001 (Rada Nadzorcza), 011 (Organizacja PLL LOT SA) |

| B | Dokumentacja niearchiwalna – przechowywać przez określoną liczbę lat (np. B5, B10) | 003 (Zjazdy, konferencje - B5), 1151 (Nagrody - B10) |

| BE | Dokumentacja niearchiwalna, której okres liczy się od określonego zdarzenia (np. BE10 – 10 lat od wygaśnięcia umowy) | 013 (Pełnomocnictwa - BE5), 120 (Akta osobowe - BE50) |

| Bc | Dokumentacja pomocnicza, bez wartości archiwalnej (krótki okres przechowywania, np. kopie robocze) | 0150 (Ewidencja obiegu - B5/Bc), 0841 (Programy pobytu delegacji - Bc) |

Kategorie archiwalne mają wpływ nie tylko na sposób przechowywania, ale także na proces przekazywania do archiwum zakładowego. System AMODIT powinien umożliwiać oznaczanie kategorii i automatyczne przypominanie o upływie okresu przechowywania.

**Najważniejsze do zapamiętania:**

- Kategoria archiwalna określa, jak długo dokument ma istnieć w systemie.
    
- Warto ją traktować jako metadane “Teczki sprawy”, a nie tylko informację z JRWA.
    

## 8. JRWA w praktyce wdrożeniowej AMODIT

Kiedy rozumiemy już zasady klasyfikacji, łatwiej zobaczyć, że JRWA nie jest „biurową formalnością”, lecz **szkieletem logicznym** całego systemu dokumentacyjnego.

W praktyce jego wpływ obejmuje każdy element AMODIT – od rejestrów po raporty.

W procesie wdrożenia warto zwrócić uwagę na kilka kluczowych aspektów:

1. **Odwzorowanie struktury JRWA** – każda klasa z JRWA 1997 powinna mieć swój odpowiednik w słowniku systemowym/rejestrze.
    
2. **Powiązanie JRWA z procesami** – każda sprawa powinna być przypisana do konkretnego symbolu klasy.
    
3. **Znak sprawy jako automatyczny identyfikator** – generowany według schematu z § 21 Instrukcji LOT.
    
4. **Integracja z instrukcją kancelaryjną** – system powinien umożliwiać takie same czynności, jakie przewiduje Instrukcja LOT z 2025 r.
    
5. **Wersjonowanie słownika/rejestru JRWA** – ważne dla zachowania zgodności historycznej.
    

Dzięki temu AMODIT staje się nie tylko narzędziem workflow, ale **pełnoprawnym systemem kancelaryjno-archiwalnym**, który wspiera zgodność z przepisami.

**Najważniejsze do zapamiętania:**

- AMODIT i JRWA muszą być spójne – procesy, rejestry i raporty muszą odzwierciedlać strukturę wykazu akt (z 1997 r.).
    

## 9. Najczęstsze błędy przy wdrażaniu JRWA

Z doświadczeń wdrożeń w instytucjach publicznych i spółkach wynika, że problemy z JRWA zwykle wynikają nie z przepisów, ale z ich interpretacji.

Poniżej najczęstsze błędy, które warto znać:

- **Mieszanie klasyfikacji rzeczowej i strukturalnej** – przypisywanie spraw do działów zamiast do tematów.
    
- **Używanie JRWA tylko jako listy folderów** – brak rozumienia jego logiki.
    
- **Nieprawidłowe nadawanie znaków spraw** – pomijanie elementów lub błędne formaty.
    
- **Brak spójności między JRWA a instrukcją kancelaryjną** – szczególnie w zakresie dekretacji i archiwizacji.
    
- **Brak aktualizacji JRWA po zmianach w zadaniach organizacji.** (To ryzyko w LOT – mają nowe instrukcje, ale stary JRWA).
    

Unikanie tych błędów wymaga świadomości, że JRWA to nie dokument „dla archiwisty”, ale narzędzie zarządzania informacją w całej instytucji.

**Najważniejsze do zapamiętania:**

- JRWA trzeba rozumieć i stosować konsekwentnie – błędy w jego interpretacji przekładają się bezpośrednio na błędy w systemie.
    
- Każdy projekt AMODIT, który ma obsługiwać dokumentację urzędową, powinien zaczynać się od analizy JRWA klienta.
    

## 10. Dostęp do struktury JRWA i zasady nadawania uprawnień

Nie każda osoba w organizacji ma prawo przeglądać całe drzewo JRWA ani zakładać sprawy w dowolnej klasie.

Zasady dostępu wynikają wprost z logiki kancelaryjnej oraz z wymogów bezpieczeństwa informacji i RODO.

Zarówno w systemach EZD, jak i w rozwiązaniach takich jak AMODIT, dostęp do klas JRWA musi być ściśle powiązany z rolą i zakresem obowiązków pracownika.

### 10.1 Zasada ogólna – dostęp według roli i komórki organizacyjnej

JRWA klasyfikuje dokumenty rzeczowo, ale uprawnienia do pracy w ramach tej klasy są przydzielane organizacyjnie.

Pracownik księgowości nie może zakładać spraw w klasach dotyczących kadr czy marketingu — tak samo, jak dział HR nie powinien mieć wglądu w sprawy finansowe.

System EZD (i każdy system go wspierający) musi rozróżniać:

- widoczność drzewa JRWA,
    
- prawo do zakładania spraw,
    
- prawo do wglądu lub edycji akt,
    
- prawo do dekretacji lub zatwierdzania dokumentów.
    

Uprawnienia wynikają z przynależności do komórki organizacyjnej, stanowiska oraz ewentualnych pełnionych ról (np. zastępstwo, administrator kancelaryjny, archiwista).

### 10.2 Ograniczanie widoczności drzewa JRWA

W praktyce oznacza to, że użytkownik systemu widzi jedynie te gałęzie JRWA, które dotyczą jego komórki organizacyjnej.

Podczas zakładania sprawy system powinien prezentować wyłącznie te klasy JRWA, do których dana jednostka ma przypisane prawo tworzenia akt.

Taki model jest zgodny z zasadą **„need to know”** – pracownik widzi tylko to, co jest mu niezbędne do pracy.

W AMODIT można to odwzorować poprzez:

- przypisanie klas JRWA do grup użytkowników lub działów,
    
- definiowanie widoczności rejestrów spraw według komórki organizacyjnej,
    
- kontrolowanie dostępu do procesów (np. „Korespondencja przychodząca” tylko dla sekretariatu).
    

### 10.3 Uprawnienia specjalne i kontekstowe

Niektóre osoby (np. dyrektorzy, audytorzy, archiwiści) mogą posiadać szerszy dostęp — np. w trybie przeglądania całego drzewa JRWA, ale bez prawa edycji lub tworzenia spraw.

Z kolei administratorzy systemowi posiadają dostęp techniczny, ale nie merytoryczny (nie mogą ingerować w treść akt).

Instrukcje kancelaryjne (zarówno LOT, jak i Rozporządzenie) potwierdzają tę zasadę, wskazując, że użytkownik systemu ma dostęp tylko w zakresie niezbędnym do wykonywania swoich obowiązków.

**Najważniejsze do zapamiętania:**

- JRWA jest wspólne dla całej organizacji, ale dostęp do jego klas jest ściśle ograniczony.
    
- Pracownik widzi tylko te klasy, które dotyczą jego obowiązków służbowych.
    
- W AMODIT zasada ta powinna być odzwierciedlona przez przypisanie klas JRWA do komórek organizacyjnych, ról i poziomów dostępu.
    

## 11. Cyfrowa teczka akt i praktyki EZD (2025–2028)

Transformacja do EZD nie jest już pytaniem „czy?”, ale „jak?”. Według zapowiedzi rządowych i strategii cyfryzacji, od **1 stycznia 2028 r.** wszystkie podmioty realizujące zadania publiczne mają dokumentować przebieg załatwiania spraw w **systemach klasy EZD** (nie oznacza to obowiązku użycia konkretnego produktu, ale klasy rozwiązań).

To jest na razie tło strategiczne i kontekst dla LOT, który – jak ustaliliśmy w Rozdziale 2 – działa obecnie w systemie tradycyjnym.

### 11.1 Czym jest „cyfrowa teczka akt”

W modelu cyfrowym teczka akt to **byt logiczny** w systemie: powiązane dokumenty elektroniczne + **metadane**, które umożliwiają wyszukiwanie, kontrolę i długotrwałe przechowanie. W pojęciach rozporządzenia mieści się tu:

- **akta sprawy** – kompletny, chronologiczny zapis postępowania,
    
- **metadane** – usystematyzowane informacje (np. data wpływu, nadawca, znak sprawy, JRWA),
    
- **odwzorowanie cyfrowe** – skan dokumentu papierowego, powiązany z oryginałem.
    

Dla nas, jako firmy wdrażającej AMODIT, oznacza to, że „teczka” nie jest folderem plików, tylko **zdefiniowanym obiektem** z regułami: JRWA, znak sprawy, kategorie archiwalne, wersjonowanie i ślad czynności.

### 11.2 Integralność i korekta błędów

System EZD dokumentuje przebieg sprawy. To wymaga **integralności zapisu** – dokumentu nie „usuwamy”, tylko:

- **anulujemy** lub **oznaczamy jako błędny** (z uzasadnieniem),
    
- ewentualnie **przepisujemy** do właściwej sprawy z pełnym śladem audytowym,
    
- zachowujemy historię wersji i działań użytkowników.
    

To godzi wymogi dowodowe z praktyczną potrzebą korygowania pomyłek.

### 11.3 Rola JRWA w cyfrowej teczce

Każda sprawa **musi zostać przypisana** do właściwej klasy JRWA – z tego wynikają znak sprawy i kategoria archiwalna. W systemie klasy EZD klasyfikacja następuje **na początku** (z opcją późniejszej korekty na podstawie uprawnień i ścieżek akceptacji), a nie „na końcu”, jak bywało w praktykach papierowych.

**Najważniejsze do zapamiętania:**

- Przejście na EZD (po 2028 r.) jest standardem, do którego LOT będzie musiał się dostosować.
    
- „Teczka cyfrowa” to nie folder, lecz obiekt z metadanymi, regułami JRWA i pełnym audytem.
    

## 12. Przypisywanie spraw do teczek JRWA w AMODIT

Jednym z najważniejszych momentów w pracy użytkownika jest **decyzja o tym, do której teczki JRWA przypiąć daną sprawę**.

Od ergonomii tego działania zależy, czy klasyfikacja będzie dla użytkownika naturalna, czy stanie się barierą.

### 12.1 Logika kancelaryjna – kiedy i kto decyduje

Zgodnie z zasadami kancelaryjnymi:

- każda sprawa (czyli case w AMODIT) **powinna mieć przypisaną klasę JRWA** już na etapie rejestracji,
    
- ale **nie zawsze wiadomo od razu**, czy sprawa należy do istniejącej teczki, czy wymaga utworzenia nowej.
    

Dlatego decyzja o przypisaniu sprawy do teczki JRWA **musi zapaść najpóźniej w momencie rejestracji**, lecz może być **uszczegółowiona później**, jeśli `Teczka_sprawy` jeszcze nie istnieje.

### 12.2 Logika systemowa w AMODIT – trzy warianty

#### Wariant A – przypisanie przy rejestracji sprawy

Najbardziej naturalny scenariusz:

1. Użytkownik rejestruje nową sprawę (np. pismo przychodzące).
    
2. W formularzu widzi pole **„Teczka sprawy JRWA”** (lookup/picker).
    
    - może wybrać istniejącą teczkę z listy,
        
    - albo kliknąć **„➕ Utwórz nową teczkę JRWA”**, co otwiera mini-kreator teczki.
        

- Po zapisaniu sprawy system automatycznie wiąże ją z teczką i uzupełnia symbol JRWA oraz kategorię archiwalną.
    

#### Wariant B – przypisanie w trakcie obiegu

Niektóre procesy (np. Umowy, Projekty, Reklamacje) pozwalają na podjęcie decyzji dopiero po kilku krokach.

1. Pole „Teczka sprawy JRWA” jest nieobowiązkowe przy rejestracji.
    
2. W wybranym etapie procesu (np. „Weryfikacja merytoryczna”) dostępna jest akcja **„Przypisz do teczki JRWA”**.
    
3. Użytkownik wybiera teczkę z listy lub tworzy nową.
    

#### Wariant C – przypisanie automatyczne przez reguły systemowe

Dla procesów o przewidywalnych strukturach system może przypinać sprawy automatycznie, np.:

- do jedynej aktywnej teczki w danej klasie i roku,
    
- według rozpoznanych metadanych (np. numer projektu, kontrahent).
    

### 12.3 Najlepszy moment przypisania (rekomendacja)

| Typ procesu | Moment przypisania | Kto decyduje |

| Korespondencja, wnioski, pisma | podczas rejestracji | sekretariat / użytkownik rejestrujący |

| Umowy, projekty, inwestycje | po weryfikacji merytorycznej | pracownik merytoryczny / koordynator |

| Procesy powtarzalne (np. faktury, reklamacje) | automatycznie przez reguły | system (wg klasy JRWA i metadanych) |

### 12.4 Role decyzyjne i odpowiedzialność

| Rola | Zakres decyzji |

| Użytkownik merytoryczny | Wybiera lub tworzy teczkę przy pracy ze sprawą. |

| Koordynator kancelaryjny | Nadzoruje poprawność przypisań, może je korygować. |

| Archiwista | Weryfikuje powiązania przy przekazywaniu do archiwum. |

| Administrator JRWA | Definiuje reguły przypisania automatycznego i zakres uprawnień. |

### 12.5 Implementacja w AMODIT

- Formularz sprawy zawiera pole **„Teczka sprawy JRWA”** (lookup).
    
- Pod polem dostępny jest przycisk **„➕ Utwórz nową teczkę JRWA”**, który otwiera uproszczony formularz.
    
- Po zapisaniu, relacja **Sprawa ↔ Teczka_sprawy** jest dwukierunkowa.
    
- Na formularzu `Teczka_sprawy` dostępny jest raport **„Zawartość teczki”**, pokazujący powiązane sprawy.
    

**Najważniejsze do zapamiętania:**

- System AMODIT powinien integrować decyzję o przypięciu sprawy do teczki z naturalnym momentem pracy użytkownika – tam, gdzie i tak rejestruje lub klasyfikuje dokument.
    
- Nie tworzymy osobnego procesu klasyfikacji JRWA – **wplatamy wybór teczki w rytm pracy użytkownika.**
    

## 13. Cykl życia po zamknięciu sprawy: Archiwum Zakładowe (AZ)

_(Ten rozdział został dodany, aby uzupełnić Kompendium o procesy wynikające z Instrukcji Archiwalnej LOT)_

Zrozumienie JRWA i prowadzenia spraw to połowa sukcesu. Równie ważne jest, co dzieje się ze sprawą **po jej zamknięciu**. Tu kluczowe role odgrywają "Instrukcja kancelaryjna LOT S.A." (Rozdział 8) oraz "Instrukcja w sprawie organizacji i zakresu działania archiwum zakładowego LOT S.A." (zał. 2 do Uchwały 3-2025-BA).

AMODIT musi wspierać te procesy, aby zapewnić ciągłość obiegu.

### 13.1 Przekazywanie akt do Archiwum Zakładowego (AZ)

Sprawa nie trafia do AZ natychmiast po zamknięciu.

1. **Okres przechowywania w komórce:** Komórki organizacyjne przechowują akta przez **pełne dwa lata kalendarzowe** po roku, w którym sprawa została zakończona (Instrukcja Kancelaryjna LOT, § 37 ust. 1). Dopiero po tym czasie przekazuje się je do AZ.
    
2. **Spis zdawczo-odbiorczy:** Jest to kluczowy dokument transferu. AMODIT powinien wspierać jego generowanie. Zgodnie z § 39 Instrukcji Kancelaryjnej LOT, spis ten musi zawierać m.in.:
    
    - Listę teczek (oznaczenie komórki, symbol JRWA).
        
    - Tytuł teczki (nazwa z JRWA).
        
    - Daty skrajne (rok najwcześniejszego i najpóźniejszego pisma).
        
    - Kategorię archiwalną (A, B, BE, Bc).
        
    - Spis sporządza się osobno dla materiałów archiwalnych (A) i dokumentacji niearchiwalnej (B).
        
3. **Odmowa przejęcia przez AZ:** Archiwista ma prawo odmówić przejęcia dokumentacji (§ 37 ust. 4 Instrukcji Kancelaryjnej LOT), jeśli jest ona nieuporządkowana, błędnie zaklasyfikowana lub spis zawiera błędy.
    
    - _Implikacja dla AMODIT:_ System musi posiadać **walidacje** i **statusy** (`Do przekazania`, `Zatwierdzone przez AZ`, `Odrzucone przez AZ`), aby zarządzać tym procesem.
        

### 13.2 Ewidencja i przechowywanie w Archiwum Zakładowym

Po zaakceptowaniu spisów zdawczo-odbiorczych, Archiwista przejmuje dokumentację i nadaje jej **sygnaturę archiwalną** (Instrukcja Archiwalna LOT, § 15 ust. 2 pkt 5).

Sygnatura ta (np. `numer spisu / numer pozycji ze spisu`) jest nowym "adresem" teczki w archiwum. AMODIT powinien mieć pole na przechowywanie tej sygnatury, aby umożliwić szybkie odnalezienie teczki papierowej.

Archiwista prowadzi własne ewidencje (wykaz spisów zdawczo-odbiorczych, ewidencję udostępnień), które AMODIT może wspierać lub integrować.

### 13.3 Udostępnianie, wycofywanie i brakowanie

Teczka w AZ "żyje" – może być potrzebna pracownikom lub brakowana.

**1. Udostępnianie (Rozdział 8 Instrukcji Archiwalnej LOT)**

Proces ten musi być precyzyjnie odwzorowany w AMODIT zgodnie z ustaleniami (transkrypcja z 5.11.2025):

- **Jeden proces (Wniosek):** Zamiast tworzyć osobne procesy, AMODIT powinien udostępniać **jeden proces "Wniosek o udostępnienie akt z AZ"**.
    
- **Wybór formatu:** Wniosek ten musi zawierać pole wyboru (np. checkbox) pozwalające określić, o jaką formę wnioskuje pracownik:
    
    - **Dostęp do wersji elektronicznej** (skanu).
        
    - **Wypożyczenie wersji papierowej** (oryginału).
        
- **Dwie ścieżki akceptacji:** Proces musi kierować wniosek do odpowiedniego akceptanta (zgodnie z § 26 Instrukcji Archiwalnej i ustaleniami ze spotkania):
    
    - **Wnioskodawca wewnętrzny (pracownik LOT):** Wniosek trafia do akceptacji **Kierownika Komórki**, która pierwotnie wytworzyła akta.
        
    - **Wnioskodawca zewnętrzny (np. sąd, organ, obywatel):** Wniosek (zarejestrowany w AMODIT jako pismo przychodzące) trafia do akceptacji **Kierownika Jednostki** (Prezesa / Członka Zarządu).
        
- **Realizacja przez Archiwistę (Różne mechanizmy):**
    
    - **Dla formatu elektronicznego:** Archiwista nadaje wnioskodawcy (lub grupie osób) czasowy dostęp do akt w AMODIT. System **automatycznie cofa uprawnienia** po upływie terminu (np. 30 dni).
        
    - **Dla formatu papierowego:** Archiwista fizycznie wydaje teczkę, a w AMODIT odnotowuje fakt jej wypożyczenia (kto, co, data). Po fizycznym zwrocie oryginału, Archiwista musi **ręcznie "odhaczyć" (potwierdzić) zwrot** w systemie.
        
- **Ewidencja:** AMODIT musi prowadzić pełną ewidencję udostępnień (§ 29 Instrukcji Archiwalnej), rejestrując każdy wniosek, akceptację, wydanie i zwrot.
    

**2. Wycofywanie (Rozdział 9 Instrukcji Archiwalnej LOT)**

- Jeśli sprawa musi zostać **wznowiona**, komórka merytoryczna wnioskuje o **wycofanie** akt z AZ (§ 30).
    
- Odbywa się to na podstawie **protokołu** (§ 31).
    
- _Implikacja dla AMODIT:_ Musi istnieć proces systemowy pozwalający na formalne "wycofanie" teczki z ewidencji AZ i przywrócenie jej do stanu "w obiegu" w komórce merytorycznej.
    

**3. Brakowanie (Rozdział 10 Instrukcji Archiwalnej LOT)**

- Dotyczy dokumentacji niearchiwalnej (kat. B), której minął okres przechowywania.
    
- Archiwista inicjuje proces, typując dokumentację i tworząc **spisy dokumentacji do wybrakowania** (§ 32).
    
- Kierownicy komórek opiniują te spisy (mogą wydłużyć okres przechowywania).
    
- Całość wymaga zgody Archiwum Państwowego.
    
- _Implikacja dla AMODIT:_ System musi wspierać **typowanie** (np. raport "Teczki do brakowania w tym roku"), generowanie spisów i śledzenie statusu akceptacji.
    

**Najważniejsze do zapamiętania (Procesy AZ):**

- AMODIT musi wspierać nie tylko tworzenie spraw, ale cały ich cykl życia, włączając w to: przekazanie do AZ (spis zdawczo-odbiorczy), ewidencję (sygnatura), udostępnianie (wniosek i ewidencja), wycofywanie (protokół) i brakowanie (spisy).
    
- Logika ta jest precyzyjnie opisana w **Instrukcji Kancelaryjnej (zał. 1)** i **Instrukcji Archiwalnej (zał. 2)** do Uchwały Zarządu LOT nr 3-2025-BA.



## 14. ADE – integracja AMODIT z Archiwum Dokumentów Elektronicznych

### 14.1. Cel i kontekst
**Archiwum Dokumentów Elektronicznych (ADE)** to państwowy system przyjmowania, walidacji, przejmowania i udostępniania materiałów archiwalnych w postaci elektronicznej. Po stronie jednostek (np. LOT) rolą systemu dziedzinowego/EZD (AMODIT) jest **przygotowanie i przekazanie zgodnych paczek archiwalnych** oraz obsługa formalnego procesu przekazania (wniosek, statusy, protokoły). Na portalu publicznym ADE udostępniono narzędzia wspierające stronę „format-first”: **Walidację paczki archiwalnej** i **Wizualizację paczki**. 

### 14.2. Co jest publiczne, a co partner‑gated
- **Publicznie dostępne**: definicje i materiały dot. paczki archiwalnej, słowniczek pojęć, narzędzia walidacji/wizualizacji oraz schematy XSD (m.in. **wniosek o przekazanie**, **JRWA jako załącznik do wniosku**). citeturn0search9turn0search10turn0search0turn0search14turn0search4turn0search8  
- **Dostęp ograniczony (po zawarciu współpracy)**: pełna **„Dokumentacja interfejsu … (API EZD)”** opisująca endpointy, statusy, mechanizmy uwierzytelniania. NDAP/NAC prowadzą integracje w modelu partner-gated (zaproszenia dla producentów systemów EZD). 

> **Wniosek praktyczny:** zanim uzyskamy dostęp do specyfikacji API, **większość prac** po stronie AMODIT i LOT powinna skupić się na poprawnym **generowaniu i walidowaniu paczek** oraz na mapowaniu metadanych do XSD.

### 14.3. „Paczka archiwalna” – kluczowe pojęcia i struktura
- **Definicja**: „nieskompresowany zbiór plików o znanej strukturze” zawierający **dokumenty elektroniczne** oraz opisujące je **metadane**; każdy dokument musi przynależeć do co najmniej jednej **sprawy** (lub innej grupy), a metadane muszą być spójne ze schematami XSD. 
- **Warstwa katalogowa (najwyższy poziom)**: **`dokumenty/`**, **`metadane/`**, **`sprawy/`**. To „twarda” reguła opisana w oficjalnych materiałach ADE. 

**Implikacje dla AMODIT:**  
1) Eksportujemy pliki treści do `dokumenty/` (zachowując ewentualne podstruktury dla dokumentów wieloplikowych). 2) Generujemy XML metadanych w `metadane/` zgodnie z bieżącym XSD. 3) Tworzymy metadane spraw/teczek w `sprawy/` i pilnujemy relacji dokument↔sprawa. 

### 14.4. Narzędzia: walidacja, wizualizacja, schematy XSD
- **Walidator paczki** – służy do techniczno‑logicznej weryfikacji paczki (używać w cyklu CI/CD przed jakąkolwiek wysyłką).  
- **Wizualizacja paczki** – podgląd merytoryczny do kontroli zawartości przez archiwistę zakładowego/koordynatora. 
- **Schematy XSD** – udostępnione publicznie m.in.:  
  • **Wniosek o przekazanie materiałów** (XSD),  
  • **JRWA jako załącznik do wniosku** (XSD),  
  • **Struktura układu metadanych** (kolejne wersje, np. *Metadane‑1.7*). 

> **Dobre praktyki:** „zamknij” wersje XSD w repo (lock na konkretnych wydaniach) i uruchom **testy kontraktowe** – każde wydanie paczki przechodzi walidację offline oraz sanity‑check wizualizacji.

### 14.5. Model procesu przekazania (UI ↔ M2M)
Formalny proces obejmuje: **złożenie wniosku o przekazanie**, weryfikację/akceptację po stronie Archiwum Państwowego, **przekazanie paczki**, walidacje po stronie ADE i **protokoły przejęcia**. ADE przewiduje zarówno realizację manualną (Portal Jednostki/Archiwisty), jak i **automatyzację przez API** po stronie systemu EZD. 

> **Asynchroniczność:** po stronie API należy spodziewać się statusów i dłuższych operacji (polling/ew. notyfikacje) – dokładną semantykę statusów określa niepubliczna dokumentacja API EZD. 

### 14.6. Dostęp i uwierzytelnianie
- **Portale i szkolenia:** publiczny portal informacyjny **ade.gov.pl**, **Portal Jednostki** (konto instytucjonalne), **Portal Archiwisty**, oraz **Platforma szkoleniowa** pod adresem **ps.ade.gov.pl**. citeturn1search1turn1search5turn1search0  
- **API (M2M):** szczegóły uwierzytelniania/endpointów przekazywane są po stronie NDAP/NAC w trybie współpracy z producentami systemów – przyjmujemy założenia projektowe dopiero po otrzymaniu specyfikacji. 

### 14.7. Zakres prac po stronie AMODIT (LOT)
1) **Generator paczek (format‑first):** mapowanie metadanych AMODIT ↔ XSD (dokumenty, sprawy/teczki, JRWA), budowa structure `dokumenty/metadane/sprawy`, nadawanie powiązań dokument↔sprawa. 
2) **Walidacja/Wizualizacja w pipeline:** automatyczne kroki CI (walidator), kontrola merytoryczna (wizualizacja) – blokada release’u na błędach walidacji. 
3) **Wniosek o przekazanie (XSD):** generowanie wniosku i załączników (np. JRWA) jako pre‑krok do teletransmisji paczki.  
4) **Klient API ADE (po otrzymaniu specyfikacji):** obsługa cyklu: *utwórz/uzupełnij wniosek → przesył paczki → odczyt statusów → pobranie protokołów*. (Technikalia: limity rozmiaru, wznowienia, idempotencja – zgodnie ze specyfikacją M2M).   
5) **Bezpieczeństwo i operacje:** zarządzanie kluczami/sekretami, whitelisting adresów ADE, ślad audytowy, retencja logów, monitoring błędów. 

### 14.8. Zależności od JRWA i AZ
- ADE dotyczy **materiałów archiwalnych** (kategoria „A”) – plan przekazywania i decyzje klasyfikacyjne wynikają z JRWA i polityk archiwalnych. NDAP wskazuje zasady przekazywania dokumentów elektronicznych do właściwego AP. 
- W AMODIT zapewniamy zgodność metadanych JRWA, a cykl AZ (spisy zdawczo‑odbiorcze, ewidencja) pozostaje spójny z rozdz. 13 – przekaz do ADE jest **osobnym strumieniem** dla materiałów „A”, realizowanym na podstawie wniosku. 

### 14.9. Częsty fałszywy trop: „ADE = e‑Doręczenia” (NIE)
„Adres do e‑Doręczeń (e‑Doręczenia)” to **inny system** i inne API (OpenAPI/OIDC/signed JWT); dotyczy korespondencji, nie przekazywania paczek archiwalnych do archiwów państwowych. Nie używamy dokumentacji e‑Doręczeń do integracji z ADE. 

### 14.10. Checklista wdrożeniowa (LOT → AMODIT)
- [ ] Zatwierdzony **słownik JRWA** i reguły kompletności (które sprawy/dokumenty wchodzą do materiałów „A”).  
- [ ] Mapowanie **pól AMODIT → XSD** (dokumenty, sprawy/teczki, JRWA).  
- [ ] Implementacja **generatora paczek** i **wniosku (XSD)**; wersjonowanie schematów. 
- [ ] **Walidacja** (automaty + ręczna wizualizacja) w procesie QA.   
- [ ] Uzgodnienia formalne z NDAP/NAC (dostęp **API EZD**, środowiska/konta).   
- [ ] Implementacja **klienta API** i testy z archiwum właściwym dla LOT (po otrzymaniu specyfikacji).  
- [ ] Monitorowanie, audyt, procedury błędów/ponowień.

**Najważniejsze do zapamiętania:**  
- ADE to nie „tylko API” – **centrum ciężkości** jest w **poprawnym formacie paczki** i zgodności z XSD. 
- Szczegóły transportu/uwierzytelniania są przekazywane po nawiązaniu współpracy (partner‑gated).   
- Walidacja i wizualizacja to **obowiązkowy etap** QA przed przekazaniem do właściwego AP. 
