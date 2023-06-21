import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n3')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for x in a:
        cond1 = x % 10 in (5, 7)
        cond2 = x % 9 != 0 and x % 11 != 0
        if cond1 and cond2:
            res.append(x)

    print(len(res), max(res) + min(res))


main()