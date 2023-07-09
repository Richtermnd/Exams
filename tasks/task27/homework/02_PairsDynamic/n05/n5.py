import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n05/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    k = [[0] * 80, [0] * 80]
    for _ in range(n):
        x = int(f.readline())
        mod = 0 if x % 80 == 0 else 80 - x % 80
        res += k[not x > 50_000][mod]

        k[0][x % 80] += 1
        k[1][x % 80] += x > 50_000
    
    print(res)


solution('A')
solution('B')