import os
from math import dist
from itertools import combinations


os.chdir('tasks/task27/homework/01_PairsStatic/n19/')

def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    ox = []
    h = 0
    for _ in range(n):
        x, y = [int(elem) for elem in f.readline().split()]
        if y == 0:
            ox.append(x)
        else:
            h = max(h, abs(y))
    
    base = max(abs(p1 - p2) for p1, p2 in combinations(ox, 2)) 
    # print(base, h)
    res =  base * h // 2
    print(res)


solution('A')
solution('B')