import os


os.chdir('tasks/task27/homework/03_SubSequence/n03')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    res = 0
    mods = [0] * 11
    k = 0
    for _ in range(n):
        x = int(f.readline())
        k += x % 5 == 0
        if k % 11 == 0:
            res += 1
        
        res += mods[k % 11]
        mods[k % 11] += 1
    
    print(res)


solution('A')
solution('B')
