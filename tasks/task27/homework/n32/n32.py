import os


os.chdir('tasks/task27/homework/n32/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n, m = [int(x) for x in f.readline().split()]

    a = [int(f.readline()) for _ in range(n)]  # массив размером n, в котором хранится кол-во едениц для каждого пункта
    
    res = s = sum(a[:2 * m + 1])
    for i in range(2 * m + 1, 2 * n - m):
        
        s += a[i % n]  # прибавляем следующий
        s -= a[(i - 2 * m - 1) % n]  # вычитаем последний

        res = max(res, s)

    print(res)


solution('A')
solution('B')