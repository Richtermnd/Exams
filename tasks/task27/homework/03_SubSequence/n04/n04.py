import os


os.chdir('tasks/task27/homework/03_SubSequence/n04')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    mods = [float('inf')] * 3
    k = 0
    s = 0
    for _ in range(n):
        x = int(f.readline())
        k += x % 5 == 0
        s += x
        if k % 3 == 0:
            res = s
        
        res = max(res, s - mods[k % 3])
        mods[k % 3] = min(mods[k % 3], s)
    
    print(res)


solution('A')
solution('B')
