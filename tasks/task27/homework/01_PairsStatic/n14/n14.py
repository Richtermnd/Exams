import os
from itertools import combinations


os.chdir('tasks/task27/homework/01_PairsStatic/n14/')


def solution(var):
    """Анализ

    12: * * 3 4
    12: * 2 2 3

    """
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    m = [[] for _ in range(12)]
    for _ in range(n):
        x = int(f.readline())
        m[x % 12].append(x)

    a = []
    for i in range(12):
        m[i].sort()
        a.extend(m[i][-4:])
    
    ans = []
    for x, y, w, z in combinations(a, 4):
        if x * y * w * z % 12 == 0:
            ans.append(x + y + z + w)
    print(max(ans))
    

solution('A')
solution('B')