from coder import coder
import unittest

class TestCoder(unittest.TestCase):

	def test_encode(self):
		'''can encode given a secret keyword'''
		c = coder.Coder()
		self.assertEqual("egsgqwtahuiljgs", c.encode("scones", "meetmebythetree"))
		self.assertEqual("hmkbxebpxpmyllyrxiiqtoltfgzzv", c.encode("vigilance", "meetmeontuesdayeveningatseven"))

if __name__ == '__main__':
	unittest.main()
