from itertools import permutations


def check_valid(p):
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if i - j == p[i] - p[j] or i + p[i] == j + p[j]:
                return 0
    return 1


def queen(n):
    answer = 0
    # индекс в перестановке отвечает за номер строки, значение за номер колонки
    for i in permutations(range(n)):
        answer += check_valid(i)
    return answer


n = int(input())
print(queen(n))
