#### main
Denne notebooken har tidligere hetet mappe_del_1. Vi har i slutten av prosessen valgt å skifte navn til main. 
Her har vi lastet ned datasettet med API. Vi har så jobbet for å bli kjent med datasettet. Dette er fila som må runnes først for at de andre notebookene skal fungere. 
Får å laste ned datasettet trengs også client-ID som vi har lagt inn i en .env-fil. Dere kan hente ut client-ID med å lage bruker her: https://frost.met.no/howto.html
Vi har så delt dataen i tre og lagt de i hver sin CSV-fil.

#### temperature
Her gjøres analysen for temperaturdataen. Vi har lastet inn temperature.csv fra data og jobbet med å forstå dataene. Vi har fylt inn manglende verdier, fjernet ekstreme verdier og gjort rede for duplikater. Den rensede dataen er lagt inn i en egen CSV-fil, og denne dataen er brukt for å gjøre resten av analysen. Vi har så visualisert dataen på flere ulike måter. Til slutt er det gjort en predikativ analyse.

#### precipitation
Her gjøres analysen for nedbørdataen. Vi har lastet inn precipitation.csv fra data og jobbet med å forstå dataene. Vi har fylt inn manglende verdier og fjernet ekstreme verdier. Den rensede dataen er lagt inn i en egen CSV-fil, og denne dataen er brukt for å gjøre resten av analysen. Vi har så visualisert dataen på flere ulike måter. Til slutt er det gjort en predikativ analyse.

#### wind
Her gjøres analysen for vinddataen. Vi har lastet inn wind.csv fra data og jobbet med å forstå dataene. Vi har fylt inn manglende verdier, fjernet ekstreme verdier og gjort rede for duplikater. Den rensede dataen er lagt inn i en egen CSV-fil, og denne dataen er brukt for å gjøre resten av analysen. Vi har så visualisert dataen på flere ulike måter. Til slutt er det gjort en predikativ analyse.

#### comparison
Her har vi brukt visualiseringer til å se om det er en sammenheng mellom de ulike datatypene.