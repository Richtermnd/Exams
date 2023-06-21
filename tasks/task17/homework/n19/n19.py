import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n19')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    for i in range(len(a) - 2):
        x, y, z = a[i: i + 3]
        x = x > 0 and x % 10 == 9
        y = y > 0 and y % 10 == 9
        z = z > 0 and z % 10 == 9
        
        if not x and y and not z:
            res.append(sum(a[i: i + 3]))

    print(len(res), max(res))

main()