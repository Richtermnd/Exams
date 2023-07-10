import os


os.chdir('tasks/task27/homework/03_SubSequence/n09')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = 0
    mods = [0] * 117
    s1 = sum(a[:5])
    s2 = 0
    for i in range(5, n):
        s2 += a[i - 5]
        mods[s2 % 117] += 1
        
        s1 += a[i]
        if s1 % 117 == 0:
            res += 1
        
        res += mods[s1 % 117]
        # mods[s1 % 117] += 1
    
    print(res)


solution('A')
solution('B')
