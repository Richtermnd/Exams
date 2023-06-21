import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n7')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 1):
        s = a[i] + a[i + 1]
        m = a[i] * a[i + 1]

        if m > 0 and s % 7 == 0:
            res.append(m)

    print(len(res), min(res))

main()