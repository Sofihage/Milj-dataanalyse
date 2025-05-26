### functions
Her har vi lagt inn alle funksjonene vi bruker felles. 

##### make_datetime
Her gjøres 'referansetid' i et valgt datasett om til datetime. Dette gjøres for å lettere bruke referansetid i utregninger og som akser i grafer. Der er også mulig å skrive inn egen kolonne som skal gjøres om til datetime. Det er ment for når 'referansetid' heter 'referencetime'

##### label
Her gis valgt kolonne en integer label. Om brukeren ikke velger kolonne selv, er det 'tidsforskyvning' som får label.

##### median
Her brukes np.median til å finne medianen til 'verdi'-kolonna i et valgt datasett. 

##### average_year
Her brukes np.mean til å finne gjennomsnittet til 'verdi'-kolonna i et valgt datasett.

##### average_other
Her brukes np.mean til å finne gjennomsnittet til 'verdi'-kolonna i et valgt datasett, der gjennomsnittet blir sortert etter en annen kolonne. Hvis brukeren ikke skriver inn en egen kolonne blir det regnet ut gjennomsnittet for hver måned.

##### std
Her brukes np.std til å finne standardavviket til 'verdi'-kolonna i et valgt datasett.

##### lower_upper_limit
Finner øvre og nedre grense i et datasett med hjelp av standardavvik og gjennomsnitt.

##### missing_numbers
Her telles antall verdier i hver kolonne i et valgt datasett som er None eller NaN. Det visualiseres også hvor mange verdier hver kolonne har. Så printes de linjene som inneholder None eller NaN i en valgt kolonne. Om brukeren ikke velger kolonne selv, vises linjene med None eller NaN som verdi.

##### train_test_set
Her deles et valgt datasett inn i train og test. Brukeren velger selv test-størrelsen. X er satt til å være 'referansetid' og y er 'verdi'.

##### linear 
Her brukes sklearn til å lage en lineær regresjon med train-dataen som lages i funksjonen ovenfor.

##### poly
Her brukes sklearn til å lage en andregrads polynom regresjon med train-dataen som lages i funksjonen ovenfor.