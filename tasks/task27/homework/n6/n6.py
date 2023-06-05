import os


os.chdir('tasks/task27/homework/n6/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    max_odd = -float('inf')
    max_even = -float('inf')
    res = -float('inf')
    for _ in range(n):
        x = int(f.readline())
        if x % 2:
            res = max(res, x + max_even)
        else:
            res = max(res, x + max_odd)

        if x % 2:
            max_odd = max(max_odd, x)
        else:
            max_even = max(max_even, x)
        
    print(res)


solution('A')
solution('B')