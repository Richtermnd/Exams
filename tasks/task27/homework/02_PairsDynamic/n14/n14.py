import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n14/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    mods = [float('inf')] * 144
    res = float('inf')
    for x in a:
        mod = 0 if x % 144 == 0 else 144 - x % 144
        if mods[mod] < x:
            res = min(res, mods[mod] + x)
        
        mods[x % 144] = min(mods[x % 144], x)
    
    print(res)


solution('A')
solution('B')