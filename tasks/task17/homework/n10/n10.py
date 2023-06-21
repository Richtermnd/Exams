import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n10')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 2):
        if any(x % 3 == 2 for x in a[i:i + 3]):
            res.append(min(a[i:i + 3]))

    print(len(res), sum(res))


main()