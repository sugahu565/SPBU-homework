from itertools import permutations


def check_valid(p):
    # проверка для каждой пары ферзей, не бьют ли они друг друга
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            # проверка по диагоналям
            if i - j == p[i] - p[j] or i + p[i] == j + p[j]:
                return 0
    return 1


def queen(n):
    answer = 0
    # индекс в перестановке отвечает за номер строки, значение за номер колонки
    for i in permutations(range(n)):
        answer += check_valid(i)
    return answer
