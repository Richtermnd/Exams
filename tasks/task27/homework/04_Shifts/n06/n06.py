import os


os.chdir('tasks/task27/homework/04_Shifts/n06')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    a = [int(x) for x in f]
    total = sum(a)
    
    s = 0
    for i, orders in enumerate(a):
        s += i * orders
    res = s

    expensive = 0
    for i in range(n - 1):
        expensive += a[i]
        s = s + expensive - (total - expensive)
        res = max(res, s)

    print(res)


solution('A')
solution('B')
