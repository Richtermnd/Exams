import os
from collections import defaultdict


os.chdir('tasks/task27/homework/n17/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = defaultdict(int)
    for _ in range(n):
        x = f.readline().strip()
        res[x[0]] += 1
    
    print(min(res.values()))

solution('A')
solution('B')