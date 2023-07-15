import os


os.chdir('tasks/task27/homework/04_Shifts/n01')


def solution(var):
    f = open(f'27{var}.txt')
    n, m = [int(x) for x in f.readline().split()]
    a = [int(x) for x in f]
    res = 0
    s = sum(a[:2 * m + 1])
    for i in range(m + 1, n - m):
        s -= a[i - m - 1]
        s += a[i + m]
        res = max(res, s)

    print(res)


solution('A')
solution('B')
