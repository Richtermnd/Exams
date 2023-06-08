import os


os.chdir('tasks/task27/homework/n27/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    pairs = [[-float('inf'), float('inf')] for _ in range(2077)]
    s = 0
    cur_len = 0
    res = [float('inf'), -float('inf')]
    for _ in range(n):
        x = int(f.readline())
        s += x
        cur_len += 1

        if s % 2077 == 0:
            pair = [s ,cur_len]
            res = min(res, pair, key=lambda x: (x[0], -x[1]))
        
        diff_sum, diff_len = pairs[s % 2077]
        pair = [s - diff_sum, cur_len - diff_len]
        res = min(res, pair, key=lambda x: (x[0], -x[1]))

        pair = [s, cur_len]
        pairs[s % 2077] = max(pairs[s % 2077], pair, key=lambda x: (x[0], -x[1]))
    
    print(res[1])


def static_solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    data = [int(f.readline()) for _ in range(n)]
    res_sum = float('inf')
    res_len = -float('inf')
    for i in range(n):
        for j in range(i, n):
            l = j - i
            s = sum(data[i:j])
            if s < res_sum or s == res_sum and l > res_len:
                res_len = l
                res_sum = s
    print(res_len)


solution('A')
static_solution('A')
solution('B')