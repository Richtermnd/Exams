import os


os.chdir('tasks/task27/homework/n_/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = []
    for _ in range(n):
        x = int(f.readline())
        a.append(x)
    res = ...
    print(res)


solution('A')
solution('B')