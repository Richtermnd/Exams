import os
from math import ceil


os.chdir('tasks/task27/homework/04_Shifts/n09')


def min_dist(p1, p2, n):
    """ Минимальное расстояние на кольцевой дороге. """
    return min(abs(p1 - p2), n - abs(p1 - p2))


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    a = [int(x) for x in f]
    total = sum(a)
    
    # Сумма для 0 пункта.
    s = 0
    for i in range(n):
        s += a[i] * min_dist(i, 0, n)
    
    res_sum = s
    res_index = 1
    
    cheaper = sum(a[1:n // 2 + 1])
    expensive = total - cheaper

    for i in range(1, n):
        s = s + expensive - cheaper
        if s < res_sum:
            res_sum = s
            res_index = i + 1
        
        cheaper -= a[i]
        cheaper += a[(n // 2 + i) % n]
        expensive = total - cheaper
        
    print(res_index)

solution('A')
solution('B')
