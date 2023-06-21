import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n17')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    s = max(x for x in a if x % 10 == 4) + min(x for x in a if x % 10 == 4)

    for i in range(len(a) - 1):
        if sum(a[i:i + 2]) < s:
            res.append(sum(a[i:i + 2]))

    print(len(res), max(res))

main()