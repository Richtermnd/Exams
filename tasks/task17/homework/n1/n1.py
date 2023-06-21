import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n1')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for x in a:
        cond1 = x % 3 == 0
        cond2 = x % 7 != 0 and x % 17 != 0 and x % 19 != 0 and x % 27 != 0
        if cond1 and cond2:
            res.append(x)

    print(len(res), max(res))

main()