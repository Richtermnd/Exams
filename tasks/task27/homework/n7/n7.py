import os


os.chdir('tasks/task27/homework/n7/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    min_c = float('inf')
    min_c31 = float('inf')
    res = float('inf')
    for _ in range(n):
        x = int(f.readline())
        if x % 31 == 0:
            res = min(res, x * min_c)
        else:
            res = min(res, x * min_c31)
        
        min_c = min(min_c, x)
        if x % 31 == 0:
            min_c31 = min(min_c31, x)
    
    print(res)


solution('A')
solution('B')