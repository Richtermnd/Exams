import os
from functools import reduce


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n11')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 3):
        cond1 = a[i] > a[i + 1] > a[i + 2] > a[i + 3]
        cond2 = a[i] - a[i + 3] > 1000
        if cond1 and cond2:
            res.append(sum(a[i:i + 4]))
            
    print(len(res), min(res))

main()