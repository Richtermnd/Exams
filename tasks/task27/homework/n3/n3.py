import os


os.chdir('tasks/task27/homework/n3/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    c_odd = 0
    c_even = 0
    c5_odd = 0
    c5_even = 0
    res = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 5 == 0:
            if x % 2:
                res += c_even
            else:
                res += c_odd
        else:
            res += c5_even if x % 2 else c5_odd
        
        c_odd += x % 2
        c_even += not x % 2
        c5_odd += x % 2 and x % 5 == 0
        c5_even += x % 2 == 0 and x % 5 == 0
    
    print(res)


solution('A')
solution('B')