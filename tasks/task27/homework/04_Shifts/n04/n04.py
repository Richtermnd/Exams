import os
from math import ceil
from collections import namedtuple


os.chdir('tasks/task27/homework/04_Shifts/n04')


def solution(var):
    f = open(f'27{var}.txt')
    n, v, m = [int(x) for x in f.readline().split()]
    
    Point = namedtuple('Point', ['km', 'weight'])
    a: list[Point] = []
    for line in f:
        km, weight = [int(x) for x in line.split()]
        a.append(Point(km, ceil(weight / v)))
    a.sort()

    st, fn = 0, 0
    res = s = a[0].weight
    for curr in range(n):
        while fn + 1 != n and a[fn + 1].km - a[curr].km <= m:
            fn += 1
            s += a[fn].weight
        while a[curr].km - a[st].km > m:
            s -= a[st].weight
            st += 1
        res = max(res, s)
    print(res)


solution('A')
solution('B')
