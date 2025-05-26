### test_functions
Her har vi gjennomført enhetstester på alle funksjonene som ligger i functions.py fila i src.

Vi har brukt assertEqual og lagt inn resultatet fra funksjonen vi tester og det vi forventer å få ut. 
Vi har også i et tilfelle brukt pd.testing.assert_series_equal. Det er testen for 'average_other'-funksjona. Det er brukt fordi resulatet har vært en pandas series.
Vi har også brukt np.testing.assert_array_equal. Det er testene for 'linear' og 'poly' funksjonene. Det er fordi resultatet har vært en numpy array.

Vi har også gjennomført noen negative tester. Vi har ikke gjort det på alle, fordi mesteparten tar inn det samme argumentet: et datasett. Vi brukte self.assertRaises(TypeError) for å teste at funksjonene ikke fungerer når et datasett ikke blit lagt inn.