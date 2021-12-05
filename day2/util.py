def readInput(filename):
    with open(filename) as f:
        return [line.split() for line in f]
