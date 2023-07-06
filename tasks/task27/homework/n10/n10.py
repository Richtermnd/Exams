import os


os.chdir('tasks/task27/homework/n10/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    max_even, max_odd = 0, 0
    for _ in range(n):
        x = int(f.readline())
        if x % 2:
            max_odd = max(max_odd, x)
        else:
            max_even = max(max_even, x)
    res = max_even + max_odd
    print(res)


solution('A')
solution('B')