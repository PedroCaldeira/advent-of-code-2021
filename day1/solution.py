

def solution(depths, window_size):
    result = 0
    for i in range(window_size, len(depths)):
        previous = sum(depths[i - window_size:i])
        current = sum(depths[i + 1 - window_size:i + 1])
        if current > previous:
            result += 1
    return result


def main():

    #  get input files
    with open('./day1.example.txt') as example_f:
        example_input = [int(n) for n in example_f.read().splitlines()]
    with open('./day1.txt') as f:
        chall_input = [int(n) for n in f.read().splitlines()]

    #  run examples
    p1_example_out = solution(example_input, 1)
    p2_example_out = solution(example_input, 3)
    #  assert examples correctness
    assert(p1_example_out == 7)
    assert(p2_example_out == 5)

    #  get values
    p1_chall_out = solution(chall_input, 1)
    p2_chall_out = solution(chall_input, 3)

    print("Part 1 output: ", p1_chall_out)
    print("Part 2 output: ", p2_chall_out)


if __name__ == "__main__":
    main()
