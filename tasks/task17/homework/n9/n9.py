import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n9')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 2):
        cond1 = any(x % 12 == 0 for x in a[i:i + 3])
        cond2 = all(x % 3 == 0 for x in a[i:i + 3])
        if cond1 and cond2:
            res.append(sum(a[i:i + 3]) / 3)

    print(len(res), min(res))

main()