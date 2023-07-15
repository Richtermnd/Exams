import os
from math import ceil
from collections import namedtuple


os.chdir('tasks/task27/homework/04_Shifts/n05')


def solution(var):
    f = open(f'27{var}.txt')
    n, k, m = [int(x) for x in f.readline().split()]

    Point = namedtuple('Point', ['km', 'weight'])
    a: list[Point] = []
    for line in f:
        km, weight = [int(x) for x in line.split()]
        km %= k
        weight = ceil(weight / 9)
        a.append(Point(km, weight))
        a.append(Point(k + km, weight))
    a.sort()

    res = s = a[0].weight
    st, fn = 0, 0
    for cur in range(2 * n):
        while fn + 1 != 2 * n and a[fn + 1].km - a[cur].km <= m:
            fn += 1
            s += a[fn].weight
        while a[cur].km - a[st].km > m:
            s -= a[st].weight
            st += 1
        res = max(res, s)
    
    print(res)


solution('A')
solution('B')
