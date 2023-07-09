import os


os.chdir('tasks/task27/homework/01_PairsStatic/n_/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    for _ in range(n):
        x = int(f.readline())
        
    res = ...
    print(res)


solution('A')
solution('B')