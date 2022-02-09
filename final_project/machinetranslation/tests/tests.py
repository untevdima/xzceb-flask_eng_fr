import unittest
from  translator import french_to_english, english_to_french

class TestEngToFr (unittest.TestCase):
    def test_engtofr(self):
        self.assertEqual(english_to_french('Null'),'Null')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        

class TestFrToEng (unittest.TestCase):
    def test_frToEng(self):
        self.assertEqual(french_to_english('Null'),'Null')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        

if __name__ == "__main__":
   unittest.main()     