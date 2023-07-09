import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n09/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0

    a = [int(x) for x in f]
    k, k23 = 0, 0
    for i in range(9, n):
        k += 1
        k23 += a[i - 9] % 23 == 0

        if a[i] % 23 == 0:
            res += k
        else:
            res += k23

    print(res)


solution('A')
solution('B')