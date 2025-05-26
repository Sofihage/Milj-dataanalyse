## Oppsettet til mappen
#### Data
I mappa med navnet data har vi lagret datasettet i flere mindre filer. Vi har først delt det inn i temperatur, nedbør og vind, og når vi har renset de ulike datasettene har vi lagret de i filene som begynner med clean_. 

#### Docs
I denne mappa har vi lagt KI-deklasjonene våre og refleksjonsnotatet. 

#### Notebooks
Det er her selve analysen har foregått. Vi har begynt med notebooken som heter main (tidligere mappe_del_1). Her har vi lastet ned datasettet med hjelp av API. Vi hentet ut hver vår client_id ved å lage bruker her: https://frost.met.no/howto.html. Vi har kopiert kode for å hente ut dataen: https://frost.met.no/python_example.html. Vi har lagret hver vår client-id i en .env fil. Vi har så blitt kjent med datasettet og delt det inn i tre deler: temperatur, vind og nedbør. 

For at resten av notebookene skal fungere er det derfor viktig at main blir kjørt først.

Hver del av datasettet har fått sin egen notebook der resten av analysen har foregått. Disse heter temperature, wind og precipitation. Her har vi jobbet med å forstå og visualisere dataen, i tillegg til at vi har gjennomført predikative analyser.

Til slutt har vi jobbet for å finne sammenhengene mellom dataene. Disse ligger i notebooken som heter comparison. Her har vi sett på om de ulike datasettene påvirker hverandre.

#### src
Her har vi lagt fila med alle våre felles funksjoner. Dette er funksjoner som alle bruker og de er videre forklart i README-fila til src.

#### tests
Her har vi gjennomført enhetstester for alle funksjonene i funksjonsfila.

## Vurderingskriterier
Hver oppgave har flere vurderingskriterier og siden alle oppgavene vi har svart på i mappen går litt over i hverandre har vi valgt å svare på de spørsmålene som står i vurderingskriteriene her. Dette er for å dokumentere hva som har blitt gjort i hver oppgave og for å vise hva vi har tenkt når vi har gjennomført oppgavene.

#### Oppgave 1: Sett opp utviklingsmiljø
Vi har laget en repository i github og koblet på alle gruppemedlemmene. Alle har laget sin egen .venv. Etterhvert som vi har funnet ut hvilke biblioteket etc. vi må installere og importere for å løse oppgaven, vil vi opprette en requirements-fil der alle nødvendige installasjoner for å kjøre programmet vil være listet.

#### Oppgave 2: Datainnsamling
Vi hentet ut hver vår client_id ved å lage bruker her: https://frost.met.no/howto.html
Vi har kopiert kode for å hente ut dataen: https://frost.met.no/python_example.html

Vi har hentet data fra Metrologisk institutt. Andre nettsider vi var inne på og vurderte å hente ut data fra var norske klimaservicesenter og openweathermap.org. Vi valgte å bruke Metrologisk institutt fordi de, som et statlig institutt, er en pålitelig kilde og er lett tilgjengelig. Vi synes også det var praktisk at de hadde en API vi synes var lett å finne ut av. I tillegg har de mange store datasett, så det var lett å finne noe som var relevant for vår oppgave. 

For å få tilgang på dataene krevdes det at vi lagde hver vår bruker på siden, og fikk mottatt hver vår klientkode/ID. Disse har vi lagret i hver vår lokale ENV-fil. Det at metrologisk institutt bruker klientkoder/ID ser vi på en tegn at nettsida har tatt nødvendige forbehold for å sikre sine data og bruken av disse. 

Vi har lastet ned dataen med bruk av API. API gjør at vi ikke trenger å manuelt endre datasettet ved endringer av innholdet, som er grunnen til at vi valgte dette framfor å laste ned en statisk CSV-fil. Vi valgte å bruke Metrologisk Institutt sin egen kode for å laste ned datasettet for å komme i gang med arbeidet raskest mulig. Dette gjør imidlertid at vi har brukt en del tid på å tolke og tilpasse koden. Dataen vi hentet ut ved hjelp av API-en har vi lagret i JSON-format. Denne filtypen ligner en Python Dictionary og fungerer bra for store datasett.

Frost-datasettet inneholder mange forskjellige typer data. De mest aktuelle for oss er nedbør, temperatur, vind og tidspunkt. Dette er elementId, value, unit, timeOffset og referenceTime i datasettet. Vi vil bruke disse til å gjøre en grundig analyse av datasettet. Vi planlegger å regne ut gjennomsnitt for hver enkelt type data, samt å utforske ulike sammenhenger mellom dem. Vi ønsker også å se om vi kan forutsi fremtidige resultater ut ifra datagrunnlaget vi allerede har ved bruk av en maskinlæringmodell, i tillegg til å lage grafer for ulike utvalg av data.

#### Oppgave 3: Databehandling
For å identifisere manglende verdier i datasettet brukte vi Pythonbiblioteket missingno. Ved å representere datasettets verdier i et søylediagram fant vi ut at det ikke var noen verdier som manglet av de attributtene vi skal bruke i oppgaven. Vi har også brukt .duplicated for å avdekke duplikater i datasettet. Vi hadde ikke manglende verdier i datasettet, men det inneholdt noen duplikater. Etter å ha telt gjennom alle referansetidene og funnet ut at hver referansetid skjer like mange ganger har vi konkludert med at duplikatene bare er at samme værtype, referansetid og tidsforskyvning har samme verdi. Derfor har vi latt duplikatene bli.

Vi kunne brukte list comprehensions blant annet for å finne ut hvilke værtyper vi har i datasettet.

Pandas SQL er mye lettere å lese enn tradisjonelle Pandas-operasjoner. Ved bruk av SQL kan vi lettere se hva vi spør om. Dette er relevant, fordi det er gruppeoppgave og siden vi har mulighet til å jobbe på hver vår plass uten å diskutere hva tankene våre er, er det viktig at koden er lett å lese for alle. Vi har brukt SQL for å lese temperatur, nedbør og vind for seg selv og vi har deretter lagt disse inn i egne CSV-filer.

Spesifikke uregelmessigheter i dataene vi kan møte på er ekstremt høye eller lave temperaturer, ekstremt nedbør eller ekstrem vind. Hvis vi møter på disse kommer vi til å filtrere dem ut og erstatte med verdiene fra en rad før eller etter. 


#### Oppgave 4: Dataanalyse
Vi kan bruke pandas og numpy til å beregne gjennomsnitt, median og standardavvik med å bruke noen av de innebygde funksjonene de har. For eksampel kan vi bare skrive np.median og så legge inn hva vi vil finne medianen til, for å bruke numpy til å regne ut medianen. Det samme gjelder gjennomsnitt og standardavvik. Gjennomsnitt og verdi er viktig for å kunne bli godt kjent med datasettet. For oss som har data om vær, viser gjennomsnittet og medianen hvilken verdi eller værmengde som er vanlig. Medianen skiller seg vekk fra gjennomsnitt, siden den ikke blir påvirket av de mest ekstreme verdiene i like stor grad. Standardavvik brukes for å finne verdier som kanskje ikke burde være med i analysen. For eksmpel har vi brukt 3*standardavviket ut fra hver side av gjennomsnittet for å finne ut hvilke verdier som ikke burde være med i analysen. 

Et eksempel på bruk av enkel statistisk analyse som har blitt gjennomført i vårt datasett er å sjekke om tidsforskyvning påvirker værtypen. Da finner vi gjennomsnittet av alle verdiene til hver av tidsforskyvningene og sammenligner dem.

Vi planlegger å fjerne de mest ekstreme verdiene til datasettet. Det bruker vi både gjennomsnittet og standardavviket til. Disse verdiene fjernes sånn at de ikke påvirker resten av analysen. For eksmepel så er det greit å fjerne de høyeste verdiene av vind når hvis det har vært en orkan som vanligvis ikke pleier å skje. Hvis disse tas med i analysen, gir påvirker det til å få en upålitelig analyse. I tillegg har vi brukt en del sunn fornuft. Vær er noe vi kjenner til og det er lett å forstå at om det for eksempel plutselig er 20 grader i januar er det noe som ikke stemmer. 

Vi har valgt å lage litt ulike visualiseringer for å støtte analysen. Vi har for eksempel visualisert de ulike verdiene eller de ulike tidsforskyvningene. Vi har også brukt gjennomsnitt eller andre visualiseringer for å bekrefte eller støtte opp til det som vises. For eksempelhar vi i temperatur og nedbør visualisert de ulike tidsforskyvningene som ulike farger og brukt gjennomsnitt til å bekrefte det som sees.


#### Oppgave 5: Visualiseringer
Vi har alle brukt scatterplot for å vise frem datasettene for temperatur, vind og nedbør. Vi prøvde oss frem med flere andre, men fant ut at det var best å bruke scatter. Datasettene er lagt opp sånn at det går gjennom året to ganger. Så først fra januar til desember og så en gjentakelse. Hvis vi for eksempel brukte linjediagram gjorde det at det kom en lang strek som gikk fra desember til januar. Selv om det er flere løsninger på det, for eksempel å sortere verdiene etter referansetid, valgte vi å heller bruke scatter. 

Vi har for det meste brukt matplotlib, men også litt seaborn. Bibliotekene har vært nyttige fordi de har gjort det mulig å lage mange ulike typer grafer på samme måte. For eksempel så lar de oss lage både linje, scatter og histogram veldig lett. Dette gjør at vi kan jobbe mer effektivt.

Vi valgte å legge til data der de manglet for å skape en kontinuitet. Med så mye data og flere verdier hver dag, er det derimot ikke sikkert at noen manglende verdier her og der hadde gitt mye utslag for visualiseringen. 

Prossessen med å bruke plotly for å lage interaktive visualiseringer er ganske lik matplotlib. Først må vi importere plotly.express. Vi må så velge type graf og gi informasjonen om datasettet, x og y aksene og om vi vil kan vi gi farge som lages ut ifra de ulike kolonnene i datasettet. For eksmepel om fargen settes til verdi blir grafen fargelagt i mange forskjellige farger som representerer de ulike verdiene. All den informasjonen plutter vi inn i en varibel som heter fig. Vi kan velge å gi navn til grafen med å bruke .update_layout. Grafen blir interaktiv og vi kan zoome inn og holde over de ulike punktene og så får vi informasjon om de.

Vi har også brukt Ipywidgets for å gi ulike valgmuligheter til brukeren. For eksempel å bytte farge i plotly-grafer eller vise frem lineær eller andregradsregresjon. For å gjøre det, har vi lagt plottet til grafen i en funksjon med valgmuligheten som et argument for grafen. For eksempel om det er en widget for å skifte farge, så står variabelen som 'color'. Så brukes ipywigdets sin interact til å lage ulike wigdets. Da skrives inn liste med valgmuligheter og gis samme navn som argumentet til grafen. En wigdet lages med den informasjonen som er gitt. Det er også mulig å bestemme selv hvilken type wigdets vi vil ha. Da legges det inn i en egen variabel det er legges inn hvilken type widgets som ønskes. Denne variabelen brukes på samme måte som tidligere.

Vi har alle brukt de samme typene visualiseringer. Det gjør at brukeren bare må sette seg inn i de ulike typene visualiseringer én gang og kan kjenne igjen visualiseringene senere. Der vi ser at grafene ikke gir de mest tydelige visualiseringene har vi valgt å sammenligne de med andre typer grafer for å vise at hvilken graf som brukes påvirker hvor lett det er å skjønne visualiseringen. Vi har også gjort vårt beste for å bruke ulike farger, men som fortsatt passer greit sammen. Det er for at grafene lett skal fange oppmerksomheten til brukerne.

#### Oppgave 6: Predikativ analyse
Som forklart tidligere har vi valgt å bruke scatterplots på de store datasettene. Det er fordi det plottet ble oversiktig og lett leselig uten at vi måtte gjøre masse med datasettet på forhånd. Vi har brukt linjediagram for å vise den predikative analysen og statistiske verdier som gjennomsnitt og median. Det er igjen fordi vi syntes det ble mest oversiktig. Vi har også brukt histogram for å vise hvilke verdier som dukker opp flest ganger. Det gjorde at det var lettere å se nøyaktig hvilke verdier som dukket opp oftest.

Vi har brukt matplotlib og seaborn til å gi tilpassede akser, titler, og farger til grafene. Vi har valgt å gi norske aksenavn og titler. Det gjør lesligheten bedre for oss, men også de vi har tenkt på som målgruppen. Vi har henta norsk værdata fra metrologisk institutt, så det gir mening at målgruppa er norsk.

Datasettet inneholdt ikke manglende verdier. Når vi har brukt standardavvik til å fjerne noen verdier har ikke det vært mange nok til å gi et stort utslag på datasettet. Det er fordi vi har data med enten 2 eller 4 verdier per dag. Når en forsvinner, ville ikke det merkes tydelig. 

Vi har valgt visualiseringer etter tilbakemelding fra innleveringene av mappa underveis i prosessen. Vi kom fort frem til at scatter var den typen visualasjon som var mest effektiv til å vise frem de største datasettene. Linjediagram passet flott det er ikke var stor variasjon mellom dataene, for eksempel gjennomsnitt over tid. Histogram passet bra for å vise fordelingen av verdier. Vi har også vært nøye med å ta i bruk interaktive plot, men for det meste bruke vanlige statiske grafer. Det er fordi selv om interaktive grafer er kjekke, kan de fort føles litt rotete eller overveldende. Derfor har vi valgt ut noen vi har brukt interaktive grafer på og andre ikke.

#### Oppgave 7: Refleksjonsnotat
Vi har lagt refleksjonsnotatet i en egen fil under docs. 