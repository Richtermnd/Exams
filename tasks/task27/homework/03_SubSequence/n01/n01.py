import os


os.chdir('tasks/task27/homework/03_SubSequence/n01')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    mods = [float('inf')] * 1000
    s = 0
    for _ in range(n):
        x = int(f.readline())
        s += x
        if s % 1000 == 0:
            res = s
        
        res = max(res, s - mods[s % 1000])
        mods[s % 1000] = min(mods[s % 1000], s)

    print(res)


solution('A')
solution('B')
