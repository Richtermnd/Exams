import os


os.chdir('tasks/task27/homework/05_PartialSums/n01')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    res = [0]
    for _ in range(n):
        line = [int(x) for x in f.readline().split()]
        res = [a + b for a in res for b in line]
        res = {x % 3: x for x in sorted(res)}.values()

    print(max(x for x in res if x % 3 != 0))


solution('A')
solution('B')
