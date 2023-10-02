import unittest
from FizzBuzz import *

class Test_FizzBuzz(unittest.TestCase):

    def setUp(self):
        self.instance=FizzBuzz()

    def test_affiche_sans_param(self):
        with self.subTest(self):
            self.assertEqual(self.instance.affiche(100), "fizzIsLol")
        with self.subTest(self):
            self.assertEqual(self.instance.affiche(5), "fizzlol")
        with self.subTest(self):
            self.assertEqual(self.instance.affiche(3), "fizz")

if __name__ == '__main__':
    unittest.main()