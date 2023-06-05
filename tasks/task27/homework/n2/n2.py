import os


os.chdir('tasks/task27/homework/n2/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    c = 0
    c5, c13, c65 = 0, 0, 0
    res = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 65 == 0:
            res += c
        elif x % 13 == 0:
            res += c5
        elif x % 5 == 0:
            res += c13
        else:
            res += c65

        c += 1
        c5 += x % 5 == 0
        c13 += x % 13 == 0
        c65 += x % 65 == 0
    
    print(res)


solution('A')
solution('B')