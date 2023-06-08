import os


os.chdir('tasks/task27/homework/n22/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    mods = [0] * 666
    s = 0
    res = 0  # счётчик кол-ва последовательностей
    for _ in range(n):
        x = int(f.readline())
        s += x
        if s % 666 == 0:
            res += 1
        
        res += mods[s % 666]

        mods[s % 666] += 1
    
    print(res)


solution('A')
solution('B')