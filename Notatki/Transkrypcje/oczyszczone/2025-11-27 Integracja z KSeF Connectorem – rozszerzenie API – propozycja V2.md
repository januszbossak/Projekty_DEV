**Integracja z KSeF Connectorem – rozszerzenie API – propozycja V2**  
  
  **Adrian Kotowski**
**- nowy kontroler API zamiast rozbudowy istniejącego handlera ashx**   
rezygnacja z niewspieranej technologii, brak wsparcia dla handlerów w .NET Core w przypadku migracji z .NET Framework

- **nowy endpoint z dwiema metodami POST i PUT**  
niemalże identyczna struktura żądań co w przypadku starego handlera + zwracanie ID sprawy + możliwość przekazywania CustomAttributes  
wykorzystanie wspólnego kodu

**- endpoint będzie „należał do rodziny endpointów REST API Amodit”**  
wspólny prefiks w ramach routingu: **restapi/**integration/ksef/v1  
nowy wzorzec dla tworzenia innych endpointów pod dedykowane integracje

**- endpoint będzie miał niezależne uwierzytelnienie niż REST API Amodit**  
wykorzystywany będzie ten sam (niewygasający) token, który był używany poprzez handler  
**endpoint nie będzie podlegał licencjonowaniu** tak jak pozostałe endpointy w REST API Amodit

**- zachowana kompatybilność wsteczna**  
stary handler będzie dalej funkcjonował   
KSeF Connector będzie sprawdzał czy dostępny jest nowy endpoint, a jak nie to będzie wywoływał stary handler (ustalone z zespołem P. Wągla) 
**Piotr Buczkowski ** zatwierdził zmiany mogę wrzucić nawet za chwilę, jest tego kilka linijek