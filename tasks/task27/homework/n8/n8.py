import os


os.chdir('tasks/task27/homework/n8/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    
    max_c = [-float('inf'), -float('inf')]
    max_c23 = [-float('inf'), -float('inf')]
    res = -float('inf')

    for _ in range(n):
        x = int(f.readline())
        if x % 23 == 0:
            a = x + max_c[x % 2]
            b = x + max_c23[x % 2]
            res = max(res, a, b)
        else:
            temp = x + max_c23[x % 2]
            res = max(res, temp)
        
        max_c[x % 2] = max(max_c[x % 2], x)
        if x % 23 == 0:
            max_c23[x % 2] = max(max_c23[x % 2], x)
    
    print(res)


solution('A')
solution('B')