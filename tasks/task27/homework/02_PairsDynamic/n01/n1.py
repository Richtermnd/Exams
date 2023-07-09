import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n01/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    k, k7 = 0, 0
    res = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 7 == 0:
            res += k
        else:
            res += k7

        k += 1
        k7 += x % 7 == 0
    
    print(res)


solution('A')
solution('B')