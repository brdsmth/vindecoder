import unittest
# from package.src import start
from package.src import config
import start


class myTests(unittest.TestCase):

	def setup(self):
		self.number = 1

	def test1(self):

		self.assertIsInstance(AWS.rdsconn(), object)

		# continue

	def test2(self):

		self.assertIsEqual(config.test, 'testing')



if __name__ == '__main__':
    unittest.main()
