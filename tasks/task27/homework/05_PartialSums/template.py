import os


os.chdir('tasks/task27/homework/05_PartialSums/n_')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    res = []
    for _ in range(n):
        line = [int(x) for x in f.readline().split()]
        res = [a + b for a in line for b in res]
        res = {x % ...: x for x in sorted(res)}
    print(max(x for x in res if ...))


solution('A')
solution('B')
