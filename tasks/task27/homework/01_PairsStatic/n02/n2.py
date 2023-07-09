import os
from math import comb


os.chdir('tasks/task27/homework/01_PairsStatic/n02/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = 0
    a7 = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 7:
            a += 1
        else:
            a7 += 1
    
    res = comb(a7, 2) + a7 * a
    print(res)


solution('A')
solution('B')