import os


os.chdir('tasks/task27/homework/n16/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline()) 
    mods = [0] * 100
    res = 0
    for _ in range(n):
        x = int(f.readline())
        mod = 12 - x % 100 if x % 100 <= 12 else 112 - x % 100
        if mods[mod] > x:
            res = max(res, mods[mod] + x)
        
        mods[x % 100] = max(mods[x % 100], x)
    print(res)

solution('A')
solution('B')