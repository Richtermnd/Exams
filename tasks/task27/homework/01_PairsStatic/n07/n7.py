import os
from math import comb


os.chdir('tasks/task27/homework/01_PairsStatic/n07/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [0] * 69
    for _ in range(n):
        x = int(f.readline())
        a[x % 69] += 1
    
    res = sum(comb(x, 2) for x in a)
    print(res)


solution('A')
solution('B')