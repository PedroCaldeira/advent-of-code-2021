from util import readInput
from solution import solutionP1, solutionP2


def main():

    #  get input file
    task_input = readInput(f'./day3.txt')

    # get solutions
    print("Part 1 output:", solutionP1(task_input))
    print("Part 2 output:", solutionP2(task_input))


if __name__ == "__main__":
    main()
