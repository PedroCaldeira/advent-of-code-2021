def get_or(values):
    if values[0] == '':
        return ''
    if len(values) == 1:
        return values[0]

    zeros, ones = 0, 0
    bits = [v[0] for v in values]
    for bit in bits:
        if bit == '0':
            zeros += 1
        elif bit == '1':
            ones += 1
    if zeros > ones:
        return '0' + get_or([v[1:] for v in values if v[0] == '0'])
    elif ones > zeros:
        return '1' + get_or([v[1:] for v in values if v[0] == '1'])
    else:
        return '1' + get_or([v[1:] for v in values if v[0] == '1'])


def get_co2r(values):
    if values[0] == '':
        return ''
    if len(values) == 1:
        return values[0]

    zeros, ones = 0, 0
    bits = [v[0] for v in values]
    for bit in bits:
        if bit == '0':
            zeros += 1
        elif bit == '1':
            ones += 1
    if zeros > ones:
        return '1' + get_co2r([v[1:] for v in values if v[0] == '1'])
    elif ones > zeros:
        return '0' + get_co2r([v[1:] for v in values if v[0] == '0'])
    else:
        return '0' + get_co2r([v[1:] for v in values if v[0] == '0'])


def solutionP1(bit_numbers):
    gr = ['0'] * len(bit_numbers[0])
    for idx, bits_at_idx in enumerate(zip(*bit_numbers)):
        zeros, ones = 0, 0

        for bit in bits_at_idx:
            if bit == '0':
                zeros += 1
            elif bit == '1':
                ones += 1

        if ones > zeros:
            gr[idx] = '1'

    er = ['0' if v == '1' else '1' for v in gr]
    gr_val = int(''.join(gr), 2)
    er_val = int(''.join(er), 2)

    return gr_val * er_val


def solutionP2(bit_numbers):
    return int(get_co2r(bit_numbers), 2) * int(get_or(bit_numbers), 2)
