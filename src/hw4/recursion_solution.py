def check_bit(a, b):
    return (1 << a) & b == 0


def queen(n, i = 0, ban_sum_diag = 0, ban_diff_diag = 0, ban_column = 0):
    '''
    i - отвечает за то, в какой строке хотим поместить ферзя
    если у ферзей одинаковые столбец-строка, то они на одной диагонали
    если у ферхей одинаковые столбец+строка, то они на одной диагонали
    ban_sum_diag - если сумма какого-то ферзя равна m, то m бит равен 1
    ban_diff_diag - если разность какого-то ферзя равна m, m + (n - 1) бит равен 1
    ban_column - если занята m колонка, то m бит равен 1
    '''
    k = 0
    for j in range(n):
        # проверка на зянятость диагоналей, столбца
        if check_bit(i + j, ban_sum_diag) and check_bit(i - j + (n - 1), ban_diff_diag) and check_bit(j, ban_column):
            if i == n - 1:
                k += 1
            else:
                new_ban_sum = ban_sum_diag | (1 << i + j)
                new_ban_diff = ban_diff_diag | (1 << (i - j + (n - 1)))
                new_ban_column = ban_column | (1 << j)
                k += queen(n, i + 1, new_ban_sum, new_ban_diff, new_ban_column)
    return k
