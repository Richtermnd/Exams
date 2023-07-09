import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n11/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = 0

    k = [0] * 10
    for i in range(6, n):
        k[a[i - 6] % 10] += 1
        
        mod = a[i] % 10
        if mod == 1:
            res += k[3]
        elif mod == 3:
            res += k[1]
        elif mod == 7:
            res += k[9]
        elif mod == 9:
            res += k[7]
        
    print(res)


solution('A')
solution('B')