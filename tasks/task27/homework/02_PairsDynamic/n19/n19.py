import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n19/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = float('inf')
    k = [float('inf')] * 23
    k2 = [float('inf')] * 23
    k3 = [float('inf')] * 23
    k6 = [float('inf')] * 23
    for i in range(7, n):
        x = a[i - 7]
        k[x % 23] += min(k[x % 23], x)
        if x % 2 == 0:
            k2[x % 23] = min(k2[x % 23], x)
        if x % 3 == 0:
            k3[x % 23] = min(k3[x % 23], x)
        if x % 6 == 0:
            k6[x % 23] = min(k6[x % 23], x)

        mod = (23 - x % 23) % 23
        if x % 6 == 0:
            res = min(res, x + k[mod])
        elif x % 3 == 0:
            res = min(res, x + k2[mod])
        elif x % 2 == 0:
            res = min(res, x + k3[mod])
        else:
            res = min(res, x + k6[mod])
    
    print(res)


solution('A')
solution('B')