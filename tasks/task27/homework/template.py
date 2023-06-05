import os


os.chdir('tasks/task27/homework/n_/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    c = 0
    res = 0
    for _ in range(n):
        x = int(f.readline())

        c += 1
    
    print(res)


solution('A')
solution('B')