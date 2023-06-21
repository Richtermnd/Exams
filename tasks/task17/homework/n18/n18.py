import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n18')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 1):
        x, y = a[i:i + 2]
        if x % 9 == 0:
            if y % 9 != 0 and abs(y % 8) == 3:
                res.append(max(x, y))
        elif y % 9 == 0:
            if x % 9 != 0 and abs(x % 8) == 3:
                res.append(max(x, y))

    print(len(res), max(res))

main()