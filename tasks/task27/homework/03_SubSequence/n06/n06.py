import os


os.chdir('tasks/task27/homework/03_SubSequence/n06')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res_s = 0
    res_l = 0
    mods = [float('inf')] * 69
    lengths = [0] * 69
    s = 0
    l = 0
    for _ in range(n):
        x = int(f.readline())
        s += x
        l += 1
        if s % 69 == 0:
            if s > res_s or s == res_s and l + 1 < res_l:
                res_s = s
                res_l = l + 1
        
        mod = s % 69
        _s = s - mods[mod]
        _l = l - lengths[mod]
        if _s > res_s or _s == res_s and _l < res_l:
            res_s = _s
            res_l = _l
        
        if mods[s % 69] > s:
            mods[s % 69] = s
            lengths[s % 69] = l
    print(res_l)


solution('A')
solution('B')
