import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n04/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    mods = [0] * 131
    res = 0
    for _ in range(n):
        x = int(f.readline())
        mod = 0 if x % 131 == 0 else 131 - x % 131
        res += mods[mod]

        mods[x % 131] += 1
    
    print(res)


solution('A')
solution('B')