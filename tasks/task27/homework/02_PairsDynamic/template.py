import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n_/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    for _ in range(n):
        x = int(f.readline())
    
    print(res)


solution('A')
solution('B')
