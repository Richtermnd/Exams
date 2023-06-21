import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n5')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for x in a:
        cond1 = x % 16 == 11
        cond2 = x % 7 == 0 and x % 6 != 0 and x % 13 != 0 and x % 19 != 0
        if cond1 and cond2:
            res.append(x)

    print(sum(res), len(res))


main()