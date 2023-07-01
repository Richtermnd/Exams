import re
import time
from fnmatch import fnmatch


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - start)
        print(res)
        return res
    
    return inner


@timer
def re_solution():
    mask = '123\d*567\d'
    min_number = 123567  # Минимально возможное число, удовлетворяющее маске
    div = 169  # Делитель из задачи

    closest = (min_number // div + 1) * div if min_number % div else min_number
    res = []
    for i in range(closest, 10 ** 9 + 1, div):
        if re.fullmatch(mask, str(i)):
            res.append((i, i // div))
    return res


@timer
def slice_solution():
    min_number = 123567  # Минимально возможное число, удовлетворяющее маске
    div = 169  # Делитель из задачи

    closest = (min_number // div + 1) * div if min_number % div else min_number
    res = []
    for i in range(closest, 10 ** 9 + 1, div):
        s = str(i)
        if s[:3] == '123' and s[-4:-1] == '567':
            res.append((i, i // div))
    return res


@timer
def fnmatch_solution():
    mask = '123*567?'
    min_number = 123567  # Минимально возможное число, удовлетворяющее маске
    div = 169  # Делитель из задачи

    closest = (min_number // div + 1) * div if min_number % div else min_number
    res = []
    for i in range(closest, 10 ** 9 + 1, div):
        if fnmatch(str(i), mask):
            res.append((i, i // div))
    return res


re_res = re_solution()
# [print(*elem) for elem in re_res]
slice_res = slice_solution()
# [print(*elem) for elem in slice_res]
fnmatch_res = fnmatch_solution()
# [print(*elem) for elem in fnmatch_res]
