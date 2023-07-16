import os


os.chdir('tasks/task27/homework/05_PartialSums/n05')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    res = []
    for _ in range(n):
        x = int(f.readline())
        res = res + [a + x for a in res] + [x]
        res = list({x % 17: x for x in sorted(res)}.values())

    print(max(x for x in res if x % 17 == 0))


solution('A')
solution('B')
