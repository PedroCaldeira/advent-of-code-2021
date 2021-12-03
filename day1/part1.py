
def solution(depths):
    nr_increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            nr_increases += 1
    return nr_increases


def main():
    #  Example
    with open('./day1.example.txt') as f:
        example_input = f.read().splitlines()
    print("Example Solution: ", solution(example_input))
    values = [int(n) for n in example_input]
    assert(solution(example_input) == 7)

    #  Solution
    with open('./day1.txt') as f:
        chall_input = f.read().splitlines()
    values = [int(n) for n in chall_input]
    print("Solution: ", solution(values))


if __name__ == "__main__":
    main()
