import os


os.chdir('tasks/task27/homework/n23/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    s = 0
    counts = [0] * 11
    count = 0 # кол-во чисел делющихся на 5
    res = 0  # кол-во
    for _ in range(n):
        x = int(f.readline())
        s += x
        if x % 5 == 0:
            count += 1
        
        if count % 11 == 0:
            res += 1
        
        res += counts[count % 11]

        counts[count % 11] += 1
    
    print(res)


solution('A')
solution('B')