import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n02/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    # 65 = 5 * 13
    k, k5, k13, k65 = 0, 0, 0, 0
    res = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 65 == 0:
            res += k
        elif x % 13 == 0:
            res += k5
        elif x % 5 == 0:
            res += k13
        else:
            res += k65
        
        k += 1
        k5 += x % 5 == 0
        k13 += x % 13 == 0
        k65 += x % 65 == 0
    print(res)


solution('A')
solution('B')