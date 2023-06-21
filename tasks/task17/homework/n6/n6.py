import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n6')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 1):
        x, y = a[i], a[i + 1]
        if (x + y) % 3 == 0 and (x + y) % 6 != 0 and abs(x * y) % 10 == 8:
            res.append(x + y)
        
    print(len(res), max(res))


main()