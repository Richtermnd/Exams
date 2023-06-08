import os


os.chdir('tasks/task27/homework/n26/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    min_sums = [float('inf')] * 69
    lengths = [float('inf')] * 69
    cur_len = 0  # длина текущей последовательности
    s = 0
    res_len = float('inf')
    res = -float('inf')
    for _ in range(n):
        x = int(f.readline())
        s += x
        cur_len += 1
        if s % 69 == 0:
            bigger_sum = s > res
            lesser_len = s == res and cur_len < res_len
            if bigger_sum or lesser_len:
                res = s
                res_len = cur_len
        
        temp_sum = s - min_sums[s % 69]
        temp_len = cur_len - lengths[s % 69]
        
        bigger_sum = temp_sum > res
        lesser_len = temp_sum == res and temp_len < res_len
        if bigger_sum or lesser_len:
            res = temp_sum
            res_len = temp_len
        
        temp = [min_sums[s % 69], lengths[s % 69]]
        min_sums[s % 69], lengths[s % 69] = min(temp, [s, cur_len], key=lambda x: (x[0], -x[1]))
        
    print(res_len)


solution('A')
solution('B')