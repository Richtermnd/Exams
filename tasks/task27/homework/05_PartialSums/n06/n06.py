import os


os.chdir('tasks/task27/homework/05_PartialSums/n06')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    res = [0] * 10
    for _ in range(n):
        x = int(f.readline())
        temp = res[:]
        for i in range(10):
            temp[(i + x) % 10] += res[i]
        temp[x % 10] += 1
        res = temp
    print(res[5])


solution('A')
solution('B')
