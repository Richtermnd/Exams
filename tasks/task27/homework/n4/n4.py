import os


os.chdir('tasks/task27/homework/n4/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    mods = [0] * 131
    res = 0
    for _ in range(n):
        x = int(f.readline())
        fill_mod = 0 if x % 131 == 0 else 131 - x % 131
        res += mods[fill_mod]

        mods[x % 131] += 1
    
    print(res)


solution('A')
solution('B')