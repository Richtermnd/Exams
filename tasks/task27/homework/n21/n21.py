import os


os.chdir('tasks/task27/homework/n21/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    mods = [float('inf')] * 1000  # минимальные остатки
    s = 0  # общая сумма
    res = -float('inf')  # максимальная сумма
    for _ in range(n):
        x = int(f.readline())
        s += x
        if s % 1000 == 0:
            res = max(res, s)
        
        res = max(res, s - mods[s % 1000])
        mods[s % 1000] = min(mods[s % 1000], s)
    
    assert res % 1000 == 0, res
    print(res)


solution('A')
solution('B')