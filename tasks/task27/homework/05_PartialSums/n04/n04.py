import os
from itertools import combinations


os.chdir('tasks/task27/homework/05_PartialSums/n04')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    res = [0]
    for _ in range(n):
        line = [int(x) for x in f.readline().split()]
        line = [sum(pair) for pair in combinations(line, 2)]
        res = [a + b for a in line for b in res]
        res = {x % 4: x for x in sorted(res)}.values()
    print(max(x for x in res if x % 4 == 0))


solution('A')
solution('B')
