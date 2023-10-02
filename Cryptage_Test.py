import unittest
from Cryptage import *

class Cryptage_Test(unittest.TestCase):
    
    def test_crypt(self):
        self.assertEqual(Cryptage("Fizz"), "GjAA")
        self.assertEqual(Cryptage("Qiyana"), "GjhRzR")
        self.assertEqual(Cryptage("Fizz est sur lol"), "aftuatvsampmGjAA")




if __name__ == '__main__':
    unittest.main()