import os
from itertools import groupby


os.chdir('d:/ЕГЭ/tasks/task26/homework/n24/')


def main():
    f = open('26.txt')
    n = int(f.readline())
    a = [tuple(int(x) for x in f.readline().split()) for _ in range(n)]
    key = lambda x: x[0]
    a.sort(key=key)

    latest_year = [0, 0]
    cnt = 0
    for year, marks in groupby(a, key=key):  # groupby supremacy
        marks = set(marks)
        cnt += 8 - len(marks)
        latest_year = max(latest_year, [8 - len(marks), year])

    print(cnt, latest_year[1])


main()
