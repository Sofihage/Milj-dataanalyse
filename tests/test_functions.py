import sys, os
src_path_2 = '..\\venv\\Lib\\site-packages'
if src_path_2 not in sys.path:
    sys.path.insert(0, src_path_2)

import unittest
import pandas as pd
import numpy as np
import datetime
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))


import functions as fc

data = {
  "verdi": [-4.9, -3.8, 10.4, 6.3, 6.9],
  "tidsforskyvning": ['PT0H', 'PT6H', 'PT18H', 'PT6H', 'PT0H'],
  "referansetid": ['2024-01-01T00:00:00.000Z', 
                  '2024-01-01T00:00:00.000Z', 
                  '2024-01-01T00:00:00.000Z', 
                  '2024-01-01T00:00:00.000Z', 
                  '2024-01-01T00:00:00.000Z']
}

data = pd.DataFrame(data)

class test_functions(unittest.TestCase):


    def test_make_datetime(self):
      fc.make_datetime(data)
      dt = np.dtype('datetime64')
      self.assertEqual(dt.name, 'datetime64')


    def test_make_datetime_invalid(self):
      with self.assertRaises(TypeError):
        fc.make_datetime('Hello')


    def test_label(self):
      fc.label(data)
      self.assertEqual(data['tidsforskyvning'][0], 0)


    def test_median(self):
      median = fc.median(data)
      self.assertEqual(median, 6.3)


    def test_median_invalid(self):
      with self.assertRaises(TypeError):
        fc.median(0)


    def test_average_year(self):
      mean = fc.average_year(data)
      self.assertEqual(mean, 2.98)


    def test_average_year_invalid(self):
      with self.assertRaises(TypeError):
        fc.average_year(0)


    def test_average_other(self):
      average = fc.average_other(data, 'tidsforskyvning')
      expected= pd.Series({0: 1, 1: 10.4, 2: 1.25}, name='verdi')
      expected.index.name = "tidsforskyvning"
      pd.testing.assert_series_equal(average, expected)


    def test_std(self):
      std = fc.std(data)
      self.assertEqual(round(std, 2), 6.16)


    def test_train_test_set(self):
      X_train, X_test, y_train, y_test = fc.train_test_set(data, 0.2)
      self.assertEqual(len(X_train), 4)
      self.assertEqual(len(y_train), 4)
      self.assertEqual(len(X_test), 1)
      self.assertEqual(len(y_test), 1)

   
    def test_linear(self):
      X_train, X_test, y_train, y_test = fc.train_test_set(data, 0.2)
      lin=fc.linear(X_train, y_train)
      regr = linear_model.LinearRegression()
      regr.fit(X_train, y_train)
      expected = regr.predict(X_train)
      np.testing.assert_array_equal(lin, expected)

    
    def test_linear_invalid(self):
      with self.assertRaises(TypeError):
        fc.linear('test')

      
    def test_poly(self):
      X_train, X_test, y_train, y_test = fc.train_test_set(data, 0.2)
      poly=fc.poly(X_train, y_train)
      poly_ = PolynomialFeatures(degree=2, include_bias=False)
      poly_features = poly_.fit_transform(X_train)
      poly_reg = linear_model.LinearRegression()
      poly_reg.fit(poly_features, y_train)
      expected = poly_reg.predict(poly_features)
      np.testing.assert_array_equal(poly, expected)

    def test_poly_invalid(self):
      with self.assertRaises(TypeError):
        fc.poly('test')


suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_functions))

unittest.TextTestRunner().run(suite)