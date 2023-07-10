import os


os.chdir('tasks/task27/homework/03_SubSequence/n10')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = -float('inf')
    mods = [float('inf')] * 7
    q = []
    s = 0
    k = 0
    for _ in range(6):
        x = int(f.readline())
        s += x
        k += x % 7 == 0 and x > 0
        q.append([s, k])
    
    for _ in range(n - 6):
        x = int(f.readline())
        s += x
        k += x % 7 == 0 and x > 0
        if k % 7 == 0:
            res = max(res, s)
        
        res = max(res, s - mods[k % 7])
        
        _s, _k = q.pop(0)
        mods[_k % 7] = min(mods[_k % 7], _s)
        q.append([s, k])

    print(res)


solution('A')
solution('B')
