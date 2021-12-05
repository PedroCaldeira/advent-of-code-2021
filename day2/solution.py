p1_commands = {
    'forward': lambda val, sub: {'hp': sub['hp'] + val,
                                 'depth': sub['depth']},
    'down': lambda val, sub: {'hp': sub['hp'],
                              'depth': sub['depth'] + val},
    'up': lambda val, sub: {'hp': sub['hp'],
                            'depth': sub['depth'] - val}
}

p2_commands = {
    'forward': lambda val, sub: {'hp': sub['hp'] + val,
                                 'depth': sub['depth'] + sub['aim'] * val,
                                 'aim': sub['aim']},
    'down': lambda val, sub: {'hp': sub['hp'],
                              'depth': sub['depth'],
                              'aim': sub['aim'] + val},
    'up': lambda val, sub: {'hp': sub['hp'],
                            'depth': sub['depth'],
                            'aim': sub['aim'] - val}
}


def solution(given_cmds, commands):
    sub = {"hp": 0, "depth": 0, "aim": 0}
    for cmd, val in given_cmds:
        sub = commands[cmd](int(val), sub)
    return sub['hp'] * sub['depth']


def solutionP1(given_cmds):
    return solution(given_cmds, p1_commands)


def solutionP2(given_cmds):
    return solution(given_cmds, p2_commands)
