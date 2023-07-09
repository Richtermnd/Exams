import os
from math import comb


os.chdir('tasks/task27/homework/01_PairsStatic/n20/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    ox = 0
    oy = 0
    xd = 0
    for _ in range(n):
        x, y = [int(elem) for elem in f.readline().split()]
        if x == 0:
            oy += 1
        elif y == 0:
            ox += 1
        else:
            xd += 1
        
    res = ox * oy * xd
    print(res)


solution('A')
solution('B')