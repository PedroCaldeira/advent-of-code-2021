import unittest
from util import readInput
from solution import solutionP1, solutionP2


class TestSolution(unittest.TestCase):

    testInput = readInput(f'./day0.example.txt')

    def testP1(self):
        self.assertEqual(solutionP1(self.testInput), None)

    def testP2(self):
        self.assertEqual(solutionP2(self.testInput), None)


if __name__ == '__main__':
    unittest.main()
