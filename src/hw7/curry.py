def __curry(function, length_arg, args):
    if length_arg < len(args):
        raise Exception("too many arguments")
    if length_arg == len(args):
        try:
            return function(*args)
        except:
            raise Exception("invalid arguments or invalid number of arguments")

    def next_function(x):
        return __curry(function, length_arg, args + [x])

    return next_function


def curry(function, lenght_arg):
    if lenght_arg < 0:
        raise Exception("invalid lenght of arguments")
    return __curry(function, lenght_arg, [])


def uncurry(function, lenght_arg):
    def need_function(*args):
        curr_arg = args[0]
        now_function = function
        for x in args:
            now_function = now_function(x)
        return now_function
    return need_function

