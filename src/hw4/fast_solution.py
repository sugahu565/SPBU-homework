from recursion_solution import queen


def pre_calculation(n):
    answer = {
        1: 1,
        2: 0,
        3: 0,
        4: 2,
        5: 10,
        6: 4,
        7: 40,
        8: 92,
        9: 352,
        10: 724,
        11: 2680,
        12: 14200,
        13: 73712,
        14: 365596,
        15: 2279184
    }
    if n < 16:
        return answer[n]
    else:
        return queen(n)

