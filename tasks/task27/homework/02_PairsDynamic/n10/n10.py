import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n10/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = 0
    k, k13 = [0, 0], [0, 0]
    for i in range(5, n):
        k[a[i - 5] % 2] += 1
        k13[a[i - 5] % 2] += a[i - 5] % 13 == 0

        if a[i] % 13 == 0:
            res += k[not a[i] % 2]
        else:
            res += k13[not a[i] % 2]
    
    print(res)


solution('A')
solution('B')