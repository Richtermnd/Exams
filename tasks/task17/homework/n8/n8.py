import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n8')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 2):
        s = a[i] + a[i + 1] + a[i + 2]
        m = a[i] * a[i + 1] * a[i + 2]
        if m % 7 == 0 and abs(s) % 10 == 5:
            res.append(s)

    print(len(res), max(res))

main()