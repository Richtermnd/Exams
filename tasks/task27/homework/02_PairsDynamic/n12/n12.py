import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n12/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    mods = [0] * 8
    res = 0
    for i in range(1, n):
        mods[a[i - 1] % 8] += 1

        if i > 7:
            mods[a[i - 7 - 1] % 8] -= 1
        
        mod = 0 if a[i] % 8 == 0 else 8 - a[i] % 8
        res += sum(mods[i] for i in range(8) if i != mod)
    print(res)


solution('A')
solution('B')