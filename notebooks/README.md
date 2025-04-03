Her gjøres oppgavene 
Oppgave 1: Sett opp utviklingsmiljø
Vi har laget en repository i github og koblet på alle gruppemedlemmene. Alle har laget sin egen .venv. Etterhvert som vi har funnet ut hvilke biblioteket etc. vi må installere og importere for å løse oppgaven, vil vi opprette en resources-fil der alle nødvendige installasjoner for å kjøre programmet vil være listet.

Oppgave 2: Datainnsamling
Vi hentet ut hver vår client_id ved å lage bruker her: https://frost.met.no/howto.html
Vi har kopiert kode for å hente ut dataen: https://frost.met.no/python_example.html

Vi har hentet data fra Metrologisk institutt. Andre nettsider vi var inne på og vurderte å hente ut data fra var norske klimaservicesenter og openweathermap.org. Vi valgte å bruke Metrologisk institutt fordi de, som et statlig institutt, er en pålitelig kilde og er lett tilgjengelig. Vi synes også det var praktisk at de hadde en API vi synes var lett å finne ut av. I tillegg har de mange store datasett, så det var lett å finne noe som var relevant for vår oppgave. 

For å få tilgang på dataene krevdes det at vi lagde hver vår bruker på siden, og fikk mottatt hver vår klientkode/ID. Disse har vi lagret i hver vår lokale ENV-fil. Det at metrologisk institutt bruker klientkoder/ID ser vi på en tegn at nettsida har tatt nødvendige forbehold for å sikre sine data og bruken av disse. 

Vi har lastet ned dataen med bruk av API. API gjør at vi ikke trenger å manuelt endre datasettet ved endringer av innholdet, som er grunnen til at vi valgte dette framfor å laste ned en statisk CSV-fil. Vi valgte å bruke Metrologisk Institutt sin egen kode for å laste ned datasettetfor å komme i gang med arbeidet rasket mulig. Dette gjør imidlertid at vi har brukt en del tid på å tolke og tilpasse koden. Dataen vi hentet ut ved hjelp av API-en har vi lagret i JSON-format. Denne filtypen ligner en Python Dictionary og fungerer bra for store datasett. 

Frost-datasettet inneholder mange forskjellige typer data. De mest aktuelle for oss er nedbør, temperatur, vind og tidspunkt. Dette er elementId, value, unit, timeOffset og referenceTime i datasettet. Vi vil bruke disse til å gjøre en grundig analyse av datasettet. Vi planlegger å regne ut gjennomsnitt for hver enkelt type data, samt å utforske ulike sammenhenger mellom dem. Vi ønsker også å se om vi kan forutsi fremtidige resultater ut ifra datagrunnlaget vi allerede har ved bruk av en maskinlæringmodell, i tillegg til å lage grafer for ulike utvalg av data.


Oppgave 3: Databehandling
For å identifisere manglende verdier i datasettet brukte vi Pythonbiblioteket missingno. Ved å representere datasettets verdier i et søylediagram fant vi ut at det ikke var noen verdier som manglt av de attributtene vi skal bruke i oppgaven. Vi har også brukt .duplicated for å avdekke duplikater i datasettet. Vi hadde hverken manglende verdier eller duplikater.

Vi kunne bruke list comprehensions for å for eksempel multiplisere eller dividere data, dele opp dataen i ulike deler eller legge sammen ulike koloner. Vi har ikke hatt bruk for å multiplisere eller dividere og vi brukte SQL for å dele opp dataen. 

Pandas SQL er mye lettere å lese enn tradisjonelle Pandas-operasjoner. Ved bruk av SQL kan vi lettere se hva vi spørr om. Dette er relevant, fordi det er gruppeoppgave og siden vi har mulighet til å jobbe på hver vår plass uten å diskutere hva tankene våre er, er det viktig at koden er lett å lese for alle. Vi har brukt SQL for å lese temperatur, nedbør og vind for seg selv og vi har deretter lagt disse inn i egne filer.

Spesifikke uregelmessigheter i dataene vi kan møte på er ekstremt høye eller lave temperaturer, datoer som ikke eksisterer, ekstremt nedbør eller ekstrem vind. Hvis vi møter på disse kommer vi til å sette inn veridene fra en rad eller etter. Hvis vi møter på en dato som ikke eksisterer, kommer vi til å se rundt om det er noen som mangler og eventuelt flytte på den, hvis ikke kommer vi til å slette den. 