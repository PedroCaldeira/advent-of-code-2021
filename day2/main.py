from util import readInput
from solution import solutionP1, solutionP2


def main():

    task_input = readInput('./day2.txt')

    print("Part 1 output:", solutionP1(task_input))
    print("Part 2 output:", solutionP2(task_input))


if __name__ == "__main__":
    main()
