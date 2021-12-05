def readInput(filename):
    with open(filename) as f:
        return [int(n) for n in f.read().splitlines()]
