import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n15/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = 0
    max_mods = [-float('inf')] * 137
    min_mods = [float('inf')] * 137
    for i in range(5, n):
        mod = a[i] % 137
        if max_mods[mod] != -float('inf'):
            res = max(res, abs(max_mods[mod] - a[i]))
        if min_mods[mod] != float('inf'):
            res = max(res, abs(min_mods[mod] - a[i]))

        mod = a[i - 5] % 137
        max_mods[mod] = max(max_mods[mod], a[i - 5])
        min_mods[mod] = min(min_mods[mod], a[i - 5])

    print(res)


solution('A')
solution('B')