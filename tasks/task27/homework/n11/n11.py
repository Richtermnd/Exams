import os


os.chdir('tasks/task27/homework/n11/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    min_a = float('inf')
    min_a31 = float('inf')
    for _ in range(n):
        x = int(f.readline())
        if x % 31 == 0:
            min_a31 = min(min_a31, x)
        else:
            min_a = min(min_a, x)
    
    res = min(min_a31 * min_a31, min_a31 * min_a)
    print(res)


solution('A')
solution('B')