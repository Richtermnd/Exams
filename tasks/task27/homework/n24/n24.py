import os


os.chdir('tasks/task27/homework/n24/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    s = 0
    min_sums = [float('inf')] * 3
    count = 0 # кол-во чисел делющихся на 5
    res = -float('inf')  # максимальная сумма
    for _ in range(n):
        x = int(f.readline())
        s += x
        if x % 5 == 0:
            count += 1
        
        if count % 3 == 0:
            res = max(res, s)
        
        res = max(res, s - min_sums[count % 3])

        min_sums[count % 3] = min(min_sums[count % 3], s)
    
    print(res)


solution('A')
solution('B')