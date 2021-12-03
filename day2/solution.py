p1_commands = {
    'forward': lambda value, sub: {'hp': sub['hp'] + value,
                                   'depth': sub['depth']},
    'down': lambda value, sub: {'hp': sub['hp'],
                                'depth': sub['depth'] + value},
    'up': lambda value, sub: {'hp': sub['hp'],
                              'depth': sub['depth'] - value}
}

p2_commands = {
    'forward': lambda value, sub: {'hp': sub['hp'] + value,
                                   'depth': sub['depth'] + sub['aim'] * value,
                                   'aim': sub['aim']},

    'down': lambda value, sub: {'hp': sub['hp'],
                                'depth': sub['depth'],
                                'aim': sub['aim'] + value},

    'up': lambda value, sub: {'hp': sub['hp'],
                              'depth': sub['depth'],
                              'aim': sub['aim'] - value}
}


def solution(given_cmds, commands):
    sub = {"hp": 0, "depth": 0, "aim": 0}
    for cmd, val in given_cmds:
        sub = commands[cmd](int(val), sub)
    return sub['hp'] * sub['depth']


def parse_input(lines):
    return [line.split() for line in lines]


def main():
    with open('./day2.example.txt') as f:
        example_input = parse_input(f.read().splitlines())
    with open('./day2.txt') as f:
        chall_input = parse_input(f.read().splitlines())

    p1_ex_output = solution(example_input, p1_commands)
    assert(p1_ex_output == 150)

    p2_ex_output = solution(example_input, p2_commands)
    assert(p2_ex_output == 900)

    print("Part 1 output: ", solution(chall_input, p1_commands))
    print("Part 2 output: ", solution(chall_input, p2_commands))


if __name__ == "__main__":
    main()
