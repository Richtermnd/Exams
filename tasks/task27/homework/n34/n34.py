import os


os.chdir('tasks/task27/homework/n34/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n, v, m = [int(x) for x in f.readline().split()]

    a = []
    for _ in range(n):
        # dist - удалённость, c - кол-во контейнеров
        dist, c = [int(x) for x in f.readline().split()]
        c = c // v if c % v == 0 else c // v + 1  # отдельный контейнер под остатки

        a.append([dist, c])
    a.sort()  # т.к удалённость уникальная, то сортировка происходит по ней

    start, finish = 0, 0
    # Сдвигаем правый крайний пункт, чтобы найти пункт на расстоянии максимальном не превышающим m
    # Тем самым a[finish] находится на оптимальном удаление от самого первого дома
    while a[finish - 1][0] - a[start][0] <= m:  
        finish += 1
    res = s = sum([elem[1] for elem in a[start:finish]])

    # используем finish как точку старта, чтобы убрать лишние
    for cur in range(finish, n):
        # Сдвигаю крайний правый пункт до тех пор, пока расстояние валидное
        while finish + 1 < n and a[finish + 1][0] - a[cur][0] <= m:
            finish += 1
            s += a[finish][1]
        
        # Как только расстояние становится больше дозволенного
        # Начинаю срезать левую грань, чтобы компенсировать
        while a[cur][0] - a[start][0] > m:
            s -= a[start][1]
            start += 1

        # после всех этих махинаций находится максимальное кол-во пунктов для a[cur]
        res = max(res, s)
    
    print(res)


solution('A')
solution('B')