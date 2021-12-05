import unittest
from util import readInput
from solution import solutionP1, solutionP2


class TestSolution(unittest.TestCase):

    test_input = readInput('./day2.example.txt')

    def testP1(self):
        self.assertEqual(solutionP1(self.test_input), 150)

    def testP2(self):
        self.assertEqual(solutionP2(self.test_input), 900)


if __name__ == '__main__':
    unittest.main()
