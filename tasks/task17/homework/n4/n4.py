import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n4')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for x in a:
        cond1 = x % 13 == 7
        cond2 = x % 7 != 0 and x % 11 != 0
        if cond1 and cond2:
            res.append(x)

    print(max(res) - min(res), len(res))


main()