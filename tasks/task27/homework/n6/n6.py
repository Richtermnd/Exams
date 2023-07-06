import os


os.chdir('tasks/task27/homework/n6/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    mods = [0] * 131
    for _ in range(n):
        x = int(f.readline())
        mods[x % 131] += 1

    # +----------------------------------------------+
    # | У нечетного числа один частный случай - нули |
    # +----------------------------------------------+

    res = mods[0] * (mods[0] - 1) // 2
    for i in range(1, 131 // 2 + 1):
        res += mods[i] * mods[131 - i]
    print(res)


def static_solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(f.readline()) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 131 == 0:
                res += 1
    print(res)

static_solution('A')
solution('A')
solution('B')