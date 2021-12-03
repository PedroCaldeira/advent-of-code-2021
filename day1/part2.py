
def solution(depths, window_size):
    result = 0
    for i in range(window_size, len(depths)):
        previous = sum(depths[i - window_size:i])
        current = sum(depths[i + 1 - window_size:i + 1])
        if current > previous:
            result += 1
    return result


def main():
    with open('./day1.example.txt') as example_f:
        example_input = [int(n) for n in example_f.read().splitlines()]
    with open('./day1.txt') as f:
        chall_input = [int(n) for n in f.read().splitlines()]

    # Verify Examples
    p1_example_solution = solution(example_input, 1)
    p2_example_solution = solution(example_input, 3)
    assert(p1_example_solution == 7)
    assert(p2_example_solution == 5)

    p1_chall_solution = solution(chall_input, 1)
    p2_chall_solution = solution(chall_input, 3)

    print("Part 1 Solution: ", p1_chall_solution)
    print("Part 2 Solution: ", p2_chall_solution)


if __name__ == "__main__":
    main()
