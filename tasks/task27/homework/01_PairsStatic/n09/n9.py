import os


os.chdir('tasks/task27/homework/01_PairsStatic/n09/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [0] * 2001
    for _ in range(n):
        x = int(f.readline())
        if x > 2000:
            continue
        a[x] += 1
    
    res = a[1000] * (a[1000] - 1) // 2  # Частный случай.
    for i in range(1000):  # 0 и 2000 будет.
        res += a[i] * a[2000 - i]
    print(res)


def brutforce(var):
    """ Меня напугала еденица в ответе. """
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(f.readline()) for _ in range(n)]

    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == 2000:
                res += 1
    print(res)


brutforce('A')
solution('A')
solution('B')
