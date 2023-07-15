import os
from math import ceil


os.chdir('tasks/task27/homework/04_Shifts/n10')


def min_dist(p1, p2, n):
    """ Минимальное расстояние на кольцевой дороге. """
    return min(abs(p1 - p2), n - abs(p1 - p2))



def solution(var):
    f = open(f'27{var}.txt')
    n, k, v = [int(x) for x in f.readline().split()]
    a = [0] * k
    total = 0
    for line in f:
        km, weight = [int(x) for x in line.split()]
        total += ceil(weight / v)
        a[km % k] = ceil(weight / v)

    s = 0
    for i in range(k):
        s += min(i, k - i) * a[i]
    res = s

    cheaper = sum(a[1:k // 2 + 1])
    expensive = total - cheaper
    for i in range(1, k):
        s = s - cheaper + expensive
        if a[i]:
            res = min(res, s)
        cheaper = cheaper - a[i] + a[(k // 2 + i) % k]
        expensive = total - cheaper
    
    print(res)


solution('A')
solution('B')
