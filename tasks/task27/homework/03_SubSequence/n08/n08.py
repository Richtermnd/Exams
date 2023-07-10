import os


os.chdir('tasks/task27/homework/03_SubSequence/n08')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = -float('inf')
    s = 0
    k = 0
    mods = [float('inf')] * 30
    for _ in range(n):
        x = int(f.readline())
        s += x
        k += x > 0 and x % 2 == 0
        if k % 30 == 0:
            res = max(res, s)
        
        _s = s - mods[k % 30]
        res = max(res, _s)

        mods[k % 30] = min(mods[k % 30], s)
    print(res)


solution('A')
solution('B')
