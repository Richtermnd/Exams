import os


os.chdir('tasks/task27/homework/03_SubSequence/n02')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    mods = [0] * 666
    s = 0
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
