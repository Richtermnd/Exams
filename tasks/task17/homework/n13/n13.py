import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n13')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 1):
        if 50 <= sum(abs(x) for x in a[i:i + 2]) <= 200:
            res.append(min(a[i:i + 2]))

    print(len(res), min(res))


main()