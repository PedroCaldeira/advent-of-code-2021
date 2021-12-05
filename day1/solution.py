def solution(depths, windowSize, aggrFunc):
    #  keep count of increments
    increments = 0

    #  iterate from start of second window so we can compare with previous
    for start in range(1, len(depths) - windowSize + 1):
        #  calculate end of window
        end = start + windowSize

        #  apply aggregating function to prev and current window
        previous = aggrFunc(depths[start-1:end-1])
        current = aggrFunc(depths[start:end])

        #  increment increments if there's an increment AHAH
        if current > previous:
            increments += 1

    return increments


def solutionP1(depths):
    return solution(depths, 1, sum)


def solutionP2(depths):
    return solution(depths, 3, sum)
