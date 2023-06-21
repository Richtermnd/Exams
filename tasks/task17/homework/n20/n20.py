import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n20')


def main():
    a = [int(x) for x in open('17.txt')]
    res = []

    s = sum(sum(int(c) for c in str(x)) for x in a if x % 35 == 0)

    for i in range(len(a) - 1):
        x, y = a[i:i + 2]
        cond1 = x > s and y <= s and hex(y)[-2:] == 'ef'
        cond2 =  y > s and x <= s and hex(x)[-2:] == 'ef'
        if cond1 or cond2:
            res.append(x + y)

    print(len(res), min(res))


main()