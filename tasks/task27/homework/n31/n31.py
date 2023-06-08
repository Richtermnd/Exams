import os


os.chdir('tasks/task27/homework/n31/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n, m = [int(x) for x in f.readline().split()]

    a = []  # массив размером n, в котором хранится кол-во еды для каждого пункта
    for _ in range(n):
        a.append(int(f.readline()))
    
    res = s = sum(a[:2 * m + 1])
    for i in range(2 * m + 1, n - m):
        s += a[i]
        s -= a[i - 2 * m - 1]

        res = max(res, s)

    print(res)


solution('A')
solution('B')