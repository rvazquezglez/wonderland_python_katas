import unittest
from doublets.code.doublets import DoubletSolver
from doublets.test import words


class DoubletsTester(unittest.TestCase):
    def test_doublet(self):
        ds = DoubletSolver(words.dictionary)  # Replace for list of words (dictionary)

        self.assertEqual(["head", "heal", "teal", "tell", "tall", "tail"], ds.get_doublet("head", "tail"))
        self.assertEqual(["door", "boor", "book", "look", "lock"], ds.get_doublet("door", "lock"))
        self.assertEqual(["bank", "bonk", "book", "look", "loon", "loan"], ds.get_doublet("bank", "loan"))
        self.assertEqual(["bank", "bonk", "book", "look", "loon", "loan"], ds.get_doublet("bank", "loan"))
        self.assertEqual(["wheat", "cheat", "cheap", "cheep", "creep" "creed" "breed" "bread"],
                         ds.get_doublet("wheat", "bread"))

        self.assertEqual([], ds.get_doublet("ye", "freezer"))
