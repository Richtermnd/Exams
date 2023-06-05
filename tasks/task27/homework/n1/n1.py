import os


os.chdir('tasks/task27/homework/n1/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    c = 0
    c7 = 0
    res = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 7 == 0:
            res += c
        else:
            res += c7

        c += 1
        c7 += x % 7 == 0
    
    print(res)


solution('A')
solution('B')