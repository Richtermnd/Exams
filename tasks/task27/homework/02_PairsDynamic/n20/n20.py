import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n20')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = float('inf')
    mods = [[float('inf')] * 107 for _ in range(5)]
    for i, x in enumerate(a):
        row = i % 5
        mod = (107 - x % 107) % 107
        res = min(res, mods[row][mod] + x)

        mods[row][x % 107] = min(mods[row][x % 107], x)
    
    print(res)


solution('A')
solution('B')