def rise_elem(arr, ind):
    parent_ind = (ind - 1) // 2
    while ind > 0 and arr[ind] > arr[parent_ind]:
        arr[ind], arr[parent_ind] = arr[parent_ind], arr[ind]
        ind = parent_ind
        parent_ind = (parent_ind - 1) // 2


def fall_elem(arr, len_arr, ind=0):
    swap = 1
    l_child = ind * 2 + 1
    r_child = l_child + 1
    while swap and l_child < len_arr:
        swap = 0

        j = l_child
        if r_child < len_arr and arr[r_child] > arr[l_child]:
            j = r_child

        if arr[j] > arr[ind]:
            arr[j], arr[ind] = arr[ind], arr[j]
            swap = 1
            ind = j
        l_child = ind * 2 + 1
        r_child = l_child + 1


def heap_sort(arr):
    for i in range(1, len(arr)):
        rise_elem(arr, i)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        fall_elem(arr, i)
