def bubble_sort(args):
    swap = 1
    while swap:
        swap = 0
        for i in range(1, len(args)):
            if args[i - 1] > args[i]:
                args[i - 1], args[i] = args[i], args[i - 1]
                swap = 1
