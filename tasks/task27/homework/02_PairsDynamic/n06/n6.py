import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n06/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    max_odd, max_even = 0, 0
    for _ in range(n):
        x = int(f.readline())
        if x % 2 == 0:
            max_even = max(max_even, x)
        else:
            max_odd = max(max_odd, x)
    
    res = max_even + max_odd
    print(res)


solution('A')
solution('B')