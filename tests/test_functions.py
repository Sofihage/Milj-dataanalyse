import unittest
import sys, os
import pandas as pd
import numpy as np
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))


import functions as fc

data = {
  "verdi": [-4.9, -3.8, 10.4, 6.3, 6.9],
  "tidsforskyvning": ['PT0H', 'PT6H', 'PT18H', 'PT6H', 'PT0H'],
  "referansetid": ['2024-01-01T00:00:00.000Z', '2024-01-01T00:00:00.000Z', '2024-01-01T00:00:00.000Z', '2024-01-01T00:00:00.000Z', '2024-01-01T00:00:00.000Z']
}


class test_functions(unittest.TestCase):

    def test_make_datetime(self):
      fc.make_datetime(data)
      dt = np.dtype('datetime64')
      self.assertEqual(dt.name, 'datetime64')


    def test_label(self):
      fc.label(data)
      self.assertEqual(data['tidsforskyvning'][0], 0)


suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_functions))

unittest.TextTestRunner().run(suite)