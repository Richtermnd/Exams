import re
import time


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start)
        return res
    
    return inner


@timer
def re_solution():
    mask = '1234\d*7'
    min_number = 12347  # Минимально возможное число, удовлетворяющее маске
    div = 141  # Делитель из задачи

    closest = (12347 // 141 + 1) * 141 if min_number % div else min_number
    res = []
    for i in range(closest, 10 ** 8, div):
        if re.fullmatch(mask, str(i)):
            res.append((i, i // div))
    return res


@timer
def slice_solution():
    min_number = 12347  # Минимально возможное число, удовлетворяющее маске
    div = 141  # Делитель из задачи

    closest = (12347 // 141 + 1) * 141 if min_number % div else min_number
    res = []
    for i in range(closest, 10 ** 8, div):
        s = str(i)
        if s[:4] == '1234' and s[-1] == '7':
            res.append((i, i // div))
    return res


re_res = re_solution()
slice_res = slice_solution()
print(re_res)
print(slice_res)