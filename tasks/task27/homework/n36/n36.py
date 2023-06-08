import os


os.chdir('tasks/task27/homework/n36/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())

    a = [int(f.readline()) for _ in range(n)]  # массив размером n, в котором хранится кол-во единиц для каждого пункта

    res = ...

    # print(res)


solution('A')
solution('B')