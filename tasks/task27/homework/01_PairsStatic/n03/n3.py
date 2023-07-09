import os
from math import comb


os.chdir('tasks/task27/homework/01_PairsStatic/n03/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = 0
    a5 = 0
    a13 = 0
    a65 = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 65 == 0:
            a65 += 1
        elif x % 13 == 0:
            a13 += 1
        elif x % 5 == 0:
            a5 += 1
        else:
            a += 1
    res = comb(a65, 2) + a65 * (n - a65) + a13 * a5
    print(res)


solution('A')
solution('B')