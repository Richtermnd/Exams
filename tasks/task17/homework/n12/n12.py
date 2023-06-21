import os
from math import prod


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n12')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 1):
        cond1 = any(x < 0 for x in a[i:i + 2])
        cond2 = sum(a[i:i + 2]) >= 100
        if cond1 and cond2:
            res.append(prod(a[i:i + 2]))

    print(len(res), max(res))


main()