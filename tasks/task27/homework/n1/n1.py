import os
from math import comb

os.chdir('tasks/task27/homework/n1/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    odd = 0  # нечетные
    even = 0  # четные
    for _ in range(n):
        x = int(f.readline())
        if x % 2:
            odd += 1
        else:
            even += 1
    res = comb(odd, 2) + comb(even, 2)  # comb работает, confirmed.
    print(res)


solution('A')
solution('B')
