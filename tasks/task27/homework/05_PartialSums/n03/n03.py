import os


os.chdir('tasks/task27/homework/05_PartialSums/n03')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    res = [0]
    for _ in range(n):
        line = [int(x) for x in f.readline().split()]
        res = [a + b for a in line for b in res]
        res = {x % 5: x for x in sorted(res, reverse=True)}.values()
    print(min(x for x in res if x % 5 != 0))


solution('A')
solution('B')
