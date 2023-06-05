import os


os.chdir('tasks/task27/homework/n19/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    q = [int(f.readline()) for _ in range(6)]
    mods = [float('inf')] * 23
    res = float('inf')
    for _ in range(n - 6):
        x = int(f.readline())

        fill_mod = 0 if x % 23 == 0 else 23 - x % 23
        if (mods[fill_mod] * x) % 6 == 0:
            assert mods[fill_mod] * x % 6 == 0
            assert (mods[fill_mod] + x) % 23 == 0, (mods[fill_mod] + x) / 23
            res = min(res, mods[fill_mod] + x)

        mods[q[0] % 23] = min(mods[q[0] % 23], q[0])
        q.append(x)
        q.pop(0)

    print(res)


solution('A')
solution('B')



