import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n2')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for x in a:
        cond1 = x % 10 in (2, 7)  # Фестиваль проклятых решений
        cond2 = x % 3 == x % 11 == 0
        if cond1 and cond2:
            res.append(x)

    print(len(res), min(res))


main()