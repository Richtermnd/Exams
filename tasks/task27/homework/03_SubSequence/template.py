import os


os.chdir('tasks/task27/homework/03_SubSequence/n_')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    s = 0
    for _ in range(n):
        x = int(f.readline())
        s += x

    
    print(res)


solution('A')
solution('B')
