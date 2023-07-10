import os


os.chdir('tasks/task27/homework/03_SubSequence/n05')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = float('inf')
    mods = [0] * n
    s = 0
    k = 0
    for _ in range(n):
        x = int(f.readline())
        s += x
        k += x % 3 == 0
        if k == 10:
            res = min(res, s)
        if k >= 10:
            res = min(res, s - mods[k - 10])
            mods[k] = max(mods[k], s)

    
    print(res)


solution('A')
solution('B')
