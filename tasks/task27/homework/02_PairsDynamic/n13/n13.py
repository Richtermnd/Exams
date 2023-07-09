import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n13/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = 0

    mods = [[0] * 13, [0] * 13]
    for i in range(6, n):
        x = a[i - 6]
        mods[x % 2][x % 13] += 1

        x = a[i]
        res += mods[0][x % 13]
        if x % 2 == 0:
            res += mods[1][x % 13]        
    
    print(res)


solution('A')
solution('B')