import unittest
from util import readInput
from solution import solutionP1, solutionP2


class TestSolution(unittest.TestCase):

    testInput = readInput('./day1.example.txt')

    def testP1(self):
        self.assertEqual(solutionP1(self.testInput), 7)

    def testP2(self):
        self.assertEqual(solutionP2(self.testInput), 5)


if __name__ == '__main__':
    unittest.main()
