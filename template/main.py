from util import readInput
from solution import solutionP1, solutionP2


def main():

    #  get input file
    taskInput = readInput(f'./day0.txt')

    # get solutions
    print("Part 1 output:", solutionP1(taskInput))
    print("Part 2 output:", solutionP2(taskInput))


if __name__ == "__main__":
    main()
