import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n03/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    k, k5 = [0, 0], [0, 0]
    for _ in range(n):
        x = int(f.readline())
        if x % 5 == 0:
            res += k[not x % 2]
        else:
            res += k5[not x % 2]
        
        k[x % 2] += 1
        k5[x % 2] += x % 5 == 0
    print(res)


solution('A')
solution('B')