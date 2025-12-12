WinRaR w wersji < 7.12 Beta i podatności

Łukasz Poskrobko 

Dostaliśmy właśnie alert z Microsoft Defender, że w organizacji mamy **10 urządzeń**, które posiadają właśnie tą wersję aplikacji WinRar. Prośba o jej usunięcie albo zaktualizowanie do najnowszej wersji (7.12 Beta lub nowszej) jak najszybciej.

Do czasu pełnej aktualizacji nie otwierajmy archiwów z nieznanych źródeł (szczególnie z maili i stron www) i blokujmy rozszerzenia .rar/.zip z zewnątrz na bramce pocztowej tam, gdzie to możliwe

WinRar w tych wersjach umożliwia zdalne wykonanie kodu (RCE) poprzez błąd typu directory traversal przy rozpakowywaniu specjalnie spreparowanego archiwum i ma **ocenę CVSS 7,8 (High).**

## **Co to za podatność:**

CVE-2025-6218 to luka w obsłudze ścieżek plików w RARLAB WinRAR – archiwum może zawierać złośliwe ścieżki (np. z sekwencjami typu „../”), które podczas rozpakowywania powodują zapis plików poza docelowym katalogiem, w tym nadpisanie plików systemowych lub startowych użytkownika

**Po otwarciu takiego archiwum atakujący może doprowadzić do uruchomienia swojego kodu z uprawnieniami aktualnie zalogowanego użytkownika, co może skutkować kradzieżą danych, instalacją malware lub uzyskaniem trwałego dostępu.**

## Zakres i status:

Podatność dotyczy określonych wersji WinRAR dla Windows (głównie przed wersją 7.12 Beta 1, w której wprowadzono poprawkę).

Luka jest aktywnie wykorzystywana przez różne grupy atakujące, a agencje takie jak CISA zalecają jej niezwłoczne załatanie; w części środowisk rządowych wyznaczono nawet twarde terminy na aktualizację.


- [ ] ## Działania po stronie DEV w odniesieniu do systemu AMODIT
U nas w DEV do sprawdzenia też czy to nie dotyczy bibliotek z których korzystamy do obsługi ZIP. Pewnie nie, ale warto sprawdzić. Marek Dziakowski w TC i w AMODIT

Odpowiedź: korzystamy z 7zip

Wniosek: Przeprowadzano weryfikację pod kątem potencjalnego występowania podatności w AMODIT. Używana przez AMODIT bibliotek 7zip, która jest inna niż w notatce Łukasza Poskrobko o WinRar