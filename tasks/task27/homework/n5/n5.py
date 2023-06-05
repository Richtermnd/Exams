import os


os.chdir('tasks/task27/homework/n5/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    m = 80
    b = 50_000
    mods_large = [0] * m
    mods_small = [0] * m
    res = 0
    for _ in range(n):
        x = int(f.readline())
        fill_mod = 0 if x % m == 0 else m - x % m

        if x > b:
            res += mods_small[fill_mod]
        res += mods_large[fill_mod]

        if x > b:
            mods_large[x % m] += 1
        else:
            mods_small[x % m] += 1

    print(res)


solution('A')
solution('B')