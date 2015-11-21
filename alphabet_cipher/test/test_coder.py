from coder import coder
import unittest

class TestCoder(unittest.TestCase):

	def test_encode(self):
		'''Can encode given a secret keyword'''
		c = coder.Coder()
		self.assertEqual("egsgqwtahuiljgs", c.encode("scones", "meetmebythetree"))
		self.assertEqual("hmkbxebpxpmyllyrxiiqtoltfgzzv", c.encode("vigilance", "meetmeontuesdayeveningatseven"))

	def test_decode(self):
		'''Can decode a crypted message given a secret keyword'''
		c = coder.Coder()
		self.assertEqual("meetmebythetree", c.decode("scones", "egsgqwtahuiljgs"))
		self.assertEqual("meetmeontuesdayeveningatseven", c.decode("vigilance", "hmkbxebpxpmyllyrxiiqtoltfgzzv"))

	def test_decipher(self):
		'''Can extract the secret keyword given an encrypted message and the original message'''
		self.assertEqual("scones", c.decipher("hcqxqqtqljmlzhwiivgbsapaiwcenmyu", "packmyboxwithfivedozenliquorjugs"))
		self.assertEqual("vigilance", c.decode("opkyfipmfmwcvqoklyhxywgeecpvhelzg", "thequickbrownfoxjumpsoveralazydog"))


if __name__ == '__main__':
	unittest.main()
