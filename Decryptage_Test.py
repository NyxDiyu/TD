import unittest
from Decryptage import *

class Decryptage_Test(unittest.TestCase):


        def test_decrypt(self):
            self.assertEqual(Decryptage("GjAA"), "Fizz")
            self.assertEqual(Decryptage("GjhRzR"), "Qiyana")
            self.assertEqual(Decryptage("aftuatvsampmGjAA"), "Fizz est sur lol")


if __name__ == '__main__':
    unittest.main()