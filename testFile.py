import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join('.')))

from pythonFile import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
      self.calc = Calculator();

    def test_add(self):
      self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add(self):
      self.assertEqual(self.calc.sub(1, 2), -1)
    
    def test_add(self):
      self.assertEqual(self.calc.mul(1, 2), 2)
    
    def test_add(self):
      self.assertEqual(self.calc.div(1, 2), 1/2)


if __name__ == '__main__':
    unittest.main()
