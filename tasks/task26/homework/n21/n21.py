import os


os.chdir('d:/ЕГЭ/tasks/task26/homework/n21/')


def main():
    f = open('26.txt')
    n = int(f.readline())
    a = [int(f.readline()) for _ in range(n)]

    res = set(a)
    print(len(res), max(map(a.count, res)))


main()
