import os
from math import ceil


os.chdir('tasks/task27/homework/04_Shifts/n08')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    a = []
    total = 0
    for line in f:
        km, weight = [int(x) for x in line.split()]
        total += ceil(weight / 36)
        a.append((km, ceil(weight / 36)))
    
    s = 0
    storage = a[0]
    for place in a:
        s += abs(place[0] - storage[0]) * place[1]
    res = s

    expensive = 0
    for i in range(1, n):
        r = a[i][0] - a[i - 1][0]
        expensive += a[i - 1][1]
        s = s + r * expensive - r * (total - expensive)
        res = min(res, s)
    print(res)


solution('A')
solution('B')
