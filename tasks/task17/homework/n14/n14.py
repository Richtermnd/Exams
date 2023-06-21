import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n14')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    avg = sum(a) / len(a)

    for i in range(len(a) - 2):
        if sum(x > avg for x in a[i:i + 3]) >= 2:
            res.append(sum(a[i:i + 3]))

    print(len(res), max(res))

main()