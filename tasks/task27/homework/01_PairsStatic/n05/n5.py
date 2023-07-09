import os
from math import comb


os.chdir('tasks/task27/homework/01_PairsStatic/n05/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 19 == 0:
            res += 1
    print(comb(res, 3))


solution('A')
solution('B')