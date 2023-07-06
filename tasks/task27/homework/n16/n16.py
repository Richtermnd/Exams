import os
from collections import defaultdict


os.chdir('tasks/task27/homework/n16/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = defaultdict(int)
    for _ in range(n):
        x = f.readline().strip()
        res[sum(int(c) for c in x)] += 1
    print(max(res.values()))


solution('A')
solution('B')