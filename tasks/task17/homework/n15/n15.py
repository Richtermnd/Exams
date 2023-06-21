import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n15')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    mx = max(x for x in a if x % 19 == 0)

    for i in range(len(a) - 1):
        if any(x > mx for x in a[i:i + 2]):
            res.append(sum(a[i:i + 2]))

    print(len(res), min(res))

main()