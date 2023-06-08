import os


os.chdir('tasks/task27/homework/n25/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    max_seq = [-float('inf')] * n
    cnt = 0  # счётчик особых чисел
    s = 0
    res = float('inf')
    for _ in range(n):
        x = int(f.readline())
        s += x
        if x % 3 == 0:
            cnt += 1
        
        if cnt == 10:
            res = min(res, s)

        if cnt >= 10:
            res = min(res, s - max_seq[cnt - 10])
        
        max_seq[cnt] = max(max_seq[cnt], s)


    print(res)


solution('A')
solution('B')