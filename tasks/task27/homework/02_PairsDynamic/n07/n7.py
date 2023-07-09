import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n07/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = float('inf')
    k, k31 = float('inf'), float('inf')
    for _ in range(n):
        x = int(f.readline())
        if x % 31 == 0:
            res = min(res, k * x)
        else:
            res = min(res, k31 * x)
        
        k = min(k, x)
        if x % 31 == 0:
            k31 = min(k31, x)

    print(res)


solution('A')
solution('B')