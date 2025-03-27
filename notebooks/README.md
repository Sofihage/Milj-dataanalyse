Her gjøres oppgavene 
Oppgave 1:
Vi har laget utviklingsmiljø i github og delt mellom oss alle. Alle har laget sin egen .venv.

Oppgave 2:
Vi hentet ut hver vår client_id ved å lage bruker her: https://frost.met.no/howto.html
Vi har kopiert kode for å hente ut dataen: https://frost.met.no/python_example.html

Vi har hentet data fra Metrologisk institutt. Andre nettsider vi var inne på var norske klimaservicesenter og openweathermap.org. Vi valgte å bruke Metrologisk institutt, fordi de hadde en API vi synes var lett å finne ut av. Vi har også valgt de, fordi de er en pålitelig kilde. Metrologisk insitutt er statlig og er derfor lett å ha tillit og tilgang til de. Vi har alle laget vår egen bruker og fått vår egen client_ID. Disse har vi lagret i hver vår lokale ENV-fil. Det at metrologisk institutt bruker client_ID ser vi på en tegn at nettsida er trygg. De har i tillegg mange store datasett, så det var lett å finne noe relevant. 

Vi har lastet ned dataen med bruk av API. API gjør at vi ikke trenger å manuelt endre datasettet ved endringer av innholdet. Derfor valgte vi dette istedenfor for eksempel å laste ned en statisk CSV-fil. Vi valgte å bruke Metrologisk Institutt sin egen kode for å laste ned datasettet. Dette gjorde det fort å komme igang, men gjør at vi har brukt en del tid på å tolke og tilpasse koden. Inne i API-en har vi lagret dataen som JSON. Det er lignende en Python Dictionary og er god for store datasett. 

Frost-datasettet inneholder masse forskjellige typer data. De mest aktuelle for oss er nedbør, temperatur, vind og tidspunkt. Dette er elementId, value, unit, timeOffset og referenceTime i datasettet. Vi tenker vi kan bruke disse til å gjøre en grundig analyse av datasettet. Vi tenker vi kan regne ut gjennomsnitt, både for hver enkelt type data, men også finne noen sammen henger mellom de. Vi har også lyst til å se om vi kan finne fremtidige data ut ifra det vi allerede har og om vi kan lage grafer for alle de forskjellige dataene.  


Oppgave 3:
For å identifisere manglende verdier i datasettet brukte vi missingno biblioteket i Python. Vi laget det om til et søylediagram og fant ut at av de atributtene vi skal bruke i oppgaven var det ingen verdier som manglet. Vi har også brukt .duplicated for å finne ut om vi hadde noen duplikater i datasettet. Vi hadde hverken manglende verdier eller duplikater.

Vi kunne bruke list comprehensions for å for eksempel multiplisere eller dividere data, dele opp dataen i ulike deler eller legge sammen ulike koloner. Vi har ikke hatt bruk for å multiplisere eller dividere og vi brukte SQL for å dele opp dataen. 

Pandas SQL er mye lettere å lese enn tradisjonelle Pandas-operasjoner. Ved bruk av SQL kan vi lettere se hva vi spørr om. Dette er relevant, fordi det er gruppeoppgave og siden vi har mulighet til å jobbe på hver vår plass uten å diskutere hva tankene våre er, er det viktig at koden er lett å lese for alle. Vi har brukt SQL for å lese temperatur, nedbør og vind for seg selv og vi har deretter lagt disse inn i egne filer.

Spesifikke uregelmessigheter i dataene vi kan møte på er ekstremt høye eller lave temperaturer, datoer som ikke eksisterer, ekstremt nedbør eller ekstrem vind. Hvis vi møter på disse kommer vi til å sette inn veridene fra en rad eller etter. Hvis vi møter på en dato som ikke eksisterer, kommer vi til å se rundt om det er noen som mangler og eventuelt flytte på den, hvis ikke kommer vi til å slette den. 