import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n16/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = 0
    k = [0] * 100
    for x in a:
        fill = 112 - x % 100 if x % 100 > 12 else 12 - x % 100  # Гений?
        if k[fill] > x:
            res = max(res, x + k[fill])

        k[x % 100] = max(k[x % 100], x)
    
    print(res)


solution('A')
solution('B')