import os


os.chdir('tasks/task27/homework/03_SubSequence/n07')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res_s = float('inf')
    res_l = -float('inf')
    mods = [-float('inf')] * 2077
    lengths = [-float('inf')] * 2077
    s = 0
    for i in range(n):
        x = int(f.readline())
        s += x
        # Последовательность от нуля до i.
        if s % 2077 == 0:
            if s < res_s or s == res_s and i + 1 > res_l:
                res_s = s
                res_l = i + 1
        
        # Усеченная подпоследовательность.
        _s = s - mods[s % 2077]
        _l = i + 1 - lengths[s % 2077]
        if _s < res_s or _s == res_s and _l > res_l:
            res_s = _s
            res_l = _l
        
        # обновляем статистику.
        if s > mods[s % 2077]:
            mods[s % 2077] = s
            lengths[s % 2077] = i + 1
        
    print(res_l)


solution('A')
solution('B')
