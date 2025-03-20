Her gjøres oppgavene 
Oppgave 1:
Vi har laget utviklingsmiljø i github og delt mellom oss alle. Alle har laget sin egen .venv.

Oppgave 2:
Vi har hentet data fra Metrologisk institutt. Andre nettsider vi var inne på var norske klimaservicesenter og openweathermap.org. Vi valgte å bruke Metrologisk institutt, fordi de hadde en API vi synes var lett å finne ut av. Vi har også valgt de, fordi de er en pålitelig kilde. Metrologisk insitutt er statlig og er derfor lett å ha tillit og tilgang til de. Vi har alle laget vår egen bruker og fått vår egen client_ID. Disse har vi lagret i hver vår lokale ENV-fil. Det at metrologisk institutt bruker client_ID ser vi på en tegn at nettsida er trygg.
De har i tillegg mange store datasett, så det var lett å finne noe relevant. 

Vi har lastet ned dataen med bruk av API. API gjør at vi ikke trenger å manuelt endre datasettet ved endringer av innholdet. Derfor valgte vi dette istedenfor for eksempel å laste ned en statisk CSV-fil. Vi valgte å bruke Metrologisk Institutt sin egen kode for å laste ned datasettet. Dette gjorde det fort å komme igang, men gjør at vi har brukt en del tid på å tolke og tilpasse koden. 

Frost-datasettet inneholder masse forskjellige typer data. De mest aktuelle for oss er nedbør, temperatur og tidspunkt. Vi tenker vi kan bruke disse til å gjøre en grundig analyse av datasettet. Vi tenker vi kan regne ut gjennomsnitt, både for hver enkelt type data, men også finne noen sammen henger mellom de tre. Vi har også lyst til å se om vi kan finne fremtidige data ut ifra det vi allerede har.  