import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n08/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    k = [0, 0]
    k23 = [0, 0]
    for _ in range(n):
        x = int(f.readline())
        if x % 23 == 0:
            res = max(res, k[x % 2] + x)
        else:
            res = max(res, k23[x % 2] + x)
        
        k[x % 2] = max(k[x % 2], x)
        if x % 23 == 0:
            k23[x % 2] = max(k23[x % 2], x)
        
    print(res)


solution('A')
solution('B')