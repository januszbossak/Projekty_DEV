[[2024-04-16 wtorek]]
Omawialiśmy dzisiaj koncepcję uproszczonego okna dialogowego.
Dyskusja pokazała że są dwie potrzeby, dwa zastosowania.

1. Proste okno dialogowe
w tej koncepcji nie ma odrębnego procesu, ani reguł.
Okno dialogowe jest w zasadzie rozwinięciem koncepcji "okna potwierdzania reguły ręcznej" gdzie dodane byłyby opcje wyświetlania pól do wypełnienia.
pola proste jak tekst, data, liczba, użytkownik, może słownik.
tych pól nie trzeba by definiować na formularzu.
byłyby definiowane w wywołaniu okna dialogowego.

cechy:
- pozwala obsłużyć bardzo proste sytuacje gdzie np trzeba podać kilka danych np imię nazwisko, wybrać jakąś kategorię, datę itp. która natychmiast, po zamknięciu okna, się użyje.

2. Okno dialogowe na podstawie formularza
w tej koncepcji zakładamy, że istnieje definicja procesu z definicją formularza. 
to może być jakiś nowy typ procesu np "proces - formularz"
taki proces służyłby do generowania formularza, który użytkownik by wypełniał.
wywołanie z poziomu reguł procesu np funkcją ShowDialog("nazwa formularza", .... inne parametry)
takie wywołanie powodowaałoby otwarcie formularza, który użytkownik mógłby wypełnić
potrzebne by były akcje, które może użytkownik wykonać, ale to mogłoby działać jak w pkt 1 gdzie definiuje się akcje/przyciski
albo
mogłłyby one pochodzić z definicji tego "procesu - formularza"
Wywołanie okna nie powodowało by utworzenia sprawy, w rozumieniu nadania jen numeru caseID i zapisaniu w bazie danych.
Raczej widzimy to jako formularz do wypełnienia, a po wypełnieniu i zamknięciu okna i powrocie do głównegho formularza, w jakiś sposób dane uzyskane w oknie musiałyby być skonsumowane. Przykładow przypisane do pól na formularzu głównym. Takie okno mogłoby zwracać obiekt JSON.
Okno dialogowe musiałoby być możliwie uproszczone, bez większości obecnych elementów formularza sprawy, prawego panelu, załączników, spraw powiązanych, historii itp.

3. Okno dialogowe na podstawie procesu
w tym przypadku, zakładamy, że istnieje pełnoprawny proces, z formularzem, regułami, diagramem itd.
Różnica do koncepcji w pkt 2 jest taka, że tu sprawy powstają i są zapisywane w bazie danych.
Podobieństwo natomiast do pkt 2 jest w części dotyczącej wyglądu okna dialogowego z formularzem. Powinno być ono maksymalnie uproszczone i pozbawione większości elementów normalnego okna sprawy.
